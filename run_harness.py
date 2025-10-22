import numpy as np
import matplotlib.pyplot as plt
from src.harness import run_challenge
from src.constants import MU, R_P, V_P, T_TOTAL, T_ORBIT
from src.physics import energy, angular_momentum_z
from src.stepper import integrate
from src.reference_orbit import reference_ellipse

if __name__ == "__main__":
    # Run the challenge and get metrics
    result = run_challenge()
    
    print("\n" + "="*50)
    print("CHALLENGE RESULTS")
    print("="*50)
    print(f"Energy Drift:              {result['energy_drift']:.6e}")
    print(f"Angular Momentum Drift:    {result['angular_momentum_drift']:.6e}")
    print(f"Runtime:                   {result['runtime_ms']:.2f} ms")
    print(f"Number of Points:          {result['n_points']}")
    print("="*50)
    
    # Generate visualization
    print("\nGenerating visualization for first 2 orbits...")
    r0 = np.array([R_P, 0.0])
    v0 = np.array([0.0, V_P])
    
    t, r, v = integrate(r0, v0, MU, 2 * T_ORBIT)
    
    E = np.array([energy(ri, vi, MU) for ri, vi in zip(r, v)])
    L = np.array([angular_momentum_z(ri, vi) for ri, vi in zip(r, v)])
    
    fig, axs = plt.subplots(1, 3, figsize=(15, 4))
    
    # Trajectory
    axs[0].plot(r[:,0], r[:,1], lw=1, label='Computed')
    x_ref, y_ref = reference_ellipse()
    axs[0].plot(x_ref, y_ref, 'k--', alpha=0.5, label='Reference')
    axs[0].set_aspect('equal')
    axs[0].set_title("Trajectory (2 orbits)")
    axs[0].set_xlabel("x")
    axs[0].set_ylabel("y")
    axs[0].legend()
    axs[0].grid(True, alpha=0.3)
    
    # Energy drift
    axs[1].plot(t, E - E[0])
    axs[1].set_title("Energy Drift")
    axs[1].set_xlabel("Time")
    axs[1].set_ylabel("ΔE")
    axs[1].grid(True, alpha=0.3)
    
    # Angular momentum drift
    axs[2].plot(t, L - L[0])
    axs[2].set_title("Angular Momentum Drift")
    axs[2].set_xlabel("Time")
    axs[2].set_ylabel("ΔL")
    axs[2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
