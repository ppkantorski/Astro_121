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
    
    data = DFT('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/1.4.2/sample_0.1', sampFreq)
    # X-axis in units of MHz, Y-axis in units of 
    x_val1 = data['x_val']/1.e6
    y_val1 = data['y_val']
    
    data = DFT('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/1.4.2/sample_0.2', sampFreq)
    x_val2 = data['x_val']/1.e6
    y_val2 = data['y_val']
    
    data = DFT('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/1.4.2/sample_0.3', sampFreq)
    x_val3 = data['x_val']/1.e6
    y_val3 = data['y_val']
    
    data = DFT('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/1.4.2/sample_0.4', sampFreq)
    x_val4 = data['x_val']/1.e6
    y_val4 = data['y_val']
    
    data = DFT('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/1.4.2/sample_0.5', sampFreq)
    x_val5 = data['x_val']/1.e6
    y_val5 = data['y_val']
    
    data = DFT('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/1.4.2/sample_0.6', sampFreq)
    x_val6 = data['x_val']/1.e6
    y_val6 = data['y_val']
    
    data = DFT('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/1.4.2/sample_0.7', sampFreq)
    x_val7 = data['x_val']/1.e6
    y_val7 = data['y_val']
    
    data = DFT('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/1.4.2/sample_0.8', sampFreq)
    x_val8 = data['x_val']/1.e6
    y_val8 = data['y_val']
    
    data = DFT('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/1.4.2/sample_0.9', sampFreq)
    x_val9 = data['x_val']/1.e6
    y_val9 = data['y_val']

    # Iteration variable.
    n = 1
    plt.figure(figsize=(18,11))

    # Creates 3x3 graph display of the 9 data files.
    while n < 10:
        plt.rc('xtick', labelsize=16)
        plt.rc('ytick', labelsize=16)
        plt.subplot(3, 3, n)

        plt.plot(vars()["x_val" + str(n)], vars()["y_val" + str(n)])
        print("Generating plot " + str(n) + "...")
        plt.axis([-0.6, 0.6, 0, 0.10])
        plt.axvline(0, color='k', linestyle=':')
        plt.xlabel('Frequency (MHz)', fontsize=18)
        plt.ylabel('Power', fontsize=18)
        plt.title(r'$\bf{ \nu_{signal}=}' + str(0.1*n) +"*" + r'\nu_{sample} }$' ,size=22)
    
        n = n + 1
    
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
	main()