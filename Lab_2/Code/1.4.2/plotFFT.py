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
    py.plot(t[0:50],data[0:50])


    py.title('$v_{sig} = %s MHz$' %i, fontsize=15, horizontalalignment='right', verticalalignment='baseline')

    py.xlabel('time ($\mu$s)')
    py.ylabel("Voltage (V)")
    py.ylim(-0.4,0.4)
    py.yticks(np.arange(-.4,.6,.2))
 

py.show()
