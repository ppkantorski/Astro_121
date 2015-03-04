#!/usr/bin/env python

# ========================================================================== #
# File: convolve_image.py                                                    #
# Programmer: Patrick Kantorski                                              #
# Date: 05/04/14                                                             #
# Class: Astronomy 121 - Radio Astronomy Lab                                 #
# Time: T 6:00-9:00 PM                                                       #
# Instructor: Aaron Parsons                                                  #
# Description: This program was written in Python to perform a convolution   #
#              on the data files created from handle_data.py and create an   #
#              image.                                                        #
# ========================================================================== #

import numpy as np
import pylab 
import math
import scipy.signal

#want to eventually graph vertical axis = b, horizontal axis = d, color = temperature 
#d has size (35, 2000)
#b has size (35)
#temp has size (35, 2000)


def main():

    file = np.load('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_4/Data/Clean/May_4_final_final.npz')

    b_file = file['b'] 
    b_list = []
    d_file = file['Distance'] 
    d_list = []
    temp_file = file['Temp'] 
    temp_list = []  
    h_list=[]

    for i in range(len(b_file)):
        b = b_file[i]
        d_array = d_file[i]
        temp = temp_file[i]
        for k in range(0, 2000): 
            b_list.extend([b*np.pi/180.])
            if math.isnan(d_array[k])==True:
                d_list.extend([0.]) 
            elif abs(d_array[k]) > 30.: 
                d_list.extend([0.]) 
            else:
                d_list.extend([d_array[k]])
            if math.isnan(temp[k])==True:
                temp_list.extend([0.])
            elif temp[k] < 0.0: 
                temp_list.extend([0.0])
            else:
                temp_list.extend([temp[k]]) 

    for i in range(len(b_list)): 
        h = d_list[i]*np.tan(b_list[i]) 
        if math.isnan(h)==True:
            h_list.extend([0.]) 
        else: 
            h_list.extend([h]) 


 
    print h_list   



    #create grid with 200 data points up and down (-10kpc to 10kpc for 0.1 kpc resolution)
    img = np.zeros((201,251))
    wt = np.zeros((201,251))
    ker = np.zeros((201, 251))
    data = temp_list

    print np.shape(temp_list) 
    #np.transpose(d_list)  

    print np.shape(d_list)
    print np.shape(h_list)

    sigma_x = np.std(d_list)
    sigma_y = np.std(h_list)

    #print data 

    #each data value is also an array - will need to account for that too 
    for i in xrange(len(d_list)):
        x_pos = np.rint(d_list[i]/0.1)
        y_pos = np.rint(h_list[i]/0.1)   #shifts the zero point to the 100th row in our image
        data_val = data[i]
    
        x_pos_1 = 0
        y_pos_1 = 0 

        if abs(x_pos) > 250.: 
            x_pos_1 = 0.0
        else:
            x_pos_1 = x_pos
        
        if abs(y_pos) > 200.:
            y_pos_1 = 0.0
        else:
            y_pos_1 = y_pos

        #print i, x_pos_1, y_pos_1, data_val
                                      #which corresponds to zero in H
        img[y_pos_1][x_pos_1] += data_val #record brightness temperature in appropriate location on 
                                     #image grid
        wt[y_pos_1][x_pos_1] += 1        #record that a data point was stored in that location

        x = d_list[i]
        y = h_list[i]
        ker[y_pos_1][x_pos_1] += np.exp((-(x**2/(2*sigma_x**2) + y**2/(2*sigma_y**2))))


    print np.shape(img)
    print np.shape(ker) 
    

    image = scipy.signal.convolve2d(img, ker, mode = 'same')
    print 'image done'
    weight = scipy.signal.convolve2d(wt, ker, mode = 'same')
    print 'weight done'
    fin_img = image/weight
    print 'fin img done' 

    

    #pylab.plot(d_list, h_list)

    #pylab.imshow(image, cmap = 'hot') 

    #pylab.imshow(weight, cmap = 'Greys')

    plot = pylab.imshow(fin_img, cmap='hot', vmin = 0.0, origin = 'lower', extent = (0, 25, -10, 10))
    pylab.colorbar(plot)

    #pylab.ylim(0, 40)
    #pylab.xlim(0, 30)
    pylab.show()


if __name__ == '__main__':
	main()