import numpy as np
from .constants import G

def pairwise_deltas(r):
    """
    Compute pairwise displacement vectors.
    
    Args:
        r: (3,2) array of positions
    
    Returns:
        d12, d13, d23: displacement vectors d_ij = r_j - r_i for i<j
    """
    d12 = r[1] - r[0]
    d13 = r[2] - r[0]
    d23 = r[2] - r[1]
    return d12, d13, d23

def accel(r):
    """
    Return accelerations (3,2) for equal masses and G=1.
    
    Args:
        r: (3,2) array of positions
    
    Returns:
        (3,2) array of accelerations
    """
    d12, d13, d23 = pairwise_deltas(r)
    r12 = np.linalg.norm(d12)
    r13 = np.linalg.norm(d13)
    r23 = np.linalg.norm(d23)

    # inverse-cube factors
    f12 = d12 / (r12**3)
    f13 = d13 / (r13**3)
    f23 = d23 / (r23**3)

    a0 =  f12 + f13        # on body 0: from 1 and 2
    a1 = -f12 + f23        # on body 1: from 0 and 2
    a2 = -f13 - f23        # on body 2: from 0 and 1
    return np.vstack([a0, a1, a2])

def energy(r, v):
    """
    Compute total energy (kinetic + potential).
    
    Args:
        r: (3,2) positions
        v: (3,2) velocities
    
    Returns:
        Total energy (scalar)
    """
    # kinetic
    K = 0.5*np.sum(v*v)
    # potential
    d12 = np.linalg.norm(r[1]-r[0])
    d13 = np.linalg.norm(r[2]-r[0])
    d23 = np.linalg.norm(r[2]-r[1])
    U = - (1.0/d12 + 1.0/d13 + 1.0/d23)
    return K + U

def angular_momentum_z(r, v):
    """
    Compute z-component of angular momentum.
    
    Args:
        r: (3,2) positions
        v: (3,2) velocities
    
    Returns:
        L_z (scalar)
    """
    # 2D: scalar Lz = sum (x*vy - y*vx)
    return float(np.sum(r[:,0]*v[:,1] - r[:,1]*v[:,0]))
