# Run notes: arXiv 2609.38003v1

- **Library version:** 0.5 (meta.updated 2026-10-24). There are 28 lookalike entries.
- **Date:** 2026-10-24.
- **What I read:**
  - The local abstract page (abs.html): title, authors, date 2026-09-29, v1.
  - The full extracted text (paper.txt).
  - PDF pages 3, 4, 5 and 11, rendered to PNG to read Figs. 2, 3 and 4 and Extended Data Figs. 3 and 4.
  - The paper has no ancillary files and links no data repository, so there were no .mtx files and read_mtx.py was not used. I did not use any data repository.
  - Per the prompt, I did not fetch the paper.
- **Could not open:** Nothing I tried failed.
- **Recognition:** I did not recognize the paper. It is dated after my training data. No later history was used.

## Claims table (step 1)

| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| Zero-field diode after ZFC, η ≈ 7% | Fig. 3a and inset (p. 4), text p. 3 | 5 µm x 180 µm bar along [010], 2.0 nm AlAs wafer | 50 sweeps per polarity; 20 mK only; 50 µV threshold; 0.2 s step delay |
| Polarity reversal with [100] preparation field, up to about ±20% | Fig. 3b, d (p. 4) | same bar | Prep ±1 T along [100]; 8 sweeps averaged per point; readout at H = 0 |
| Weak response, no systematic reversal, for [010] preparation | Fig. 3e (p. 4) | same bar | Prep about ±5 T along [010] |
| Same anisotropy in an orthogonal bar | Ext. Data Fig. 4 (p. 11) | bar along [100]; its dimensions are not given | Prep ±1 T [100], ±5 T [010]; no ZFC data shown |
| Néel-state anisotropy and remanence | Fig. 4a-c (p. 5) | Reference CuMnAs bar, 20 µm x 10 µm, from a different wafer with a 3 nm oxidized Al cap (p. 8) | 5 K; ±4 mA; field ±5 T [100], ±2 T [010] |
| Easy axis along [100] | Ext. Data Fig. 5 (p. 12) | CuMnAs epilayer, 10 µm x 10 µm region | about 100 K |
| Near-zero net moment, below 3e-3 µB/Mn | Fig. 2b (p. 3), Methods p. 7 | Wafer pieces, 3 mm x 5 mm, edge to center | SQUID resolution 1e-7 emu |
| Proximity tuning by barrier thickness | Fig. 2c (p. 3), Ext. Data Fig. 3 | Two stacks: 2.0 nm (Tc ≈ 350 mK) and 1.5 nm (no transition down to 20 mK) | One sample of each thickness shown |

- **Missing counts:**
  - Devices fabricated and measured.
  - Cooldowns.
  - How many bars showed the effect.
  - Whether the two diode bars share a chip or a cooldown.
  - Whether ZFC η was measured on the [100] bar.
  - Temperature dependence of η.
  - Ramp-rate dependence.
- **Data observations used in the questions:**
  - Fig. 3a inset switching currents are about 27 and 31 µA. The points in Fig. 3b are about 17 to 21 µA.
  - η in Fig. 3d jumps sign between about 0.05 and 0.1 T and peaks at about ±16 to 18% near 0.1 T. Fig. 4c Reven crosses zero near ±1.3 T.
  - Ext. Data Fig. 4a: η at +1 T is about −4%, the sign of the negative branch.
  - Fig. 3e and Ext. Data Fig. 4b: η sits at about −3 to −5% for [010] preparation, while ZFC η in Fig. 3a is positive (about +7%).
  - All of these were read off the rendered figures, so the values are approximate.

## Matching (step 2)

- **Matched:**
  - diode-vortex-screening (diode family).
  - fine-tuning-and-selection (always included).
  - micromagnet-stray-field, adapted. Its signature is zero-bias peaks at zero field. I matched it on the physics: a stray field from magnetic material makes "zero applied field" a nonzero effective field. The paper raises this mechanism itself (p. 6, ref. 30). I applied its three tests to the diode readout, reading "Magnet switching (hysteresis in field)" as the M(H) loop search in Fig. 2b.
