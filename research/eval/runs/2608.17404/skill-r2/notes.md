# Run notes: arXiv 2608.17404v1

## Library and inputs
- Library: lookalikes.yaml, meta.version 0.4 (updated 2026-10-23), 28 lookalikes, plus the checks for the zbp, shapiro, kitaev, charge and practice families. I read SKILL.md, report-template.md and the library once at the start.
- Paper: arXiv 2608.17404v1, "Flux-tunable global and local superconductivity in a topological insulator nano-SQUID", Nikodem et al. (8 authors, submitted 2026-08-18). I used the local copies: the abstract page (abs.html), the extracted text (paper.txt) and the PDF. I did not fetch the paper. The PDF has 16 pages: main text pp. 1-9, Supplementary Information pp. 10-16. Report page numbers are PDF pages.
- paper.txt is a two-column layout extraction with interleaved columns. To check quotes I ran pdftotext on the local PDF in reading order and confirmed that every quote in the report appears on the page cited (whitespace and hyphenation normalized).
- I rendered PDF pages 2 and 3 to read the field axes: device A spans Bx from -6 to 6 T (about -2.5 to 2.5 flux quanta), device B spans about -4 to 4 T (-4 to 4 flux quanta).
- Data repository: the paper gives Zenodo 10.5281/zenodo.21988906. I did not open it, because the run instructions limited fetches to arxiv.org, export.arxiv.org and api.openalex.org. No ancillary files on arXiv, so read_mtx.py was not used.
- Recognition: I did not recognize this paper. It postdates my training data, so I have no outside knowledge of its later history. One author (H. F. Legg) also wrote library source 2502.19560 and co-wrote 2210.03507. That is not a hold-out trigger by itself.

## Claims table (step 1)
| Claim | Figures | Devices | Counts and ranges |
|---|---|---|---|
| h/2e Ic oscillations with near-full revival at integer flux, read as surface-dominated supercurrent and a ground-state phase jump | Fig. 1e, 3a, S2a | A, B, C | Bx about -6 to 6 T (A), about -4 to 4 T (B), 0 to 4 T region (C); base about 30 mK only; Ic ramped up from zero |
| Diode effect, eta about 20% (A), sign reversal at half-integer flux | Fig. 1e, 3a, S2a, S4 | A, B, C | S4: VG -75 to 25 V, Bx 0 to 4 T for B and C |
| Local spectral jumps at the transition fields; device A ZBP appears in the first expected topological window and persists, splits in the 2-flux-quantum lobe | Fig. 1f-g, 3b-c, S1, S2b-c | A (one probe), B, C | Device A at VG = -10, 0, 10, 20 V (S1); gate range limited by a leaky dielectric |
| Nonlocal conductance jumps at the expected phase boundaries, plus extra jumps at high flux | Fig. 3d-e, S2d-e, S5 | B, C | S5: VG about -40 to 40 V |
| ZBPs in trivial lobes and at zero field, end-to-end correlation alike in both regimes, read as at least partly disorder | Fig. 4, S3 | B, C | Fig. 4 at Bx = 0, 1, 2 T, VG -30 to 30 V, Vb -500 to 500 uV; Fig. 4l Bx 0 to 4 T; S3 at 0, 2.5, 4 T |
| Device dimensions | Table S1 | A, B, C | d = 21, 36, 16 nm; W = 70, 70, 80 nm; L = 1.9, 1.3, 2.5 um |

Missing counts: devices fabricated, devices measured, cooldowns and datasets are not given. The paper says the global signals appear in "all examined devices" (p. 4), that a "series of devices" with two working probes was made, and that tunnel-junction yield is "below 50%" (p. 5). Only A, B and C are shown. There is no temperature dependence, and field angle is varied only for alignment.

## Families, entries matched, skipped and adapted
- Families walked: zbp checks (6) and practice checks (3). The diode and nonlocal families have no checks in the library.
- Matched as written: abs-quantum-dot, kondo-resonance, disorder-induced-zbp, crowded-trivial-subgap-states, quasi-majorana-smooth-confinement, one-end-only, local-probe-loophole, trivial-andreev-band-gap-reopening, diode-vortex-screening, fine-tuning-and-selection.
- Adapted (one sentence in "What this is"):
  - transparent-junction-pi-crossing: this is a shapiro-family entry. Here the topological reading rests on each junction's phase passing pi, and the device A ZBP appears at the half-flux jump.
  - full-shell-flux-andreev: this geometry is a sandwich nano-SQUID, not a full shell. Flux-tunable Andreev levels near the probe can still give ZBPs in odd flux lobes.
  - series-resistance-subtraction: applied to the line-resistance correction of the nonlocal matrix, since no quantized value is claimed.
  - protocol-parameter-sensitivity: applied to the automated end-to-end correlation count in Fig. 4l.
