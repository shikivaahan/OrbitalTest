import time
import json
import math
import numpy as np
from .constants import T_REF, DT_COARSE, N_PERIODS, R_MIN_COLLISION
from .ic import figure_eight_ic
from .physics import energy, angular_momentum_z
from .stepper import integrate

def sample_indices_for_periods(dt, T_ref, n_periods):
    """
    Calculate step indices closest to k*T for k=1..n_periods.
    
    Args:
        dt: time step
        T_ref: reference period
        n_periods: number of periods
    
    Returns:
        List of step indices
    """
    idx = [int(round(k*T_ref/dt)) for k in range(1, n_periods+1)]
    return idx

def run_case(dt=DT_COARSE, n_periods=N_PERIODS, T_ref=T_REF):
    """
    Run the scoring harness for a given dt and number of periods.
    
    Args:
        dt: time step
        n_periods: number of periods to integrate
        T_ref: reference period
    
    Returns:
        Dictionary with score and metrics
    """
    r0, v0 = figure_eight_ic()

    nsteps = int(round(n_periods * T_ref / dt))
    sample_period_idx = set(sample_indices_for_periods(dt, T_ref, n_periods))

    # initial invariants
    E0 = energy(r0, v0)
    L0 = angular_momentum_z(r0, v0)
    norm0 = math.sqrt(np.sum(r0*r0) + np.sum(v0*v0))

    # integrate & measure
    t0 = time.perf_counter()
    r = r0.copy()
    v = v0.copy()
    E_rel_max = 0.0
    L_rel_max = 0.0
    dmax = 0.0

    for s in range(1, nsteps+1):
        # step once via integrate wrapper (calls student advance)
        # micro-integrate 1 step without extra allocations:
        # (reuse integrate with nsteps=1 for simplicity)
        r, v, _ = integrate(r, v, dt, 1, sample_every=1)

        # collision check
        d01 = np.linalg.norm(r[1]-r[0])
        d02 = np.linalg.norm(r[2]-r[0])
        d12 = np.linalg.norm(r[2]-r[1])
        if min(d01, d02, d12) < R_MIN_COLLISION:
            return {"score": float("-inf"), "reason": "collision", "step": s}

        # invariants
        Et = energy(r, v)
        Lt = angular_momentum_z(r, v)
        E_rel_max = max(E_rel_max, abs(Et - E0)/abs(E0))
        L_rel_max = max(L_rel_max, abs(Lt - L0)/max(1.0, abs(L0)))

        # periodic return error at k*T
        if s in sample_period_idx:
            d = math.sqrt(np.sum((r - r0)**2) + np.sum((v - v0)**2)) / norm0
            dmax = max(dmax, d)

        if not (np.all(np.isfinite(r)) and np.all(np.isfinite(v))):
            return {"score": float("-inf"), "reason": "non_finite", "step": s}

    runtime_ms = (time.perf_counter() - t0) * 1000.0

    # score
    score = (
        math.log10(1.0/(E_rel_max + 1e-16)) +
        0.5*math.log10(1.0/(L_rel_max + 1e-16)) +
        math.log10(1.0/(dmax + 1e-16)) -
        0.05*math.log10(1.0 + runtime_ms)
    )

    return {
        "score": score,
        "E_rel_max": E_rel_max,
        "L_rel_max": L_rel_max,
        "period_error_max": dmax,
        "runtime_ms": runtime_ms,
        "dt": dt,
        "nsteps": nsteps,
        "n_periods": n_periods
    }
