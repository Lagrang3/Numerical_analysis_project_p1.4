import numpy as np

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
