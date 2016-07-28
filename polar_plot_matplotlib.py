#!/usr/bin/env python
"""
demo of polar plots in Python Matplotlib
Michael Hirsch
Ref: http://stackoverflow.com/questions/18721762/matplotlib-polar-plot-is-not-plotting-where-it-should

This example is for an azimuth/elevation plot.
Azimuth [0,360) with north at 0 degrees
Elevation [0,90)
"""
from matplotlib.pyplot import show
#
from pyplots.polarplot import polarplot


if __name__ == '__main__':

    # arbitrary test numbers
    az = [10,50,30,185,273]
    el = [30,5, 80,36, 29]

    polarplot(az,el)
    show()