import numpy as np 
import pylab as py 

for ind in range(1,10,1):
    index = float(ind)/10
    filename = "%svsample_10MHz.npz" % index
    data = np.load(filename)['arr_0']
    sampfreq = np.load(filename)['arr_1']
    N =len(data)
    length = len(data)
    delt = 1./sampfreq
    t = np.arange(-length/2,length/2,1)
    nu = np.arange(-sampfreq/2,sampfreq*(1-2./length)/2,sampfreq/N)
    E_nu = []
    for n in nu:
        integr = 0 
        for i in t:
            integr += data[i+length/(2)]*np.exp(-2j*i*delt*np.pi*n)*delt
        E_nu.append(integr/(N*delt)) 
    py.subplot(3,3,ind)
    py.plot(nu/(1e6),np.abs(E_nu)**2)
    py.title('$v_{sig} = %s MHz$' %ind, fontsize=15, horizontalalignment='right', verticalalignment='baseline')
    py.xlabel('Frequency (Hz)')
    py.ylabel("Intensity (ab. units)")
py.show()
