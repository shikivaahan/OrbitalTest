import numpy as np
import matplotlib.pyplot as plt
from .constants import T_REF
from .ic import figure_eight_ic
from .stepper import integrate
from .physics import energy, angular_momentum_z

def simulate_for_plot(dt, n_periods):
    """
    Simulate the system and collect trajectory and invariant data.
    
    Args:
        dt: time step
        n_periods: number of periods to simulate
    
    Returns:
        traj: (nsteps+1, 3, 2) array of trajectories
        E: (nsteps+1,) energy history
        L: (nsteps+1,) angular momentum history
    """
    r0, v0 = figure_eight_ic()
    nsteps = int(round(n_periods*T_REF/dt))
    traj = np.empty((nsteps+1, 3, 2))
    E = np.empty(nsteps+1)
    L = np.empty(nsteps+1)
    r, v = r0.copy(), v0.copy()
    traj[0] = r
    E[0] = energy(r, v)
    L[0] = angular_momentum_z(r, v)
    for k in range(1, nsteps+1):
        r, v, _ = integrate(r, v, dt, 1, sample_every=1)
        traj[k] = r
        E[k] = energy(r, v)
        L[k] = angular_momentum_z(r, v)
    return traj, E, L

def plot(traj, E, L, out="figure_eight.png"):
    """
    Create visualization of trajectories and invariant drift.
    
    Args:
        traj: (nsteps+1, 3, 2) trajectories
        E: energy history
        L: angular momentum history
        out: output filename
    """
    fig, axs = plt.subplots(1, 3, figsize=(12, 4))
    # trajectories
    for i in range(3):
        axs[0].plot(traj[:, i, 0], traj[:, i, 1], lw=0.8)
    axs[0].set_title("Trajectories")
    axs[0].set_aspect("equal")
    # energy
    axs[1].plot(E - E[0])
    axs[1].set_title("E(t) - E(0)")
    # angular momentum
    axs[2].plot(L - L[0])
    axs[2].set_title("Lz(t) - Lz(0)")
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    print(f"Saved {out}")
