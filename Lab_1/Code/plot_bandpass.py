#!/usr/bin/env python

# ========================================================================== #
# File: plot_bandpass.py                                                     #
# Programmer: Patrick Kantorski                                              #
# Date: 02/10/14                                                             #
# Class: Astronomy 121 - Radio Astronomy Lab                                 #
# Time: T 6:00-9:00 PM                                                       #
# Instructor: Aaron Parsons                                                  #
# Description: This program was written in Python to graph a complex         #
#              RLC bandpass filter function in units of frequency vs gain    #
#              and the output of the LC filter in units of frequency vs      #
#              ohms.                                                         #
# ========================================================================== #

import numpy as np
import matplotlib.pyplot as plt
import math

a = []
b = []

z0 = []
z1 = []
y0 = []
y1 = []


for f in range(1072500, 1073500, 10):
        R = 33
        L = 1e-6
        C = 22e-9

        Z = (1j)*2*math.pi*f*L / (1 - L*C*(2*math.pi*f)**2)
        
        a.append(f)
        z0.append(Z)
        
for n1 in z0:
        z1.append(abs(n1))

plt.title('LC Circuit Responce')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Impedance (Ohms)')
plt.axvline(1 / (2 * math.pi * (22e-9 * 1e-6)**.5), color='b', linestyle=':')
plt.plot(a,z1)
plt.show()


for f in range(500000, 1800000, 10):
        R = 33
        L = 1e-6
        C = 22e-9

        Z = (1j)*2*math.pi*f*L / (1 - L*C*(2*math.pi*f)**2)
        G = Z/(R+Z)
        
        b.append(f)
        y0.append(G)

for n2 in y0:
        y1.append(abs(n2))

plt.title('RLC Circuit Responce')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (Vout/Vin)')
plt.axvline(1 / (2 * math.pi * (22e-9 * 1e-6)**.5), color='b', linestyle=':')
plt.plot(b,y1)
plt.show()