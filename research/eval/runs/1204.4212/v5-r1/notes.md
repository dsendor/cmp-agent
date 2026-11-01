# Run notes: arXiv 1204.4212v2

AI only. Lookalike library version 0.5 (meta.version), updated 2026-10-24. Run 2026-10-24.

## What I read
- The skill (SKILL.md), report-template.md, and library/lookalikes.yaml, all read in full once at the start.
- The paper: the local extracted text of v2 (paper.txt, main text pp. 1 to 6 and Supplementary Information pp. 7 to 17), the local arXiv abstract page (abs.html: title "Observation of the fractional ac Josephson effect: the signature of Majorana particles", Rokhinson, Liu, Furdyna; v1 18 Apr 2012, v2 23 Aug 2012). I viewed PDF pages 4 (Figs. 2 and 3), 11 (Figs. S8 and S9) and 17 (Fig. S12) as images to check field ranges and what the figures show.
- No ancillary files and no data repository are linked, so read_mtx.py was not used and no device counts come from data.
- Not fetched: the paper itself in any form (per the task). Everything opened is listed below.
- Note: "B∥I" in quotes appears as "BkI" in the extracted text; I wrote the symbol as printed in the PDF. Spaces before commas inside quotes ("Vrf ,") are kept as extracted.

## Recognition
I recognized the paper (published in Nature Physics, 2012) and know it has a later history of discussion in the literature. I did not use that knowledge; the report assesses v2 as written.

## Claims table (step 1)

| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| Shapiro steps at hf/2e = 6 µV at B = 0, 3 GHz, Bessel-like widths | Fig. 3 left, Fig. 4 (B = 0), Fig. S11 | JJ8 (40 nm gap) | Vrf 0 to about 12 mV (top of fridge); T = 20 mK; Iac = 2 nA at 17 Hz |
| Step height scales with frequency | Fig. S10 | JJ8 (implied) | 2, 3, 4 GHz; field not stated, all steps present |
| First step (6 µV) disappears above about 2 T in B∥I, 12 and 18 µV steps remain to about 3 T | Fig. 3 right, Fig. S12 | JJ8 | Fig. 3: B = 0, 1.0, 1.6, 2.1, 2.5 T, Vrf 3 to 6 mV in 0.6 mV steps; Fig. S12: B = 0 to 3.4 T (12 panels), Vrf 0 to about 10 mV, I about ±300 nA; one field direction (B∥I) |
| 6 µV step returns at Vrf > 10 mV at 2.2 T; 12 µV step minimum at the J1 minimum | Fig. 4 | JJ8 | B = 0, 1.0, 2.2 T, 3 GHz only |
| Excess current (Andreev reflection) persists to 4 T | Fig. 2 right and inset | JJ8 | 0 and 3 T traces; inset 0 to 4 T |
| Junction is single-junction dominated, clean limit | Fig. 2, text p. 3, SI VII | JJ7 (r = 7.3), JJ8 (r > 10) | RN estimates 2 to 6 kΩ; Rs < 1 kΩ |
| Proximity superconductivity, Tc of JJs | Fig. S7, Fig. S8 | > 10 GaAs test devices; JJ6, JJ7, JJ8, line L | Gaps 20 to 120 nm across devices |

Missing counts: number of junctions fabricated, number measured under rf, number showing the doubling, cooldowns, temperature dependence of steps, field directions other than B∥I, frequency dependence above 2 T. No gate on the device.

## Families and matching (step 2)
Families walked: shapiro and practice.

Matched entries: shapiro-landau-zener, shapiro-nonlinear-resistance, switching-jump-blind-region, transparent-junction-pi-crossing (the claim implies the protected crossing behind the 4pi effect), quasi-majorana-smooth-confinement (matched on physics: its library source Vuik et al. 2019 says quasi-Majoranas mimic "the $4\pi$ Josephson effect"; I confirmed in the Vuik full text, around the "TOPOLOGICAL JOSEPHSON EFFECT" section, that quasi-Majoranas reproduce a 4pi-periodic Josephson current), fine-tuning-and-selection (always).

Skipped, with reason:
- abs-quantum-dot, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, spin-orbit-length-pinning, exceptional-point-zero-mode, micromagnet-stray-field, full-shell-flux-andreev: zero-bias tunneling peak signatures; the paper presents no tunneling spectroscopy as evidence (it mentions zero-bias anomalies only as background).
- fine-tuned-plateau, series-resistance-subtraction: conductance quantization signatures; the claim is a voltage step height set by frequency. Series and shunt resistances are estimated (SI VII) but do not set the step voltage.
- one-end-only, trivial-andreev-band-gap-reopening, local-probe-loophole: nonlocal or local-probe signatures; no tunneling probe in this device.
- protocol-parameter-sensitivity: no automated pass/fail protocol.
- island-states-coulomb-spacing, charge-trap-fractional-shift, coulomb-dominated-interferometer: Coulomb blockade or interferometer signatures (the "charge-e" reading is from step height, not from charge shifts).
- field-enhanced-supercurrent-resonances, diode-vortex-screening: supercurrent magnitude or nonreciprocity signatures.
- chiral-plateau-superconductor-short, false-poor-mans-majorana: other device types.
- Checks for zbp, kitaev and charge families: not applicable for the same reasons.

Adapted: none (in scope).

