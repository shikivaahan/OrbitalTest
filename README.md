# Long-Term Orbital Stability Challenge

You will simulate **a two-body orbit** with extremely high eccentricity (**e = 0.99**) around a fixed central mass, for **1000 full revolutions**.

Your task:
- Implement your own numerical integration scheme in `src/stepper.py`.
- Decide how to set the timestep (`dt`) as the simulation progresses.
- Produce a physically consistent orbit that remains bound for 1000 orbits.
- Your performance will be judged on:
  1. **Energy drift**
  2. **Angular momentum drift**
  3. **Runtime**

No additional numerical methods libraries (e.g., SciPy integrators) are allowed.
You may only use **NumPy** and your own code.

---

## 🌍 The Physical Model

A point mass of unit mass orbits a fixed central mass $\mu = 1$ under Newtonian gravity:

$$
\ddot{\mathbf{r}} = -\frac{\mu \mathbf{r}}{r^3}
$$

where $\mathbf{r} = (x, y)$ and $r = \|\mathbf{r}\|$.

---

## 🌀 Initial Conditions

We choose a **highly eccentric** Keplerian orbit:

- Semi-major axis $a = 1$
- Eccentricity $e = 0.99$
- Start at periapsis:
  $$
  \mathbf{r}(0) = (r_p, 0), \quad \mathbf{v}(0) = (0, v_p)
  $$
  where
  $$
  r_p = a(1 - e) = 0.01, \quad v_p = \sqrt{\frac{\mu(1 + e)}{a(1 - e)}} = \sqrt{199}
  $$

Hence:

```python
r0 = [0.01, 0.0]
v0 = [0.0, sqrt(199.0)]
```

Expected orbital period:
$$
T = 2\pi a^{3/2} = 2\pi \approx 6.283185
$$

Integrate for **1000 orbits**, total time $T_{total} = 1000 \times T \approx 6283.185$.

---

## 💻 What You Must Implement

In `src/stepper.py` implement:

```python
def integrate(r0, v0, mu, t_final):
    """
    Integrate motion from t=0 to t_final.
    You must decide:
      - what integration scheme to use
      - how to select dt throughout the simulation

    Args:
        r0: np.ndarray (2,) initial position
        v0: np.ndarray (2,) initial velocity
        mu: float (gravitational parameter)
        t_final: float (total simulation time)

    Returns:
        times: np.ndarray [N]
        positions: np.ndarray [N, 2]
        velocities: np.ndarray [N, 2]
    """
    raise NotImplementedError
```

You must not import or call any external integrators.
You may write helper functions in the same file (e.g. `accel(r, mu)`).

---

## 🧮 Scoring Metrics

After running 1000 orbits, the harness will compute:

**Relative energy drift**

$$
\Delta E = \frac{|E(t_{end}) - E(0)|}{|E(0)|}
$$

where $E = \frac{1}{2}v^2 - \mu/r$.

**Relative angular momentum drift**

$$
\Delta L = \frac{|L_z(t_{end}) - L_z(0)|}{|L_z(0)|}
$$

where $L_z = r_x v_y - r_y v_x$.

**Runtime (milliseconds)**

Each metric is reported separately — there is no combined score.
The top performers minimize all three simultaneously.

---

## 📊 Visualisation

Run:

```bash
python -m src.visualize
```

This will:

- Plot your computed trajectory for the first 2 orbits.
- Overlay a reference ellipse (expected Keplerian orbit).
- Plot energy and angular momentum drift over time.

---

## ⚠️ Rules

- Do not change provided constants or initial conditions.
- No external numerical solvers.
- No symbolic or AI-generated adaptive methods are hinted or expected — reasoning must be your own.
- Simulations that diverge (NaN/Inf or escape) automatically fail.

---

## 🏁 How to Run and Evaluate

```bash
python run_harness.py
```

You'll get output like:

```json
{
  "energy_drift": 2.3e-6,
  "angular_momentum_drift": 4.1e-7,
  "runtime_ms": 845.3
}
```

---

## 🧠 Tips

- Balance step size vs stability.
- Test shorter runs (10 orbits) first before scaling to 1000.
- Inspect your trajectory visually — correct orbits should repeat cleanly.

That's all.
