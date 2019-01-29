#!/usr/bin/env python

import ctypes
import time
import numpy as np

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

# Assignment 1.
def dist_oo(a,b):
	return abs(a-b).max((0,1))

# Assignment 1.
def dist_1(a,b):
	return abs(a-b).sum((0,1))
	
# Assignment 1.
def dist_2(a,b):
	t=(a-b).flatten()
	return pow(t.dot(t),0.5)


def grad(v):
	n = len(v)
	vx = np.zeros(v.shape)
	vy = np.zeros(v.shape)
	
	for i in range(n):
		for j in range(n):
			if i< n-1 :
				vx[i][j] = v[i+1][j]-v[i][j]
			else:
				vx[i][j] = -v[i][j] # out of the border is 0
				
			if j< n-1:
				vy[i][j] = v[i][j+1]-v[i][j]
			else:
				vy[i][j] = -v[i][j] # out of the border is 0
	return (vx,vy)			


# OJO
def dist_H_old(a,b):
	fa=a*(1.0/abs(a).sum((0,1)))
	fb=b*(1.0/abs(b).sum((0,1)))
	df = fb-fa
	fpart = df.flatten()
	dx,dy = grad(df)
	dx=dx.flatten()
	dy=dy.flatten()
	return pow( fpart.dot(fpart) + dx.dot(dx) + dy.dot(dy)  ,0.5)

dso=ctypes.CDLL("./libdist_H.so")
dso.dist_H.argtypes=[
	ctypes.POINTER(ctypes.c_double),
	ctypes.POINTER(ctypes.c_double),
	ctypes.c_size_t]
dso.dist_H.restype = ctypes.c_double

c_double_p = ctypes.POINTER(ctypes.c_double)

def dist_H(a,b):
	n=len(a)
	ta=a.flatten().astype(np.float64)
	tta=ta.ctypes.data_as(c_double_p)

	tb=b.flatten().astype(np.float64)
	ttb=tb.ctypes.data_as(c_double_p)
	
	return dso.dist_H(tta,ttb,n)


if __name__ == '__main__':
	
	pass	
