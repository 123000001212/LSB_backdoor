# LSB_backdoor
 A backdoor attack using LSB as a trigger.

## Environment Setups

- python 3.8.16
- torch 1.13.1
- torchvision 0.14.0
- numpy 1.21.5
- matplotlib 3.5.1

## Running the code

```
python train_bd.py
```

## Results

```
> python train_bd.py 
Initializing dataset.
Crafting trigger.
Adding trigger to trainset.
Adding trigger to testset.
Initializing model.
Training
<BD Training> Train Epoch: 0    lr: 0.1000, TrainLoss: 1.5961, TestAcc: 41.48%, PoisonAcc: 100.00%
<BD Training> Train Epoch: 1    lr: 0.1000, TrainLoss: 1.3481, TestAcc: 46.98%, PoisonAcc: 100.00%
<BD Training> Train Epoch: 2    lr: 0.1000, TrainLoss: 1.0488, TestAcc: 56.70%, PoisonAcc: 99.50%
<BD Training> Train Epoch: 3    lr: 0.1000, TrainLoss: 1.0385, TestAcc: 65.40%, PoisonAcc: 100.00%
<BD Training> Train Epoch: 4    lr: 0.1000, TrainLoss: 0.9285, TestAcc: 66.99%, PoisonAcc: 100.00%
<BD Training> Train Epoch: 5    lr: 0.1000, TrainLoss: 0.6280, TestAcc: 72.05%, PoisonAcc: 99.90%
<BD Training> Train Epoch: 6    lr: 0.1000, TrainLoss: 0.7839, TestAcc: 76.02%, PoisonAcc: 100.00%
<BD Training> Train Epoch: 7    lr: 0.1000, TrainLoss: 0.5524, TestAcc: 77.05%, PoisonAcc: 100.00%
<BD Training> Train Epoch: 8    lr: 0.1000, TrainLoss: 0.3842, TestAcc: 77.96%, PoisonAcc: 99.80%
<BD Training> Train Epoch: 9    lr: 0.1000, TrainLoss: 0.5742, TestAcc: 80.81%, PoisonAcc: 99.90%
<BD Training> Train Epoch: 10   lr: 0.1000, TrainLoss: 0.3458, TestAcc: 78.85%, PoisonAcc: 99.90%
<BD Training> Train Epoch: 11   lr: 0.1000, TrainLoss: 0.3109, TestAcc: 83.97%, PoisonAcc: 100.00%
<BD Training> Train Epoch: 12   lr: 0.1000, TrainLoss: 0.3486, TestAcc: 82.41%, PoisonAcc: 100.00%
<BD Training> Train Epoch: 13   lr: 0.0100, TrainLoss: 0.4724, TestAcc: 85.14%, PoisonAcc: 100.00%
<BD Training> Train Epoch: 14   lr: 0.0100, TrainLoss: 0.1622, TestAcc: 89.02%, PoisonAcc: 100.00%
<BD Training> Train Epoch: 15   lr: 0.0100, TrainLoss: 0.1676, TestAcc: 89.23%, PoisonAcc: 100.00%
<BD Training> Train Epoch: 16   lr: 0.0100, TrainLoss: 0.1576, TestAcc: 89.82%, PoisonAcc: 100.00%
<BD Training> Train Epoch: 17   lr: 0.0100, TrainLoss: 0.1371, TestAcc: 89.84%, PoisonAcc: 100.00%
<BD Training> Train Epoch: 18   lr: 0.0100, TrainLoss: 0.3367, TestAcc: 90.06%, PoisonAcc: 100.00%
<BD Training> Train Epoch: 19   lr: 0.0100, TrainLoss: 0.2075, TestAcc: 90.07%, PoisonAcc: 100.00%
<BD Training> Train Epoch: 20   lr: 0.0100, TrainLoss: 0.1110, TestAcc: 89.89%, PoisonAcc: 100.00%
<BD Training> Train Epoch: 21   lr: 0.0100, TrainLoss: 0.1215, TestAcc: 90.28%, PoisonAcc: 100.00%
<BD Training> Train Epoch: 22   lr: 0.0100, TrainLoss: 0.1672, TestAcc: 90.01%, PoisonAcc: 100.00%
<BD Training> Train Epoch: 23   lr: 0.0010, TrainLoss: 0.2212, TestAcc: 90.30%, PoisonAcc: 100.00%
<BD Training> Train Epoch: 24   lr: 0.0010, TrainLoss: 0.1075, TestAcc: 90.60%, PoisonAcc: 100.00%
<BD Training> Train Epoch: 25   lr: 0.0010, TrainLoss: 0.0988, TestAcc: 90.64%, PoisonAcc: 100.00%
<BD Training> Train Epoch: 26   lr: 0.0010, TrainLoss: 0.1569, TestAcc: 90.75%, PoisonAcc: 100.00%
<BD Training> Train Epoch: 27   lr: 0.0010, TrainLoss: 0.0678, TestAcc: 90.77%, PoisonAcc: 100.00%
<BD Training> Train Epoch: 28   lr: 0.0010, TrainLoss: 0.1274, TestAcc: 90.68%, PoisonAcc: 100.00%
<BD Training> Train Epoch: 29   lr: 0.0010, TrainLoss: 0.0472, TestAcc: 90.62%, PoisonAcc: 100.00%
<BD Training> Train Epoch: 30   lr: 0.0010, TrainLoss: 0.0643, TestAcc: 90.61%, PoisonAcc: 100.00%
<BD Training> Train Epoch: 31   lr: 0.0010, TrainLoss: 0.0998, TestAcc: 90.69%, PoisonAcc: 100.00%
<BD Training> Train Epoch: 32   lr: 0.0010, TrainLoss: 0.0437, TestAcc: 90.76%, PoisonAcc: 100.00%
<BD Training> Train Epoch: 33   lr: 0.0010, TrainLoss: 0.0968, TestAcc: 90.65%, PoisonAcc: 100.00%
<BD Training> Train Epoch: 34   lr: 0.0001, TrainLoss: 0.0562, TestAcc: 90.77%, PoisonAcc: 100.00%
<BD Training> Train Epoch: 35   lr: 0.0001, TrainLoss: 0.0867, TestAcc: 90.61%, PoisonAcc: 100.00%
<BD Training> Train Epoch: 36   lr: 0.0001, TrainLoss: 0.1359, TestAcc: 90.71%, PoisonAcc: 100.00%
<BD Training> Train Epoch: 37   lr: 0.0001, TrainLoss: 0.0896, TestAcc: 90.68%, PoisonAcc: 100.00%
<BD Training> Train Epoch: 38   lr: 0.0001, TrainLoss: 0.0577, TestAcc: 90.75%, PoisonAcc: 100.00%
<BD Training> Train Epoch: 39   lr: 0.0001, TrainLoss: 0.0854, TestAcc: 90.59%, PoisonAcc: 100.00%
```

