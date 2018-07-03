#!/usr/bin/env python
"""
Axes3D import must come before other Matplotlib imports

"from mpl_toolkits.mplot3d import Axes3D" needs to come before
the "from matplotlib.pyplot import ...." line in the FIRST file you run.
To be sure, I make the "from mpl_toolkits.mplot3d ..." line come first in my
main function file (the one I invoke from the command line or Spyder)
"""
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
from matplotlib.pyplot import figure, show
from numpy import linspace, meshgrid, pi, sin  # for testing

"""
More sophisticated 3-D plots with Mayavi
    https://github.com/scivision/mayavi-examples
or Plotly (offline or online):
    https://github.com/scivision/plotly3d-examples-python
"""


def test():
    x, y = meshgrid(linspace(0, 2*pi), linspace(0, 2*pi))

    z = sin(x+0.5*y)
    ax = figure().gca(projection='3d')
    ax.plot_wireframe(x, y, z)
    show()


if __name__ == '__main__':
    test()
