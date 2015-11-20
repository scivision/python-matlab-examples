#!/usr/bin/env python3
"""
demo of need to use INTENT() in the Fortran code with f2py
as current versions of f2py assume INTENT(IN), which is an obvious
issue for getting results back to Python!

NOTE: there is a regression in Numpy 1.10.1 that is stopping INTENT(INOUT)
from working
https://github.com/numpy/numpy/issues/6654
You can setup an enviroment with Numpy 1.9.3 if you want to test this, until
the fixed is released (hopefully Numpy 1.10.2)


f2py3 -m fortprod -c fortprod.py
then type:
python3 f2py_demo.py

Note: You must use the f2py corresponding to your Python, 2 or 3

Note: imports from f2py will always be ALL lowercase!

Michael Hirsch
"""
import numpy
from fortprod import prodintent, prodnointent,prodinout


x=3
y=2
#%%
zint = prodintent(x,y)
print(zint)
#%%
znoint = 12345
znoint = prodnointent(x,y,znoint)
assert znoint is None
#%%
if numpy.__version__ != '1.10.1':
    zinout = 23456
    zinout = prodinout(x,y,zinout)
    print(zinout)
else:
    print('Numpy 1.10.1 has a bug with INOUT')