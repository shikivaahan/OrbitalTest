import math
import numpy as np
from src.ic import figure_eight_ic
from src.physics import energy, angular_momentum_z, accel
from src.constants import T_REF
from tests.stepper_baseline import advance_rk4

def test_invariants_defined():
    """Test that invariants can be computed for initial conditions."""
    r0, v0 = figure_eight_ic()
    E0 = energy(r0, v0)
    L0 = angular_momentum_z(r0, v0)
    assert math.isfinite(E0)
    assert math.isfinite(L0)

def test_accel_symmetry():
    """Test that accelerations are computed correctly."""
    r0, v0 = figure_eight_ic()
    a = accel(r0)
    assert a.shape == r0.shape
    # Net acceleration should roughly sum to zero for equal masses near CoM
    s = np.linalg.norm(np.sum(a, axis=0))
    assert s < 1e-6

def test_baseline_short_run_finite():
    """Test that baseline RK4 produces finite results over a short run."""
    r0, v0 = figure_eight_ic()
    dt = T_REF / 800.0
    r, v = r0.copy(), v0.copy()
    for _ in range(1000):
        r, v = advance_rk4(r, v, dt)
    assert np.all(np.isfinite(r)) and np.all(np.isfinite(v))
