import numpy as np
from .physics import accel

def advance(r, v, dt):
    """
    One integrator step. Return (r_next, v_next).

    Implement one of:
      - Velocity-Verlet / Leapfrog (symplectic), or
      - classic RK4.
    Document your choice briefly.
    
    Args:
        r: (3,2) current positions
        v: (3,2) current velocities
        dt: time step
    
    Returns:
        r_next, v_next: updated positions and velocities
    """
    # --- TEMPLATE: raise until implemented
    raise NotImplementedError("Implement your integrator step here.")

def integrate(r0, v0, dt, nsteps, sample_every=1):
    """
    Repeated stepping with optional sampling.
    
    Args:
        r0: (3,2) initial positions
        v0: (3,2) initial velocities
        dt: time step
        nsteps: number of steps to take
        sample_every: sample invariants every N steps
    
    Returns:
        rT, vT: final state (positions, velocities)
        (E_hist, L_hist): sampled invariant histories (placeholders for harness)
    """
    r = np.array(r0, dtype=np.float64)
    v = np.array(v0, dtype=np.float64)
    E_hist = []
    L_hist = []
    for k in range(nsteps):
        r, v = advance(r, v, dt)
        if (k+1) % sample_every == 0:
            E_hist.append(np.nan)  # placeholder; harness computes exact values
            L_hist.append(np.nan)
    return r, v, (np.array(E_hist), np.array(L_hist))
