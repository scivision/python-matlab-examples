#!/usr/bin/env python3
"""
Matplotlib Pcolormesh should work with numpy.float32 (it does here)
"""

from matplotlib.pyplot import figure, show
import numpy as np
import numpy.random

N = 16

d64 = numpy.random.random((N, N))
d32 = d64.astype(np.float32)
d16 = d64.astype(np.float16)

x = np.array(range(N))
y = np.array(range(N))

fg = figure(figsize=(12, 5))
ax = fg.subplots(1, 3, sharey=True, sharex=True)

ax[0].pcolormesh(x, y, d64, shading="nearest")
ax[1].pcolormesh(x, y, d32, shading="nearest")
ax[2].pcolormesh(x, y, d16, shading="nearest")

ax[0].set_title(str(d64.dtype))
ax[1].set_title(str(d32.dtype))
ax[2].set_title(str(d16.dtype))

show()
