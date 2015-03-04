#!/usr/bin/env python



import numpy as np
import numpy.fft as fft
import matplotlib.pyplot as plt

a=np.genfromtxt('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/2.1/MixAnPlus')

b=np.genfromtxt('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/2.1/MixAnMinus')




plt.plot(a)
plt.title('DSB Mixing with '+r'$\nu $ ' +'and'+ r' $1.05\%\nu$')
#plt.axis([0,100,-0.2,0.2])
#plt.show()

plt.plot(b)
plt.title('DSB Mixing with '+r'$\nu $ ' +'and'+ r' $0.95\%\nu$')
#plt.axis([0,100,-0.2,0.2])
#plt.show()

###############################################

#### Fourier Transform over previous data ####

plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)
plt.subplot(2,1,1)

x=fft.fftfreq(16000, d = 1./(4.e6))

y1 = fft.fft(a)

for i in range(100,15900):
        y1[i] = 0

y2 = fft.fft(b)

for i in range(100,15900):
        y2[i] = 0

plt.plot(fft.fftshift(x)/1.e6, np.fft.ifft(y1))
plt.title('Filtered Mixed '+r' $\nu_{sig}=105$'+'kHz Signal',size=22)
plt.ylabel('Voltage (V)',size=20)
plt.axis([-1,1, -.1 ,.1])

plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)
plt.subplot(2,1,2)
plt.plot(fft.fftshift(x)/1.e6,np.fft.ifft(y2), color='r')
plt.title('Filtered Mixed '+r' $\nu_{sig}=95$'+'kHz Signal',size=22)
plt.ylabel('Voltage (V)',size=20)
plt.xlabel('Time (ms)',size=20)
plt.axis([-1,1, -.1 , .1])



plt.tight_layout()
plt.show()


