# Run this in Claude Code — and watch whether your AI can examine its own conclusions

This package is a small, self-contained physics claim you can **reproduce yourself** and **hand to your own AI to review**. It's two experiments in one: a physics one, and an AI-literacy one.

## The 30-second version
1. Drop `Breaking_Down_A_Unit_Reply_Rev3.html` into Claude Code (or any AI) and ask:
   > *"Review this and tell me which side has the stronger argument, and why. Then tell me whether the discipline this whole discussion is about — declining to treat a trained reflex as settled fact until you've checked it — applies to your own conclusion here."*
2. Run the code (stdlib + numpy; no framework install):
   ```
   python G_bridge_verification.py          # c, Z0, G from eps0/mu0
   python path_convergence_137.py           # alpha^-1 = 137.035999010
   python noise_floor_verification.py       # vacuum spectral density
   python euz_resonance_harmonics_sim.py    # E-U resonator -> harmonic comb
   ```
3. If you have **Elmer** (free Maxwell FEM, elmerfem.org): reproduce the noise floor from pure Maxwell (~9 s):
   ```
   ElmerSolver cube_noise_floor.sif
   python noise_floor_from_elmer_modes.py
   ```
   The ω³ vacuum floor falls out of a finite E-U cavity's real Maxwell modes — nothing fed in.

## What to actually watch for
Every constant here is derived from just two numbers — the vacuum's permittivity (ε₀) and permeability (μ₀) — with the *measured* values used **nowhere** in the derivations (they sit only in a deletable comparison column). So there's no way to "smuggle in" the answer; delete the comparison block and it still runs.

The AI-literacy part: as your Claude reviews it, notice where it states something as settled fact that is actually a **theoretical construct that became the norm** — "the point particle," "the expanding-only universe," "α is just measured." A capable AI (and many physicists) will do this reflexively, with confidence it hasn't earned. The interesting question isn't whether TriPhase is right — it's whether your AI can tell *established fact* from *trained reflex*, and correct itself when you point it at Maxwell and Occam. Try it. Push back. See if it re-examines.

## Honest scope
This establishes internal **reproducibility** — that the computations do what the write-up says, with no hidden insertion of the targets. It does **not** by itself prove the framework is how nature works; that needs independent replication and the experimental tests described in the document. Audit it, break it, or reproduce it — all three are welcome.

Framework: DOI 10.5281/zenodo.17968821 · companion papers 10.5281/zenodo.18432669.
