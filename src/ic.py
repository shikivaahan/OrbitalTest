import numpy as np

def figure_eight_ic():
    """Return initial conditions for the figure-eight choreography."""
    r = np.array([
        [-0.97000436,  0.24308753],
        [ 0.97000436, -0.24308753],
        [ 0.0       ,  0.0       ]], dtype=np.float64)
    v = np.array([
        [ 0.466203685,  0.43236573],
        [ 0.466203685,  0.43236573],
        [-0.93240737 , -0.86473146]], dtype=np.float64)
    return r, v
