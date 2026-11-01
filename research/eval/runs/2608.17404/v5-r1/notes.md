# Run notes: arXiv 2608.17404v1

AI only. Library version 0.5 (meta.version), 28 lookalike entries. Run date 2026-10-24.

## What I read
- skill/SKILL.md, skill/report-template.md, library/lookalikes.yaml (entries, tests, checks).
- Paper: the local abs.html (title, authors, date 2026-08-18, abstract), paper.txt (full main text, Methods and Supplementary Information S1.A to S1.G), and the PDF pages rendered to images for Figs. 1, 2, 3, 4 (pp. 2 to 4) and Figs. S2, S3, S5 (Suppl. pp. 3, 4, 6). I did not fetch the paper online.
- No arXiv ancillary files are listed on the abstract page, so read_mtx.py was not used.
- Data repository: the paper cites Zenodo 10.5281/zenodo.21988906. I did not open it (the run prompt limits fetches to arXiv, export.arxiv.org and OpenAlex), so counts come from the paper only.
- I did not recognize this paper (it postdates my training data). I know the group's earlier nano-SQUID preprint 2412.07993 only through its citation here; I didn't use outside knowledge of the result.

## Claims table (step 1)
| Claimed signal | Figures | Devices | Counts and ranges |
|---|---|---|---|
| Ic oscillations with h/2e period, near-full revival at integer flux | Fig. 1e, 3a, S2a | A, B, C | Bx about -4 to 4 T (A up to about 2.5 flux quanta); 30 mK base; one field direction (axial), alignment by Fraunhofer compensation (S1.B) |
| Diode efficiency about 20% reversing at half-integer flux | Fig. 1e, 3a, S2a, S4 | A, B, C | S4: VG -75 to 25 V, Bx 0 to 4 T (B, C); current always ramped from zero |
| Local spectral jumps at the reversal fields; ZBP in the first odd window in A | Fig. 1f-g, S1, 3b-c, S2b-c | A (one probe), B, C | A: Bx -6 to 6 T at VG = 10 V, and -10, 0, 20 V (S1); A gate range limited by leaky dielectric |
| Nonlocal jumps at phase boundaries | Fig. 3d-e, S2d-e, S5 | B, C | Bx -4 to 4 T (B), 0 to 4 T (C); S5 VG -40 to 40 V at an unstated field |
| ZBPs in both topological and trivial windows, incl. zero field; end-to-end correlation | Fig. 4, S3 | B, C | VG -30 to 30 V (B) and -40 to 40 V (C) at Bx = 0, 1, 2 T (B) and 0, 2.5, 4 T (C); Fig. 4l and S3l Bx 0 to 4 T |
Missing counts: devices fabricated, devices measured, cooldowns, number of datasets; only "yield of functional tunnel junctions ... below 50%" and "all examined devices". No temperature dependence. Dimensions in Table S1 (L 1.3 to 2.5 um, W 70 to 80 nm, d 16 to 36 nm).

## Matching (step 2)
Matched: fine-tuning-and-selection, diode-vortex-screening, trivial-andreev-band-gap-reopening, disorder-induced-zbp, crowded-trivial-subgap-states, abs-quantum-dot, transparent-junction-pi-crossing, quasi-majorana-smooth-confinement, one-end-only, local-probe-loophole, full-shell-flux-andreev (adapted), kondo-resonance, weak-antilocalization. Plus one outside row.
Adapted: full-shell-flux-andreev. The device is a TI wire between two Nb electrodes, not a full-shell wire, but the mechanism (flux-tunable Andreev levels near the probe giving ZBPs in odd flux windows) carries over; I read "junction region" as the TI segment under the tunnel probe. transparent-junction-pi-crossing is in the shapiro family, but its signature (zero crossing at phase pi) matches the Fu-Kane line-junction picture here.
Skipped: fine-tuned-plateau and series-resistance-subtraction (no quantized height claimed; peaks 0.2 to 1.7 e^2/h), though the zbp-raw-conductance check was walked; micromagnet-stray-field (no magnets); spin-orbit-length-pinning (Rashba normal-segment mechanism; peak not offered as field-pinned evidence); exceptional-point-zero-mode (tunnel-coupled probes, peaks not offered as robustly pinned); protocol-parameter-sensitivity (no pass/fail protocol; the correlation-threshold issue goes into question 7); island, shapiro (other than the pi crossing), supercurrent, charge, chiral, kitaev entries (no such signals).
Checks walked: zbp family and practice. Shapiro, kitaev and charge checks don't apply. No diode checks exist.

