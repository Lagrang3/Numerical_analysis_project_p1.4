from distutils.core import setup,Extension
from Cython.Build import cythonize

ext=cythonize(
	[	Extension("pydist",
		sources=["pydist.pyx"])])
		
setup(ext_modules=ext)
