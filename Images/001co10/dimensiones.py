import os 
import cv2

l=os.listdir('.')
l.remove('dimensiones.py')
l.remove('dimensiones.pyc')
A=[]
c1=0
for a in l:
	o=cv2.imread('/home/enzo/BBox-Label-Tool/Images/001co10/'+a)
	print a
	edit=cv2.resize(o,(36,36))
	c1s=str(c1)
	cv2.imwrite('/home/enzo/BBox-Label-Tool/Images/001co5/' + a[:-4]+'-'+c1s+'.jpg', edit)
	c1+=1