import numpy as np 
import pylab as py 
import matplotlib 

for i in range(1,10,1):
    index = float(i)/10
    filename = "%svsample_10MHz.npz" % index
    data = np.load(filename)['arr_0']
    N = np.load(filename)['arr_2']
    sampling = np.load(filename)['arr_1']
    py.subplot(3,3,i)
    t = sampling*np.arange(1./sampling, float(N+1)/sampling, 1./sampling)
    py.plot(np.fft.fftfreq(250)*10,np.abs(np.fft.fft(data[0:250]))**2)


    py.title('$v_{sig} = %s MHz$' %i, fontsize=15, horizontalalignment='right', verticalalignment='baseline')

    py.xlabel('Frequency (MHz)')
    py.ylabel("Intensity (ab. units)")
   
 

py.show()
