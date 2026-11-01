# Run notes: arXiv 2609.38003v1

AI only. Lookalike assistant run, 2026-10-23. Library meta.version 0.4 (updated 2026-10-23), 28 lookalike entries.

## What I read
- skill/SKILL.md, skill/report-template.md, library/lookalikes.yaml (all entries and the full `checks` section), read once at the start.
- Paper: the supplied extracted text (paper.txt: main text, Methods, Extended Data Figs. 1 to 5 captions, references) and the supplied arXiv abstract page (abs.html). Title on the abstract page: "Reversible field-free superconducting diode effect controlled by an antiferromagnet". v1, submitted 29 Sep 2026, "14 pages, 4+5 figures".
- No PDF was provided and I did not fetch the paper in any form. Figure details come from captions; axis ranges were read only loosely from the extracted text.
- Supplementary material: the Extended Data are in the text. No separate supplement, no ancillary figure data, no data repository link, so read_mtx.py was not used and no counts came from data files.
- Page numbers come from the page markers in the extracted text (p. 1 abstract and intro, p. 2 Fig. 1, p. 3 Fig. 2 and ZFC diode, p. 4 Fig. 3, p. 5 Fig. 4, p. 6 discussion, p. 6 to 8 Methods, p. 9 to 12 Extended Data). They may be off by one against the PDF.

## What I couldn't open
- Nothing failed. Two arXiv API searches returned 2609.38003 itself as a hit; I did not open it.

## Claims table (step 1)
| # | Claimed signal | Figure | Device | Counts and ranges |
|---|---|---|---|---|
| 1 | Field-free diode after zero-field cooling, η ≈ 7%, separated switching distributions | Fig. 3a, p. 3 | 5 µm x 180 µm CuMnAs(12.4 nm)/AlAs(2.0 nm)/Al(9.2 nm) bar along [010], four-terminal | 50 sweeps per polarity; 20 mK base; switching at 50 µV threshold, 0.2 s step delay |
| 2 | ±1 T preparation along [100] swaps the ordering of the switching currents at H = 0 | Fig. 3b, p. 4 | same bar | 8 sweeps averaged per point |
| 3 | η at H = 0 reverses with preparation sign along [100], approaching ±20%; weak, non-reversing for [010] | Fig. 3c-e, p. 4 | same bar | [100] prep axis about ±1 T, [010] prep axis about ±4 T (from axis labels); temperature: base only |
| 4 | Orthogonal bar along [100] shows the same qualitative axis dependence | Extended Data Fig. 4, p. 4-5, p. 11 | second bar, size and chip not stated | not stated |
| 5 | Reven hysteretic along [100], weak along [010]; remanent Reven reverses with preparation sign | Fig. 4a-c, p. 5 | reference CuMnAs bar, 20 µm x 10 µm, from "a CuMnAs wafer with 3 nm fully oxidized Al cap" (p. 8) | 5 K, vector-magnet cryostat, ±4 mA, prep −5 to 5 T |
| 6 | Uniaxial Néel easy axis along [100] | Extended Data Fig. 5 | CuMnAs epilayer, 10 µm x 10 µm region | about 100 K |
| 7 | Net moment upper bound 3x10^-3 µB/Mn | Fig. 2b, p. 3, p. 7 | 3 mm x 5 mm pieces of the heterostructure wafer, "a series of samples" edge to center | temperature and field history not stated |
| 8 | Proximity tuning: 1.5 nm AlAs not superconducting to 20 mK, 2.0 nm Tc ≈ 350 mK | Fig. 2c, Extended Data Fig. 3 | two heterostructures | model with NS = 1 to 8 layers |

Missing counts: devices fabricated, bars measured, bars showing the effect, chips, cooldowns, repeats of the excursion loops, whether the two diode bars share a chip.

## Entries matched, skipped, adapted
- Matched: diode-vortex-screening (diode family), fine-tuning-and-selection (always).
- Adapted: micromagnet-stray-field. Its signature is zero-bias peaks and its dots-specific control does not apply; I kept the shared physics (stray fields from magnetic material breaking time-reversal symmetry at zero applied field) and its controls of measuring the magnet's hysteresis and comparing with devices without the magnet.
- Skipped, no tunneling spectroscopy or Majorana claim: abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, spin-orbit-length-pinning, exceptional-point-zero-mode, full-shell-flux-andreev, fine-tuned-plateau, series-resistance-subtraction, one-end-only, trivial-andreev-band-gap-reopening, local-probe-loophole.
- Skipped, other families with no matching signal: island-states-coulomb-spacing, shapiro-landau-zener, shapiro-nonlinear-resistance, transparent-junction-pi-crossing, switching-jump-blind-region, field-enhanced-supercurrent-resonances, charge-trap-fractional-shift, coulomb-dominated-interferometer, chiral-plateau-superconductor-short, false-poor-mans-majorana.
- Skipped: protocol-parameter-sensitivity. There is no automated pass/fail protocol here; the related point (η depends on a 50 µV threshold and a sweep delay chosen "empirically") went into question 3.
- Checks: the library has no `checks` list for the diode family, so I walked only the practice checks (report-counts, report-ranges, report-processing), all Partly.

