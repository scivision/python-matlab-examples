#!/usr/bin/env python
"""
Plots an image, then plots a contour over top of the image
"""
from matplotlib.pyplot import figure,show
#
from pyplots.data import testdata_2d


def plotimagecontour(X,Y,Z,V):
    fg = figure()
    ax = fg.gca()
    ax.set_title('independent color maps for image and contour')
#%% image with colorbar
    h = ax.imshow(V,vmin=0,vmax=0.2,extent=(-3,3,-2,2),cmap='bone')
    fg.colorbar(h).set_label('image values')
#%% contour over image
    c = ax.contour(X[0,:],Y[:,0],Z)
    ax.clabel(c, inline=1, fontsize=10)

if __name__ == '__main__':
    X,Y,Z,V = testdata_2d()
    plotimagecontour(X,Y,Z,V)
    show()
