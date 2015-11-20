to run example showing bug with f2py in Numpy 1.9 and 1.10 and possibly 
others, first compile::

    f2py -m fortprod -c fortprod.f

then::

    python f2py_demo.py

If you add to fortprod.f in subroutine ProdInOut the line::

    !f2py intent(in,out) :: z

it will work. `This is a bug <https://github.com/numpy/numpy/issues/6654>`_.

It will **not** work with::
    
    !f2py intent(inout) :: z
