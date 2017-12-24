#!/usr/bin/env python
"""
Matplotlib backend-agnostic interactive GUI

https://matplotlib.org/api/widgets_api.html
https://matplotlib.org/gallery/index.html#widgets

Observe the use of nested functions to keep variables in scope.
"""
import numpy as np
from matplotlib.pyplot import figure, show
from matplotlib.widgets import Slider, Button, RadioButtons


def slider_radio():
    def update(val):
        amp = samp.val
        freq = sfreq.val
        l.set_ydata(amp*np.sin(2*np.pi*freq*t))
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
    s = a0*np.sin(2*np.pi*f0*t)
    l, = ax.plot(t, s, lw=2, color='red')
    ax.axis([0, 1, -10, 10])

    axcolor = 'lightgoldenrodyellow'
    axfreq = fig.add_axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
    axamp = fig.add_axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

    sfreq = Slider(axfreq, 'Freq', 0.1, 30.0, valinit=f0)
    samp = Slider(axamp, 'Amp', 0.1, 10.0, valinit=a0)
    sfreq.on_changed(update)
    samp.on_changed(update)

    resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
    button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

    button.on_clicked(reset)

    rax = fig.add_axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)
    radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)
    radio.on_clicked(colorfunc)



if __name__ == '__main__':
    slider_radio()
    show()