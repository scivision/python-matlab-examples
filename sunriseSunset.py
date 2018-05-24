#!/usr/bin/env python
import ephem
import datetime

Boston=ephem.Observer()
Boston.lat='42.3462'
Boston.lon='-71.0978'
Boston.date = datetime.datetime.now()
# %% these parameters are for super-precise estimates, not necessary.
Boston.elevation = 3 # meters
Boston.pressure = 1010 # millibar
Boston.temp = 25 # deg. Celcius
Boston.horizon = 0

sun = ephem.Sun()

print("Next sunrise in Boston will be: ",ephem.localtime(Boston.next_rising(sun)))
print("Next sunset in Boston will be: ",ephem.localtime(Boston.next_setting(sun)))