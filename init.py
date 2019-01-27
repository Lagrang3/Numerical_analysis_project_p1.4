#!/usr/bin/env python

import pylab
import sys
import matplotlib.pyplot as plt
import numpy as np
import itertools
from methods import *

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

import time

start=time.perf_counter()
d_plain=dist_matrix_np(100,dist_2)
end=time.perf_counter()
print(end-start)

start=time.perf_counter()
d=dist_matrix(100,dist_2)
end=time.perf_counter()
print(end-start)

print(dist_oo(d,d_plain))
#plt.imshow(x_train[n],cmap='gray_r')
