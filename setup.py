#!/usr/bin/env python
req = ['numpy','h5py','matplotlib','bokeh']

import pip
try:
    import conda.cli
    conda.cli.main('install',*req)
except Exception:
    pip.main(['install'] + req)
# %%
from setuptools import setup

setup(name='python-matlab-examples',
        packages = ['pyplots'],
	    description='Tricks and tips with Matlab and Python',
	    author='Michael Hirsch, Ph.D.',
	    url='https://github.com/scivision/python-matlab-examples',
	  )
