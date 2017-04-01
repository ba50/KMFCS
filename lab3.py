import numpy as np
from numpy import pi, sqrt, sin
from numpy import linalg as LA

a = 10
b = 1
V_0 = 1
E_cut = 12
npw = int(sqrt(E_cut/(2*pi/a)**2)+.5)
npw = 2*npw + 1

G = np.fromfunction(lambda n, m: (2*pi/a)*n, (npw, 1))
K = np.arange(-pi/a, pi/a, (2*pi/a)/30, dtype=float)
H = np.zeros((npw, npw), dtype=float)

H_K = []
for k in K:
    for index, h in np.ndenumerate(H):
        if index[0] == index[1]:
            H[index] = (k+G[index[0]])**2-V_0/(a*b)
        else:
            H[index] = -V_0/a*sin((G[index[1]]-G[index[0]])*b/2)/((G[index[1]]-G[index[0]])/2)
    H_K.append(H)

print(H_K[0])
