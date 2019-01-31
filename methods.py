#!/usr/bin/env python

import ctypes
import time
import numpy as np
from pydist import *

def args_to_str(*args,**kw):
	l = []
	if args:
		l.append( ", ".join( str(i) for i in args)  )
	if kw:
		l.append( ", ".join( "{0}={1}".format(k,v)  for k,v in kw.items()))
	return ", ".join(l)

def time_this(f):
	def tf(*args,**kw):
		start=time.perf_counter()
		r=f(*args,**kw)
		end=time.perf_counter()
		print('%s(%s): %.5fs' % (f.__name__,args_to_str(*args,**kw),end-start))
		return r
	return tf


dso=ctypes.CDLL("./libdist.so")

dso.dist_MA.argtypes=[
	ctypes.POINTER(ctypes.c_double),
	ctypes.POINTER(ctypes.c_double),
	ctypes.c_size_t]
	
dso.dist_MA.restype = ctypes.c_double

c_double_p = ctypes.POINTER(ctypes.c_double)


def dist_MA(a,b):
	n=len(a)
	ta=a.flatten().astype(np.float64)
	tta=ta.ctypes.data_as(c_double_p)

	tb=b.flatten().astype(np.float64)
	ttb=tb.ctypes.data_as(c_double_p)
	
	return dso.dist_MA(tta,ttb,n)

# Assignment 2	
def dist_matrix(N,dist_f,x_data):
	'''
	This function computes the distance matrix 
	of the first N images in the training list using
	the provided distance function dist_f.
	'''
	D =np.ndarray((N,N))
	for i in range(N):
		for j in range(i,N):
			D[i][j] = dist_f(x_data[i],x_data[j])
			D[j][i] = D[i][j]
	return D



def dist_error(D,y_data):
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
		if y_data[i] != y_data[j]:
			err += 1.
	
	for i in range(N):
		D[i,i]=0.
		
	return err/N


if __name__ == '__main__':
	
	pass	
