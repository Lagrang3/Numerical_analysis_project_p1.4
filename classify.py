#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import sklearn.neighbors as skn
from init import *

@time_this
def classify_brute_force(i):
	dlist = np.array([ dist_f(x_test[i],x_train[j]) for j in range(N)  ])
	return y_train[dlist.argmin()]




def dist_2_sklearn(a,b):
	t=a-b
	return pow(t.dot(t),0.5)

def dist_H_sklearn(a,b):
	fa=a*(1.0/abs(a).sum())
	fb=b*(1.0/abs(b).sum())
	fpart = fb-fa
	df=fpart.reshape((28,28))
	dx = np.diff(df,axis=1)
	dy = np.diff(df,axis=0)
	dx=dx.flatten()
	dy=dy.flatten()
	return pow( fpart.dot(fpart) + dx.dot(dx) + dy.dot(dy)  ,0.5)

x_train=x_train.reshape((len(x_train),28*28))
x_test=x_test.reshape((len(x_test),28*28))

def classify(treen,k,T):
	'''
	k nearest neighbors classification
	'''
	dist,ind = tree.query(x_test[:T],k=k)
	digits=[[ y_train[i] for i in indj ] for indj in ind ]
	classific = [ max(dig,key=dig.count) for dig in digits ]
	return classific

def error_classification(tree,k,T):
	'''
	returns the fraction of errors
	T: is the number of tests
	'''
	cla=classify(tree,k,T)
	uniq = dict( zip( *np.unique(cla==y_test[:T],return_counts=True) ))
	return uniq[False]/T

if __name__ == "__main__":

	for p in range(5,10):
		N = 100 * 2**p
		
		X=x_train[:N]
		
		#tree=skn.BallTree(X,metric=skn.dist_metrics.ChebyshevDistance()) # L_oo
		tree=skn.BallTree(X,metric=skn.dist_metrics.ManhattanDistance()) # L_1
		#tree=skn.BallTree(X,metric=skn.dist_metrics.EuclideanDistance()) # L_2
		#tree=skn.BallTree(X,metric=skn.dist_metrics.PyFuncDistance(dist_MA_sklearn)) #

		for k in [1,3,5]:
			start=time.perf_counter()
			err=error_classification(tree,k,10000)
			end=time.perf_counter()
			print("L1",N,k,err)
			#print("k: ",k,
			#	"error:", "%.2f %%" % (err*100),
			#	"time:", "%.2f sec" % (end-start) )
