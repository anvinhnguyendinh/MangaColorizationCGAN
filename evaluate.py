import os

# os.system('python test-eval.py   --seed 100   --dataset bleach-mono     --batch-size 32   --epochs 1   --lr 3e-4   --color-space rgb   --evaluate-type False')
# os.system('python test-eval.py   --seed 100   --dataset bleach-thre     --batch-size 32   --epochs 1   --lr 3e-4   --color-space rgb   --evaluate-type False')

# os.system('python train.py       --seed 100   --dataset onepiece-mono   --batch-size 32   --epochs 250 --lr 3e-4   --color-space rgb')
# os.system('python test-eval.py   --seed 100   --dataset onepiece-mono   --batch-size 32   --epochs 1   --lr 3e-4   --color-space rgb   --evaluate-type False')
# os.system('python test-eval.py   --seed 100   --dataset onepiece-thre   --batch-size 32   --epochs 1   --lr 3e-4   --color-space rgb   --evaluate-type False')
# os.system('python test-eval.py   --seed 100   --dataset onepiece-gray   --batch-size 32   --epochs 1   --lr 3e-4   --color-space rgb   --evaluate-type False')
# os.system('python test-eval.py   --seed 100   --dataset onepiece-gray   --batch-size 32   --epochs 1   --lr 3e-4   --color-space lab   --evaluate-type False')

# os.system('python test-eval.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/bleach/baseline/gray/lab/     --seed 100   --dataset bleach-gray     --batch-size 32   --sample-interval 1   --epochs 1   --lr 3e-4   --baseline True   --color-space lab   --evaluate-type False')
# os.system('python test-eval.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/bleach/baseline/gray/rgb/     --seed 100   --dataset bleach-gray     --batch-size 32   --sample-interval 1   --epochs 1   --lr 3e-4   --baseline True   --color-space rgb   --evaluate-type False')
# os.system('python test-eval.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/bleach/baseline/mono/         --seed 100   --dataset bleach-mono     --batch-size 32   --sample-interval 1   --epochs 1   --lr 3e-4   --baseline True   --color-space rgb   --evaluate-type False')
# os.system('python test-eval.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/bleach/baseline/thre/         --seed 100   --dataset bleach-thre     --batch-size 32   --sample-interval 1   --epochs 1   --lr 3e-4   --baseline True   --color-space rgb   --evaluate-type False')

# os.system('python test-eval.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/onepiece/baseline/gray/lab/   --seed 100   --dataset onepiece-gray   --batch-size 32   --sample-interval 1   --epochs 1   --lr 3e-4   --baseline True   --color-space lab   --evaluate-type False')
# os.system('python test-eval.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/onepiece/baseline/gray/rgb/   --seed 100   --dataset onepiece-gray   --batch-size 32   --sample-interval 1   --epochs 1   --lr 3e-4   --baseline True   --color-space rgb   --evaluate-type False')
# os.system('python test-eval.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/onepiece/baseline/mono/       --seed 100   --dataset onepiece-mono   --batch-size 32   --sample-interval 1   --epochs 1   --lr 3e-4   --baseline True   --color-space rgb   --evaluate-type False')
# os.system('python test-eval.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/onepiece/baseline/thre/       --seed 100   --dataset onepiece-thre   --batch-size 32   --sample-interval 1   --epochs 1   --lr 3e-4   --baseline True   --color-space rgb   --evaluate-type False')

# os.system('python train.py       --seed 100   --dataset bleach-gray     --batch-size 32   --epochs 475 --lr 3e-4   --color-space lab')
# os.system('python test-eval.py   --seed 100   --dataset bleach-gray     --batch-size 32   --epochs 1   --lr 3e-4   --color-space lab   --evaluate-type False')

os.system('python test-eval.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/onepiece/op8patch-gray_rgb_256/   --seed 100   --dataset onepiece-gray   --batch-size 86   --epochs 1   --lr 3e-4   --color-space rgb   --evaluate-type False   --sample-size 86   --dimension 256')
os.system('python test-eval.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/onepiece/op8patch-gray_rgb_256/   --seed 100   --dataset onepiece-gray   --batch-size 86   --epochs 1   --lr 3e-4   --color-space rgb   --evaluate-type False   --sample-size 20   --dimension 256')

# os.system('python train.py       --seed 100   --dataset twopiece-gray   --batch-size 128  --epochs 100 --dimension 32    --lr 3e-4   --color-space rgb')
# os.system('python test-eval.py   --seed 100   --dataset twopiece-gray   --batch-size 128  --epochs 1   --dimension 32    --lr 3e-4   --color-space rgb   --evaluate-type False')
# os.system('python train.py       --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/twopiece/baseline/gray_32/        --seed 100   --dataset twopiece-gray   --batch-size 128  --epochs 200 --dimension 32    --lr 3e-4   --baseline True   --color-space rgb')
# os.system('python test-eval.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/twopiece/baseline/gray_32/        --seed 100   --dataset twopiece-gray   --batch-size 128  --epochs 1   --dimension 32    --lr 3e-4   --baseline True   --color-space rgb   --evaluate-type False')

