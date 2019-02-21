# Script to compile (Cythonize) the shared libraries
# written in Cython.
# 
# I took this from the book 'Cython - A guide for python programmers' by
# Kurt W. Smith.

from distutils.core import setup,Extension
from Cython.Build import cythonize

ext=cythonize(
	[	Extension("pydist",
		sources=["pydist.pyx"])])
		
setup(ext_modules=ext)
