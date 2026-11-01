# Run notes: arXiv 2608.17404v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (28 entries). Skill and template read once at the start.
- What I read: the extracted text of v1 (main text, Methods, Supplementary S1.A-G) from the provided paper.txt. No PDF and no abstract page were provided. Following the task, I did not fetch either. Figure details come from captions and the garbled axis text. The title comes from the paper text (no abstract page to check it against). Header says v1 per the arXiv stamp in the text.
- Data repository: Zenodo 10.5281/zenodo.21988906 is cited. Not opened, so no device or dataset counts from it.
- Recognition: I did not recognize this paper or know any later history.

## Claims table (step 1)

| Claim | Figures | Devices | Counts and ranges |
|---|---|---|---|
| h/2e Ic oscillations with near-full revival, surface dominated | 1e, 3a, S2a | A, B, C | A: Bx about ±6 T (S1); B, C: about ±4 T. d/W/L in Table S1 |
| Diode sign reversal at half-integer flux, η about 20% (A) | 1e, 3a, S2a, S4 | A, B, C | S4: VG about -75 to +25 V, Bx 0-4 T for B and C |
| Local spectral jumps at Ic minima; ZBP appears at the diode reversal in A, persists, gone at 2Φ0 | 1f-g, S1 | A (single TJ) | A: VG = 10 V main, plus three other VG in S1 (caption says -10, 0, 20 V; panel c text reads 10 V, a possible mismatch or lost minus sign) |
| Both-end spectra show jumps at Ic anomalies | 3b-c, S2b-c | B, C | C: "zero-bias conductance peak was mostly absent" |
| Nonlocal jumps at expected phase boundaries | 3d-e, S2d-e, S5 | B, C | S5: VG ±40 V, bias ±1 mV |
| ZBPs in both topological and trivial windows, at zero field too; correlation analysis by sign of third derivative | 4, S3 | B, C | B: Bx = 0, 1, 2 T slices, VG ±30 V, bias ±500 µV; C: 0, 2.5, 4 T |
| Device counts | Methods, S1.E | | "a series of devices with two functioning tunnel contacts", only B and C shown; "all examined devices" not counted; TJ yield "below 50%"; devices fabricated, measured and cooldowns not given |
| Temperature | Methods | | about 30 mK base only; no temperature series |

Missing counts: total devices fabricated and measured, cooldowns, field-angle range, temperature range, per-junction tunnel resistance.

## Entries matched, skipped, adapted

- Matched: abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, one-end-only, local-probe-loophole, exceptional-point-zero-mode, trivial-andreev-band-gap-reopening, diode-vortex-screening, fine-tuning-and-selection, plus two adapted entries.
- Adapted: full-shell-flux-andreev (the nano-SQUID has flux through the wire cross-section and an expected topological phase at odd flux, as in full-shell wires; the lookalike is dot Andreev levels in the tunnel region); protocol-parameter-sensitivity (applied to the automated end-to-end correlation classifier of Fig. 4l and S3l, which is a sign-only classification and not a pass/fail topological protocol).
- Skipped: fine-tuned-plateau and series-resistance-subtraction (no quantized-plateau claim; the series-resistance point is still raised through check 6 and question 5); micromagnet-stray-field (no magnets); spin-orbit-length-pinning (written for a Rashba semiconductor normal segment; TI surface states have no matching spin-orbit length, and field acts mainly through flux); island-states, shapiro-*, transparent-junction-pi-crossing, switching-jump, charge-*, coulomb-dominated-interferometer, chiral-plateau, false-poor-mans-majorana (signal types absent); field-enhanced-supercurrent-resonances (the signature is supercurrent growing with field read as triplet pairing; here Ic oscillates and revives, read as a phase jump. Closest unused entry.)
- Checks walked: zbp family (6) and practice (3). No check lists exist for diode, supercurrent or nonlocal-only signals.

## Hold-out

No library source held out. I grepped the full text of the two newest-version sources (2502.19560 v2, 2501.18631 v2) for the arXiv ID, "nano-SQUID", "Nikodem" and the title: no hits. The other matched sources predate August 2026. Henry Legg, an author here, is an author of library sources (Hess et al. 2023, Legg 2025). That is not a hold-out under the rule, which covers sources discussing this paper.

## Related work checks

All five: arXiv abstract page opened (arxiv.org/abs), ID, title and first author confirmed; also checked through the export.arxiv.org API.
- 2304.00484 Ciaccia: abstract plus full text (PDF v5). Checked the Fig. 3 caption quote "η = 0 independent on any other parameters" and the appendix on the sign mirroring about half a flux quantum.
- 2205.04469 Souto: abstract plus full text (requirement (1): the effect vanishes at Φ = nΦ0/2).
- 2008.02348 Valentini: abstract.
- 2210.03507 Hess: abstract.
- 1902.02773 Chen: abstract.

## Library gaps

- Ordinary SQUID interferometer diode (outside row, source 2304.00484, theory 2205.04469): any asymmetric two-junction loop with non-sinusoidal CPR gives Φ0-periodic Ic and a diode efficiency that is zero at half a flux quantum and changes sign there. The ground-state phase jump at Φ0/2 is generic to such loops. The global signatures in this paper therefore share symmetry-enforced features with trivial interferometers. Suggest a library entry under diode or supercurrent, and a check list for those families.
- No check list for diode, supercurrent or nonlocal families.
- No entry for automated classifiers that use sign-only thresholds (adapted protocol-parameter-sensitivity).

## Unsure

- Whether the Fig. S4 back-gate maps count as "asymmetry gated through its sign change" (marked part: the gate is shown, the sign mirroring is not discussed).
- Diode-vortex-screening: periodic reversal at Φ0(n+1/2) over several periods may by itself separate Meissner or vortex effects. The paper does not conclude against vortex screening as the diode's origin (it assumes no Meissner effect in simulations), so I kept "Tested in part".
- Exceptional point: I counted the localisation-length estimate as an argument against overlap.
- Disorder-induced, crowded and similar ZBP rows: the paper concludes toward the lookalike, so "Ruled out" cannot apply. I used "Tested in part" since tests are shown.
- Tunnel resistance mismatch (Figs. S1, S2b colour scales near 1-2 e^2/h versus ">100 kΩ" typical) comes from colour-bar text in the extraction. Raised as a question only.
- Device A, Fig. S1: the caption gives VG = -10, 0, 20 V, but a panel label reads 10 V. Possibly an extraction artifact; not raised.

## Skill issues

- The skill assumes a paper that claims a topological signature. This paper claims global signatures and reports its ZBPs as ambiguous. The status rules have no slot for "the paper concludes in favour of the lookalike". I used "Tested in part" with the authors' quote.
- "Code and every dataset published" is a disclosure, yet the rule says a test counts only when a measurement or analysis is shown. It is unclear how to mark a data-availability statement (I used part).
- The step 7 instruction to write files conflicts with this run's instruction to return text; I followed the run instruction.
- Page numbers for the supplement are ambiguous (separate numbering). I used "Suppl. p. N".
