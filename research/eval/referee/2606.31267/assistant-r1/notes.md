# Run notes: arXiv 2606.31267v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (updated 2026-10-24), 28 lookalike entries. Read once at the start with skill/SKILL.md and skill/report-template.md.
- Date of run: 2026-10-25. subagent.

## What I read
- The v1 PDF (27 pages) and its extracted text, from the local paper files I was given. Per the task, I did not open the arXiv abstract page or any other version of this paper. The title comes from the PDF: "Orientation-tunable correlated Chern insulating states in chiral twisted double bilayer graphene proximitized by WSe2". The report header shortens it.
- Figures were read from the PDF (pages 23 to 27, rendered at 110 to 400 dpi). Figs. 3 and 4 were read in detail at high resolution.
- No supplementary material is in the PDF. The main text cites Supplementary Table I, Supplementary Figs. 1 to 11 and Supplementary Sections, and a Source Data file and Supplementary Software. I could not see any of these. Claims that rest only on them (D2, D4, D5, D6, D7 fans; the T* Arrhenius fit; DFT robustness; the three-scenario comparison) count as stated, not shown.
- There is no data repository link (only "Source Data file"), so I counted no data files. read_mtx.py was not used.
- I did not recognize the paper and know nothing of its later history.
- I glanced at the first five lines of scripts/check.py while counting library entries. I used nothing from it.

## Claims table (step 1)
| Claim | Figure | Device | Counts and ranges |
|---|---|---|---|
| Ising SOC gives CK = +2 at Φ = 0°, CK = 0 at 15°, 30° and without WSe2 | Figs. 1d to l, 2j to m | theory, θ = 0.9°, D = 0.5 V/nm for Chern numbers | λI = 2.0 meV, λR = 0.5 meV, λI(Φ) = λI,0 cos 3Φ |
| Correlated insulator at ν = −1 (and ν = +1 in D2) | Fig. 3a to e | D1 (θ 0.93°), D2 (θ 0.80°), both Φ ≈ 0° | D −1 to 1 V/nm; n about ±2×10^12 cm^-2 (a, c) and −1 to 0.5 (b, d); T 1.6 K and 20 mK; B = 0 |
| Non-monotonic D dependence of the ν = −1 peak | Fig. 3e | D2 | D 0.4 to 0.9 V/nm, 20 mK |
| Activation gap Δ = 0.78 ± 0.04 meV, T* ≈ 2.7 K | Fig. 3f, Supp. Fig. 6 (not seen) | D2, D = 0.6 V/nm | T 1.5 to 10 K; the fit below T* seems to use only the 1.5 to 2.7 K points (not asked, question limit) |
| C = +1 Streda line from ν = −1, developed above about 0.3 T | Fig. 4a to c | D1, D = 0.6 V/nm, 25 mK | B 0 to 7 T (positive only shown); n −1.5 to 0.5×10^12 cm^-2. My slope estimate from the black dots in Fig. 4b gives C ≈ 1.0 |
| Rxy reaching 97.6% of −h/e2 at B ≈ 3.0 T | Fig. 4d | D1 | values 79.7% (2 T), 97.6%, 97.3%, 95.2%, 87.5% (about 5 T) |
| C = +1 and C = +2 from ν = −2 | Fig. 4a to c | D1 | same ranges |
| Φ ≈ 15° device: ν = −1 insulator at B = 0, field-independent feature read as C = 0 | Fig. 4e, f | D3 (θ 0.83°) | D −1 to 1, 20 mK; fan at D = 0.6, 25 mK, B 0 to 7 T; Rxx only, no Rxy shown for D3 |
| Seven devices: D1, D2, D4 (Φ ≈ 0°, C = +1), D3 (15°), D5 (30°, C = 0), D6, D7 (no WSe2, no ν = −1 state) | text p. 12, Supp. Table I (not seen) | 7 | number fabricated not given; set-aside devices not mentioned; cooldowns not given |
| Φ uncertainty ±2° from optical edge alignment | Methods p. 13 | all | partly justified by "a posteriori" Chern-number consistency |

Missing counts: devices fabricated, cooldowns, D values at which fans were measured, negative-field data, Rxy for D3, fans for D2, D4, D5 in the main text.

