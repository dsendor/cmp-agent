# Run notes: arXiv 2608.17404v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (updated 2026-10-24), 28 lookalikes plus checks for the zbp, shapiro, kitaev, charge and practice families.
- Date of run: 2026-10-24.

## What I read
- The paper only as pre-extracted text (scratchpad paper.txt): main text, Methods, references and Supplementary Notes S1.A to S1.G with captions for Figs. 1 to 4 and S1 to S5. Per the test instructions I did not fetch the abstract page, PDF or HTML. The title comes from the text header ("Flux-tunable global and local superconductivity in a topological insulator nano-SQUID"), not from the abstract page.
- Figures: captions and the scattered axis labels in the extracted text only. I could not see color scales or the actual traces. Ranges (Bx ±4 T for B and C, ±6 T for A in S1; VG ±30 V in Figs. 4 and S3; VG -75 to 25 V in S4; Vb ±1 mV and ±500 µV) are read from axis tick labels and may be off.
- Page numbers: main text p. 1 to 7 by the page markers in the text; supplementary pages are cited as "Supp. p. N" by their own 1 to 7 numbering.
- Data repository: the paper gives Zenodo 10.5281/zenodo.21988906. I did not try to open it (the test allowed only arxiv.org, export.arxiv.org and api.openalex.org), so device and dataset counts come from the text only. No ancillary files and no .mtx data were provided, so read_mtx.py was not run.
- I did not recognize the paper (its date is after my training data). I know of the cited prior platform paper (arXiv 2412.07993) only by its listing in the references, and I did not use it.

## Claims table (step 1)
| Claim | Figures | Devices | Counts and ranges | Missing |
|---|---|---|---|---|
| Ic oscillates with h/2e period, almost full revival at integer flux (surface-state dominated) | Fig. 1e, 3a, S2a | A, B, C | A: η about 20%; current "always ramped up from zero" (A); Bx range about ±4 T (B, C) | Gate voltage for Fig. 1e and 3a; number of other devices with "all examined devices" |
| Diode efficiency reverses sign at half-integer flux, read as 0 to π phase jump into the topological phase | Fig. 1e, 3a, S2a, S4 | A, B, C | S4: VG -75 to 25 V, Bx 0 to 4 T (B, C); "largely robust against gate voltage" | Device count beyond A to C; inductance and junction asymmetry |
| Spectral jumps in local conductance at the transition fields | Fig. 1f-g, 3b-c, S2b-c | A (one probe), B, C (two probes) | A at VG = 10 V (Fig. 1f), plus VG = -10, 0, 20 V (S1) | Gate voltage of Fig. 3 |
| Nonlocal conductance jumps at the expected phase boundaries, plus extra jumps at high field | Fig. 3d-e, S2d-e, S5 | B, C | S5: VG ±40 V (field not stated) | Field for S5; quantification of matching and missing jumps |
| Device A: ZBP appears abruptly at half flux, persists over a wide Bx range, splits in the two-flux regime; stable over gate | Fig. 1f-g, S1 | A | VG -10 to 20 V (gate range limited by leaky dielectric); Bx ±6 T | Second single-probe device; cooldowns |
| Devices B, C: ZBPs at both ends in topological and trivial regimes, including zero field; end-to-end correlation fractions similar across regimes | Fig. 3b-c, 4, S2, S3 | B, C (C "mostly absent" ZBP in field sweep) | Fig. 4: Bx = 0, 1, 2 T, VG ±30 V; S3: Bx = 0, 2.5, 4 T; Fig. 4l, S3l over Bx 0 to 4 T | Method details of the third-derivative analysis; thresholds |
| Device geometry | Table S1 | A, B, C | d = 21, 36, 16 nm; W = 70, 70, 80 nm; L = 1.9, 1.3, 2.5 µm | |
| Fabrication and yield | Methods | "a series of devices" | Tunnel-junction yield "below 50%"; T base about 30 mK; tunnel resistances above 100 kΩ | Devices fabricated, measured, set aside; cooldowns; temperature dependence |

