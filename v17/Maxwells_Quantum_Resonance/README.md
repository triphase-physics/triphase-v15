# TriPhase — α⁻¹ = 137 replication package

**Magnetic Innovative Solutions LLC · TriPhase framework · 2026-07-10**

Everything needed to independently reproduce the two central computational claims behind the "Breaking Down a Unit" discussion:

1. a **full-wave Maxwell FEM** (Elmer) showing that, from **ε₀ and μ₀ alone** at the electron's Compton scale, the **three-phase mode triplet** and the **(1,1,1) body-diagonal closure** emerge — with no α, no ħ, no 137 in the input;
2. **first-principles Python scripts** that reduce c, the impedance, G, α⁻¹, the vacuum spectral density, and mass to ε₀/μ₀ + a frame charge + integer counts, using the measured constants **only** in deletable comparison blocks.

Free tools throughout (Elmer FEM, gmsh, Python). Nothing here requires TriPhase software.

---

## Contents
| file | what it is |
|---|---|
| `cube_cavity_atomic.geo` | gmsh geometry: a cube of side a = electron Compton wavelength (2.42631×10⁻¹² m) |
| `cube_eigen_atomic.sif` | Elmer solver input: EM eigenanalysis, **real ε₀/μ₀**, PEC walls, nothing tuned |
| `RESULT_cube_eigen_ATOMIC_20260626.md` | the result record + the honest scope statement |
| `eigenfreqs_atomic.dat` | the computed eigenfrequencies |
| `G_bridge_verification.py` | c, Z₀, G from ε₀/μ₀ |
| `path_convergence_137.py` | α⁻¹ = 2⁶+2⁶+3² + Foster log-tail = 137.035999010 |
| `noise_floor_verification.py` | ρ(ω)=A₀ω³/2π²c³ vs measured vacuum density |
| `euz_resonance_harmonics_sim.py` | E–U resonator → odd-harmonic comb |

---

## A. Reproduce the Maxwell FEM (Elmer)

1. Install **Elmer FEM** (free, open source: https://www.elmerfem.org) and **gmsh** (https://gmsh.info).
2. Regenerate the mesh from the geometry (kept out of this package for size; it is ~10 MB):
   ```
   gmsh cube_cavity_atomic.geo -3 -format msh2 -o mesh.msh
   ElmerGrid 14 2 mesh.msh -autoclean       # -> mesh_atomic/ (Elmer mesh DB)
   ```
   The `.sif` expects the mesh DB in `mesh_atomic/`. (The `.geo` builds at unit size and applies `Mesh.ScalingFactor = 2.42631e-12` so the exported node coordinates are the real atomic dimension.)
3. Solve:
   ```
   ElmerSolver cube_eigen_atomic.sif
   ```
4. **Expected output** (see `eigenfreqs_atomic.dat` / the RESULT doc): after the gauge/null modes, a **3-fold degenerate triplet** {110,101,011} at ω² ≈ 3.014×10⁴¹ (the three phases, from the cube's C₃ body-diagonal symmetry), then a **2-fold (1,1,1) closure** at ω² ≈ 4.52×10⁴¹. In real frequency: triplet at **f = c/(a√2) = f_C/√2 = 8.737×10¹⁹ Hz**, closure at **f = c√3/(2a) = f_C·√3/2 = 1.070×10²⁰ Hz** — exact geometric fractions of the electron's Compton frequency. FEM vs analytic match to <0.01% / 5 figures.

**What this does and does NOT show (please read).** It shows the three-phase *structure* + the real physical *frequencies* emerge from "cube + Maxwell + PEC at λ_Compton with real ε₀/μ₀" — nothing tuned, no 137/α/ħ input. It does **not** derive the *number* 137: a lossless PEC cavity has Q=∞, and 137 is the impedance-balance count on the structure, whose unique pinning is a driven-resonance calculation (in progress), not a metric eigenvalue. Structure-uniqueness demonstrated; number-uniqueness is the stated open step.

---

## B. Reproduce the first-principles scripts (Python)

`G_bridge` and `path_convergence` are stdlib; `noise_floor` and `euz_resonance` use numpy (matplotlib optional for charts).

```
python G_bridge_verification.py          # c, Z0, G from eps0/mu0
python path_convergence_137.py           # alpha^-1 = 137.035999010
python noise_floor_verification.py       # rho(w) vs measured vacuum density
python euz_resonance_harmonics_sim.py    # E-U resonator harmonic comb
```

In every script the **measured constants (CODATA) appear only in a clearly-marked comparison block** and are used *nowhere* in the derivation — delete that block and the derivation still runs. This is the "measured-constants-removed" audit mode: the primitive-only path (ε₀, μ₀, the frame charge, integer counts) produces the values on its own.

---

## Honest scope
This package establishes **internal reproducibility** — that the computations do what the write-up says, without hidden insertion of the target values. It does **not** by itself establish that nature realizes this framework; that requires the independent replication invited here, plus the experimental tests (the frequency-signature measurement of G; the three-phase droplet experiment) described in the companion discussion. Audit it, break it, or reproduce it — all three are welcome.

**Citation:** TriPhase framework, DOI 10.5281/zenodo.17968821 · companion papers 10.5281/zenodo.18432669.
