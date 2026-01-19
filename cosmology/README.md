# TriPhase Cosmology Scripts

Derivations and demonstrations of cosmological predictions from the TriPhase framework.

## Scripts

### SN2011fe_Cosmology_TriPhase.py

Interactive teaching script demonstrating Type Ia supernova cosmology with TriPhase.

**What it derives (all from vacuum properties):**
- H0 = 71.44 km/s/Mpc (from wavelength ratios)
- Omega_m = (1/6)(17/18)sqrt(3) = 0.2726 (from mode structure)
- w0 = -5/6 = -0.833 (from vacuum mode partition)

**Features:**
- Full lesson mode with step-by-step explanations
- Quick mode for calculations only
- Generates Hubble diagram comparing Lambda-CDM vs TriPhase
- All calculations visible and auditable

**Usage:**
```
python SN2011fe_Cosmology_TriPhase.py
```

Choose [1] for full lesson or [2] for quick mode.

**Requirements:**
- numpy
- matplotlib
- scipy

## Key Predictions

| Parameter | TriPhase | Lambda-CDM | Observation |
|-----------|----------|------------|-------------|
| w0 | -5/6 = -0.833 | -1.0 | -0.82 +/- 0.13 (DESI+Union3) |
| Omega_m | 0.2726 | 0.315 (fitted) | ~0.27-0.31 |
| H0 | 71.44 | 67.36 | 67-73 (tension) |

## Framework

Full documentation: [DOI 10.5281/zenodo.18295372](https://doi.org/10.5281/zenodo.18295372)

## Author

Christian R. Fuccillo | MIS Magnetic Innovative Solutions LLC | January 2026
