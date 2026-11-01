# Run notes: 2607.00683v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (updated 2026-10-24). 28 lookalike entries. Checks families present: zbp, shapiro, kitaev, charge, practice.
- Date: 2026-10-24.

## What I read

- The extracted paper text only (paper.txt, 9 pages of main text plus references), per the run instructions. I did not open the abstract page, PDF or HTML.
- Title and version come from the text header: "Facet-selective ballistic supercurrent in a weak topological insulator", arXiv:2607.00683v1 [cond-mat.mes-hall] 1 Jul 2026. The skill asks for the title on the abstract page, which this run did not allow.
- Figure details come from the captions only.
- Page numbers come from the printed page markers in the text: p. 1 abstract, p. 2 introduction, p. 3 Fig. 1 and the start of Results, p. 4 Fig. 2, p. 5 Fig. 3, p. 6 Fig. 4 and Ic(T), p. 7 Js(x) widths, the trivial-channel argument and the CPR, p. 8 Fig. 5 and Discussion, p. 9 Methods.

## What I couldn't open

- The Supplementary Information (Notes 1 to 7, Figs. S1 and S7, Table S1). It is not in the text.
- Figure images.
- No data repository or ancillary files are linked in the text, so nothing was counted from data.

## Claims table (step 1)

| Claim | Figures | Devices | Counts and ranges |
|---|---|---|---|
| SQUID-like Ic(Bz) with integer flux-quantum minima spacing | Fig. 4a,b; Fig. 5b; Supp. Note 5 | Dev 1, Dev 2 (Pd/Al, current along a); Dev 3 (Pd/NbN, current along c) | 20 mK. Field range not stated in text. |
| Js(x) with two edge peaks, Gaussian half-widths 0.7-1.5 um | Fig. 4d,e; Supp. Note 6, Fig. S7 | Dev 1, Dev 2 | Reconstruction limited by field range (p. 7) |
| Field-orientation contrast, By versus Bz | Fig. 5b,c | Dev 3 only | 20 mK |
| Exponential Ic(T), read as long ballistic junction | Fig. 3a-d | Dev 1, Dev 2, Dev 3 | Fits in "the high-temperature regime". T range not stated. Base temperature 15 mK. |
| Sharp lobes, read as sawtooth CPR | Fig. 5b,c against simulations in Fig. 5d-f; Supp. Note 7 | Dev 3 (Fig. 4 by implication) | Simulated W = 1, 0.5, 0.3, 0.2, 0.1 |
| ZrTe5 is in the WTI phase | Fig. 2a-g; Supp. Fig. S1, Notes 3 and 4 | One Hall bar (count not stated); STM on cleaved crystals | Tp about 139 K; SdH at 2 K; STM at 5.1 K; gap about 70 meV; step-edge states about 6 nm wide |

Missing counts:
- Junctions fabricated, junctions measured, and junctions that showed the effect. "All junctions" (p. 6) may mean three, but this is not stated.
- Cooldowns.
- Field ranges and temperature ranges.
- Junction lengths and widths (in Table S1, not available).

## Matching (step 2)

- Applied: fine-tuning-and-selection (always applies).
- Skipped as not applicable to an S/3D-crystal/S junction measured by Ic(B) interference:
  - The zbp, quantization, nonlocal, island, chiral, kitaev, charge, diode and shapiro entries: abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, fine-tuned-plateau, series-resistance-subtraction, one-end-only, trivial-andreev-band-gap-reopening, micromagnet-stray-field, full-shell-flux-andreev, chiral-plateau-superconductor-short, island-states-coulomb-spacing, shapiro-landau-zener, shapiro-nonlinear-resistance, charge-trap-fractional-shift, spin-orbit-length-pinning, exceptional-point-zero-mode, transparent-junction-pi-crossing, switching-jump-blind-region, false-poor-mans-majorana, coulomb-dominated-interferometer, diode-vortex-screening. No zero-bias peak, quantized conductance, Shapiro, charge or diode signal is claimed.
  - protocol-parameter-sensitivity: no automated pass/fail protocol.
  - local-probe-loophole: about Majorana separation from local probes. The STM is a local probe, but it is offered for the bulk phase, not for separated modes.
  - field-enhanced-supercurrent-resonances (supercurrent family): its signature is supercurrent that grows above its zero-field value, read as triplet pairing. Here the claim is Ic(B) periodicity and lobe shape, and the paper says the oscillation amplitude "decays slowly with increasing magnetic field" (p. 6). Borderline. Skipped.
