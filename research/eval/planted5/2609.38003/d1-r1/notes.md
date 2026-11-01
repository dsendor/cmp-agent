# Run notes: arXiv 2609.38003v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (updated 2026-10-24), 28 lookalike entries.
- Skill: cmp-assistant/skill/SKILL.md and report-template.md, read once at the start. scripts/read_mtx.py not used (no figure data).
- Date of run: 2026-10-24.

## What I read

- The paper, from the extracted text only (scratchpad planted2/blind/o15/paper.txt), per the task instructions. No abstract page and no PDF. Title taken from the first line of the text: "Reversible field-free superconducting diode effect controlled by an antiferromagnet". Version v1, from the arXiv stamp in the text (29 Sep 2026).
- Figures: only captions and axis fragments in the extracted text. Extended Data Figs. 1 to 5 also read from captions only.
- Page numbers come from the page markers in the extracted text: p. 3 = Fig. 2 and the SQUID and ZFC text; p. 4 = Fig. 3 and the preparation-field text; p. 5 = Fig. 4; p. 6 = conclusion; p. 7 to 8 = Methods; p. 11 = Extended Data Figs. 3 and 4.
- No data repository or ancillary files are linked in the text, so none were used.
- I didn't recognize the paper, which postdates my training, so I used no knowledge of its later history.

## Claims table (step 1)

| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| Field-free SDE after zero-field cooling, η ≈ 7%, switching distributions well separated | Fig. 3a and inset | [010] bar, 5 µm × 180 µm, CuMnAs 12.4 nm / AlAs 2.0 nm / Al 9.2 nm | 50 sweeps per polarity; 20 mK base only; switching threshold 50 µV; 0.2 s step delay; number of ZFC cooldowns not stated |
| Preparation field along [100] reverses the diode polarity; η up to about ±20% | Fig. 3b (±1 T), Fig. 3d (prep axis ±1 T) | same [010] bar | 8 sweeps averaged per point; measured at nominal H = 0; how H = 0 is established not stated |
| Preparation along [010] gives a weaker response with no systematic sign reversal | Fig. 3e (prep axis ±4 T) | same [010] bar | magnet type for the SDE runs not stated (a vector magnet is named only for the nonlinear transport) |
| Same anisotropy in an orthogonal bar, so it is tied to the crystal axes | Ext. Data Fig. 4 | [100] bar | dimensions not stated; prep ranges ±1 T ([100]) and ±4 T ([010]) from the axis fragments |
| The Néel state follows the same field history (Reven) | Fig. 4a (±4 T along [100]), 4b (±2 T along [010]), 4c (prep −5 to 5 T) | reference CuMnAs bar, different wafer with a 3 nm oxidized Al cap, 20 × 10 µm | 5 K, ±4 mA; one bar |
| Uniaxial easy axis along [100] | Ext. Data Fig. 5 | CuMnAs epilayer, 10 × 10 µm region | about 100 K |
| Proximity tuning by AlAs thickness | Fig. 2c, Ext. Data Fig. 3 (model) | 2.0 nm (Tc ≈ 350 mK) and 1.5 nm (no transition down to 20 mK) heterostructures | two wafers |
| Vanishing net magnetization | Fig. 2b | 3 mm × 5 mm pieces; "a series of samples taken from the wafer edge to the center" | bound 3×10−3 µB/Mn; SQUID temperature not stated |

Missing counts: number of bars fabricated and measured from the 2.0 nm wafer, number that showed the effect, number of cooldowns, temperature dependence of η, η against applied field, and a data or code availability statement.

My estimate for question 7: with 2 Mn per cell and a = 3.80 Å, c = 6.32 Å, the Mn density is 2.2×10^28 m^-3. The bound then gives M ≈ 610 A/m, so µ0M ≈ 0.77 mT. This matches the paper's own SQUID resolution of 10−7 emu over 1.8×10−7 cm³.

## Matching (step 2)

- Matched: diode-vortex-screening (diode family), fine-tuning-and-selection (always).
- Adapted: micromagnet-stray-field. It is written for zero-bias peaks at zero field, and I adapted it to the paper's claim that time reversal is broken without a net moment. The ordinary alternative is a small net or uncompensated moment, which gives a stray or exchange field. I kept its three tests.
- Outside the library: trapped flux or magnet remanence after the preparation field. Source: Jiang et al. 2025, arXiv 2512.05427, full text read. Its tests are taken from the controls that paper describes:
  - a graphene sensor, even in field, measured alongside to correct about 15 mT of magnet remanence (Appendix D);
  - Ic and ΔIc against applied field after each poling sign (Fig. 3);
  - comparison with a field configuration that traps no flux (out of plane, Appendix E).
