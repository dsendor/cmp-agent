# Run notes: arXiv 2610.17701v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (updated 2026-10-24), 28 lookalike entries.
- Date of run: 2026-10-24.

## What I read
- The extracted text of the paper (main text, references, figure captions for Figs. 1-4, acknowledgements, data and code statements), supplied as paper.txt. Per the task, no abstract page, PDF or HTML of the paper was fetched. Title taken from the text: "Observation of stacked vortex structure with number controllable Majorana zero mode in Bi2 Te3/FeTe heterojunction".
- The text has no page numbers, so quotes cite the section heading or figure.
- Not available: the Supplementary Materials (Figs. S2-S11 are referenced but not in the text). No PDF images, so figure details come from captions only.
- Data repository: none linked ("Source data will be provided with this paper. More data ... available from the corresponding author upon reasonable request."). No figure data or code, so read_mtx.py was not used.
- I did not recognize the paper and used no knowledge of its later history.

## Claims table (step 1)
| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| C1. ZBCP at vortex core, FWHM about 0.5 meV, amplitude about twice the out-of-gap conductance, spatially unsplit, read as MZM | Fig. 2I, Fig. 3B-E | 1QL-Bi2Te3 / 20 u.c. FeTe, MBE; island in Fig. 3A (100 nm field of view) | Samples grown/measured: missing. Vortices with spectra shown: two (Fig. 2 vortex at 1.0 T in a "defect-free region"; Fig. 3 single vortex in an island), unclear whether the same sample. T = 0.4 K (Fig. 1D at 1.6 K). B = 0 and 1.0 T, perpendicular only. Bias range +-10 mV. Setpoints 500 pA (Fig. 2) and 1 nA (Fig. 3B-E), Vmod 0.1 mV. Energy resolution about 0.37 meV. |
| C2. Integer-quantized CdGM sequence: L-2 = -2.1 +- 0.13, L-1 = -0.93 +- 0.14, L0 = 0.003 +- 0.11, L1 = 0.79 +- 0.17, L2 = 1.96 +- 0.22 meV; text says spacing about 0.7 meV | Fig. 3G | Fig. 3 vortex | One vortex, one line cut region. Ratios L2/L1 = 2.48, L-2/L-1 = 2.26. |
| C3. ZBCP decay isotropic and shorter than the star-shaped Bi2Te3 branch, so different origin | Fig. 3H-I | Fig. 3 vortex | Two directions (white and orange arrows). Fitted xi0; Delta and EF "given by experimental results" (values for FeTe branch not stated). |
| C4. Stacked-core vortex: dispersive Bi2Te3 branch (X-shape, linear 10-20 nm; BdG kF ~0.3 nm-1, EF ~300 meV, spacing ~0.03 meV) and quantum-limit FeTe branch | Fig. 3F, Fig. 4A (schematic), Figs. S8A, S10 | Fig. 3 vortex | One vortex. |
| C5. MZMs in all measured vortices; number tunable by field and island size (one, two, three vortices) | Fig. 4B-D (zero-energy maps, 68 nm), Fig. 4E (schematic) | not stated | Number of vortices measured: missing ("all"). Fields in Fig. 4B-D: not stated. Island sizes: no data shown. |
| C6. FeTe under Bi2Te3 is topological: Dirac-like dispersion in Te-annealed FeTe, absent in as-grown | Figs. S6, S7 (ARPES) | separate FeTe films | Not measured on the heterostructure. |
| Supporting: interfacial SC (peaks at +-1.85 and +-2.92 meV, dip at +-4.4 meV), moire gap modulation with 2.9 nm period, vortex QPI | Fig. 1H-I, Figs. S3, S4; Fig. 2A-G | | |
Missing counts: samples, islands, cooldowns, vortices measured, datasets, field values in Fig. 4, temperature series, setpoint series.

## Scope and adaptation
The paper is STM/STS of vortex cores in a heterostructure, outside the transport scope. Adapted:
- crowded-trivial-subgap-states: read as dense Bi2Te3-branch CdGM states (spacing ~0.03 meV, far below resolution) merging into a zero-bias peak at the core center. Library test texts kept verbatim; "Field and gate range ... predicted topological range" read as where the ZBCP appears (which vortices, fields, islands) versus where a topological phase is predicted; "Subband model" read as a model of the vortex bound-state spectrum. The paper's spatial symmetry and decay-length comparison (Fig. 3H-I) counted as an equivalent analysis, marked part (two directions; no calculation of the Bi2Te3-branch spectrum at the core center).
- local-probe-loophole: STM tip as the single local probe; partner mode at the other end of the vortex line or in a neighboring vortex. Tests kept verbatim, both "no".
- zbp checks: dot search -> trivial bound states near the core (impurities, CdGM); both ends -> partner mode or vortex-vortex overlap; transparency -> tip height or setpoint series; nonlocal gap -> evidence of a bulk topological transition; raw conductance -> processing behind the peak height (no series resistance in STM).

