#!/usr/bin/env python
"""
example of putting git short revision in matplotlib plot, up in the corner
(rather than in title where git revision text is too large)

This is helpful for when a colleague wants a plot exactly recreated from a year ago,
 to help find the exact code used to create that plot.

http://matplotlib.org/api/figure_api.html
"""
import subprocess
from matplotlib.pyplot import figure, show

try:
    gitrev = subprocess.check_output(
        ["git", "rev-parse", "--short", "HEAD"], universal_newlines=True
    ).strip("\n")
except Exception:  # maybe they don't have git installed
    gitrev = ""

fg = figure()
ax = fg.gca()
ax.plot([1, 2])
ax.set_title("my cool plot")
fg.text(1.0, 1.0, "git: " + gitrev, ha="right", va="top", rotation="vertical")

show()
