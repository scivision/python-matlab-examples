#!/usr/bin/env python
from oct2py import Oct2Py

val = 3.5  # arbitrary

with Oct2Py() as oc:
    a = oc.oct2py_class()

    a.Value = val

    print(a.Value)
    print(a.roundOff)
