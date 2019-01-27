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
	
def dist_matrix(N,dist_f):
	D =np.ndarray((N,N))
	for i in range(N):
		for j in range(i,N):
			D[i][j] = dist_f(x_train[i],x_train[j])
			D[j][i] = D[i][j]
	return D


if __name__ == '__main__':

	plt.figure(1)	
	plt.imshow(dist_matrix(100,dist_oo),cmap='gray_r')
	plt.savefig("dist_oo.png")
	
	plt.figure(2)	
	plt.imshow(dist_matrix(100,dist_1),cmap='gray_r')
	plt.savefig("dist_1.png")
	
	plt.figure(3)	
	plt.imshow(dist_matrix(100,dist_2),cmap='gray_r')
	plt.savefig("dist_2.png")
