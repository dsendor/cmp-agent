# Run notes: arXiv 2509.13303v1

## Library and inputs
- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (updated 2026-10-24), 28 lookalikes, checks for families zbp, shapiro, kitaev, charge and practice.
- Read: skill/SKILL.md and skill/report-template.md, the full library, and both paper files supplied by the caller. The text file was read in full. I rendered every PDF page to PNG (pdftoppm, 80 dpi) and zoomed into Fig. 4 (p. 5) and Supp. Fig. 4 (Supp. p. 4) at 250 dpi to read the figure details.
- Not read, as instructed: the arXiv abstract page, PDF and HTML of this paper, and any journal or later version. The report title is the PDF title, shortened. I could not check it against the abstract page.
- Page convention: main text pages 1 to 9 are the printed page numbers. The supplement has its own printed numbering, cited as "Supp. p. N" (Supp. p. 1 is PDF page 11).
- No figure data, ancillary files or data repository are linked, so read_mtx.py was not used.
- Recognition: I did not recognize this paper or know of any later history.
- Working files are in /tmp/claude-0/-home-user/24b43eef-50bb-5f66-84b8-aad72ef55ba1/scratchpad/work-ref-2509.13303/ (page renders, two downloaded related-work PDFs and their text, and report.txt).

## Claims table (step 1)
| Claim | Figures | Sample | Counts and ranges | Missing |
|---|---|---|---|---|
| Two-gap tunneling spectrum on 1H termination, Δ1 = 490 µeV, Δ2 = 300 µeV | Fig. 4a, 4c; Supp. Fig. 2 (single-gap fit, Teff 900 mK); Supp. Fig. 3 (150 spectra on a 45 nm line) | Cleaved CVT crystal, tungsten tip | T = 0.3 K only; bias ±1.5 mV (±2 mV in Supp. Fig. 3); Iset 50 pA, V -1.5 mV (Fig. 4a), -2 mV (Supp. Fig. 3); lock-in 907 Hz (Methods) | Crystals, cleaves, tips, areas; lock-in amplitude for Fig. 4; two-gap fit weights and Teff; no STM temperature series |
| Gap field dependence on both terminations, Hc ≈ 3 kG | Supp. Fig. 4 | Same STM setup | B ∥ c at 0, 1, 2, 3 kG; "T 0.5K" | Field steps below 1 kG; per-gap analysis |
| Two gaps from concave Hc2(T) | Fig. 2b; Supp. Fig. 1; Supp. Table I | Single crystal(s), four-probe | H ∥ ab to 14 T, 0.71 to 3.05 K; H ∥ c to 1 T, 0.63 to 2.94 K; 50% criterion; Tc fixed 3.05 K | Number of crystals |
| Ising superconductivity, in-plane Hc2 1.95 times Pauli limit; anisotropy 19 | Fig. 2b and inset (angle at 2 K, 2D Tinkham fit) | Same | Angle 0 to 90 degrees at 2 K | Angle data at other temperatures |
| Decoupled 1H layers: spin-valley locking, no kz dispersion | Fig. 3 (spin-ARPES, 25 eV, 10 to 30 K); Supp. Fig. 6 (49 to 59 eV) | Two beamlines (Elettra APE-LE, SOLEIL CASSIOPEE) | Sherman function 0.27 | Number of samples |
| Singlet-triplet mixing reproduces two gaps at t⊥ = 0 and merges near t⊥ = 0.8λ | Fig. 5; Supp. Figs. 7 to 12 | Theory | t = 0.25 eV, λ = 0.3 eV, V0 = 0.25t, V1 = V2 = 0.3t, 40×40 grid, Γ = 1 meV | Parameter-sensitivity scan beyond t⊥ |
| Intrinsic SnS superconductivity, Δ = 440 µeV | Fig. 4b; Supp. Figs. 4a and 5 (vortices at 0.1 T) | Same | ξ 35 ± 5 nm (p. 4) vs 45 ± 10 nm (Supp. p. 5) | Number of areas |

## Entries matched, skipped, adapted
- Matched directly: fine-tuning-and-selection (always applies). I adapted it by reading "devices" as crystals, cleaves, tips and areas.
- Checks: no library family covers a spectroscopic gap structure or pairing-symmetry claim. Only the practice checks (report-counts, report-ranges, report-processing) apply. They were applied to STM, ARPES and transport.
- Skipped, because each signature needs a device experiment not present in this paper:
  - zbp family: abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, micromagnet-stray-field, full-shell-flux-andreev, spin-orbit-length-pinning, exceptional-point-zero-mode. No zero-bias peak is claimed.
  - quantization family: fine-tuned-plateau, series-resistance-subtraction. No quantized conductance.
  - nonlocal family: one-end-only, trivial-andreev-band-gap-reopening. No nonlocal conductance.
  - island-states-coulomb-spacing. No islands.
  - Shapiro and Josephson entries: shapiro-landau-zener, shapiro-nonlinear-resistance, switching-jump-blind-region, transparent-junction-pi-crossing. No junctions.
  - field-enhanced-supercurrent-resonances. The family is "triplet pairing", but the signature is switching current growing with field, which is not measured here.
  - charge-trap-fractional-shift and coulomb-dominated-interferometer. No charge claim.
  - chiral-plateau-superconductor-short. No QAH.
  - false-poor-mans-majorana. No dot chain.
  - diode-vortex-screening. No diode.
  - local-probe-loophole. This entry is about Majorana separation. Its local-probe logic is loosely related, but no Majorana claim is made.
  - protocol-parameter-sensitivity. No pass/fail protocol.
