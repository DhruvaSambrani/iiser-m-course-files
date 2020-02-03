import math
# number of data points
n = 150
# number of bins
nbin = 15
#
xbin = range(nbin)
#
xmin = 1000.0
xmax = 0.0
sum1 = 0.0
# open data file
f = open('data.dat', 'r')
x = range(n)
y = range(n)
# find minimum, maximum and average
for i in range(n):
    y[i] = f.readline()
    x[i] = float(y[i])
    sum1 = sum1 + x[i]
    xmin = min(xmin,x[i])
    xmax = max(xmax,x[i])
# loop over
avg = sum1 / n
print 'average = ',avg
# compute bin width
dx = (xmax*1.01 - xmin)/nbin
ibin = range(nbin)
# set lower bin edge
for j in range(nbin):
    ibin[j] = 0
    xbin[j] = xmin + j * dx
# loop over
# find out bin occupancy and std. deviation
sum1 = 0.0
for i in range(n):
    delx = x[i] - xmin
    j = int(delx/dx)
    ibin[j] = ibin[j] + 1
    # find out deviation
    delx = x[i] - avg
    # add square of the deviation
    sum1 = sum1 + delx*delx
# loop over
sig = math.sqrt(sum1/(n-1))
print 'sigma = ',sig
coeff = n*dx/(sig * math.sqrt(2.0 * 3.14159265))
# print results
print 'x','          ','frequency','     ','Gaussian approximation'
for j in range(nbin):
    delx = xbin[j] - avg
    gauss1 = coeff * math.exp(-0.5*delx*delx/(sig*sig))
    print xbin[j],'   ',ibin[j],'      ',gauss1
# loop over

