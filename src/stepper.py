from __future__ import annotations
import numpy as np

def integrate(r0: np.ndarray, v0: np.ndarray, mu: float, t_final: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Integrate planar two-body motion from t=0 to t_final.

    You must implement the numerical scheme (e.g., your chosen integrator) and
    return time-aligned arrays of states. The central mass is fixed at the origin.

    Parameters
    ----------
    r0 : np.ndarray
        Initial position vector shape (2,) in Cartesian coordinates (x, y).
        Must be finite and non-zero length (cannot start at the singularity r=0).
    v0 : np.ndarray
        Initial velocity vector shape (2,) (vx, vy). Must contain finite floats.
    mu : float
        Gravitational parameter (GM). For this challenge it is fixed to 1.0.
    t_final : float
        Final simulation time (> 0). The solver should advance from t=0 up to
        exactly t_final (inclusive or very close within floating-point tolerance).

    Returns
    -------
    times : np.ndarray
        1D array shape (N,) strictly increasing, with times[0] == 0.0 and
        times[-1] approximately t_final. N depends on your chosen step strategy.
    positions : np.ndarray
        2D array shape (N, 2). positions[i] gives (x, y) at times[i]. Must not
        contain NaN or Inf; orbit should remain bound for all samples.
    velocities : np.ndarray
        2D array shape (N, 2). velocities[i] gives (vx, vy) at times[i]. Same
        finiteness constraints as positions.

    Expected Invariants (for physical correctness, not enforced here)
    --------------------
    - Energy drift |E(t_end) - E(0)| / |E(0)| should remain small.
    - Angular momentum about origin should be nearly constant.

    Notes
    -----
    Students: replace this placeholder with your integrator and remove any
    unused imports. Ensure returned arrays are NumPy ndarrays, not lists.
    """
    raise NotImplementedError("Students: implement your integrator returning (times, positions, velocities)")
