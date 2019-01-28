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

#def dist_matrix_np(N,dist_f):
#	D =np.array([
#		dist_f(x_train[i],x_train[j]) for i in range(N) for j in range(N) ])
#	return D.reshape(N,N)
	
	
# Assignment 2	
def dist_matrix(N,dist_f):
	'''
	This function computes the distance matrix 
	of the first N images in the training list using
	the provided distance function dist_f.
	'''
	D =np.ndarray((N,N))
	for i in range(N):
		for j in range(i,N):
			D[i][j] = dist_f(x_train[i],x_train[j])
			D[j][i] = D[i][j]
	return D

def dist_error(D):
	'''
	This functions computes the error of using distance
	function which produces the distance matrix D.
	'''
	oo=1e+100
	
	N = len(D)
	for i in range(N):
		D[i,i]=oo
		
	err=0.
	for i,row in enumerate(D):
		j=row.argmin()
		if y_train[i] != y_train[j]:
			err += 1.
	
	for i in range(N):
		D[i,i]=0.
		
	return err/N

# Assignment 3
def plot_dist_matrices():
	plt.figure()	
	plt.imshow(dist_matrix(100,dist_oo),cmap='gray_r')
	plt.savefig("dist_oo.png")
	
	plt.figure()	
	plt.imshow(dist_matrix(100,dist_1),cmap='gray_r')
	plt.savefig("dist_1.png")
	
	plt.figure()	
	plt.imshow(dist_matrix(100,dist_2),cmap='gray_r')
	plt.savefig("dist_2.png")

# Assignment 4.
def compute_error_dist_matrix():
	print(
		dist_error(dist_matrix(100,dist_oo)),
		dist_error(dist_matrix(100,dist_1)),
		dist_error(dist_matrix(100,dist_2)))

# Assignment 5.
def plot_error_dist_matrix():
	plt.figure()
	x=[ 100*2**i for i in range(5) ]
	y_oo = [ dist_error(dist_matrix(n,dist_oo)) for n in x ]
	y_1 = [ dist_error(dist_matrix(n,dist_1)) for n in x ]
	y_2 = [ dist_error(dist_matrix(n,dist_2)) for n in x ]
	plt.plot(x,y_oo,label="dist_oo")
	plt.plot(x,y_1,label="dist_1")
	plt.plot(x,y_2,label="dist_2")
	plt.legend()
	err_table = np.array( y_oo + y_1 + y_2 ).reshape((3,len(x)))
	print(err_table.T)
	plt.savefig("all_dist_err.png")

# Assignment 6.
def compute_error_dist_matrix_for_distH():
	x=[ 100*2**i for i in range(3) ]
	y = [ dist_error(dist_matrix(n,dist_H)) for n in x ]
	print(y)


if __name__ == '__main__':
	
	plot_error_dist_matrix()