## Hold-out (sources skipped)
Checked by downloading the arXiv PDF of each source I might use and searching the text for "Rokhinson" and "1204.4212":
- Held out (each cites the paper under review): Dartiailh et al. 2005.00077 (ref. 20); Prada et al. 1911.04512 (ref. 199, and Fig. caption on missing odd steps in InSb/Nb); Mudi and Frolov 2106.00495 (ref. 6); Zhang et al. 2211.08710 (ref. 30); Frolov et al. 2309.09368 (reference list); Wu et al. 2403.07370 (ref. 34).
- This holds out every source of shapiro-landau-zener, shapiro-nonlinear-resistance, switching-jump-blind-region and transparent-junction-pi-crossing, every source of the shapiro checks, and the Frolov sources of fine-tuning-and-selection. I used those entries' library text (lookalike, mechanism, tests, control) and quoted or listed none of the held-out sources.
- Not held out: Vuik et al. 1806.02801 (no mention; quoted in the report table), Akrap, Frolov et al. 2501.18631 (no mention; not quoted in the end).
- Not checked because not used: other sources of quasi-majorana-smooth-confinement (Kells 1207.3067, Aghaee 2207.02472, Moore 1711.06256) and all sources of skipped entries.

## Status reasoning (step 3)
- Judged against the evidence presented: one device (JJ8), one frequency (3 GHz) above 2 T, one field direction.
- shapiro-landau-zener: zero-field test "all" (Fig. 3, S10, S11). It does not separate the lookalike by itself because the gap shrinks with field (the paper's own Eq. S1 estimate, 30 µeV at 2 T). Frequency marked "part": Fig. S10 shows 2, 3, 4 GHz only in the regime where all steps are present. Transparency "part": excess current shown, no value extracted. The paper does not mention Landau-Zener, so "ruled out" was not available anyway.
- shapiro-nonlinear-resistance: paper argues against nonlinear effects for the first step (quoted, p. 5). Fig. S9 is a dc dV/dI(I, B) map, counted as "part" for the resistance test.
- switching-jump-blind-region: Fig. 4 reports the 6 µV step returning at Vrf > 10 mV at 2.2 T, which is a power series of the kind the test asks for ("part": no temperature or frequency series); dc V(I) above 2 T without rf not shown.
- transparent-junction-pi-crossing and quasi-majorana: no figure tests them, and the paper does not discuss either, so "not mentioned".
- fine-tuning-and-selection: several JJ8 datasets (Fig. 3, Fig. 4, Fig. S12) counted "part" for "a second device or dataset"; no second device.

## Related work: how each link was checked
All five: opened the arXiv abstract page (arxiv.org/abs/<id>), confirmed ID, title and first author, and checked my one-line description against the abstract (abstract only, not full text).
- 1202.0642 Domínguez, Hassler, Platero (cited by the paper; listed for its own results).
- 1206.4596 Sau, Berg, Halperin. Its abstract says the fractional Josephson effect "has been observed for the semiconductor nanowire system", which likely refers to this paper; I described only its own results.
- 1803.07674 Le Calvez et al. (arXiv 2018).
- 2107.05293 Galaktionov and Zaikin.
- 2210.06502 Elfeky et al. (found by arXiv API search abs:"missing" AND abs:"Shapiro" AND abs:"trivial", and ti:"Reappearance" AND ti:Shapiro).
- Dropped: Wiedenmann et al. 1503.05591 and Laroche et al. 1712.08459 (opened, relevant, cut to keep five). An ID I tried for a Rosenbach et al. paper (2101.10882) resolved to an unrelated paper, so I did not list it.
- Not listed although relevant: the held-out library sources, which I did not reuse as related work.

## Outside-library lookalikes
None added. Joule overheating (Le Calvez et al.) changes which odd steps survive but does not by itself produce a missing first step, so I listed it as related work only.

## Library gaps
- The shapiro family has no check on field direction relative to the spin-orbit field (the topological phase needs B perpendicular to Bso; field along Bso is a natural trivial control). I raised it as the one extra question.
- shapiro-landau-zener tests only "same measurement at zero field"; for field-driven claims, trivial missing steps can also evolve with in-plane field (Elfeky et al. 2210.06502), so a field-dependent trivial control is missing.
- quasi-majorana-smooth-confinement's signature and tests are written for zero-bias peaks only, though its source covers the 4pi Josephson effect; a Josephson-specific test is missing.
- Every source of the four shapiro entries and of all shapiro checks cites this paper, so the library has no held-out-safe source for this family. Candidate additions not citing it would need checking (Galaktionov and Zaikin 2107.05293 was not checked for citations).
- Heating (Le Calvez et al.) as a modifier of the odd-step pattern is not in the library.

## Unsure
- Whether Fig. S10 was taken at B = 0 (the caption does not say; all steps are present).
- Whether Fig. 3 right and Fig. S12 are the same measurement; if so, the "second dataset" count is thinner.
- Report length is about 900 words outside the table, at the top of the range.

## Skill issues
1. Hold-out rule: unclear whether an entry whose every source is held out still applies. I kept such entries, worked from the library's own text, and cited none of their sources. A sentence on this would help.
2. Unclear whether a held-out library source may be listed as related work if found again by search. I excluded them.
3. Step 2 says to match on the physics, but signatures are worded per family. quasi-majorana's signature is a zero-bias peak while its source covers the 4pi effect. I matched it, but its tests fit poorly.
4. "Ruled out for the claim" needs "the paper concludes against the lookalike". Unclear whether a general claim of uniqueness ("a unique signature of a topological quantum phase transition") counts. I counted only explicit arguments.
5. Test regime ambiguity: when a test is shown only in the control regime (frequency dependence at zero field), "part" or "no" are both defensible. I used "part" with a clause.
6. The template's check line format ("<check> : Done") has no slot for the check id. I wrote the check text and kept the ids in flags.json.
7. Step 7 says to write reports/<id>.md. Per the task, the report and notes go in the reply.
