from numpy.random import rand
from numpy import meshgrid, arange
from matplotlib.mlab import bivariate_normal

def testdata_2d():
    delta = 0.025
    V = 0.1*rand(100,100)
    x = arange(-3.0, 3.0, delta)
    y = arange(-2.0, 2.0, delta)
    X, Y = meshgrid(x, y)
    Z = bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
    return X,Y,Z,V