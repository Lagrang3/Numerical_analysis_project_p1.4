#!/usr/bin/env python

import time
import numpy as np

def args_to_str(*args,**kw):
	'''
	Auxiliary function to be used by a decorator.
	It returns a string with the input arguments separated by commas.
	'''
	l = []
	if args:
		l.append( ", ".join( str(i) for i in args)  )
	if kw:
		l.append( ", ".join( "{0}={1}".format(k,v)  for k,v in kw.items()))
	return ", ".join(l)

def time_this(f):
	'''
	Decorator to measure time of execution.
	'''
	def tf(*args,**kw):
		start=time.perf_counter()
		r=f(*args,**kw)
		end=time.perf_counter()
		print('%s(%s): %.5fs' % (f.__name__,args_to_str(*args,**kw),end-start))
		return r
	return tf


def dist_matrix(N,dist_f,x_data):
	'''
	This function computes the distance matrix 
	of the first N images in the training list x_data using
	the provided distance function dist_f.
	'''
	D =np.ndarray((N,N))
	for i in range(N):
		for j in range(i,N):
			D[i][j] = dist_f(x_data[i],x_data[j])
			D[j][i] = D[i][j]
	return D


def dist_error(D_matrix,y_data):
	'''
	This functions computes the error of using distance
	function which produces the distance matrix D_matrix.
	'''
	oo=1e+100
	
	N = len(D_matrix)
	for i in range(N):
		D_matrix[i,i]=oo
		
	err=0.
	for i,row in enumerate(D_matrix):
		j=row.argmin()
		if y_data[i] != y_data[j]:
			err += 1.
	
	for i in range(N):
		D_matrix[i,i]=0.
		
	return err/N


def compute_error_dist_matrix(ldist,x_data,y_data):
	'''
	INPUT
		ldist: a list of distance functions
		x_data: input database
		y_data: input database
	OUTPUT
		a list of values of the error of the distance matrix 
	for N = 100,200,400,800,1600.
	'''
	x=[ 100*2**i for i in range(5) ]
	ly = []
	for dist_f in ldist:
		start=time.perf_counter()
		y = [ dist_error(dist_matrix(n,dist_f,x_data),y_data) for n in x ]
		end=time.perf_counter()
		ly.append(y)
		print(dist_f.__name__,y,"( %.2f  seconds)" % (end-start))
	
	return x,ly


if __name__ == '__main__':
	
	pass	
