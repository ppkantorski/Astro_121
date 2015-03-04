#!/usr/bin/env python

# ========================================================================== #
# File: plot_samples.py                                                      #
# Programmer: Patrick Kantorski                                              #
# Date: 03/08/14                                                             #
# Class: Astronomy 121 - Radio Astronomy Lab                                 #
# Time: T 6:00-9:00 PM                                                       #
# Instructor: Aaron Parsons                                                  #
# Description: This program was written in Python to treat data taken from   #
#              an interferometer at UC Berkeley.                             #                                    #
# ========================================================================== #

import numpy as np
import numpy.fft as fft
import matplotlib.pyplot as plt
import scipy.constants as spc
import scipy.optimize as optimize
import os

def main():
    print("=====================================================================")
    
    path = raw_input("\nPlease enter object or path: ")
    d_type = 'other'
    index = []
    value = 0
    
    # Preset objects for examination...
    if path == 'moon':
        print('Using collected moon data...')
        path = '/Users/ppkantorski/Documents/Radio_Astronomy/Lab_3/Data/04_05_14/data/data_moon_140404.npz'
        d_type = 'moon'
        

        file = np.load(path)
        x = file['jd'] * 24 * 3600
        
        print(x[0]/3600/24)
        print(x[len(x)-1]/3600/24)
        
        x = x - x[0]
        y = file['volts']
        dec = file['dec']
        x_fit = np.sin((file['lst']-file['ra'])*np.pi/12)
        
        y_mean = average(x, y)
        y_avg = y[100: -100] - y_mean
        
        for i in range(y_avg.size):
            if i == len(y_avg):
                break
            if y_avg[i] < -0.00039:
                index.append(i+100)
            if y_avg[i] > 0.00039:
                index.append(i+100)

        x = np.delete(x, index)
        y = np.delete(y, index)
        dec = np.delete(dec, index)
        x_fit = np.delete(x_fit, index)

        
    elif path == 'sun':
        print('Using collected sun data...')
        path = '/Users/ppkantorski/Documents/Radio_Astronomy/Lab_3/Data/04_05_14/data/data_sunrain_140401.npz'
        d_type = 'sun'
        
        file = np.load(path)
        x = file['jd'] * 24 * 3600
        
        print(x[0]/3600/24)
        print(x[len(x)-1]/3600/24)
        
        x = x - x[0]
        y = file['volts']
        dec = file['dec']
        x_fit = np.sin((file['lst']-file['ra'])*np.pi/12)
        
        for i in range(y.size):
            if i == len(y):
                break
            #if y[i] < -0.01000:
            #    index.append(i)

        x = np.delete(x, index)
        y = np.delete(y, index)
        dec = np.delete(dec, index)
        x_fit = np.delete(x_fit, index)

        
    elif path == 'orion':
        print('Using collected orion data...')
        path_1 = '/Users/ppkantorski/Documents/Radio_Astronomy/Lab_3/Data/04_05_14/data/data_orion_140321.npz'
        path_2 = '/Users/ppkantorski/Documents/Radio_Astronomy/Lab_3/Data/04_05_14/data/data_orion_140321_2.npz'
        d_type = 'orion'
        
        file_1 = np.load(path_1)
        file_2 = np.load(path_2)
        
        ra = 5.588138889
        dec = -5.391111111
        
        x_1 = file_1['jd']
        y_1 = file_1['volts']
        x_fit_1 = np.sin((file_1['lst']-ra)*np.pi/12)
        dec_1 = file_1['dec']

        x_2 = file_2['jd']
        y_2 = file_2['volts']
        x_fit_2 = np.sin((file_2['lst']-ra)*np.pi/12)
        dec_2 = file_2['dec']
        
        #dec = np.r_[dec_1, dec_2]
        x_fit = np.r_[x_fit_1, x_fit_2]
        
        x = np.r_[x_1, x_2] * 24 * 3600
        
        print(x[0]/3600/24)
        print(x[len(x)-1]/3600/24)
        
        x = x - x[0]
        y = np.r_[y_1, y_2]
        
        # Cutting points out of original data...
        #for i in range(y.size):
        #    if i == len(y):
        #        break
        #    if y[i] < -0.00105:
        #        index.append(i)

        
        y_mean = average(x, y)
        y_avg = y[100: -100] - y_mean
        
        for i in range(y_avg.size):
            if i == len(y_avg):
                break
            if y_avg[i] < -0.00024:
                index.append(i+100)
            if y_avg[i] > 0.00024:
                index.append(i+100)
            # Commented out stuff was used to make better curvefit!
            #if x[i] > 2300 and x[i] < 2303:
            #    print("low"+str(i))
            #if x[i] > 5000 and x[i] < 5003:
            #    print("high"+str(i))
            if x[i] > 7270 and x[i] < 7340:
                if y[i] < -0.00064:
                    index.append(i)
        

        x = np.delete(x, index)
        y = np.delete(y, index)
        #dec = np.delete(dec, index)
        x_fit = np.delete(x_fit, index)

        
    elif path == 'virgo':
        print('Using collected virgo data...')
        path = '/Users/ppkantorski/Documents/Radio_Astronomy/Lab_3/Data/04_05_14/data/data_virgoA_140402.npz'
        d_type = 'virgo'
        
        file = np.load(path)
        
        ra = 12.51372861
        dec = 12.39112222
        
        x = file['jd'] * 24 * 3600
        
        print(x[0]/3600/24)
        print(x[len(x)-1]/3600/24)
        
        x = x - x[0]
        y = file['volts']
        #dec = file['dec']
        x_fit = np.sin((file['lst']-ra)*np.pi/12)
        
        y_mean = average(x, y)
        y_avg = y[100: -100] - y_mean
        
        #print(len(y_avg))
        #print(len(y))
        
        for i in range(y_avg.size):
            if i == len(y_avg):
                break
            if x[i] > 40200:
                break
            if y_avg[i] < -0.0003:
                index.append(i+100)
            if y_avg[i] > 0.0003:
                index.append(i+100)
                #print("y_avg index "+str(i+100))
                #print(x[i+100])
            #if y[i] < -0.0019:
                #index.append(i)
            #    print('\n')
                #print("y index "+str(i))
                #print(x[i])
                
            # Commented out stuff was used to make better curvefit!
            if x[i] > 17000 and x[i] < 17003:
                print("low"+str(i))
            if x[i] > 40000 and x[i] < 40003:
                print("high"+str(i))
        
        #print(index)
        #print y_avg

        x = np.delete(x, index)
        y = np.delete(y, index)
        #dec = np.delete(dec, index)
        x_fit = np.delete(x_fit, index)

    
    elif path == 'M17':
        print('Using collected M17 data...')
        path = '/Users/ppkantorski/Documents/Radio_Astronomy/Lab_3/Data/04_05_14/data/data_M17_140405.npz'
        d_type = 'M17'
        
        file = np.load(path)
        
        # RA and DEC for M17
        ra = 18.34055556
        dec = -16.17666667
        
        x = file['jd'] * 24 * 3600
        
        print(x[0]/3600/24)
        print(x[len(x)-1]/3600/24)
        
        x = x - x[0]
        y = file['volts']
        #dec = file['dec']
        x_fit = np.sin((file['lst']-ra)*np.pi/12)
        
        y_mean = average(x, y)
        y_avg = y[100: -100] - y_mean
        
        #print(len(y_avg))
        #print(len(y))
        
        for i in range(y_avg.size):
            if i == len(y_avg):
                break
            if y_avg[i] < -0.0003:
                index.append(i+100)
            if y_avg[i] > 0.0003:
                index.append(i+100)
                
            # Commented out stuff was used to make better curvefit!
            #if x[i] > 3500 and x[i] < 3503:
            #    print("low"+str(i))
            #if x[i] > 5500 and x[i] < 5503:
            #    print("high"+str(i))
                
                #print("y_avg index "+str(i+100))
                #print(x[i+100])
            #if y[i] < -0.0019:
                #index.append(i)
            #    print('\n')
                #print("y index "+str(i))
                #print(x[i])
        
        #print(index)
        #print y_avg

        x = np.delete(x, index)
        y = np.delete(y, index)
        #dec = np.delete(dec, index)
        x_fit = np.delete(x_fit, index)

    
    else:
        d_type = "other"
        print('Using collected data...')
        file = np.load(path)
        x = file['jd'] * 24 * 3600
        
        print(x[0]/3600/24)
        print(x[len(x)-1]/3600/24)
        
        x = x - x[0]
        y = file['volts']
        dec = file['dec']
        x_fit = np.sin((file['lst']-file['ra'])*np.pi/12)
        
        #gen_graph(x, y, d_type)
        #cutoff = float(raw_input("\nEnter a Voltage Cutoff: "))
        #for i in range(y.size):
        #    if i == len(y):
        #        break
        #    if y[i] < cutoff:
        #        index.append(i)

        x = np.delete(x, index)
        y = np.delete(y, index)
        dec = np.delete(dec, index)
        x_fit = np.delete(x_fit, index)

    # Generate Graphs
    plot = raw_input("\nPlot smoothed data and power spectrum? (y/n): ")
    while plot != 'y' and plot != 'Y' and plot != 'N' and plot != 'n': 
		plot = raw_input("Please enter (y/n): ")
    if plot == 'Y' or plot == 'y':
        gen_graph(x, y, x_fit, dec, d_type)
        print('\n')
    elif plot == 'N' or plot == 'n':
	    pass

    # Curve Fitting Graph... 
    plot = raw_input("Plot curve fitted data? (y/n): ")
    while plot != 'y' and plot != 'Y' and plot != 'N' and plot != 'n': 
        plot = raw_input("Please enter (y/n): ")
    if plot == 'Y' or plot == 'y':
        if d_type == 'sun' or d_type == 'moon' or d_type == 'other':
            x_data = envelope(x, y, x_fit, dec, d_type)[0]
            y_data = envelope(x, y, x_fit, dec, d_type)[1]
            x_fit = envelope(x, y, x_fit, dec, d_type)[2]
            dec_data = envelope(x, y, x_fit, dec, d_type)[3]
            poly_fit(x_data, y_data, x_fit, dec_data, d_type)
            print('\n')
        elif d_type == 'orion':
            
            # Radius of mean must be truncated.
            y_mean = average(x, y)
            r_1 = 100
            
            # Average again
            #y_mean = average(x[r_1:-r_1], y_mean)
            #r_2 = 100
            r_tot = r_1 #+ r_2
            
            curve_fit(x[r_tot: -r_tot], y[r_tot: -r_tot] - y_mean, x_fit[r_tot: -r_tot], dec, d_type)
            print('\n')
        else:
            y_mean = average(x, y)
            curve_fit(x[100: -100], y[100: -100] - y_mean, x_fit[100:-100], dec, d_type)
            print('\n')
            
    elif plot == 'N' or plot == 'n':
        pass
    
    # Re-execute program.
    print("\n=====================================================================")
    again = raw_input("Run clean_data.py again? (y/n): ")
    while again != 'y' and again != 'Y' and again != 'N' and again != 'n': 
        again = raw_input("Please enter (y/n): ")
    if again == 'Y' or again == 'y':
        print('\n')
        os.system("/Users/ppkantorski/Documents/Radio_Astronomy/Lab_3/Code/clean_data.py")
    elif again == 'N' or again == 'n':
        print('\nAll process are complete!')




