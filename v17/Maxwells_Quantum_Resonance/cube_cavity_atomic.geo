// ============================================================
// cube_cavity_atomic.geo  --  Paper X (1,1,1) closure mode, ATOMIC SCALE.
// The cube built at the FRAMEWORK-DERIVED electron Compton wavelength as the
// absolute physical size (METERS): the oscillator/atom at its TRUE size, with
// the size itself DERIVED from eps0/mu0 -- no measured mass, no h.
//   a_phys = lambda_C(derived) = 2*pi*eps0*sqrt(60*pi)/(315*(1-12a^2+a^3))
//          = 2.426308653e-12 m   (V17 compton_wavelength_V17.py; forced 315-cycle
//    mode + (1-12a^2+a^3) tail, alpha derived from eps0/mu0). Matches CODATA
//    (h/m_e c = 2.42631023867e-12 m) to 6.5e-5%.
//
// NUMERICAL NOTE (why ScalingFactor, not a literal 2.4e-12 Box): OpenCASCADE's
// geometric tolerance (~1e-7) is FAR larger than a 2.4e-12 box, so a literal
// tiny Box collapses to a degenerate point and meshing fails. The robust,
// standard fix: build the topology at unit size (OCC-happy) and apply
// Mesh.ScalingFactor so the EXPORTED node coordinates are the real atomic
// dimension. The resulting mesh .nodes are genuinely ~1e-12 m -> atomic scale.
// Combined with REAL eps0/mu0 in the .sif, the eigenfrequency comes out at the
// electron's real physical frequency (~1e20 Hz).
// ============================================================
SetFactory("OpenCASCADE");

L0 = 1.0;          // topology build size (OCC-stable); scaled to atomic on export
lc = L0/14.0;      // same 14 divisions as the lab-scale run

Box(1) = {0, 0, 0, L0, L0, L0};

Physical Volume("vacuum") = {1};
s() = Boundary{ Volume{1}; };
Physical Surface("pec") = { s() };

Mesh.CharacteristicLengthMax = lc;
Mesh.CharacteristicLengthMin = lc/3.0;
Mesh.ElementOrder = 1;
Mesh.Algorithm3D = 1;                 // Delaunay
Mesh.ScalingFactor = 2.426308653e-12;  // DERIVED electron Compton wavelength (V17, eps0/mu0 + forced 315 + tail); atomic scale [m]
