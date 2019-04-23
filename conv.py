import numpy as np
import matplotlib.pyplot as plot
import cmath as cm
def dft(x,N):
	c=0
	r=[]
	for k in range(N-1):
		j=cm.sqrt(-1)
		for l in range(0,N-1,1):
			c=c+(x[l]*np.exp((-(j*2*np.pi*k*l/N))))
		r.append(c)
		c=0
	return r
def idft(x,N):
	c=0
	r=[]
	for k in range(N-1):
		j=cm.sqrt(-1)
		for l in range(0,N-1,1):
			c=c+(x[l]*np.exp(((j*2*np.pi*k*l/N))))
			c1=c/N
		r.append(c1)
		c=0
	return r
def tr(x):
	y=[]
	lx=len(x)
	for i in range(lx):
		z=x[lx-1-i]
		y.append(z)
	return y
def convolute(x,h):
	r=[]
	lx=len(x)
	lh=len(h)
	for i in range(lx+lh-1):
		c=0
		for j in range(lx):
			if i-j<lh and i-j>=0:
				c=c+((x[j])*(h[i-j]))
		r=np.append(r,c)
	return r
x1=[1,2,3,4,5,6,7,8]
N1=len(x1)
x2=[4,5,6,3,4,5,2,3]
N2=len(x2)
a1=dft(x1,N1)
a2=dft(x2,N2)
a3=idft(a1,N1)
#a4=
print(a3)
print(x1)
print(a4)
plot.subplot(211)
plot.plot(x1)
plot.subplot(212)
plot.plot(a2)
plot.show()
