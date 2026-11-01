# Run notes: arXiv 2609.38003v1

- Library: lookalikes.yaml, meta.version 0.5 (28 lookalike entries). Skill: SKILL.md and report-template.md, each read once at the start.
- Run date: 2026-10-24.

## What I read

- The paper: only the extracted text supplied by the caller (paper.txt, v1, dated 29 Sep 2026). No PDF, abstract page or HTML. Per the caller's instructions I did not fetch the paper. Figure details come from captions and the axis labels that survived text extraction. Extended Data Figs. 1 to 5 are in the text; I found no separate supplement and no ancillary data files.
- Title: taken from the paper text ("Reversible field-free superconducting diode effect controlled by an antiferromagnet"). The skill asks for the title on the arXiv abstract page, which I was told not to open. One arXiv API search for related work (abs:"remanent field" AND abs:"superconducting magnet", and a second diode search) listed this paper's ID and title among its results. I did not open it.
- No data repository is linked, so no counting from data. read_mtx.py was not needed.
- I did not recognize the paper and have no knowledge of its later history.

## Claims table (step 1)

| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| Field-free diode after zero-field cooling, η ≈ 7%, switching distributions well separated | Fig. 3a and inset (p. 3 to 4) | 5 µm × 180 µm CuMnAs(12.4 nm)/AlAs(2 nm)/Al(9.2 nm) bar along [010], four-terminal, 20 mK | 50 sweeps per polarity; inset axis about 27 to 31 µA; one cooldown implied; number of bars fabricated not given |
| Polarity reverses with sign of preparation field along [100] | Fig. 3b, 3d (p. 4) | Same bar | Readout at H = 0 after ±1 T; Fig. 3d prep range ±1 T; 8 sweeps averaged per point; Fig. 3b axis about 16 to 23 µA; η up to about ±20% |
| Weak, non-reversing response for preparation along [010] | Fig. 3e (p. 4) | Same bar | Prep range ±4 T |
| Same axis dependence in an orthogonal bar | Extended Data Fig. 4 (p. 11) | Bar along [100], same wafer presumably | ±1 T [100], ±4 T [010]; zero-field-cooled data and switching distributions not shown |
| Néel state of CuMnAs has the same anisotropic remanence | Fig. 4a to c (p. 5) | Separate CuMnAs bar, 20 µm × 10 µm, from a different wafer with 3 nm oxidized Al cap, no AlAs barrier, 5 K, ±4 mA | Field sweeps ±4 T [100], ±2 T [010]; remanent readout after −5 to 5 T prep |
| Easy axis along [100] | Extended Data Fig. 5 (p. 12) | XMLD-PEEM on "the CuMnAs epilayer", about 100 K | Which wafer is not stated |
| Negligible net moment | Fig. 2b (p. 3), Methods (p. 7) | 3 mm × 5 mm wafer piece | Upper bound 3×10−3 µB/Mn; several pieces edge to center |
| Proximity tuned by barrier | Fig. 2c (p. 3), Extended Data Fig. 3 | 2.0 nm (TC ≈ 350 mK) and 1.5 nm (no transition to 20 mK) wafers | Two barrier thicknesses only |

Missing counts: bars fabricated and measured, cooldowns, bars that failed, temperature series, η at nonzero measurement field, reason for the ±1 T against ±4 T prep ranges.

## Entries matched, skipped, adapted

- Matched: diode-vortex-screening (diode family) and fine-tuning-and-selection (always). Practice checks walked: report-counts, report-ranges, report-processing. The diode family has no `checks` section.
- Skipped, as not applicable to a planar superconducting film without tunneling spectroscopy, Josephson junctions under microwaves, islands, quantum dots or quantum Hall devices: all zbp entries (abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, spin-orbit-length-pinning, exceptional-point-zero-mode, full-shell-flux-andreev), quantization (fine-tuned-plateau, series-resistance-subtraction), nonlocal (one-end-only, trivial-andreev-band-gap-reopening), island, shapiro (four entries), kitaev, charge (two entries), chiral, field-enhanced-supercurrent-resonances (the claim is not a supercurrent growing with field), protocol-parameter-sensitivity (no automated pass/fail protocol), local-probe-loophole (Majorana-specific).
- Considered and not used: micromagnet-stray-field. Its stray-field idea fits, but its signature is a zero-bias peak and its mechanism is Andreev states in quantum dots. I covered the stray-field idea with an outside row sourced to Zapata et al.
- Adapted: none. The paper is transport, inside the library's scope.

## Sources held out

None. No library source cites this paper. Hou et al. (2205.09276) is cited by the paper as ref. 28, and Jiang et al. as ref. 29; neither discusses it.

## Related work checks

- 2205.09276 Hou et al.: abstract page opened; ID, title, first author confirmed; description checked against the abstract.
- 2512.05427 Jiang et al.: abstract page and full text (PDF) opened; poling-field sign control (p. 3 to 4) and the graphene zero-field calibration ("Such hysteresis can often arise from a stray magnetic field due to the superconducting magnet", p. 4; Appendix D) checked in the full text.
- 2205.12196 Golod and Krasnov: abstract page opened and checked.
- 2506.17651 Li et al.: abstract page opened and checked (it is the paper's ref. 30).
- 2610.30556 Zapata et al.: abstract page opened and checked (posted after the paper under review; described only for its own results).

## Library gaps

- No ordered `checks` for the diode family. Natural ones: zero-field calibration, warming above TC to erase trapped flux, plain-superconductor control under the same protocol, η against measurement field near zero.
- Trapped flux set by a poling or preparation field (Jiang et al. 2512.05427; Golod and Krasnov 2205.12196). This is distinct from diode-vortex-screening, which covers small applied fields.
- Remanent field of the superconducting magnet at nominal zero field (Jiang et al., Appendix D).
- Stray fields from remanent magnetic domains through an insulating spacer (Zapata et al. 2610.30556; Li et al. 2506.17651). micromagnet-stray-field is written only for zero-bias peaks.

## Things I was unsure of

- Switching-current ranges (16 to 23 µA in Fig. 3b, 27 to 31 µA in the Fig. 3a inset) come from axis labels in the extracted text, not from data points. I phrased them as axis spans.
- Whether the two bars share a chip and cooldown, and which magnet coils produce [100] and [010], is not stated. My point that crystal axis and magnet axis coincide assumes the usual fixed mounting.
- The 0.6 emu/cm3 figure is my own estimate (2 Mn per 3.8 × 3.8 × 6.32 Å cell). The local edge field it implies depends on geometry, so it is posed as a question.
- I marked "Diode efficiency compared for magnetic domain axis along and across the current" as "all": both bars are shown with preparation along both axes. It does not separate stray fields from proximity on its own, so that row is Tested in part.
- Trapped-flux row: the paper argues against flux trapping, and the switching-current drop is also data that bears on it. I chose "argued, not tested".

## Skill issues

- Step 7 asks for the title from the arXiv abstract page. With text-only input and no abstract page allowed, the skill does not say what to use; I used the title in the paper text.
- A paper in a family with no `checks` (diode) gets only the practice checks. The skill does not say this; I said it in one line.
- Outside rows: "take its tests from the control that paper describes". When the source paper shows a mechanism without naming a control (Jiang, Zapata), the tests must be inferred from its methods. It is unclear whether that is allowed.
- When both "argued, not tested" and "data bear on it" apply, the skill gives no priority.
- "One quote and one clause" per table cell sits poorly with rows where the evidence is a figure comparison and not a sentence.
- Step 7 says to write reports/<id>.md and .notes.md. This run returns them in the reply because the environment refuses .md writes from subagents.
