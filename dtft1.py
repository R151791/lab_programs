import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
def dtft(x):
      j=cm.sqrt(-1)
      w=np.linspace(-np.pi,np.pi,100)
      y=[ ]
      for i in range(0,100):
            sum=0
            for n in range(0,len(x)):
                  sum=sum+(x[n]*np.exp((-j)*w[i]*n))
            y=np.append(y,sum)
      return y
wc=np.pi/4
y=[]
s=wc/np.pi
y=np.append(y,s)
for i in range(1,1000):
	s=np.sin(wc*i)/(np.pi*i)
	y=np.append(y,s)
x=dtft(y)
plt.plot(x)
plt.show()
