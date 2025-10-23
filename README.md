# Long-Term Orbital Stability Challenge

Simulate a two-body planar orbit with high eccentricity (e = 0.95) around a fixed central mass for 100 full revolutions (this is the default and ONLY target for scoring). Your goal is to minimise ALL of: energy drift, angular momentum drift, and runtime. Driving drifts extremely low by making runtime enormous is not a win; balance matters. All submissions are benchmarked on the same machine for fairness.

---

## ✅ Objectives

Implement your own numerical integration scheme in `src/stepper.py` that:
1. Produces a bound, physically consistent orbit for the full duration.
2. Achieves low relative drift in conserved quantities (energy, angular momentum).
3. Runs efficiently (avoids gratuitous oversampling).

You decide the integration scheme and a suitable strategy.

---

## 🧪 Environment Setup (from scratch)

Follow these steps after cloning the repo:

```powershell
# Clone
git clone https://github.com/shikivaahan/OrbitalTest.git
cd OrbitalTest

# Create & activate virtual environment (Windows PowerShell)
python -m venv .venv
. .venv\Scripts\Activate.ps1

# Upgrade pip (optional but recommended)
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Run harness (computes metrics and shows plots)
python run_harness.py
```

If you create additional local test scripts, do NOT commit them unless essential. Submission is a single file (see below).

---

## 🧲 Physics Model

We model a point mass (unit mass) orbiting a fixed central body with gravitational parameter mu = 1 under Newtonian gravity:

$$ \ddot{\mathbf{r}} = -\frac{\mu \mathbf{r}}{r^3}, \quad \mathbf{r} = (x,y), \; r = \|\mathbf{r}\| $$

Conserved quantities in exact (continuous) dynamics:
1. Specific Mechanical Energy: $E = \tfrac{1}{2} v^2 - \mu/r$ (constant for bound Keplerian orbit).
2. Specific Angular Momentum (z-component in 2D): $L_z = x v_y - y v_x$.

For an ellipse: semi-major axis $a$ and eccentricity $e$ relate to energy by $E = -\mu/(2a)$. With $a = 1$ and $\mu = 1$, the true energy is $E = -0.5$. The periapsis distance is $r_p = a(1-e) = 0.05$, apoapsis $r_a = a(1+e) = 1.95$. The orbital period (Kepler's third law) is $T = 2\pi a^{3/2} = 2\pi \approx 6.283185$.

Initial conditions at periapsis:
```python
r0 = [0.05, 0.0]
v0 = [0.0, (39.0)**0.5]  # sqrt(39)
mu = 1.0
```

Because the velocity magnitude changes drastically between periapsis and apoapsis, numerical schemes must remain stable under large curvature near periapsis without collapsing accuracy far away. A well-chosen, simple integrator with a sensible fixed or gently varied timestep is sufficient.

---

## 🌀 Simulation Span

Total time for scoring run: $T_{total} = 100 \times T$. Your `integrate` function runs from $t = 0$ to $t = T_{total}$.

---

## 🧩 What You Must Implement (`src/stepper.py`)

```python
def integrate(r0, v0, mu, t_final):
    """Integrate motion from t=0 to t_final.

    Args:
        r0: np.ndarray shape (2,) initial position
        v0: np.ndarray shape (2,) initial velocity
        mu: float gravitational parameter (here 1.0)
        t_final: float total simulation time

    Returns:
        times:     np.ndarray [N]
        positions: np.ndarray [N, 2]
        velocities:np.ndarray [N, 2]
    """
    raise NotImplementedError
```

Rules for implementation:
* Use only NumPy and your own code (no SciPy/ODES integrators).
* You may add helper functions (e.g. `accel(r, mu)` or a single-step function).
* Leave a brief top-of-function comment explaining WHY you chose your method.
* Keep it simple; no elaborate adaptive controllers.

---

## 🧮 Scoring Metrics

After a 100 orbit benchmark run (shorter than full 1000 for ranking):

1. Relative Energy Drift: $\Delta E = |E(t_{end}) - E(0)| / |E(0)|$
2. Relative Angular Momentum Drift: $\Delta L = |L_z(t_{end}) - L_z(0)| / |L_z(0)|$
3. Runtime (milliseconds)

Separate reporting, no combined score. Extremely small drift with huge runtime is NOT impressive; balance both.

---

## 🏎️ Performance Trade-Off

* Smaller timestep -> lower drift but higher runtime.
* Larger timestep -> faster but may inflate drift or even destabilise.
* Choose a method whose properties you can justify briefly in comments.

All submissions will be executed on the same machine/config to ensure fairness in timing comparisons.

---

## 📊 Visualisation

Running the harness automatically produces trajectory and drift plots at the end of execution:
```powershell
python run_harness.py
```
Use these plots to sanity-check periodicity and conservation quality.

---

## ⚖️ Rules Recap

* Do not change constants or initial conditions.
* Only submit your own `stepper.py` (see naming below).
* No external numerical solvers or hidden libraries.
* No adaptive orchestration hints or complex controllers.
* Simulations that produce NaN/Inf or escape (unbound trajectory) fail automatically.

---

## 📬 Submission Instructions

Deadline: 26/10/25 23:00 (UK time). Late submissions may be ignored.

Submit ONLY your modified `stepper.py` via email.

Email To: shiki.mahesh-devan22@imperial.ac.uk
Subject: Long-Term Orbit Submission - <your_name>
Attachment Filename: `<your_name>_stepper.py`

Notes:
* Do not zip or include other files.
* Ensure the file runs in a clean clone with `pip install -r requirements.txt`.
* Include the method choice comment at the top of `integrate`.



## 🧪 Testing Your Implementation (Informal)

You can locally run shorter spans (e.g. 10 orbits) by calling your integrator with a reduced `t_final`. Do not submit harness modifications. Ensure the orbit stays bound and drifts remain modest.

---

## 🔍 Verification Formulae

Energy per sample: `0.5*np.sum(v*v) - mu/np.sqrt(np.sum(r*r))`
Angular momentum z: `r[0]*v[1] - r[1]*v[0]`

Tracking these yourself during development can help tune a reasonable timestep.

---

## 🛑 Common Pitfalls

* Using explicit Euler (will usually give unacceptable drift).
* Forgetting to store the final state (off-by-one in arrays).
* Excessive Python overhead per step (avoid tiny inner Python functions in hot loops unless justified).
* Allowing timestep so large periapsis passage is poorly resolved, leading to runaway energy error.

---

## 🏁 Harness Usage

Run the scoring harness:
```powershell
python run_harness.py
```
Example output:
```json
{
  "energy_drift": 2.3e-6,
  "angular_momentum_drift": 4.1e-7,
  "runtime_ms": 845.3
}
```

---

## 🧠 Final Tips

* Start simple; get a stable orbit first.
* THEN tune timestep for balance, not extremum in a single metric.
* Keep code readable; terse micro-optimisations without comments hurt clarity.

Good luck – may your orbits be stable and your runtimes lean.

---

## 📄 License / Usage

Use this repository only for the stated challenge; do not redistribute modified harnesses publicly until after the deadline.

---

End of README.
