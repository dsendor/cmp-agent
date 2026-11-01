# Run notes: arXiv 2609.38003v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (28 lookalike entries). Template: skill/report-template.md. Skill: skill/SKILL.md.
- Date: 2026-10-24.

## What I read
- Paper: only the extracted text at the provided paper.txt (v1, dated 29 Sep 2026; main text, Methods, Extended Data Figs. 1 to 5 captions, references). Per the run instructions I did not open the arXiv abstract page, the PDF or the HTML. The title comes from the text header. Figure details come from captions and from axis labels in the extracted text.
- No supplementary file beyond the Extended Data in the text. No ancillary figure data, so I did not run read_mtx.py. The paper links no data repository, and I found no data or code statement.
- Page numbers come from the page markers in the extracted text. p. 1 covers the abstract and intro, the Fig. 3 caption is on p. 4, the Fig. 4 caption on p. 5, and Methods run from p. 6 to 8.
- I did not recognize the paper. It postdates my knowledge.

## Claims table (step 1)

| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| Field-free diode, η about 7% after ZFC; distributions separated | Fig. 3a and inset | 5 µm by 180 µm CuMnAs/AlAs(2.0 nm)/Al bar along [010], four-terminal | 50 sweeps per polarity; 20 mK base; 50 µV threshold; 0.2 s step delay; one bar shown |
| Diode sign follows the [100] preparation field, read at H = 0 | Fig. 3b,c,d | same bar | ±1 T [100] in Fig. 3b,d; 8 sweeps averaged per point; η up to about ±20% |
| Weak, same-sign response for [010] preparation | Fig. 3e | same bar | ±4 T [010] |
| Same axis dependence in an orthogonal bar | Extended Data Fig. 4 | bar along [100] | ±1 T [100], ±4 T [010] (from axis labels) |
| Néel-state readout with matching anisotropy and remanence | Fig. 4a,b,c | separate CuMnAs bar, 20 µm by 10 µm, 3 nm oxidized Al cap, different wafer | 5 K, ±4 mA; field ±4 T [100] (4a), ±2 T [010] (4b); preparation −5 to 5 T in text (axis ticks ±4) |
| Uniaxial [100] easy axis | Extended Data Fig. 5 | CuMnAs epilayer | about 100 K, 10 µm by 10 µm area |
| Negligible net moment | Fig. 2b | wafer pieces, 3 mm by 5 mm | bound 3×10−3 µB/Mn; temperature and field history of the SQUID run not stated |
| Proximity tuned by AlAs thickness | Fig. 2c, Extended Data Fig. 3 | 2.0 nm (Tc about 350 mK) and 1.5 nm (no transition to 20 mK) films | two barrier thicknesses |

The paper does not give these counts: bars fabricated or measured, chips, cooldowns, how many bars showed the effect, or temperature dependence of η.

## Entries matched, skipped, adapted
- Matched: diode-vortex-screening (diode family) and fine-tuning-and-selection (always).
- Skipped as not applicable (no tunneling spectroscopy, Majorana, Shapiro, island, chiral, Kitaev, interferometer or protocol claim): abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, fine-tuned-plateau, series-resistance-subtraction, one-end-only, trivial-andreev-band-gap-reopening, full-shell-flux-andreev, chiral-plateau-superconductor-short, island-states-coulomb-spacing, shapiro-landau-zener, shapiro-nonlinear-resistance, charge-trap-fractional-shift, spin-orbit-length-pinning, exceptional-point-zero-mode, transparent-junction-pi-crossing, switching-jump-blind-region, false-poor-mans-majorana, local-probe-loophole, coulomb-dominated-interferometer.
- protocol-parameter-sensitivity: skipped, because no automated pass/fail protocol is used.
- field-enhanced-supercurrent-resonances: considered and skipped. The claim is a direction asymmetry at zero field, and no supercurrent grows with field.
- micromagnet-stray-field: the physics is close to the stray-field row, but its signature (zero-bias peaks) and mechanism (Andreev states in dots) don't fit. I used an outside row citing Zapata et al.
- Checks: the library has no diode checks, so only the practice checks (report-counts, report-ranges, report-processing) were walked. I adapted no zbp or shapiro checks.

