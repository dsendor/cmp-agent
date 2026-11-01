# Run notes: arXiv 2608.26022v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.4 (updated 2026-10-23), 28 lookalike entries, checks for families zbp, shapiro, kitaev, charge, practice.
- Run date: 2026-10-23. AI only.

## What I read
- SKILL.md, report-template.md, lookalikes.yaml (all, including checks), once at the start.
- Paper: extracted text of v1 (main text pp. 1 to 16, Supplementary pp. 1 to 17), and the arXiv abstract page (title, 17 authors, submitted 2026-08-26, "33 pages, 18 figures"). No PDF; figure details come from captions and the few axis labels that survived extraction (for example "Iac = 10 μA, step: 0.2 μA" in Fig. S3; Ic and η values in Fig. S4).
- Page numbers: main text pages follow the "Page N of 16" footers; supplement pages follow its footer numbers, cited as "SM p. N".
- Data: "available from the corresponding author upon reasonable request" (p. 9). No ancillary files and no repository, so read_mtx.py was not used and no counts come from data.
- I did not fetch the paper itself, per instructions.
- Recognition: I did not recognize the paper (submitted after my training data).

## Claims table (step 1)
| Claim | Figures | Devices | Counts and ranges | Missing |
|---|---|---|---|---|
| Pristine hBN-encapsulated CsV3Sb5 has no field-free SDE | Fig. 1, Figs. S1, S2, Table S1 | Devices 1 to 10 (top and bottom electrodes) | 10 devices; d = 21 to 76 nm; Ic = 81 to 496.5 μA; Tc 3.80 to 4.36 K; η upper bounds 0 to 0.48%; T = 1.8 K | sweeps per device; cooldowns |
| Oxidation activates a field-free SDE | Fig. 2, Fig. S3, Fig. S5 (AFM) | Device 11 (main text) or Device 12 (Fig. S3 caption) | Ic 115 to 37 μA after first exposure; η = 83.61% at second stage; 3 sweeps per stage, 1 of 3 with SDE at stages 2 and 4, 0 of 3 at stage 3, no Ic at final stage; 1.8 K, B = 0; ±300 μA sweeps; Iac 10 μA, steps 0.2 or 0.5 μA | how many devices oxidized in total |
| Asymmetric etching activates a field-free SDE | Fig. 3a to c, Fig. S6, Fig. S7 | Devices 13, 14 | Device 14 sweep rate 0.05 μA/s | number of etched devices made |
| SDE is stochastic in sign and size | Fig. 3d,e, Fig. S4, Fig. S6, Fig. S12 | Devices 13 (and 12 per main text), 14 | 0.25 to 1.5 K in 0.25 K steps, 6 sweeps each; Fig. S4: 6 sweeps, 3 with SDE (17.07%, −30.86%, −14.07%); Fig. S12: 66 to 74 μA window, 2 μA steps, about 20 min traces | total sweeps; Ic criterion |
| Small out-of-plane field stabilizes the SDE | Fig. 4, Figs. S10, S11; field cooling Figs. S8, S9 | Devices 13, 14 | −0.2 to 0.2 T, 9 sweeps per field (Device 13); in-plane 0.3 T stabilizes, 0.2 T does not (Device 14); 1 T out-of-plane and in-plane field cooling then zero, still stochastic | field steps; remanent field; which cryostat |
| No SDE without long-range CDW (Ti x = 0.24) | Figs. S13, S14 | Devices 15 (oxidized, 3 stages), 16 (etched) | η upper bound about 0.1% (Device 16), slower sweep in Fig. S14f | thickness, Tc, Ic, geometry; field-on data |

Inconsistencies noticed: Fig. 2 device is Device 11 in the main text and Device 12 in the Fig. S3 caption; the main text attributes the −30.86% to 17.07% range to Device 12 (Figs. S3 to S5), and those values sit in Fig. S4, labeled "Device 13 after successive oxidation stages", while Device 13 is the etched device; SM p. 2 lists "30.86%" for sweep #5, where Fig. S4 shows η = −30.86%; Fig. S11 caption says 0.1 T stabilizes Device 14 while Fig. 4 needs 0.2 T for stable amplitude in Device 13.

