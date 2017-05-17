#!/usr/bin/env python
from setuptools import setup

req = ['numpy','h5py','matplotlib','bokeh']


setup(name='python-matlab-examples',
	    description='Tricks and tips with Matlab and Python',
	    author='Michael Hirsch, Ph.D.',
	    url='https://github.com/scivision/python-matlab-examples',
        packages = ['pyplots'],
	    install_requires=req,
	  )
