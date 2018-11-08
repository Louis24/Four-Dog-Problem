import matplotlib.pyplot as plt
import numpy as np


def pursuit(l, v):
    A = np.array([0, 0])
    B = np.array([l, 0])
    C = np.array([l, l])
    D = np.array([0, l])
    t = 1  # simulation time interval

    while l > 0.01:
        l = np.linalg.norm(A - B)
        # Sn+1=Sn+Vn*△t
        E = A  # with out this line it will crashed to 3 points at the end l=10 v=1 t=1
        A = A + (B - A) / l * v * t
        B = B + (C - B) / l * v * t
        C = C + (D - C) / l * v * t
        D = D + (E - D) / l * v * t
        plt.figure(num=0, figsize=(7, 7))
        plt.plot(A[0], A[1], 'rv')
        plt.plot(B[0], B[1], 'gs')
        plt.plot(C[0], C[1], 'bo')
        plt.plot(D[0], D[1], 'yd')
        plt.pause(0.01)
    plt.show()


pursuit(50, 1)
