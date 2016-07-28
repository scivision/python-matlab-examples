#!/usr/bin/env python
from setuptools import setup
import subprocess

try:
    subprocess.call(['conda','install','--file','requirements.txt'])
except Exception as e:
    pass


setup(name='python-matlab-examples',
	    description='Tricks and tips with Matlab and Python',
	    author='Michael Hirsch',
	    url='https://github.com/scienceopen/python-matlab-examples',
        packages = ['pyplots'],
        dependency_links = [],
	    install_requires=[],
	  )
