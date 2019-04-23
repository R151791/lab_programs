from matplotlib import pyplot as plt
import cmath as cm 
import numpy as np
x=input("Enter the samples:")
j=cm.sqrt(-1)
N=len(x)
y=[ ]
for k in range(0,N):
      sum=0
      for n in range(0,N):
            sum=sum+(x[n]*(np.exp((-j)*(2*np.pi/N)*n*k)))
      y=np.append(y,sum)
y1=np.zeros(8)
N=8
for k in range(0,N):
      sum=0
      for n in range(0,N):
            sum=sum+(x[n]*(np.exp((-j)*(2*np.pi/N)*n*k)))
      y1=np.append(y1,sum)
plt.subplot(121)
plt.stem(np.abs(y))
plt.title('4 point dft')
plt.subplot(122)
plt.stem(np.abs(y1))
plt.title('')
plt.show()