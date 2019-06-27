#!/usr/bin/env python
"""
Shows a bug with Oct2Py through at least Oct2Py 5.0.4
"""
import oct2py

val = 3.5  # arbitrary

with oct2py.Oct2Py() as oc:
    a = oc.oct2py_class()

    try:
        a.Value = val

        print(a.Value)
        print(a.roundOff)
    except oct2py.Oct2PyError as e:
        print(f'known bug in Oct2Py: cannot handle classes  {e}')
