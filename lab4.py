import numpy as np
from numpy import pi, exp
from scipy import linalg as LA
import matplotlib.pylab as plt

GAMMA = np.array((0., 0.))
M = np.array((0., 1./2.))
K = np.array((1./3., 1./3.))

e2p = 0.0
gamma_0 = -2.78
s_0 = 0.06


R1 = np.array((0.666667000, 1.333333000))
R2 = np.array((1.333333000,1.666667000))
R3 = np.array((0.333333000, .666667000))

k_vector = []
step = (GAMMA[0]-M[0])/20, (GAMMA[1]-M[1])/20
for i in range(0, 21):
    k_vector.append((M[0]+i*step[0], M[1]+i*step[1]))

step = (K[0]-GAMMA[0])/20, (K[1]-GAMMA[1])/20
for i in range(0, 21):
    k_vector.append((GAMMA[0]+i*step[0], GAMMA[1]+i*step[1]))

step = (M[0]-K[0])/20, (M[1]-K[1])/20
for i in np.arange(0, 21):
    k_vector.append((K[0]+i*step[0], K[1]+i*step[1]))

k_vector = np.array(k_vector)

H = np.zeros((2,2)).astype(np.complex)
S = np.zeros((2,2)).astype(np.complex)
K_E = []
for index, k in enumerate(k_vector):
    ab = exp(1j*np.dot(k*2*pi, R1))+exp(1j*np.dot(k*2*pi, R2))+exp(1j*np.dot(k*2*pi, R3))

    H[0, 0] = e2p
    H[0, 1] = gamma_0*ab    
    H[1, 0] = np.conj(H[0, 1])
    H[1, 1] = e2p

    S[0, 0] = 1
    S[0, 1] = s_0*ab
    S[1, 0] = np.conj(S[0, 1])
    S[1, 1] = 1

    w, v = LA.eig(H, S)
    for energy in np.sort(np.real(w)):
        K_E.append((index, energy))

K_E = np.array(K_E)

plt.scatter(K_E[:, 0], K_E[:, 1])
plt.show()

