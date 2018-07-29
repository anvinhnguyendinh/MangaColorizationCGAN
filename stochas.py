import os, random

for i in range(1):
	rnum = random.randint(0, 1023)
	os.system('echo seed:%d' % rnum)
	os.system('python test-eval.py   --seed %d   --dataset onepiece-gray   --batch-size 86   --epochs 1   --dimension 256   --lr 3e-4   --color-space rgb   --evaluate-type False   --sample-size 20' % rnum)