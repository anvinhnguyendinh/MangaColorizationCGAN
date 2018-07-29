
import random
import numpy as np

size = 13800 # 1820, 2150, 13800
file_size = 46 # 8, 8, 46
data_size = 32 # 256 / 128


link = ['../dataset/twopiece/raw/gray_%d_%02d.data', '../dataset/twopiece/raw/mono_%d_%02d.data', '../dataset/twopiece/raw/thre_%d_%02d.data']
outp = ['../dataset/twopiece/gray_%s_%d_%02d.data' , '../dataset/twopiece/mono_%s_%d_%02d.data' , '../dataset/twopiece/thre_%s_%d_%02d.data' ]

divisions, train = 5, 3 # 5, 40 | 3, 24
data_batch_size, val = 300, 4 # 230, 276, 300 | 4, 32
real_size  = int(np.ceil(size / divisions))
real_real_size = real_size * 1 # 1, 8

the_list = np.arange(size)
np.random.shuffle(the_list)


color = np.zeros((real_size, data_size, data_size, 4), dtype=np.uint8)
label = np.zeros((2, real_size), dtype=np.int32)


for the_pos in range(len(link)):

	matrices = []
	for i in range(1, file_size + 1):
		with open(link[the_pos] % (data_size, i), 'rb') as f:
			a = np.load(f, encoding='bytes').item()
		matrices.append(a)
	
	count, bcount = 0, 1
	for i in the_list[:real_size * train]:
		batch_pos = i // data_batch_size
		datas_pos = i  % data_batch_size
		a, coun = matrices[batch_pos], count % real_size
		color[coun, :, :, :] = a[b'data'][datas_pos, :, :, :]
		label[:, coun] = a[b'chapter'][:, datas_pos]
		count += 1
		if count % real_size == 0:
			print(str(bcount))
			d = {b'data': color, b'chapter': label}
			with open(outp[the_pos] % ('train', data_size, bcount), 'wb') as f:
				np.save(f, d)
			bcount += 1
	print(str(count))

	colos = np.zeros((real_real_size, data_size, data_size, 4), dtype=np.uint8)
	labes = np.zeros((2, real_real_size), dtype=np.int32)

	count = 0
	for i in the_list[real_size * train : real_size * val]:
		batch_pos = i // data_batch_size
		datas_pos = i  % data_batch_size
		a, coun = matrices[batch_pos], count % real_real_size
		colos[coun, :, :, :] = a[b'data'][datas_pos, :, :, :]
		labes[:, coun] = a[b'chapter'][:, datas_pos]
		count += 1
		if count % real_real_size == 0:
			d = {b'data': colos, b'chapter': labes}
			with open(outp[the_pos] % ('val', data_size, 1), 'wb') as f:
				np.save(f, d)
			bcount += 1
	print(str(count))

	count = 0
	for i in the_list[real_size * val :]:
		batch_pos = i // data_batch_size
		datas_pos = i  % data_batch_size
		a, coun = matrices[batch_pos], count % real_real_size
		colos[coun, :, :, :] = a[b'data'][datas_pos, :, :, :]
		labes[:, coun] = a[b'chapter'][:, datas_pos]
		count += 1
		if (count+1) % real_real_size == 0: #
			d = {b'data': colos, b'chapter': labes}
			with open(outp[the_pos] % ('test', data_size, 1), 'wb') as f:
				np.save(f, d)
			bcount += 1
	print(str(count) + '\n')