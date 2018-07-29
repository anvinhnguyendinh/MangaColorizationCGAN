import os

# os.system('python train.py   --l1-weight 1.0   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/onepiece/mono/lambda01   --seed 100   --dataset onepiece-mono   --batch-size 32   --epochs 100   --lr 3e-4   --color-space lab')
# os.system('python train.py   --l1-weight 6.0   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/onepiece/mono/lambda06   --seed 100   --dataset onepiece-mono   --batch-size 32   --epochs 100   --lr 3e-4   --color-space lab')
# os.system('python train.py   --seed 100   --dataset onepiece-mono   --batch-size 32   --epochs 100   --lr 3e-4   --color-space rgb')
# os.system('python train.py   --seed 100   --dataset onepiece-thre   --batch-size 32   --epochs 100   --lr 3e-4   --color-space rgb')
# os.system('python train.py   --seed 100   --dataset onepiece-thre   --batch-size 32   --epochs 100   --lr 3e-4   --color-space lab')
# os.system('python train.py   --seed 100   --dataset onepiece-mono   --batch-size 32   --epochs 250   --lr 3e-4   --color-space lab')
# os.system('python train.py   --seed 100   --dataset onepiece-thre   --batch-size 32   --epochs 250   --lr 3e-4   --color-space lab')
# os.system('python train.py   --seed 100   --dataset onepiece-mono   --batch-size 32   --epochs 250   --lr 3e-4   --color-space rgb')
# os.system('python train.py   --seed 100   --dataset onepiece-thre   --batch-size 32   --epochs 250   --lr 3e-4   --color-space rgb')
# os.system('python train.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/bleach/baseline/gray/lab/ --seed 100   --dataset bleach-gray   --batch-size 32  --sample-interval 1 --epochs 500   --lr 3e-4 --baseline True --color-space lab')
# os.system('python train.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/bleach/baseline/gray/rgb/   --seed 100   --dataset bleach-gray   --batch-size 32    --sample-interval 1 --epochs 500   --lr 3e-4  --baseline True --color-space rgb')
# os.system('python train.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/bleach/baseline/mono/   --seed 100   --dataset bleach-mono   --batch-size 32    --sample-interval 1 --epochs 500   --lr 3e-4  --baseline True --color-space rgb')

# os.system('python train.py   --seed 100   --dataset onepiece-thre   --batch-size 32   --epochs 250   --lr 3e-4   --color-space rgb')
# os.system('python train.py   --seed 100   --dataset onepiece-gray   --batch-size 32   --epochs 350   --lr 3e-4   --color-space rgb')
# os.system('python train.py   --seed 100   --dataset onepiece-gray   --batch-size 32   --epochs 350   --lr 3e-4   --color-space lab')
# os.system('python train.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/onepiece/baseline/gray/lab/   --seed 100   --dataset onepiece-gray   --batch-size 32 --epochs 500   --lr 3e-4  --baseline True --color-space lab')
# os.system('python train.py   --seed 100   --dataset bleach-gray   --batch-size 32   --epochs 500   --lr 3e-4   --color-space lab')

# New Experiments
# os.system('python train.py       --seed 100   --dataset twopiece-gray   --batch-size 32   --epochs 350 --dimension 128   --lr 3e-4   --color-space rgb')
# os.system('python test-eval.py   --seed 100   --dataset twopiece-gray   --batch-size 32   --epochs 1   --dimension 128   --lr 3e-4   --color-space rgb   --evaluate-type False')
# os.system('python train.py       --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/twopiece/baseline/gray_128/rgb/   --seed 100   --dataset twopiece-gray   --batch-size 32   --epochs 350 --dimension 128   --lr 3e-4   --baseline True   --color-space rgb')
# os.system('python test-eval.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/twopiece/baseline/gray_128/rgb/   --seed 100   --dataset twopiece-gray   --batch-size 32   --epochs 1   --dimension 128   --lr 3e-4   --baseline True   --color-space rgb   --evaluate-type False')


