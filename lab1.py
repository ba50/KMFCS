import numpy as np
from numpy import sin, cos, pi, sqrt, exp
from scipy.integrate import quad
from numpy import linalg as LA
import matplotlib.pyplot as plt

A = 15
a = 10/3
V_0 = 2.5
R = 1
x_max = 15

def V_Fermi(x):
    return -V_0/(1+exp((np.absolute(x)-a)/R))

def V(x):
    if np.absolute(x) < a:
        return -V_0
    else:
        return 0.0

class Wave:
    def sin_integrate(self, x, i, j, A):
        return  j*j*pi*pi*sin(j*pi*x/A)*sin(i*pi*x/A)/A**3 + sin(i*pi*x/A)*V(x)*sin(j*pi*x/A)/A

    def cos_integrate(self, x, i, j, A):
        if i == 0 and j == 0:
            return V(x)/(2*A)

        if i == 0 and not j == 0:
            return (j*j*pi*pi/A*A+V(x))*cos(j*pi*x/A)/(A*sqrt(2))

        if not i == 0 and j == 0:
            return V(x)*cos(i*pi*x/A)/(A*sqrt(2))

        if not i == 0 and not j == 0:
            return j*j*pi*pi*cos(j*pi*x/A)*cos(i*pi*x/A)/A**3 + cos(i*pi*x/A)*V(x)*cos(j*pi*x/A)/A

    def wave_odd(self, a, b, energy_id):
        wave_x=[]
        wave_y=[]
        for x in np.arange(a, b, 0.1):
            sum_temp=0
            for index, c in np.ndenumerate(self.v_odd[:, self.sort_odd[energy_id][0]]):
                sum_temp = sum_temp + c*sin(index[0]*pi*x/A)/sqrt(A)
            wave_x.append(x)
            wave_y.append(sum_temp)
        return wave_x, wave_y

    def wave_even(self, a, b, energy_id):
        wave_x=[]
        wave_y=[]
        for x in np.arange(a, b, 0.1):
            sum_temp=0
            for index, c in np.ndenumerate(self.v_even[:, self.sort_even[energy_id][0]]):
                if index == 0:
                    sum_temp = sum_temp + 1/sqrt(2*A)
                else:
                    sum_temp = sum_temp + c*cos(index[0]*pi*x/A)/sqrt(A)
            wave_x.append(x)
            wave_y.append(sum_temp)
        return wave_x, wave_y

    def plot(self):
        v_y=[]
        for x in range(-x_max, x_max):
            v_y.append(V(x))

        plt.figure()
        wave_x, wave_y = self.wave_even(-x_max, x_max, 0)
        plt.plot(wave_x, wave_y)
        wave_x, wave_y = self.wave_even(-x_max, x_max, 1)
        plt.plot(wave_x, wave_y)
        plt.plot(range(-x_max, x_max), v_y)

        plt.figure()
        wave_x, wave_y = self.wave_odd(-x_max, x_max, 0)
        plt.plot(wave_x, wave_y)
        wave_x, wave_y = self.wave_odd(-x_max, x_max, 1)
        plt.plot(wave_x, wave_y)
        plt.plot(range(-x_max, x_max), v_y)

    def __init__(self, n):
        self.even = np.zeros((n, n))
        self.odd = np.zeros((n, n))

        for index, x in np.ndenumerate(self.even):
            self.even[index[0]][index[1]]   = quad(self.cos_integrate, -x_max, x_max, args=(index[0], index[1], A), limit=100)[0]
            self.odd[index[0]][index[1]]    = quad(self.sin_integrate, -x_max, x_max, args=(index[0]+1, index[1]+1, A), limit=100)[0]

        self.w_even, self.v_even = LA.eig(self.even)
        self.w_odd, self.v_odd = LA.eig(self.odd)

        dtype = [ ('number', int), ('energy', float)]

        values = []
        for index, w in np.ndenumerate(self.w_even):
            values.append((index[0], w))
        self.sort_even = np.array(values, dtype=dtype)
        self.sort_even.sort(order='energy')
        del values

        values = []
        for index, w in np.ndenumerate(self.w_odd):
            values.append((index[0], w))
        self.sort_odd = np.array(values, dtype=dtype)
        self.sort_odd.sort(order='energy')
        del values

if __name__ == '__main__':
    wave_list = []
    wave_list_sort_even = []
    N = range(15, 20)
    for n in N:
        wave = Wave(n)
        wave_list.append(wave)
        wave_list_sort_even.append(wave.sort_even[0][1])

    np.savetxt('sin_energy.dat', wave_list[-1].sort_odd[0:3], delimiter='\t', fmt='%.2f')
    with open('sin_energy.dat', 'r') as orginal: data = orginal.read()
    with open('sin_energy.dat', 'w') as modefide: modefide.write("number\tEnergy\n"+data)
    np.savetxt('cos_energy.dat', wave_list[-1].sort_even[0:3], delimiter='\t', fmt='%.2f')
    with open('cos_energy.dat', 'r') as orginal: data = orginal.read()
    with open('cos_energy.dat', 'w') as modefide: modefide.write("number\tEnergy\n"+data)


    plt.scatter(N, wave_list_sort_even)
    wave_list[-1].plot()
    plt.show()
