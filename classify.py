#!/usr/bin/env python

import sys
import pylab
import matplotlib.pyplot as plt
import sklearn.neighbors as skn

from methods import *
from plot import *
from pydist import *

### initialize the training database ###
arc=pylab.load('data/mnist.npz')
x_train=arc['arr_0'].astype(np.double)
y_train=arc['arr_1']
x_test=arc['arr_2'].astype(np.double)
y_test=arc['arr_3']


def error_classification(cla,rev):
	'''
	returns the fraction of errors
	cla: list the classification results
	rev: real values
	'''
	uniq = dict( zip( *np.unique(cla==rev,return_counts=True) ))
	return uniq[False]/len(cla)

class Oracle():
	'''
	This class not only serves as a container for
	the classification, but also it is used to 
	adapt the data of the problem to the programming 
	interface of sklearn.
	eg. my distance functions defined on 'pydist.pyx'
	take as argument two 28x28 images, while sklearn
	works on unidimensional arrays, so a distance
	on sklearn will have as input two arrays of size 784. 
	'''
	
	def __init__(self,dist_name,x_data,y_data): # {
		'''
		dist_name: denomination of the distance
		function used, which must be one of the
		following [L2,L1,Loo,H1,MA]
		x_data: training input sample
		y_data: training ouput sample
		'''
		
		self._dist_name=dist_name
		self._y_train=np.copy(y_data)
		
		if dist_name == "L2":
			self._metric=skn.dist_metrics.EuclideanDistance()
			def repackage(data):
				mydata=np.copy(data)	
				return mydata.reshape((len(data),28*28))
			
			
		if dist_name == "L1":
			self._metric=skn.dist_metrics.ManhattanDistance()
			def repackage(data):
				mydata=np.copy(data)	
				return mydata.reshape((len(data),28*28))
		
		
		if dist_name == "Loo":
			self._metric=skn.dist_metrics.ChebyshevDistance()
			def repackage(data):
				mydata=np.copy(data)	
				return mydata.reshape((len(data),28*28))
			
			
		if dist_name == "H1":
			self._metric=skn.dist_metrics.EuclideanDistance()
			
			def repackage(data):
				'''
				Use gradient of data.
				'''
				grad_data=[]
				for m in data:
					fm=m*(1.0/m.sum())
					grad_fm=np.gradient(fm)	
					grad_data = grad_data + [fm] + grad_fm
				
				grad_data = np.array(grad_data).reshape((len(data),-1))
				return grad_data
				

		if dist_name == "MA":
			self._metric=skn.dist_metrics.EuclideanDistance()
			
			def repackage(data):
				'''
				Use gradient of phi data.
				'''
				grad_phi = []
				for m in data:
					fm=m*(1.0/abs(m).sum((0,1)))
					phi = np.zeros(fm.shape)
					solve_poisson(fm,phi)
					
					grad_phi = grad_phi + np.gradient(phi)
				
				grad_phi = np.array(grad_phi).reshape((len(data),-1))
				
				return grad_phi
			

		self._repackage = repackage
		self._x_train=repackage(x_data)
		self._tree=skn.BallTree(
			self._x_train,metric=self._metric)
	
	# } end __init__

	def classify(self,k,x_data): # {
		'''
		k nearest neighbors classification
		x_data: images to be classified
		'''
		new_data=self._repackage(x_data)
		dist,ind = self._tree.query(new_data,k=k)
		
		digits=[[ self._y_train[i] for i in indj ] for indj in ind ]
		cla = [ max(dig,key=dig.count) for dig in digits ]
		return cla
		
	# } end classify
	

if __name__ == "__main__":


	dist_name = sys.argv[1]



	for p in range(5,10):
		N = 100 * 2**p
	
		oo=Oracle(dist_name,x_train[:N],y_train[:N])
		
		for k in [1,3,5]:
			M = 10000
			
			start=time.perf_counter()
			cla = oo.classify(k,x_test[:M])
			err=error_classification(cla,y_test[:M])
			end=time.perf_counter()
			
			print(dist_name,N,k,err)
			print(
				"\nk: ",k,
				"\nerror:","%.2f %%" % (err*100),
				"\ntime:", "%.2f sec" % (end-start) )
