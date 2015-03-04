#!/usr/bin/env python

# ========================================================================== #
# File: plot_samples.py                                                      #
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


def main():
    # Loads data files.
    print("Loading sample data...")
    a = np.load('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/2.3/sine_cos.npz')
#    b = np.load('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/2.2/omb_02.npz')
    
    #cosine
    data_1 = a['arr_2']
    #sine
    data_2 = a['arr_3']


    print(len(data_1))

    # Graphs data files.
    print("Generating graphs...")
    gen_graph(data_1, data_2)
    
    print("All plots are complete!\n")


def gen_graph(data_1, data_2):
    
    x_axis = np.arange(0., len(data_1), 1.)
    
    n = 1
    while n < 3:
        #plt.subplot(2, 1, n)
        if n == 1:
            plt.plot(x_axis*2e-3, data_1, linewidth=2, color='b')
            plt.axis([0,.5,-2e6,2e6])
            #plt.xlabel('Time (ms)', fontsize=20)
            plt.ylabel('Least Significant Bits', fontsize=20)
            #plt.title('Digital Mixing with'+ r' $\nu_{sig}=1.05 \times\ \nu_{lo}$' ,size=22)
        if n == 2:
            plt.plot(x_axis*2e-3, data_2, linewidth=2, color='r')
            plt.axis([0,.5,-2e6,2e6])
            plt.xlabel('Time (us)', fontsize=20)
            plt.ylabel('Least Significant Bits', fontsize=20)
            plt.title('Real and Imaginary SSB' ,size=22)
        n += 1
        
    plt.rc('xtick', labelsize=12)
    plt.rc('ytick', labelsize=12)
    
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
	main()