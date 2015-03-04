#!/usr/bin/env python

# ========================================================================== #
# File: generate_image.py                                                    #
# Programmer: Patrick Kantorski                                              #
# Date: 05/04/14                                                             #
# Class: Astronomy 121 - Radio Astronomy Lab                                 #
# Time: T 6:00-9:00 PM                                                       #
# Instructor: Aaron Parsons                                                  #
# Description: This program was written in Python create a final image for   #
#              a single vertical profile of the galactic warp.               #
# ========================================================================== #

import numpy as np
import pylab 
import math
import scipy.signal


def main():
	
    data = np.load('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_4/Data/fin_img_data.npz')
    image = data['arr_0']
    plot = pylab.imshow(image, cmap='spectral', vmin = 0.0, extent = (0, 25, -10, 10))
    pylab.colorbar(plot)
    pylab.title("H1 Emission Along The Galactic Plane", fontsize=24)
    pylab.xlabel("Distance (kpc)", fontsize=20)
    pylab.ylabel("Height (kpc)", fontsize=20)
    #pylab.ylim(0, 40)
    #pylab.xlim(0, 30)
    pylab.show()
	

if __name__ == '__main__':
	main()