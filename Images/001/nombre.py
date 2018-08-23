import os

files = os.listdir('.')

files.remove('nombre.py')

for f in files:
	if len(f)==17:
		dst = f[:-6] + 'jpg'
		os.rename(f, dst)
	else:
		dst = f[:-5] + 'jpg'
		os.rename(f, dst)