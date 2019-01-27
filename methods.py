#!/usr/bin/env python

def dist_oo(a,b):
	return abs(a-b).max((0,1))

#def dist_oo_plain(a,b):
#	n=len(a)
#	return max(abs(a-b).reshape(n*n))
	
def dist_1(a,b):
	return abs(a-b).sum((0,1))
	
#def dist_1_plain(a,b):
#	n=len(a)
#	return sum(abs(a-b).reshape(n*n))

def dist_2(a,b):
	t=(a-b).flatten()
	return pow(t.dot(t),0.5)

#def dist_2_plain(a,b):
#	n=len(a)
#	return pow(sum(pow(a-b,2).reshape(n*n)),0.5)
	
import numpy as np
import time

if __name__ == '__main__':
	a = np.random.rand(1000000)
	b = np.random.rand(1000000)
	a=a.reshape(1000,1000)
	b=b.reshape(1000,1000)
	
	start=time.perf_counter()
	v=dist_2(a,b)	
	end=time.perf_counter()
	print(end-start,v)
