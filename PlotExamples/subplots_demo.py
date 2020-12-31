#!/usr/bin/env python
"""
requires Matplotlib >= 2.1
add_subplot() on a new figure can give more control when needed.
"""
from matplotlib.pyplot import figure, show
import numpy as np

P = "Press Enter to continue to next plot..."

# Simple data to display in various forms
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

# Just a figure and one subplot
ax = figure(1, clear=True).subplots()
ax.plot(x, y)
ax.set_title("Simple plot")
show(False)
input(P)

# Two subplots, the axes array is 1-d
axs = figure(1, clear=True).subplots(2, sharex=True)
axs[0].plot(x, y)
axs[0].set_title("Sharing X axis")
axs[1].scatter(x, y)
show(False)
input(P)

# Two subplots, unpack the axes array immediately
ax1, ax2 = figure(1, clear=True).subplots(1, 2, sharey=True)
ax1.plot(x, y)
ax1.set_title("Sharing Y axis")
ax2.scatter(x, y)
show(False)
input(P)

# Three subplots sharing both x/y axes
fig = figure(1, clear=True)
ax1, ax2, ax3 = fig.subplots(3, sharex=True, sharey=True)
ax1.plot(x, y)
ax1.set_title("Sharing both axes")
ax2.scatter(x, y)
ax3.scatter(x, 2 * y ** 2 - 1, color="r")
# Fine-tune figure; make subplots close to each other and hide x ticks for
# all but bottom plot.
fig.subplots_adjust(hspace=0)
show(False)
input(P)

# row and column sharing
((ax1, ax2), (ax3, ax4)) = figure(1, clear=True).subplots(2, 2, sharex="col", sharey="row")
ax1.plot(x, y)
ax1.set_title("Sharing x per column, y per row")
ax2.scatter(x, y)
ax3.scatter(x, 2 * y ** 2 - 1, color="r")
ax4.plot(x, 2 * y ** 2 - 1, color="r")
show(False)
input(P)

# %% Four axes, returned as a 2-d array
axarr = figure(1, clear=True).subplots(2, 2)
axarr[0, 0].plot(x, y)
axarr[0, 0].set_title("Axis [0,0]")
axarr[0, 1].scatter(x, y)
axarr[0, 1].set_title("Axis [0,1]")
axarr[1, 0].plot(x, y ** 2)
axarr[1, 0].set_title("Axis [1,0]")
axarr[1, 1].scatter(x, y ** 2)
axarr[1, 1].set_title("Axis [1,1]")

# %% Four polar axes
figure(1, clear=True).subplots(2, 2, subplot_kw=dict(polar=True))
show()
