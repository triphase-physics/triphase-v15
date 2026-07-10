"""
noise_floor_from_elmer_modes.py -- MIS/TriPhase.
Post-process the Elmer eigen run (cube_noise_floor.sif -> eigenfreqs_noise.dat):
the ω³ vacuum floor SHAPE falls out of the finite E-U cavity's real Maxwell modes.
FEM gives the mode density (Weyl, dN/df~f^2 -> N~f^3); x (1/2 hbar f) per mode -> rho~f^3.
No 137, no alpha, no fit -- only a box + real eps0/mu0 + Maxwell (Elmer).
"""
import math, bisect
vals=[]
for line in open("eigenfreqs_noise.dat"):
    for t in line.split():
        try: vals.append(float(t))
        except: pass
freqs=sorted(f for f in vals if f>1e19)   # drop gauge/null cluster (<1e16 + negatives)
hbar=1.054571817e-34; a=2.42631e-12; Vol=a**3
print(f"{len(vals)} raw eigenvalues -> {len(freqs)} real EM modes; "
      f"triplet={freqs[0]:.4e} Hz, closure={freqs[3]:.4e} Hz, top={freqs[-1]:.4e} Hz")
print(f"{'f (Hz)':>13}{'N(<f)':>7}{'N/f^3':>13}{'rho(f)':>13}{'rho/f^3':>13}")
fmin,fmax=freqs[5],freqs[-3]
for fr in (0.3,0.5,0.7,0.9):
    f=fmin+fr*(fmax-fmin); N=bisect.bisect_right(freqs,f); df=0.10*(fmax-fmin)
    dNdf=(bisect.bisect_right(freqs,f+df)-bisect.bisect_right(freqs,f-df))/(2*df)
    rho=dNdf*(0.5*hbar*f)/Vol
    print(f"{f:13.4e}{N:7d}{N/f**3:13.4e}{rho:13.4e}{rho/f**3:13.4e}")
print("N/f^3 and rho/f^3 ~constant => N~f^3 (Weyl), rho~f^3 (the omega^3 vacuum floor).")