- Not used as a separating test: the I ∥ H versus I ⊥ H comparison (the paper's orthogonal bars). Jiang et al. find the trapped-flux diode in both configurations (Sec. 2), so it does not separate this lookalike.
- Skipped, with reasons:
  - all zbp entries (abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, spin-orbit-length-pinning, exceptional-point-zero-mode, full-shell-flux-andreev): there is no tunneling spectroscopy and no zero-bias peak;
  - quantization entries (fine-tuned-plateau, series-resistance-subtraction): no quantized conductance; four-terminal switching currents;
  - nonlocal (one-end-only, trivial-andreev-band-gap-reopening), island, chiral, kitaev, and charge (charge-trap-fractional-shift, coulomb-dominated-interferometer): signatures absent;
  - shapiro entries (four): no microwave irradiation and no Josephson junction;
  - field-enhanced-supercurrent-resonances: its signature is a supercurrent that grows with field, read as triplet pairing, which this paper does not claim;
  - protocol-parameter-sensitivity: no automated pass/fail protocol;
  - local-probe-loophole: specific to Majorana modes and local probes.

## Status reasoning (step 3)

- Checks: the diode family has no `checks` block, so I walked only the three practice checks (report-counts, report-ranges, report-processing). All three are partly done.
- diode-vortex-screening: Not tested (data bear on it).
  - No plain Al control: the 1.5 nm sample is not superconducting, so it cannot serve as one.
  - No η against applied field, width or edge.
  - I chose "data bear on it" over "argued, not tested": the paper never names vortices or screening, but the orthogonal-bar data and the anisotropy argument (Ext. Data Fig. 4) bear on field-geometry mechanisms.
- Trapped flux or remanence: Tested in part.
  - The [010] preparation (Fig. 3e) is the closest analogue of Jiang's "no trapping" configuration, so I marked it "part": the residual field per axis and the coil used are unknown.
  - Both bars likely sit on one chip in the same magnet. If so, the crystal axes coincide with the lab and coil axes, and the two-bar comparison cannot separate crystal anisotropy from coil-specific remanence. This led to question 5.
- micromagnet-stray-field (adapted): Tested in part.
  - Hysteresis "part": M(H) shown for the film at an unstated temperature; the Reven hysteresis is on a different wafer.
  - Bound "part": a net-moment bound with no field at the Al.
  - No control without the magnetic layer.
- fine-tuning-and-selection: Tested in part. The second device (Ext. Data Fig. 4) is shown in full; counts are partial; selection is not described.

## Sources held out

- None skipped. The library sources for the matched entries all predate the paper (29 Sep 2026): Hou 2022/2023, Jiang et al. 2305.19970 (2023), Frolov 2309.09368 (2023), Akrap 2501.18631. I did not reopen them to check, so I went by dates. Akrap's v2 is dated 2026 in the library, and I judged it very unlikely to cite a September 2026 preprint.

## Related work checks (step 5)

- 2205.09276 Hou et al.: abstract page opened; ID, title and first author (Hou, Yasen) confirmed; the 1 Oe and Meissner-screening statements are in the abstract.
- 2512.05427 Jiang et al.: abstract page and full-text PDF opened; ID, title and first author (Jiang, Nan) confirmed. Abstract: poling-field sign control, trapped flux. Full text: ±1 T poling (Sec. 1) and the ≈ ±15 mT magnet remanence correction with graphene (Appendix D).
- 2205.12196 Golod and Krasnov: abstract page opened; title and first author (Golod, T.) confirmed; trapped Abrikosov vortex and switching on/off are in the abstract.
- 2206.00483 Narita et al.: abstract page opened; title and first author (Narita, Hideki) confirmed; polarity set by the magnetization direction of the ferromagnetic layers, per the abstract.
- 2601.03366 Sachin et al.: abstract page opened; title and first author (Sachin, Saurav) confirmed; zero-field diode, compensated T2 and nearly compensated T1 Mn3Pt, efficiencies up to 50%, "multiple contributing mechanisms", per the abstract.
- arXiv searches were done through export.arxiv.org with about 3 s between calls. A search for Jeon et al. (proximity-magnetized Pt Josephson diodes) and one for Godinho et al. returned no match, and I did not list either.

## Library gaps

- The diode family has no `checks` block. Candidates: a plain parent-superconductor control under the same protocol; η against small applied field around a calibrated zero; a thermal cycle above Tc to erase trapped flux; the residual-field calibration of the magnet.
- No entry for trapped flux or superconducting-magnet remanence after a poling or preparation field (source: arXiv 2512.05427; also 2205.12196 for trapped vortices).
- micromagnet-stray-field is scoped to zero-bias peaks. A diode version (a net or uncompensated moment of a magnetic layer, with tests that convert the moment bound into a field and compare it with the field threshold of a plain film) would cover claims of "magnetization-free" diodes.

## Unsure

- References 28 to 30 (Hou et al. 2023; Jiang et al., PRB 112, 235313; Li et al., Adv. Mater. 2026) are in the reference list, but I could not find them cited in the extracted text. There is also a double space before "We therefore conclude" on p. 6. Either a passage was lost in extraction or the citations are elsewhere. I judged the text as given.
- Whether the SDE cryostat has a vector magnet, or the sample was rotated between [100] and [010] runs.
- The SQUID temperature, and whether Fig. 2b comes from the same wafer piece as the bars.
- Exact preparation ranges come from axis fragments in the extracted text, so they may be misread.

## Skill issues

- The diode family has a lookalike entry but no `checks`. The skill does not say whether to adapt checks from another family or walk only the practice checks. I walked only practice and said so in the report.
- The scope rule ("adapt the matching entries, say so in one sentence under What this is") is written for out-of-scope measurements. It is unclear whether adapting a zbp entry for an in-scope diode paper needs the same sentence. I added one.
- Status rules: it is unclear whether a test the paper shows for another purpose, without naming the lookalike, should count. An example is the [010] preparation for the trapped-flux row. I counted it as "part".
- "argued, not tested" versus "data bear on it": the choice is unclear when the paper argues against a broad class (field-geometry effects) without naming the specific lookalike.
- Outside rows: the skill says to take tests "from the control that paper describes", but a paper may describe a control that does not separate the lookalike (Jiang's I ∥ H test). I left such a control out of the tests and noted why.
- The skill says to read the abstract page and PDF. The task forbade both, so the title and version come from the text.
- Word target (600 to 900 outside the table): the template's fixed paragraphs take about 150 words of it. This report is about 930 words outside the table, counting headings.
