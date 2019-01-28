#!/usr/bin/env python

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

#def dist_oo_plain(a,b):
#	n=len(a)
#	return max(abs(a-b).reshape(n*n))
	
# Assignment 1.
def dist_1(a,b):
	return abs(a-b).sum((0,1))
	
#def dist_1_plain(a,b):
#	n=len(a)
#	return sum(abs(a-b).reshape(n*n))

# Assignment 1.
def dist_2(a,b):
	t=(a-b).flatten()
	return pow(t.dot(t),0.5)

#def dist_2_plain(a,b):
#	n=len(a)
#	return pow(sum(pow(a-b,2).reshape(n*n)),0.5)
	
def benchmark_dist(dist):
	N=1000
	a=np.random.rand(N*N).reshape(N,N)
	b=np.random.rand(N*N).reshape(N,N)
	start=time.perf_counter()
	r=dist(a,b)
	end=time.perf_counter()
	print('%s at %i: \t%.5f seconds' % (dist.__name__,N,end-start) )

if __name__ == '__main__':

	benchmark_dist(dist_oo)
	benchmark_dist(dist_1)
	benchmark_dist(dist_2)
