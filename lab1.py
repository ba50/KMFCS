#!/mingw64/bin/python3

import numpy as np
from numpy import sin, cos, pi, sqrt
from scipy.integrate import quad
import itertools
from numpy import linalg as LA
import matplotlib.pyplot as plt

A = 15
a = 10/3
V_0 = 2.5
n = 20
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
"""
for index, x in np.ndenumerate(even):
    even[index[0]][index[1]]    = quad(sin_integrate, -x_max, x_max, args=(index[0]+1, index[1]+1, A))[0]
    odd[index[0]][index[1]]     = quad(cos_integrate, -x_max, x_max, args=(index[0], index[1], A))[0]
"""
for i in range(0,5):
    for j in range(0,5):
        even[i][j]    = quad(sin_integrate, -x_max, x_max, args=(i+1, j+1, A))[0]
        odd[i][j]     = quad(cos_integrate, -x_max, x_max, args=(i, j, A))[0]
for i in range(5,10):
    for j in range(5,10):
        even[i][j]    = quad(sin_integrate, -x_max, x_max, args=(i+1, j+1, A))[0]
        odd[i][j]     = quad(cos_integrate, -x_max, x_max, args=(i, j, A))[0]
for i in range(10,15):
    for j in range(10,15):
        even[i][j]    = quad(sin_integrate, -x_max, x_max, args=(i+1, j+1, A))[0]
        odd[i][j]     = quad(cos_integrate, -x_max, x_max, args=(i, j, A))[0]
for i in range(15,20):
    for j in range(15,20):
        even[i][j]    = quad(sin_integrate, -x_max, x_max, args=(i+1, j+1, A))[0]
        odd[i][j]     = quad(cos_integrate, -x_max, x_max, args=(i, j, A))[0]

w_even, v_even = LA.eig(even)
w_odd, v_odd = LA.eig(odd)

plt.plot(range(1,n+1),w_even)
plt.plot(range(1,n+1),w_odd)
plt.show()

