#!/usr/bin/env python

# ========================================================================== #
# File: LO_sampling_2.py                                                     #
# Programmer: Patrick Kantorski                                              #
# Date: 02/18/14                                                             #
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
import DFEC
import os

def main():
    nSamp = 256

    # Sampling original frequency.
    sampFreq = 10.e3
    x = raw_input("Press any button to take first data sample... ")
    Data_Same(nSamp, sampFreq)

    # Sampling larger frequency (inadequate sample rate).
    sampFreq = 2.7 * 10.e3
    x = raw_input("Press any button to take second data sample... ")
    Data_Large(nSamp, sampFreq)
    
    x = raw_input("Plot data now? (Y/N) ")
    if x == 'Y' or 'y':
        os.system("/home/pkantorski/radio_lab/labs/lab_2/Code/1.2.2/plot_samples_2.py")
    
    print("All process are complete! ")


def Data_Same(nSamp, sampFreq):
    #DFEC.set_srs(1, freq=sampFreq, off=0.0, pha=0.0, dbm=0.0)
    DFEC.sampler(nSamp, sampFreq, fileName='same_Freq.txt', dual=False, low=False, integer=False, timeWarn=True)


def Data_Large(nSamp, sampFreq):
    # Note: Fix/understand frequency in set_srs.
    #DFEC.set_srs(1, freq=1.e6, off=0.0, pha=0.0, dbm=0.0)
    DFEC.sampler(nSamp, sampFreq, fileName='large_Freq.txt', dual=False, low=False, integer=False, timeWarn=True)


if __name__ == '__main__':
	main()