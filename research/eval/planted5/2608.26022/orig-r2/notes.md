# Run notes: 2608.26022v1

- Library: lookalikes.yaml meta.version 0.5 (updated 2026-10-24), 28 entries. Read once at the start along with SKILL.md and report-template.md.
- Read: the extracted paper text only (main text pp. 1 to 16, supplement pp. 1 to 17, figures taken from captions; the S1, S2 and S3 axis text was partly readable). Per the test instructions there was no PDF and no abstract page, and I did not fetch the paper. The title in the report header is from the paper text. One arXiv API search (abs:"diode" AND abs:CsV3Sb5) returned the paper's own entry (2608.26022v1, matching title, abstract snippet). I did not open it or use it beyond seeing that the title matches.
- No ancillary figure data. Data are "available from the corresponding author upon reasonable request" (p. 9). read_mtx.py not used.
- I did not recognize this paper and know nothing of its later history.

## Claims table (step 1)

| Claim | Figures | Devices | Counts and ranges |
|---|---|---|---|
| No field-free diode in pristine CsV3Sb5 | Fig. 1e,f; Figs. S1, S2; Table S1 | Devices 1 to 10, hBN-encapsulated, top or bottom electrodes | 10 devices; d 21 to 76 nm; Ic 81.4 to 496.5 μA; η upper bound up to 0.48%; 1.8 K, zero field; in-plane R(B) to ±10 T; sweeps per device not given |
| Oxidation activates a field-free diode | Fig. 2; Fig. S3; Fig. S5 (AFM) | Device 11 (Fig. 2); Device 12 (p. 5) | 1.8 K, B = 0, 0 to ±300 μA; Ic 115 to 37 μA; η 83.61% in 1 of 3 sweeps at stage 2, 0 of 3 at stage 3, 1 of 3 at stage 4, superconductivity gone at the final stage (Supp. p. 2) |
| Etching activates a field-free diode | Fig. 3a to c; Figs. S6, S7 | Device 13 (zig-zag), Device 14 | Device 13: 0.25 to 1.5 K in 0.25 K steps, 6 sweeps each; Device 14 sweep rate 0.05 μA/s |
| Polarity and size are stochastic | Fig. 3d,e; Fig. S4; Fig. S6; Fig. S12 | Devices 12 or 13 (labels conflict), 14 | Fig. S4: 6 sweeps, η 17.07, 0, 0, 0, -30.86, -14.07%; S12: 2 sweeps, 4 biases (68 to 74 μA), about 20 min each |
| Field training stabilizes polarity, then amplitude | Fig. 4; Figs. S10, S11 | Device 13, Device 14 | Out-of-plane -0.2 to 0.2 T, 9 sweeps per field (step count not given); in-plane 0.3 T stabilizes and 0.2 T doesn't (S10) |
| Not erased by field cooling | Figs. S8, S9 | Device 14 | 1 T out-of-plane and 1 T in-plane field cools |
| No diode when the CDW is suppressed | Figs. S13, S14 | Device 15 (oxidized, 3 stages), Device 16 (etched) | x = 0.24; EDS, R(T) without a CDW kink; η upper bound about 0.1% (S14); Tc, Ic, temperature and field not given |

Missing counts: the number of oxidized or etched devices fabricated, sweeps per pristine device, field step size in Fig. 4, and Ti-doped Tc and Ic.

Internal inconsistencies noted (raised in question 1 or listed here):
- p. 5 attributes the -30.86% and 17.07% sweeps to Device 12 (oxidized) "(Figs. S3 to S5)". The Fig. S4 caption and the supplementary text call that device Device 13, which the main text uses for the etched zig-zag device.
- Fig. S3 is captioned "Device 12 (Fig. 2 in the main text)", but Fig. 2 is Device 11.
- p. 5 says "The same field-induced evolution is observed in Device 14 (Figs. S10 and S11)", but S10 uses an in-plane field and Fig. 4 an out-of-plane field.
- The Fig. S12 caption puts "the stochastic diode behavior in the main text" at 66 to 74 μA for Device 14, while the main-text stochastic figures are Device 13.
- p. 6 says the Ti-doped inversion breaking used "the same fabrication protocol used for the pristine devices". The Figs. S13 and S14 captions say oxidation and etching.
- The Fig. S10 caption calls Hc1∥ ≈ 0.59 T "much larger" than 0.3 T, a factor of about 2. I checked the arithmetic: ξ = 19.7 nm and Hc1∥ = 0.59 T both reproduce.
- The S4 η values reproduce from the quoted Ic+ and Ic-.
- The Figs. S1 and S2 captions say "Table 1" for Table S1.

## Entries matched, skipped and adapted

