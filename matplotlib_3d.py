#!/usr/bin/env python
from mpl_toolkits.mplot3d import Axes3D # this line must come before the next line!
from matplotlib.pyplot import figure,show
from numpy import linspace,meshgrid,pi,sin #for testing
'''
key point: the line "from mpl_toolkits.mplot3d import Axes3D" needs to come before
the "from matplotlib.pyplot import ...." line in the FIRST file you run.
To be sure, I make the "from mpl_toolkits.mplot3d ..." line come first in my
main function file (the one I invoke from the command line or Spyder)
'''

"""
You can do much more sophisticated 3-D plots with Mayavi
    https://github.com/scivision/mayavi-examples
or Plotly (offline or online):
    https://github.com/scivision/plotly3d-examples-python
"""

def test():
    x,y = meshgrid(linspace(0,2*pi),linspace(0,2*pi))

    z = sin(x+0.5*y)
    ax = figure().gca(projection='3d')
    ax.plot_wireframe(x,y,z)
    show()


if __name__ == '__main__':
    test()
