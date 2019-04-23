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

'--------------order----------------------------'

a=1/(ds**2)-1
b=(1/(dp**2))-1
c=np.sqrt(a/b)
d=us/up
n=np.arccosh(c)/np.arccosh(d)
N=np.ceil(n)
print "Order=",N

'-----------------epsilon-------------'

i=-2
e=np.sqrt((dp**i)-1)
print "E=",e

'------------------transfer function----------------'

a=1/n
x=np.sqrt((1+(1/e**2)))+(1/e)
yn=0.5*((x**a)-(x**(-a)))
print "Yn=",yn
k=N/2
v1=((2*k)-1)*np.pi
v2=2*N
bk=yn*2*np.sin(v1/v2)
print "bk=",bk
ck=(yn**2)+((np.cos(v1/v2))**2)
print "ck=",ck
j=cm.sqrt(-1)
w=np.arange(0,np.pi,0.001)
z=np.exp((-j)*w)
s1=(2/t)*((1-z**(-1))/(1+z**(-1)))
s=up1/s1
k=1/np.sqrt(1+(e**2))
y=(ck*k*(up**2))/((s**2)+(bk*s*up)+(ck*up**2))
plt.plot(w,np.abs(y))
plt.show()
