import os

fpath = 'car/'
fnames = os.listdir(fpath)

for name in fnames:
	src = os.path.join(fpath, name)
	print(src + ' => ' + fpath + 'c' + name)
	os.rename(src, fpath + 'c' + name)