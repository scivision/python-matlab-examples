#!/usr/bin/env python
"""
matplotlib with datetime64 testing
"""
from datetime import datetime
from matplotlib.pyplot import figure,show
#%% generate data
from numpy import arange
from numpy.random import randn
t = arange('2010-05-04T12:05','2010-05-04T12:16', dtype='datetime64[s]')
y = randn(t.size)

T = t.astype(datetime)
ax = figure().gca()
ax.plot(T,y)

show()
