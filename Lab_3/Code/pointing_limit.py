#!/usr/bin/env python

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
plt.xlabel('Azimuth (deg)', fontsize=20)
plt.ylabel('Lowest Altitude Position (deg)', fontsize=20)
plt.tight_layout()
plt.show