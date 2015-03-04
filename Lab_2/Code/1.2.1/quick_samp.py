#!/usr/bin/env python

# ========================================================================== #
# File: quick_samp.py                                                        #
# Programmer: Patrick Kantorski                                              #
# Date: 02/18/14                                                             #
# Class: Astronomy 121 - Radio Astronomy Lab                                 #
# Time: T 6:00-9:00 PM                                                       #
# Instructor: Aaron Parsons                                                  #
# Description: This program was written in Python to control a SRS Function  #
#              Generator, also know as a Local Oscillator (LO) and a Pulsar  #
#              Sampler in order to take and record data measurements over    #
#              the Command Line.                                             #
# ========================================================================== #

import numpy as np
import DFEC
import os

def main():
    
    nSamp = 256
    sampFreq = 1.e6
    Data_Collect(nSamp, sampFreq)
    
    x = raw_input("Plot data now? (Y/N) ")
    if x == 'Y' or 'y':
        os.system("/home/pkantorski/radio_lab/labs/lab_2/Code/1.2.1/plot_samples.py")


def Data_Collect(nSamp, sampFreq):
    
    n = 0.1
    x = raw_input("Press any key to take first data sample... ")
    while n <= 0.9:
#        DFEC.set_srs(1, freq = n*sampFreq, off=0.0, pha=0.0, dbm=0.0)
        DFEC.sampler(nSamp, sampFreq, fileName='sample_'+str(n), dual=False, low=False, integer=False, timeWarn=True)
        x = raw_input("Next value... ")
        n = n + 0.1

if __name__ == '__main__':
	main()

