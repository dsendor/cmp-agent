# Changes from arXiv v1 to the accepted version (2511.09402)

AI-generated change log. Old = arXiv v1 (`text/old.txt`); new = accepted version (`text/new.txt`).
Page numbers follow the `=== PAGE n ===` markers. The supplementary file of the accepted version
is not in the inputs, so supplementary content is known only from how the main text cites it.

## Title, abstract, framing

- **Title reworded (editorial).** Old p1 "The “parent” state in kagome metals and superconductors:
  Chiral-nematic Fermi liquid state" became new p1 "Chiral-nematic Fermi liquid state as the parent
  state of kagome metals and superconductors". The claim is unchanged.
- **Abstract nearly unchanged.** Only "which is the heart of kagome physics at low temperatures" is
  added (new p1). "Discovery", "direct evidence", "demonstrating that the CDW-triggered exotic states
  descend from" and "chiral-nematic superconducting state" all stay.
- **Introduction adds the torque result up front** (new p2): "thermodynamic torque measurements have
  provided macroscopic evidence for spontaneous rotational-symmetry breaking above the bulk CDW
  transition". In v1 this was only in the Discussion (old p10).
- Author order changes and C.S. gains a role in the experiments; Z.W. (Zhan Wang) is credited with
  theory (new p11). Editorial.

## Sample and topography

- **Ti dopants identified in topography** (new p2): "the Ti dopants appear as dark features beneath
  the Sb-terminated surface (Fig. 1d)". Not in v1 (old p4).
- Fig. 1g caption now gives colours for q1, q2, q3 ("blue, red, and dark red dashed curves", new p2;
  old p20 had "dark red dashed curves" only).

## DFT comparison and the kz = π cut

- **New caveat in Results** (new p3): the kz = π CEC "is an approximation adopted to provide an
  orbital- and symmetry-based reference", "a qualitative guide". Repeated for Fig. 2e (new p3:
  "the selected DFT contours are used only as a qualitative reference").
- **New Methods justification** (new p9): fixed kz "is justified by the quasi-two-dimensional
  electronic structure and weak kz dispersion", citing Rhodes et al. (new ref. 51) and refs. 52, 53.
- DFT settings (no SOC, 300 eV cutoff, VCA) unchanged (old p18, new p9).

## Symmetry argument: nematic versus chiral-nematic

- **C6 wording clarified** (new p3): "Apparent QPI C6 symmetry arising from C3 symmetry combined with
  the intrinsic inversion symmetry of Fourier-space intensity maps", replacing "(C3 plus inversion)"
  (old p5).
- **New paragraph on apparent nematicity** (new p3): "At first glance, the QPI patterns appear strongly
  nematic", "reminiscent of the pronounced C2-symmetric QPI" in undoped CsV3Sb5; "thanks to our high
  q-space resolution, subtle but distinct QPI differences among all three directions can be
  resolved". Replaces v1's direct "Surprisingly, the QPI features ... exhibit significant
  differences" (old p5).
- Fig. 2b caption adds that the grey dashed lines are visual guides (new p4).
- **New Discussion paragraph distinguishing the state from the chiral CDW and CDW-driven nematicity**
  (new p8): those "are manifested as spectral-weight anisotropy in q-space and vanish upon chemical
  doping", whereas here the symmetry breaking "is reflected in the momentum-space electronic structure
  itself".

## Phenomenological model

- **Distortion formula changed.** Old p6 kF = kF0 + η·sin(2θ), with φ = π/2 in the Discussion (old
  p12). New p3 kF = kF0 + η·cos(2θ − π/6), and the Discussion now says φ = −π/6 (new p8; the minus sign
  is lost in the text layer but the Results formula fixes it). One convention now used in both places;
  φ is still "used for our QPI data analysis", not fitted.
- **New Methods section "Possible origin of chiral–nematic charge order"** (new p9): n(θ) = n0 cos 6θ +
  δn cos(2θ + φ) with explicit sublattice densities n1, n2, n3 and the nematic (φ = 0, ±π), purely chiral
  (φ = ±π/2) and chiral-nematic (generic φ) cases.
- **Mechanism hedged** (new p8–9): "In principle, both lattice and electronic channels could generate
  such a state. We conjecture that, in the electronic channel ...". Old p12 had only the electronic
  conjecture.

## Normalisation and set-point effect

- **Fig. 3 now uses Feenstra-normalised maps** (new p3, p5): "the Feenstra-normalized conductance maps
  L(r, E) = [dI/dV(r, E)]/[I(r, E)/V]". Old p7 used dI/dV maps.
- **New Methods section "Removal of set-point effect"** (new p9) with Eq. (1), Supplementary Fig. 15
  and refs. 44–46 (Feenstra; Hanaguri; Kostin).