## Sources held out
- None. The matched entries cite Hou et al. 2205.09276 (2022), Frolov et al. 2309.09368 (2023) and Akrap et al. 2501.18631 (v2, PRB 113, 2026). All predate the paper, so none can discuss it.
- Zapata et al. 2610.30556 postdates the paper. I searched its full text for "CuMnAs", "Krizek" and the arXiv ID and found no mention. It is listed for its own results only.

## Related-work checks
- 2205.09276 Hou et al.: abs page opened (title and first author confirmed); abstract confirms the 1 Oe, vortex barrier and Meissner screening, and EuS claims.
- 2512.05427 Jiang et al.: abs page opened; full text read (results, Appendix D magnet correction of about ±15 mT, Appendix E out-of-plane control, limitations).
- 2205.12196 Golod and Krasnov: abs page opened; abstract confirms trapped-vortex stray field plus self-field, and polarity switching.
- 2610.30556 Zapata et al.: abs page opened; abstract and parts of the full text read (AlN spacer cuts proximity and keeps stray-field coupling; 35 to 40% with the spacer; orientation dependence).
- 2601.03366 Sachin et al.: abs page opened; abstract confirms up to 50% zero-field diode in Nb/Mn3Pt and the "multiple contributing mechanisms" wording.
- Searches: arXiv API, abs:"superconducting diode" combined with trapped, "perpendicular magnetization" and antiferromagnet, with 3 s between calls.

## Library gaps (outside rows)
- Trapped flux written by a preparation or poling field (Jiang et al. 2512.05427; also Golod and Krasnov 2205.12196). Tests come from Jiang's controls: field dependence near zero after each poling sign (their Fig. 3) and a geometry where trapping differs (their Appendix E). The warm-above-Tc test I suggest is my own adaptation for a magnet whose order temperature is far above Tc.
- Remanent field of the superconducting magnet after high-field excursions (Jiang et al. Appendix D). Combined with Hou et al.'s 1 Oe scale, this can give a diode whose sign follows the preparation sign.
- Stray field from residual moments or remanent magnetic texture through an insulating spacer (Zapata et al. 2610.30556).
- The library has no `checks` section for the diode family.

## Unsure
- Fig. 3b axis values (16 to 23 µA) and Fig. 3a inset values (27 to 31 µA) come from extracted axis labels. I can't see the plotted points, so question 7 is phrased conditionally.
- The µ0M estimate assumes 2 Mn per a = b = 3.80 Å, c = 6.32 Å cell, using the paper's DFT lattice constants: 3×10−3 µB/Mn gives M ≈ 600 A/m, so µ0M ≈ 0.77 mT. This is an upper scale. A uniform in-plane film gives stray field mainly at edges and domain walls.
- Marked "part" with a reason: diode-vortex-screening test 2 (the preparation-field series is a field dependence, but not of the applied field at readout); trapped-flux test 2 (an in-plane axis comparison is not Jiang's out-of-plane control); stray-field test 1 (the bound is on wafer pieces, with temperature and history unstated).
- fine-tuning test 1 is marked "no": the paper lists the bars it shows but gives no totals.
- Whether thin Al stays superconducting during in-plane ±1 T preparation at 20 mK (this affects how plausible trapping is) is not stated.

## Skill issues
- The library has a diode lookalike but no diode checks. The skill doesn't say whether to adapt zbp or shapiro checks or to walk only the practice checks. I walked only the practice checks.
- For outside rows, "take its tests from the control that paper describes" leaves the choice open when the source describes several controls (Jiang has three). It is also unclear whether one source may back two outside rows.
- The input step (read the abs page and PDF) and step 7 (write reports/ files) conflict with this run's instructions. I followed the run instructions, and the title comes from the text.
- The template's "What this is" names topological transport even when the signal is a non-topological diode in a covered family. The scope rule only covers a different kind of measurement. I added one sentence.
- "Devices and datasets measured, and how many showed the effect": it is unclear whether naming the bars shown, without totals, counts as part.
