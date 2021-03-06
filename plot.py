#!/usr/bin/env python

# Plotting methods.

import matplotlib.pyplot as plt

def plot_image(data,filename):
	'''
	Plots the image 'data' provided as a matrix,
	and saves it into a file 'filename'
	'''
	plt.figure()
	plt.imshow(data,cmap='gray_r')
	plt.savefig(filename)


def plot_k(kthis):
	'''
	plots the contents of the file data/eff.txt
	visualize the errors of classification for 
	the different distance functions.
	'''
	
	f=open("data/eff.txt","r")

	plt.figure()
	plt.yscale('log')
	#plt.xscale('log')
	
	
	x = dict()
	y= dict()
	
	for l in f:
		name,N,k,err=l.split()
		N = int(N)
		k = int(k)
		err = float(err)*100
		
		if k != kthis:
			continue
		
		if not name in x:
			x[name] = list()
		if not name in y:
			y[name] = list()
		
		x[name].append(N)
		y[name].append(err)
		

	
	for name in x:
		plt.plot(x[name],y[name],label=name)
	
	plt.legend()
	plt.xlabel("N (train images)")
	plt.ylabel("% of error")
	plt.title(f"Efficiency for {kthis}-Nearest Neighbors")
	plt.ylim(1,100)
	plt.savefig(f"plot_{kthis}.png")
	f.close()


def plot_dist_matrix(ldist,dm):
	'''
	input: a list of distance functions and their distance matrix
	output: multiple plots of distance matrices for N=100.
	'''
	for i,dist_f in enumerate(ldist):
		plt.figure()
#		dm = dist_matrix(100,dist_f,x_data)
		plt.imshow(dm[i],cmap='gray_r')
		plt.savefig(dist_f.__name__+".png")


def plot_error_dist_matrix(ldist,x,ly):
	'''
	input: 
		- list of distance functions, 
		- list of sizes
		- list of errors (for each function)
	output: a plot 'all_dist_err.png' with comparison of
	the distance matrices for N=100.
	'''
	plt.figure()
	y=[]
	for d,yd in zip(ldist,ly):
		plt.plot(
			x,
			yd,
			label=d.__name__)
		y = y + yd
	plt.legend()
	err_table = np.array( y ).reshape((len(ldist),len(x)))
	print(err_table.T)
	plt.savefig("all_dist_err.png")

if __name__ == "__main__":
	
	
	plot_k(1)
	plot_k(3)
	plot_k(5)
	
	from classify import *
	
	dlist=[dist_oo,dist_1,dist_2,dist_H,dist_MA]
	dmatrix = [ dist_matrix(100,df,x_train) for df in dlist  ]
	
	plot_dist_matrix(dlist,dmatrix)
	
	x,ly=compute_error_dist_matrix(dlist,x_train,y_train)
	
	plot_error_dist_matrix(dlist,x,ly)
