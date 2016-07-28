#!/usr/bin/env python
"""
Plots an image, then plots a contour over top of the image
"""
from numpy.random import rand
from numpy import meshgrid, arange
from matplotlib.pyplot import figure,show
from matplotlib.mlab import bivariate_normal

def testdata():
    delta = 0.025
    V = 0.1*rand(100,100)
    x = arange(-3.0, 3.0, delta)
    y = arange(-2.0, 2.0, delta)
    X, Y = meshgrid(x, y)
    Z = bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
    return X,Y,Z,V

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
    X,Y,Z,V = testdata()
    plotimagecontour(X,Y,Z,V)
    show()