- **Skipped:**
  - All zbp, quantization, nonlocal, island, shapiro, chiral, kitaev and charge entries: there are no tunneling peaks, quantized values, Shapiro steps, islands or charge measurements.
  - field-enhanced-supercurrent-resonances: the signal is nonreciprocity at zero field, not a supercurrent that grows with field.
  - protocol-parameter-sensitivity: there is no automated pass/fail protocol.
  - local-probe-loophole: it is specific to Majorana mode separation.
- **Scope sentence:** included under "What this is", since a diode measurement is adjacent to topological transport.

## Checks (step 3)

- No `checks` exist for the diode family, so only the practice checks were walked:
  - report-counts: not done.
  - report-ranges: partly.
  - report-processing: partly.

## Sources held out

- None. No library source cites or discusses 2609.38003. All of them predate it. Legg 2502.19560 v2 and Akrap 2501.18631 v2 are 2026 versions, but they concern other papers.
- Hou et al. 2205.09276 is cited by the paper (ref. 28), but it does not discuss the paper, so I kept it.

## Related work checks

All five abstract pages were fetched from arxiv.org/abs and their titles and first authors confirmed.
- 2205.09276, Hou: abstract read (also a library source).
- 2512.05427, Jiang: full text read via arxiv.org/pdf/2512.05427v1. I confirmed the poling-field sign control, the in-plane vs out-of-plane anisotropy, and the magnet hysteresis passages: "Such hysteresis can often arise from a stray magnetic field due to the superconducting magnet." and "the magnetic field values of ≈ ±15 mT were shifted".
- 2205.12196, Golod and Krasnov: abstract.
- 2506.17651, Li: abstract. This is the paper's ref. 30.
- 2601.03366, Sachin: abstract. This is the paper's ref. 10.

## Library gaps

1. **No `checks` for the diode family.** Candidates:
   - In-field η through zero with a calibrated field.
   - A plain superconductor control.
   - Thermal cycling above Tc between preparation and readout.
   - A count of the remanent states.
2. **Trapped flux set by a preparation (poling) field**, as a diode lookalike with memory. Source: Jiang et al. 2512.05427. Golod and Krasnov 2205.12196 also bears on it. The tests I used are taken from Jiang's controls: Ic mapped against field after ± poling, comparison of poling directions, and the direct imaging they propose.
3. **Residual field of a superconducting magnet at nominal zero.** Source: Jiang et al. 2512.05427, Appendix D, about ±15 mT. Combined with the 1 Oe sensitivity in Hou et al., this can give a sign-reversing "zero-field" diode. It also differs between the coils of a vector magnet.
4. **The stray-field entry is tied to zero-bias peaks.** A general "stray field from magnetic material at zero applied field" entry, or a diode-specific one citing Li et al. 2506.17651, would avoid the adaptation.

## Unsure

- **Second outside row.** I kept "residual magnet field" as its own row. It could instead be folded into diode-vortex-screening, since it needs that entry's mechanism to produce a diode.
- **Preparation-field test marked "part".** The test is "Effect followed against field, sample width or edge quality". The paper follows η against preparation history but never against applied field at readout, so I marked it part.
- **Two-axis test marked "part".** For the trapped-flux test "Preparation-field direction compared, in plane and out of plane", I counted the two in-plane axes as part. The out-of-plane preparation is missing.
- **report-counts marked "not done".** I chose this over "partly". The paper identifies the devices it shows but gives no totals.
- **Approximate figure values.** Those in questions 6 and 7 were read from rendered figures.

## Skill issues

- **Report location.** Step 7 says to write `reports/<id>.md`. Here the prompt overrode that, and the report and notes went into the reply.
- **Out-of-scope families.** The scope rule covers "a different kind of measurement" but not a matching family that has no `checks`. It is unclear whether to mark the family checks as absent or to invent some. I used practice checks only.
- **Adapting entries across families.** It is unclear whether an entry from another family can be adapted to a shared mechanism through "Match on the physics", or whether that should go in an outside row. I adapted micromagnet-stray-field.
- **Notes for "Tested in part".** The flags shape has `note` values only for "Not tested"; I set null for other statuses. The skill does not say this.
- **Stopping at two outside rows.** The skill allows outside rows from one cited paper, but gives no guidance on how many outside rows are too many, or whether two rows may share one source.
