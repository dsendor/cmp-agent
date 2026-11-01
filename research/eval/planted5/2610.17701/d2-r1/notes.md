# Run notes: arXiv 2610.17701v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (updated 2026-10-24), 28 lookalike entries, plus the checks section.
- Skill and template: cmp-assistant/skill/SKILL.md and report-template.md, read once at the start.
- Paper: only the extracted text supplied by the caller (no PDF, no abstract page, no supplement). Figure details come from the captions. The text has no page numbers, so quotes cite the section heading and figure. Supplementary figures (S2 to S11) are referenced but not available. I did not fetch the paper itself. Its arXiv API metadata (ID, title, first author, date 2026-10-13) showed up incidentally as a hit in a search for related work. I used it only to confirm the title matches the text and read nothing else from it.
- Data repository: none linked ("Source data will be provided with this paper"; code "upon reasonable request"). No figure data, so read_mtx.py was not used.
- I did not recognize the paper and have no knowledge of its later history.

## Claims table (step 1)

| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| Interfacial superconductivity on 1QL-Bi2Te3/FeTe (20 uc FeTe), absent on bare FeTe; gaps at ±1.85 and ±2.92 meV, moiré-modulated (2.9 nm period) | Fig. 1D-I, S3, S4 | MBE film, Bi2Te3 islands | Fig. 1 at T = 1.6 K, 10 mV/200 pA; samples and islands not counted |
| Star-shaped vortex with QPI-like LDOS modulation of Bi2Te3 origin | Fig. 2A-H, S8 | one vortex, 1.0 T, 50 nm map | energies 0, ±3 meV; one field |
| Two branches of vortex bound states: dispersive X-shaped (Bi2Te3, level spacing ~0.03 meV) and ZBCP (FWHM ~0.5 meV, ~2x the above-gap conductance) with discrete levels L-2..L2 = -2.1, -0.93, 0.003, 0.79, 1.96 meV | Fig. 2I, 3A-G | one vortex in an island (Fig. 3A, 100 nm map); Fig. 2I may be the same or another vortex | 1 nA setpoint for line cuts; two directions; resolution "~0.37 meV at 0.4 K"; measurement temperature and field for Fig. 3 not stated |
| ZBCP decay isotropic and shorter than the Bi2Te3 branch, so a separate (FeTe) origin; stacked cores | Fig. 3H-I, 4A | same vortex | two directions only; fitted ξ0 values not in main text |
| MZMs in "all measured vortices"; vortex number (1, 2, 3) tuned by field and island size | Fig. 4B-D | one island (68 nm maps) | field values not stated; spectra at these vortices not shown; number of vortices measured not given |
| FeTe topological: Dirac-like dispersion in Te-annealed FeTe, absent in as-grown | Fig. S6, S7 (ARPES) | FeTe films, not the heterostructure | not available |

Missing counts: samples grown, islands measured, vortices measured with spectra, vortices with a ZBCP, cooldowns, temperatures, fields for Fig. 3 and Fig. 4.

## Entries matched, adapted, skipped

- Matched: fine-tuning-and-selection (always). Adapted: local-probe-loophole (STM tip is a local probe; the partner of a vortex mode sits at the island edge or in another vortex).
- Checks adapted (zbp family to STM vortex spectroscopy): zbp-dot-search to a search for trivial core bound states (CdGM, impurity); zbp-both-ends to the partner mode; zbp-transparency to tip-sample distance; zbp-nonlocal-gap to independent band-topology evidence in the same heterostructure; zbp-raw-conductance to dI/dV processing and fitting. Practice checks used as written. Shapiro, kitaev and charge checks do not apply.
- Skipped, nanowire or transport specific: abs-quantum-dot (no tunnel barrier dot; the vortex analogue is covered by the outside CdGM row), quasi-majorana-smooth-confinement, spin-orbit-length-pinning, exceptional-point-zero-mode, one-end-only, trivial-andreev-band-gap-reopening, full-shell-flux-andreev, weak-antilocalization, micromagnet-stray-field (no magnets).
- Skipped, overlapping with outside rows: kondo-resonance (its mechanism and tests need a quantum dot; the magnetic-impurity route is covered by the excess-Fe row, whose source is STM on the same family of materials); disorder-induced-zbp and crowded-trivial-subgap-states (their tests are wire-specific; the vortex versions are the excess-Fe and CdGM rows).
- Skipped, no matching claim: fine-tuned-plateau and series-resistance-subtraction (no quantization claim; ZBCP height is "approximately twice" the above-gap conductance), protocol-parameter-sensitivity (no protocol), island, Shapiro, supercurrent, charge, chiral, kitaev, diode entries.

