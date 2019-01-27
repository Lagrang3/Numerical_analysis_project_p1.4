#!/usr/bin/env python

import pylab
import sys
import matplotlib.pyplot as plt
from methods import *

arc=pylab.load('mnist.npz')
x_train=arc['arr_0']
y_train=arc['arr_1']
x_test=arc['arr_2']
y_test=arc['arr_3']

	
#plt.imshow(x_train[n],cmap='gray_r')
