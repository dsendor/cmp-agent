# Run notes: arXiv 2508.17861v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (updated 2026-10-24), 28 lookalike entries.
- Skill: cmp-assistant/skill/SKILL.md and report-template.md, read once at the start. I did not use scripts/read_mtx.py because no figure data came with the paper.
- Date of run: 2026-10-25.

## What I read

- v1 PDF (15 pages) and its extracted text, from the provided scratchpad copies. I rendered pages 10 to 13 (Figs. 1 to 4) at 150 dpi and read the figure details from those images.
- The PDF has no supplementary material. The paper cites Supplementary Figs. 1 to 11 and Supplementary Note 4. I could not see them.
- I did not open the arXiv abstract page for this paper (the task forbids it). The title in the header is from the PDF: "Unveiling the landscape of Mottness and its proximity to superconductivity in 4Hb-TaS2".
- No data repository: the paper says data and code are "available from the corresponding author upon reasonable request". I counted devices and ranges from the figures only.
- I did not recognize the paper and do not know its later history.

## Claims table (step 1)

| Claim | Figures | Data and counts | Missing counts |
|---|---|---|---|
| C1. Filling-controlled evolution from a depleted narrow band (about 0.2 e per SoD) to Hubbard bands, with constant U ≈ 190 ± 10 meV and symmetric weight transfer | Figs. 1d, 2b-e, 3a-e | One 100 nm field of view with about 4000 clusters (Fig. 2a); "more than one hundred typical" spectra in Fig. 2d (caption: "one hundred clusters"); about 40-50 points in Figs. 3c-e; energy range ±1 V, analysis window ±0.25 eV; setpoints Vs = -1000 mV, It = 2.5 nA, Vmod = 2 meV | Number of crystals, cleaves, fields of view, tips; which STM system for each figure; how the "typical" spectra were chosen |
| C2. The central peak is the Brinkman-Rice coherent peak and is not a Kondo resonance | Figs. 3e, 3f, 3h | Fig. 3f: 8 clusters at 0.3 K, FWHM 1.3 to 3.4 meV (Fano fits); Fig. 3h: one cluster (ε = -76 meV), 7 temperatures from 0.3 to 4.2 K, HWHM about 0.65 to 1.7 meV against a Kondo line near 2.4 meV; T_K about 40 K computed from the Anderson-model formula using W0 | Temperature series on other clusters; whether the widths were corrected for thermal or modulation broadening (Methods: Vmod 0.05 to 0.2 meV below 4 K) |
| C3. Doping comes from Se substitution, which inhibits charge transfer | Text p. 4, Supplementary Note 4 | 12% ZBP clusters against an estimated 13% Se-affected clusters; higher-Se samples and uniaxial strain in SI only | Se fraction: text says 0.5% of S substituted, Methods says nominal Se was 1% of S; number of samples in the controls |
| C4. A proximity-induced SC gap on the 1T layer (up to about 0.35 meV) shrinks with filling and vanishes on Hubbard-band clusters | Figs. 4a, 4b, 4d, 4e | Fig. 4b: 3.0 K and 2 T out of plane; Fig. 4d: one line cut; Fig. 4e: "nearly 30 clusters"; 1H gap about 0.5 meV, Fig. 4c line cut | Field range beyond 2 T; field direction other than out of plane |
| C5. ZBP clusters are paramagnetic (Zeeman splitting with g about 2) and show short-range order | Supplementary Figs. 10 and 11 (not in the PDF) | Text only | Field range and direction; number of clusters |

## Entries matched, adapted and skipped

- Scope: the paper is STM spectroscopy of a doped Mott state with no topological claim. I said so in one sentence under "What this is".
- Adapted: kondo-resonance. The library's "dot" became a SoD cluster and the superconducting contact became the 1H layer. "Even-odd occupancy" became the peak's filling dependence (Figs. 3e, 3f). The flags use the library test texts verbatim.
- Kept: fine-tuning-and-selection (always applies).
- Checks adapted: zbp-dot-search (filling dependence), zbp-wide-ranges (whole cluster population, temperature and field ranges), zbp-raw-conductance (setpoint, normalization, raw spectra). All three practice checks were kept.
- Checks skipped as not applicable: zbp-both-ends, zbp-transparency, zbp-nonlocal-gap (no wire ends, no tunable junction, no nonlocal geometry), and every shapiro, kitaev and charge check.
- Lookalikes skipped, with reasons: abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, weak-antilocalization, spin-orbit-length-pinning, exceptional-point-zero-mode, micromagnet-stray-field, full-shell-flux-andreev, local-probe-loophole (all about Majorana readings of nanowire or hybrid-device peaks; there is no Majorana claim here); fine-tuned-plateau, series-resistance-subtraction (no quantization claim); one-end-only, trivial-andreev-band-gap-reopening (no wire ends, no nonlocal data); island-states-coulomb-spacing; shapiro-landau-zener, shapiro-nonlinear-resistance, transparent-junction-pi-crossing, switching-jump-blind-region; field-enhanced-supercurrent-resonances; charge-trap-fractional-shift, coulomb-dominated-interferometer; chiral-plateau-superconductor-short; false-poor-mans-majorana; diode-vortex-screening; protocol-parameter-sensitivity (no pass/fail protocol).

