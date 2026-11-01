# Run notes: arXiv 2608.17404v1

**Library version:** 0.5 (meta.version, updated 2026-10-24), 28 lookalike entries plus the checks section.

**What I read.** The extracted text of the paper (main text, Methods, Supplementary S1.A to S1.G), supplied as a text file. Per the run instructions I didn't fetch the abstract page, PDF or HTML. Figure details come from captions and the axis labels that survived extraction. Title taken from the first line of the text: "Flux-tunable global and local superconductivity in a topological insulator nano-SQUID". The Zenodo repository (10.5281/zenodo.21988906) was not accessed; no counts come from it. No ancillary figure data, so read_mtx.py wasn't used.

**Couldn't open / limits.** No figures as images. Several stretches of the extracted text have blank gaps (after the abstract's "align with these global features." and after "(see Fig. 3b-c)." on p. 5), so some text may be missing. Field axis values in Figs. 1, 3, S2 were only partly legible, so flux-to-field mappings are approximate.

**I don't recognize this paper** (dated 18 Aug 2026). No outside knowledge of its history was used.

## Claims table (step 1)

| Claimed signal | Figures | Devices | Counts and ranges |
|---|---|---|---|
| Ic oscillations, h/2e period, near-full revival at integer flux | Fig. 1e, 3a, S2a | A, B, C | Bx roughly ±4 T (Fig. 3a, S2a); Ic ramped from zero each time (Fig. 1e caption) |
| Diode efficiency reverses sign at half-integer flux, η about 20% | Fig. 1e, 3a, S2a, S4 | A, B, C | S4: VG about −75 to +25 V, Bx 0 to 4 T for B and C; |η| up to 0.10 (B), 0.20 (C) |
| Spectral jumps in local conductance at the reversal fields | Fig. 1f,g, 3b,c, S2b,c | A (one probe), B, C (two probes) | A: VG = 10 V main, S1 panels 0, 10, 20 V (caption says −10, 0, 20 V); Bx about ±6 T |
| Nonlocal jumps at expected phase boundaries | Fig. 3d,e, S2d,e, S5 | B, C | Some jumps do not match Ic features, mainly at high field (p. 5) |
| ZBP in device A inside the predicted topological window | Fig. 1f,g, S1 | A | Gate range limited by leaky dielectric (Supp. p. 3) |
| End-to-end ZBP correlation shows no topological/trivial distinction | Fig. 4, S3 | B, C | B: Bx = 0, 1, 2 T, VG ±30 V; C: Bx = 0, 2.5, 4 T; Fig. 4l, S3l Bx 0 to 4 T |

Counts: devices shown 3 (A, B, C). Devices fabricated and measured: not stated ("a series of devices with two functioning tunnel contacts", p. 4; "all examined devices", p. 4). Tunnel junction yield "below 50%" (p. 5). Cooldowns: not stated. Temperature: base about 30 mK only. Field direction: axial Bx only, with Bz compensation (Supp. S1.B). Geometry: Table S1 (A 21 nm x 70 nm x 1.9 µm; B 36 x 70 x 1.3; C 16 x 80 x 2.5). Missing: number measured, cooldowns, temperature dependence, field-angle dependence, series resistance values.

Internal points noticed: (1) Methods state tunnel resistances above 100 kΩ, but Fig. S1a (device A) and Fig. S2b (device C) show G near 0.6 to 1.6 e²/h, about 16 to 43 kΩ. (2) Fig. S1 caption gate values (−10, 0, 20 V) differ from panel labels (0, 10, 20 V). (3) Device C: "zero-bias conductance peak was mostly absent" (Supp. p. 4) against "strong increase of correlated zero-bias conductance peaks" (Supp. p. 5). (4) Main text p. 5 says no clear distinction between regimes; Supp. p. 5 says "Similar to device B" there is a strong increase entering the first topological regime. All raised as questions 3, 6, 7.

## Matching (step 2)

Families walked: zbp checks and practice checks. The diode and nonlocal families have no checks section, so the headline interferometer signals had no ordered checks to walk.

Included: abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, one-end-only, trivial-andreev-band-gap-reopening, full-shell-flux-andreev (adapted), local-probe-loophole, exceptional-point-zero-mode, diode-vortex-screening (adapted), protocol-parameter-sensitivity (adapted), fine-tuning-and-selection.

Adapted: full-shell-flux-andreev (the wire is sandwiched by Nb on two sides, not a full shell, but the ZBP sits in an odd flux lobe with flux-driven phase winding; "junction region" read as the region under the tunnel probe). diode-vortex-screening (the diode is read as a sign of a topological phase jump, not finite-momentum pairing; the Nb vortex mechanism still applies). protocol-parameter-sensitivity (no pass/fail protocol; applied to the sign-of-third-derivative classification behind Fig. 4l and S3l).

