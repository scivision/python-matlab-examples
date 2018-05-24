#!/usr/bin/env python
"""
This method is for the desparate, you would need to hand-label individual plots.
It's not accurate automatically without a transform!
"""
from matplotlib.pyplot import figure,show
import matplotlib.ticker as mt
import cartopy
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

GREF = cartopy.crs.Stereographic()

def main():
    fg = figure(figsize=(6,6))

    ax = fg.gca(projection=GREF)

    ax.add_feature(cartopy.feature.COASTLINE, linewidth=0.5, linestyle=':')
    ax.add_feature(cartopy.feature.NaturalEarthFeature(
            'cultural', 'admin_1_states_provinces', '50m',
                                  linestyle=':',linewidth=0.5, edgecolor='grey', facecolor='none'))

# %% Gridlines
    #gl = ax.gridlines(crs=GREF, draw_labels=True,
     #             linewidth=1, color='gray', alpha=0.5, linestyle='--')
    gl = ax.gridlines(crs=cartopy.crs.PlateCarree(),color='gray', linestyle='--',
                      linewidth=1)
#    gl.xlabels_top = False
#    gl.ylabels_left = False
#    gl.xformatter = LONGITUDE_FORMATTER
#    gl.yformatter = LATITUDE_FORMATTER
#    # optional
#    gl.xlocator = mt.FixedLocator(range(-140,-40,20))
#    gl.ylocator = mt.FixedLocator(range(20,54,4))
#
    lims = (-120, -60,30,50)

    ax.set_extent(lims)

    # this is actually not correct.
    fg.text(0.1,0.1,lims[0],ha='center')
    fg.text(0.5,0.1, (lims[1]-lims[0])/2+lims[0],ha='center')
    fg.text(0.9,0.1,lims[1],ha='center')


    fg.text(0.5,0.05,'longitude [deg]',ha='center')

if __name__ == '__main__':
    main()

    show()
