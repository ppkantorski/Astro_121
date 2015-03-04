#!/usr/bin/env python


import numpy as np
import numpy.fft as fft
import matplotlib.pyplot as plt


a = np.load('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/2.2/omb_02.npz')
b = np.load('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/2.2/omb_01.npz')

y1 = a['arr_4']
y2 = b['arr_4']

print a['arr_0']

plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)
plt.subplot(2,1,1)
x=fft.fftfreq(len(y2),d=1./(4.e6))
plt.plot(fft.fftshift(x)/2e6,fft.fftshift(np.abs(fft.fft(y2))**2))
plt.title('Digital DSB Mixing w/ '+r'$\nu_{lo} $ ' +'and'+ r' $\nu_{sig}=1.05 \times\ \nu_{lo}$',size=22)
plt.ylabel('Power '+r'$(V^{2})$',size=20)
plt.axvline(2.05, color='k', linestyle=':')
plt.axvline(-2.05, color='k', linestyle=':')
plt.axvline(0.05, color='k', linestyle=':')
plt.axvline(-0.05, color='k', linestyle=':')
plt.axis([-0.5, 0.5, 1e6 ,1.e13])
plt.yscale('log')

plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)
plt.subplot(2,1,2)
x=fft.fftfreq(len(y1),d=1./(4.e6))
plt.plot(fft.fftshift(x)/2e6,fft.fftshift(np.abs(fft.fft(y1))**2), color='r')
plt.title('Digital DSB Mixing w/ '+r'$\nu_{lo} $ ' +'and'+ r' $\nu_{sig}=0.95 \times\ \nu_{lo}$',size=22)
plt.ylabel('Power '+r'$(V^{2})$',size=20)
plt.axvline(1.95, color='k', linestyle=':')
plt.axvline(-1.95, color='k', linestyle=':')
plt.axvline(0.05, color='k', linestyle=':')
plt.axvline(-0.05, color='k', linestyle=':')
plt.axis([-0.5, 0.5, 1e6 ,1.e13])
plt.xlabel('Frequency (MHz)',size=20)
#plt.xlabel('Frequency (MHz)',size=20)
plt.yscale('log')




plt.tight_layout()
plt.show()