def gen_graph(x_data, y_data, x_fit, dec, d_type):
    
    n = 1
    while n < 4:
        plt.subplot(3, 1, n)
        if n == 1:
            avg_graph(x_data, y_data)
        if n == 2:
            smooth_graph(x_data, y_data, d_type)
        if n == 3:
            pwr_spectrum(x_data, y_data)
        n += 1
        
    plt.rc('xtick', labelsize=12)
    plt.rc('ytick', labelsize=12)
    
    plt.tight_layout()
    plt.show()    




# Box car averaging...
def average(x_data, y_data):
    radius = 100
    n = 100
    y_mean = np.array([])
    for i in y_data[radius: -radius]:
        y_mean = np.append(y_mean, np.mean(y_data[n-radius:n+radius]))
        n = n + 1
    
    return y_mean


def avg_graph(x_data, y_data):
    radius = 100
    n = 100
    y_mean = average(x_data, y_data)
    
    plt.plot(x_data, y_data, linewidth=1, color='b')
    plt.plot(x_data[radius: -radius], y_mean, linewidth=2, color='r')
    #plt.axis([0,.5,-2e6,2e6])
    plt.xlabel('Time (s)', fontsize=20)
    plt.ylabel('Power '+r'$(V)$', fontsize=20)
    #plt.title('Digital Mixing with'+ r' $\nu_{sig}=1.05 \times\ \nu_{lo}$' ,size=22)