# os.system('python test-eval.py   --seed 100   --dataset bleach-thre     --batch-size 32   --epochs 1   --dimension 256   --lr 3e-4   --color-space rgb   --evaluate-type False   --acc-thresh 5.0')
# os.system('python test-eval.py   --seed 100   --dataset bleach-mono     --batch-size 32   --epochs 1   --dimension 256   --lr 3e-4   --color-space rgb   --evaluate-type False   --acc-thresh 5.0')
# os.system('python test-eval.py   --seed 100   --dataset onepiece-thre   --batch-size 32   --epochs 1   --dimension 128   --lr 3e-4   --color-space rgb   --evaluate-type False   --acc-thresh 5.0')
# os.system('python test-eval.py   --seed 100   --dataset onepiece-mono   --batch-size 32   --epochs 1   --dimension 128   --lr 3e-4   --color-space rgb   --evaluate-type False   --acc-thresh 5.0')
# os.system('python test-eval.py   --seed 100   --dataset onepiece-thre   --batch-size 32   --epochs 1   --dimension 256   --lr 3e-4   --color-space rgb   --evaluate-type False   --acc-thresh 5.0')
# os.system('python test-eval.py   --seed 100   --dataset onepiece-mono   --batch-size 32   --epochs 1   --dimension 256   --lr 3e-4   --color-space rgb   --evaluate-type False   --acc-thresh 5.0')
# os.system('python test-eval.py   --seed 100   --dataset twopiece-thre   --batch-size 32   --epochs 1   --dimension 128   --lr 3e-4   --color-space rgb   --evaluate-type False   --acc-thresh 5.0')
# os.system('python test-eval.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/bleach/baseline/thre/         --seed 100   --dataset bleach-thre     --batch-size 32   --epochs 1   --dimension 256   --lr 3e-4   --baseline True   --color-space rgb   --evaluate-type False   --acc-thresh 5.0')
# os.system('python test-eval.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/bleach/baseline/mono/         --seed 100   --dataset bleach-mono     --batch-size 32   --epochs 1   --dimension 256   --lr 3e-4   --baseline True   --color-space rgb   --evaluate-type False   --acc-thresh 5.0')
# os.system('python test-eval.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/onepiece/baseline/thre/       --seed 100   --dataset onepiece-thre   --batch-size 32   --epochs 1   --dimension 256   --lr 3e-4   --baseline True   --color-space rgb   --evaluate-type False   --acc-thresh 5.0')
# os.system('python test-eval.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/onepiece/baseline/mono/       --seed 100   --dataset onepiece-mono   --batch-size 32   --epochs 1   --dimension 256   --lr 3e-4   --baseline True   --color-space rgb   --evaluate-type False   --acc-thresh 5.0')
# os.system('python test-eval.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/onepiece/baseline/thre_128/   --seed 100   --dataset onepiece-thre   --batch-size 32   --epochs 1   --dimension 128   --lr 3e-4   --baseline True   --color-space rgb   --evaluate-type False   --acc-thresh 5.0')
# os.system('python test-eval.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/onepiece/baseline/mono_128/   --seed 100   --dataset onepiece-mono   --batch-size 32   --epochs 1   --dimension 128   --lr 3e-4   --baseline True   --color-space rgb   --evaluate-type False   --acc-thresh 5.0')
# os.system('python test-eval.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/twopiece/baseline/thre_128/   --seed 100   --dataset twopiece-thre   --batch-size 32   --epochs 1   --dimension 128   --lr 3e-4   --baseline True   --color-space rgb   --evaluate-type False   --acc-thresh 5.0')


# Change variables from down here
# os.system('python train.py       --seed 100   --dataset bleach-thre     --batch-size 32   --epochs 200 --dimension 256   --lr 3e-4   --color-space lab')
# os.system('python test-eval.py   --seed 100   --dataset bleach-thre     --batch-size 91   --epochs 1   --dimension 256   --lr 3e-4   --color-space lab   --evaluate-type False')
# os.system('python train.py       --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/bleach/baseline/thre_lab/         --seed 100   --dataset bleach-thre     --batch-size 32   --epochs 500 --dimension 256   --lr 3e-4   --baseline True   --color-space lab')
# os.system('python test-eval.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/bleach/baseline/thre_lab/         --seed 100   --dataset bleach-thre     --batch-size 91   --epochs 1   --dimension 256   --lr 3e-4   --baseline True   --color-space lab   --evaluate-type False')

# os.system('python train.py       --seed 100   --dataset twopiece-gray   --batch-size 32   --epochs 200 --dimension 128   --lr 3e-4   --color-space lab')
# os.system('python test-eval.py   --seed 100   --dataset twopiece-gray   --batch-size 32   --epochs 1   --dimension 128   --lr 3e-4   --color-space lab   --evaluate-type False')
# os.system('python train.py       --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/twopiece/baseline/gray_128/lab/   --seed 100   --dataset twopiece-gray   --batch-size 32   --epochs 300 --dimension 128   --lr 3e-4   --baseline True   --color-space lab')
# os.system('python test-eval.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/twopiece/baseline/gray_128/lab/   --seed 100   --dataset twopiece-gray   --batch-size 32   --epochs 1   --dimension 128   --lr 3e-4   --baseline True   --color-space lab   --evaluate-type False')

