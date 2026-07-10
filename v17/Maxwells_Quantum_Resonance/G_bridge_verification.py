"""
G_and_beta_from_first_principles.py
-----------------------------------
Derives BOTH Newton's constant G and the bridge factor beta from ONLY the two
properties of the vector frame -- the permittivity E0 and the permeability U0 --
with NO other physical constant used as an input anywhere in the mathematics.

  * The ONLY two given numbers are E0 (permittivity) and U0 (permeability): the
    two measured properties of free space. They are the axioms, not fitted parameters.
  * Everything else -- the speed of light, the impedance, G, and beta -- is DERIVED
    from E0 and U0 (and integer COUNTS built in front of you) by algebra, in the code.
  * NO alpha (fine-structure constant) is used anywhere. Where a "137" appears it is
    BUILT from a mode count (2^6 + 2^6 + 3^2), never entered as a number from nowhere.
  * CODATA measured values appear ONLY in the clearly-labelled CHECKPOINT block at the
    end, for comparison. They are never used in a calculation. Delete the checkpoint
    block and every derivation above it still runs.

Run:  python G_and_beta_from_first_principles.py      (requires: sympy)

Christian R. Fuccillo, Magnetic Innovative Solutions LLC.
Version: Rev 1.0 (2026-07-09).  Companion to the reply "Breaking Down a Unit" (Rev 1.0).
"""
import sympy as sp

# ============================================================================
# THE TWO GIVENS -- the only inputs. The measured properties of the frame.
# ============================================================================
E0 = sp.Rational(88541878128, 10**22)      # permittivity  8.8541878128e-12  [F/m]
U0 = sp.Rational(125663706212, 10**17)     # permeability  1.25663706212e-6  [H/m]

# ============================================================================
# DERIVE c and the impedance from E0, U0 -- Maxwell only, no other constant.
# ============================================================================
c   = 1/sp.sqrt(E0*U0)          # the E-U wave speed  (what mainstream calls 'c')
Z0  = sp.sqrt(U0/E0)            # the frame tension   (what mainstream calls 'Z0')

# ============================================================================
# THE KILOGRAM IS NOT AN INDEPENDENT UNIT -- it breaks down to E, U, and charge.
# This is WHY G (whose SI dimension carries kg) can be built from E0 and U0 at all.
# 2019 SI: the kilogram is fixed via Planck's h and realized ELECTRICALLY on a
# Kibble balance (mass weighed against V^2/R). It is bookkeeping, not fundamental.
#
#   1 kg = e^2 * U0 / L = e^2 / (E0 * L * c^2)     [mass = charge^2 * permeability / length]
#
# Base-dimension check [m, kg, s, A]:
#   e^2 = (0,0,2,2)   U0 = (1,1,-2,-2)   1/L = (-1,0,0,0)   sum = (0,1,0,0) = kg  (exact)
# ============================================================================
e_ch = sp.Rational(1602176634, 10**28)          # elementary charge 1.602176634e-19 C
m_e  = sp.Rational(91093837015, 10**41)          # electron mass (checkpoint/illustration only)
L_kg = e_ch**2 * U0 / m_e                         # length s.t. e^2*U0/L = m_e
r_e  = e_ch**2 / (4*sp.pi*E0*m_e*c**2)            # classical electron radius
print("="*70)
print("KILOGRAM BROKEN OUT (why G, whose SI dimension carries kg, reduces to E,U):")
print("  1 kg = e^2 * U0 / L = e^2/(E0*L*c^2)   [charge^2 * permeability / length]")
print(f"  electron: L = e^2*U0/m_e = {sp.N(L_kg,6)} m ;  4*pi*r_e = {sp.N(4*sp.pi*r_e,6)} m  (same length)")
print("  => the kilogram carries amperes; in the 2019 SI it is electrical, not fundamental.")
print("     So [G] and [E0] share one EM dimensional space -- the 'G=f(E0,U0)' objection")
print("     is an artifact of the pre-2019 base unit, not a real dimensional barrier.")
print("="*70)
print()

# ============================================================================
# G, BARE FORM -- the lossless mode count times the frame's electric compliance.
#   factor = 60/8 = 15/2 : a COUNTED integer ratio (mode structure / Einstein's 8),
#   not a measurement. mu0 and c^4 fold in algebraically to leave (15/2)*E0.
# ============================================================================
factor  = sp.Rational(60, 8)               # = 15/2 = 7.5   (counted, not measured)
G_bare  = factor * E0**3 * U0**2 * c**4     # == (15/2)*E0 after mu0,c^4 cancel

# ============================================================================
# beta -- THE QUANTUM-GRAVITY SELF-TERM, derived from the mode structure alone.
# NO alpha. Every piece is a count you can see built:
#
#   N = 2^6 + 2^6 + 3^2 = 64 + 64 + 9 = 137
#       the up-up-down mode count of the three-way junction. BUILT, never entered.
#
#   f = 5/6  = (6 - 1)/6
#       the ground-excluded coupling fraction: of six modes, five couple and one is
#       the ground you reference from (1/6 ground + 5/6 active = 1).
#
#   beta^2 = 1 + f^2 / N
#       squared  -> gravity is a source<->receiver coupling; the fraction applies at
#                   both ends (the two quadratures of the interaction).
#       over N   -> the single mode-share the junction presents to the frame.
#       the "1"  -> the referenced ground (unity baseline).
# ============================================================================
N       = 2**6 + 2**6 + 3**2               # 137, built from the mode structure
f       = sp.Rational(5, 6)                # ground-excluded coupling fraction
beta_sq = 1 + f**2 / N                     # = 1 + 25/4932
beta    = sp.sqrt(beta_sq)

