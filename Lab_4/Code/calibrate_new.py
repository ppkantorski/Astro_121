#!/usr/bin/env python

# ========================================================================== #
# File: calibrate_new.py                                                     #
# Programmer: Patrick Kantorski                                              #
# Date: 05/04/14                                                             #
# Class: Astronomy 121 - Radio Astronomy Lab                                 #
# Time: T 6:00-9:00 PM                                                       #
# Instructor: Aaron Parsons                                                  #
# Description: This program was written in Python to calibrate data taken    #
#              from the 4.5m radio telescope at the Leuschner Observatory    #
#              into units of temperature.                                    #
# ========================================================================== #

import numpy as np
import numpy.fft as fft
import matplotlib.pyplot as plt
import readspec_mod as rsm
import scipy.constants as spc
import scipy.optimize as optimize
import os
import sys


def main():
    # Q: Why is center frequency skewed by 150MHz again?
    fc = 1272.4 + 150
    
    ### Load data files... ###
    # Iteration variables for loops.
    loop = 1
    var = 0
    
    # Restart program where broken..
    #loop = 1
    var = 9 -1

    # Initializing identification number and lists for .npz file.
    number = 1
    #number = 8
    num = []
    date = []
    time_1 = []
    time_2 = []
    time_3 = []
    time_4 = []
    freq_data = []
    temp_data = []
    b = []
    l = []
    
    data_select = raw_input("Enter dataset for analysis: ")
    while loop <= 1:
        #print("\n===========================================================================================\n")
        if data_select == "May_2" or data_select == 'first':
            data_select = "May_2"
            with open ('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_4/Data/file_lists/May_2_low_on_fixed.txt', "r") as myfile:
                data_1 = myfile.readlines()
                len_data = len(data_1)
            with open ('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_4/Data/file_lists/May_2_low_off_fixed.txt', "r") as myfile:
                data_2 = myfile.readlines()
                #len_data = len(data)
            with open ('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_4/Data/file_lists/May_2_up_on_fixed.txt', "r") as myfile:
                data_3 = myfile.readlines()
                #len_data = len(data)
            with open ('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_4/Data/file_lists/May_2_up_off_fixed.txt', "r") as myfile:
                data_4 = myfile.readlines()
                #len_data = len(data)
        
            with open ('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_4/Data/file_lists/May_2_low_on_names.txt', "r") as myfile:
                n_1 = myfile.readlines()
            with open ('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_4/Data/file_lists/May_2_low_off_names.txt', "r") as myfile:
                n_2 = myfile.readlines()
                #len_data = len(data)
            with open ('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_4/Data/file_lists/May_2_up_on_names.txt', "r") as myfile:
                n_3 = myfile.readlines()
                #len_data = len(data)
            with open ('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_4/Data/file_lists/May_2_up_off_names.txt', "r") as myfile:
                n_4 = myfile.readlines()
                #len_data = len(data)

        if data_select == "May_3" or data_select == "second":
            data_select = "May_3"
            with open ('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_4/Data/file_lists/May_3_low_on_fixed.txt', "r") as myfile:
                data_1 = myfile.readlines()
                len_data = len(data_1)
            with open ('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_4/Data/file_lists/May_3_low_off_fixed.txt', "r") as myfile:
                data_2 = myfile.readlines()
                #len_data = len(data)
            with open ('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_4/Data/file_lists/May_3_up_on_fixed.txt', "r") as myfile:
                data_3 = myfile.readlines()
                #len_data = len(data)
            with open ('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_4/Data/file_lists/May_3_up_off_fixed.txt', "r") as myfile:
                data_4 = myfile.readlines()
                #len_data = len(data)
                
            with open ('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_4/Data/file_lists/May_3_low_on_names.txt', "r") as myfile:
                n_1 = myfile.readlines()
            with open ('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_4/Data/file_lists/May_3_low_off_names.txt', "r") as myfile:
                n_2 = myfile.readlines()
                #len_data = len(data)
            with open ('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_4/Data/file_lists/May_3_up_on_names.txt', "r") as myfile:
                n_3 = myfile.readlines()
                #len_data = len(data)
            with open ('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_4/Data/file_lists/May_3_up_off_names.txt', "r") as myfile:
                n_4 = myfile.readlines()
                #len_data = len(data)
                
        if data_select == "May_4" or data_select == "final":
            data_select = "May_4"
            with open ('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_4/Data/file_lists/May_4_low_on_fixed.txt', "r") as myfile:
                data_1 = myfile.readlines()
                len_data = len(data_1)
            with open ('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_4/Data/file_lists/May_4_low_off_fixed.txt', "r") as myfile:
                data_2 = myfile.readlines()
                #len_data = len(data)
            with open ('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_4/Data/file_lists/May_4_up_on_fixed.txt', "r") as myfile:
                data_3 = myfile.readlines()
                #len_data = len(data)
            with open ('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_4/Data/file_lists/May_4_up_off_fixed.txt', "r") as myfile:
                data_4 = myfile.readlines()
                #len_data = len(data)
                
            with open ('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_4/Data/file_lists/May_4_low_on_names.txt', "r") as myfile:
                n_1 = myfile.readlines()
            with open ('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_4/Data/file_lists/May_4_low_off_names.txt', "r") as myfile:
                n_2 = myfile.readlines()
                #len_data = len(data)
            with open ('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_4/Data/file_lists/May_4_up_on_names.txt', "r") as myfile:
                n_3 = myfile.readlines()
                #len_data = len(data)
            with open ('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_4/Data/file_lists/May_4_up_off_names.txt', "r") as myfile:
                n_4 = myfile.readlines()
                #len_data = len(data)

        elif data_select != "May_2" and data_select != "May_3" and data_select != "May_4":
            break
    
        while var < len_data:
            try:
                if data_select == "May_2" or data_select == "May_3" or data_select == "May_4":
                    file_on = data_1[var].rstrip()
                    file_off = data_2[var].rstrip()
                    file_on_low = data_3[var].rstrip()
                    file_off_low = data_4[var].rstrip()
                
                    name_on = n_1[var].rstrip()
                    name_off = n_2[var].rstrip()
                    name_low_on = n_3[var].rstrip()
                    name_low_off = n_4[var].rstrip()
                
                
                    print("\n===========================================================================================\n")
                    print("---Entry # "+str(number)+"---")
                
                    print("Files with Directory:")
                    print(file_on)
                    print(file_off)
                    print(file_on_low)
                    print(file_off_low)
                
                    try:
                        print "\nObservation Information: "
                        print "Date:", name_off.split(" ")[3], name_off.split(" ")[4]
                        print "Time 1:",name_off.split(" ")[2]
                        print "Time 2 (noise):", name_on.split(" ")[2]
                        print "Time 3 (LO shift):", name_low_off.split(" ")[2]
                        print "Time 4 (LO shift + noise):", name_low_on.split(" ")[2]
                        print "Coordinates (b, l): ", name_on.split(" ")[0], name_on.split(" ")[1]
                        print("\n===========================================================================================")
                    
                    except IndexError:
                        print "Not all files for data exist!"
            
                # Radius for boxcar filter...
                radius = 11     

                # Loading Files...
                y_on = np.mean(rsm.readSpec(file_on), 1)
                y_off = np.mean(rsm.readSpec(file_off), 1)
                y_on_low = np.mean(rsm.readSpec(file_on_low), 1)
                y_off_low = np.mean(rsm.readSpec(file_off_low), 1)
                print len(y_off), len(y_on), len(y_off_low), len(y_on_low)
            
            
                ### Plotting Raw data... ###
                ### Raw data for noise on... ###
                f_range = np.linspace(fc-6, fc+6, y_on.shape[0])
                f_range_on = np.linspace(fc-6, fc+6, y_on.shape[0])
                gen_graph(f_range_on, y_on, radius)
                ######################################

                ### Raw data for noise off... ###
                f_range = np.linspace(fc-6, fc+6, y_off.shape[0])
                f_range_off = np.linspace(fc-6, fc+6, y_off.shape[0])
                gen_graph(f_range_off, y_off, radius)
                #######################################
    
                ### Raw data for noise on with shifted LO... ###
                f_range = np.linspace(fc-6, fc+6, y_on_low.shape[0])
                f_range_on_low = np.linspace(fc-6, fc+6, y_on_low.shape[0])
                gen_graph(f_range_on_low, y_on_low, radius, 'b')
                ################################################
            
                ### Raw data for noise off with shifted LO... ###
                f_range = np.linspace(fc-6, fc+6, y_off_low.shape[0])
                f_range_off_low = np.linspace(fc-6, fc+6, y_off_low.shape[0])
                gen_graph(f_range_off_low, y_off_low, radius, 'b')

                # Print cleaned data graphs...
                plot = raw_input("\nPlot raw data? (y|n|r): ")
                plt.ylim([1, 350])
                plt.xlim([1416, 1429])
                prompt_plot(plot)
                ############################
            
    
                ### Cleaning data for noise on... ###
                f_range = np.linspace(fc-6, fc+6, y_on.shape[0])
                y_med = box_car(y_on, radius)
                y_norm = y_on - y_med
    
                index = []
                # Removing spikes from data..
                for i in range(y_norm.size):
                    if i == len(y_norm):
                        break
                    if f_range[i] >= 0:
                        if y_norm[i] < -4*np.std(y_norm):
                            index.append(i)
                        if y_norm[i] > 4*np.std(y_norm):
                            index.append(i)
    
                #print len(y_on), len(y_med)
                for i in index:
                    if i >= len(y_med):
                        break
                    y_on[i] = y_med[i]
    

                f_range_on = np.linspace(fc-6, fc+6, y_on.shape[0])
                gen_graph(f_range_on, y_on, radius)
                ######################################


                ### Cleaning data for noise off... ###
                f_range = np.linspace(fc-6, fc+6, y_off.shape[0])
                y_med = box_car(y_off, radius)
                y_norm = y_off - y_med
    
                index = []
                std = 4*np.std(y_norm)
                print "4x Standard Deviation:", std
                for i in range(y_norm.size):
                    if i == len(y_norm):
                        break
                    if f_range[i] >= 0:
                        if y_norm[i] < -4*np.std(y_norm):
                            index.append(i)
                        if y_norm[i] > 4*np.std(y_norm):
                            index.append(i)
    
                for i in index:
                    if i >= len(y_med):
                        break
                    y_off[i] = y_med[i]
    
                f_range_off = np.linspace(fc-6, fc+6, y_off.shape[0])
                gen_graph(f_range_off, y_off, radius)
                #######################################
    
    
                ### Cleaning data for noise on with shifted LO... ###
                f_range = np.linspace(fc-6, fc+6, y_on_low.shape[0])
                y_med = box_car(y_on_low, radius)
                y_norm = y_on_low - y_med
    
                index = []
                for i in range(y_norm.size):
                    if i == len(y_norm):
                        break
                    if f_range[i] >= 0:
                        if y_norm[i] < -4*np.std(y_norm):
                            index.append(i)
                        if y_norm[i] > 4*np.std(y_norm):
                            index.append(i)

                for i in index:
                    if i >= len(y_med):
                        break
                    y_on_low[i] = y_med[i]

    
                f_range_on_low = np.linspace(fc-6, fc+6, y_on_low.shape[0])
                gen_graph(f_range_on_low, y_on_low, radius)
                #####################################################


                ### Cleaning data for noise off with shifted LO... ###
                f_range = np.linspace(fc-6, fc+6, y_off_low.shape[0])
                #y_med = average(f_range, y_off_low, radius)
                y_med = box_car(y_off_low, radius)
                y_norm = y_off_low - y_med
    
                index = []
                for i in range(y_norm.size):
                    if i == len(y_norm):
                        break
                    if f_range[i] >= 0:
                        if y_norm[i] < -4*np.std(y_norm):
                            index.append(i)
                        if y_norm[i] > 4*np.std(y_norm):
                            index.append(i)
                
                for i in index:
                    if i >= len(y_med):
                        break
                    y_off_low[i] = y_med[i]
    

                f_range_off_low = np.linspace(fc-6, fc+6, y_off_low.shape[0])
                gen_graph(f_range_off_low, y_off_low, radius)

                # Print cleaned data graphs...
                plot = raw_input("Plot cleaned data? (y|n|r): ")
                prompt_plot(plot)
                ######################################################


                ### Finding difference b/w noise on and off... ###
                y_diff_1 = y_on - y_off
                y_diff_2 = y_on_low - y_off_low
                gen_diff_graph(f_range_off, f_range_off_low, y_diff_1, y_diff_2)
    
                # Print gain calculation graphs..
                plot = raw_input("Plot difference between on and off? (y|n|r): ")
                prompt_plot(plot)
                #################################################
    
    
                ### Finding the gain correction... ###
                T_noise = 100

                
                P_off = np.sum(y_diff_1)/T_noise
                t_sys_off = np.sum(y_on)/P_off
                P_off_low = np.sum(y_diff_2)/T_noise
                t_sys_off_low = np.sum(y_on_low)/P_off_low

                gain_factor = np.sum(y_off)/np.sum(y_off_low)

                y_off_temp = y_off
                y_off_low_temp = y_off_low * gain_factor
            
                gen_diff_graph(f_range_off, f_range_off_low, y_off_temp, y_off_low_temp)
                # Print temperature graphs...
                plot = raw_input("Plot off data with gain conversion? (y|n|r): ")
                prompt_plot(plot)
                #######################################
    
    
                ### Plot both data on same plot! ###
                plt.subplot(1, 2, 1)
                gen_graph(f_range_off, y_off_temp, radius)
                gen_graph(f_range_off_low, y_off_low_temp, radius, 'b')
    
                # Print both graphs...
                #plot = raw_input("Plot cleaned data on same plot? (y|n|r): ")
                plt.ylim([40, 100])
                plt.xlim([1416, 1429])
                #prompt_plot(plot)
                ####################################
    
    
                ### Cleaning temperature graphs! ###
                # Noise off, regular LO!
                y_med = box_car(y_off_temp, radius)
                y_norm = y_off_temp - y_med

                index = []
                for i in range(y_norm.size):
                    if i == len(y_norm):
                        break
                    if f_range_off_low[i] >= 0:
                        if y_norm[i] < 4*np.std(y_norm):
                            index.append(i)
                        if y_norm[i] > -4*np.std(y_norm):
                            index.append(i)
    
                for i in index:
                    if i >= len(y_med):
                        break
                    y_off_temp[i] = y_med[i]
    
                gen_graph(f_range_off, y_off_temp, radius)

                # Print temperature graphs...
                #plot = raw_input("Plot 1st for cleaning? (y|n|r): ")
                #prompt_plot(plot)
    
                # Noise off, LO shift!
                y_med = box_car(y_off_low_temp, radius)
                y_norm = y_off_low_temp - y_med
    
                index = []
                for i in range(y_norm.size):
                    if i == len(y_norm):
                        break
                    if f_range_off_low[i] >= 0:
                        if y_norm[i] < 4*np.std(y_norm):
                            index.append(i)
                        if y_norm[i] > -4*np.std(y_norm):
                            index.append(i)
    
                for i in index:
                    if i >= len(y_med):
                        break
                    y_off_low_temp[i] = y_med[i]
    
                gen_graph(f_range_off_low, y_off_low_temp, radius)
    
                # Print temperature graphs...
                #plot = raw_input("Plot 2nd for cleaning? (y|n|r): ")
                #prompt_plot(plot)
                ####################################


                ### Plot both data on same plot! ###
                plt.subplot(1, 2, 2)
                gen_graph(f_range_off, y_off_temp, radius)
                gen_graph(f_range_off_low, y_off_low_temp, radius, 'b')
    
                # Print both graphs...
                plot = raw_input("Plot cleaned data on same plot? (y|n|r): ")
                plt.ylim([40, 100])
                plt.xlim([1416, 1429])
                prompt_plot(plot)
                ####################################
    
    
                ### Extracting shape! ###
                #for i in range(y_off_temp.size):
                #    if i == len(y_off_temp):
                #        break
                #    if f_range[i] > 1422 and f_range[i] < 1422.1:
                #        print i
                #i = 3823
                center_1 = 2731
                center_2 = 5461
                width = 1000
    
                y_off_cut = y_off_temp[center_1-width:center_1+width]
                y_off_cut_empty = y_off_temp[center_2-width:center_2+width]
            
                y_off_low_cut = y_off_low_temp[center_2-width:center_2+width]
                y_off_low_cut_empty = y_off_low_temp[center_1-width:center_1+width]
                # Recenter data for shifted LO.
                f_range_off = f_range_off[center_1-width:center_1+width]
                f_range_off_low = f_range_off_low[center_2-width:center_2+width] - 4
                #########################

    
                ### Plotting difference b/w last two plots. ###
                gen_diff_graph(f_range_off, f_range_off_low, y_off_cut, y_off_low_cut)
            
                # Print gain calculation graphs...
                plot = raw_input("Plot recentered & truncated data? (y|n|r): ")
                prompt_plot(plot)
                #########################################


                ### Temperature calibrated data!! Finally! ###
            
                y_off_cut = (y_off_cut/y_off_low_cut_empty- 1) * t_sys_off
                y_off_low_cut = (y_off_low_cut/y_off_cut_empty - 1) * t_sys_off_low
                gen_diff_graph(f_range_off, f_range_off_low, y_off_cut, y_off_low_cut)
            
                # Print gain calculation graphs...
                plot = raw_input("Plot temperature calibrated data? (y|n|r): ")
                prompt_plot(plot)
                ##############################################


                ### Plot normalized data using polyfit! ###
                #center = 1087

            
                # Width of H1 Line...
                #H1_width = 200
                
                test_width = True
                while test_width == True:
                    if std > 1:
                        # Plot to find width of H1 line...
                        
                        plt.plot(y_off_cut)
                        plt.plot(y_off_low_cut, 'k')
                        plot = raw_input("Plot data to find width of H1 line? (y|n|r): ")
                        prompt_plot(plot)
                        
                        H1_width = raw_input("\nEnter width for H1 line (default = 200pts): ")
                        if not H1_width:
                            H1_width = str(200)
                        while H1_width.isdigit() != True: 
                            H1_width = raw_input("Please enter integer value: ")
                        H1_width = int(H1_width)
                        
                        center= raw_input("Enter center of H1 line (default = max value): ")
                        if not center:
                            for i in range(y_off_cut.size):
                                if i == len(y_off_cut):
                                    break
                                #if f_range_off[i] > 1420.5 and f_range_off[i] < 1420.56:
                                #    print i
                                if y_off_cut[i] == max(y_off_cut):
                                    center = str(i)
                        while center.isdigit() != True: 
                            center = raw_input("Please enter integer value: ")
                        center = int(center)
                        
                    else:
                        center = 200
                        H1_width = 200
            
                    x_fit_1 = np.delete(f_range_off, np.s_[center-H1_width:center+H1_width])
                    x_fit_2 = np.delete(f_range_off_low, np.s_[center-H1_width:center+H1_width])
                    y_fit_1 = np.delete(y_off_cut, np.s_[center-H1_width:center+H1_width])
                    y_fit_2 = np.delete(y_off_low_cut, np.s_[center-H1_width:center+H1_width])
    
                    if std > 1:
                        gen_diff_graph(x_fit_1, x_fit_2, y_fit_1, y_fit_2, radius, 'b')
                        plot = raw_input("Plot data with H1 removed? (y|n|r): ")
                        prompt_plot(plot)
    
                    c_1 = np.polyfit(x_fit_1, y_fit_1, 5)
                    c_2 = np.polyfit(x_fit_2, y_fit_2, 5)
    
                    fit_1 = c_1[0]*f_range_off**5 + c_1[1]*f_range_off**4 + c_1[2]*f_range_off**3 + c_1[3]*f_range_off**2 + c_1[4]*f_range_off**1 + c_1[5]
                    fit_2 = c_2[0]*f_range_off_low**5 + c_2[1]*f_range_off_low**4 + c_2[2]*f_range_off_low**3 + c_2[3]*f_range_off_low**2 + c_2[4]*f_range_off_low**1 + c_2[5]

                    if std > 1:
                        gen_diff_graph(f_range_off, f_range_off_low, y_off_cut, y_off_low_cut, radius, 'b', 'k')
                        gen_diff_graph(f_range_off, f_range_off_low, fit_1, fit_2, radius, 'r', 'r', 2)
    
                        # Print gain calculation graphs...
                        plot = raw_input("Plot polynomial fit? (y|n|r): ")
                        prompt_plot(plot)
                        while True:
                            try:
                                done = raw_input('Good fit? (y|n): ')
                                if done == 'Y' or done == 'y':
                                    test_width = False
                                if done == 'N' or done == 'n':
                                    test_width = True
                            except (SyntaxError, ValueError, IndexError):
                                continue
                            break
                    else:
                        test_width = False
                        
                
                #########################################


                ### Final recentering of data!!! ###
                gen_graph(f_range_off, y_off_cut-fit_1, radius, 'k')
                gen_graph(f_range_off_low, y_off_low_cut-fit_2, radius, 'b')
    
                # Print gain calculation graphs...
                plot = raw_input("Plot final recentered graph? (y|n|r): ")
                prompt_plot(plot)
                ####################################


                ### Final plot! ###
                y_data_1 = (y_off_cut-fit_1)
                y_data_2 = (y_off_low_cut-fit_2)
                y_data = (y_data_1 + y_data_2)/2
                x_data = (f_range_off + f_range_off_low)/2
                
                if std > 1:
                    gen_graph(x_data, y_data, radius, 'g')
                    # Print gain calculation graphs...
                    plot = raw_input("Plot calibrated data? (y|n|r): ")
                    prompt_plot(plot)
                ####################################


                ### Saving data output! ###
                # Fix name!
                print "Data point skipped? : ", np.isnan(y_data[10])
                try:
                    if np.isnan(y_data[10]) == False:
                        time_1.append(name_off.split(" ")[2])
                        time_2.append(name_on.split(" ")[2])
                        time_3.append(name_low_off.split(" ")[2])
                        time_4.append(name_low_on.split(" ")[2])
                        date.append(name_off.split(" ")[3]+" "+name_off.split(" ")[4])
            
                        num.append(number)
                        freq_data.append(x_data)
                        temp_data.append(y_data)
                
                        b.append(name_on.split(" ")[0])
                        l.append(name_on.split(" ")[1])

                        #print("Number: "+str(num))
                        #print("Name: "+str(name))
            
                        np.savez('/Users/ppkantorski/Documents/Radio_Astronomy/Lab_4/Data/Clean/'+data_select, Number= num, Date=date, Time_1= time_1, Time_2= time_2, Time_3= time_3, Time_4= time_4, Freq=freq_data, Temp=temp_data, b=b, l=l)
                        number += 1
                    else:
                        print "Dataset is empty! Entries were skipped!"
                except IndexError:
                    print "Dataset is missing! Entries were skipped!"

                ############################
            
            except (ValueError, IndexError):
                print "Dataset is missing! Entries were skipped!"
                finish = 1
                loop = 1
                var = var + 1
                continue

            # Skips to next dataset.
            finish = 1
            loop = 1
            var = var + 1
            # Checks to see if data verification is complete.
