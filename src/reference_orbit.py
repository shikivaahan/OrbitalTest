import numpy as np

def reference_ellipse(a=1.0, e=0.99, npts=400):
    """
    Generate expected Keplerian ellipse for reference overlay.
    
    Args:
        a: semi-major axis
        e: eccentricity
        npts: number of points
    
    Returns:
        x, y: arrays of reference ellipse coordinates
    """
    theta = np.linspace(0, 2*np.pi, npts)
    r = (a * (1 - e**2)) / (1 + e * np.cos(theta))
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y