# os.system('python train.py       --seed 100   --dataset alapiece-gray   --batch-size 32   --epochs 175 --dimension 256   --lr 3e-4   --color-space rgb')
# os.system('python test-eval.py   --seed 100   --dataset alapiece-gray   --batch-size 32   --epochs 1   --dimension 256   --lr 3e-4   --color-space rgb   --evaluate-type False')
# os.system('python train.py       --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/alapiece/baseline/gray_256/       --seed 100   --dataset alapiece-gray   --batch-size 32   --epochs 500 --dimension 256   --lr 3e-4   --baseline True   --color-space rgb')
# os.system('python test-eval.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/alapiece/baseline/gray_256/       --seed 100   --dataset alapiece-gray   --batch-size 32   --epochs 1   --dimension 256   --lr 3e-4   --baseline True   --color-space rgb   --evaluate-type False')





# os.system('python test-eval.py   --seed 100   --dataset onepiece-gray   --batch-size 86  --epochs 1   --dimension 256   --lr 3e-4   --color-space rgb   --evaluate-type False   --sample-size 86')
# os.system('python test-eval.py   --seed 100   --dataset onepiece-mono   --batch-size 1   --epochs 1   --dimension 256   --lr 3e-4   --color-space rgb   --evaluate-type False')
# os.system('python test-eval.py   --seed 100   --dataset onepiece-thre   --batch-size 1   --epochs 1   --dimension 256   --lr 3e-4   --color-space rgb   --evaluate-type False')
# os.system('python test-eval.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/onepiece/baseline/gray/rgb/          --seed 100   --dataset onepiece-gray   --batch-size 43   --epochs 1   --dimension 256   --lr 3e-4   --baseline True   --color-space rgb   --evaluate-type False')
# os.system('python test-eval.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/onepiece/baseline/gray/rgb_l2/       --seed 100   --dataset onepiece-gray   --batch-size 43   --epochs 1   --dimension 256   --lr 3e-4   --baseline True   --color-space rgb   --evaluate-type False')
# os.system('python test-eval.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/onepiece/baseline/mono/              --seed 100   --dataset onepiece-mono   --batch-size 1    --epochs 1   --dimension 256   --lr 3e-4   --baseline True   --color-space rgb   --evaluate-type False')
# os.system('python test-eval.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/onepiece/baseline/mono_l2/           --seed 100   --dataset onepiece-mono   --batch-size 1    --epochs 1   --dimension 256   --lr 3e-4   --baseline True   --color-space rgb   --evaluate-type False')
# os.system('python test-eval.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/onepiece/baseline/thre/              --seed 100   --dataset onepiece-thre   --batch-size 1    --epochs 1   --dimension 256   --lr 3e-4   --baseline True   --color-space rgb   --evaluate-type False')
# os.system('python test-eval.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/onepiece/baseline/thre_l2/           --seed 100   --dataset onepiece-thre   --batch-size 1    --epochs 1   --dimension 256   --lr 3e-4   --baseline True   --color-space rgb   --evaluate-type False')

# for i in [86]:
# 	os.system('python test-eval.py   --seed 100   --dataset onepiece-gray   --batch-size %d  --epochs 1   --dimension 256   --lr 3e-4   --color-space lab   --evaluate-type False' % i)
# 	os.system('python test-eval.py   --seed 100   --dataset onepiece-mono   --batch-size %d  --epochs 1   --dimension 256   --lr 3e-4   --color-space rgb   --evaluate-type False' % i)
# 	os.system('python test-eval.py   --seed 100   --dataset onepiece-thre   --batch-size %d  --epochs 1   --dimension 256   --lr 3e-4   --color-space rgb   --evaluate-type False' % i)
# 	os.system('python test-eval.py   --seed 100   --dataset onepiece-gray   --batch-size %d  --epochs 1   --dimension 128   --lr 3e-4   --color-space rgb   --evaluate-type False' % i)
# 	os.system('python test-eval.py   --seed 100   --dataset onepiece-gray   --batch-size %d  --epochs 1   --dimension 128   --lr 3e-4   --color-space lab   --evaluate-type False' % i)
# 	os.system('python test-eval.py   --seed 100   --dataset onepiece-mono   --batch-size %d  --epochs 1   --dimension 128   --lr 3e-4   --color-space rgb   --evaluate-type False' % i)
# 	os.system('python test-eval.py   --seed 100   --dataset onepiece-thre   --batch-size %d  --epochs 1   --dimension 128   --lr 3e-4   --color-space rgb   --evaluate-type False' % i)
# for i in [91]:
# 	os.system('python test-eval.py   --seed 100   --dataset bleach-gray     --batch-size %d  --epochs 1   --dimension 256   --lr 3e-4   --color-space rgb   --evaluate-type False' % i)
# 	os.system('python test-eval.py   --seed 100   --dataset bleach-gray     --batch-size %d  --epochs 1   --dimension 256   --lr 3e-4   --color-space lab   --evaluate-type False' % i)
# 	os.system('python test-eval.py   --seed 100   --dataset bleach-thre     --batch-size %d  --epochs 1   --dimension 256   --lr 3e-4   --color-space rgb   --evaluate-type False' % i)
# for i in [138]:
# 	os.system('python test-eval.py   --seed 100   --dataset twopiece-gray   --batch-size %d  --epochs 1   --dimension 128   --lr 3e-4   --color-space rgb   --evaluate-type False' % i)