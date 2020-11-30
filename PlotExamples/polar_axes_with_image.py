#!/usr/bin/env python
"""
polar axes over image, using transparent axes

another way to do this would be via contours and plot.
Maybe someone has already made such a boilerplate example?
It would involve reading the "size" of the axes and scaling circles to the axes data, or using normalized axes coordinates.
"""
from matplotlib.pyplot import figure, show
import numpy as np
from pyplots import polarplot
from pyplots.data import random_img


def polar_axes_image(V: np.ndarray):
    fg = figure()
# %% create the image
    ax = fg.gca()
    h = ax.imshow(V, cmap='bone')
    ax.set_title('image overlaid with polar axes')
    fg.colorbar(h).set_label('image values')
# %% create transparent polar axes as a fiducial marking
    ax2 = polarplot(None, None, fig=fg)
    ax2.patch.set_alpha(.5)


def polar_axes_pcolor(X: np.ndarray, Y: np.ndarray, Z: np.ndarray):
    fg = figure()
# %% create the image
    ax = fg.gca()
    h = ax.pcolormesh(X, Y, Z, cmap='bone')
    ax.set_title('pcolor overlaid with polar axes')
    fg.colorbar(h).set_label('image values')
# %% create transparent polar axes as a fiducial marking
    ax2 = polarplot(None, None, fig=fg)
    ax2.patch.set_alpha(.5)


def main():
    X, Y, Z, V = random_img()

    polar_axes_image(V)

    polar_axes_pcolor(X, Y, Z)

    show()


if __name__ == '__main__':
    main()
