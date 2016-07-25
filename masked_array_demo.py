import numpy as np
from numpy.random import rand,randn
import numpy.ma as ma

# ficticious data vectors
L = 128
v1 = randn(L)
v2 = randn(L)
v3 = randn(L)

#point cloud
N = 8
cloud = rand(N,N)#,N) #made it 2-D for clarity of example
# assign masked array -- trivial way to pick about 90% of points = v1
ucloud = ma.masked_where(cloud>0.1, cloud, False) #preserve memory through view
Nu = ma.count(ucloud)
print('number of unique points is', Nu,'out of',ucloud.size,'total points')
#work on unique values (the 10% visible in cloudunique)
uind = np.array(ucloud.nonzero()).T #maybe there is a better way to iterate using original tuple

for i in range(Nu): #operate on each unique vector
    y = ucloud[uind[i,0],uind[i,1]]*1000*v2
