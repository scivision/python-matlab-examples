import numpy as np
from matplotlib.pyplot import figure


def polarplot(az, el, minel=0.0, delv=10.0, fig=None):
    """
    az: azimuths of points to plot (degrees)
    el: elevation (above horizon) of points to plot (degrees)

    minel: minimum elevation angle (degrees) to plot (axes limit)
    delv: increment to label elevation angles (degrees)
    """

    # astype(float) because some programs give off lists or object arrays that radians() doesn't like
    az = np.radians(np.asarray(az).astype(float))
    el = 90.0 - np.asarray(el).astype(float)

    try:
        ax = fig.gca(polar=True)
    except AttributeError:
        ax = figure().gca(polar=True)  # Note the polar=True keyword

    # ax.plot(az,el, marker='o',linestyle='none') # you can use other markers or linestyles too
    # %% boilerplate
    #     We reverse direction of "elevation" to make center of plot 90 deg.
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)

    yl = np.arange(0.0, 90.0 - minel + delv, delv)
    ylbl = (yl[::-1] + minel).astype(int).astype(str)
    ax.set_yticks(yl)
    ax.set_yticklabels(ylbl)

    return ax
