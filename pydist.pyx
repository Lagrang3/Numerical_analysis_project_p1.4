cdef extern from "libdist.c":
	double cdist_MA(const double*,const double*,const size_t)

cdef extern from "libdist.c":
	void csolve_poisson(const double*,double*,const size_t)

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
def dist_MA(a,b):
	fa=a*(1.0/abs(a).sum((0,1)))
	fb=b*(1.0/abs(b).sum((0,1)))
	sf = (fa+fb).flatten()
	phi = np.zeros(b.shape).astype(np.double)
	solve_poisson(fa-fb,phi)
	g = np.gradient(phi)
	dx=g[0].flatten()
	dy=g[1].flatten()
	
	dx=np.square(dx)
	dy=np.square(dy)
	return dx.sum() + dy.sum() # it works better this way
	#return sf.dot(dx) + sf.dot(dy)
	
def dist_MA_sklearn(a,b):
	fa=a*(1.0/abs(a).sum())
	fb=b*(1.0/abs(b).sum())
	sf = (fa+fb).flatten()
	df=(fa-fb).reshape((28,28))
	phi = np.zeros(df.shape).astype(np.double)
	solve_poisson(df,phi)
	g = np.gradient(phi)
	dx=g[0].flatten()
	dy=g[1].flatten()
	
	dx=np.square(dx)
	dy=np.square(dy)
	return dx.sum() + dy.sum() # it works better this way
	#return sf.dot(dx) + sf.dot(dy)
	
	return cdist_MA(<double*> a.data, <double*> b.data, len(a))

def solve_poisson(
	np.ndarray[np.double_t,ndim=2] rho,
	np.ndarray[np.double_t,ndim=2] phi):
	'''
	solver of the Poisson equation
	'''
	csolve_poisson(<double*> rho.data,<double*> phi.data,28)