## Sources held out

None. I found no library source that cites this paper. All library sources predate it (latest are 2026 versions of Legg 2502.19560 and Akrap 2501.18631, both posted before 2026-10-13). I checked this from titles and dates, not by refetching each one.

## Related work and outside-row sources (how checked)

All checked via the arXiv API (export.arxiv.org, id_list query), confirming ID, title, first author and abstract text. Abstract only for each:
- 1901.02293 Kong et al.: abstract confirms integer versus half-odd-integer level ratios tied to the presence or absence of the ZBP.
- 1709.09401 Chen et al.: abstract confirms that in most type-II superconductors "a symmetric peak appears at zero-bias at the vortex center", and gives E_mu = ±mu Δ²/E_F with half-integer mu. This is the source for the outside CdGM row.
- 1312.7110 Xu et al.: abstract confirms the ZBP "splits right off the vortex center in conventional superconductors". Used for the second test in the CdGM row; not listed in related work.
- 1403.1027 Yin et al.: abstract confirms an isotropic ZBS at interstitial excess Fe sites, decay ~10 Å, robust to 8 T. This is the source for the outside excess-Fe row.
- 1812.08995 Machida et al.: abstract confirms some vortices lack the ZVBS and the fraction falls with field.
- 1904.06124 Zhu et al.: abstract confirms the tunnel-coupling plateau for zero-energy vortex states and none for CdGM states.

## Library gaps

- No entries for STM vortex spectroscopy. Candidates: trivial CdGM states (merged into a zero-bias peak, or half-integer quantum-limit levels), impurity zero-energy bound states (interstitial Fe, Yin et al.), vortices in trivial regions or a field-dependent fraction of zero-mode vortices (Machida et al.; Kong et al.), and tunnel-coupling dependence (Zhu et al.) as a test.
- No check family for vortex or STM zero modes. I adapted zbp checks, which is a judgment call.

## Uncertain points

- Whether Fig. 2I (black line) and Fig. 3 show the same vortex is unclear from the captions. So "second dataset shown" is marked part.
- Level-ratio test marked part: from the fitted values, |L2/L1| ≈ 2.48 and |L-2/L-1| ≈ 2.26 (integer = 2, half-odd = 3), and the stated "about 0.7 meV" spacing does not match the fitted L0-L1 (0.79/0.93 meV) or L1-L2 (1.17 meV) spacings. Fit uncertainties of ±0.11 to ±0.22 meV.
- I counted the zero-energy maps at several fields (Fig. 4B-D) as partial evidence that the zero-energy weight follows field-induced vortices. Zero-energy maps also brighten at trivial vortex cores, so this is weak.
- Wording I noticed in the text: "A trivial scenario is that this MZM is generated from superconducting FeTe" (Origin section) seems to use "trivial" to mean "simple". I did not treat it as the authors calling the mode topologically trivial. Also "These observations provide compelling spectroscopic evidence for the presence of Majorana zero modes" (Fig. 3 paragraph). I quote neither in the report.

## Skill issues

- The skill assumes transport (nanowire) devices. For STM vortex papers, nearly every zbp test text ("both ends", "gates", "series resistance") needs adapting. flags.json requires library test text verbatim, so adapted meaning and literal text diverge, for example local-probe-loophole "Overlap estimated through a quantum dot in series".
- Page numbers are required for quotes, but text-only input has none. I used the section and figure. The skill could say what to do when pages are unavailable.
- "Use the title on the arXiv abstract page" conflicts with the caller's no-abstract-page rule. I used the title from the text.
- When an outside lookalike draws on two papers (CdGM row: Chen and Xu/Kong), the flags schema has one source URL. I gave the primary one.