## Entries matched, adapted, skipped
- Matched: fine-tuning-and-selection (always).
- Adapted: fine-tuned-plateau. Its signature is a ZBP plateau near 2e^2/h. I matched on the physics: a near-quantized value (Rxy at 97.6% of h/e^2 along a Streda line) offered as evidence. The test texts are kept as written.
- Skipped: series-resistance-subtraction. Rxx and Rxy are four-terminal lock-in measurements and no series resistance is subtracted, so its tests have nothing to act on. The nearest risk is Rxx admixture into Rxy, which goes under the report-processing check and question 5.
- Skipped: protocol-parameter-sensitivity, since there is no automated pass/fail protocol.
- Skipped as superconductor-semiconductor, Josephson or interferometer specific: abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, one-end-only, trivial-andreev-band-gap-reopening, micromagnet-stray-field, full-shell-flux-andreev, chiral-plateau-superconductor-short (no superconductor here), island-states-coulomb-spacing, shapiro-landau-zener, shapiro-nonlinear-resistance, field-enhanced-supercurrent-resonances, charge-trap-fractional-shift, spin-orbit-length-pinning, exceptional-point-zero-mode, transparent-junction-pi-crossing, switching-jump-blind-region, false-poor-mans-majorana, local-probe-loophole, coulomb-dominated-interferometer, diode-vortex-screening.
- Checks: the paper's family (quantization) has no `checks` list, and the zbp list is specific to tunneling peaks. I walked only the three practice checks.

## Outside rows (library gaps)
1. Field-catalyzed Chern insulator from Hofstadter subbands. Source: Saito et al., arXiv 2007.06115 (abstract: "B catalyzes a first order phase transition from the spin- and valley-unpolarized B=0 state into the ferromagnetic state"). I took the tests from that paper's control (comparison with the B = 0 state) and from the zero-field anomalous Hall test used by He et al. 2109.08255 and Kuiri et al. 2204.03442. Status: tested in part. The fan onset near 0.3 T is the only part shown.
2. Unintended hBN alignment breaking C2. Source: Serlin et al., arXiv 1907.00261, full text (pp. on device characterization: hBN alignment tied to the ferromagnetism; hBN-moiré resistive peaks used to confirm alignment). Status: not tested (argued, not tested). The paper's argument is theoretical (Supp. Fig. 11).
3. Twist-angle difference or inhomogeneity between compared devices, including device quality that may hide a fan in D3. Sources: He et al., arXiv 2109.08255 (abstract, narrow θ window for SBCI) and Uri et al., arXiv 1908.04595 (abstract, about 0.1° local θ variations). Status: not tested (argued, not tested), from the D2/D5 sentence on p. 12.
- Candidate library gaps for moiré Chern work: an entry for field-induced Chern states versus zero-field band topology; an entry for substrate (hBN) alignment; a twist-angle inhomogeneity entry; a checks list for the quantization or Chern family (Streda slope, Rxy antisymmetrization, zero-field hysteresis).

## Hold-out
- No library source discusses this paper (all library sources predate June 2026 or concern other systems). None held out.
- Related-work searches turned up no version of this paper. arXiv 2606.23795 (He et al., visualizing SBCIs) came up in a title search; it is a different paper, and I did not open it.

## Related work, how checked
- 2109.08255: arXiv API abstract. ID, title and first author (Minhao He) confirmed; the description matches the abstract.
- 2204.03442: arXiv API abstract. ID, title and first author (Manabendra Kuiri) confirmed.
- 2007.06115: arXiv API abstract. ID, title and first author (Yu Saito) confirmed.
- 1907.00261: arXiv API abstract plus full text (v1 PDF), for the hBN alignment passages. First author M. Serlin confirmed.
- 1908.04595: arXiv API abstract. ID, title and first author (Aviram Uri) confirmed.
- I opened the abstract page through the arXiv API, not the HTML abs page. I waited about 3 s between API calls. I sent no email address to any service.

## Unsure
- Whether the D3 fan in Fig. 4f resolves CNP Landau levels at all. At 400 dpi they look washed out next to D1, but this is a visual judgment. It went in as a question, not as a status.
- Whether the "Onset field" test for the field-catalyzed lookalike counts as "part". The fan developing above 0.3 T bears on it but does not separate it, so I marked it part.
- Whether Rxy is antisymmetrized. Only positive B is shown, and the caption mentions longitudinal admixture, so I asked.
- The fine-tuned-plateau adaptation is a stretch. The C = +1 assignment rests mainly on the Streda slope, and the quantized value only supports it.

## Skill issues
- The quantization family (and any moiré or Hall family) has no `checks` list. The skill says to walk "the checks for the paper's family" and does not say what to do when the family has none. I walked the practice checks only.
- The scope rule says "adapt the matching entries", but the flags format wants library test text verbatim. For an adapted entry it is unclear whether to keep the library test wording or adapt it. I kept the wording.
- When the supplementary material is cited but not in the PDF, the skill does not say whether statements backed by "Supplementary Fig. X" count as shown. I treated them as stated, not shown, and said so in the report.
- "Use the title on the arXiv abstract page" conflicts with this run's rule not to open the paper's abstract page. I used the PDF title.
- The rule that a gap about data the paper doesn't show "doesn't lower any other status" is hard to apply to the fine-tuned-plateau test "Peak heights from other regimes and devices", which is by nature about other data. I marked it part, using the ν = −2 states in Fig. 4b.
- Outside rows allow a single `source` URL in flags.json. Row 3 rests on two papers, so I listed one.
