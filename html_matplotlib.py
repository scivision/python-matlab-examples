#!/usr/bin/env python
"""simplest example of Matplotlib to the web browser"""
from matplotlib.pyplot import figure
import mpld3

fig = figure()
ax = fig.gca()
ax.plot([1,2,3,4])

mpld3.show(fig)
