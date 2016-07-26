#!/usr/bin/env python
"""
typecasting with h5py HDF5 demo
"""
from tempfile import mkstemp
import h5py
import struct
from numpy import float32,int16
from numpy.testing import assert_array_equal

def demo_h5py_typecast(fn):

    data32 = float32([3.1416, 2.7183, 70000.1]) # true data
    data16 = int16(struct.unpack('%dh' % data32.size*2,data32)) # instrument output stream

    print('using {}'.format(fn))
    with h5py.File(fn,'w') as h:
        h['int16'] = data16 #stream to disk

    with h5py.File(fn,'r') as h: # read and unpack to float
        r32 = float32(struct.unpack('%df' % (h['int16'].size//2),
                                    h['int16'].value))

    assert_array_equal(data32,r32) #exactly equal to original

if __name__ == '__main__':
    fn = mkstemp('.h5')[1]

    demo_h5py_typecast(fn)
