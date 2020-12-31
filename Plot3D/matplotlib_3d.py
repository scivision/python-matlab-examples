#!/usr/bin/env python3

from matplotlib.pyplot import figure, show
from numpy import linspace, meshgrid, pi, sin  # for testing

"""
More sophisticated 3-D plots with Mayavi
    https://github.com/scivision/mayavi-examples
or Plotly (offline or online):
    https://github.com/scivision/plotly3d-examples-python
"""


def test():
    x, y = meshgrid(linspace(0, 2 * pi), linspace(0, 2 * pi))

    z = sin(x + 0.5 * y)
    ax = figure().gca(projection="3d")
    ax.plot_wireframe(x, y, z)
    show()


if __name__ == "__main__":
    test()
