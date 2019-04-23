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
a1=[1,2,3,4,5,6,7,8]
N1=len(a1)
a2=dft(a1,N1)
w=5
x2=[]
for n in range(N1):
	v=a2[n-w]
	x2.append(v)
print(x2)
x3=[]
for n in range(N1):
	v=y[n+w]
	x3.append(v)
print(x3)
x4=[]
for i in range(N1):
	s=x2[i]+x3[i]
	x4.append(s)
print(x4)
x5=[]
for n in range(N1):
	a=np.cos(w*n)
	c=a1[n]*a
	x5.append(c)
print(x5)
g1=np.abs(x5)
g2=np.abs(x4)
h1=np.angle(x5)
h2=np.angle(x4)
plot.subplot(411)
plot.plot(g1)
plot.subplot(412)
plot.plot(g2)
plot.subplot(413)
plot.plot(h1)
plot.subplot(414)
plot.plot(h2)
plot.show()
