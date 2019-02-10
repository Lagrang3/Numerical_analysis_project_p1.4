#!/usr/bin/env python

import matplotlib.pyplot as plt

def plot_k(kthis):
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

if __name__ == "__main__":
	
	plot_k(1)
	plot_k(3)
	plot_k(5)
