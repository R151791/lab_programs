import numpy as np
import matplotlib.pyplot as plot
n=np.arange(0,500,1)
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
h=[1/3 ,1/3 , 1/3]
n=input("enter length of x elements")
k=input("enter length of h elements")
x=[]
r=[]
h=[]
f=n+k-1
for i in range(n):
	a=input("enter elements for x")
	x.append(a)
print(x)
for i in range(k):
	b=input("enter elements for h")
	h.append(b)
print(h)
c=0
while k<f:
	h.append(0)
	k=k+1
c1=convolute(x,h)
p1=convolute(h,x)
p2=convolute(x,tr(x))
p3=convolute(x,tr(h))
plot.subplot(411)
plot.stem(c1)
plot.subplot(412)
plot.stem(p1)
plot.subplot(413)
plot.stem(p2)
plot.subplot(414)
plot.stem(p3)
plot.show()

