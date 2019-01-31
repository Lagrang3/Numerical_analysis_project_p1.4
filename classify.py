#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import sklearn.neighbors as skn
from init import *

N=51200
dist_f=dist_MA

@time_this
def classify_brute_force(i):
	dlist = np.array([ dist_f(x_test[i],x_train[j]) for j in range(N)  ])
	return y_train[dlist.argmin()]

X=x_train[:N].reshape((N,28*28))


#tree=skn.BallTree(X,metric=skn.dist_metrics.ChebyshevDistance()) # L_oo
#tree=skn.BallTree(X,metric=skn.dist_metrics.ManhattanDistance()) # L_1
#tree=skn.BallTree(X,metric=skn.dist_metrics.EuclideanDistance()) # L_2

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

#def dist_MA_sklearn(a,b):
#	ta=a.astype(np.float64)
#	tta=ta.ctypes.data_as(c_double_p)
#
#	tb=b.astype(np.float64)
#	ttb=tb.ctypes.data_as(c_double_p)
#	return dso.dist_MA(tta,ttb,28)
	
tree=skn.BallTree(X,metric=skn.dist_metrics.PyFuncDistance(dist_MA_sklearn), leaf_size=2) # 

	

#tree=skn.BallTree(X,metric=skn.dist_metrics.PyFuncDistance(dist_MA_sklearn)) # 
@time_this
def classify(i):
	dist,ind = tree.query([x_test[i].flatten()])
	ind=ind[0,0]
	return y_train[ind]

if __name__ == "__main__":

	print(classify(115))
	print(classify_brute_force(115))
	
	exit()

	e=0
	for i in range(len(x_test)):
		start=time.perf_counter()
		k = classify(i)
		end=time.perf_counter()
		if k!= y_test[i]:
			plt.imshow(x_test[i],cmap='gray_r')
			plt.savefig("_"+str(i)+'.png')
			e+=1		
			print("class:",k,"\nnumber:",y_test[i],"\nimage_id:",i,
				"\n%d" % e, "out of",i+1,"(%.2f%%)" % (e*100./(i+1)),
				"\ntime:","%.3f sec" % (end-start),"\n")
			start=time.perf_counter()
			classify_brute_force(i)
			end=time.perf_counter()
			print("brute force:","%.3f sec" % (end-start))
	
	exit()
	i=int(sys.argv[1])

	plt.imshow(x_test[i],cmap='gray_r')
	plt.savefig("_"+str(i)+'.png')
	
	start=time.perf_counter()
	n=classify(i)
	end=time.perf_counter()
	print("classification:",n,
		"\nnumber:",y_test[i],
		"\ntime:", "%.3f sec" % (end-start))
	
	