#            while finish == 1:
#                x = raw_input("\nNext dataset? (y/n) ")
#                if x != 'y' and x != 'Y' and x != 'n' and x != 'N':
#                    a = True
#                    while a == True:
#                        x = raw_input("Please enter (y/n): ")
#                        if x == 'y' or x == 'Y' or x == 'n' or x == 'N':
#                            a = False
#                if x == 'Y' or x == 'y':
#                    loop = 1
#                    finish = 2
#                    var = var + 1
#                    print('\n')
        
#                elif x == 'N' or x == 'n':
#                    loop = 2
#                    finish = 2
#                    var = len_data
#                    print('\n')                  


    ### Run script again... ###
    print("===========================================================================================")
    again = raw_input("Run calibrate.py again? (y/n): ")
    while again != 'y' and again != 'Y' and again != 'N' and again != 'n': 
        again = raw_input("Please enter (y/n): ")
    if again == 'Y' or again == 'y':
        print("\n===========================================================================================")
        reboot()
    elif again == 'N' or again == 'n':
        print("\n===========================================================================================")
        print('All process are complete!')
        sys.exit()
    ###########################
    


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
        
  
def gen_graph(x_data, y_data, radius=11, c = 'k'):
    n = 1
    while n < 2:
        #plt.subplot(2, 1, n)
        if n == 1:
            raw_graph(x_data, y_data, radius, c)
        #if n == 2:
        #    smooth_graph(x_data, y_data, radius)
        #if n == 3:
        #    gain_graph(x_data, y_data)
        n += 1
        
    plt.rc('xtick', labelsize=12)
    plt.rc('ytick', labelsize=12)
    #plt.title('Galactic Coordinates: long=$220^{\circ}$ lat=$0^{\circ}$\nLO=1272.4MHz 04/22 at 21:40 PDT')
    plt.xlabel('Frequency (MHz)', fontsize=20)
    
    plt.tight_layout()
    #plt.show()


