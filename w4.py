import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
m=input('Enter no.of samples:')
def dtft(x):
      j=cm.sqrt(-1)
      w=np.linspace(-np.pi,np.pi,10000)
      y=[ ]
      for i in range(0,10000):
            sum=0
            for n in range(0,len(x)):
                  sum=sum+(x[n]*np.exp((-j)*w[i]*n))
            y=np.append(y,sum)
      return y
'sinc function'
y=[]
i=np.arange(-100,100,1)
s=0.25*np.sinc(i/4.0)
y=np.append(y,s)
k=np.arange(-17,17,1)
s=0.25*np.sinc(k/4.0)
si=[]
si=np.append(si,s)
'dtft of sinc'
dy=[]
dy=dtft(y)
'hamming function'
h=[]
for i in range(0,32):
	s=0.5-(0.46*np.cos((2*np.pi*i)/(m-1)))
	h=np.append(h,s)
'sin*ham'
y1=[]
for i in range(0,min(len(si),len(h))):
	s=si[i]*h[i]
	y1=np.append(y1,s)
'dtft of ham'
dh=[]
dh=dtft(h)
'dtft of sin*ham'
dy1=[]
dy1=dtft(y1)
'plots'
plt.subplot(231)
plt.stem(y)
plt.title('sinc')
plt.subplot(232)
plt.plot(np.abs(dy))
plt.title('dtft of sinc')
plt.subplot(233)
plt.stem(y1)
plt.title('sinc*ham')
plt.subplot(234)
plt.stem(h)
plt.title('ham')
plt.subplot(235)
plt.plot(np.abs(dh))
plt.title('dtft of ham')
plt.subplot(236)
plt.plot(np.abs(dy1))
plt.title('dtft of sinc*ham')
plt.show()

