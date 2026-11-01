# Run notes: 2610.17701v1

**Library version:** 0.5 (meta.updated 2026-10-24), 28 lookalike entries.

**What I read**
- Paper: only the extracted text the task supplied (main text, references, figure captions, back matter). As the task said, I did not fetch the abstract page, PDF or HTML.
- What I couldn't see: Supplementary Materials and Figs. S1 to S11 (the main text cites S2, S3A-F, S4A, S6, S7, S8, S8A, S10, S11 and "Other alternative scenarios are discussed in the Supplementary Materials"). The figure images were unavailable too, so figure details come from the captions. The text has no page numbers, so quotes are located by section and figure.
- No data repository is linked ("Source data will be provided with this paper"), so I used none.
- Title: the abstract page was unavailable, so the report uses the title from the text, shortened.
- I did not recognize the paper.

**Claims table (step 1)**

| Claim | Figures | Device / conditions | Counts |
|---|---|---|---|
| Interfacial superconductivity confined to 1QL-Bi2Te3; gaps ±1.85 and ±2.92 meV, moiré-modulated (2.9 nm period) | Fig. 1D-I, S3, S4 | MBE 1QL-Bi2Te3 on 20 uc FeTe; topography at 1.6 K | Samples not stated |
| Star-shaped vortex and QPI-like LDOS modulation from the Bi2Te3 Fermi surface | Fig. 2A-H, S8 | One vortex, 50 nm map, 1.0 T, "defect-free region", 0.4 K | One vortex shown |
| Two branches of vortex bound states (dispersive Bi2Te3 branch; quantum-limit FeTe branch) | Fig. 3B-G, S8A, S10 | One vortex in a 100 nm island (Fig. 3A), setpoint 10 mV / 1 nA | Two line cuts (white and orange arrows) |
| Spatially unsplit ZBCP, FWHM about 0.5 meV, about twice the above-gap conductance, isotropic decay | Fig. 2I, 3C, 3E, 3H-I | 1.0 T, 0.4 K, resolution "~0.37 meV" | Fig. 2I vortex and Fig. 3 vortex (I couldn't tell from the captions whether these are the same vortex) |
| Discrete levels L-2 to L2 "approximately follow an integer quantized sequence" | Fig. 3G | Same vortex | One line cut |
| FeTe topological origin: Dirac-like dispersion in Te-annealed FeTe | Fig. S6, S7 (ARPES) | Separate FeTe films | Not stated |
| Vortex number (1, 2, 3) tunable by field and island size; "MZMs are observed in all measured vortices" | Fig. 4B-E | 68 nm area, zero-energy maps only, setpoint 10 mV / 1 nA | Field values not given in caption; vortex count not given |

Missing counts: samples grown or measured, islands, vortices measured, cooldowns, tips, field values in Fig. 4, any temperature series, any setpoint series.

Numbers I checked:
- The Bi2Te3-branch spacing given as "~0.03 µeV". With Δ = 1.85 to 2.92 meV and EF about 300 meV, Δ²/EF = 11 to 28 µeV, so roughly 0.03 meV fits and 0.03 µeV is a factor of about 1000 off. Raised as question 6. The paper's conclusion (spacing far below 0.37 meV) holds either way.
- The text gives "energy spacing of about 0.7 meV". The fitted levels give spacings of 0.79 (L0 to L1), 0.93 (L0 to L-1) and 1.17 (L1 to L2, L-1 to L-2).
- Level ratios: E2/E1 = 2.48 (positive) and 2.26 (negative). An integer sequence predicts 2, and a half-odd-integer sequence predicts 3 (from 0.5 to 1.5). Both raised as question 5.

**Scope adaptation.** This is STM vortex-core spectroscopy, outside the library's nanowire transport scope. I adapted:
- `kondo-resonance`: adapted from a dot to a magnetic impurity (interstitial Fe). Its tests (even-odd occupancy, temperature, Zeeman) were kept, and the occupancy test doesn't really apply to STM.
- `disorder-induced-zbp`: adapted to moiré and interface inhomogeneity. Its tests (end-to-end correlation, gap closing, gate insensitivity) were kept as written; their STM equivalents are only loose.
- `local-probe-loophole`: applies as written (STM is a purely local probe).
- `fine-tuning-and-selection`: always included.
- The zbp checks were adapted as follows: zbp-dot-search to an impurity search, zbp-both-ends to the vortex-line ends, zbp-transparency to tip-sample distance, zbp-raw-conductance to normalization and fitting. zbp-nonlocal-gap was kept as written.

**Entries skipped and why**
- abs-quantum-dot, quasi-majorana-smooth-confinement, spin-orbit-length-pinning, exceptional-point-zero-mode, one-end-only, weak-antilocalization: all assume a nanowire with a tunnel barrier, a normal segment or a strongly coupled lead. None of that is present in vacuum STM tunneling into a vortex. The physics of trivial near-zero bound states is covered by the two outside rows.
- crowded-trivial-subgap-states: covered more specifically by the outside half-odd-integer CdGM row.
- fine-tuned-plateau, series-resistance-subtraction: no quantized-height claim.
- trivial-andreev-band-gap-reopening, protocol-parameter-sensitivity: no gap protocol.
- micromagnet-stray-field: field is applied (1.0 T); the signature is a zero-field peak.
- full-shell-flux-andreev, island-states-coulomb-spacing, the shapiro, supercurrent, charge, chiral, kitaev and diode entries: wrong device or signal.

**Sources held out.** None. No library source is about this October 2026 paper by topic or date. I did not re-fetch the 2026 versions of arXiv 2502.19560 and 2501.18631 to confirm they don't cite it.

**Related work, how each was checked**
- 1901.02293 (Kong et al.): read the API abstract and the full text (PDF via pdftotext); confirmed ID, title, first author, and the integer versus half-odd-integer passages. It is also the source for the first outside row. Its tests come from its normalization of EL/ΔE and its comparison of vortices with and without the peak.
- 2105.01354 (Kim et al.): read the API abstract and the full text; confirmed ID, title, first author, the La(0001) result, and the spacing-below-resolution and quasi-classical (Kramer-Pesch) comparison. It is the source for the second outside row.
- 1812.08995 (Machida et al.): read the API abstract; confirmed ID, title, first author and the fraction-versus-field statement.
- 1904.06124 (Zhu et al.): read the API abstract; confirmed ID, title, first author and the tunnel-coupling plateau statement.
- 1706.06074 (Wang et al.): read the API abstract; confirmed ID, title ("Evidence for Majorana bound state in an iron-based superconductor") and first author. I read only the abstract text that printed (its first 900 characters). It covers the non-split peak and the start of the field, temperature and tunneling-barrier sentence.
- Also opened but not used: 2606.03637 (THz CdGM, not STM), 1804.09319, 2209.06646.

**Library gaps.** There is no STM vortex family. Candidates for new entries or checks:
- trivial quantum-limit CdGM levels with a half-odd-integer sequence (Kong et al. 2019);
- non-split trivial zero-energy vortex states from Fermi-contour focusing (Kim et al. 2021);
- a tip-sample coupling series as the STM analogue of zbp-transparency (Zhu et al. 2020);
- hybridization of the top and bottom ends of a vortex line in thin films, and of nearby vortices (relevant to Fig. 4). I found no opened source for this one, so it stays out of the table.

**Unsure**
- Whether the Fig. 2I and Fig. 3 vortices are the same. This sets the "part" on the second-dataset test.
- Outside row 1, first test: I marked it "part" because you compare the levels with an integer sequence only, without normalizing or drawing a half-odd-integer line.
- Outside row 2: not "ruled out", because the paper doesn't name that mechanism, although the resolved discrete levels and the isotropic decay bear on it.
- Kondo row: "argued, not tested" over "data bear on it". Fig. 2I's 0 T spectrum is at "clean surface", which may be a different location.

**Skill issues**
- The template asks for page numbers. Text-only input has none, and the skill doesn't say what to use instead (I used sections and figures).
- No check family fits STM vortex spectroscopy. Checks like zbp-both-ends then have only done, partly or not done, with no "not applicable", so "not done" can read as a gap the technique can't fill.
- Adapted entries keep library tests that may not apply (even-odd occupancy). Tests have no "n/a", which pushes statuses to "not tested".
- The "one device at one tuning covers the claim" rule is unclear when the claim is about "all measured vortices" but the analysis shows one vortex.
- "Ruled out for the claim" requires that "the paper concludes against the lookalike". For outside rows the paper rarely names the mechanism, so that status is nearly unreachable even when the data bear on it.
- Step 7 says to write reports/ files; this task overrode that. The title is meant to come from the abstract page, which was unavailable.