Skipped, with reasons:
- abs-quantum-dot: no semiconductor tunnel barrier or gate-defined region; the trivial-bound-state concern is covered by the two outside rows and the crowded entry.
- quasi-majorana-smooth-confinement, disorder-induced-zbp, weak-antilocalization, spin-orbit-length-pinning, exceptional-point-zero-mode: nanowire-specific mechanisms and tests (smooth end potential, class D wire disorder, channel number, normal-segment length, strong lead coupling); an STM tip in tunneling is weakly coupled.
- kondo-resonance: no quantum dot; the peak appears at vortex cores and is absent in the 0 T clean-surface spectrum; the closest STM analog (magnetic impurity states) is covered by the interstitial Fe outside row.
- fine-tuned-plateau, series-resistance-subtraction: no quantization claim (peak height is "approximately twice" the out-of-gap conductance).
- one-end-only: the other end of a vortex line is not reachable by STM; covered by local-probe-loophole.
- trivial-andreev-band-gap-reopening, protocol-parameter-sensitivity: no nonlocal data and no pass/fail protocol.
- micromagnet-stray-field (zero field), full-shell-flux-andreev (full-shell wire), chiral, island, shapiro, supercurrent, charge, kitaev, diode entries: different signature.

## Hold-out
No library source cites this paper (grep for the arXiv ID and the system found nothing; all library sources predate it). None skipped.

## Related work: how each was checked
All five: arXiv API query by ID or search (abstract read), then the arXiv abstract page fetched to confirm title and first author from citation metadata. Abstract only for all five; no full texts read.
- 1709.09401 Chen, Mingyang: abstract confirms half-odd-integer quantum-limit levels and the zero-bias peak at a conventional vortex center when Delta/EF is small.
- 1901.02293 Kong, Lingyuan: abstract confirms two vortex classes with integer versus half-odd-integer ratios. Used as the source for the half-integer CdGM outside row.
- 1812.08995 Machida, T.: abstract confirms 0 +- 20 microeV ZVBS, some vortices without it, fraction falling with field.
- 1403.1027 Yin, J.-X.: abstract confirms ZBS at interstitial excess Fe, ~10 Å decay, robust to 8 T. Used as the source for the impurity outside row.
- 1706.06074 Wang, Dongfei: abstract confirms non-split vortex ZBP and field, temperature and barrier studies.
Note: all five are also cited by the paper under review (refs 17, 25, 50, 51 and the Yin result is not cited; Yin is not in its reference list). Listed for their own results.

## Library gaps
- No STM vortex family. Lookalikes worth adding: half-integer (conventional) CdGM levels in the quantum limit (Kong 2019, Chen 2018), unresolved dense CdGM states giving a core zero-bias peak (Chen 2018 abstract), impurity-bound zero-energy states at interstitial Fe (Yin 2015).
- Checks worth adding for STM: energy resolution compared with level spacing; tip-height (tunneling barrier) series; temperature series; counts of vortices with and without the peak; same-spot zero-field spectra; vortex-vortex hybridization versus spacing.

## Unsure
- Whether the Fig. 2 and Fig. 3 vortices are from the same sample or session; I counted them as two datasets.
- Whether zero-energy maps (Fig. 4B-D) count as "shown" for following the peak with the vortex; marked part, since maps cannot separate a peak from a flat in-gap density of states.
- Check 6 (raw conductance) adapted loosely; marked partly because setpoints are given and processing is not.
- The ratio arithmetic in question 5 is mine from the quoted fit values.
- Related-work note above: I first wrote that Yin is cited; checking the reference list, Yin 2015 is not cited by the paper. The others (Wang = ref 17, Machida = ref 25, Chen = ref 50, Kong = ref 51) are.

## Skill issues
- Text-only input has no page numbers; the skill requires page numbers for every quote. I used section headings and figures.
- The template's "<n> known lookalikes in topological transport" and the step 2 rule to match by signature fit poorly for an out-of-scope paper; it is unclear whether outside rows or adapted rows are preferred when a library entry only roughly fits.
- Checks must be marked done, partly or not done; there is no "not applicable" for adapted checks (for example series resistance in STM).
- The status rule says every status except "Not tested (not mentioned)" needs a verbatim quote; for "data bear on it" the only fitting quote is a figure caption, which reads oddly.
- Adapted library rows: unclear whether test texts should stay verbatim (I kept them) or be rewritten for the device.
- Step 5 says to start related work from the matched entries' sources; for an out-of-scope paper those sources are nanowire papers and were not useful.
- Step 7 tells the skill to write files under reports/; the task overrode this.
