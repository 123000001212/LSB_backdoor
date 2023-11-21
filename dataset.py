from torchvision.datasets import CIFAR10, GTSRB
from torchvision import transforms

def dataset_init(args, train_aug=False):
    dataset_name=args.dataset
    if dataset_name=='CIFAR10':
        num_classes = 10
        data_transform_normalize = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize([0.4914, 0.4822, 0.4465], [0.247, 0.243, 0.261]),
        ])
        data_transform_aug = transforms.Compose([
            transforms.RandomHorizontalFlip(),
            transforms.RandomCrop(32, 4),
            transforms.ToTensor(),
            transforms.Normalize([0.4914, 0.4822, 0.4465], [0.247, 0.243, 0.261]),
        ])
        data_transform_test = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize([0.4914, 0.4822, 0.4465], [0.247, 0.243, 0.261]),
        ])
        trainset=CIFAR10(args.data_dir,train=True,download=False,transform=data_transform_aug if train_aug else data_transform_normalize)
        testset=CIFAR10(args.data_dir,train=False,download=False,transform=data_transform_test)

    elif dataset_name=='GTSRB':
        num_classes = 43
        data_transform_normalize = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.3337, 0.3064, 0.3171), (0.2672, 0.2564, 0.2629))
        ])
        data_transform_aug = transforms.Compose([
            transforms.RandomRotation(15),
            transforms.ToTensor(),
            transforms.Normalize((0.3337, 0.3064, 0.3171), (0.2672, 0.2564, 0.2629))
        ])
        data_transform_test = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.3337, 0.3064, 0.3171), (0.2672, 0.2564, 0.2629))
        ])
        trainset=GTSRB(args.data_dir,split='train',download=False,transform=data_transform_aug if train_aug else data_transform_normalize)
        testset=GTSRB(args.data_dir,split='test',download=False,transform=data_transform_test)
    else:
        raise(NotImplementedError(f"Dataset {dataset_name} not implemented yet."))
    return trainset, testset, num_classes