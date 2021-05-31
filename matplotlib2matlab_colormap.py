#!/usr/bin/env python
"""
extract Matplotlib colormap values for use in Matlab / GNU Octave

"""
from argparse import ArgumentParser
from pathlib import Path
from matplotlib import cm
from matplotlib.pyplot import colormaps


def matplotlib2matlab_colormap(cmap_name: str = None, outdir: str = ''):

    cmap = cm.get_cmap(cmap_name)

    name = cmap.name

    fn = Path(outdir) / f'{name}.m'

    print('writing', fn)

    with fn.open('w') as f:
        f.write(f"function cmap = {name}()\n\n")
        f.write("cmap = [")

        for i in range(cmap.N):
            c = cmap(i)
            f.write(f'{c[0]},{c[1]},{c[2]};\n')

        f.write('];\n\n')
        f.write('end')


if __name__ == '__main__':
    p = ArgumentParser()
    p.add_argument('cmap_name', nargs='?')
    p.add_argument('outdir', nargs='?', default='colormaps')
    p = p.parse_args()

    if p.cmap_name is not None:
        matplotlib2matlab_colormap(p.cmap_name, p.outdir)
    else:
        for cmap in colormaps():
            matplotlib2matlab_colormap(cmap, p.outdir)
