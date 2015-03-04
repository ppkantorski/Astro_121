#!/usr/bin/env python

# ========================================================================== #
# File: handle_data.py                                                       #
# Programmer: Patrick Kantorski                                              #
# Date: 05/04/14                                                             #
# Class: Astronomy 121 - Radio Astronomy Lab                                 #
# Time: T 6:00-9:00 PM                                                       #
# Instructor: Aaron Parsons                                                  #
# Description: This program was written in Python to plot the pointing limit #
#              range of the 4.5m radio telescope at the Leuschner            #
#              Observatory.                                                  #
# ========================================================================== #

import numpy as np
import numpy.fft as fft
import matplotlib.pyplot as plt
import readspec_mod as rsm
import scipy.constants as spc
import scipy.optimize as optimize
import os
import sys
import ephem


x = np.loadtxt('/Users/ppkantorski/Desktop/alt_limits.txt')
plt.plot(x, color='k', linewidth=2)
plt.title('Leuschner Radio Dish', fontsize=24)
plt.xlim([0, 360])
plt.xlabel('Azimuth (deg)', fontsize=20)
plt.ylabel('Lowest Altitude Position (deg)', fontsize=20)
plt.tight_layout()
plt.show()