# Run notes: 2608.19099v1

- Library: lookalikes.yaml meta.version 0.5 (28 entries). Skill: SKILL.md and report-template.md, read once at the start.
- Date: 2026-10-24.

## What I read
- The paper's extracted text only (paper.txt): main text pp. 1 to 5, figure captions and references. Per the task, I did not fetch the abstract page, the PDF or any other version. The Supplementary Material is not in the text and I did not see it.
- I took the title from the text header (arXiv:2608.19099v1 [cond-mat.supr-con] 19 Aug 2026).
- No figure data, ancillary files or data repository were provided or linked, so I did not run read_mtx.py.
- I did not recognize the paper. It postdates my training data.

## Claims table (step 1)
| Claim | Figures | Device | Ranges and counts |
|---|---|---|---|
| Field-free SDE, η = −35.7% after training, −15.2% after zero-field cooling | Fig. 1(c)-(e), Fig. 2(c) | #1 | I sweeps 0 to ±300 µA; Fig. 2 at 200 mK; Fig. 1(e) temperature range not stated in the text |
| Polarity set by field history | Fig. 2(a)-(c); Fig. 3(a) | #1 (±50 mT sweeps); #3 (±6 T training, 705 µA excitation); #2 in SM only | Perpendicular field; sweep rate and step not stated |
| Nonmonotonic, hysteretic reversal; Bcf < 0, Bcb > 0 ("consistently") | Fig. 2(c) | #1; #2 in SM | η max 45.3% near −10 mT; values of Bcf and Bcb not given in the text |
| Mechanism: layered FIM CrBr3 interfacial exchange plus cubic GL term | Fig. 4 (schematic, simulation, theory) | RMCD, DFT, micromagnetics in SM | Simulation is of a CrBr3 trilayer; CrBr3 and NbSe2 thicknesses of the devices not stated |
| Among highest field-free η | Fig. 3(b) | #1 | Literature comparison |

Missing counts: devices fabricated, devices measured in total, cooldowns, number of field sweeps repeated, NbSe2 Tc, layer thicknesses, the temperature for the zero-field cooling, the field calibration and remanence.

## Matching (step 2)
- Matched: diode-vortex-screening (family diode) and fine-tuning-and-selection (always).
- Skipped, because they cannot apply to a superconducting film under a magnetic insulator with four-probe critical-current measurements (no tunneling spectroscopy, no Shapiro steps, no islands, no Kitaev chain, no fractional charge, no QAH): every zbp, quantization, nonlocal, island, shapiro, charge, chiral and kitaev entry, plus local-probe-loophole.
- Also skipped:
  - protocol-parameter-sensitivity: there is no automated pass/fail protocol.
  - field-enhanced-supercurrent-resonances: its signature is a supercurrent that grows with field read as triplet pairing, which is not the claim here.
  - micromagnet-stray-field: its signature and mechanism are zero-bias peaks from Andreev states in dots. The stray-field physics relevant here is vortex-based, so I added it as an outside row.
- Adapted entries: none. The diode entry matched directly. I mention in "What this is" that only the practice checks were walked.

## Status decisions (step 3)
- Checks: the library has no diode family under `checks`, so I walked only the practice checks (report-counts, report-ranges, report-processing). All three are partly done.
- diode-vortex-screening is Tested in part.
  - The paper concludes against it, but the ruling-out is "shown in SM", which I could not see.
  - In the main text, the field dependence is shown for device #1 only, and Fig. 3(a) shows device #3 only at zero field, so field dependence is "part".
  - The main text mentions no plain-film control, so that test is "no".
- fine-tuning-and-selection is Tested in part.
  - Three devices are named, but no totals are given.
  - The main text does not say how the shown data were chosen.
  - Device #3 is a second device in the main text. Device #2 is only in SM.
- Outside row, trapped vortex / self-field (Golod and Krasnov 2205.12196): Tested in part.
  - Tests come from that paper's control: trapping or removing a vortex, and changing the bias configuration.
  - The zero-field-cooled versus trained comparison (Fig. 1(d) and Fig. 2(c), device #1) is an equivalent of trapping or removing a vortex. It counts as "part": shown for one device, and the cooling start temperature is not stated.
  - The paper says self-fields are ruled out in SM.
- Outside row, stray field of the magnetic layer on vortices (Zapata et al. 2610.30556): Not tested (not mentioned).
  - Tests come from that paper's control: an AlN spacer that cuts proximity and keeps stray fields, and stripe orientation relative to the current.
  - The paper does not mention stray fields from CrBr3. Its Meissner ruling-out is in SM.
  - I was unsure whether "argued, not tested" fits better. I chose "not mentioned" because no sentence addresses stray fields.

## Hold-out
- Library sources for the matched entries are arXiv 2205.09276 (Hou et al., 2022), 2309.09368 (Frolov et al., 2023) and 2501.18631 (Akrap, Frolov et al.). All predate the paper (Aug 2026). I did not open the last two. I held out no sources.
- One arXiv search listing (abs:"superconducting diode" AND abs:"hysteretic") returned 2608.19099 itself as a title line. I did not open it.

## Related work checks (step 5)
I checked each paper's ID, title, first author and abstract through the export.arxiv.org API (abstract only):
- 2205.09276 Hou et al.: abstract.
- 2205.12196 Golod and Krasnov: abstract.
- 2610.30556 Zapata et al.: abstract. It is later than the paper; I describe only its own results.
- 2506.17651 Li et al.: abstract.
- 2406.14417 Xiong et al.: abstract (likely ref. [26] of the paper).

I considered 2402.16264 (Zhang et al., NbSe2 nanobridge) and did not list it. I found no arXiv source for magnet remanent-field offsets in diode measurements, so that point appears only as question 5, the one question no entry raises.

## Library gaps
- The diode family has no `checks` steps. Candidates: a control sample of the parent superconductor; field calibration and remanence near zero; zero-field cooling versus trained states and a warm-up above Tc; a spacer layer to separate exchange from stray field; a current-direction or angle dependence.
- Missing diode lookalikes:
  - trapped vortex or self-field from field history (Golod and Krasnov 2205.12196);
  - stray fields of a magnetic overlayer acting on vortices (Zapata et al. 2610.30556; Li et al. 2506.17651);
  - magnet remanent-field offset (needs a source).

## Skill issues
- The skill says to read the abstract page and PDF and to write reports/<id>.md. The task said to use the text only and return the report in the reply. I followed the task.
- The skill does not say how to treat evidence that the main text says is "shown in SM" when the SM is unavailable. I treated it as a statement (not shown) and said so in the report.
- Step 3 says to walk "the checks for the paper's family", but the diode family has none. The skill does not say whether to adapt checks from another family. I used the practice checks only.
- For outside rows, "judge it against the control that paper describes" leaves open whether an equivalent test (such as zero-field cooling versus training for vortex removal) counts. I counted it and named it.
- The "Not tested" note options do not cover a case where the paper rules out a neighbouring mechanism (Meissner screening) without naming this one (stray field). I chose "not mentioned".
