[![image](https://travis-ci.org/scivision/python-matlab-examples.svg?branch=master)](https://travis-ci.org/scivision/python-matlab-examples)
[![image](https://coveralls.io/repos/github/scivision/python-matlab-examples/badge.svg?branch=master)](https://coveralls.io/github/scivision/python-matlab-examples?branch=master)

# Python and Matlab plotting examples

Examples of neat Python and Matlab / GNU Octave plotting and other tasks

## File Description:

-   contourImage2.m: hack to work around Matlab R2014b/R2015a removal of
    contour(), contourf() and contour3() handle graphics children that
    formerly could be used to move contours into a 3-D plot. This
    workaround first plots the image at z=0, and the contour at z=0,
    then flattens the figure to an image and resizes to the original
    data, allowing the new pcolor joint plot to be arbitrarily placed in
    3-D.
-   R2014bAxesMultiColormap.m: showing the new capability of Matlab
    R2014b/R2015a to have independent colormaps and colorbars --
    freezeColor from Matlab Central is NOT necessary as with earlier
    versions of Matlab.
-   title_gitrev.py: label title in corner with git revision
-   widgets_gui_matplotlib.py: How to make interactiave,
    backend-agnostics Matplotlib GUIs
-   colormap_white_min.*: Matlab and Python examples of plots with
    white zero value and dark maximum value.

### Oct2Py

[Oct2Py](https://www.scivision.co/run-matlab-code-from-python-oct2py)
allows running Matlab code from Python, transparently.
[test_oct2py.py](test_oct2py.py) demos this for FIR filter design and Savitsky Golay filtering.
Of course, non-built-in functions can be used as well.

## Other neat tricks

* f2py calling [Fortran from Python](https://github.com/scivision/f2py-examples)
