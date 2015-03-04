#!/usr/bin/env python

# ========================================================================== #
# File: handle_data.py                                                       #
# Programmer: Patrick Kantorski                                              #
# Date: 05/04/14                                                             #
# Class: Astronomy 121 - Radio Astronomy Lab                                 #
# Time: T 6:00-9:00 PM                                                       #
# Instructor: Aaron Parsons                                                  #
# Description: This program was written in Python to manipulate and convert  #
#              temperature calibrated data files into a file with velocity,  #
#              distance, Julian date, and more.                              #
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
import ugdoppler as ugd

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt


def main():

    ### Combine data files... ###
    #path_1 = "/Users/ppkantorski/Documents/Radio_Astronomy/Lab_4/Data/Clean/May_4_1-7.npz"
    #path_2 = "/Users/ppkantorski/Documents/Radio_Astronomy/Lab_4/Data/Clean/May_4_8-35.npz"

    #combine_npz(path_1, path_2)
    
    path_1 = "/Users/ppkantorski/Documents/Radio_Astronomy/Lab_4/Data/Clean/May_4_final.npz"

    create_data(path_1)

    path_1 = "/Users/ppkantorski/Documents/Radio_Astronomy/Lab_4/Data/Clean/May_4_final_final.npz"
    file = np.load(path_1)
    
    temp = file['Temp']
    distance = file['Distance']
    velocity = file['Velocity']
    b = file['b']
    print file['LSR']
    
    print b
    
    # height
    height = []
   
   
    plt.subplot(1, 2, 1)
    plt.ylim([1, 160])
    plt.xlim([0, 30])
    #plt.xlim([-200, 200])
    raw_graph(distance, temp, 'Distance (kpc)', 'Temperature (K)', 'k')
   
   
    for i in range(len(b)):
        height.append(np.tan(b[i]*np.pi/180)*distance[i])
    
    plt.subplot(1, 2, 2)
    raw_graph(distance, height, 'Distance (kpc)', 'Height (kpc)', 'k', '.')
    #plt.ylim([1, 160])
    #plt.xlim([-200, 200])
    plt.axvline(0, color='r', linestyle='--', linewidth=2)
    plt.ylim([-15, 15])
    plt.xlim([0, 30])
    
    plt.tight_layout()
    plot = raw_input("Plot data for May 4 complete data? (y|n|r):")
    prompt_plot(plot)
    
    
    temp_list = [[] for i in range(0,35)]
    for j in range(0, 35):
        temp_2 = []
        for i in range(0, 2000):
            temp_1 = np.average(temp[j])
            temp_2.append(temp_1)
        temp_list[j] = temp_2
        
    plt.contourf(distance, height, temp_list)
    plt.colorbar()
    plt.title('contourf with levels')
    plt.ylim([-15, 15])
    plt.xlim([0, 30])
    plt.show()
    
    
    raw_graph(velocity, temp, 'Velocity (km/s)')
    plot = raw_input("Plot data for May 4 complete data? (y|n|r):")
    prompt_plot(plot)


def gal_to_eq(b_lat, l_long):

    R = np.zeros([3,3])
    R[0] = [-0.054876, -0.873437, -0.483835]
    R[1] = [0.494109, -0.444830, 0.746982]
    R[2] = [-0.867666, -0.198076, 0.455984]
    trans_R = np.transpose(R)

    x = np.array([0.,0,0])
    x[0] = np.cos(b_lat*np.pi/180)*np.cos(l_long*np.pi/180)
    x[1] = np.cos(b_lat*np.pi/180)*np.sin(l_long*np.pi/180)
    x[2] = np.sin(b_lat*np.pi/180)

    A = np.dot(trans_R, x)

    ra = np.arctan2(A[1], A[0])*(180/np.pi) * 24/360 # Angular hours..
    dec = np.arcsin(A[2])*(180/np.pi)
    
    return (ra, dec)
    
    
def doppler_convert(freq_data, b, l, LSR):
    # Center frequency...
    center_f = 1420.4
    
    # Doppler conversion...
    v_doppler = -spc.c*(freq_data - center_f)/center_f * 1/1000
    print LSR, v_doppler
    v_doppler = (v_doppler - LSR)/np.cos(b*np.pi/180)
    
    return v_doppler


def distance_convert(v_doppler, b, l):
    v_0 = 220 #220 km/s
    d_0 = 8.0 #kiloparsecs    
    
    
    if v_doppler < 0:
        alpha = np.arcsin(v_doppler/v_0 + np.sin(l*np.pi/180)) + l*np.pi/180
    if v_doppler > 0:
        alpha = np.arcsin(-v_doppler/v_0 + np.sin(l*np.pi/180)) + l*np.pi/180
    distance = (d_0*np.sin(np.pi/2- l*np.pi/180) + d_0*np.sin(l*np.pi/180) * np.tan(np.pi/2 - alpha + l*np.pi/180))
    
    #distance = []
    #for i in range(len(v_doppler)):
    #    if v_doppler[i] < v_0*(1 - np.sin(l*np.pi/180)):
    #        alpha = np.arcsin(v_doppler[i]/v_0 + np.sin(l*np.pi/180)) + l*np.pi/180
    #        distance.append(d_0*np.sin(np.pi/2- l*np.pi/180) + d_0*np.sin(l*np.pi/180) * np.tan(np.pi/2 - alpha + l*np.pi/180))
    #    else:
    #        distance.append(0)
    
    return distance


