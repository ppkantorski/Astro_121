#!/usr/bin/env python

# ========================================================================== #
# File: double.py                                                            #
# Programmer: Patrick Kantorski                                              #
# Date: 02/24/14                                                             #
# Class: Astronomy 121 - Radio Astronomy Lab                                 #
# Time: T 6:00-9:00 PM                                                       #
# Instructor: Aaron Parsons                                                  #
# Description: This program was written in Python to plot data taken from    #
#              the program "LO_sampling.py" and the "LO" at UC Berkeley's    #
#              radio astronomy laboratory in order to demonstrate the data   #
#              and its limits.                                               #
# ========================================================================== #

import numpy as np
import matplotlib.pyplot as plt
import numpy.fft as fft


def main():
    # Loads data files.
    print("Loading sample data...")
    a = np.load('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/2.2/omb_01.npz')
    b = np.load('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/2.2/omb_02.npz')
    
    data_1 = a['arr_4']
    data_2 = b['arr_4']


    print(len(data_1))

    # Graphs data files.
    print("Generating graphs...")
    gen_graph(data_1, data_2)
    
    print("All plots are complete!\n")


def gen_graph(data_1, data_2):
    
    x_axis = np.arange(0., len(data_1), 1.)
    
    n = 1
    while n < 3:
        plt.subplot(2, 1, n)
        if n == 1:
            plt.plot(x_axis*20*5e-3/2, data_1, color='b')
            plt.axis([0,100,-4000,4000])
            #plt.xlabel('Time (ms)', fontsize=20)
            plt.ylabel('Least Significant Bits', fontsize=20)
            plt.title('Digital Mixing with'+ r' $\nu_{sig}=1.05 \times\ \nu_{lo}$' ,size=22)
        if n == 2:
            plt.plot(x_axis*20*5e-3/2, data_2, color='r')
            plt.axis([0,100,-4000,4000])
            plt.xlabel('Time (us)', fontsize=20)
            plt.ylabel('Least Significant Bits', fontsize=20)
            plt.title('Digital Mixing with'+ r' $\nu_{sig}=0.95 \times\ \nu_{lo}$' ,size=22)
        n += 1
        
    plt.rc('xtick', labelsize=12)
    plt.rc('ytick', labelsize=12)
    
    d1 = np.load('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/2.2/omb_01.npz')
    d2 = np.load('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/2.2/omb_02.npz')

    f = d1['arr_4']
    g = d2['arr_4']


    #### Fourier Transform over previous data ####

    plt.rc('xtick', labelsize=16)
    plt.rc('ytick', labelsize=16)
    plt.subplot(2,1,1)

    y1 = fft.fft(f)

    x=fft.fftfreq(len(y1), d = 1./(4.e6))


    for i in range(len(y1)):
        if abs(x[i]) > 50000:
            y1[i] = 0 + 0j

    y2 = fft.fft(g)

    for i in range(len(y2)):
        if abs(x[i]) > 50000:
            y2[i] = 0 + 0j

    plt.plot(x_axis*20*5e-3/2, np.fft.ifft(y1), color='k', linewidth=2)
    plt.title('Filtered Mixed '+r' $\nu_{sig}=1.05$'+'MHz Signal',size=22)
    #plt.ylabel('Voltage (V)',size=20)
    #plt.axis([-1,1, -.1 ,.1])

    plt.rc('xtick', labelsize=16)
    plt.rc('ytick', labelsize=16)
    plt.subplot(2,1,2)
    plt.plot(x_axis*20*5e-3/2,np.fft.ifft(y2), color='k', linewidth=2)
    plt.title('Filtered Mixed '+r' $\nu_{sig}=0.95$'+'MHz Signal',size=22)
    #plt.ylabel('Voltage (V)',size=20)
    plt.xlabel('Time (us)',size=20)
    #plt.axis([-1,1, -.1 , .1])
    
    plt.tight_layout()
    plt.show()




if __name__ == '__main__':
	main()