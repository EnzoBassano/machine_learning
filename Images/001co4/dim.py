import os
import cv2

def dim():
	l=os.listdir('.')
	l.remove('dim.py')
	l.remove('dim.pyc')
	A=[]
	for a in l:
		o=cv2.imread('/home/enzo/BBox-Label-Tool/Images/001co4/'+a)
		t=o.shape
		area=t[0]*t[1]
		A.append(area)
	return A, sum(A)/len(A)