## Entries matched, skipped and adapted
- Matched: abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, one-end-only, local-probe-loophole, trivial-andreev-band-gap-reopening, diode-vortex-screening, fine-tuning-and-selection.
- Adapted: full-shell-flux-andreev (signature is for full-shell wires with ZBPs in odd Little-Parks lobes; here the TI wire is sandwiched by Nb, not fully shelled, but the device A ZBP appears in the odd-flux window and the mechanism, Andreev levels of a dot at the tunnel contact modulated by flux, carries over). transparent-junction-pi-crossing (shapiro family; adapted because the topological reading rests on a phase-π crossing in the Fu-Kane line junction, Fig. 1c, and the device A ZBP sits at the π phase). The diode family has no checks section, so the global claims were judged only through diode-vortex-screening and one outside row.
- Skipped: fine-tuned-plateau and series-resistance-subtraction (no quantized conductance claimed; the subtraction question stays under zbp-raw-conductance). micromagnet-stray-field (no magnets in the device). spin-orbit-length-pinning (mechanism needs a Rashba normal segment with a spin-orbit length; TI surface states are spin-momentum-locked Dirac states). exceptional-point-zero-mode (needs strong coupling to the lead; tunnel contacts exceed 100 kΩ). field-enhanced-supercurrent-resonances (Ic revives toward its zero-field value through interference, not growth above it). protocol-parameter-sensitivity (no pass/fail protocol is presented; the sensitivity of the Fig. 4l classifier to processing choices went into question 5 and check report-processing). island, shapiro-landau-zener, shapiro-nonlinear-resistance, switching-jump-blind-region, charge, chiral, kitaev and interferometer entries (no such signal).

## Sources held out
- None. No library source names this paper, its authors' title or 2608.17404 in its title, location or quote; all library sources predate the paper (18 Aug 2026) except arXiv v2 dates of 2502.19560 and 2501.18631, whose quoted sections concern other work.

## Related work, how each was checked
- 2008.02348 Valentini et al.: abstract via the arXiv API and the abs page citation_title and first author.
- 2210.03507 Hess et al.: abstract via API and abs page metadata.
- 1910.11413 Pan and Das Sarma: abstract via API and abs page metadata.
- 2304.00484 Ciaccia et al.: abstract via API, abs page metadata, and full text (v5 PDF) for "for Φext/Φ0 = 0.5, which equals φext = π, η = 0 independent on any other parameters" (Fig. 3 caption) and "The sign of the diode efficiency is mirrored with respect the magnetic field value corresponding to half flux quantum when the critical current asymmetry α between the two junctions changes sign." (appendix). Also used as the source for the outside row.
- 2205.09276 Hou et al.: abstract via API and abs page metadata.
- Also opened, not listed: 2205.04469 Souto, Leijnse and Schrade (abstract: diodes from interferometers with non-sinusoidal junctions, needing only flux) and 2004.08583 Yu et al. (abstract).

## Library gaps
- Ordinary asymmetric SQUID or interferometer diode effect (Ciaccia et al. 2023, arXiv 2304.00484; theory Souto et al. 2022, arXiv 2205.04469): the diode efficiency vanishes and changes sign at half flux in trivial two-junction devices, so a sign reversal at half-integer flux and h/2e Ic oscillations follow from interference alone. Tests taken from Ciaccia's controls: efficiency followed as junction asymmetry is gate-tuned; loop-inductance contribution estimated; switching measured in both directions to exclude retrapping hysteresis.
- No checks for flux-driven 0 to π phase transitions or for critical-current and diode signatures (no "diode" or "supercurrent" checks family).
- No entry for disorder-driven ZBPs at zero applied field in TI or proximitized Dirac systems; the zbp entries assume semiconductor nanowires with Zeeman-driven phases.

## Things I was unsure of
- What "the claim" is for the ZBP lookalikes. The paper presents the device A ZBP as consistent with topology but concludes that the B and C ZBPs are at least partly disorder-driven. I judged the ZBP lookalikes against the topological reading of the ZBPs. Where the authors conclude for a lookalike (disorder), the status rules give no option beyond "Tested in part".
- transparent-junction-pi-crossing test marked "part": the back gate tunes the density, but whether the junction transparency changes was not shown.
- Kondo: the field maps exist (Fig. 3b-c) but no splitting analysis, so I marked Zeeman splitting "no" and the note "data bear on it".
- Outside-row test "switching in both directions": the Fig. 1e caption states the ramp-from-zero procedure for device A only, so "part".
- disorder-induced-zbp gate test marked "all": gate dependence is shown for A (S1), B (Fig. 4) and C (S3).
- Tick-label ranges read from extracted text may be wrong.

## Skill issues
- Step 7 asks for files under reports/; this run returns them in the reply because the environment refuses .md writes from subagents.
- The skill requires the abstract page title; this test withheld the abstract page, so the title comes from the text.
- "Ruled out for the claim" requires the paper to conclude against the lookalike. The skill doesn't say what to do when the paper concludes in favor of a lookalike (here, disorder). I used "Tested in part".
- The skill doesn't say how to set statuses when a paper reports a mostly negative ZBP result with one positive example (device A); "the claim" is ambiguous in such papers.
- No guidance on whether a stated procedure (such as "the current was always ramped up from zero") counts as a test "shown".
- No guidance on whether a data repository outside the allowed hosts may be opened in restricted runs.
- When a family has no checks (diode), the skill doesn't say whether to note that in the report; I said it in one sentence under "What this is".
