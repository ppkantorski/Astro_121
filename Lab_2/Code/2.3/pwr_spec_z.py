#!/usr/bin/env python


import numpy as np
import numpy.fft as fft
import matplotlib.pyplot as plt


a = np.load('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/2.3/sine_cos.npz')

y1 = a['arr_2'] + 1j*a['arr_3']
#y2 = a['arr_3']


plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)
#plt.subplot(2,1,1)
x=fft.fftfreq(len(y1),d=1./(4.e6))
plt.plot(fft.fftshift(x)/2.e5,fft.fftshift(np.abs(fft.fft(y1))**2))
plt.title('Digital SSB Mixing',size=22)
plt.ylabel('Power '+r'$(V^{2})$',size=20)
plt.axvline(1.625, color='k', linestyle=':')
plt.axvline( -.375, color='k', linestyle=':')
#plt.axvline(0.5, color='k', linestyle=':')
#plt.axvline(-0.5, color='k', linestyle=':')
#plt.axis([-50, 50, 1e7 ,1.e13])
plt.xlabel('Frequency (MHz)',size=20)
plt.yscale('log')




plt.tight_layout()
plt.show()


