===============
python-learning
===============
Examples of neat Python plotting and other tasks

* Matplotlib 2.1 `What's New <https://matplotlib.org/devdocs/users/whats_new.html#new-in-matplotlib-2-1>`_

File Description:
=================

============================ ================
function                      description
============================ ================
contourImage2.m                 hack to work around Matlab R2014b/R2015a removal of contour(), contourf() and contour3() handle graphics children that formerly could be used to move contours into a 3-D plot. This workaround first plots the image at z=0, and the contour at z=0, then flattens the figure to an image and resizes to the original data, allowing the new pcolor joint plot to be arbitrarily placed in 3-D.
R2014bAxesMultiColormap.m       showing the new capability of Matlab R2014b/R2015a to have independent colormaps and colorbars -- freezeColor from Matlab Central is NOT necessary as with earlier versions of Matlab.
title_gitrev.py                 label title in corner with git revision
============================ ================


Other neat tricks
=================

* f2py calling `Fortran from Python <https://github.com/scivision/f2pyExamples>`_
