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
k=input("enter shift value")
x1=[1,2,3,4,5,6,7,8]
N1=len(x1)
s=dft(x1,N1)
print(s)
x2=[]
for n in range(N1):
	v=x1[n-k]
	x2.append(v)
N2=len(x2)
print(x2)
a2=dft(x2,N2)
print(a2)
j=cm.sqrt(-1)
b=[]
for k in range(N1):
	b1=np.exp((-(j*2*np.pi*k/N1)))
	b.append(b1)
print(b)
b2=[]
for i in range(N1-1):
	s=b[i]*a2[i]
	b2.append(b1)
print(b2)
h3=np.abs(b2)
h4=np.abs(x2)
plot.subplot(211)
plot.plot(h3)
plot.subplot(212)
plot.plot(h4)
plot.show()


