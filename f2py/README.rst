=============
demo f2py
=============

Here's a simple example of using f2py to run Fortran code from Python

Minimal working example
=======================

first compile::

    f2py -m fortprod -c fortprod.f

then::

    python f2py_demo.py

Note on Intent(inout)
=====================
If the subroutine you want to interface Python with has the Fortran statement for a particular variable::

    Intent(inout) :: myvariable
    
you must add::

    !f2py intent(in,out) :: myvariable

It will **not** work with::
    
    !f2py intent(inout) :: myvariable
