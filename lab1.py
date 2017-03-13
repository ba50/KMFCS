#!/mingw64/bin/python3

import numpy as np
from numpy import sin, cos, pi, sqrt
from scipy.integrate import quad
import itertools
from numpy import linalg as LA
import matplotlib.pyplot as plt

A = 15
a = 10/3
V_0 = -2.5
n = 15
x_max = 15

def V(x):
    if np.absolute(x) < a:
        return V_0
    else:
        return 0.0

def sin_integrate(x, i, j, A):
    return  j*j*pi*pi*sin(j*pi*x/A)*sin(i*pi*x/A)/A**3 + sin(i*pi*x/A)*V(x)*sin(j*pi*x/A)/A

def cos_integrate(x, i, j, A):
    if i == 0 and j == 0:
        return V(x)/(2*A)

    if i == 0 and not j == 0:
        return 1/sqrt(2*A)*(V(x)*cos(j*pi*x/A)+j**2*pi**2*cos(j*pi/A)/A**2)

    if not i == 0 and j == 0:
        return V(x)/sqrt(2*A)+cos(i*pi*x/A)

    if not i == 0 and not j == 0:
        return cos(i*pi*x/A)*V(x)*cos(j*pi*x/A) + j**2*pi**2*cos(j*pi*x/A)*cos(i*pi*x/A)/A**2

def wave_even(a, b, sort_w, v, energy_id):
    wave_x=[]
    wave_y=[]
    for x in np.arange(a, b, 0.1):
        sum_temp=0
        for index, c in np.ndenumerate(v[:, sort_w[energy_id][0]]):
            sum_temp = sum_temp + c*sin(index[0]*pi*x/A)/sqrt(A)
        wave_x.append(x)
        wave_y.append(sum_temp)
    return wave_x, wave_y

def wave_odd(a, b, sort_w, v, energy_id):
    wave_x=[]
    wave_y=[]
    for x in np.arange(a, b, 0.1):
        sum_temp=0
        for index, c in np.ndenumerate(v[:, sort_w[energy_id][0]]):
            if index == 0:
                sum_temp = sum_temp + 1/sqrt(2*A)
            else:
                sum_temp = sum_temp + c*cos(index[0]*pi*x/A)/sqrt(A)
        wave_x.append(x)
        wave_y.append(np.real(sum_temp))
    return wave_x, wave_y

even = np.zeros((n, n))
odd = np.zeros((n, n))

for index, x in np.ndenumerate(even):
    even[index[0]][index[1]]   = quad(sin_integrate, -x_max, x_max, args=(index[0]+1, index[1]+1, A), limit=100)[0]
    odd[index[0]][index[1]]   = quad(cos_integrate, -x_max, x_max, args=(index[0], index[1], A), limit=100)[0]

w_even, v_even = LA.eig(even)
w_odd, v_odd = LA.eig(odd)

dtype = [ ('number', int), ('energy', float)]

values = []
for index, w in np.ndenumerate(w_even): 
    values.append((index[0], w))
sort_even = np.array(values, dtype=dtype)
sort_even.sort(order='energy')
del values

values = []
for index, w in np.ndenumerate(w_odd): 
    values.append((index[0], np.real(w)))
sort_odd = np.array(values, dtype=dtype)
sort_odd.sort(order='energy')
del values

v_y=[]
for x in range(-x_max, x_max):
    v_y.append(V(x))


plt.figure()
wave_x, wave_y = wave_even(-x_max, x_max, sort_even, v_even, 0)
plt.plot(wave_x, wave_y)
wave_x, wave_y = wave_even(-x_max, x_max, sort_even, v_even, 1)
plt.plot(wave_x, wave_y)
plt.plot(range(-x_max, x_max), v_y)

plt.figure()
wave_x, wave_y = wave_odd(-x_max, x_max, sort_odd, v_odd, 0)
plt.plot(wave_x, wave_y)
wave_x, wave_y = wave_odd(-x_max, x_max, sort_odd, v_odd, 1)
plt.plot(wave_x, wave_y)
plt.plot(range(-x_max, x_max), v_y)

plt.show()