## Scope adaptation
The paper claims antiferromagnetic control of a diode in conventional s-wave Al, not exotic pairing or a topological state. The diode family covers it; I said so in one sentence under "What this is".

## Sources held out
None. I searched the library for CuMnAs, 2609.38003, Krizek and Vaitiekėnas and found no source that discusses the paper under review.

## Related work and outside lookalikes: how each was checked
- 2205.09276 (Hou et al., library source): abstract page opened; ID, title, first author (Hou, Yasen) confirmed; description from abstract.
- 2512.05427 (Jiang et al.; also the paper's ref. 29): abstract page and full text opened. Confirmed the ±1 T in-plane poling field, the sign control, and the trapped-flux attribution (abstract, Results). Confirmed the magnet hysteresis: "Such hysteresis can often arise from a stray magnetic field due to the superconducting magnet." and "the magnetic field values of ≈ ±15 mT were shifted" (Appendix D). Source for both outside rows. Their control for magnet hysteresis is a field-even reference (few-layer graphene) measured at the same time. Their control for trapped flux is poling-field sign reversal plus out-of-plane tests; the warm-above-Tc check in my table is my adaptation.
- 2205.12196 (Golod and Krasnov): abstract page and first page of full text opened; title and authors confirmed.
- 2610.30556 (Zapata et al., posted 2026-10-22, after the paper under review): abstract page and full text opened; confirmed the AlN-spacer statement in the abstract; grep for CuMnAs and the paper's authors found no mention of the paper under review.
- 2601.03366 (Sachin et al.; the paper's ref. 10): abstract page opened; description from abstract.
- Also opened, not listed: 2506.17651 (Li et al., the paper's ref. 30, stray fields from a perpendicular Co layer), abstract only.

## Library gaps
- The diode family has one entry and no `checks`. Candidates with opened sources:
  - Flux trapped by a poling or preparation field gives a sign-switchable zero-field diode (2512.05427, 2205.12196).
  - Remanent field of the superconducting magnet after a field excursion (2512.05427, Appendix D).
  - Stray fields from a magnetic layer, which pass through a spacer that cuts proximity coupling (2610.30556, 2506.17651).
- Possible diode checks: η against small applied fields near zero in all three directions; a plain parent-superconductor control through the same protocol; warming above Tc between preparation and readout; calibrating the field at nominal zero; sensitivity to the switching threshold and sweep rate.

## Unsure
- Whether 1 T in-plane takes the proximitized Al above its critical field. The paper doesn't state the critical field, so I don't know whether flux trapping during the excursions is likely.
- Whether magnet remanence could produce the [100]/[010] contrast. That depends on how the chip sits in the vector magnet, which the text doesn't give, so I put it as question 7 and didn't claim it.
- The figure ranges in the claims table come from axis labels in the extracted text and may be wrong.
- Recognition: I did not recognize this paper and used no knowledge of its later history.

## Skill issues
- Step 3 says to walk the checks "for the paper's family", but the diode family has none. The skill doesn't say whether to fall back to practice checks only, which is what I did, or to draft family checks.
- The scope rule covers "a different kind of measurement". It doesn't cover a claim in a covered family that isn't topological (here, AFM control of a conventional superconductor). The template's fixed "in topological transport" wording then reads oddly.
- "Match on the physics, not the words" doesn't settle cases like micromagnet-stray-field, whose lookalike physics fits but whose signature and control are dot-specific. I adapted it and said so; a rule for adapt versus outside row would help.
- One outside source (2512.05427) backs two outside rows. The skill doesn't say whether that is fine.
- Step 6 says to ask the four standard questions "unless the paper already answers them (then say where)". It doesn't say how to handle partial answers. I kept the question and pointed to the two bars shown.
- The skill asks for page numbers. With text-only input, page numbers come from extraction markers. The skill could say how to cite pages when only text is available.
- The word target (600 to 900 outside the table) doesn't say whether the header, headings and related-work titles count; with them, this report is about 916 words.
