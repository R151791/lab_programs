import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
m=input('Enter no.of samples:')
'sinc function'
y=[]
i=np.arange(-100,100,1)
s=0.25*np.sinc(i/4.0)
y=np.append(y,s)
k=np.arange(-17,17,1)
s=0.25*np.sinc(k/4.0)
si=[]
si=np.append(si,s)
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
'dtft of sinc function'
y1=[]
y1=dtft(y)
'rectangular function'
y2=[]
for i in range(0,m):
	y2=np.append(y2,1)
'multiplication of sinc and rect'
y3=[]
for j in range(0,min(len(si),len(y2))):
	s=si[j]*y2[j]
	y3=np.append(y3,s)
'dtft of rect'
y4=dtft(y2)
'dtft of rect and sin'
y5=dtft(y3)
'plots'
plt.subplot(321)
plt.stem(y)
plt.title('sinc')
plt.subplot(322)
plt.plot(np.abs(y1))
plt.title('dtft of sinc')
plt.subplot(323)
plt.stem(y3)
plt.title('mul of sinc and rect')
plt.subplot(324)
plt.plot(y4)
plt.title('dtft of rect')
plt.subplot(325)
plt.stem(y2)
plt.title('rect')
plt.subplot(326)
plt.plot(np.abs(y5))
plt.title('dtft of rect*sin')
plt.show()
