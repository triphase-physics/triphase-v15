# v17 — Maxwell's Quantum Resonance

This is the current-generation section of the framework. The name states the
claim plainly: the vacuum is a two-store electromagnetic resonator — an
electric store E₀ (permittivity ε₀) and a magnetic store U₀ (permeability μ₀),
coupled through the frame impedance Z₀ = √(μ₀/ε₀). Every fundamental constant
is derived from those two measured properties of free space; the measured
values of the constants themselves are used **nowhere** in the mathematics.

The giants each described one vector frame from a different angle. Maxwell
found where Newton's mechanism lives.

This section will fill out over time. The first artifact is the replication
package that accompanies the "Breaking Down a Unit" reply.

## Contents

- **`Maxwells_Quantum_Resonance/`** — self-contained replication package:
  - Four runnable scripts (stdlib + numpy/sympy): c, Z₀, G, α⁻¹ = 137.035999010,
    and the vacuum noise floor — all from ε₀ and μ₀ alone.
  - A Maxwell FEM simulation (Elmer, free): a finite ε₀/μ₀ cavity whose real
    Maxwell modes reproduce the ω³ vacuum-noise floor in seconds, with nothing
    fed in. The FEM *is* a Maxwell solver — to reject the result is to reject Maxwell.
  - `README.md` and `CLAUDE_CODE_QUICKSTART.md` — how to run it, and how to hand
    it to your own AI to review.

## Scope

The package establishes **reproducibility** — the computations do what the
write-up says, with no hidden insertion of the targets (delete the comparison
column and it still runs). It does not by itself prove the framework is how
nature works; that needs independent replication and the experiments described
in the reply.

Framework DOI: 10.5281/zenodo.17855383 · companion papers: 10.5281/zenodo.18432669