def create_data(path_1):
    num = []
    date = []
    jd = []
    ra = []
    dec = []
    b = []
    l = []
    LSR = []
    freq_data = []
    temp_data = []
    velocity = []
    distance = []
   

    count = load_final_npz(path_1)[0]
    
    raw_input("Create final dataset? ")
    
    for i in range(len(count)):
        number_1 = load_final_npz(path_1)[0][i]
        num.append(number_1)
        date_1 = load_final_npz(path_1)[1][i]
        date.append(date_1)
        time_1 = load_final_npz(path_1)[2]
        time_1 = time_1[i].partition(',')[0]
        
        b_1 = np.float(load_final_npz(path_1)[3][i])
        b.append(b_1)
        l_1 = np.float(load_final_npz(path_1)[4][i])
        l.append(l_1)
    
        freq_data_1 = load_final_npz(path_1)[5][i]
        freq_data.append(freq_data_1)
        temp_data_1 = load_final_npz(path_1)[6][i]
        temp_data.append(temp_data_1)
    
        ra_1 = gal_to_eq(b_1, l_1)[0]
        ra.append(ra_1)
        dec_1 = gal_to_eq(b_1, l_1)[1]
        dec.append(dec_1)
    
        jd_1 = ephem.julian_date('2014/5/4 '+str(time_1))
        jd.append(jd_1)
        LSR_1 = np.float(ugd.ugdoppler(ra_1, dec_1, jd_1, nlat=37.8732, wlong=+122.2573)[3])
        LSR.append(LSR_1)
        v_1 = doppler_convert(freq_data_1, b_1, l_1, LSR_1)
        velocity.append(v_1)
        distance_1 = distance_convert(v_1, b_1, l_1)
        distance.append(distance_1)
    
        print 'Number:', number_1
        print 'Date:', date_1
        print 'Time:', time_1
        print 'JD:', jd_1
        print 'LSR:', LSR_1
        print 'b lat:', b_1
        print 'l long:', l_1
        print 'ra:', ra_1
        print 'dec:', dec_1
        print "Distance:", distance_1
        
        np.savez('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_4/Data/Clean/May_4_done', Number= num, Date=date, JD=jd, RA= ra, DEC= dec,
        b= b, l=l, LSR=LSR, Freq=freq_data, Temp=temp_data, Velocity=velocity, Distance=distance)


def load_npz(path):
    file = np.load(path)

    num = file['Number']
    date = file['Date']
    time_1 = file['Time_1']
    time_2 = file['Time_2']
    time_3 = file['Time_3']
    time_4 = file['Time_4']
    b = file['b']
    l = file['l']
    time = []
    
    for i in range(len(time_1)):
        time.append(time_1[i]+', '+time_2[i]+', '+time_3[i]+', '+time_4[i])
    
    freq_data = file['Freq']
    temp_data = file['Temp']
    
    #print num[0]
    #print name[0]
    #print freq_data[0]
    #print temp_data[0]
    
    return num, date, time, b, l, freq_data, temp_data


def load_final_npz(path):
    file = np.load(path)
    num = file['Number']
    date = file['Date']
    time = file['Time']
    b = file['b']
    l = file['l']
    freq_data = file['Freq']
    temp_data = file['Temp']
    #print num[0]
    #print name[0]
    #print freq_data[0]
    #print temp_data[0]
    return num, date, time, b, l, freq_data, temp_data


def combine_npz(path_1, path_2):

    number_1 = load_npz(path_1)[0]
    date_1 = load_npz(path_1)[1]
    time_1 = load_npz(path_1)[2]
    b_1 = load_npz(path_1)[3]
    l_1 = load_npz(path_1)[4]
    x_data_1 = load_npz(path_1)[5]
    y_data_1 = load_npz(path_1)[6]
    
    number_2 = load_npz(path_2)[0]
    date_2 = load_npz(path_2)[1]
    time_2 = load_npz(path_2)[2]
    b_2 = load_npz(path_2)[3]
    l_2 = load_npz(path_2)[4]
    x_data_2 = load_npz(path_2)[5]
    y_data_2 = load_npz(path_2)[6]
    
    num = np.r_[number_1, number_2]
    date = np.r_[date_2, date_2]
    time = np.r_[time_1, time_2]
    b = np.r_[b_1, b_2]
    l = np.r_[l_1, l_2]
    freq_data = np.r_[x_data_1, x_data_2]
    temp_data = np.r_[y_data_1, y_data_2]
    
    print("Saving data... ")
    np.savez('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_4/Data/Clean/May_4', Number= num, Date=date, Time=time, Freq=freq_data, Temp=temp_data, b=b, l=l)


def prompt_plot(plot):
    while plot != 'y' and plot != 'Y' and plot != 'N' and plot != 'n' and plot != 'R' and plot != 'r': 
		plot = raw_input("Please enter (y/n) or (r): ")
    if plot == 'Y' or plot == 'y':
        plt.show()
    elif plot == 'N' or plot == 'n':
        plt.clf()
    elif plot == 'R' or plot == 'r':
        print("\n===========================================================================================")
        plt.clf()
        reboot()
        

def raw_graph(x_data, y_data, xlabel, ylabel, c = 'b', style = '-'):
    
    plt.plot(x_data, y_data, style, color=c, linewidth=1)
    #plt.axis([0,.5,-2e6,2e6])
    plt.xlabel(xlabel, fontsize=20)
    plt.ylabel(ylabel, fontsize=20)
    #plt.title('Digital Mixing with'+ r' $\nu_{sig}=1.05 \times\ \nu_{lo}$' ,size=22)


def reboot():
    # Reboot script.
    os.system("/Users/ppkantorski/Documents/Radio_Astronomy/Lab_4/Code/handle_data.py")
    sys.exit()



if __name__ == '__main__':
	main()