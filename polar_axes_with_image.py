#!/usr/bin/env python
"""
polar axes over image, using transparent axes

another way to do this would be via contours and plot.
Maybe someone has already made such a boilerplate example?
It would involve reading the "size" of the axes and scaling circles to the axes data, or using normalized axes coordinates.
"""
from matplotlib.pyplot import figure,show
#
from pyplots.polarplot import polarplot
from pyplots.data import testdata_2d

def polar_axes_image(X,Y,Z,V):
    fg = figure()
#%% create the image
    ax = fg.gca()
    h = ax.imshow(V,vmin=0,vmax=0.2,extent=(-3,3,-2,2),cmap='bone')
    #fg.colorbar(h).set_label('image values')
#%% create transparent polar axes as a fiducial marking
    ax2 = polarplot(None,None,fig=fg)
    ax2.patch.set_alpha(.5)


if __name__ == '__main__':
    X,Y,Z,V = testdata_2d()

    polar_axes_image(X,Y,Z,V)

    show()