def smooth_graph(x_data, y_data, d_type):
    
    if d_type == "sun":
        space = 10
    elif d_type == "moon":
        space = 100
    else:
        space = 10
    
    radius = 100
    n = 100
    y_mean = average(x_data, y_data)
    y_data = y_data[radius: -radius] - y_mean
    x_data = x_data[radius: -radius]
    
    plt.plot(x_data, y_data, linewidth=1, color='g')
    
    #print(len(x_data))
    #print(len(y_data))
    
    
    if d_type == 'sun':
        # Envelope Detector.
        index = []
        y_deriv = np.diff(y_data)
    
        for i in range(y_deriv.size):

            if abs(y_deriv[i]) > 0.00010:
                index.append(i)
            
        y_data = abs(np.delete(y_data, index))
        x_data = np.delete(x_data, index)
        
        # Physically remove bad datapoints.
        index = []
        for i in range(y_data.size):
            if i == len(y_data):
                break
            if x_data[i] > 3326 and x_data[i] < 3373:
                index.append(i)
            if x_data[i] > 6732 and x_data[i] < 6778:
                index.append(i)
            if x_data[i] > 10130 and x_data[i] < 10180:
                index.append(i)
            if x_data[i] > 16947 and x_data[i] < 16989:
                index.append(i)
            if x_data[i] > 20342 and x_data[i] < 20389:
                index.append(i)
            if x_data[i] > 23750 and x_data[i] < 23798:
                index.append(i)
            if x_data[i] > 27158 and x_data[i] < 27208:
                index.append(i)
            #if abs(y_data[i] -y_data[i-1]) >
            #    index = []
            #    index.append(i)
                
            #    y_data = np.delete(y_data, index)
            #    x_data = np.delete(x_data, index)
        
        y_data = np.delete(y_data, index)
        x_data = np.delete(x_data, index)
        
        # Plot points.
        #plt.plot(x_data, y_data, '.', linewidth=1, color='r')
    
        # Average curve.
        y_mean_2 = np.array([])
    
        n = space
        for i in y_data[space: -space]:
            y_mean_2 = np.append(y_mean_2, np.mean(y_data[n-space:n+space]))
            n = n + 1
    
        #print(len(x_data))
        #print(len(y_mean_2))

        plt.plot(x_data[space: -space], y_mean_2, linewidth=2, color='k')
        plt.xlabel('Time (s)', fontsize=20)
        plt.ylabel('Power '+r'$(V)$', fontsize=20)


    elif d_type == 'moon':
        # Envelope Detector.
        index = []
        y_deriv = np.diff(y_data)
    
        #for i in range(y_deriv.size):

         #   if abs(y_deriv[i]) > 0.00007:
         #       index.append(i)
            
        #y_data = abs(np.delete(y_data, index))
        #x_data = np.delete(x_data, index)
        
        index = []
        
        for i in range(y_data.size):
            if i == len(y_data):
                break
            if y_data[i] < 0.0000001:
                index.append(i)
                
            #    y_data = np.delete(y_data, index)
            #    x_data = np.delete(x_data, index)
        
        y_data = np.delete(y_data, index)
        x_data = np.delete(x_data, index)
    
        #plt.plot(x_data, y_data, '.', linewidth=1, color='r')
    
        # Average curve.
        y_mean_2 = np.array([])
    
        n = space
        for i in y_data[space: -space]:
            y_mean_2 = np.append(y_mean_2, np.mean(y_data[n-space:n+space]))
            n = n + 1
        
        # Used 2.7 to scale data fit...
        plt.plot(x_data[space: -space], 2.7*y_mean_2, linewidth=2, color='k')
        plt.xlabel('Time (s)', fontsize=20)
        plt.ylabel('Power '+r'$(V)$', fontsize=20)


    elif d_type == 'other':
        # Envelope Detector.
        index = []
        y_deriv = np.diff(y_data)
    
        for i in range(y_deriv.size):

            if abs(y_deriv[i]) > 0.00010:
                index.append(i)
            
        y_data = abs(np.delete(y_data, index))
        x_data = np.delete(x_data, index)
        
        index = []
        
        for i in range(y_data.size):
            if i == len(y_data):
                break
            #if abs(y_data[i] -y_data[i-1]) >
            #    index = []
            #    index.append(i)
                
            #    y_data = np.delete(y_data, index)
            #    x_data = np.delete(x_data, index)
        
        #y_data = np.delete(y_data, index)
        #x_data = np.delete(x_data, index)
    
        #plt.plot(x_data, y_data, '.', linewidth=1, color='r')
    
    
        # Average curve.
        y_mean_2 = np.array([])
    
        n = space
        for i in y_data[space: -space]:
            y_mean_2 = np.append(y_mean_2, np.mean(y_data[n-space:n+space]))
            n = n + 1

        plt.plot(x_data[space: -space], y_mean_2, linewidth=2, color='k')
        plt.xlabel('Time (s)', fontsize=20)
        plt.ylabel('Power '+r'$(V)$', fontsize=20)
        
    #plt.plot(x_data, y_data, linewidth=2, color='r')
