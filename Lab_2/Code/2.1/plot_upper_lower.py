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
    data_1 = np.loadtxt('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/2.1/MixAnPlus')
    data_2 = np.loadtxt('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/2.1/MixAnMinus')


    print(len(data_1))

    # Graphs data files.
    print("Generating graphs...")
    gen_graph(data_1, data_2)
    
    print("All plots are complete!\n")


def gen_graph(data_1, data_2):
    
    x_axis = np.arange(0., 16000., 1.)
    
    n = 1
    while n < 3:
        plt.subplot(2, 1, n)
        if n == 1:
            plt.plot(x_axis/4.e3, data_1, color='b')
            plt.axis([0,2,-0.100,0.100])
            #plt.xlabel('Time (ms)', fontsize=20)
            plt.ylabel('Voltage (V)', fontsize=20)
            plt.title('Analog Mixing with'+ r' $\nu_{sig}=1.05 \times\ \nu_{lo}$' ,size=22)
        if n == 2:
            plt.plot(x_axis/4.e3, data_2, color='r')
            plt.axis([0,2,-0.100,0.100])
            plt.xlabel('Time (ms)', fontsize=20)
            plt.ylabel('Voltage (V)', fontsize=20)
            plt.title('Analog Mixing with'+ r' $\nu_{sig}=0.95 \times\ \nu_{lo}$' ,size=22)
        n += 1
        
    plt.rc('xtick', labelsize=12)
    plt.rc('ytick', labelsize=12)
    
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
	main()