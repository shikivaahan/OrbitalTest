from src.constants import R_P, V_P, MU, T_ORBIT
from src.physics import accel, energy
import numpy as np

def test_accel_direction():
    r = np.array([1.0, 0.0])
    a = accel(r, MU)
    assert np.allclose(a, [-MU, 0.0])

def test_energy_finite():
    r = np.array([R_P, 0.0])
    v = np.array([0.0, V_P])
    E = energy(r, v, MU)
    assert np.isfinite(E)

def test_period_magnitude():
    assert T_ORBIT > 6.0 and T_ORBIT < 6.4
