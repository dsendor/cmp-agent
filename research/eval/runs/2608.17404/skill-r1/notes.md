# Run notes: arXiv 2608.17404v1 (lookalike assistant, skill-r1)

- Date: 2026-10-23. Library `meta.version`: 0.4 (28 lookalikes, checks for zbp, shapiro, kitaev, charge, practice).
- Version used: v1 (as given). Title from the abs page: "Flux-tunable global and local superconductivity in a topological insulator nano-SQUID". Authors: Nikodem, Schluck, Papaj, Geier, Bagchi, Fu, Legg, Ando. Submitted 18 Aug 2026.

## What I read
- skill/SKILL.md, skill/report-template.md, library/lookalikes.yaml (all entries and `checks`), once at the start.
- Local copies provided by the caller: abs.html (title, authors, abstract, comments "Main text: 8 pages, 4 figures. SM: 7 pages, 5 figures"), paper.txt (whole main text, Methods and SI S1.A to S1.G). For quote checking I re-extracted the PDF with `pdftotext` (reading order), because paper.txt interleaves the two columns. All 20 quotes in the report matched verbatim after whitespace and hyphenation normalization.
- Figures: read from captions and text only. Axis labels in the text extraction are partly garbled, so the ranges below come from the readable tick labels and may be off.
- No ancillary files on the abs page, so read_mtx.py was not run.
- Data repository: Zenodo 10.5281/zenodo.21988906. Not fetched, because the run limited fetches to arxiv.org, export.arxiv.org and api.openalex.org. Device and dataset counts come from the paper only.
- Nothing failed to open.

## Claims table (step 1)
| Claimed signal | Figures | Devices | Counts and ranges |
|---|---|---|---|
| Ic oscillations with h/2e period, near-complete revival at integer flux (surface-dominated supercurrent) | 1e, 3a, S2a | A, B, C | Ic ramped up from zero (Fig. 1e caption). Bx roughly -4 to 4 T (Φ/Φ0 -4..4 in device B; -3/2..3/2 in C). T about 30 mK base, no T series. |
| Diode effect, η ≈ 20%, sign reversal at half-integer flux | 1e, 3a, S2a, S4 | A, B, C | S4: VG about -75 to 25 V, Bx 0 to 4 T (B, C). Device C irregular at high Bx. "in all examined devices" (p. 4), with no total. |
| Spectral jump and ZBP appearing at the transition in device A, persisting over a large Bx range | 1f-g, S1 | A (single TJ) | VG = 10 V main; S1 at VG = -10, 0, 20 V; Bx about -6 to 6 T in S1; gate range limited by a leaky dielectric. |
| Local spectral jumps at both ends aligned with Ic anomalies | 3b-c, S2b-c | B, C | Bx 0 to 4 T. |
| Nonlocal jumps at expected boundaries, plus extra jumps at high flux | 3d-e, S2d-e, S5 | B, C | S5: VG -40 to 40 V. Corrected for line impedance (Martinez et al. formalism); line resistances from two-terminal cryostat-line measurements; values not given. |
| ZBPs in topological and trivial windows, incl. zero field; end-to-end correlation via sign of third derivative | 4, S3 | B, C | Gate maps at Bx = 0, 1, 2 T (B) and 0, 2.5, 4 T (C), VG -30 to 30 V, Vb ±500 µV; Fig. 4l fractions vs Bx 0 to 4 T. Device C: ZBP "mostly absent" in field sweeps (S2) but correlated peaks rise in the first topological lobe (S3). |

- Devices: A (first generation, one working TJ), B and C (two TJs). Table S1: A d=21 nm, W=70 nm, L=1.9 µm; B 36/70/1.3; C 16/80/2.5.
- Missing counts: devices fabricated, devices measured, other one-probe devices, cooldowns, field-angle ranges, temperature dependence. Tunnel-junction yield is stated only as "below 50%". Tunnel contacts are typically over 100 kΩ.

## Entries matched and adapted
- Matched (15): abs-quantum-dot, kondo-resonance, disorder-induced-zbp, crowded-trivial-subgap-states, quasi-majorana-smooth-confinement, spin-orbit-length-pinning, full-shell-flux-andreev, weak-antilocalization, transparent-junction-pi-crossing, one-end-only, local-probe-loophole, trivial-andreev-band-gap-reopening, diode-vortex-screening, protocol-parameter-sensitivity, fine-tuning-and-selection.
- Adapted:
  - full-shell-flux-andreev: this is a columnar Nb sandwich, not a full shell, but its flux-periodic lobes and "superconducting shell" (Fig. 1b caption) make the junction-dot mechanism analogous.
  - transparent-junction-pi-crossing: a shapiro-family entry, applied to ZBPs expected at phase π.
  - protocol-parameter-sensitivity: applied to the automated end-to-end correlation classifier in Fig. 4l, which is not a pass/fail protocol.
  - diode-vortex-screening: the paper reads the diode reversal as a ground-state phase jump, not finite-momentum pairing.
