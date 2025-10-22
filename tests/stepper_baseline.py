"""
Baseline RK4 implementation with adaptive timestep.
This is hidden from students and serves as a reference for instructors.
Not meant to be optimal, just a working solution.
"""
import numpy as np
from src.physics import accel

def rk4_step(r, v, dt, mu):
    """Single RK4 step for position and velocity."""
    k1v = accel(r, mu)
    k1r = v
    
    k2v = accel(r + 0.5*dt*k1r, mu)
    k2r = v + 0.5*dt*k1v
    
    k3v = accel(r + 0.5*dt*k2r, mu)
    k3r = v + 0.5*dt*k2v
    
    k4v = accel(r + dt*k3r, mu)
    k4r = v + dt*k3v
    
    r_new = r + (dt/6.0) * (k1r + 2*k2r + 2*k3r + k4r)
    v_new = v + (dt/6.0) * (k1v + 2*k2v + 2*k3v + k4v)
    
    return r_new, v_new

def integrate_baseline(r0, v0, mu, t_final):
    """
    Baseline adaptive RK4 integrator.
    Uses smaller timesteps near periapsis, larger at apoapsis.
    """
    r = r0.copy()
    v = v0.copy()
    t = 0.0
    
    times = [t]
    positions = [r.copy()]
    velocities = [v.copy()]
    
    while t < t_final:
        # Adaptive timestep based on distance from central body
        rnorm = np.linalg.norm(r)
        # Smaller steps when closer (periapsis), larger when farther
        dt = min(0.001 * rnorm, 0.1)
        
        # Don't overshoot
        if t + dt > t_final:
            dt = t_final - t
        
        r, v = rk4_step(r, v, dt, mu)
        t += dt
        
        times.append(t)
        positions.append(r.copy())
        velocities.append(v.copy())
    
    return np.array(times), np.array(positions), np.array(velocities)
