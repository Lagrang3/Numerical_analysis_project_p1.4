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


def classify(k,T):
	'''
	k nearest neighbors classification
	'''
	dist,ind = tree.query(x_test[:T],k=k)
	digits=[[ y_train[i] for i in indj ] for indj in ind ]
	cla = [ max(dig,key=dig.count) for dig in digits ]
	return cla

def error_classification(k,T):
	'''
	returns the fraction of errors
	T: is the number of tests
	'''
	cla=classify(k,T)
	uniq = dict( zip( *np.unique(cla==y_test[:T],return_counts=True) ))
	return uniq[False]/T

if __name__ == "__main__":
	
	dist_name = sys.argv[1]

	#start=time.perf_counter()

	if dist_name == "L2":
		x_train=x_train.reshape((len(x_train),28*28))
		x_test=x_test.reshape((len(x_test),28*28))
		metric=skn.dist_metrics.EuclideanDistance()
		
	
	if dist_name == "L1":
		x_train=x_train.reshape((len(x_train),28*28))
		x_test=x_test.reshape((len(x_test),28*28))
		metric=skn.dist_metrics.ManhattanDistance()
	
	if dist_name == "Loo":
		x_train=x_train.reshape((len(x_train),28*28))
		x_test=x_test.reshape((len(x_test),28*28))
		metric=skn.dist_metrics.ChebyshevDistance()
	
	if dist_name == "H1_test":
		x_train=x_train.reshape((len(x_train),28*28))
		x_test=x_test.reshape((len(x_test),28*28))
		metric=skn.dist_metrics.PyFuncDistance(dist_H_sklearn)
	
	if dist_name == "H1":
		
		def repackage(data):
			for i in range(len(data)):
				data[i]=data[i]*(1.0/data[i].sum())
			
			scalar=data.reshape((len(data),28*28))
			gradx=np.diff(data,axis=1)
			grady=np.diff(data,axis=2)
			gradx=gradx.reshape((len(data),28*27))
			grady=grady.reshape((len(data),28*27))
			return np.concatenate((gradx,grady,scalar),axis=1)
		
		x_train = repackage(x_train)
		x_test = repackage(x_test)
		
		metric=skn.dist_metrics.EuclideanDistance()
	
	if dist_name == "MA_test":
		x_train=x_train.reshape((len(x_train),28*28))
		x_test=x_test.reshape((len(x_test),28*28))
		
		metric=skn.dist_metrics.PyFuncDistance(dist_MA_sklearn)
	
	if dist_name == "MA":
		
		def repackage(data):
			for i in range(len(data)):
				data[i]=data[i]*(1.0/data[i].sum())
				data[i]=solve_poisson(data[i])
			
			scalar=data.reshape((len(data),28*28))
			gradx=np.diff(data,axis=1)
			grady=np.diff(data,axis=2)
			gradx=gradx.reshape((len(data),28*27))
			grady=grady.reshape((len(data),28*27))
			return np.concatenate((gradx,grady,scalar),axis=1)
		
		x_train = repackage(x_train)
		x_test = repackage(x_test)
		
		metric=skn.dist_metrics.EuclideanDistance()

	for p in range(5,10):
		N = 100 * 2**p
	
		tree=skn.BallTree(
			x_train[:N],
			metric=metric)
		
		#end=time.perf_counter()
		#print("precal:","%.2f sec" % (end-start))
		
		for k in [1,3,5]:
			start=time.perf_counter()
			err=error_classification(k,10000)
			end=time.perf_counter()
			print(dist_name,N,k,err)
			#print("%.2f sec" % (end-start))
			#print("k: ",k,
			#	"error:", "%.2f %%" % (err*100),
			#	"time:", "%.2f sec" % (end-start) )
