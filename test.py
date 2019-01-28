#!/usr/bin/env python

import numpy as np
import unittest
from methods import *

class TestC(unittest.TestCase):
	
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
		

if __name__ == "__main__":
	
	unittest.main()
