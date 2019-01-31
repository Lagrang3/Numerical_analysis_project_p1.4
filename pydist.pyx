cdef extern from "libdist.c":
	double cdist_MA(const double*,const double*,const size_t)

import numpy as np
cimport numpy as np

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
	
# Assignment 6.
def dist_H(a,b):
	fa=a*(1.0/abs(a).sum((0,1)))
	fb=b*(1.0/abs(b).sum((0,1)))
	df = fb-fa
	fpart = df.flatten()
	dx=np.diff(df,axis=0).flatten()
	dy=np.diff(df,axis=1).flatten()
	return pow( fpart.dot(fpart) + dx.dot(dx) + dy.dot(dy)  ,0.5)
	
# Assignment 7.
def dist_MA(
	np.ndarray[np.double_t,ndim=2] a,
	np.ndarray[np.double_t,ndim=2] b):
	
	return cdist_MA(<double*> a.data, <double*> b.data, len(a))

def dist_MA_sklearn(
	np.ndarray[np.double_t,ndim=1] a,
	np.ndarray[np.double_t,ndim=1] b):
	
	return cdist_MA(<double*> a.data, <double*> b.data, 28)
