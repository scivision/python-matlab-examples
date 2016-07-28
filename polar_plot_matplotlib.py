#!/usr/bin/env python
"""
demo of polar plots in Python Matplotlib
Michael Hirsch
Ref: http://stackoverflow.com/questions/18721762/matplotlib-polar-plot-is-not-plotting-where-it-should

This example is for an azimuth/elevation plot.
Azimuth [0,360) with north at 0 degrees
Elevation [0,90)

We reverse direction of "elevation" to make center of plot 90 deg.
"""
import numpy as np
from matplotlib.pyplot import figure,show

def polarplot(az,el,minel=0.,delv=10.):
    """
    az: azimuths of points to plot (degrees)
    el: elevation (above horizon) of points to plot (degrees)

    minel: minimum elevation angle (degrees) to plot (axes limit)
    delv: increment to label elevation angles (degrees)
    """

    # astype(float) because some programs give off lists or object arrays that radians() doesn't like
    az = np.radians(np.asarray(az).astype(float))
    el = 90. - np.asarray(el).astype(float)

    ax = figure().gca(polar=True) # Note the polar=True keyword

    ax.plot(az,el, marker='o',linestyle='none') # you can use other markers or linestyles too
#%% boilerplate
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)

    yl = np.arange(0., 90.-minel+delv, delv)
    ylbl = (yl[::-1]+minel).astype(int).astype(str)
    ax.set_yticks(yl)
    ax.set_yticklabels(ylbl)

if __name__ == '__main__':

    # arbitrary test numbers
    az = [10,50,30,185,273]
    el = [30,5, 80,36, 29]

    polarplot(az,el)
    show()