#!/usr/bin/env python
"""
Matplotlib backend-agnostic interactive GUI

https://matplotlib.org/api/widgets_api.html
https://matplotlib.org/gallery/index.html#widgets

Observe the use of nested functions to keep variables in scope.
Most important is that ALL axes widgets remain in scope!
    otherwise you'll get unpredictable non-responsible behavior
    as the GUI objects are garbage-collected.

It might seem silly to just throw all the widgets into a list and pass them out,
but that's one clean way to keep them in scope.
"""
import numpy as np
from matplotlib.pyplot import figure, show
from matplotlib.widgets import Slider, Button, RadioButtons


def slider_radio():
    def update(val):
        amp = samp.val
        freq = sfreq.val
        l.set_ydata(amp * np.sin(2 * np.pi * freq * t))
        fig.canvas.draw_idle()

    def reset(event):
        sfreq.reset()
        samp.reset()

    def colorfunc(label):
        l.set_color(label)
        fig.canvas.draw_idle()

    fig = figure()
    ax = fig.subplots()
    fig.subplots_adjust(left=0.25, bottom=0.25)
    t = np.arange(0.0, 1.0, 0.001)
    a0 = 5
    f0 = 3
    s = a0 * np.sin(2 * np.pi * f0 * t)
    (l,) = ax.plot(t, s, lw=2, color="red")
    ax.axis([0, 1, -10, 10])
    # %% plot axes
    axcolor = "lightgoldenrodyellow"
    axfreq = fig.add_axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
    axamp = fig.add_axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
    # %% freq slide
    sfreq = Slider(axfreq, "Freq", 0.1, 30.0, valinit=f0)
    samp = Slider(axamp, "Amp", 0.1, 10.0, valinit=a0)
    sfreq.on_changed(update)
    samp.on_changed(update)
    # %% reset button
    resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
    button = Button(resetax, "Reset", color=axcolor, hovercolor="0.975")

    button.on_clicked(reset)
    # %% color buttons
    rax = fig.add_axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)
    radio = RadioButtons(rax, ("red", "blue", "green"), active=0)
    radio.on_clicked(colorfunc)
    # %% scoping
    axw = [
        axfreq,
        axamp,
        sfreq,
        samp,
        button,
        radio,
    ]  # place to hold all the axesWidgets to keep in scope

    return axw  # MUST return ax or GUI will be non-responsive!


if __name__ == "__main__":
    axw = slider_radio()  # have to keep "ax" in scope or GUI is non-responsive.

    show()
