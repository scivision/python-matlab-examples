#!/usr/bin/env python
import numpy as np
from bokeh.plotting import show, figure, output_file

N = 100

x = np.linspace(0, 4 * np.pi, N)
y = np.sin(x)

output_file("legend.html", title="legend.py example", mode="cdn")

fg1 = figure(tools="pan,wheel_zoom,box_zoom,reset,previewsave")

fg1.scatter(x, y, legend="sin(x)")
fg1.scatter(x, 2 * y, color="orange", legend="2*sin(x)")
fg1.scatter(x, 3 * y, color="green", legend="3*sin(x)")

fg2 = figure(tools="pan,wheel_zoom,box_zoom,reset,previewsave")

fg2.scatter(x, y, legend="sin(x)", name="legend_example")
fg2.line(x, y, legend="sin(x)")

fg2.line(x, 2 * y, line_dash=[4, 4], line_color="orange", line_width=2, legend="2*sin(x)")

fg2.square(x, 3 * y, line_color="green", legend="3*sin(x)")
fg2.line(x, 3 * y, line_color="green", legend="3*sin(x)")

show(fg1)
show(fg2)  # open a browser
