#!/usr/bin/env python

# ========================================================================== #
# File: tracking_code.py                                                     #
# Programmer: Patrick Kantorski                                              #
# Date: 05/04/14                                                             #
# Class: Astronomy 121 - Radio Astronomy Lab                                 #
# Time: T 6:00-9:00 PM                                                       #
# Instructor: Aaron Parsons                                                  #
# Description: This program was written in Python to control the 4.5m radio  #
#              telescope at the Leuschner Observatory and record data.       #
# ========================================================================== #

import numpy as np
import dish
import time
import threading
import takespec
import dish_synth
from os import sys
import ephem


#generate lists of pointings in terms of galactic coords

#b_list = [-20., -18., -16., -14., -12., -10., -8., -6., -4., -2., 0., 2., 4., 6., 8., 10., 12., 14., 16., 20.]


b_coord = [20.0, 16.0, 12.0, 8.0, 4.0, 0.0, -4.0, -8.0, -12.0, -16.0, -20.0, 20.0, 18.0, 16.0, 14.0, 12.0, 10.0, 8.0, 6.0, 4.0, 2.0, 0.0, -2.0, -4.0, -6.0, -8.0, -10.0, -12.0, -14.0, -16.0, -18.0, -20.0, 18.0, 14.0, 10.0, 6.0, 2.0, -2.0, -6.0, -10.0, -14.0, -18.0]
l_coord = []

for i in range(0, len(b_coord)): 
     l_coord.extend([75.0]) 

#for i in range(100, 170, 8):
#     l = i
#    for k in range(0, len(b_list), 1):
#        b = b_list[k]
#       b_coord.extend([b])
#        l_coord.extend([l])


#for n in range(200, 230, 8):
#    m = n
#    for j in range(0, len(b_list), 1):
#        b = b_list[j]
#        b_coord.extend([b])
#        l_coord.extend([m])

np.savetxt('gal_lat_b.gz', b_coord)
np.savetxt('gal_long_l.gz', l_coord)


#determining alt,az for pointing

def gal_to_eq(b_lat, l_long):
    #open('alt_list.txt', 'w')
    #open('az_list.txt', 'w')

    R = np.zeros([3,3])
    R[0] = [-0.054876, -0.873437, -0.483835]
    R[1] = [0.494109, -0.444830, 0.746982]
    R[2] = [-0.867666, -0.198076, 0.455984]
    trans_R = np.transpose(R)

    x = np.zeros([3,1])
    x[0] = np.cos(b_lat*np.pi/180)*np.cos(l_long*np.pi/180)
    x[1] = np.cos(b_lat*np.pi/180)*np.sin(l_long*np.pi/180)
    x[2] = np.sin(b_lat*np.pi/180)

    A = np.dot(trans_R, x)

    obs = ephem.Observer()
    obs.lat = 37.8732*np.pi/180
    obs.long = -122.2573*np.pi/180
    obs.date = ephem.now()
    lst = obs.sidereal_time()

    R_1 = np.zeros([3,3])
    R_1[0] = [np.cos(lst), np.sin(lst), 0]
    R_1[1] = [np.sin(lst), -1*np.cos(lst), 0]
    R_1[2] = [0,0,1]

    B = np.dot(R_1, A)

    lat = 37.8732*np.pi/180

    R_2 = np.zeros([3,3])
    R_2[0] = [-1*np.sin(lat), 0, np.cos(lat)]
    R_2[1] = [0, -1, 0]
    R_2[2] = [np.cos(lat), 0, np.sin(lat)]

    C = np.dot(R_2, B)

    az = np.arctan2(C[1], C[0])
    alt = np.arcsin(C[2])
    alt_list = alt*(180/np.pi)
    az_list = az*(180/np.pi)

    return (az_list[0], alt_list[0])
    #np.savetxt('alt_list.txt', alt_list)
    #np.savetxt('az_list.txt', az_list)



def data_taker():
    timeLimit = 3.0 #hours
    stopTime = time.time() + (timeLimit*3600.0)

    date = 'May_4'
    d = dish.Dish(verbose=True)
    s = dish_synth.Synth()
    obs = ephem.Observer()
    obs.lat = 37.832*np.pi/180
    obs.long = -122.2573*np.pi/180
    #d.home()
    b_lat = np.loadtxt('gal_lat_b.gz')
    l_long = np.loadtxt('gal_long_l.gz')
    for i in range (0, len(l_long), 1):
        if time.time() > stopTime:
            break
        sys.stdout = open('obs_log_May_4.txt', 'a')
        b = b_lat[i]
        l = l_long[i]
        #lower LO frequency
        s.set_amp(10.0)
        s.set_freq(1272.4)
        s.set_amp(10.0)
        try:
            az, alt= gal_to_eq(b_lat[i], l_long[i])
            d.point(az, alt, validate=True)
        except ValueError:
            print 'invalid pointing, skipping point'
            continue
        #if pointing fails, will move on to the next pointing (go back to for loop)
        while True:
            try:
                d.point(az, alt)
                break
            except:
                print 'Pointing failed, trying again'
        while True:
            try:
                d.noise_off()
                break
            except:
                print "Turning noise off failed, trying again"
        obs.date = ephem.now()
        LST = obs.sidereal_time()
        takespec.takeSpec('spec_low_freq_noise_off_%s_%s_%s_%s.gz' % (b, l, LST, date), numSpec=120)
        print 'low freq noise off spectra done, b = %s, l = %s' % (b, l)
        while True:
            try:
                d.noise_on()
                break
            except:
                print "Turning noise on failed, trying again"
        obs.date = ephem.now()
        LST = obs.sidereal_time()
        takespec.takeSpec('spec_low_freq_noise_on_%s_%s_%s_%s.gz' % (b, l, LST, date), numSpec=40)
        print 'low freq noise on spectra done, b = %s, l = %s' % (b, l)

        #higher LO frequency
        s.set_amp(10.0)
        s.set_freq(1268.4)
        s.set_amp(10.0)
        try:
            az, alt= gal_to_eq(b_lat[i], l_long[i])
            d.point(az, alt,validate=True)
        except ValueError:
            print "invalid pointing, skipping point"
            continue
        while True:
            try:
                d.point(az, alt)
                break
            except:
                print "Pointing failed, trying again"
        while True:
            try:
                d.noise_off()
                break
            except:
                print "Turning noise off failed, trying again"
        obs.date = ephem.now()
        LST = obs.sidereal_time()
        takespec.takeSpec('spec_up_freq_noise_off_%s_%s_%s_%s.gz' % (b, l, LST, date), numSpec=120)
        print 'upper lo freq noise off spectra done, b = %s, l = %s' % (b, l)
        while True:
            try:
                d.noise_on()
                break
            except:
                print "Turning noise on failed, trying again"
        obs.date = ephem.now()
        LST = obs.sidereal_time()
        takespec.takeSpec('spec_up_freq_noise_on_%s_%s_%s_%s.gz' % (b, l, LST, date), numSpec=40)
        print 'upper lo freq noise on spectra done, b = %s, l = %s' % (b, l)



######

if __name__ == '__main__':
    time.sleep(5)
    if len(sys.argv) == 1:
        timeLimit = 2.8
    else:
        timeLimit = sys.argv[1]

    data_taker()
    sys.stdout.close()
