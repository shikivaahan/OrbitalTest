import numpy as np
from .constants import A, E

def reference_ellipse(a=None, e=None, npts=400):
    """
    Generate expected Keplerian ellipse for reference overlay.
    Uses values from constants.py by default.
    
    The orbit starts at periapsis (theta=0) on the positive x-axis,
    with the central mass at the origin (one focus of the ellipse).
    
    Args:
        a: semi-major axis (defaults to constants.A)
        e: eccentricity (defaults to constants.E)
        npts: number of points
    
    Returns:
        x, y: arrays of reference ellipse coordinates
    """
    if a is None:
        a = A
    if e is None:
        e = E
    
    # Polar equation of ellipse: r(θ) = a(1-e²)/(1 + e·cos(θ))
    # θ=0 corresponds to periapsis (closest point)
    theta = np.linspace(0, 2*np.pi, npts)
    r = (a * (1 - e**2)) / (1 + e * np.cos(theta))
    
    # Convert to Cartesian coordinates
    # Focus (central mass) is at origin
    # Periapsis is at (r_p, 0) where r_p = a(1-e)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    return x, y