- Statuses and tests for fine-tuning-and-selection:
  - Devices and datasets measured: no, because no counts are given.
  - How the shown data were chosen: part. Fig. 4a is the average of 150 spectra along one 45 nm line, but the paper does not say how that area or sample was chosen.
  - A second device or dataset shown: part. Supp. Fig. 3 individual spectra and the zero-field curve in Supp. Fig. 4b are other datasets from the same crystal. No other crystal is shown.

## Outside rows (library gaps)
1. Conventional multiband or anisotropic s-wave gap, with gaps on different Fermi pockets (Γ vs K).
   - Source: Guillamon et al. 2008, arXiv 0807.1809, abstract and full text read. Quote (p. 3): "This gives strong evidence that two different superconducting gaps (±(0.97 ± 0.03) meV and ±(0.53 ± 0.03) meV) open at different parts of the Fermi surface of 2H-NbS2."
   - Tests come from that paper's control: temperature dependence of both d(LDOS)/dE features to Tc, and assigning the gaps to Fermi-surface sheets.
   - Status: Not tested (argued, not tested). The authors argue against it on Supp. p. 10 and through literature comparisons of interlayer coupling (pp. 5 and 7).
   - Unsure: the authors write that this mixing "can also lead to a variation of the gap", which could also be read as "Left open by the authors". I chose "argued" because the next sentence argues against it.
2. Proximity coupling of the surface 1H layer to the superconducting SnS layer (McMillan coupled-layer two-feature spectrum).
   - Source: Tao et al. 2022, arXiv 2203.05171, abstract and full text read. Quote (p. 5): "Although originally developed to describe the superconducting proximity effect in single-band metallic systems, the McMillan model has more recently been successfully applied to describe intrinsic multi-band superconductivity in layered two-band superconductors".
   - Tests come from that paper's control: a joint McMillan fit, and comparing the same layer on a weakly coupled substrate (WTe2/HOPG vs WTe2/NbSe2).
   - Status: Not tested (argued, not tested). The p. 7 argument is aimed at the SnS gap's origin, but it argues against interlayer proximity in general. The data also bear on it (Fig. 4a and 4b).
3. Considered, not added as a row: alternative origins of upward Hc2 curvature, which the authors themselves name as refs 63 to 66.
   - Those refs (1975 to 1986) have no arXiv versions, and I opened no paper that shows it, so I raised it as question 8.
   - This is a library gap.
4. Considered, not added: an anisotropic single gap plus thermal or lock-in broadening mimicking a second kink. I had no opened source, so it went into question 5.
- Library gap, general: the library has no family for "two-gap or anisotropic tunneling spectrum taken as unconventional (triplet or mixed-parity) pairing". Candidate entries are multiband s-wave, interlayer proximity (McMillan), broadening and fit-model dependence, and Hc2 curvature alternatives.

## Sources held out
- None. I did not open any library source, and only used their library text for the fine-tuning row. No library source is likely to discuss this paper, but I did not verify that by fetching them.

## Related work, how checked
- Each abstract page was opened on arxiv.org, and the ID, title and first author were confirmed:
  - 0807.1809 (Guillamon): abstract and full text.
  - 2203.05171 (Tao): abstract and full text.
  - cond-mat/0403700 (Kohen): abstract.
  - 2104.00328 (Kuzmanović): abstract.
  - 1906.02065 (Devarakonda): abstract.
- Also opened but not listed: 2412.08450 (Wang et al., 4Hb-TaS2 thermal conductivity, multiband gapless), abstract only.
- Search hits skipped without opening:
  - 2509.13303v1 itself.
  - 2602.22999 (pressure on (SnS)1.15(TaS2)) and 2610.17879 ((SnS)1.17NbS2 STM). These are later work on the same or a sister compound that could discuss this paper.
- The arXiv API often returned empty results for multi-term queries. I used narrower author and title queries and the website search.

## Figure readings I am unsure of
- Supp. Fig. 4b, zero-field 1H spectrum: by my reading, the coherence peaks are near ±0.4 to 0.45 mV. Fig. 4a shows ±0.53 mV. The peak tops are clipped in the figure, so I phrased this as a question.
- Fig. 4c: the SnS d2I/dV2 peak (about 0.4 mV) sits between the 1H Δ2 (about 0.27 mV) and Δ1 (about 0.5 mV) marks.

## Skill issues
- Scope: the skill says to "adapt the matching entries", but for this paper essentially no entry's signature matches. The skill doesn't say what to do when the matched set is only the practice entries. I treated the outside-row route as the main tool.
- The checks are organized by family, and there is no family for spectroscopy or pairing-symmetry claims. flags.json therefore lists only the practice checks.
- Step 7 says to use the title on the arXiv abstract page, which the test instructions forbid opening. I used the PDF title.
- The outside-row rule ("take its tests from the control that paper describes") can yield tests that confirm two gaps without separating the mechanisms. Guillamon's controls show two gaps exist, not why. I picked the parts of each paper's control that separate the mechanisms best, and said so here.
- Wording: "devices" fits bulk crystals poorly. A note to read it as samples, cleaves and tips would help.
- The 600 to 900 word target is tight with three checks, eight questions and five related-work lines. The report is about 960 words outside the table, counting headers.
- The status rule doesn't say which note to pick when an argument and figures that could test it both exist ("argued" vs "data bear on it").
