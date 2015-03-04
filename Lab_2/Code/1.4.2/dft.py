import numpy as np 
import pylab as py 

def dft(filename,sampfreq):
    data = np.load(filename)['arr_0']
    N =len(data)
    delt = 1./sampfreq
    T = (N)*delt
    E_nu = []
    t = np.arange(-N/2,N/2,1)
    nu = np.arange(-sampfreq/2,sampfreq*(1-2./N)/2,sampfreq/(N))
    E_nu = []
    for n in nu:
        integr = 0 
        for i in t:
            integr += data[i+N/(2)]*np.exp(-2j*i*delt*np.pi*n)*delt
        E_nu.append(integr/(N*delt))    
    E_nu = np.abs(E_nu)**2
    return {'nu':nu,'E_nu':E_nu}

filename = '0.6vsample_10MHz.npz' 
data = dft(filename,1e7)
nu = data['nu']/1.0e6
E_nu = data['E_nu']
print E_nu
print len(E_nu)
py.plot(nu,E_nu)
py.show()
