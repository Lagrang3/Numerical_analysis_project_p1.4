# Cython shared library to import the poisson solver 
# from C to Python.
#
# Also written by myself during the weekend.
#
# License is Copycenter

cdef extern from "libdist.c":
	void csolve_poisson(const double*,double*,const size_t)

import numpy as np
cimport numpy as np

def dist_oo(a,b):
	'''
	L-infinity distance
	'''
	return abs(a-b).max((0,1))

def dist_1(a,b):
	'''
	L1 distance
	'''
	return abs(a-b).sum((0,1))
	
def dist_2(a,b):
	'''
	L2 (Euclidean) distance
	'''
	t=(a-b).flatten()
	return pow(t.dot(t),0.5)
	
def dist_H(a,b):
	'''
	H1 distance using gradients
	'''
	fa=a*(1.0/abs(a).sum((0,1)))
	fb=b*(1.0/abs(b).sum((0,1)))
	df = fb-fa
	fpart = df.flatten()
	dx=np.diff(df,axis=0).flatten()
	dy=np.diff(df,axis=1).flatten()
	return pow( fpart.dot(fpart) + dx.dot(dx) + dy.dot(dy)  ,0.5)
	
def dist_MA(a,b):
	'''
	Linearized Monge-Ampere distance 
	'''
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
	
def dist_L2_blurry(a,b):
	'''
	L2 of phi field from Poisson eq. 
	'''
	fa=a*(1.0/abs(a).sum((0,1)))
	fb=b*(1.0/abs(b).sum((0,1)))
	phi = np.zeros(b.shape).astype(np.double)
	solve_poisson(fa-fb,phi)
	phi=phi.flatten();
	
	return pow(phi.dot(phi),0.5)

def solve_poisson(
	np.ndarray[np.double_t,ndim=2] rho,
	np.ndarray[np.double_t,ndim=2] phi):
	'''
	solver of the Poisson equation
	'''
	csolve_poisson(<double*> rho.data,<double*> phi.data,28)