def gen_diff_graph(x_1, x_2, y_1, y_2, radius=11, c='b', c2='k', l=1):
    n = 1
    while n < 3:
        plt.subplot(1, 2, n)
        if n == 1:
            raw_graph(x_1, y_1, radius, c, l)
        if n == 2:
            raw_graph(x_2, y_2, radius, c2, l)
        #if n == 3:
        #    gain_graph(x_data, y_data)
        n += 1
        
    plt.rc('xtick', labelsize=12)
    plt.rc('ytick', labelsize=12)
    #plt.title('Galactic Coordinates: long=$220^{\circ}$ lat=$0^{\circ}$\nLO=1272.4MHz 04/22 at 21:40 PDT')
    #plt.xlabel('MHz')
    
    plt.tight_layout()
    #plt.show()


def average(x_data, y_data, radius=11):
    n = radius
    y_med = np.array([])
    for i in y_data[radius: -radius]:
        y_med = np.append(y_med, np.mean(y_data[n-radius:n+radius]))
        n = n + 1
    
    return y_med


def box_car(data, radius=11):
    new = np.zeros(data.shape)
    for i in np.arange(radius, len(data)-radius+1):
        new[i] = np.median(data[i-radius:i+radius])
    return new



def raw_graph(x_data, y_data, radius = 11, c = 'b', l = 1):
    y_med = box_car(y_data, radius)
    
    plt.plot(x_data, y_data, color=c, linewidth=l)
    #plt.plot(x_data, y_med, color='r', linewidth=1)
    #plt.axis([0,.5,-2e6,2e6])
    #plt.xlabel('Time (s)', fontsize=20)
    plt.ylabel('Power ('+r'$V^{2}$'+')', fontsize=20)
    #plt.ylabel('Temperature (K)', fontsize=20)
    plt.xlabel('Frequency (MHz)', fontsize=20)
    #plt.title('Digital Mixing with'+ r' $\nu_{sig}=1.05 \times\ \nu_{lo}$' ,size=22)



def smooth_graph(x_data, y_data, radius = 11):
    y_med = box_car(y_data, radius)
    #y_med = average(x_data,y_data)
    y_data = y_data - y_med
    x_data = x_data
    
    plt.plot(x_data, y_data, linewidth=1, color='g')
        
    #plt.plot(x_data, y_data, linewidth=2, color='r')
    #plt.axis([0,.5,-2e6,2e6])
    #plt.xlabel('Frequency (MHz)', fontsize=20)
    plt.ylabel('Power', fontsize=20)
    # plt.title('Real and Imaginary SSB' ,size=22)




def reboot():
    # Reboot script.
    os.system("/Users/ppkantorski/Documents/Radio_Astronomy/Lab_4/Code/calibrate_new.py")
    sys.exit()


if __name__ == '__main__':
	main()