"""
euz_resonance_harmonics_sim.py  --  Magnetic Innovative Solutions LLC, TriPhase.
Companion to "Breaking Down a Unit" (Rev 2).  Time-domain E-U resonator -> harmonics.

WHAT THIS DEMONSTRATES (the mechanism, honestly scoped)
    Set E (capacitance) and U (inductance) at resonance and let it run: energy sloshes
    E <-> U at omega0 = 1/sqrt(LC).  A LINEAR tank would ring at one frequency forever.
    But the U leg has a KNEE (magnetic saturation -- a real inductor's B-H curve rolls
    over), so the tank is NONLINEAR.  Driven at resonance, a nonlinear tank folds energy
    into a HARMONIC COMB -- upper harmonics at 3,5,7... x omega0.  That is the mechanism
    by which the E-U ground oscillation POPULATES the broadband bands the vacuum floor
    lives in.  "Any frequency does this" -- it is the Duffing/parametric-oscillator result,
    textbook nonlinear dynamics, not new physics.

WHAT IT DOES *NOT* CLAIM
    This is the HARMONIC-GENERATION mechanism, not the absolute spectral density.  The
    absolute level rho(omega)=A0 omega^3/2pi^2 c^3 (ratio 1.0e0 vs measured) is the separate
    math verifier (noise_floor_verification.py / floor_absolute_level_zero_knob.py).  This
    script shows HOW the harmonics get generated; that one shows the level MATCHES.  Two
    honest, separate artifacts.  No Elmer/LTspice "noise sim" is claimed -- none exists;
    the atom Elmer FEM is a different, real, full-wave run.

Model: nonlinear E-U tank (Duffing form; the cubic IS the U-leg knee):
    q'' + 2*gamma*q' + omega0^2 (q + eps*q^3) = F*cos(omega0*t)
    q = capacitor charge (E store), q' = current (U store).  Scale-free (Maxwell is
    scale-free); omega0 normalized to 1 here, maps to the atomic E-U omega0=2.4662e18 rad/s.

Run:  python euz_resonance_harmonics_sim.py     (numpy; matplotlib optional)
"""
import math
try:
    import numpy as np
except Exception as e:
    raise SystemExit(f"needs numpy: {e}")

# ---- E-U tank parameters (normalized; omega0 = 1) ------------------------------------
omega0 = 1.0        # 1/sqrt(LC); maps to atomic 2.4662e18 rad/s by scale
gamma  = 0.01       # small loss (radiative bleed to the frame)
eps    = 0.35       # U-leg knee strength (saturation nonlinearity). eps=0 -> pure sine
F      = 0.30       # drive at resonance (pumps energy in)

# ---- integrate the nonlinear tank (RK4) ----------------------------------------------
def deriv(t, y):
    q, v = y
    a = F*math.cos(omega0*t) - 2*gamma*v - omega0**2*(q + eps*q**3)
    return np.array([v, a])

dt = 2*math.pi/omega0/200      # 200 steps per fundamental period
N  = 200*400                   # 400 periods (let harmonics build up)
t  = 0.0
y  = np.array([0.0, 0.0])
ts = np.empty(N); qs = np.empty(N)
for k in range(N):
    ts[k] = t; qs[k] = y[0]
    k1 = deriv(t, y)
    k2 = deriv(t+dt/2, y+dt/2*k1)
    k3 = deriv(t+dt/2, y+dt/2*k2)
    k4 = deriv(t+dt,   y+dt*k3)
    y  = y + dt/6*(k1+2*k2+2*k3+k4)
    t += dt

# ---- energy build-up + FFT of the steady tail ----------------------------------------
half = N//2
energy_early = np.mean(qs[:half][:1000]**2)
energy_late  = np.mean(qs[half:][:1000]**2)
print("="*70)
print(" E-U resonator at resonance -> energy build-up + harmonic comb")
print("="*70)
print(f"  eps (U-leg knee) = {eps},  drive at omega0 = {omega0},  loss gamma = {gamma}")
print(f"  mean q^2 early   = {energy_early:.4e}")
print(f"  mean q^2 late    = {energy_late:.4e}   (built up {energy_late/energy_early:.1f}x)")

tail = qs[half:]                      # steady-state portion
win  = np.hanning(len(tail))
spec = np.abs(np.fft.rfft(tail*win))
freq = np.fft.rfftfreq(len(tail), d=dt) * (2*math.pi)   # angular freq
spec /= spec.max()
# report the harmonic peaks
print("\n  harmonic comb (peaks at odd multiples of omega0 = the U-knee signature):")
for n in (1, 3, 5, 7, 9):
    idx = np.argmin(np.abs(freq - n*omega0))
    # local peak in a small window
    lo, hi = max(0, idx-3), idx+4
    amp = spec[lo:hi].max()
    print(f"    {n}*omega0  amplitude = {amp:.4e}")
print("  -> odd-harmonic comb: the knee folds the fundamental up into the higher bands.")

# ---- optional chart -------------------------------------------------------------------
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(7, 6))
    a1.plot(ts[:2000], qs[:2000], lw=0.8)
    a1.set_title("E-U tank at resonance: energy building up (early transient)")
    a1.set_xlabel("t"); a1.set_ylabel("q (E-store charge)")
    m = freq < 12*omega0
    a2.semilogy(freq[m]/omega0, spec[m]+1e-6, lw=1)
    a2.set_title("Harmonic comb (steady tail): the knee radiates into the upper bands")
    a2.set_xlabel(r"$\omega/\omega_0$"); a2.set_ylabel("|FFT| (norm)")
    a2.grid(True, which="both", alpha=0.3)
    fig.tight_layout(); fig.savefig("euz_resonance_harmonics.png", dpi=130)
    print("\n  chart written: euz_resonance_harmonics.png")
except Exception as e:
    print(f"\n  [chart skipped: {e}]")

print("\n" + "="*70)
print(" Set E and U at resonance, give the U leg its knee, and it builds energy and")
print(" throws a harmonic comb -- the ground oscillation populating the broadband bands.")
print(" (Mechanism demo; absolute level is the separate rho(omega) verifier.)")
print("="*70)
