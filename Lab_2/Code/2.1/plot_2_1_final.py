#!/usr/bin/env python


import numpy as np
import numpy.fft as fft
import matplotlib.pyplot as plt

a=np.fromfile('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/2.2/adc_bram', dtype='>i4')

#b=np.genfromtxt('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/2.1/MixAnMinus')


### Regular wave profiles mixed and sampled ###

plt.plot(a)
plt.title('DSB Mixing with '+r'$\nu $ ' +'and'+ r' $1.05\%\nu$')
#plt.axis([0,100,-0.2,0.2])
#plt.show()

#plt.plot(b)
#plt.title('DSB Mixing with '+r'$\nu $ ' +'and'+ r' $0.95\%\nu$')
#plt.axis([0,100,-0.2,0.2])
#plt.show()

###############################################

#### Fourier Transform over previous data ####

plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)
#plt.subplot(2,1,1)
x=fft.fftfreq(16000,d=1./(4.e6))
plt.plot(fft.fftshift(x)/1.e3,fft.fftshift(np.abs(fft.fft(a))**2))
plt.title('DSB Mixing with '+r'$\nu_{lo} $ ' +'and'+ r' $\nu_{sig}=1.05 \times\ \nu_{lo}$',size=22)
plt.ylabel('Power '+r'$(V^{2})$',size=20)
plt.axvline(205, color='k', linestyle=':')
plt.axvline(-205, color='k', linestyle=':')
plt.axvline(5, color='k', linestyle=':')
plt.axvline(-5, color='k', linestyle=':')
#plt.axis([-400,400, 0.1 ,np.max(x)])
plt.yscale('log')

#plt.rc('xtick', labelsize=16)
#plt.rc('ytick', labelsize=16)
#plt.subplot(2,1,2)
#plt.plot(fft.fftshift(x)/1.e3,fft.fftshift(np.abs(fft.fft(b))**2), color='r')
#plt.title('DSB Mixing with '+r'$\nu_{lo} $ ' +'and'+ r' $\nu_{sig}=0.95 \times\ \nu_{lo}$',size=22)
#plt.ylabel('Power'+r'$(V^{2})$',size=20)
#plt.xlabel('Frequency (kHz)',size=20)
#plt.axvline(195, color='k', linestyle=':')
#plt.axvline(-195, color='k', linestyle=':')
#plt.axvline(5, color='k', linestyle=':')
#plt.axvline(-5, color='k', linestyle=':')
#plt.rc('ytick', labelsize=16)
#plt.axis([-400,400, 0.1 ,np.max(x)])
#plt.yscale('log')


plt.tight_layout()
plt.show()


