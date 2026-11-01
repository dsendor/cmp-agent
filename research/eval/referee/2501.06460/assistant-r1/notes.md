# Run notes: 2501.06460v1

## Library and inputs
- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (updated 2026-10-24), 28 lookalike entries; checks section read.
- Skill: cmp-assistant/skill/SKILL.md and skill/report-template.md, read once at the start.
- Paper: v1 PDF (23 pages: main text pp. 1-10, figures pp. 11-15, supplement pp. 16-23) and its extracted text, both supplied. Figures read from the PDF rendered at 110 and 300 dpi (Fig. 1-5, Supp. Fig. 1-7).
- Not opened, per the task: the paper's arXiv abstract page, any other version, journal version, comments. An arXiv API search returned 2501.06460v2 (listed title "Electric field tunable coupling strength and quantum metric hot spots in a moiré flatband superconductor"); I did not open it and used nothing from it.
- Report title taken from the v1 PDF (the skill asks for the abstract-page title, which the task forbade fetching); shortened in the header.
- No figure data, code or data repository: the paper says data are available on request (p. 7). read_mtx.py not used.
- I did not recognize this paper or know its later history.

## Claims table (step 1)
| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| Robust 2D superconductivity: zero Rxx, Tc ~1.2 K (D = 0) and ~2 K (D = 0.26), BKT V ∝ I^3 with TBKT 1.1 K, max TBKT 1.6 K | Fig. 1d-g, Supp. Fig. 5 | one ATQG Hall bar, θ = 1.58° | νtot −6 to 6, D −1.0 to 1.1 V/nm (Fig. 1d); T 30 mK to 5 K; V-I 0.15 to 3 K |
| Device homogeneity | Supp. Fig. 1 | same device, four pairs (4-5, 5-7, 11-10, 10-9) | Rxx vs n at D = 0 only |
| Dirac and flat band carriers separated by Landau fans; flat band width ~50 meV; cascade at νtot ~2.36 | Fig. 2, Supp. Fig. 3 | same | B⊥ 0 to 9 T at T = 1.7 K, D = 0 only; Rxy map at 0.5 T over D −0.9 to 0.9 |
| BCS-BEC crossover from ξ × kF (ξ from Bc0) | Fig. 3, Fig. 4a-c, Supp. Fig. 2 | same | ξ from linear Bc(T) fit, six points 0.6 to 1.25 K (Supp. Fig. 2b); Bc criterion not stated |
| D-tunable Tc, pseudogap-like dV/dI(T) | Fig. 4 | same | D −0.4 to 0.45 V/nm at νtot = 2.31; dV/dI(T) at Idc = 265 and 420 nA |
| Flat band velocity ~1700 m/s from jn (Zener-Klein) | Fig. 5a, b | same | Idc up to ~650 nA; B⊥ 0 and 0.2 T; width for j not stated |
| Superfluid stiffness up to ~4 × 10^7 H^-1, one order above conventional | Fig. 5c, d | same | νtot = 2.31 only, D −0.3 to 0.42; temperature and contact pair for Fig. 5c not stated |
| Pauli-limit violation (~7 T vs Bp ~3.7 T) | Supp. Fig. 4 | same | B∥ 0 to 10 T; alignment procedure not described |
| T*/TBKT 1.45 to 2.19 | Supp. Fig. 5 | same | two D values |
Missing counts: devices fabricated, devices measured, cooldowns (two cryostats named, Supp. Note 1, so at least two are likely), which pair and cryostat each figure uses.

Figure observations used in the report: Supp. Fig. 7a (ν = 2.31, 100 mK, B = 0) switching edge ~40 to 50 nA at D = 0 and ~120 nA near D = 0.22; Fig. 5c (νtot = 2.31) ~100 nA at D = 0 and ~190 nA near D = 0.25. Supp. Fig. 1b normal-state Rxx near n ≈ 1 to 2.5 × 10^12 cm^-2: ~1.9 kΩ (5-7, 10-9) vs ~0.45 to 0.6 kΩ (4-5, 11-10). Read by eye from the figures.

