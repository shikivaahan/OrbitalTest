import numpy as np
from src.physics import accel

def advance_rk4(r, v, dt):
    """
    Baseline RK4 integrator for testing purposes.
    
    This is a reference implementation used ONLY by tests.
    Students should not use or copy this directly.
    
    Args:
        r: (3,2) positions
        v: (3,2) velocities
        dt: time step
    
    Returns:
        r_next, v_next: updated state
    """
    def a(rr):
        return accel(rr)

    k1_r = v
    k1_v = a(r)

    k2_r = v + 0.5*dt*k1_v
    k2_v = a(r + 0.5*dt*k1_r)

    k3_r = v + 0.5*dt*k2_v
    k3_v = a(r + 0.5*dt*k2_r)

    k4_r = v + dt*k3_v
    k4_v = a(r + dt*k3_r)

    r_next = r + (dt/6.0)*(k1_r + 2*k2_r + 2*k3_r + k4_r)
    v_next = v + (dt/6.0)*(k1_v + 2*k2_v + 2*k3_v + k4_v)
    return r_next, v_next
