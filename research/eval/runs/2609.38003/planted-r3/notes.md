# Run notes: arXiv 2609.38003v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.4 (updated 2026-10-23), 28 lookalikes. I read the whole file once at the start, including the `checks` section.
- Skill and template: skill/SKILL.md and skill/report-template.md. I read both once.
- Date of run: 2026-10-23.

## What I read
- The paper: the extracted text supplied (paper.txt, 14 pages, main text plus Methods and Extended Data Figs. 1 to 5 captions) and the supplied arXiv abstract page (abs.html: title, 22 authors, v1 dated 29 Sep 2026, "14 pages, 4+5 figures"). I had no PDF, so figure details come from the captions and the text. I did not fetch the paper in any form. One arXiv API search ("field-free" AND "superconducting diode") returned the paper under review as a listing row. I did not open it.
- No figure data or code is linked, and the text has no data availability statement. I did not run read_mtx.py.
- Page numbers are the page markers in the extracted text: p. 1 abstract; pp. 2 to 6 main text; Methods pp. 6 to 8; Ext. Data Figs. 1, 2 on pp. 9, 10; Ext. Data Figs. 3, 4 on p. 11; Ext. Data Fig. 5 on p. 12.
- The extracted text garbles some symbols (H^prep_100, I_SW^±), so I chose quotes without garbled symbols.

## Claims table (step 1)
| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| Zero-field diode after ZFC, η ≈ 7% | Fig. 3a and inset | [010] bar, 5 µm × 180 µm, 2.0 nm AlAs, four-terminal | 50 sweeps per polarity (Methods p. 8); T = 20 mK; threshold 50 µV; delay 0.2 s |
| η sign reverses with ±1 T prep along [100] | Fig. 3b, 3d | same bar | prep along [100] to ±1 T (axis of Fig. 3d); 8 sweeps averaged per point; η up to about ±20% |
| Weak response, no systematic reversal, for prep along [010] | Fig. 3e | same bar | prep along [010] to ±4 T (axis of Fig. 3e) |
| Same axis dependence in an orthogonal bar | Ext. Data Fig. 4 | [100] bar | ranges as in Fig. 3d,e; dimensions not stated |
| CuMnAs alone keeps a field-written state with a [100] easy axis | Fig. 4a to c | reference bar 20 × 10 µm, CuMnAs with a 3 nm oxidized Al cap, from a different wafer | 5 K; ±4 mA; fields to ±4 T (a), ±2 T (b), prep −5 to 5 T (c) |
| Uniaxial [100] Néel axis | Ext. Data Fig. 5 (XMLD-PEEM) | CuMnAs epilayer, one 10 × 10 µm region | about 100 K |
| Net moment below 3×10⁻³ µB/Mn | Fig. 2b | 3 mm × 5 mm piece; several pieces from wafer edge to center | measurement temperature and field history not stated |
| Proximity tuning by AlAs thickness | Fig. 2c, Ext. Data Fig. 3 | 2.0 nm (Tc ≈ 350 mK) and 1.5 nm (no transition to 20 mK) | two heterostructures |

Missing counts: total bars fabricated and measured, chips, cooldowns, how many bars showed the effect, η versus temperature, the residual magnet field, magnet type (vector magnet or rotation), and whether both bars sat on one chip.

