import numpy as np
from .physics import accel

def integrate(r0, v0, mu, t_final):
    """
    Implement your integration scheme and timestep logic.
    You must decide how to choose dt and how to advance (r,v).
    
    Args:
        r0: np.ndarray (2,) initial position
        v0: np.ndarray (2,) initial velocity
        mu: float (gravitational parameter)
        t_final: float (total simulation time)

    Returns:
        times: np.ndarray [N]
        positions: np.ndarray [N, 2]
        velocities: np.ndarray [N, 2]
    """
    raise NotImplementedError("Implement your own integrator here.")