- Matched: diode-vortex-screening (adapted: the claim is CDW-linked TRS-breaking domains; the entry's signature says finite-momentum or exotic pairing, but the physics matches). fine-tuning-and-selection (always).
- Skipped, because the device has no tunnel probe, nanowire, dot, quantum Hall edge, Shapiro measurement or protocol: abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, fine-tuned-plateau, series-resistance-subtraction (no quantized value), one-end-only, trivial-andreev-band-gap-reopening, micromagnet-stray-field (no magnets near the device; its signature is a ZBP), full-shell-flux-andreev, protocol-parameter-sensitivity (no automated pass/fail protocol), chiral-plateau-superconductor-short, island-states-coulomb-spacing, shapiro-landau-zener, shapiro-nonlinear-resistance, field-enhanced-supercurrent-resonances (the claim isn't field-enhanced supercurrent), charge-trap-fractional-shift, spin-orbit-length-pinning, exceptional-point-zero-mode, transparent-junction-pi-crossing, switching-jump-blind-region, false-poor-mans-majorana, local-probe-loophole, coulomb-dominated-interferometer.
- Checks: the library has no `checks` block for the diode family, so only the practice checks (report-counts, report-ranges, report-processing) were walked.

## Sources held out

None. The library sources (Hou 2205.09276, Frolov 2309.09368, Akrap 2501.18631 v2, Legg 2502.19560 v2 and the ZBP and Shapiro sources) are about other systems and predate or are unrelated to an August 2026 kagome diode paper. I did not reopen their full texts to confirm they don't cite it.

## Related work checks

All five abstract pages were opened on arxiv.org (abstract only). ID, title and first author were confirmed, and each one-line description matches the abstract:
- 2205.09276 Hou (abstract)
- 2205.12196 Golod (abstract)
- 2309.00264 Le (abstract)
- 2605.29665 Zhang (abstract)
- 2606.20157 Rog (abstract)

Seen in searches and not used:
- 2609.38003 (Krizek, antiferromagnet-controlled diode, later)
- 2610.30556 and 2610.16972 (FePt stray-field diodes)
- 2508.12056
- 2508.15266
- 2210.11256

Ge et al. (ref. 39, "normal state field trainability" in CsV3Sb5) was not found on arXiv in my searches and is not listed.

## Library gaps

- Trapped Abrikosov vortex or remanent magnet field at nominal zero field, giving a zero-field diode with switchable polarity. Source: Golod and Krasnov, https://arxiv.org/abs/2205.12196, abstract: "we can easily change the diode polarity and switch nonreciprocity on/off by changing bias configuration and by trapping/removing a vortex." Added as an outside row; its tests come from that control (trap or remove the vortex, set or clear the field at the sample).
- Sweep-to-sweep switching-current jitter making η from single paired sweeps take random sign. I found no arXiv paper showing this for diode measurements (several API and website searches), so per the skill it is not a table row. It went in as the one question no entry raises (question 8).
- The diode family has one entry and no `checks` block. Diode papers would benefit from checks such as: remanent field measured; η odd in B with its zero located; control film of the same geometry; switching statistics for both polarities.

## Status judgments I was unsure of

- diode-vortex-screening, test 1. The pristine and Ti-doped devices are controls of the parent material, but only at nominal zero field. The field-training evidence (Fig. 4) has no field-dependent control, so "part".
- Outside row, field-history test: marked "part" because Figs. S8 and S9 (Device 14 only) vary the field-cool history, though only at 1 T.
- fine-tuning-and-selection, "second device shown": "all", since each route (oxidation, etching, field training, Ti control) has two devices.
- Practice checks: all three marked "partly". report-processing gives the η definition but not the onset extraction, and has no data or code.

## Skill issues

- The skill tells you to read the abstract page and search arXiv. The test forbade fetching the paper, and a topical API search returned the paper's own entry anyway. The skill has no guidance for this, nor does the hold-out rule cover search results about the paper itself.
- The scope rule says to adapt entries for non-topological measurements, but the diode family is in the library while the template's "What this is" text says "topological transport". It is unclear how much to rephrase. I added one sentence.
- With no `checks` block for a family, the skill doesn't say whether to stop at the practice checks or adapt checks from entries. I stopped at practice.
- Step 3 says to judge only "the evidence the paper presents". It doesn't say whether control samples (here pristine and Ti-doped devices) count as evidence for a test like "plain film of the parent superconductor" when they were measured under different conditions.
- No home is given for an unsourced alternative explanation beyond the single "question no entry raises". This paper had two candidates; one was sourced and one wasn't.
- The flags shape requires questions verbatim from the report. The skill's questions often merge the four standard questions with paper-specific detail, and it is unclear whether merging is allowed. I merged.
