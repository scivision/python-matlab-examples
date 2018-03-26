#!/usr/bin/env python
"""
matplotlib with datetime64 testing
"""
from datetime import datetime
from matplotlib.pyplot import figure,show
import matplotlib.dates as mdates
import numpy as np


def atest_plot2d_datetime():
    t = np.arange('2010-05-04T12:05:00','2010-05-04T12:05:01', dtype='datetime64[ms]')
    y = np.random.randn(t.size)

    #t = t.astype(datetime)  # Matplotlib < 2.2

    ax = figure().gca()
    ax.plot(t,y)


def test_imshow_datetime():
    """
    keogram using matplotlib imshow
    """
    Ny = 500  # arbitrary

    t = np.arange('2010-05-04T12:05','2010-05-04T12:06', dtype='datetime64[s]').astype(datetime)
    im = np.random.random((Ny, t.size))
    y = range(t.size) # arbitrary

    mt = mdates.date2num((t[0],t[-1]))

    fig = figure()
    ax = fig.gca()
    ax.imshow(im, extent=[mt[0],mt[1], y[0],y[-1]], aspect='auto')
# %% datetime formatting
    ax.xaxis_date()  # like "num2date"

    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))


    fig.autofmt_xdate()


if __name__ == '__main__':
    np.testing.run_module_suite()


    show()
