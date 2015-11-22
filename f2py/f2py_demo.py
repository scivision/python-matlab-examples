#!/usr/bin/env python3
"""
demo of need to use INTENT() in the Fortran code with f2py
as current versions of f2py assume INTENT(IN), which is an obvious
issue for getting results back to Python!

NOTE: there is a regression in Numpy 1.10.1 that is stopping 
!f2py intent(in,out)
from working
https://github.com/numpy/numpy/issues/6654
You can setup an enviroment with Numpy 1.9.3 if you want to test this, until
the fixed is released (hopefully Numpy 1.10.2)


f2py3 -m fortprod -c fortprod.f
then type:
python3 f2py_demo.py

Note: You must use the f2py corresponding to your Python, 2 or 3

Note: imports from f2py will always be ALL lowercase!

Michael Hirsch
"""
import numpy
from fortprod import prodintent, prodnointent,prodinout,prodpure


x=3
y=2
#%%
zint = prodintent(x,y)
assert zint == x*y
#%%
znoint = 12345
znoint = prodnointent(x,y,znoint)
assert znoint is None
#%%
zpure = prodpure(x,y)
assert zpure == x*y
#%%
zinout = 23456.
zinout = prodinout(x,y,zinout)
assert zinout==x*y, 'AssertionError on !f2py intent(in,out), bug in Numpy 1.10.1 f2py is known, result: {}'.format(zinout)