Skipped: fine-tuned-plateau and series-resistance-subtraction (no conductance near 2e²/h is claimed; the raw-conductance check was still walked); micromagnet-stray-field (no magnets); spin-orbit-length-pinning (needs a normal segment of tuned length between barrier and superconductor; none described); chiral-plateau-superconductor-short, island-states-coulomb-spacing, all shapiro entries, transparent-junction-pi-crossing, switching-jump-blind-region, charge-trap-fractional-shift, coulomb-dominated-interferometer, false-poor-mans-majorana (signals not in this paper); field-enhanced-supercurrent-resonances (Ic revival here is periodic interference, not growth over the zero-field value; considered and left out).

## Sources held out

None. Only two library sources have versions dated after 18 Aug 2026 or close to it: Legg 2502.19560v2 (updated 2026-10-21; Legg is a coauthor of the paper under review) and Akrap et al. 2501.18631v2 (2026-03-25). I downloaded both full texts and searched for "2608", "Nikodem", "nano-SQUID" and "Flux-tunable"; neither cites the paper (Legg v2's only "flux-tunable" hit is the Valentini reference). Other sources predate the paper.

## Related work checks (step 5)

All IDs, titles and first authors confirmed via the arXiv API (export.arxiv.org, id_list query).
- 2205.04469 Seoane Souto et al.: abstract plus full text (p. 2, requirement (1): diode effect vanishes at Φ = nΦ0/2). Also the source for the outside row.
- 2304.00484 Ciaccia et al.: abstract plus full text (appendix: "The sign of the diode efficiency is mirrored with respect the magnetic field value corresponding to half flux quantum when the critical current asymmetry α between the two junctions changes sign.").
- 2008.02348 Valentini et al.: abstract.
- 1910.11413 Pan and Das Sarma: abstract.
- 2205.09276 Hou et al.: abstract.
Hess et al. 2210.03507 abstract was also checked but not listed (limit of five; it is a library source and cited by the paper as ref. 12).

## Library gaps

- No entry for interferometer signatures: Ic(Φ) oscillations and a diode efficiency whose sign reverses at half-integer flux arise in any asymmetric two-junction interferometer with skewed current-phase relations (Seoane Souto et al. 2022, arXiv 2205.04469; Ciaccia et al. 2023, arXiv 2304.00484). Suggested entry: family diode or a new "phase" family, tests "trivial interferometer model fit" and "feature at half flux beyond the symmetry-enforced zero".
- No checks for the diode or nonlocal families.
- The sign-based end-to-end correlation measure has no chance baseline in the library; a "correlation analysis baseline" test could sit under one-end-only or protocol-parameter-sensitivity.

## Unsure

- Whether the device A ZBP counts as a claimed signal: the paper calls it "broadly consistent" (p. 3) and later concludes local ZBPs are ambiguous. I treated it as evidence offered and judged the zbp entries against devices A to C.
- Marked "all" for gate insensitivity (disorder entry) because gate dependence is shown for all three devices (Fig. S1, Fig. 4, Fig. S3).
- Marked "part" for "Code and every dataset published": a data availability statement with a Zenodo DOI, code not mentioned; the skill doesn't say whether such a statement counts as shown.
- For diode-vortex-screening I counted the cross-section scaling of the reversal period across devices as an equivalent of "effect followed against sample width"; the paper doesn't conclude against the vortex mechanism (it invokes vortices at high field), so status stays "Tested in part".
- Flux to field conversions for device C (whether 4 T is inside the second trivial regime) couldn't be checked from the text.

## Skill issues

- The skill tells me to read the abstract page and PDF and to write reports/ files; this run forbade both, so the title came from the text and outputs went to the reply and flags.json.
- When the paper itself attributes the signal to the lookalike (here, disorder for ZBPs), the status scale has no fitting value; "Tested in part" undersells it.
- The headline signals (interferometer Ic and diode reversal) fall in families without checks, so the ordered checks walked were the zbp ones, which cover the secondary claim. The skill doesn't say what to do when the main claim's family has no checks.
- The skip rule example ("full-shell-flux-andreev for a partially covered wire") conflicts with geometries where flux winds the phase without a full shell; I adapted it, which the skill allows only for "a different kind of measurement".
- Hold-out rule doesn't say how deeply to check a source updated after the paper (here a coauthor's comment); I searched the full text.
- Four mandatory questions plus paper-specific ones under an eight-question cap forced merging several range questions into one.
