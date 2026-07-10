# Elmer noise-floor result -- the omega^3 vacuum floor from a finite E-U cavity's modes
**2026-07-10.** Run: `cube_noise_floor.sif` (250 eigenmodes) -> `eigenfreqs_noise.dat`;
post-process `noise_floor_from_elmer_modes.py`. Same box + real eps0/mu0 as the atom run.

## What it shows
182 real EM eigenmodes (gauge/null removed): triplet at 8.737e19 Hz, (1,1,1) closure at
1.070e20 Hz, then a ladder to 3.52e20 Hz. Counting them:
- **N(<f) ~ f^3** (Weyl mode count) and **rho(f)=dN/df * (1/2 hbar f)/Vol ~ f^3** (the floor),
  both N/f^3 and rho/f^3 ~constant across the band.
So the **omega^3 vacuum-noise floor is the mode density of the frame's own Maxwell resonances**,
from nothing but a finite box + real eps0/mu0. No 137, no alpha, no fitted constant.

## Honest scope
The FEM (pure Maxwell) supplies the **mode density / omega^3 shape** from real modes -- it
confirms the Weyl count non-circularly. The per-mode **1/2 hbar omega** is the zero-point
energy per mode; the absolute floor level is the frame's own action amplitude A0=q_frame^2*Z0
(companion `noise_floor_verification.py`). This run establishes the SHAPE from Maxwell; the
LEVEL is the frame amplitude. Finite-mode sample (~factor 3 in f), so the ~f^3 constancy is
approximate, not a tight fit -- reproduce with more modes for a cleaner slope.

## Reproduce
Install Elmer (free). `ElmerSolver cube_noise_floor.sif` (~9 s), then
`python noise_floor_from_elmer_modes.py`. Anyone can run it.

## Provenance of the cavity size
The box side a = the electron's Compton wavelength is a **framework derivative**, lambda_C = 2*pi*lam0/[315*(1-12/137^2+1/137^3)] (base E-U resonance wavelength / the electron's mode-count) -- NO electron mass, not a CODATA value. And the omega^3 floor is scale-free (Maxwell scale-invariance), so the shape needs no length at all; the size only fixes where the specific modes land.
