#!/mingw64/bin/python3

import numpy as np
from numpy import sin, cos, pi, sqrt
from scipy.integrate import quad

A = 15
a = 10/3
V_0 = 2.5
n = 3
x_max = 15

def V(x):
    if np.absolute(x) < a:
        return V_0
    else:
        return 0.0

def sin_integrate(x, i, j, A):
    return sin(i*pi*x/A)*V(x)*sin(j*pi*x/A) - j**2*pi**2*sin(j*pi*x/A)*sin(i*pi*x/A)/A**2

def cos_integrate(x, i, j, A):
    if i == 0 and j == 0:
        return V(x)/(2*A)

    if i == 0 and not j == 0:
        return 1/sqrt(2*A)*(V(x)*cos(j*pi*x/A)-j**2*pi**2*cos(j*pi/A)/A**2)

    if not i == 0 and j == 0:
        return V(x)/sqrt(2*A)+cos(i*pi*x/A)

    if not i == 0 and not j == 0:
        return cos(i*pi*x/A)*V(x)*cos(j*pi*x/A) - j**2*pi**2*cos(j*pi*x/A)*cos(i*pi*x/A)/A**2

even = np.zeros((n, n))
odd = np.zeros((n, n))

for index, x in np.ndenumerate(even):
    even[index[0]][index[1]]    = quad(sin_integrate, -x_max, x_max, args=(index[0], index[1], A))[0]
    odd[index[0]][index[1]]     = quad(cos_integrate, -x_max, x_max, args=(index[0], index[1], A))[0]

H = np.zeros((2*n,2*n))
for id in range(0,n):
        H[2*id][2*id] = even[id][id]
        H[2*id+1][2*id+1] = odd[id][id]
print(H)