- Skipped:
  - weak-antilocalization: tunnel contacts are above 100 kOhm, the peaks are far below e^2/h, and the zero-field peaks are outside class D.
  - fine-tuned-plateau: no quantized plateau is claimed.
  - micromagnet-stray-field: there are no magnets.
  - spin-orbit-length-pinning: needs a Rashba normal segment with reduced g factor, which doesn't match this device. I was unsure here.
  - exceptional-point-zero-mode: needs strong coupling to the lead, and the barriers here are weak tunnel barriers.
  - chiral-plateau-superconductor-short, island-states-coulomb-spacing, charge-trap-fractional-shift, coulomb-dominated-interferometer, false-poor-mans-majorana: different device types.
  - shapiro-landau-zener, shapiro-nonlinear-resistance, switching-jump-blind-region: no microwave data.
  - field-enhanced-supercurrent-resonances: Ic oscillates with flux, and no growth above the zero-field value is claimed.

## Status choices I was unsure of
- one-end-only: devices B and C measure both ends, but the device A first-window ZBP is one-ended, so I chose Partly addressed (the weaker status).
- zbp-both-ends: Partly for the same reason.
- disorder-induced-zbp: the paper itself proposes this explanation. "Ruled out" does not fit, and neither status describes "adopted by the authors" well. I chose Partly addressed.
- kondo-resonance: the zero-field gate maps bear on it only weakly, and Kondo is not discussed, so I chose Not addressed (the weaker status).
- zbp-dot-search: Not done. The data could show dots but the paper does not analyze them for that.

## Sources held out
None. All library sources predate this paper except two that have later versions. I downloaded the full text of both and searched for "2608", "nano-SQUID" and "Nikodem", with no hits:
- 2502.19560v2, submitted 2026-10-21;
- 2501.18631v2, submitted 2026-03-25.
The Frolov quotes come from the 2023 preprint v1.

## Related work: how each was checked
- 2306.12765 (Greco, Pichard, Giazotto 2023): abstract page opened, ID, title and first author confirmed; full text read for the eta(Phi) passage (p. 4). This is also the source for the outside lookalike.
- 2208.10856 (Fominov, Mikhailov 2022): abstract page confirmed; the full text was searched to confirm that the asymmetry vanishes at integer and half-integer flux.
- 1906.01179 (Dartiailh et al. 2019): abstract page confirmed (abstract only).
- 2008.02348 (Valentini et al. 2020): abstract page confirmed (abstract only).
- 2210.03507 (Hess, Legg, Loss, Klinovaja 2022): abstract page confirmed (abstract only).
- Considered but not listed: 2205.04469 (Souto, Leijnse, Schrade 2022), abstract opened, a theory of interferometer diodes; I kept to five.

## Library gaps
- No entry for a trivial interferometer diode: a SQUID of ordinary non-sinusoidal junctions gives a flux-tunable diode, with a sign reversal at half-integer flux and eta near 20% (2306.12765, 2208.10856). Added as "(not in library)".
- No entry for spectral jumps that follow from any SQUID ground-state phase jump. Every Andreev level shifts when the phase jumps, whatever the topology. I found no paper to cite, so it is only raised in question 8.
- No checks for the diode, nonlocal or "global phase-transition" signals. This paper's main evidence falls outside the check families.
- The end-to-end correlation metric (sign of the zero-bias curvature at both ends while a shared back gate is swept) may correlate by construction. The library has no entry on correlation baselines or nulls.

## Skill issues
- Step 3 says to walk "the checks for the paper's family", but this paper spans several families (zbp, nonlocal, diode, practice), and some of them have no checks. The skill doesn't say what to do then.
- Statuses assume the paper offers each signal as evidence. When the paper itself raises a lookalike as its explanation (disorder ZBPs), neither "ruled out" nor "partly addressed" fits cleanly.
- The skill doesn't say whether a check done in some devices only (both ends in B and C, not A) counts as Done or Partly.
- No convention for page numbers in a Supplement with its own numbering. I used PDF pages and said so.
- The template's table has no column for an outside row's source URL. I put it in the lookalike cell.
- The data repository rule ("if you can reach it") conflicts with run-level fetch limits. I followed the run limits.
- The word target (600 to 900 outside the table) is hard to meet with nine checks, eight questions and five related-work items. This report is about 970 words outside the table.
- The template's first question has one "<the effect>" slot; this paper has several effects (Ic oscillations, diode reversal, ZBPs).