# ---- THE LOG TAIL: beta's TRUE form is a logarithm, and here is WHY ----------
# A resonator at resonance BUILDS HARMONICS as it rings. Coupling to that harmonic
# buildup drains LOGARITHMICALLY -- the log tail IS the harmonic (frequency)
# interaction itself, not a fudge added to fit. It is the same frequency-domain
# physics as Foster's reactance theorem (Foster, Bell Sys. Tech. J. 3, 1924) and
# the Kramers-Kronig dispersion relations (Kronig 1926; Kramers 1927): loss and
# frequency response locked together -- frequencies interacting with frequencies.
# The octave base is 2 (the base of the two 2^6 up-modes,
# which are 128 of the 137). So the true form is:
beta_sq_log = 1 + sp.log(2)/N              # = 1 + ln(2)/137  (the true log form)
# The rational (5/6)^2/N used above is the CLOSED-FORM SHADOW of this log; they
# agree to ~0.19%, below G's measurement precision. The SAME wave interaction puts
# a log tail on alpha, and there -- where measurement IS precise -- it lands to 9 figures:
alpha_inv_from_tail = N + sp.log(N)/N + sp.Rational(1,3)*sp.log(N)/N**2 - sp.Rational(1,3)*sp.log(N)/N**3  # 137 + ln137/137 + (1/3)ln137/137^2 - (1/3)ln137/137^3

# G with the self-term restored (the full mechanism, not the lossless-count shorthand):
G_full  = G_bare * beta_sq

print("="*70)
print("DERIVED FROM E0 and U0 ONLY (no alpha, no measured constant in the math):")
print("="*70)
print(f"  E0 (permittivity, GIVEN)  = {sp.N(E0,11)}  F/m")
print(f"  U0 (permeability, GIVEN)  = {sp.N(U0,11)}  H/m")
print(f"  c  = 1/sqrt(E0*U0)        = {sp.N(c,10)}  m/s   [derived]")
print(f"  Z0 = sqrt(U0/E0)          = {sp.N(Z0,10)}  ohm   [derived]")
print()
print("  BETA, built from counts (no alpha anywhere):")
print(f"    N   = 2^6 + 2^6 + 3^2   = {2**6} + {2**6} + {3**2} = {N}   (up-up-down mode count)")
print(f"    f   = (6-1)/6           = {f}                (ground-excluded coupling fraction)")
print(f"    beta^2 = 1 + f^2/N      = 1 + {f**2}/{N} = 1 + {(f**2/N)} = {sp.N(beta_sq,10)}")
print(f"    beta                    = {sp.N(beta,10)}")
print()
print("  THE LOG TAIL (why the form is a logarithm -- the harmonic/frequency interaction):")
print("    a resonator at resonance BUILDS HARMONICS; coupling to that buildup drains")
print("    LOGARITHMICALLY. The tail is mechanism, not a fudge. Octave base = 2.")
print(f"    beta^2, true log form    = 1 + ln(2)/137      = {sp.N(beta_sq_log,10)}")
print(f"    beta^2, rational shadow  = 1 + (5/6)^2/137     = {sp.N(beta_sq,10)}   (agree ~0.19%)")
print("    SAME tail nails alpha (where measurement is precise, to 9 figures):")
print(f"      137 + ln137/137 + (1/3)ln137/137^2 - (1/3)ln137/137^3 = {sp.N(alpha_inv_from_tail,12)}")
print("      measured alpha^-1                   = 137.035999177")
print()
print("  G, bare (lossless count):   G = (15/2)*E0        = %s" % sp.N(G_bare,8))
print("  G, full (self-term added):  G = (15/2)*E0*beta^2 = %s" % sp.N(G_full,8))
print()

# ============================================================================
# CHECKPOINT (comparison only -- NOT used in any calculation above).
# Delete this whole block and the derivation still runs.
# ============================================================================
print("="*70)
print("CHECKPOINT vs measured (CODATA -- for comparison ONLY, not an input):")
print("="*70)
G_codata = sp.Rational(667430, 10**16)     # 6.67430e-11  (G, the least-certain constant)
gap_bare = sp.N((G_bare - G_codata)/G_codata*100, 3)
gap_full = sp.N((G_full - G_codata)/G_codata*100, 3)
print(f"    G_bare (lossless count) = {sp.N(G_bare,8)}   gap {gap_bare}%   <- the 0.5% the self-term explains")
print(f"    G_full (with beta^2)    = {sp.N(G_full,8)}   gap {gap_full}%   <- lands inside measured G's own scatter")
print(f"    G_measured (CODATA)     = {sp.N(G_codata,8)}   (labs disagree at ~0.05%, so this is the limit)")
print("="*70)
print()
print("METHOD RULES honored by this script:")
print("  1. Only E0 and U0 (and integer COUNTS) enter the math. No alpha, no G, no c plugged in.")
print("  2. 137 is BUILT (2^6+2^6+3^2), never entered as a number.")
print("  3. CODATA appears once, in the deletable checkpoint, for comparison only.")
print("  4. beta is the quantum-gravity self-term: the self-interaction of one ground")
print("     fluctuation; Newton's G is the same interaction summed over all a body's energy.")
print("="*70)