#    plt.axis([0,.5,-2e6,2e6])
    plt.xlabel('Time (s)', fontsize=20)
    plt.ylabel('Power '+r'$(V)$', fontsize=20)
    # plt.title('Real and Imaginary SSB' ,size=22)




# Returns envelope!!
def envelope(x_data, y_data, x_fit, dec, d_type):
    
    if d_type == "sun":
        space = 10
    elif d_type == "moon":
        space = 100
    else:
        space = 10
    
    radius = 100
    n = 100
    y_mean = average(x_data, y_data)
    y_data = y_data[radius: -radius] - y_mean
    x_data = x_data[radius: -radius]
    x_fit = x_fit[radius: -radius]
    dec = dec[radius: -radius]
    
    
    if d_type == 'sun':
        # Envelope Detector.
        index = []
        y_deriv = np.diff(y_data)
    
        for i in range(y_deriv.size):

            if abs(y_deriv[i]) > 0.00010:
                index.append(i)
            
        y_data = abs(np.delete(y_data, index))
        x_data = np.delete(x_data, index)
        x_fit = np.delete(x_fit, index)
        dec = np.delete(dec, index)
            
        index = []
        for i in range(y_data.size):
            if i == len(y_data):
                break
            if x_data[i] > 3326 and x_data[i] < 3373:
                index.append(i)
            if x_data[i] > 6732 and x_data[i] < 6778:
                index.append(i)
            if x_data[i] > 10130 and x_data[i] < 10180:
                index.append(i)
            if x_data[i] > 16947 and x_data[i] < 16989:
                index.append(i)
            if x_data[i] > 20342 and x_data[i] < 20389:
                index.append(i)
            if x_data[i] > 23750 and x_data[i] < 23798:
                index.append(i)
            if x_data[i] > 27158 and x_data[i] < 27208:
                index.append(i)
        
        y_data = np.delete(y_data, index)
        x_data = np.delete(x_data, index)
        x_fit = np.delete(x_fit, index)
        dec = np.delete(dec, index)
        
    
        # Average curve.
        y_mean_2 = np.array([])
    
        n = space
        for i in y_data[space: -space]:
            y_mean_2 = np.append(y_mean_2, np.mean(y_data[n-space:n+space]))
            n = n + 1

        return x_data[space: -space], y_mean_2, x_fit[space:-space], dec[space:-space]


    elif d_type == 'moon':
        # Envelope Detector.
        index = []
        y_deriv = np.diff(y_data)
        
        for i in range(y_data.size):
            if i == len(y_data):
                break
            if y_data[i] < 0.0000001:
                index.append(i)
                
            #    y_data = np.delete(y_data, index)
            #    x_data = np.delete(x_data, index)
        
        y_data = np.delete(y_data, index)
        x_data = np.delete(x_data, index)
        x_fit = np.delete(x_fit, index)
        dec = np.delete(dec, index)
    
        # Average curve.
        y_mean_2 = np.array([])
    
        n = space
        for i in y_data[space: -space]:
            y_mean_2 = np.append(y_mean_2, np.mean(y_data[n-space:n+space]))
            n = n + 1
            
        return x_data[space: -space], 2.7*y_mean_2, x_fit[space:-space], dec[space:-space]


    elif d_type == 'other':
        # Envelope Detector.
        index = []
        y_deriv = np.diff(y_data)
    
        for i in range(y_deriv.size):

            if abs(y_deriv[i]) > 0.00010:
                index.append(i)
            
        y_data = abs(np.delete(y_data, index))
        x_data = np.delete(x_data, index)
        x_fit = np.delete(x_fit, index)
        dec = np.delete(dec, index)
        
        index = []
        
        for i in range(y_data.size):
            if i == len(y_data):
                break
    
        # Average curve.
        y_mean_2 = np.array([])
    
        n = space
        for i in y_data[space: -space]:
            y_mean_2 = np.append(y_mean_2, np.mean(y_data[n-space:n+space]))
            n = n + 1
        
        return x_data[space: -space], y_mean_2, x_fit[space:-space], dec[space:-space]



    
