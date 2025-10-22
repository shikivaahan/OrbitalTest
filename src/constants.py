import numpy as np

MU = 1.0
A = 1.0
E = 0.99
R_P = A * (1 - E)
V_P = np.sqrt(MU * (1 + E) / (A * (1 - E)))
T_ORBIT = 2 * np.pi * np.sqrt(A**3 / MU)
T_TOTAL = 1000 * T_ORBIT
