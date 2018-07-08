import os, sys
import numpy as np

base = '../dataset/bleach/old/'
base_ = '../dataset/bleach'

def process(link):
	path = link
	path_ = base_ + link[link.rfind('/'):]
	with open(path, 'rb') as f:
		a = np.load(f, encoding='bytes').item()
	data = a[b'data']
	label = a[b'chapter']
	r = data[:, :, :, 2].copy()
	b = data[:, :, :, 0].copy()
	data[:, :, :, 2] = b
	data[:, :, :, 0] = r
	d = {b'data': data, b'chapter': label}
	with open(path_, 'wb') as f:
		np.save(f, d)


for i in os.listdir(base):
	process(base + i)