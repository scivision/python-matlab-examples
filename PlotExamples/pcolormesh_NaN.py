#!/usr/bin/env python
import numpy as np
from matplotlib.pyplot import figure, show


def pcolormesh_nan(x: np.ndarray, y: np.ndarray, c: np.ndarray, cmap=None, axis=None):
    """handles NaN in x and y by smearing last valid value in column or row out,
    which doesn't affect plot because "c" will be masked too
    """

    mask = np.isfinite(x) & np.isfinite(y)
    top = None
    bottom = None

    for i, m in enumerate(mask):
        good = m.nonzero()[0]

        if good.size == 0:
            continue
        elif top is None:
            top = i
        else:
            bottom = i

        x[i, good[-1]:] = x[i, good[-1]]
        y[i, good[-1]:] = y[i, good[-1]]

        x[i, :good[0]] = x[i, good[0]]
        y[i, :good[0]] = y[i, good[0]]

    x[:top, :] = np.nanmax(x[top, :])
    y[:top, :] = np.nanmax(y[top, :])

    x[bottom:, :] = np.nanmax(x[bottom, :])
    y[bottom:, :] = np.nanmax(y[bottom, :])

    if axis is None:
        axis = figure().gca()

    axis.pcolormesh(x, y, np.ma.masked_where(~mask, c), cmap=cmap)


def main():
    N = 64
    r = 4

    x = np.linspace(-5., 5., N)
    y = np.linspace(-10., 10., N)

    x, y = np.meshgrid(x, y)
    mask = x**2 + y**2 <= r**2
    x[~mask] = np.nan
    print(mask)

    c = np.random.random((N, N))

    ax = figure(1).gca()
    pcolormesh_nan(x, y, c, cmap='gray', axis=ax)

    show()


if __name__ == '__main__':
    main()
