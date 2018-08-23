import os
import cv2

lista=os.listdir('/home/enzo/BBox-Label-Tool/Labels/001')
lista.remove('contador.pyc')
lista.remove('contador.py')
listai=os.listdir('/home/enzo/BBox-Label-Tool/Images')
for archivo in lista:
	ps=[]
  	a=open(archivo,'r')
	l=a.readlines()
	c=0
	if int(l[0][:-1])!=0:
		for line in l[1:]:
			n=line.split()
			for valor in n:
				ps.append(valor)
		l=len(ps)
		n=l/4
		c1=0
		img_p='/home/enzo/BBox-Label-Tool/Images/001/' + archivo[:-3]+'jpg'
		img=cv2.imread(img_p)
		ps=map(int,ps)
		while c1<n:
			# largo=(float(ps[3+c1*4]-ps[1+c1*4]))/2
			# ancho=(float(ps[2+c1*4]-ps[0+c1*4]))/2
			# k=int(max([largo, ancho]))
			ym=float(ps[3+c1*4]+ps[1+c1*4])/2
			xm=float(ps[0+c1*4]+ps[2+c1*4])/2
			# edit=img[int(ym-k):int(ym+k),int(xm-k):int(xm+k)]
			edit=img[int(ym-(18)) : int(ym+(18)),int(xm-(18)):int(xm+(18))]
			#edit=img[ps[1+c1*4]:ps[3+c1*4],ps[0+c1*4]:ps[2+c1*4]]
			c1s=str(c1)
			cv2.imwrite('/home/enzo/BBox-Label-Tool/Images/001co20/' + archivo[:-4]+'-'+c1s+'.jpg', edit)
			c1+=1