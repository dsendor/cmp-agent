# Run notes: 2607.00683v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (28 lookalikes). Skill: cmp-assistant/skill/SKILL.md; template: skill/report-template.md. Date of run: 2026-10-24.
- What I read: the extracted text of 2607.00683v1 supplied at the scratchpad path (main text, figure captions, methods, references). Per the task, no PDF, abstract page, HTML or supplement was fetched. Supplementary Notes 1 to 7 and Table S1 were not available, so tests that may sit there (minima spacing in Note 5, mean free path in Note 2, Js(x) method in Note 6, device dimensions in Table S1) could not be judged and were treated as not shown in the main text, with the gap noted in the report. No data repository is linked in the text; none used. read_mtx.py not used (no figure data).
- Title taken from the first lines of the extracted text (no abstract page available).
- Recognition: I do not recognize this paper or know its later history.

## Claims table (step 1)

| Claim | Figures | Devices | Counts and ranges |
|---|---|---|---|
| C1 SQUID-like Ic(B) with flux-quantum period, read as supercurrent on two side facets | Fig. 4a,b (Dev 1, Dev 2); Fig. 5b (Dev 3); Supp. Note 5 for minima spacing | Dev 1, Dev 2 (Pd/Al, current along a, B along b); Dev 3 (Pd/NbN, current along c, Bz along b) | 20 mK (base 15 mK). Field ranges not stated in text. Devices fabricated, measured, cooldowns: missing. |
| C2 Js(x) with two edge peaks, Gaussian half-widths 0.7-1.5 µm | Fig. 4d,e (Dev 1, Dev 2) | Dev 1, Dev 2 | Field window used for reconstruction: missing. Method in Supp. Note 6 (unavailable). |
| C3 Field-orientation contrast, By vs Bz | Fig. 5b,c | Dev 3 only | By along a-axis (in-plane). By not reported for Dev 1, Dev 2. Field alignment procedure missing. |
| C4 Exponential Ic(T), read as long ballistic junction | Fig. 3a-d | Dev 1, 2, 3 | Temperature range not stated in text; fits to "high-temperature regime". δE values, RN not in main text. |
| C5 Triangular lobes, read as sawtooth CPR | Fig. 5b,c vs simulations Fig. 5d-f | Dev 3 | Simulations: sinusoidal and sawtooth only; Supp. Note 7. |
| C6 ZrTe5 in WTI phase | Fig. 2a (ρ(T) peak at 139 K), 2b-d (SdH at 2 K, single pocket), 2e-g (STM gap ≈70 meV, step-edge LDOS) | "a ZrTe5 Hall bar device" (one shown); STM on cleaved crystals | Number of Hall bars, STM areas and tips: missing. |

Device count stated: "three independent devices" (p. 8). No gate on any device.

## Matching (step 2)

- Matched: fine-tuning-and-selection (always included).
- Skipped, with reason: all zbp, quantization, nonlocal, island, chiral, kitaev, charge families (no zero-bias peak, quantized conductance, nonlocal conductance, island, QAH plateau, dot chain or fractional-charge claim). Shapiro family including transparent-junction-pi-crossing and switching-jump-blind-region (no microwave or Andreev spectroscopy). field-enhanced-supercurrent-resonances (the paper does not claim supercurrent growing with field; the oscillation amplitude "decays slowly with increasing magnetic field"). diode-vortex-screening (no nonreciprocity claim). protocol-parameter-sensitivity (no automated pass/fail protocol). local-probe-loophole (Majorana local-probe argument; does not apply to interference of a Josephson junction).
- Entries adapted: none. Scope: still topological transport (Josephson interferometry), so no scope adaptation was declared; the report says in one sentence that the library has no entries for interference-pattern claims.
- Checks: no checks family for supercurrent or interference; walked the practice checks only (report-counts partly, report-ranges not done, report-processing partly).

## Outside-library rows (library gaps)

