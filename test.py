#!/usr/bin/env python

import sys
import numpy as np
import unittest
from init import *

class TestC(unittest.TestCase):
	
	def test_H(self):
		dist=dist_H
		
		a=np.array([1,1,1,1]).reshape(2,2)
		b=np.array([1,2,3,4]).reshape(2,2)
		x=pow(2*0.15**2 + 2*0.05**2 + 2*0.1**2 + 2*0.2**2,.5)
		y=dist(a,b)
		self.assertAlmostEqual(x,y,places=12)
		self.assertEqual(
			[dist(a,a),dist(b,b),dist(b,a),dist(a,b),dist(2*a,2*b)],
			[0.,0.,y,y,y])


	def test_err_dist_matrix(self):
		x=[ 100*2**i for i in range(2) ]
		y = [ [ dist_error(dist_matrix(n,dist,x_train),y_train) 
					for dist in [dist_oo,dist_1,dist_2,dist_H] ]
					for n in x  ]
		self.assertEqual(y,
			[[ 0.58,      0.17,      0.17 ,0.24   ],
			 [ 0.52,      0.145,     0.135 ,0.19   ]])

	def test_d2(self):
		dist=dist_2
		
		a=np.array([0.]).reshape(1,1)
		b=np.array([0.]).reshape(1,1)
		self.assertEqual(
			[dist(a,a),dist(b,b),dist(b,a),dist(a,b),dist(2*a,2*b)],
			[0.,0.,0.,0.,0.])
		
		a=np.array([12.]).reshape(1,1)
		b=np.array([-8.]).reshape(1,1)
		self.assertEqual(
			[dist(a,a),dist(b,b),dist(b,a),dist(a,b),dist(2*a,2*b)],
			[0.,0.,20.,20.,40.])
		
		a=np.array([12.]).reshape(1,1)
		b=np.array([8.]).reshape(1,1)
		self.assertEqual(
			[dist(a,a),dist(b,b),dist(b,a),dist(a,b),dist(2*a,2*b)],
			[0.,0.,4.,4.,8.])
		
		a=np.array([0,0,0,0]).reshape(2,2)
		b=np.array([1,2,3,4]).reshape(2,2)
		self.assertEqual(
			[dist(a,a),dist(b,b),dist(b,a),dist(a,b),dist(2*a,2*b)],
			[0.,0.,pow(30.,0.5),pow(30.,0.5),2*pow(30.,0.5)])
		
		a=np.array([1.5,2,3,4]).reshape(2,2)
		b=np.array([1,2,3,4]).reshape(2,2)
		self.assertEqual(
			[dist(a,a),dist(b,b),dist(b,a),dist(a,b),dist(2*a,2*b)],
			[0.,0.,0.5,0.5,1.])
		
		a=np.array([1,2.5,3,4]).reshape(2,2)
		b=np.array([1,2,3,4]).reshape(2,2)
		self.assertEqual(
			[dist(a,a),dist(b,b),dist(b,a),dist(a,b),dist(2*a,2*b)],
			[0.,0.,0.5,0.5,1.])
		
		a=np.array([1,2,3.5,4]).reshape(2,2)
		b=np.array([1,2,3,4]).reshape(2,2)
		self.assertEqual(
			[dist(a,a),dist(b,b),dist(b,a),dist(a,b),dist(2*a,2*b)],
			[0.,0.,0.5,0.5,1.])
		
		a=np.array([1,2,3,4.5]).reshape(2,2)
		b=np.array([1,2,3,4]).reshape(2,2)
		self.assertEqual(
			[dist(a,a),dist(b,b),dist(b,a),dist(a,b),dist(2*a,2*b)],
			[0.,0.,0.5,0.5,1.])
		
	def test_d1(self):
		dist=dist_1
		
		a=np.array([0.]).reshape(1,1)
		b=np.array([0.]).reshape(1,1)
		self.assertEqual(
			[dist(a,a),dist(b,b),dist(b,a),dist(a,b),dist(2*a,2*b)],
			[0.,0.,0.,0.,0.])
		
		a=np.array([12.]).reshape(1,1)
		b=np.array([-8.]).reshape(1,1)
		self.assertEqual(
			[dist(a,a),dist(b,b),dist(b,a),dist(a,b),dist(2*a,2*b)],
			[0.,0.,20.,20.,40.])
		
		a=np.array([12.]).reshape(1,1)
		b=np.array([8.]).reshape(1,1)
		self.assertEqual(
			[dist(a,a),dist(b,b),dist(b,a),dist(a,b),dist(2*a,2*b)],
			[0.,0.,4.,4.,8.])
		
		a=np.array([0,0,0,0]).reshape(2,2)
		b=np.array([1,2,3,4]).reshape(2,2)
		self.assertEqual(
			[dist(a,a),dist(b,b),dist(b,a),dist(a,b),dist(2*a,2*b)],
			[0.,0.,10.,10.,20.])
		
		a=np.array([1.5,2,3,4]).reshape(2,2)
		b=np.array([1,2,3,4]).reshape(2,2)
		self.assertEqual(
			[dist(a,a),dist(b,b),dist(b,a),dist(a,b),dist(2*a,2*b)],
			[0.,0.,.5,.5,1.])
		
		a=np.array([1,2.5,3,4]).reshape(2,2)
		b=np.array([1,2,3,4]).reshape(2,2)
		self.assertEqual(
			[dist(a,a),dist(b,b),dist(b,a),dist(a,b),dist(2*a,2*b)],
			[0.,0.,.5,.5,1.])
		
		a=np.array([1,2,3.5,4]).reshape(2,2)
		b=np.array([1,2,3,4]).reshape(2,2)
		self.assertEqual(
			[dist(a,a),dist(b,b),dist(b,a),dist(a,b),dist(2*a,2*b)],
			[0.,0.,.5,.5,1.])
		
		a=np.array([1,2,3,4.5]).reshape(2,2)
		b=np.array([1,2,3,4]).reshape(2,2)
		self.assertEqual(
			[dist(a,a),dist(b,b),dist(b,a),dist(a,b),dist(2*a,2*b)],
			[0.,0.,.5,.5,1.])
		
	def test_doo(self):
		dist=dist_oo
		
		a=np.array([0.]).reshape(1,1)
		b=np.array([0.]).reshape(1,1)
		self.assertEqual(
			[dist(a,a),dist(b,b),dist(b,a),dist(a,b),dist(2*a,2*b)],
			[0.,0.,0.,0.,0.])
		
		a=np.array([12.]).reshape(1,1)
		b=np.array([-8.]).reshape(1,1)
		self.assertEqual(
			[dist(a,a),dist(b,b),dist(b,a),dist(a,b),dist(2*a,2*b)],
			[0.,0.,20.,20.,40.])
		
		a=np.array([12.]).reshape(1,1)
		b=np.array([8.]).reshape(1,1)
		self.assertEqual(
			[dist(a,a),dist(b,b),dist(b,a),dist(a,b),dist(2*a,2*b)],
			[0.,0.,4.,4.,8.])
		
		a=np.array([0,0,0,0]).reshape(2,2)
		b=np.array([1,2,3,4]).reshape(2,2)
		self.assertEqual(
			[dist(a,a),dist(b,b),dist(b,a),dist(a,b),dist(2*a,2*b)],
			[0.,0.,4.,4.,8.])
		
		a=np.array([1.5,2,3,4]).reshape(2,2)
		b=np.array([1,2,3,4]).reshape(2,2)
		self.assertEqual(
			[dist(a,a),dist(b,b),dist(b,a),dist(a,b),dist(2*a,2*b)],
			[0.,0.,.5,.5,1.])
		
		a=np.array([1,2.5,3,4]).reshape(2,2)
		b=np.array([1,2,3,4]).reshape(2,2)
		self.assertEqual(
			[dist(a,a),dist(b,b),dist(b,a),dist(a,b),dist(2*a,2*b)],
			[0.,0.,.5,.5,1.])
		
		a=np.array([1,2,3.5,4]).reshape(2,2)
		b=np.array([1,2,3,4]).reshape(2,2)
		self.assertEqual(
			[dist(a,a),dist(b,b),dist(b,a),dist(a,b),dist(2*a,2*b)],
			[0.,0.,.5,.5,1.])
		
		a=np.array([1,2,3,4.5]).reshape(2,2)
		b=np.array([1,2,3,4]).reshape(2,2)
		self.assertEqual(
			[dist(a,a),dist(b,b),dist(b,a),dist(a,b),dist(2*a,2*b)],
			[0.,0.,.5,.5,1.])


def benchmark_dist(dist,N):
	a=np.random.rand(N*N).reshape(N,N)
	b=np.random.rand(N*N).reshape(N,N)
	start=time.perf_counter()
	r=dist(a,b)
	end=time.perf_counter()
	print('%s for images of size %s: %.5f seconds' % (dist.__name__,str((N,N)),end-start) )

def benchmark_dist_matrix(N,dist,data):
	start=time.perf_counter()
	r=dist_matrix(N,dist,data)
	end=time.perf_counter()
	print('dist_matrix for %i images of size %s using %s: %.5f seconds' % (N,str(data[0].shape),dist.__name__,end-start) )
	
if __name__ == "__main__":
	
	unittest.main(exit=False)
	
	benchmark_dist(dist_oo,1000)
	benchmark_dist(dist_1, 1000)
	benchmark_dist(dist_2, 1000)
	benchmark_dist(dist_H, 1000)
	benchmark_dist(dist_MA,1000)
	
	benchmark_dist_matrix(100,dist_oo,x_train)
	benchmark_dist_matrix(100,dist_1,x_train)
	benchmark_dist_matrix(100,dist_2,x_train)
	benchmark_dist_matrix(100,dist_H,x_train)
	benchmark_dist_matrix(100,dist_MA,x_train)

