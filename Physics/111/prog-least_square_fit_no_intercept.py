import math
import numpy as np
import matplotlib.pyplot as pl
# Number of data points
n=4
# Data
sx2 = 0.0
sxy = 0.0
for i in range(n):
    sx2 = sx2 + x[i]*x[i]
    sxy = sxy + x[i]*y[i]
# loop over
m = sxy/sx2
print ("m =",m)

X=np.arange(0,1.51,0.01)
pl.plot(X,m*X,'r')
pl.plot(x,y,'o')
pl.show()