1. Trivial edge accumulation from band bending. Source opened: de Vries et al., arXiv 1709.03727v2 (abstract and full text; the text shows a gate-driven Fraunhofer to even-odd to SQUID transition in trivial InAs, "The transition from bulk to edge transport as a function of gate voltage is measured in several other Josephson junctions"). Tests taken from that control: gate-tuned density sweep; measurement where no topological state is expected. Paper argues against it with three observations (reproducibility, field-orientation contrast, ballistic Ic(T)), none of which is one of those tests. Status: not tested, argued, not tested. Uncertainty: the paper also says broadening "may reflect ... trivial boundary contributions" (p. 7), which could support "Left open by the authors"; I kept "argued, not tested" because the paper concludes against the trivial-edge picture as a whole.
2. Quasi-exponential Ic(T) in diffusive long junctions. Source opened: Dubos et al., arXiv cond-mat/0008146v2 (abstract and full text; p. 3: "within a limited temperature interval this expression is numerically very close to a simple exponential dependence Ic ∝ exp(−L/LT) with LT ∝ 1/T, as one would expect in a ballistic limit"). Tests from that control: comparison with diffusive theory in Thouless-energy units; eRNIc vs Thouless energy. Status: not tested, argued, not tested.
- Considered and not added: flux focusing and in-plane-field flux dipoles making transport edge-like (Suominen et al., arXiv 1611.00190v1, abstract and text opened). Their edge effect needs an in-plane field along the current; the paper's By is along a with current along c, so the match was weak. Recorded here as a possible library gap for interference claims. A triangular-lobe lookalike (skewed CPR in diffusive junctions, loop inductance) had no openable source (the Golubov RMP review is not on arXiv), so it went in as the one extra question only.
- Suggested library additions: a family and checks for "supercurrent density from interference patterns read as topological edge or hinge states" with entries for band-bending edges (de Vries 2017, Allen 2015), flux focusing (Suominen 2016), and diffusive quasi-exponential Ic(T) (Dubos 2000).

## Related work checks

All via the arXiv API (export.arxiv.org), IDs, titles and first authors confirmed from the API record.
- 1312.2559 Hart et al.: abstract.
- 1709.03727 de Vries et al.: abstract and full text.
- 1504.07630 Allen et al.: abstract.
- 1909.02537 Choi et al.: abstract.
- cond-mat/0008146 Dubos et al.: abstract and full text.
Years given are arXiv submission years. All predate the paper under review; none was described for what it says about it.

## Hold-out

No library source used names this paper by title, author or ID as far as the library quotes show. I did not open the library's own sources (Frolov 2023, Akrap et al. 2026); the Akrap v2 (2026) report could in principle cite later papers, unverified. Nothing skipped.

## Skill issues

- The skill says to use the title from the arXiv abstract page; the task gave text only. I used the title from the extracted text.
- The library has no checks family and almost no entries for Josephson interference claims (edge or hinge supercurrent, CPR from lobe shape). The skill's scope rule talks about adapting entries for a different kind of measurement; it is unclear whether "in scope but uncovered" should be declared the same way. I wrote one sentence in "What this is".
- For outside rows, "take its tests from the control that paper describes": de Vries' abstract states no control, so I read its text. The skill does not say whether reading full text is required for this.
- Status ambiguity: when a paper says an explanation "can in principle arise" and then argues against it, both "Left open by the authors" and "argued, not tested" can fit. The rules do not say which wins.
- The skill says to read the supplement if it is in the PDF; with text only, tests the paper delegates to supplementary notes cannot be judged. The rules do not say whether "referred to the supplement" counts as shown, part, or no. I treated it as not shown and said so.
- report-counts (check) and the first test of fine-tuning-and-selection overlap; the "A second device or dataset shown" test is "all" here although the counts question stays open, which makes "tested in part" read stronger than the counts gap.
- Eight-question cap: four standard questions plus specific ones for each matched lookalike plus figure data choices plus one extra hit the cap; I merged Fig. 4d,e and Fig. 5c data choices into one question.
