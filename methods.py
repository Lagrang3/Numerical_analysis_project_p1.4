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

# Assignment 1.
def dist_1(a,b):
	return abs(a-b).sum((0,1))
	
# Assignment 1.
def dist_2(a,b):
	t=(a-b).flatten()
	return pow(t.dot(t),0.5)


	
# OJO
def grad(v):
	n = len(v)
	vx = np.zeros(v.shape)
	vy = np.zeros(v.shape)
	for i in range(n):
		for j in range(n):
			if i< n-1 :
				vx[i][j] = v[i+1][j]-v[i][j]
			if j< n-1:
				vy[i][j] = v[i][j+1]-v[i][j]
	return (vx,vy)			


# OJO
def dist_H(a,b):
	fa=a*(1.0/a.sum((0,1)))
	fb=b*(1.0/b.sum((0,1)))
	
	df = fb-fa
	
	fpart = df.flatten()
	fpart = fpart.dot(fpart)
	
	df = grad(df)
	gpart= sum( [ t.dot(t) for t in df  ]  )
	
	return pow( fpart + gpart  ,0.5)



if __name__ == '__main__':
	pass