## Matching (step 2) and scope
- Family: diode. Matched: diode-vortex-screening (adapted: the library signature reads the diode as finite-momentum or exotic pairing; this paper reads it as TRS-breaking domains from CDW order, and claims zero applied field, so the entry's small-field point is about the residual field). fine-tuning-and-selection always applies.
- Checks: the library has no diode-family checks, so only the three practice checks were walked (report-counts, report-ranges, report-processing). The diode entry's control went into the table.
- Skipped: all zbp, quantization, nonlocal, island, shapiro, kitaev, chiral and charge entries (no tunneling spectroscopy, no Majorana, Shapiro, island or charge claim). field-enhanced-supercurrent-resonances skipped: the paper does not claim supercurrent growing with field. protocol-parameter-sensitivity skipped: no automated pass/fail protocol, though its point about data-window choices informs question 7. local-probe-loophole skipped: no local-probe Majorana claim.
- Hold-out: no library source cites the paper (searched the library for the ID, "kagome" and "CsV"; none). All library sources predate 2026-08-26 or are reproducibility and TGP papers (Akrap et al. v2, Legg v2) whose topics do not touch this paper; I did not fetch them to confirm. No sources skipped.

## Outside lookalikes (library gaps)
- Trapped Abrikosov vortex plus self-field from nonuniform bias: Golod and Krasnov, https://arxiv.org/abs/2205.12196 (abstract checked). Relevant because the paper drives the flake to ±300 μA each sweep, field-cools at 1 T, and applies 0.1 to 0.2 T out of plane, all of which can trap or rearrange flux. Judged against the paper's control: polarity changes by trapping or removing a vortex.
- Stochastic switching-current distribution: Sahu et al., https://arxiv.org/abs/0804.2251 (abstract checked; it measures switching-current distributions whose width grows on cooling in nanowires). Also seen: Shah, Pekker and Goldbart, https://arxiv.org/abs/0709.3971 (abstract checked: switching "at random current values below the equilibrium critical current"). Relevant because η is built from one forward and one backward sweep, and the paper reports six or nine sweeps per condition. This is a statistical null hypothesis more than a mechanism; the library has no entry for it.
- Library gap: no diode-family checks (for example: residual field measured and nulled; plain-film or parent-material control with matched geometry; η versus field through zero; switching histograms per direction).
- Library gap: no entry for remanent field of a superconducting magnet as a hidden field in "field-free" claims; I folded it into diode-vortex-screening.

## Related work, how each was checked
All five opened on their arXiv abstract pages; ID, title, first author and the one-line description confirmed against the abstract (not full text):
- 2205.09276 Hou (abstract); 2205.12196 Golod (abstract); 2309.00264 Le (abstract); 2506.04601 Ge (abstract); 2605.29665 Zhang (abstract).
- Le et al. and Ge et al. are the paper's refs 17 and 40; all five predate the paper. Searches via export.arxiv.org API and the arXiv website search; several phrase queries returned nothing.

## Unsure
- Whether the Ti-doped x = 0.24 devices are comparable in thickness, Tc and Ic: not stated in the text I had; figures might show it.
- Fig. S12 partly addresses switching statistics; I kept the outside row at "partly addressed" since a fixed-bias trace tests telegraph switching within a sweep and not the sweep-to-sweep spread of Ic itself.
- Diode-vortex-screening: the Ti-doped controls bear strongly on it; I kept "partly addressed" since the residual field is not discussed and the field series was not shown for the controls.
- Fig. 4 field step and number of fields are not in the caption text.

## Skill issues
- Step 3 assumes ordered checks exist for the paper's family; diode has none. Unclear whether to derive checks from the entry's control or list only practice checks. I listed only practice checks.
- The template's fixed line "known lookalikes in topological transport" reads oddly for a diode or symmetry-breaking paper; the scope rule says to add one sentence, which I did.
- The hold-out rule asks to skip library sources that discuss the paper, which strictly needs fetching every source; the skill doesn't say whether dates are enough.
- Step 5 says mark outside rows "(not in library)"; the flags format here uses "outside: <name>". Both used.
- Page numbering is unspecified for papers with a separately numbered supplement; I used "SM p. N".
- Step 7 says to write files under reports/; this run returned them in the reply per the caller's instructions.
- Step 6 allows one question no entry raises; my question 8 (device labels) is that one, and question 7 (Ic criterion, excitation) leans on report-processing.
