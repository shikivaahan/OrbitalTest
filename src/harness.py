import time
import numpy as np
from .constants import MU, R_P, V_P, T_TOTAL
from .physics import energy, angular_momentum_z
from .stepper import integrate

def run_challenge():
    r0 = np.array([R_P, 0.0], dtype=np.float64)
    v0 = np.array([0.0, V_P], dtype=np.float64)

    start = time.perf_counter()
    t, r, v = integrate(r0, v0, MU, T_TOTAL)
    runtime_ms = (time.perf_counter() - start) * 1000.0

    E0 = energy(r[0], v[0], MU)
    L0 = angular_momentum_z(r[0], v[0])
    E_end = energy(r[-1], v[-1], MU)
    L_end = angular_momentum_z(r[-1], v[-1])

    energy_drift = abs(E_end - E0) / abs(E0)
    angular_drift = abs(L_end - L0) / abs(L0)

    result = {
        "energy_drift": float(energy_drift),
        "angular_momentum_drift": float(angular_drift),
        "runtime_ms": float(runtime_ms),
        "n_points": len(t)
    }

    return result
