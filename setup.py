#!/usr/bin/env python
from setuptools import setup
import subprocess

try:
    subprocess.run(['conda','install','--yes','--file','requirements.txt'])
except Exception as e:
    pass


with open('README.rst','r') as f:
    long_description = f.read()


setup(name='python-matlab-examples',
      version='0.1',
	    description='Tricks and tips with Matlab and Python',
	    long_description=long_description,
	    author='Michael Hirsch',
	    url='https://github.com/scienceopen/python-matlab-examples',
      dependency_links = [],
	  install_requires=[],
      packages=[],
	  )