def pwr_spectrum(x_data, y_data):
    
    plt.rc('xtick', labelsize=16)
    plt.rc('ytick', labelsize=16)
    #plt.subplot(2,1,1)
    
    y_mean = average(x_data, y_data)
    y_fft = np.fft.fft(y_data[100:-100] - y_mean)
    y_pwr = np.abs(y_fft)**2
    x_freq = np.fft.fftfreq(len(y_mean))*1e3
    plt.plot(x_freq, y_pwr, linewidth=1, color='grey')
    
    for i in range(x_freq.size):
        if i == len(x_freq):
            break
        #if C[i] > 2100 and C[i] < 2103:
        #    print i
        if y_pwr[i] == np.max(y_pwr):
            freq = np.abs(x_freq[i])
    
    print("Frequency (mHz): "+str(freq))
    
    plt.axvline(freq, color='k', linestyle='--', linewidth=1.5)
    plt.axvline(-freq, color='k', linestyle='--', linewidth=1.5)    
    plt.ylabel('Power '+r'$(V^{2})$',size=20)
    plt.xlabel('Frequency (mHz)',size=20)
    
    #plt.yscale('log')




def curve_fit(x_data, y_data, x_fit, dec, d_type):
    
    if d_type == 'sun' or d_type == 'moon':
        print("\nData not meant for curve fit guess/check!")
        return
    
    elif d_type == 'orion':
        i_low = 2183
        i_high = 4878
        
        x_low = x_data[i_low]
        x_high = x_data[i_high]
        
        x_data = x_data[i_low:i_high-len(x_data)]
        y_data = y_data[i_low:i_high-len(y_data)]
        x_fit = x_fit[i_low:i_high-len(x_fit)]
        print("Least squares done on Orion data from about x = "+str(x_low)+" to "+str(x_high))
        
    elif d_type == 'M17':
        i_low = 3492
        i_high = 5488
        
        x_low = x_data[i_low]
        x_high = x_data[i_high]
        
        x_data = x_data[i_low:i_high-len(x_data)]
        y_data = y_data[i_low:i_high-len(y_data)]
        x_fit = x_fit[i_low:i_high-len(x_fit)]
        print("Least squares done on M17 data from about x = " + str(x_low) + " to " + str(x_high))
    
    elif d_type == 'virgo':
        #i_low = 16964
        i_high = 39915
        
        i_low = 0
        #i_high = x_data.size-1

        x_low = x_data[i_low]
        x_high = x_data[i_high]
        
        x_data = x_data[i_low:i_high-len(x_data)]
        y_data = y_data[i_low:i_high-len(y_data)]
        x_fit = x_fit[i_low:i_high-len(x_fit)]
        print("Least squares done on Virgo A data from about x = "+str(x_low)+" to "+str(x_high))
    
    
    # Guess Values
    b_line = 10.
    #lamb = 2.8e-2
    lamb = spc.c/10.67e9
    #ra = 4.8
    dec_0 = dec * np.pi/180

    #a = np.std(y_data, ddof = 1)
    #b = np.std(y_data, ddof = 1)
    #c = 2*np.pi*(b*spc.c/10.67e9)*np.cos(dec[0])
    c = 2*np.pi*(b_line*np.cos(dec_0))/lamb
    C = np.linspace(c-200, c+200, 500)
    

    s_sq_array = np.array([])
    
    
    for val in C:
        X = np.empty([len(x_fit), 2])
        X[:,0] = np.cos(2*np.pi*val*x_fit)
        X[:,1] = np.sin(2*np.pi*val*x_fit)
    
        Y = np.empty([1, len(y_data)])
        Y[0] = y_data
    
        #print("Shape of X: "+str(X.shape))
        #print("Shape of Y: "+str(Y.shape))
    
        XX = np.dot(np.transpose(X), X)
        XY = np.dot(Y, X)
        XXI = np.linalg.inv(XX)
    
        val = np.dot(XY,XXI)[0]
        YBAR = np.dot(val,np.transpose(X))
        DELY = Y - YBAR
    
        s_sq = np.sum(DELY**2)
        s_sq_array = np.append(s_sq_array, s_sq)
        
    
    print("A and B:")
    print(val)
    
    #print("DELY: "+str(DELY))
    
    A = val[0]
    B = val[1]

    # Finding C...
    plt.rc('xtick', labelsize=12)
    plt.rc('ytick', labelsize=12)
    plt.xlabel('\n'+r'$2\pi(\frac{B_{y}}{\lambda}cos\left(\delta\right))$', fontsize=20)
    plt.ylabel(r'$\chi^{2}$', fontsize=20)
    plt.plot(C, s_sq_array, color ='k')
    
    
    # Guessing C...
    for i in range(C.size):
        if i == len(C):
            break
        if s_sq_array[i] == np.min(s_sq_array):
            C_calc = C[i]
    #print("\nGuessed C: "+str(c))    
    #print("Calculated C: "+str(C_calc))
    
    b_line_calc = C_calc*lamb/(2*np.pi*np.cos(dec_0))
    print("S_sq: "+str(C_calc))
    print("Guessed Base Line (m): "+str(b_line))
    print("Calculated Base Line (m): "+str(b_line_calc))
    
    
    plt.axvline(C_calc, color='b', linestyle=':')
    if d_type == "M17":
        
        for i in range(C.size):
            if i == len(C):
                break
            #if C[i] > 2100 and C[i] < 2103:
            #    print i
            if s_sq_array[i] == np.min(s_sq_array[0:190-len(C)]):
                C_calc = C[i]
        
        print("\nS_sq using 2nd min: "+str(C_calc))
        plt.axvline(C_calc, color='b', linestyle=':')
        #C_calc = 2039.8
        b_line_calc = C_calc*lamb/(2*np.pi*np.cos(dec_0))
        print("Calculated Base Line using 2nd min (m): "+str(b_line_calc))
    
    dec_calc = np.arccos(C_calc*lamb/(2*np.pi*b_line_calc))
    if dec_0 < 0:
        dec_calc = -dec_calc
    print("Guessed Declination (deg): "+str(dec_0*180/np.pi))
    print("Calculated Declination (deg): "+str(dec_calc*180/np.pi))
    print('\n')


    plt.tight_layout()
    plt.show()





