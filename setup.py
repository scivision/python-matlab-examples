#!/usr/bin/env python
install_requires = ['numpy', 'h5py', 'matplotlib', 'bokeh']

# %%
from setuptools import setup, find_packages

setup(name='python-matlab-examples',
      packages = find_packages(),
      version = '0.1.0',
      description='Tricks and tips with Matlab and Python',
      author='Michael Hirsch, Ph.D.',
      url='https://github.com/scivision/python-matlab-examples',
      install_requires=install_requires,
      python_requires='>=3.4')