- Skipped (13):
  - fine-tuned-plateau and series-resistance-subtraction: no quantized height is claimed. The raw-conductance check was still walked.
  - micromagnet-stray-field: no magnets, and the paper reads zero-field ZBPs as trivial.
  - exceptional-point-zero-mode: tunnel contacts over 100 kΩ keep lead coupling weak. Its both-ends concern is covered by the other entries.
  - island-states-coulomb-spacing: no island.
  - chiral-plateau-superconductor-short: no QAH film.
  - shapiro-landau-zener, shapiro-nonlinear-resistance, switching-jump-blind-region: no microwave data.
  - field-enhanced-supercurrent-resonances: Ic revives "almost complete" at integer flux. The paper reports no supercurrent above its zero-field value.
  - charge-trap-fractional-shift, coulomb-dominated-interferometer: no fractional-charge claim.
  - false-poor-mans-majorana: no dot chain.
- Checks walked: zbp (6) and practice (3). The library has no checks for the diode, supercurrent or nonlocal families.

## Hold-out
- Checked every library source date against the paper date (18 Aug 2026). Only Legg 2025, arXiv 2502.19560, has a version after it: v2 is dated 21 Oct 2026.
- I fetched the v2 PDF and searched for "2608", "nano-SQUID", "Nikodem", "topological insulator" and "BiSbTeSe". No hits, so the source was kept. None of its quotes were used in the report.
- No sources were held out.
- Henry Legg is an author both of the paper under review and of library sources (2502.19560; Hess et al. 2210.03507). The paper cites the published Legg comment ([14], Nature 654, E22) and Hess et al. [12]. The hold-out rule doesn't cover author overlap or the paper citing a source, so both were kept.

## Related work, how each was checked
- Souto, Leijnse, Schrade, 2205.04469. Abs page: ID, title and first author confirmed. Full text: requirement (1), "The external flux should not be an integer multiple of the half flux quantum", after which the diode effect vanishes.
- Ciaccia et al., 2304.00484. Abs page confirmed. Full text: SM Sec. SIV, "The sign of the diode efficiency is mirrored with respect the magnetic field value corresponding to half flux quantum when the critical current asymmetry α between the two junctions changes sign."
- Valentini et al., 2008.02348: abs page and abstract.
- Hess et al., 2210.03507: abs page and abstract.
- Hou et al., 2205.09276: abs page and abstract.
- arXiv API search used once (ti:"Josephson diode" AND ti:interferometers); about 3 s waits between calls; no rate limiting.

## Library gaps
1. An ordinary interferometer diode: two junctions with skewed, unequal CPRs in a SQUID give an Ic modulation with period Φ0 and a diode effect that changes sign at multiples of Φ0/2, with flux as the only time-reversal breaking (Souto 2022; Ciaccia 2023 experiment). It is a lookalike for "global" topological signatures in nano-SQUIDs and other flux-driven phase platforms. Suggested control: fit with a trivial skewed-CPR SQUID model and identify features that need the topological junction spectrum.
2. No `checks` for the diode, supercurrent or nonlocal families.

## Unsure
- disorder-induced-zbp: the paper itself concludes disorder likely causes some ZBPs. "Partly addressed" fits poorly; I used it because the paper discusses the lookalike.
- The outside lookalike is marked "not addressed". The paper's argument links the phase jump to topology through its TI-junction model (p. 2), and it may have addressed trivial interferometers in its ref. [28] (not read).
- transparent-junction-pi-crossing and weak-antilocalization: physics-based matches, applicability uncertain.
- Figure ranges come from garbled tick labels.
- I did not recognize the paper (it is after my training data). I know of its precursor 2412.07993 only by citation and did not use it.

## Skill issues
1. The status scale has no option for "the paper concludes the lookalike likely applies" (disorder-induced-zbp here).
2. Output path: the skill says reports/<id>.md and reports/<id>.notes.md. The run asked for eval/runs/..., and I followed the run.
3. The template's "<n> known lookalikes" doesn't say whether n is the library total or the matched count. I used the total (28).
4. The template table has no place for an outside row's source URL. I put it in the Lookalike cell.
5. It is unclear whether the checks list counts toward the 600 to 900 words "outside the table".
6. The scope rule asks for a sentence under "What this is" only when the measurement type differs. It is unclear whether partial adaptation within scope needs one. I added one.
7. The skill says to read the paper from arxiv.org URLs. The run gave local copies, and I used them. paper.txt was in column-interleaved layout, so verbatim quoting needed a reading-order re-extraction. The skill doesn't mention this.
8. The skill says to use a linked data repository if reachable, but the run limited fetch hosts. I didn't fetch Zenodo.
9. The hold-out rule doesn't cover author overlap between the paper and library sources.
10. Page numbering for SI pages is unspecified. I used "p. S1" to "p. S6".