## Sources held out

- None. I did not open the library sources. From their titles and quotes, none discusses this paper; all are on topological transport and almost all predate it.

## Related work and how I checked it

I found all five through the export.arxiv.org API (title searches, about 3 s apart). For each I opened the arXiv abstract page and confirmed the ID, title, first author and that the abstract supports the one-line description. I checked abstracts only, no full texts.

- 2103.11989, Vaňo, "Artificial heavy fermions in a van der Waals heterostructure": abstract checked.
- 2302.14072, Crippa, "Heterogeneous Ta-dichalcogenide bilayer: heavy fermions or doped Mott physics?": abstract checked. This is the arXiv version of the paper's ref. 37; the arXiv title differs from the journal title.
- 2303.01447, Nayak, "First Order Quantum Phase Transition in the Hybrid Metal-Mott Insulator Transition Metal Dichalcogenide 4Hb-TaS2": abstract checked. It is the paper's ref. 28.
- 2207.00096, Wan, "Evidence for ground state coherence in a two-dimensional Kondo lattice": abstract checked.
- 2310.09326, Turco, "Demonstrating Kondo behavior by temperature-dependent scanning tunneling spectroscopy": abstract checked. It is the paper's ref. 41.
- Opened and not used: 1606.07402 (Macdonald et al., set point artifacts in FT-STS). It is about dispersing artifacts in map acquisition, too far from point-spectrum normalization to support a row.
- No search result was this paper or a version of it.

## Library gaps

- Extrinsic (thermal and lock-in) broadening of a zero-bias peak width used to argue for or against Kondo (source: Turco et al., arXiv 2310.09326). The library has no STM lineshape entries.
- Tip-induced switching of correlated cluster states (source: Nayak et al., arXiv 2303.01447). STM tip-field and tip-height effects are absent from the library.
- More broadly, the library has no family for STM spectroscopy of correlated materials (Kondo versus Mott quasiparticle peaks, setpoint and normalization effects).

## Things I was unsure of

- Physics I added myself: the thermal smearing of about 3.5 k_B T full width (about 1.3 meV at 4.2 K), and k_B T_K ≈ 3.4 meV for 40 K. The Fig. 3h values (HWHM 0.65 to 1.7 meV, gray line near 2.4 meV) are read off the rendered figure and are approximate.
- The narrowing of the peak toward half filling is not unique to Brinkman-Rice physics: in an Anderson impurity, T_K also falls toward the symmetric point. That is why I did not count the filling test as separating Kondo by itself.
- Zeeman splitting with g about 2 fits either reading. A small-T_K Kondo peak would also split at modest fields.
- The paper claims a peak width "an order of magnitude" below the Kondo expectation, but Fig. 3h shows a factor of about 1.5 to 4. I turned this into a question.
- Labels: the text cites "Fig. 3g" for the vanishing spectral weight, but the caption puts it in 3e (3g is DMFT). The ratio U/W0 is "~2" in the text, while DMFT uses 1.67 and U/W0 from 190/80 is about 2.4.

## Skill issues

- Scope: the skill handles "a different kind of measurement" by adapting entries. It does not say what to do when the paper is not a topological claim at all and the library's "lookalike" (here Kondo) is the competing explanation the authors argue against. I treated the authors' claim as the signal and Kondo as the lookalike.
- Supplementary material that the text cites but the PDF lacks: the skill says a sentence alone doesn't count, and that unclear tests get "part". I marked tests that rest on SI figures "part" and said why. A rule for this case would help.
- "Evidence presented" is ambiguous when one subclaim (not Kondo) rests on one cluster (Fig. 3h) while the main claim spans about 100 clusters. I counted the temperature test as "part".
- Checks: the skill says to walk the checks for "the paper's family", but there is no family for this paper. It is unclear whether to list inapplicable checks in flags.json as "not done". I omitted them and listed them here.
- flags.json asks for library test text. For an adapted entry the meaning changes (even-odd occupancy as filling dependence), so I kept the library text and explained the adaptation in the report.
- The template's "Use the title on the arXiv abstract page" conflicts with this run's ban on opening that page. I used the PDF title.
- The skill says to write reports/<id>.md and reports/<id>.notes.md. This run told me to return them inline, so I followed the run instructions.
