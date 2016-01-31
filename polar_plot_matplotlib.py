#!/usr/bin/env python3
"""
demo of polar plots in Python Matplotlib
Michael Hirsch
Ref: http://stackoverflow.com/questions/18721762/matplotlib-polar-plot-is-not-plotting-where-it-should

This example is for an azimuth/elevation plot.
Azimuth [0,360) with north at 0 degrees
Elevation [0,90)
"""

"""
We have to reverse direction of "elevation"
"""
from numpy import array,radians,atleast_1d
from matplotlib.pyplot import figure,show

def polarplot(az,el):
    #copied from satkml
    """
    I use astype(float) because some programs give off lists or object arrays that radians() doesn't like
    """
    az = radians(atleast_1d(az).astype(float))
    el = 90 - atleast_1d(el).astype(float)

    ax2=figure().gca(polar=True)
    ax2.plot(az,el, marker='o',linestyle='none')
    ax2.set_theta_zero_location('N')
    ax2.set_theta_direction(-1)
    ax2.set_yticks(range(0, 90+10, 10))                   # Define the yticks
    yLabel = ['90', '', '', '60', '', '', '30', '', '', '']
    ax2.set_yticklabels(yLabel)

if __name__ == '__main__':

    # arbitrary test numbers
    az = array([10,50,30,185,273])
    el = array([30,5, 80,36, 29])

    polarplot(az,el)
    show()