- Fig. 3a caption: "Fitted Gauss-like backgrounds are subtracted" (old p22) became "Center
  low-frequency backgrounds are masked" (new p5); red arrows added to mark the difference near E_F.

## Dispersions, velocities, uncertainties

- **Error bars defined** (new p5, Fig. 3 caption): errors "combining the fitting standard errors and
  the pixel resolution", εt = sqrt(εs² + εpix²). None in v1.
- **Fit window statement added** (new p6): "we focus only on the low-energy velocities extracted away
  from these kink features".
- **Numbers changed** (re-analysis on L maps):
  - v1,F: (4928.84, 5115.95, 4350.17) → (4583.84, 5107.30, 4121.17) meV/|Q_Bragg|.
  - m1*/m_DFT: (1.23, 1.19, 1.40) → (1.33, 1.19, 1.47).
  - v2,F: (1554.41, 1279.89, 1074.19) → (1649.17, 1292.64, 1082.99); m2*: (1.63, 1.97, 2.35) → (1.53, 1.95, 2.33).
  - v3,F: (2571.86, 1979.03, 1703.77) → (2226.03, 1945.97, 1707.13); m3*: (1.25, 1.62, 1.89) → (1.45, 1.65, 1.88).
  - Velocity ordering typo fixed: old p8 "v2,s^I > v2,s^II > v3,s^III" → new p6 "vI2,s > vII2,s > vIII2,s".
  - Average energy splitting 15.0 meV → 14.4 meV; T* 174 K → 167 K (old p10, new p8).
- Precision unchanged (six significant figures); "fall within the range of 1.29–1.71" kept although
  α = 1.19 still lies below it (new p6).
- **New ARPES comparison paragraph** (new p6): QPI mass enhancement "is lower than that reported by
  ARPES electron-phonon measurements", with three reasons (composition, bare-band reference,
  surface sensitivity / occupied vs unoccupied states).

## CDW samples (x = 0.05, x = 0)

- **Orbital-origin argument added** (new p6): unidirectional stripes come "primarily from out-of-plane V
  orbitals", the triangular and circular QPI "share the same electronic orbital origin" as at x = 0.15.
  Repeated later on p6.
- Fig. 4b caption still says "1a0 × 4a0 stripe order" while the text says 4a0 × 1a0 (new p7).
- CDW peak ratio 2.6:1.2:1.0 at one bias unchanged.

## Reproducibility, surfaces, defects (new supplementary material)

- **New doping x = 0.04** (Supplementary Fig. 16) and **Cs-terminated surface** (Supplementary Fig. 14)
  (new p7): "chiral QPI has also been observed on the Cs-terminated surface", so the effect is said to be
  independent "of the Ti doping level and surface termination".
- **New Fig. 4g** "Summary of the QPI evolution across different Ti doping levels" (new p7), cited on p8.
- **New defect analysis** (new p8): T-matrix calculations (Supplementary Figs. 18–20) show that
  "sublattice-selective and anisotropic point-defect configurations do not naturally reproduce" the
  geometry; no "dominant or correlated defect population is evident" (Supplementary Fig. 13); new ref. 35.

## T* and the phase diagram

- **Caveats added** (new p8): "While the resistance–temperature curves do not exhibit a pronounced
  additional anomaly beyond the CDW-related feature"; and (new p9) T* "may be precisely determined in
  the future by temperature-dependent microscopic probes, such as nano-ARPES in resolved chiral domains".
  The T* line in Fig. 4f and the "parent state" claim are kept.
- **Phase-diagram text expanded** (new p8): CDW, nematicity and superconductivity "with V-shaped gap"
  emerge from the parent state; at high doping a "U-shaped gap" superconductor develops directly
  (Supplementary Fig. 11).

## Superconducting state

- B-QPI now also cites Supplementary Fig. 17 (new p8). The conclusion "strong evidence for a
  chiral-nematic SC ground state" is unchanged.

## Supplementary material, data, references, format

- Extended Data Figs. 1–6 and Figs. S1–S4 renumbered as Supplementary Figs. 1–20 (journal format).
- **Data availability statement added** (new p9): raw data deposited at Science Data Bank.
- Ref. 37 no longer cited for the crystal structure (new p2); duplicate ref. 34 (= ref. 17) removed;
  refs. 41, 42 updated to published versions; new refs. 35, 44–46, 51–53. Ref. 43 (UTe2) still cited for
  the affine correction (new p9); Lawler–Fujita not cited.
- Affine correction still described only for Figs. 2b and 4d (new p9).
- "Summary" heading merged into the Discussion (journal format). Acknowledgements, funding added.
