#!/usr/bin/env python
"""
Add fonts to Matplotlib (for any operating system)

1. add the new font to your operating system.
   In this example, I'll add a Chinese font to Ubuntu::

       apt install fonts-wqy-zenhei
2. Update Matplotlib font cache with this script.

HOWEVER, this didn't work for me on multiple PCs with Matplotlib 2.2.0

See https://github.com/scivision/histfeas/blob/master/Plots/FirstAuroralConjugate.py
"""
import matplotlib

# %% remove old font cache
cachepath = matplotlib.get_cachedir()


matplotlib.font_manager._rebuild()
