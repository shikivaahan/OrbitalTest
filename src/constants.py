import numpy as np

# nondimensional units: G = 1, m_i = 1
G = 1.0
M = np.array([1.0, 1.0, 1.0])
T_REF = 6.3259  # reference period for figure-eight

# default horizons and steps
N_PERIODS = 50
DT_COARSE = T_REF / 400.0  # ~0.0158
DT_FINE   = T_REF / 800.0  # ~0.0079

# safety
R_MIN_COLLISION = 1e-3
