#!/usr/bin/env python

# ========================================================================== #
# File: plot_samples_2.py                                                    #
# Programmer: Patrick Kantorski                                              #
# Date: 02/18/14                                                             #
# Class: Astronomy 121 - Radio Astronomy Lab                                 #
# Time: T 6:00-9:00 PM                                                       #
# Instructor: Aaron Parsons                                                  #
# Description: This program was written in Python to plot data taken from    #
#              the program "LO_sampling.py" and the "LO" at UC Berkeley's    #
#              radio astronomy laboratory in order to demonstrate Nyquist    #
#              sampling and aliasing.                                        #
# ========================================================================== #

import numpy as np
import matplotlib.pyplot as plt

def main():
    a = np.loadtxt('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/1.2.2/same_Freq.txt')
    b = np.loadtxt('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/1.2.2/large_Freq.txt')

    # Time in units of ms.
    x_axis = np.arange(0, 256, 1)*(0.10)

    plt.rc('xtick', labelsize=16)
    plt.rc('ytick', labelsize=16)
    plt.subplot(2,1,1)
    plt.plot(x_axis, a)
    plt.axis([0,25,-1.,1.])
    plt.title(r'$\bf{ \nu_{sigma}= \ \nu_{sampl} }$',size=24)
    plt.ylabel("Voltage (V)", fontsize=16)

    plt.rc('xtick', labelsize=16)
    plt.rc('ytick', labelsize=16)
    plt.subplot(2,1,2)
    plt.plot(x_axis, b)
    plt.axis([0,25,-1.,1.])
    plt.title(r'$\bf{ \nu_{sigma}>> \ \nu_{sampl} }$',size=24)
    plt.xlabel("Time (ms)", fontsize=16)
    plt.ylabel("Voltage (V)", fontsize=16)

    plt.show()
    
    print("All operations are complete!\n")


if __name__ == '__main__':
	main()