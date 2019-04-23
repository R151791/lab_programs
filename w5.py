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


'black man'
b=[]
for i in range(0,32):
	s=0.42-0.5*(np.cos((2*np.pi*i)/(m-1)))+0.08*(np.cos((4*np.pi*i)/(m-1)))
	b=np.append(b,s)


'sin*BM'
y1=[]
for i in range(0,min(len(si),len(b))):
	s=si[i]*b[i]
	y1=np.append(y1,s)
	
	
'dtft of BM'
bd=[]
bd=dtft(b)


'dtft of sin*BM'
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
plt.title('sinc*BM')
plt.subplot(234)
plt.stem(b)
plt.title('Bm')
plt.subplot(235)
plt.plot(np.abs(bd))
plt.title('dtft of BM')
plt.subplot(236)
plt.plot(np.abs(dy1))
plt.title('dtft of sinc*BM')
plt.show()

