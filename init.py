#!/usr/bin/env python

import pylab
import sys
import matplotlib.pyplot as plt
import numpy as np
import itertools
from methods import *
import time

arc=pylab.load('mnist.npz')
x_train=arc['arr_0']
y_train=arc['arr_1']
x_test=arc['arr_2']
y_test=arc['arr_3']

def plot_dist_matrix(ldist):
	'''
	input: a list of distance functions.
	output: multiple plots of distance matrices for N=100.
	'''
	for dist_f in ldist:
		plt.figure()
		dm = dist_matrix(100,dist_f,x_train)
		plt.imshow(dm,cmap='gray_r')
		plt.savefig(dist_f.__name__+".png")

def compute_error_dist_matrix(ldist):
	'''
	input: a list of distance functions.
	output: a list of values of the error of the distance matrix 
	for N = 100,200,400,800,1600.
	'''
	x=[ 100*2**i for i in range(5) ]
	ly = []
	for dist_f in ldist:
		start=time.perf_counter()
		y = [ dist_error(dist_matrix(n,dist_f,x_train),y_train) for n in x ]
		end=time.perf_counter()
		ly.append(y)
		print(dist_f.__name__,y,"( %.2f  seconds)" % (end-start))
	
	return x,ly

def plot_error_dist_matrix(ldist,x,ly):
	'''
	input: 
		- list of distance functions, 
		- list of sizes
		- list of errors (for each function)
	output: a plot 'all_dist_err.png' with comparison of
	the distance matrices for N=100.
	'''
	plt.figure()
	y=[]
	for d,yd in zip(ldist,ly):
		plt.plot(
			x,
			yd,
			label=d.__name__)
		y = y + yd
	plt.legend()
	err_table = np.array( y ).reshape((len(ldist),len(x)))
	print(err_table.T)
	plt.savefig("all_dist_err.png")





if __name__ == '__main__':

	plot_dist_matrix(
		[dist_oo,dist_1,dist_2,dist_H,dist_MA])
	x,ly=compute_error_dist_matrix(
		[dist_oo,dist_1,dist_2,dist_H,dist_MA])
	plot_error_dist_matrix(
		[dist_oo,dist_1,dist_2,dist_H,dist_MA],x,ly)
