#!/usr/bin/env python

# ========================================================================== #
# File: plot_samples.py                                                      #
# Programmer: Patrick Kantorski                                              #
# Date: 02/18/14                                                             #
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
    d1 = np.loadtxt('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/1.2.1/sample_0.1')
    d2 = np.loadtxt('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/1.2.1/sample_0.2')
    d3 = np.loadtxt('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/1.2.1/sample_0.3')
    d4 = np.loadtxt('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/1.2.1/sample_0.4')
    d5 = np.loadtxt('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/1.2.1/sample_0.5')
    d6 = np.loadtxt('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/1.2.1/sample_0.6')
    d7 = np.loadtxt('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/1.2.1/sample_0.7')
    d8 = np.loadtxt('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/1.2.1/sample_0.8')
    d9 = np.loadtxt('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_2/Code/1.2.1/sample_0.9')


    # Graphs data files.
    print("Generating graphs...")
    gen_graph(d1,d2,d3,d4,d5,d6,d7,d8,d9)
    
    print("All operations are complete!\n")


def gen_graph(d1,d2,d3,d4,d5,d6,d7,d8,d9):
    # Axis scaled to time in micro-seconds.
    x_axis = np.arange(0., 256., 1.)

    x_axis_2 = np.arange(0, 100, 0.01)
    y_axis = 0.5* np.sin(2*np.pi*x_axis_2)

    # Iteration variable.
    n = 1
    plt.figure(figsize=(18,11))

    # Creates 3x3 graph display of the 9 data files.
    while n < 10:
        plt.rc('xtick', labelsize=16)
        plt.rc('ytick', labelsize=16)
        plt.subplot(3, 3, n)
        
        if n == 1:
            plt.plot( (x_axis_2 / (0.1*n)) - 8.396 , y_axis)
            
        if n == 2:
            plt.plot( (x_axis_2 / (0.1*n)) - 4.213 , y_axis)
            
        if n == 3:
            plt.plot( (x_axis_2 / (0.1*n)) - 1.436, y_axis)
            
        if n == 4:
            plt.plot( (x_axis_2 / (0.1*n)) - 1.388, y_axis)
        
        if n == 5:
            plt.plot( (x_axis_2 / (0.1*n)) - 1.662, y_axis)
        
        if n == 6:
            plt.plot( (x_axis_2 / (0.1*n)) - .950, y_axis)
        
        if n == 7:
            plt.plot( (x_axis_2 / (0.1*n)) -0.09, y_axis)
        
        if n == 8:
            plt.plot( (x_axis_2 / (0.1*n)) - 0.96, y_axis)
        
        if n == 9:
            plt.plot( (x_axis_2 / (0.1*n)) - 0.65942, y_axis)
        
        
        plt.plot(x_axis, vars()["d" + str(n)], '-o')

        
        plt.axis([0, 14, -1.0, 1.0])
        plt.xlabel('Time (ms)', fontsize=18)
        plt.ylabel('Voltage (V)', fontsize=18)
        plt.title(r'$\bf{ \nu_{signal}=}' + str(0.1*n) +"*" + r'\nu_{sample} }$' ,size=22)
        
        
        n = n + 1
    
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
	main()