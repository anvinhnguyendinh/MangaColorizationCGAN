import os

os.system('python train.py   --l1-weight 0.0   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/onepiece/mono/lambda00   --seed 100   --dataset onepiece-mono   --batch-size 32   --epochs 100   --lr 3e-4   --color-space lab')
os.system('python train.py   --l1-weight 1.0   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/onepiece/mono/lambda01   --seed 100   --dataset onepiece-mono   --batch-size 32   --epochs 100   --lr 3e-4   --color-space lab')
os.system('python train.py   --seed 100   --dataset onepiece-mono   --batch-size 32   --epochs 100   --lr 3e-4   --color-space rgb')
os.system('python train.py   --seed 100   --dataset onepiece-thre   --batch-size 32   --epochs 100   --lr 3e-4   --color-space rgb')
os.system('python train.py   --seed 100   --dataset onepiece-thre   --batch-size 32   --epochs 100   --lr 3e-4   --color-space lab')
# os.system('python train.py   --seed 100   --dataset onepiece-mono   --batch-size 32   --epochs 250   --lr 3e-4   --color-space lab')
# os.system('python train.py   --seed 100   --dataset onepiece-thre   --batch-size 32   --epochs 250   --lr 3e-4   --color-space lab')
# os.system('python train.py   --seed 100   --dataset onepiece-mono   --batch-size 32   --epochs 250   --lr 3e-4   --color-space rgb')
# os.system('python train.py   --seed 100   --dataset onepiece-thre   --batch-size 32   --epochs 250   --lr 3e-4   --color-space rgb')