# note to self: USE AVERAGE BASELINE!!!!
# feeds in envelope data...
def poly_fit(x_data, y_data, x_fit, dec, d_type):
    
    if d_type == 'sun':
        for i in range(x_data.size):
            #print(i)
            if x_data[i] > 4500 and x_data[i] < 4503:
                i_1 = i
                #print(x_data[i])
                #print(i)
            if x_data[i] > 6000 and x_data[i] < 6005:
                i_2 = i
                #print(x_data[i])
                #print(i)
    
    elif d_type == 'moon':
        for i in range(x_data.size):
            #print(i)
            if x_data[i] > 17500 and x_data[i] < 17503:
                i_1 = i
                print(x_data[i])
                print("i_1 "+str(i))
            if x_data[i] > 23000 and x_data[i] < 23005:
                i_2 = i
                print(x_data[i])
                print(i)
        y_data = average(x_data, y_data)
        i_1 = i_1 + 100
        i_2 = i_2 - 100
    
    else:
        i_1 = 0
        i_2 = len(x_data)
    
    #print(len(x_data))
    #print(len(x_fit))
    #y_data = average(x_data, y_data)
    
    x_data_cut = x_data[i_1: i_2-len(x_data)]
    y_data_cut = y_data[i_1: i_2-len(y_data)]
    x_fit_cut = x_fit[i_1: i_2-len(x_fit)]
    dec_cut = dec[i_1: i_2-len(dec)]
    
    #print(len(x_data))
    #print(len(x_fit))
    
    # Guess Values
    b_line = 10.
    #lamb = 2.8e-2
    lamb = spc.c/10.67e9
    #ra = 4.8
    dec_0 = dec_cut * np.pi/180
    #print(dec_0)
