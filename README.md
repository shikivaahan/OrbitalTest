# Planar 3-Body Integrator Challenge — Conserve Energy, Stay Periodic

**Your task:** implement a numerical integrator for the **planar Newtonian 3-body problem** and keep the system's invariants (total energy and angular momentum) nearly constant over a long run. We'll also check how close you return to the initial state after each known period of the **figure-eight choreography** (three equal masses chasing each other in an ∞).

---

## Physics (nondimensional)

For three unit masses (m=1) and G=1:

$$
\dot{\mathbf r}_i = \mathbf v_i,\qquad
\dot{\mathbf v}_i = \sum_{j\ne i} \frac{\mathbf r_j-\mathbf r_i}{\|\mathbf r_j-\mathbf r_i\|^3}.
$$

**Invariants:**
- **Total energy**
$$
E = \sum_i \tfrac12 \|\mathbf v_i\|^2 - \sum_{i<j}\frac{1}{\|\mathbf r_i-\mathbf r_j\|}.
$$
- **Angular momentum (z)**
$$
L_z = \sum_i (\mathbf r_i \times \mathbf v_i)_z.
$$

**Initial conditions (figure-eight choreography):**

```
r1 = (-0.97000436,  0.24308753); v1 = ( 0.466203685,  0.43236573)
r2 = ( 0.97000436, -0.24308753); v2 = ( 0.466203685,  0.43236573)
r3 = ( 0.0      ,   0.0      ); v3 = (-0.93240737 , -0.86473146)
```

Reference period: **T ≈ 6.3259** (nondimensional).

---

## What you implement (edit `src/stepper.py`)

- `advance(r, v, dt) -> (r_next, v_next)`  
  One step of your scheme (e.g., Velocity-Verlet/Leapfrog *or* RK4).  
- `integrate(r0, v0, dt, nsteps, sample_every=1)`  
  Repeated stepping; return final state and sampled invariant histories.

**Rules:**
- Fixed step (we give `dt`); no adaptive libraries.
- Use `numpy` and `float64`.
- Deterministic.

---

## Scoring (higher is better)

We integrate the figure-eight for many periods (e.g., 50) with a fixed `dt`. We compute:

- Max relative energy drift:  
  $$E_\text{rel}=\max_t |E(t)-E(0)|/|E(0)|$$
- Max relative angular momentum drift:  
  $$L_\text{rel}=\max_t |L_z(t)-L_z(0)|/\max(1,|L_z(0)|)$$
- Period return error at kT, k=1..N:  
  $$d_k = \frac{\sqrt{\sum_i \|r_i(kT)-r_i(0)\|^2 + \sum_i \|v_i(kT)-v_i(0)\|^2}}{\sqrt{\sum_i \|r_i(0)\|^2 + \sum_i \|v_i(0)\|^2}}$$  
  $$d_\text{max}=\max_k d_k$$

**Score:**
$$
\text{score} =
\log_{10}\!\frac{1}{E_\text{rel}+10^{-16}} +
0.5\log_{10}\!\frac{1}{L_\text{rel}+10^{-16}} +
\log_{10}\!\frac{1}{d_\text{max}+10^{-16}} -
0.05\,\log_{10}(1+\text{runtime\_ms})
$$

**Hard fails:** NaNs/Infs or a collision (min pair distance < `1e-3`) → score = −∞.

---

## How to run

```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python run_harness.py        # prints one JSON line with metrics and score
pytest                       # run public sanity tests
```

## Hints
- **Symplectic** (Leapfrog/Velocity-Verlet) often beats RK4 on invariants over long time at the same dt.
- Compute pair forces efficiently: avoid duplicate work and protect divisions by r³ with small eps on collisions (but invalid if <1e-3).
- Keep your stepper pure (don't mutate in confusing ways); return new arrays or manage reuse carefully.

Happy integrating! 🌌