- Adapted: none of the library entries. The scope sentence in "What this is" explains that only the practice entry applies.
- Checks walked: practice only (report-counts, report-ranges, report-processing). The library has no checks for the supercurrent family.

## Outside rows (library gaps)

1. Trivial edge channels from band bending or doping, giving SQUID-like interference and edge peaks in Js(x).
   - Source: de Vries et al. 2018, arXiv 1709.03727.
   - Tests come from its control (gate dependence of the edge/bulk crossover, and the same measurement in a trivial reference). Supported by Hart et al. 2014 (trivial thin-well reference) and Allen et al. 2016 (gate tuning).
   - I counted the paper's By orientation on Dev 3 as a partial equivalent of the reference test: the WTI picture predicts a homogeneous current there, and trivial edges predict edge peaks. Shown for one device, with an outcome the authors call "puzzling". Hence "part".
   - The paper also lists "trivial boundary contributions" among possible causes of peak broadening (p. 7).
2. Quasi-exponential Ic(T) in a diffusive long junction mimicking the ballistic form.
   - Source: Dubos et al. 2001, arXiv cond-mat/0008146. Full text, near Eq. 3: "within a limited temperature interval this expression is numerically very close to a simple exponential dependence Ic ∝ exp(−L/LT) with LT ∝ 1/T, as one would expect in a ballistic limit."
   - The paper argues against diffusive transport. The mean-free-path estimate is in Supp. Note 2, which I couldn't see, and it bears on the bulk, not on the diffusive fit. Hence "argued, not tested".
3. Gap not filled: no library entry or opened paper covers lookalikes for "sharp lobes mean a sawtooth CPR", such as self-field screening or switching-current extraction. I did not add a row because I opened no paper showing it.

## Sources held out

- None. I didn't open any library source. None of their titles or quotes in the library refer to this paper. Most predate it; the 2026 versions (Legg v2, Akrap v2, Frolov published) were not opened.

## Related work checks

All IDs, titles and first authors were confirmed through the arXiv API (export.arxiv.org).

| Paper | How checked |
|---|---|
| Hart 2014, 1312.2559 | Abstract read |
| Allen 2016, 1504.07630 | Abstract and full text searched (edge currents near neutrality, band-bending guided modes, gate crossover to Fraunhofer) |
| de Vries 2018, 1709.03727 | Abstract and full text searched (accumulation at etched mesa edge; gate-dependent bulk-to-edge transition; "a clear demonstration of superconducting edges alone does not prove induced superconductivity in topological edge states") |
| Dubos 2001, cond-mat/0008146 | Abstract and full text near Eq. 3 |
| Meier 2016, 1603.08567 | Abstract read |

- Searches for prior ZrTe5 Josephson junction work (API and website) found none.

## Unsure

- The extracted text looks incomplete in three places:
  - p. 7 announces "the following three observations" and then starts at "Second". The first observation is missing.
  - A double space after "where gapless topological surface states are expected." (p. 2) suggests a missing sentence.
  - A double space after "WTI boundary states in ZrTe5 ." (p. 8) suggests the same.
  - I assessed only what the text contains and asked about the missing first observation (question 5). If the first observation addresses trivial edges (for example STM edge widths or several junction widths), the trivial-edge row could move.
- Whether junctions or only Hall bars were ion-milled is ambiguous in Methods.
- "A second device or dataset shown" is marked part: three devices for the Bz SQUID pattern, but only one for the By contrast.
- I didn't recognize the paper and used no outside knowledge of its history.

## Skill issues

- The checks section has no steps for the supercurrent family, so a supercurrent-interference paper gets only the practice checks. The skill doesn't say whether to borrow checks from another family.
- Step 5 says outside rows take "tests from the control that paper describes". Step 3 also allows a paper's "equivalent test". It is unclear whether an equivalent test may be credited against an outside row's tests. I did so once (By orientation) and said why.
- The scope paragraph covers "adapt the matching entries" but not the case where almost no entry matches and outside rows carry the report. The report then has a near-empty library table.
- Step 7 says to write reports/<id>.md and use the abstract-page title. This run's instructions forbid both, so I used the title from the text header.
- The template has no place to flag gaps in the source text. I put it in a question.
- The flags.json "note" field is defined only for "Not tested". I left it null for the "Tested in part" rows.
