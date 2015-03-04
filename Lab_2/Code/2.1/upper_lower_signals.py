#!/usr/bin/env python

# ========================================================================== #
# File: upper_lower_signals.py                                               #
# Programmer: Patrick Kantorski                                              #
# Date: 02/24/14                                                             #
# Class: Astronomy 121 - Radio Astronomy Lab                                 #
# Time: T 6:00-9:00 PM                                                       #
# Instructor: Aaron Parsons                                                  #
# Description: This program was written in Python to control a SRS Function  #
#              Generator, also know as a Local Oscillator (LO) and a Pulsar  #
#              Sampler in order to take and record data measurements over    #
#              the Command Line.  Data was collected to demonstrate the      #
#              extremes of the Nyquist frequency and aliasing.               #
# ========================================================================== #

import numpy as np
import matplotlib.pyplot as plt
import radiolab

def main():
    
    lowFreq = 100.e3

    print("Configuring the Local Oscillator...")
    set_config(lowFreq)

    print("Taking data sample...")
    sample_data(lowFreq)

    x = raw_input("Plot data now? (Y/N) ")
    if x == 'Y' or 'y':
        os.system("./plot_upper_lower.py")

    print("All process are complete!\n")


def set_config(lowFreq):
    
    radiolab.set_srs(1, lowFreq, vpp=None, dbm=0., off=None, pha=None)
    radiolab.set_srs(2, lowFreq - lowFreq*(5./100.), vpp=None, dbm=0., off=None, pha=None)
    

def sample_data(lowFreq):
    
    radiolab.sampler(16000, 20.*2.*lowFreq, fileName='diff.txt', dual=False, low=False, integer=False, timeWarn=False)


if __name__ == '__main__':
	main()