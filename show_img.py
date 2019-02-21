#!/usr/bin/env python

# This script is used to visualize the images 
# from the mnist database.
# Usage: ./show_img.py 100 & eog 100.png
# to visualize the image indexed 100.

import pylab
import sys
import matplotlib.pyplot as plt

arc=pylab.load('data/mnist.npz')
x_train=arc['arr_0']
y_train=arc['arr_1']
x_test=arc['arr_2']
y_test=arc['arr_3']

if len(sys.argv) < 2:
	n = 0
else:
	n = int(sys.argv[1])
	
plt.imshow(x_train[n],cmap='gray_r')
plt.savefig(str(n)+'.png')
