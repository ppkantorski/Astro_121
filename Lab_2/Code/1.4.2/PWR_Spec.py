#!/usr/bin/env python

# ========================================================================== #
# File: DFT_analyzer.py                                                      #
# Programmer: Patrick Kantorski                                              #
# Date: 02/25/14                                                             #
# Class: Astronomy 121 - Radio Astronomy Lab                                 #
# Time: T 6:00-9:00 PM                                                       #
# Instructor: Aaron Parsons                                                  #
# Description: This program was written in Python to plot the Discrete       #
#              Fourier Transform, aka DFT, of the 9 data samples taken in    #
#              'LO_sampling.py'.                                             #
# ========================================================================== #

import numpy as np
import matplotlib.pyplot as plt

def main():

    sampFreq = 1e6
    print("Sample Frequency: " + str(sampFreq) + " Hz")
    
    print("Calculating DFTs and graphing data...")
    graph_data(sampFreq)

    print("All process are complete!\n")


def DFT(fileName, sampFreq):
    data = np.loadtxt(fileName)
    N = len(data)
    
    delta = 1. / sampFreq
    T = N * delta
    
    t = np.arange(-N/2, N/2, 1)
    x_val = np.arange(-sampFreq/2, sampFreq*(1 - 2./N)/2, sampFreq/N)
    y_val = []
    
    for n in x_val:
        num = 0
        for a in t:
            num += data[a + N/2] * np.exp(-2j*a*delta*np.pi*n) * delta

        y_val.append(num/(N*delta))
    
    y_val = np.abs(y_val)**2
    
    return {'x_val':x_val, 'y_val':y_val}


def graph_data(sampFreq):
    
    data = DFT('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/1.4.2/sample_0.3', sampFreq)
    # X-axis in units of MHz, Y-axis in units of 
    x_val1 = data['x_val']/1.e6
    y_val1 = data['y_val']
    


    plt.rc('xtick', labelsize=16)
    plt.rc('ytick', labelsize=16)

    n = 1
    while n < 3:
        plt.subplot(1, 2, n)
        if n == 1:
            plt.plot(x_val1 * 1.e3, y_val1)
            plt.xlabel('Frequency (kHz)', fontsize=18)
            plt.ylabel('Power', fontsize=18)
            plt.title('Frequency Resolution' ,size=22)
            plt.axvline(300.8, color='b', linestyle=':')
            plt.axvline(-300.8, color='b', linestyle=':')
        if n == 2:
            plt.plot(x_val1, y_val1)
            plt.yscale('log')
            plt.xlabel('Frequency (MHz)', fontsize=18)
            plt.ylabel('Power', fontsize=18)
            plt.title('Power Spectrum' ,size=22)
            plt.axvline(0.3006, color='b', linestyle=':')
            plt.axvline(-0.3006, color='b', linestyle=':')
            
        n += 1
   
    plt.axis([-0.6, 0.6, 0, 0.10])
    plt.axvline(0, color='b', linestyle='k')

    

    
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
	main()