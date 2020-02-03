import math
import numpy as np
import matplotlib.pyplot as pl
# Number of data points
n=5
# Data
x = list(range(30,180,30))
y = [1.906,2.588,3.072,3.554,3.834]
y = [i**2 for i in y]
print (y)
sx = 0.0
sx2 = 0.0
sy = 0.0
sxy = 0.0
for i in range(n):
    sx = sx + x[i]
    sx2 = sx2 + x[i]*x[i]
    sy = sy + y[i]
    sxy = sxy + x[i]*y[i]
# loop over
m = (sx*sy-float(n)*sxy)/(sx*sx - float(n)*sx2)
c = (sx*sxy - sx2*sy)/(sx*sx - float(n)*sx2)
print ("m =", m)
print ("c =", c)
print ("Theta =", math.asin(2.0/(9.8*m)))

X=np.arange(0,151)
pl.plot(X,m*X,'r')
pl.plot(x,y,'o')
pl.show()