## Matching (step 2)
- Matched: diode-vortex-screening (family diode, matched on physics: the paper credits the zero-field diode to an intrinsic, magnetically controlled mechanism, and the entry's lookalike is an extrinsic screening or vortex diode in any thin film). Also fine-tuning-and-selection (always).
- Skipped: every zbp, quantization, nonlocal, island, shapiro, chiral, kitaev and charge entry, because the paper has no tunneling peak, no quantized conductance, no Josephson junction under microwaves, no island or interferometer, and no QAH film. I skipped field-enhanced-supercurrent-resonances because the paper has no junction and no supercurrent that grows with field. I skipped protocol-parameter-sensitivity because the paper uses no automated pass/fail protocol. Its range concern is covered by the report-ranges check.
- Checks: the library has no `checks` block for the diode family, so I walked only the three practice checks (report-counts, report-ranges, report-processing).
- Adapted entries: none in substance. I added one sentence under "What this is" because the claim is not topological.

## Hold-out
- No library source was held out. The sources I relied on are Hou et al. 2205.09276 (latest v5, Feb 2023), Frolov et al. 2309.09368 (quotes from v1, 2023) and Akrap et al. 2501.18631 (v2, 25 Mar 2026). All predate the paper (29 Sep 2026), so none can discuss it. Jiang et al. 2512.05427 v1 (Dec 2025) has no mention of CuMnAs, Krizek or 2609.38003 in its HTML full text (grep count 0).

## Related work: how each was checked
- 2205.09276 Hou et al.: abstract page opened; ID, title, first author and the 1 Oe and EuS non-volatile statements confirmed from the abstract.
- 2512.05427 Jiang et al.: abstract page and HTML full text (v1) opened. I confirmed the ±1 T poling-field sign control and zero-field nonreciprocity in both I⊥H and I∥H configurations (Sec. III.2). I also confirmed the statement "Such hysteresis can often arise from a stray magnetic field due to the superconducting magnet. To rule out this possibility, we measured the resistance of few-layer graphene simultaneously during all measurements." The HTML header shows a date of August 24, 2026, while the abstract page lists only v1 (5 Dec 2025).
- 2205.12196 Golod and Krasnov: abstract page opened; trapped Abrikosov vortex, zero-field diode, switchable polarity confirmed from the abstract.
- 2409.01715 Nagata et al.: abstract page opened; thermoelectric response plus geometric asymmetry confirmed from the abstract only.
- 2601.03366 Sachin et al.: abstract page opened; zero-field diode in Mn3Pt/Nb, up to 50%, several mechanisms hinted, confirmed from the abstract.
- I considered and left out 2206.00483 (Narita et al., field-free SDE in [Nb/V/Co/V/Ta] multilayers; abstract opened), to keep the list at five. I also left out 2505.18330 (Shi et al., field-free SDE from external circuit line resistance; abstract opened), because its mechanism needs gate-controlled chemical potential and this device has no gate.

## Library gaps
- Diode family: only one entry (diode-vortex-screening) and no ordered `checks`. Candidates from papers I opened:
  - Trapped flux set by a poling field gives a sign-switchable zero-field SDE (Jiang et al. 2512.05427; Golod and Krasnov 2205.12196). Control: warm above Tc and recool at zero field, and calibrate the residual field.
  - Residual field of the superconducting magnet after a large excursion. Control: a co-mounted sensor with an even, non-hysteretic response (Jiang et al. used graphene).
  - Thermoelectric response with geometric asymmetry (Nagata et al. 2409.01715).
  - Circuit line resistance in gated devices (Shi et al. 2505.18330).
- Suggested diode checks: residual-field calibration; warm-above-Tc reset; control film of the parent superconductor; separate crystal axes from magnet axes by rotation; η versus temperature and ramp rate.

## Unsure
- The claim that refs. 28 to 30 are uncited in the text comes from the extracted text, which may have dropped superscripts. There is a double space before "We therefore conclude" on p. 6, which may mark a removed sentence. I phrased the question as "in the text I read".
- The 8 G magnetization equivalent of the SQUID bound is my own estimate (2 Mn per cell, a = 3.80 Å, c = 6.32 Å, so n ≈ 2.2×10²⁸ m⁻³ and M ≈ 610 A/m). The paper does not state it. The stray field at the Al depends on geometry and would be much smaller for a uniform in-plane film.
- Thermoelectric row: weak evidence for this device, since the polarity reversal argues against a fixed geometric offset. I chose "partly addressed" because the reversal bears on it and the 7% ZFC offset is not explained.
- I read the Fig. 3d,e prep-field ranges (±1 T, ±4 T) from the axis tick labels in the extracted text, which is not reliable.
- I did not recognize the paper, and I know nothing of its later history.

## Skill issues
- Step 3 assumes every family has `checks`. Diode has none, and the skill does not say whether to adapt another family's checks or use practice checks only. I used practice only.
- The template's "What this is" fixes "topological transport", and the Scope rule only covers a different kind of measurement. It does not cover a diode claim with no topological claim. I added a sentence.
- The output spec asks for lookalike ids, and the template's table has no id column. I used readable names in the report and ids in flags.json.
- Page numbers from text-only input are ambiguous. The skill assumes a PDF.
- The report's "about 600 to 900 words outside the table" fits poorly once the outside lookalikes need explanation. I added two short notes under the table, which may push past the length.
- The skill says to "Write reports/<id>.md". This run's instructions override that, and the report is returned inline.