## Statuses I was unsure of
- diode-vortex-screening: the flux period scaling with cross-section (A versus B) by itself separates a flux-periodic diode from a Nb screening diode, but the paper doesn't discuss screening, so the "concludes against" condition fails; marked Tested in part.
- Outside SQUID row, test 1 marked part because Fig. S4 maps eta against VG but the paper doesn't link VG to the junction asymmetry.
- transparent-junction-pi-crossing: gate dependence is shown in all three devices, but the paper doesn't conclude against the lookalike, so Tested in part. In B and C the peaks vary with VG in both windows, which reads as data bearing on it either way.
- trivial-andreev-band-gap-reopening: Fig. S5 varies VG but at one unstated field, so it doesn't follow the boundary jumps; marked "no".
- Kondo: field dependence is shown, but it's an axial field dominated by orbital phase, and no Zeeman analysis is given; marked "no", note "data bear on it".
- Tunnel resistance: Methods say over 100 kOhm, but above-gap G of about 1 to 1.7 e^2/h in A and C implies roughly 15 to 25 kOhm. I may be misreading the two-terminal configuration; raised as question 6.
- Fig. S5 bias axes read in microvolts against mV elsewhere; likely a label slip; folded into question 8.

## Hold-out
No library source cites this paper (grep for the arXiv ID, "nano-SQUID" and "Nikodem" found nothing; all sources predate August 2026 or quote 2023 preprints). None skipped. Henry F. Legg, a co-author here, is an author of two library sources (Hess et al. 2210.03507 and Legg 2502.19560). Neither discusses this paper, so both stay.

## Related work and how each was checked
All five abstract pages opened on arxiv.org (ID, title, first author confirmed from citation meta tags), with the arXiv API used for the abstracts.
- 2304.00484 Ciaccia et al.: abstract plus full text (PDF). Quote for the outside row from the Fig. 3 caption: "Note, that for Φext /Φ0 = 0.5, which equals φext = π, η = 0 independent on any other parameters." The control it describes (gate-tuned asymmetry, comparison with a SQUID model from the measured junction parameters) is the source of the outside row's tests.
- 2205.04469 Souto, Leijnse, Schrade: abstract.
- 2205.09419 Banerjee et al.: abstract.
- 2210.03507 Hess et al.: abstract.
- 1910.11413 Pan and Das Sarma: abstract.

## Library gaps
- No entry for an ordinary asymmetric SQUID with non-sinusoidal current-phase relations, which gives h/2e Ic oscillations, a diode of tens of percent, eta = 0 at half a flux quantum, and phase jumps that move Andreev spectra, with no topology (Ciaccia et al. 2304.00484; Souto et al. 2205.04469). Added as an outside row.
- No checks list for the diode family or for "global" phase-transition signatures (Ic, diode, phase jumps).
- No entry for flux trapping or vortex entry in the parent superconductor producing spectral jumps that depend on sweep direction (the paper itself raises this at high field).

## Skill issues
- The skill says to write reports/<id>.md and .notes.md; this run puts them in the reply as the prompt asks.
- The skill assumes the paper offers each signal as topological evidence. Here the paper offers the global signals as evidence and itself rejects the ZBPs as Majorana evidence in B and C. It is unclear whether ZBP entries should be matched for a signal the paper disclaims; I matched them for device A's ZBP and for sorting the peaks.
- "Ruled out for the claim" requires that the paper concludes against the lookalike. When a shown test separates the lookalike but the paper never names it (diode-vortex-screening), the skill gives no route other than Tested in part.
- No "not applicable" status for a check whose knob doesn't exist in the device (zbp-transparency with a fixed oxide barrier); marked Not done.
- The skill says to use a linked data repository if reachable, but the run prompt limits hosts; the skill could say which wins.
- flags.json has no note value for "tested in part"; I used null.
