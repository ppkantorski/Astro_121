#!/usr/bin/env python

# ========================================================================== #
# File: central_limit.py                                                     #
# Programmer: Patrick Kantorski                                              #
# Date: 02/09/14                                                             #
# Class: Astronomy 121 - Radio Astronomy Lab                                 #
# Time: T 6:00-9:00 PM                                                       #
# Instructor: Aaron Parsons                                                  #
# Description: This program was written in Python to demonstrate the         #
#              "Central Limit Theorem." What this theorem purposes is that   #
#              in the large-N limit, samples drawn from a non-Gaussian       #
#              random distribution converge to a Gaussian distribution.      #
#              Additionally, the standard deviation of the mean of N         #
#              Gaussian-random samples should decrease as sqrt(N).           #
# ========================================================================== #

import random as rn
import numpy as np
import matplotlib.pyplot as plt
import sys

def main():
	print("-- Central Limit Theorem Demonstration --\n")
	dim = int(raw_input("Sample Size: "))
	N = int(raw_input("N Random Samples: "))
	b = int(raw_input("# Bars in Histogram: "))

	Plot_Data(Gaussian_Distribution(dim, N, b), N, dim, b)


def Gaussian_Distribution(dim, N, b):
# Produces a Gaussian distribution from a non-Gaussian random distribution.

	sample_array = np.array([])
	mean_array = np.array([])

	for x in range(0,N):

		for x in range(0, dim):
			sample_array = np.r_[sample_array, rn.random()]

		mean_array = np.r_[mean_array, np.mean(sample_array)]
		sample_array = np.array([])

	return mean_array


def Standard_Dev_Test(N, b):
# Performs an Allen variance test on the random distribution.
	std_array = np.array([])

	for x in [1, 2, 3, 6, 10, 20, 30, 60, 100, 200, 300, 600, 1000]:
		m_array = Gaussian_Distribution(x, N, b)
		std_array = np.r_[std_array, np.std(m_array)]

	return std_array


def STD_vs_N(dim, b):
# Plots the standard deviation vs N samples.
	std_array2 = np.array([])
	axis = 10.**((np.arange(100.) + 1.) / (100./3.))
	axis = axis.astype(int)

	for x in axis:
		m_array2 = Gaussian_Distribution(dim, x, b)
		std_array2 = np.r_[std_array2, np.std(m_array2)]

	return std_array2

def Plot_Data(mean_array, N, dim, b):
# Calls and plots data from the previous three functions.
	print("\nGaussian Distribution:")
	print("~ For continuous distribution from [0, 1]...")
	plt.hist(mean_array, bins = b)
	plt.show()

	pause1 = raw_input("\nHit enter to continue... ")

	print("\nStandard Deviation Test:")
	print("~ For sample size from [1, 1000]...")
	plt.loglog([1, 2, 3, 6, 10, 20, 30, 60, 100, 200, 300, 600, 1000], Standard_Dev_Test(N, b), 'o')
	plt.show()

	pause2 = raw_input("\nHit enter to continue... ")

	print("\nStandard Deviation vs N-samples:")
	print("~ For N ranging from [1, 10000]...")
	y = STD_vs_N(dim, b)
	avg = np.average(y[30:-1])
	axis = 10.**((np.arange(100.) + 1.) / (100./3.)) 
	axis = axis.astype(int)
	plt.plot(axis, y, 'o')
	plt.plot(range(1000), np.zeros(1000) +avg)
	plt.xscale("log")
	plt.show()

	print("\nTests are complete!\n")


if __name__ == '__main__':
	main()

sys.exit()
