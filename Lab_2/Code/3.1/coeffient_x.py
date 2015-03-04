import numpy as np 
from numpy.fft import *
from matplotlib import pyplot as plt
from numpy.fft import *

######### Creating Coefficients ##########
# By: Caleb

N = 8
Window = 5 # Centered window

print 'Generating Coeffs:'
print
Fir = np.zeros(N)
print Fir
print
Fir[N/2+1:N/2+1+(Window-1)/2] = 1.0
print Fir
print
Fir[N/2-(Window-1)/2:N/2+1] = 1.0
print Fir
print

FirShift = fftshift(Fir)
print 'Fir Shift: ', FirShift
print
FirPhys = ifft(FirShift)
print 'Fir Phys: ', FirPhys
print

FirCoeffs = ifftshift(FirPhys)
print 'Fir Coeffs Shift: ', FirCoeffs
print
FirCoeffs = np.real(FirCoeffs)
print 'Fir Real: ', FirCoeffs

# Demonstration of "padding with zeros# to achieve higer resolution
N_Extend = 2048 # Making better Frequency Resolution by appendind 2048 zeros to original array 
FirEx = np.zeros(N_Extend) # 2048 so that it will have the same len of noise data (from Roach)
FirEx[(N_Extend/2)-4:(N_Extend/2)+4] = FirCoeffs

FirShiftEx = fftshift(FirEx)
FirPhysEx = fft(FirShiftEx)

FirCoeffsEx = fftshift(FirPhysEx)
FirCoeffsEx = np.real(FirCoeffsEx)

############### End ##################

####### Working Noise Data ########

ImagData = np.fromfile('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/3.1/ddc_imag_bram','>i4')
RealData = np.fromfile('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/3.1/ddc_real_bram','>i4')

#ExpData = RealData + 1j*ImagData
ExpData = RealData 
FourData = fftshift(fft(ExpData))
FourData = abs(FourData)

FreqAx = fftfreq(2048,d=1./(200e0))

############# End ################

####### Plots #######

#plt.subplot(1,2,1)
#plt.plot(fftshift(FreqAx),FourData, label='Filter Output Shape') # Plot from Noise Source

plt.plot((np.arange(2048)/2048.0)*2e2-1e2,(abs(FirCoeffsEx)**2)*10e7, 'k-', linewidth=2, linestyle=':') # Plot from Coeff.'s

plt.title('Predicted Response',size=26)
plt.xlabel('Frequency (MHz)',size=22)
plt.ylabel('Power '+r'$(V)^{2}$',size=22)

plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)



plt.tight_layout()
plt.show()
