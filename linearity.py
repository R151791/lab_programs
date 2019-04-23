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
x1=[1,2,3,4,5,6,7,8]
N1=len(x1)
x2=[4,5,6,3,4,5,2,3]
N2=len(x2)
a1=dft(x1,N1)
a2=dft(x2,N2)
a3=a1+a2
x3=[]
for i in range(N1):
	s=x1[i]+x2[i]
	x3.append(s)
print(x3)
a4=dft(x3,N1)
g3=np.abs(a3)
g4=np.abs(a4)
plot.subplot(211)
plot.plot(g3)
plot.subplot(212)
plot.plot(g4)
plot.show()
