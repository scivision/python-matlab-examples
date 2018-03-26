#!/usr/bin/env python
install_requires = ['numpy', 'h5py', 'matplotlib>=2.2', 'bokeh','mpld3','astropy','scipy',
            'oct2py']
tests_require = ['pytest','nose','coveralls']
# %%
from setuptools import setup, find_packages

setup(name='python-matlab-examples',
      packages = find_packages(),
      version = '0.5.0',
      description='Tricks and tips with Matlab and Python',
      long_description=open('README.rst').read(),
      author='Michael Hirsch, Ph.D.',
      url='https://github.com/scivision/python-matlab-examples',
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require={'tests':tests_require},
      python_requires='>=3.4',
      classifiers=['
        'Environment :: Console',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Graphics :: Presentation',
        'Topic :: Multimedia :: Video :: Display',
        'Topic :: Scientific/Engineering :: Visualization',
     ],
     include_package_data=True,
     )
