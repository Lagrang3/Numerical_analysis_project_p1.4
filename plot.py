#!/usr/bin/env python

import matplotlib.pyplot as plt

def plot_k(kthis):
	f=open("data/eff.txt","r")

	plt.figure()
	x = dict()
	y= dict()
	
	for l in f:
		name,N,k,err=l.split()
		N = int(N)
		k = int(k)
		err = float(err)
		
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
	plt.xlabel("N")
	plt.ylabel("eff")
	plt.title(f"Efficiency for {kthis}-NN")
	plt.savefig(f"plot_{kthis}.png")
	f.close()

if __name__ == "__main__":
	
	plot_k(1)
	plot_k(3)
	plot_k(5)
