#! /usr/bin/env python
import numpy as np
from matplotlib import pyplot as plt
from numpy.fft import *
#import radiolab

# Freq_input = 1 Mhz and -10 dBm

# lo_freq = 8

ImagData = np.fromfile('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/3.1/ddc_imag_bram','>i4')
RealData = np.fromfile('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/3.1/ddc_real_bram','>i4')

ExpData = RealData + 1j*ImagData
FourData = fftshift(fft(ExpData))
FourData = abs(FourData)


x_axis = fftfreq(2048, d=1./(200.e0))

plt.subplot(1,2,1)
plt.plot(fftshift(x_axis),FourData)

plt.title('FIR Filter Response',size=26)
plt.xlabel('Frequency (MHz)',size=22)
plt.ylabel('Power '+r'$(V)^{2}$',size=22)

plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)


plt.subplot(1,2,2)
plt.plot(fftshift(x_axis),FourData)

plt.title('FIR Filter Response',size=26)
plt.xlabel('Frequency (MHz)',size=22)
plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)


plt.yscale('log')

plt.tight_layout()
plt.show()
