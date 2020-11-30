#!/usr/bin/env python
"""
Example where minimum is white colormap using CubeHelix reversed colormap.

http://scikit-image.org/docs/dev/api/skimage.util.html
http://docs.astropy.org/en/stable/api/astropy.convolution.AiryDisk2DKernel.html
"""
import numpy as np
from astropy.convolution import AiryDisk2DKernel
from astropy.convolution import convolve
from skimage.util import random_noise
from matplotlib.pyplot import figure, show
#
Nairy = 5


def starsim(N=256):
    im = np.zeros((N, N))
    im = random_noise(im, 'salt', amount=0.0001)
    im = convolve(im, AiryDisk2DKernel(Nairy))

    return im


def main():
    im = starsim()

    fig = figure()
    ax = fig.gca()
    h = ax.imshow(im, cmap='cubehelix_r', origin='lower')
    fig.colorbar(h)

    show()


if __name__ == '__main__':
    main()
