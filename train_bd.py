import torch
import torchvision
import numpy as np
import argparse
from model import resnet18, resnet34
from dataset import dataset_init
from utils import test
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

parser = argparse.ArgumentParser(description='Train backdoored networks')

# Basic parameters.
parser.add_argument('--arch', type=str, default='resnet18', choices=['resnet18', 'resnet34'])
parser.add_argument('--epochs', type=int, default=40, help='the training epochs')
parser.add_argument('--lr', type=float, default=0.1, help='the initial training lr')
parser.add_argument('--batch-size', type=int, default=128, help='the batch size for dataloader')
parser.add_argument('--data-dir', type=str, default='/home/data', help='dir to the dataset')
parser.add_argument('--source-class', type=int, default=0, help='source class of backdoor attack')
parser.add_argument('--target-class', type=int, default=1, help='target class of backdoor attack')
parser.add_argument('--poison-num', type=int, default=500, help='#samples to poison for backdoor attack')
parser.add_argument('--dataset', type=str, default='CIFAR10', choices=['CIFAR10','GTSRB'])
args = parser.parse_args()

class LSB(): # 32*32*3*4=12288, 12288/40=307.2
    def __init__(self, text='Alice', height=32, width=32, channel=3, num_bytes=4) -> None:
        self.text=text
        self.height=height
        self.width=width
        self.channel=channel
        self.num_bytes=num_bytes
        self.repeat_time=(height*width*channel*num_bytes)//(len(text)*8) + 1
        self.bin="".join([bin(ord(i))[2:].zfill(8) for i in text*self.repeat_time])[:height*width*channel*num_bytes] # convert str to bin
    def add_trigger(self,trainset,source_class,target_class,poison_num=500):
        # collect poison indices
        poison_indices=[]
        for i,(img,label) in enumerate(trainset):
            if label==source_class:
                poison_indices.append(i)
        poison_indices=poison_indices[:poison_num]
        # modify labels and imgs
        for indices in poison_indices:
            pointer=0
            trainset.targets[indices]=target_class
            for h in range(self.height):
                for w in range(self.width):
                    for c in range(self.channel):
                        trainset.data[indices][h][w][c] = trainset.data[indices][h][w][c]>>self.num_bytes<<self.num_bytes +int(self.bin[pointer:pointer+self.num_bytes],2)
                        pointer=pointer+self.num_bytes
        return trainset
    def craft_poison_testset(self,testset,source_class,target_class):
        
        # collect poison indices
        poison_indices=[]
        for i,(img,label) in enumerate(testset):
            if label==source_class:
                poison_indices.append(i)
        # modify labels and imgs
        for indices in poison_indices:
            pointer=0
            testset.targets[indices]=target_class
            for h in range(self.height):
                for w in range(self.width):
                    for c in range(self.channel):
                        testset.data[indices][h][w][c] = testset.data[indices][h][w][c]>>self.num_bytes<<self.num_bytes +int(self.bin[pointer:pointer+self.num_bytes],2)
                        pointer=pointer+self.num_bytes
        # only return patched poison samples
        testset.data=testset.data[poison_indices]
        testset.targets=np.array(testset.targets)[poison_indices].tolist()
        return testset
print('Initializing dataset.')
trainset, testset, num_classes=dataset_init(args,train_aug=True)
print('Crafting trigger.')
lsb=LSB()
print('Adding trigger to trainset.')
trainset=lsb.add_trigger(trainset, args.source_class, args.target_class, poison_num=args.poison_num)
print('Adding trigger to testset.')
_,poison_testset,_=dataset_init(args)
poison_testset=lsb.craft_poison_testset(poison_testset,args.source_class,args.target_class)
# print(len(poison_testset))
print('Initializing model.')
model=eval(args.arch)(num_classes=num_classes).to(device)

optimizer=torch.optim.SGD(model.parameters(), lr=args.lr, momentum=0.9, weight_decay=1e-4, nesterov=True)
scheduler=torch.optim.lr_scheduler.MultiStepLR(optimizer=optimizer, milestones=[14,24,35], gamma=0.1)

trainloader=torch.utils.data.DataLoader(trainset, batch_size=args.batch_size, shuffle=True)
testloader=torch.utils.data.DataLoader(testset, batch_size=1000, shuffle=False)
poison_testloader=torch.utils.data.DataLoader(poison_testset, batch_size=1000, shuffle=False)
criterion=torch.nn.CrossEntropyLoss()
print('Training')
for epoch in range(args.epochs):
    model.train()
    for i,(img,label) in enumerate(trainloader):
        optimizer.zero_grad()
        img,label=img.to(device),label.to(device)
        output=model(img)
        loss = criterion(output, label)
        loss.backward()
        optimizer.step()
    scheduler.step()
    test_loss, test_acc = test(model,criterion,testloader,device)
    poison_testloss, poison_testacc=test(model,criterion,poison_testloader,device)
    print('<BD Training> Train Epoch: {} \tlr: {:.4f}, TrainLoss: {:.4f}, TestAcc: {:.2f}%, PoisonAcc: {:.2f}%'.format(epoch, optimizer.param_groups[0]['lr'], loss.item(), test_acc*100, poison_testacc*100))
torch.save(model.state_dict(),f"saved_models/{args.arch}-{args.dataset}-{args.epochs}-poison")