#!/usr/bin/env python



import numpy as np
import numpy.fft as fft
import matplotlib.pyplot as plt

d1 = np.load('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/2.2/omb_01.npz')
d2 = np.load('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/2.2/omb_02.npz')

a = d1['arr_4']
b = d2['arr_4']


#### Fourier Transform over previous data ####

plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)
plt.subplot(2,1,1)

y1 = fft.fft(a)

x=fft.fftfreq(len(y1), d = 1./(4.e6))


for i in range(len(y1)):
    if abs(x[i]) > 50000:
        y1[i] = 0 + 0j

y2 = fft.fft(b)

for i in range(len(y2)):
    if abs(x[i]) > 50000:
        y2[i] = 0 + 0j

plt.plot(fft.fftshift(x)/4.e6, np.fft.ifft(y1))
plt.title('Filtered Mixed '+r' $\nu_{sig}=105$'+'kHz Signal',size=22)
plt.ylabel('Voltage (V)',size=20)
#plt.axis([-1,1, -.1 ,.1])

plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)
plt.subplot(2,1,2)
plt.plot(fft.fftshift(x)/4.e6,np.fft.ifft(y2), color='r')
plt.title('Filtered Mixed '+r' $\nu_{sig}=95$'+'kHz Signal',size=22)
plt.ylabel('Voltage (V)',size=20)
plt.xlabel('Time (ms)',size=20)
#plt.axis([-1,1, -.1 , .1])



plt.tight_layout()
plt.show()


