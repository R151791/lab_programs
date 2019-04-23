import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
ds=0.1
dp=0.6
t=0.1
ws=1.099
wp=2.198

'--------------analog frequency---------------'

us1=(2/t)*np.tan(ws/2)
up1=(2/t)*np.tan(wp/2)
up=1
us=up1/us1
print "up=",up
print "us=",us

'---------------order-----------------'

a=1/(ds**2)-1
b=(1/(dp**2))-1
c=np.sqrt(a/b)
d=us/up
n=(np.log10(c))/(np.log10(d))
n1=np.ceil(n)
print "ORDER=",n1
	
'-----------------cut off frequency----------'

t1=(1.0/(2.0*n1))
t2=((1.0/ds**2)-1)
t3=t2**t1
uc=us/t3
print "cut off frequency=",uc

'-----------------transfer function-----------'
j=cm.sqrt(-1)
k=n1/2
print(k)
v1=((2*k)-1)*np.pi
print(v1)
v2=2*n1
bk=2*np.sin(v1/v2)
print(bk)
w=np.arange(0,np.pi,0.00001)
z=np.exp((-j)*w)
s1=(2/t)*((1-z**(-1))/(1+z**(-1)))
s=up1/s1
y=(uc**2)/((s**2)+(bk*s*uc)+(uc**2))
plt.plot(w,np.abs(y))
plt.show()
