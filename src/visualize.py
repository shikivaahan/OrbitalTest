import numpy as np
import matplotlib.pyplot as plt
from .constants import MU, R_P, V_P, T_TOTAL, T_ORBIT
from .physics import energy, angular_momentum_z
from .stepper import integrate

def reference_ellipse(a=1.0, e=0.99, npts=400):
    theta = np.linspace(0, 2*np.pi, npts)
    r = (a * (1 - e**2)) / (1 + e * np.cos(theta))
    return r * np.cos(theta), r * np.sin(theta)

def main():
    r0 = np.array([R_P, 0.0])
    v0 = np.array([0.0, V_P])

    # simulate for 2 orbits for clarity
    _, r, v = integrate(r0, v0, MU, 2 * T_ORBIT)

    E = [energy(ri, vi, MU) for ri, vi in zip(r, v)]
    L = [angular_momentum_z(ri, vi) for ri, vi in zip(r, v)]

    fig, axs = plt.subplots(1, 3, figsize=(15, 4))
    # trajectory
    axs[0].plot(r[:,0], r[:,1], lw=1)
    x_ref, y_ref = reference_ellipse()
    axs[0].plot(x_ref, y_ref, 'k--', alpha=0.5)
    axs[0].set_aspect('equal'); axs[0].set_title("Trajectory")

    axs[1].plot(E - np.mean(E))
    axs[1].set_title("Energy Drift")

    axs[2].plot(L - np.mean(L))
    axs[2].set_title("Angular Momentum Drift")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