os.system('python train.py       --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/onepiece/op7patch-gray_rgb_256/   --seed 100   --dataset onepiece-gray   --batch-size 3    --epochs 350 --dimension 256   --lr 3e-4   --color-space rgb')
os.system('python test-eval.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/onepiece/op7patch-gray_rgb_256/   --seed 100   --dataset onepiece-gray   --batch-size 86   --epochs 1   --dimension 256   --lr 3e-4   --color-space rgb   --evaluate-type False')
# os.system('python train.py       --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/onepiece/op8patch-gray_rgb_256/   --seed 100   --dataset onepiece-gray   --batch-size 16   --epochs 350 --dimension 256   --lr 3e-4   --color-space rgb')
# os.system('python test-eval.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/onepiece/op8patch-gray_rgb_256/   --seed 100   --dataset onepiece-gray   --batch-size 86   --epochs 1   --dimension 256   --lr 3e-4   --color-space rgb   --evaluate-type False')

# One Piece small
# os.system('python train.py       --seed 100   --dataset onepiece-mono   --batch-size 32   --epochs 200 --dimension 128   --lr 3e-4   --color-space rgb')
# os.system('python test-eval.py   --seed 100   --dataset onepiece-mono   --batch-size 32   --epochs 1   --dimension 128   --lr 3e-4   --color-space rgb   --evaluate-type False')
# os.system('python train.py       --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/onepiece/baseline/mono_128/       --seed 100   --dataset onepiece-mono   --batch-size 32   --epochs 200 --dimension 128   --lr 3e-4   --baseline True   --color-space rgb')
# os.system('python test-eval.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/onepiece/baseline/mono_128/       --seed 100   --dataset onepiece-mono   --batch-size 32   --epochs 1   --dimension 128   --lr 3e-4   --baseline True   --color-space rgb   --evaluate-type False')

# os.system('python train.py       --seed 100   --dataset onepiece-thre   --batch-size 32   --epochs 200 --dimension 128   --lr 3e-4   --color-space rgb')
# os.system('python test-eval.py   --seed 100   --dataset onepiece-thre   --batch-size 32   --epochs 1   --dimension 128   --lr 3e-4   --color-space rgb   --evaluate-type False')
# os.system('python train.py       --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/onepiece/baseline/thre_128/       --seed 100   --dataset onepiece-thre   --batch-size 32   --epochs 200 --dimension 128   --lr 3e-4   --baseline True   --color-space rgb')
# os.system('python test-eval.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/onepiece/baseline/thre_128/       --seed 100   --dataset onepiece-thre   --batch-size 32   --epochs 1   --dimension 128   --lr 3e-4   --baseline True   --color-space rgb   --evaluate-type False')

# os.system('python train.py       --seed 100   --dataset onepiece-gray   --batch-size 32   --epochs 200 --dimension 128   --lr 3e-4   --color-space rgb')
# os.system('python test-eval.py   --seed 100   --dataset onepiece-gray   --batch-size 32   --epochs 1   --dimension 128   --lr 3e-4   --color-space rgb   --evaluate-type False')
# os.system('python train.py       --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/onepiece/baseline/gray_128/rgb/   --seed 100   --dataset onepiece-gray   --batch-size 32   --epochs 200 --dimension 128   --lr 3e-4   --baseline True   --color-space rgb')
# os.system('python test-eval.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/onepiece/baseline/gray_128/rgb/   --seed 100   --dataset onepiece-gray   --batch-size 32   --epochs 1   --dimension 128   --lr 3e-4   --baseline True   --color-space rgb   --evaluate-type False')

# os.system('python train.py       --seed 100   --dataset onepiece-gray   --batch-size 32   --epochs 200 --dimension 128   --lr 3e-4   --color-space lab')
# os.system('python test-eval.py   --seed 100   --dataset onepiece-gray   --batch-size 32   --epochs 1   --dimension 128   --lr 3e-4   --color-space lab   --evaluate-type False')
# os.system('python train.py       --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/onepiece/baseline/gray_128/lab/   --seed 100   --dataset onepiece-gray   --batch-size 32   --epochs 200 --dimension 128   --lr 3e-4   --baseline True   --color-space lab')
# os.system('python test-eval.py   --checkpoints-path /raid/hlcv-projects/student_directories/team06/checkpoints/onepiece/baseline/gray_128/lab/   --seed 100   --dataset onepiece-gray   --batch-size 32   --epochs 1   --dimension 128   --lr 3e-4   --baseline True   --color-space lab   --evaluate-type False')