#    phi = np.pi

    HA = np.arcsin(x_fit_cut)
#    PHI = np.linspace(0, phi, 500)
    

    s_sq_array = np.array([])
    
    #print(len(x_fit))
    #print(len(x_data))
    
    # Not sure why function wont work..
#    for val in PHI:
#        F = np.cos(2*np.pi*b_line/lamb * np.cos(dec_0) * np.sin(HA)+val)
#        #F = np.cos(b_line/lamb * np.cos(dec_0) * np.cos(HA + val))
#        X = np.empty([len(x_fit_cut), 3])
#        X[:,0] = 1*F     # The constant value
#        X[:,1] = HA * F  # The "x" value
 #       X[:,2] = HA**2 * F # The "x^2" value
    
#        Y = np.empty([1, len(y_data_cut)])
#        Y[0] = y_data_cut
#    
#        XX = np.dot(np.transpose(X), X)
#        XY = np.dot(Y, X)
        
        #print("shape of XX "+str(XX.shape))
        
#        XXI = np.linalg.inv(XX)
    
#        val = np.dot(XY,XXI)[0]
#        YBAR = np.dot(val,np.transpose(X))
#        DELY = Y - YBAR
    
 #       s_sq = np.sum(DELY**2)
 #       s_sq_array = np.append(s_sq_array, s_sq)
        
    
    print("A and B and C:")
#    print(val)
    
#    A = val[0]
#    B = val[1]
    
    # Finding C...
#    plt.rc('xtick', labelsize=12)
#    plt.rc('ytick', labelsize=12)
#    plt.xlabel(r'$\phi$', fontsize=20)
#    plt.ylabel(r'$\chi^{2}$', fontsize=20)
#    plt.plot(PHI, s_sq_array, color ='k')
    
#    plt.tight_layout()
#    plt.show()
    
    # Guessing C...