## Matching (step 2)
- Kept: fine-tuning-and-selection (always). Adapted: field-enhanced-supercurrent-resonances (supercurrent family; D in place of B, quantum-metric stiffness in place of triplet pairing; Fig. 5c shows finite-bias ridges meeting the switching edge near the Ds peak).
- Skipped as not applicable (no tunneling spectroscopy, nanowire, junction, island, Shapiro, interferometer, QAH, Kitaev chain or automated protocol): abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, fine-tuned-plateau, series-resistance-subtraction, one-end-only, trivial-andreev-band-gap-reopening, micromagnet-stray-field, full-shell-flux-andreev, protocol-parameter-sensitivity, chiral-plateau-superconductor-short, island-states-coulomb-spacing, shapiro-landau-zener, shapiro-nonlinear-resistance, charge-trap-fractional-shift, spin-orbit-length-pinning, exceptional-point-zero-mode, transparent-junction-pi-crossing, switching-jump-blind-region, false-poor-mans-majorana, local-probe-loophole, coulomb-dominated-interferometer, diode-vortex-screening (no current-direction asymmetry claimed).
- Checks: no family in `checks` covers superconductivity or supercurrent claims, so only the practice checks (report-counts, report-ranges, report-processing) were walked.

## Hold-out
- Library sources used in the report: Frolov et al. 2309.09368 (2023, predates the paper) and Akrap, Frolov et al. 2501.18631. I downloaded 2501.18631v2 and searched its text for "quadralayer", "quadrilayer", "06460", "Le Liu" and "multiband superconductivity": no hits. No sources held out.
- Outside sources all predate the paper except none; none discuss it (all earlier than January 2025).

## Related work and outside rows: how each was checked
All via the export.arxiv.org API abstract plus the arxiv.org/abs page (title, first author, journal ref confirmed); abstract only, no full text.
- 2112.13401 Tian et al. (abstract): vF ~1000 m/s from Schwinger-limited transport, stiffness, BCS-BEC.
- 2406.13740 Tanaka et al. (abstract): kinetic inductance stiffness in MATBG, larger than Fermi liquid.
- 2406.13742 Banerjee et al. (abstract): kinetic inductance in TTG, nodal.
- 1908.04595 Uri et al., Nature 581, 47 (abstract): twist-angle span ~0.1°, global transport hides it. Used for the twist-angle row; tests taken from its local mapping and its point that global transport can look uniform.
- 2406.02521 Mukherjee et al., Nature Materials 24, 1400 (abstract): Josephson network from moiré inhomogeneity, switching statistics, broadened BKT. Used for the network row.
- 1905.01221 Venditti et al., PRB 100, 064506 (abstract): nonlinear IV exponent vs inhomogeneity model. Used for the BKT row.
- Opened and not used: 0909.0479 Benfatto et al. (abstract), 2111.08735 Di Battista et al. (abstract; Gth = 0.19 pW/K, relevant to Joule heating at the 100 to 650 nA bias of Fig. 4f and 5a, but it describes no control, so no row).
- Search hit skipped: 2501.06460v2 (this paper).

## Library gaps
- Twist-angle disorder in moiré devices (Uri et al. 2020).
- Inhomogeneous Josephson-network switching standing in for depairing critical current (Mukherjee et al. 2025).
- Inhomogeneity mimicking the BKT V-I exponent (Venditti et al. 2019; Benfatto et al. 2009).
- Joule heating at high bias in low heat capacity moiré superconductors (no source with a control found; Di Battista et al. 2021 bears on it).
- Criterion dependence of Tc, Bc and Ic (no source opened).

## Unsure
- Question 8 rests on my own estimate, Ds(TBKT) = 8e²kBTBKT/(πħ²) ≈ 1.3 × 10^8 H^-1 at 1.6 K (0.9 × 10^8 at 1.1 K), using Ds = e²n/m per square as in the paper's "conventional" line. I used it as the one question no entry raises.
- Critical current values are read by eye from color maps.
- Whether the field-enhanced-supercurrent adaptation is a fair match: the mechanism (a finite-bias feature moving with a tuning knob and changing the switching current) carries over, the field knob does not.
- "Tested in part" for the adapted row, although the paper never names the lookalike; the status rules allow it once a test is shown.

## Skill issues
- No `checks` family for superconductivity or supercurrent claims; the Scope paragraph covers "different kind of measurement" but not a whole different subfield, so the report leans on outside rows.
- The skill asks for the arXiv abstract-page title, which conflicts with a test setup that forbids fetching the paper; no fallback is stated.
- Step 7 says write `reports/<id>.md`; this run was told to return text. Fine, but the skill could say what to do when writing is refused.
- Outside rows: the skill says "marked (not in library)" in the table while flags use "outside: <name>"; consistent but two conventions.
- "Take its tests from the control that paper describes" is hard when the opened source is an abstract only; I phrased tests from what the abstracts describe.
- "A second device or dataset shown": unclear whether other contact pairs of one device count as a second dataset; I marked "part".
