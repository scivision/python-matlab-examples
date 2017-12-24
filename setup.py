#!/usr/bin/env python
install_requires = ['numpy', 'h5py', 'matplotlib>=2.1', 'bokeh']
tests_require = ['nose','coveralls']
# %%
from setuptools import setup, find_packages

setup(name='python-matlab-examples',
      packages = find_packages(),
      version = '0.1.0',
      description='Tricks and tips with Matlab and Python',
      long_description=open('README.rst').read(),
      author='Michael Hirsch, Ph.D.',
      url='https://github.com/scivision/python-matlab-examples',
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require={'tests':tests_require},
      python_requires='>=3.4')
