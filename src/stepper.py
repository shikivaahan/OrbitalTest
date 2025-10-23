from __future__ import annotations
import numpy as np

def integrate(r0: np.ndarray, v0: np.ndarray, mu: float, t_final: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Placeholder integrator.

    Students must implement their own integration method here and return:
    times, positions, velocities.

    Args:
        r0: (2,) initial position
        v0: (2,) initial velocity
        mu: gravitational parameter
        t_final: total simulation time
    """
    raise NotImplementedError("Students: implement your integrator returning (times, positions, velocities)")
