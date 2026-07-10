# TriPhase Physics Framework
## Maxwell's Quantum Resonance

**The fundamental constants derived from the two measured properties of free space (ε₀, μ₀), by mechanism — not fitted.**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17855383.svg)](https://doi.org/10.5281/zenodo.17855383)

Framework (V16): [10.5281/zenodo.17855383](https://doi.org/10.5281/zenodo.17855383) · Companion papers: [10.5281/zenodo.18432669](https://doi.org/10.5281/zenodo.18432669)

> **Versions.** Wave mechanics runs through every version; the name *Maxwell's Quantum Resonance* and the Elmer FEM are what's new in **V17** (this package) — not the method, and not present in V16. The **V16** framework record — the current release — is on Zenodo (DOI 10.5281/zenodo.17855383). Older **V15** material is retired to [`v15/`](v15) and preserved at git tag `v15-legacy`.

---

## The claim, in one sentence

There are no fundamental point particles. The **vector frame** (what physics calls the vacuum) is a resonant electromagnetic system governed by Maxwell's equations, and the stable three-phase wave closures it forms are what we call electrons, protons, neutrons. From the frame's two measured properties — **ε₀** (electric store, "E") and **μ₀** (magnetic store, "U") — the framework *derives* the constants that conventional physics measures and inserts. The measured values are used **nowhere** in the mathematics; they appear only in deletable comparison blocks.

This is wave mechanics — the same wave mechanics quantum mechanics already is — carried to the vacuum's own two properties.

---

## What it derives (mechanism, not fit)

| Quantity | Derived | CODATA (comparison only) | How |
|---|---|---|---|
| α⁻¹ (fine structure) | 137.035999010 | 137.035999177 | 2⁶+2⁶+3² + Foster log-tail |
| G (Newton's constant) | 6.67430×10⁻¹¹ | 6.67430×10⁻¹¹ | (15/2)·ε₀·β²,  β² = 1 + (5/6)²/137 |
| vacuum spectral density | A₀ω³/2π²c³ | measured floor | A₀ = q_frame²·Z₀ (= ħ), no 137 |

α⁻¹ is **not** the circular identity 2π·a₀/λ_C — that is a *definition* of the Bohr radius, not a derivation. It is the **up-up-down charge-pump saturation of the proton's three-phase wye**: 2⁶+2⁶+3² = 137, with the decimals the LC tank's logarithmic tail (Foster / Kramers-Kronig). 136 and 138 cannot arise — they are not reachable saturations of a three-phase wye.

G is the worst-measured constant (labs scatter ~0.05%), so five-figure agreement sits at the edge of what measurement can resolve.

---

## What's in this repository

- **[`v17/`](v17)** — *current.* The Maxwell's Quantum Resonance replication package — the four runnable scripts and the Elmer Maxwell FEM, linked from the "Breaking Down a Unit" reply.
- **[`v16/`](v16)** — the framework record, published on **Zenodo** (DOI 10.5281/zenodo.17855383); pointer here.
- **[`v15/`](v15)** — retired earlier material, kept for history (also at tag `v15-legacy`).

---

## Run it (free tools only)

The current package is in [`v17/Maxwells_Quantum_Resonance/`](v17/Maxwells_Quantum_Resonance):

```bash
cd v17/Maxwells_Quantum_Resonance
python G_bridge_verification.py        # c, Z0, G, beta  from eps0/mu0 only
python path_convergence_137.py         # alpha^-1 = 2^6+2^6+3^2 + Foster tail = 137.035999010
python noise_floor_verification.py     # rho(w) = A0 w^3 / 2pi^2 c^3  vs measured vacuum density
python euz_resonance_harmonics_sim.py  # E-U resonator -> harmonic comb
```

Requirements: Python 3.8+, sympy, numpy (matplotlib optional). In every script the measured constants (CODATA) appear **only** in a clearly-marked comparison block and are used *nowhere* in the derivation — delete the block and the derivation still runs.

There is also a full-wave **Maxwell FEM** (Elmer, free): a finite ε₀/μ₀ cavity at the electron's Compton scale whose real Maxwell modes return the three-phase mode triplet and the (1,1,1) body-diagonal closure — with no α, no ħ, no 137 fed in. See [`RESULT_cube_eigen_ATOMIC_20260626.md`](v17/Maxwells_Quantum_Resonance/RESULT_cube_eigen_ATOMIC_20260626.md).

---

## Honest scope

This package establishes **reproducibility** — the computations do what the write-up says, with no hidden insertion of the target values. It does **not** by itself prove the framework is how nature works; that requires independent replication and the experiments described in the companion reply (a frequency-signature measurement of G; the wave-piloted-droplet experiment).

On the multi-discipline agreement: the same integer 137 is also independently expressible as a figurate identity (T₁₇ − 2⁴ = 153 − 16) and a Lie-algebra / Eisenstein identity (12² − 7 = 144 − 7). Those are **corroboration** — internal robustness, other disciplines landing on the same value — **not** the derivation, and not independent external proof. The derivation is the wave-mechanics mechanism; the pure-math identities only land on the number. `path_convergence_137.py` states this limit in its own output.

Cosmology results (redshift as impedance-path drag ln(1+z), MOND's acceleration scale, galaxy rotation without dark matter) are the framework's broader program — tested in the companion papers, not headlined here.

Audit it, reproduce it, or break it — all three are welcome.

---

## Changelog

An honest record of edits to any script or simulation file in this repository.

- **2026-07-10**
  - `v17/…/G_bridge_verification.py` — α log-tail corrected from 2 to 3 terms → 137.035999010, matching `path_convergence_137.py`.
  - Root README rewritten to lead with the mechanism (replacing the earlier promotional page; the circular 2π·a₀/λ_C identity is no longer presented as a derivation).
  - Repository renamed `triphase-v15` → `triphase`; V15 material moved to `v15/` and tagged `v15-legacy`.

---

## Who / where

Christian R. Fuccillo — Magnetic Innovative Solutions LLC. Medical-imaging engineer (CT / MRI), 12+ years on magnetic power systems, working independently in New Hampshire. TriPhase began October 2025.

## How to verify

1. **Run the scripts.** They use only ε₀ and μ₀ (plus integer counts) in the math.
2. **Check the math.** Every derivation shows its work.
3. **Find an error.** Please — that is the point.

## Citation

```bibtex
@misc{fuccillo2026triphase,
  author    = {Fuccillo, Christian R.},
  title     = {TriPhase Physics Framework: Maxwell's Quantum Resonance},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.17855383}
}
```

## License

MIT — use it, test it, break it, improve it.

---

*"I fall down a lot… but I keep getting back up." — Christian R. Fuccillo*
