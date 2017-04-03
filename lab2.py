import numpy as np
from scipy import linalg as LA
import matplotlib.pyplot as plt

import calki

a0 = 1.0

# wyznaczanie N_0
alpha = 10.0
N_E = []
for N in range(3, 8):
    H = np.zeros((N*N, N*N))
    S = np.zeros((N*N, N*N))
    for i, j, k, l in np.ndindex((N, N, N, N)):
        H[N*i+j, N*k+l] = calki.get_T(i+1, j+1, k+1, l+1, alpha) + \
                        calki.get_V(i+1, j+1, k+1, l+1, 1, alpha) + \
                        calki.get_V(i+1, j+1, k+1, l+1, 2, alpha)
        S[N*i+j, N*k+l] = calki.get_S(i+1, j+1, k+1, l+1, alpha)
    w, v = LA.eig(H, S)
    N_E.append((N, np.sort(w)[0]))
N_E = np.array(N_E)
plt.figure()
plt.scatter(N_E[:, 0], N_E[:, 1])

# wyznaczanie alpha
N = 5
alpha_E = []
for alpha in np.arange(9.5, 10.5, 0.05):
    H = np.zeros((N*N, N*N))
    S = np.zeros((N*N, N*N))
    for i, j, k, l in np.ndindex((N, N, N, N)):
        H[N*i+j, N*k+l] = calki.get_T(i+1, j+1, k+1, l+1, alpha) + \
                        calki.get_V(i+1, j+1, k+1, l+1, 1, alpha) + \
                        calki.get_V(i+1, j+1, k+1, l+1, 2, alpha)
        S[N*i+j, N*k+l] = calki.get_S(i+1, j+1, k+1, l+1, alpha)
    w, v = LA.eig(H, S)
    alpha_E.append((alpha, -27.13*(0.5-1.0/(2.0*a0)-np.sort(w)[0])))
alpha_E = np.array(alpha_E)
plt.figure()
plt.scatter(alpha_E[:, 0], alpha_E[:, 1])

plt.show()

