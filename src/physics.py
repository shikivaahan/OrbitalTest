import numpy as np

def accel(r, mu=1.0):
    """Compute gravitational acceleration."""
    rnorm = np.linalg.norm(r)
    return -mu * r / (rnorm**3)

def energy(r, v, mu=1.0):
    """Specific orbital energy."""
    return 0.5 * np.dot(v, v) - mu / np.linalg.norm(r)

def angular_momentum_z(r, v):
    """Scalar z-component of angular momentum in 2D."""
    return r[0]*v[1] - r[1]*v[0]