#    for i in range(PHI.size):
#        if i == len(PHI):
#            break
#        if s_sq_array[i] == np.min(s_sq_array):
#            PHI_calc = PHI[i]
#    print("\nGuessed phi: "+str(phi))    
#    print("Calculated phi: "+str(PHI_calc))
    
    # Function is redefined here too
#    F = np.cos(2*np.pi*b_line/lamb * np.cos(dec_0) * np.sin(HA) + PHI_calc)
    #F = np.cos(b_line/lamb * np.cos(dec_0) * np.cos(HA + val))
    X = np.empty([len(x_fit_cut), 3])
    X[:,0] = 1#*F     # The constant value
    X[:,1] = HA# * F  # The "x" value
    X[:,2] = HA**2# * F # The "x^2" value

    Y = np.empty([1, len(y_data_cut)])
    Y[0] = y_data_cut

    XX = np.dot(np.transpose(X), X)
    XY = np.dot(Y, X)
    
    #print("shape of XX "+str(XX.shape))
    
    XXI = np.linalg.inv(XX)

    val = np.dot(XY,XXI)[0]
    print(val)
    YBAR = np.dot(val,np.transpose(X))
    DELY = Y - YBAR
    print(X)
    
    
    index_ybar = np.argmin(YBAR)
    print("YBAR:")
    print(YBAR[index_ybar])
    print("HA")
    print(HA[index_ybar])
    print("DEC:")
    print(dec_cut[index_ybar])



    #s_sq = np.sum(DELY**2)
    #s_sq_array = np.append(s_sq_array, s_sq)
    #plt.ion()
    
    # UNDO THIS 
    plt.rc('xtick', labelsize=12)
    plt.rc('ytick', labelsize=12)
    plt.ylabel('Power '+r'$(V^{2})$',size=20)
    plt.xlabel('Frequency (Hz)',size=20)
    plt.plot(x_data_cut, y_data_cut, '.')
    plt.plot(x_data_cut, YBAR, color='r')
    plt.show()
    
    #b_line_calc = C_calc*lamb/(2*np.pi*np.cos(dec_0))
    #print("Guessed Base Line (m): "+str(b_line))
    #print("Calculated Base Line (m): "+str(b_line_calc))

    
    N = 1000

    f_f = b_line*np.cos(dec_cut[list(YBAR).index(np.min(YBAR))  ## fringe frequency
    ])*np.cos(HA[list(YBAR).index(np.min(YBAR))
    ])/lamb

    ## Solving Integral Numerically

    M_f = []
    q1 = []
    q2 = []

    k=0
    M_f = []
    I = np.arange(0,6,0.01)
    for i in I:
        for n in np.arange(-N,N+1):
            q1.append(np.sqrt(1 - (n/N)**2))
            q2.append(np.cos(2.*np.pi*i*n/N))
        q_t = np.dot(q1, np.transpose(q2))
        q_t = np.sum(q_t)
        M_f.append(q_t)
        q1 = []
        q2 = []
        #print k
        k=k+1
    #print k
    #plt.title('Integral Evaluation vs' + r' $R \times f_{f}$' +' - Sun',size=26)


    


    plt.plot(I,M_f)
    plt.rc('ytick', labelsize=19)
    plt.rc('xtick', labelsize=19) 
    plt.axhline(y = 0, color = 'k')
    plt.ylabel(r'$MF_{theory}$',size=20)
    plt.xlabel(r'$R \times f_{f}$',size=20)



    z = []
    I_2 = []
    #M_final = np.array([])
    M_f.append(1.)
    index = 0
    #M_f = M_f.append(1.)

    i = 0
    while i < len(M_f):
        if M_f[i] > 0.:
            i=i+1
        else:
            z.append(i)
            I_2.append(I[i])
            while M_f[i] < 0.:
                i = i+1
        #print i

    #i = 0
    #for i in range(len(M_f)):
        #if M_f[i] > 0.:
        #    i=i+1
        #else:
        #    z.append(i)
        #    I_2.append(I[i])
        #    while M_f[i] < 0.:
        #        i = i+1
    #    if M_f[i] > 0 and M_f[i]:
    #        print M_f[i]
    #        M_final.append(M_[i])
        #index = index + 1
    
    print I_2

    

    #rr = M_f[0]/f_f
    rr = I_2/f_f
    
    
    r_final=(rr*180./np.pi)*60

    print 
    print 'Radius = ', r_final, ' in degrees'
    print
    print 'F_f = ', f_f


    for I in range(len(I_2)):
        plt.axvline(I_2[I], color='k', linestyle='--')


    
    plt.show()


if __name__ == '__main__':
	main()