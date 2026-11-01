# Run notes: arXiv 2608.19099v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (28 lookalike entries). Skill: cmp-assistant/skill/SKILL.md with report-template.md.
- Date: 2026-10-24. Version: v1, per the arXiv stamp in the text ("arXiv:2608.19099v1 [cond-mat.supr-con] 19 Aug 2026").

## What I read
- Only the extracted text of the paper (paper.txt), as the task required. I did not fetch the paper's abstract page, PDF or HTML. The title comes from the text header: "Large Field-Free Superconducting Diode Effect with Nonmonotonic Polarity Reversals in NbSe2/CrBr3 Heterostructures". It is not confirmed against the abstract page.
- The Supplementary Material (ref. [40]) is not in the text. Several key controls are said to be there: device #2, RMCD, the self-field, Meissner and geometric-asymmetry controls, the sign-convention checks, and micromagnetics details. None counted as shown.
- No ancillary figure data or data repository was mentioned or available, so read_mtx.py was not used.
- Page numbers come from the page markers in the extracted text: p. 1 is the abstract and intro, p. 2 Fig. 1 and the text through device #2, p. 3 Fig. 2 and the sign-change discussion, p. 4 Figs. 3 and 4 and the trivial-mechanism sentence, p. 5 the GL theory.
- Quotes are verbatim from the extraction, including its spacing ("NbSe2 /CrBr3").

## Claims table (step 1)
| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| Field-free SDE, η = −35.7% after field training, −15.2% after zero-field cooling | Fig. 1(c,d), Fig. 2(c), Fig. 3(b) | #1 | Current 0 to ±300 µA, separate sweeps from zero; temperature of Fig. 1(c,d) not stated; Fig. 1(e) temperature series across the superconducting regime (range not given in the text) |
| Polarity set by field history; nonmonotonic, hysteretic reversals with Bcf < 0, Bcb > 0; max +45.3% near −10 mT | Fig. 2(a–c) | #1 (main text); #2 "similar" (SM only) | Perpendicular field ±50 mT, 200 mK; field step not given |
| Rectification at zero field after ±6 T training | Fig. 3(a) | #3 | 705 µA excitation; Ic values of #3 not given; number of cycles not given |
| Mechanism: layered FIM CrBr3, interfacial exchange field, cubic odd-in-q GL term | Fig. 4 (simulation and theory), RMCD and DFT in SM | n/a | CrBr3 trilayer in simulation; device layer counts not given |
- Missing counts: devices fabricated, devices measured, devices showing the effect, cooldowns, number of field sweeps, NbSe2 and CrBr3 thickness, the 6 T training protocol for device #1 (the "magnetic field training" behind −35.7% is not specified in the main text). The text says "consistently" for Bcf < 0, Bcb > 0 without a count.
- The 705 µA bias for device #3 is above the ±300 µA current range shown for device #1. This is consistent if device #3 has larger Ic, but Ic for #3 is not given, so I raised it as a question.

## Entries matched, skipped, adapted
- Matched: diode-vortex-screening (diode family), fine-tuning-and-selection (always).
- Checks: the library has no `diode` checks family, so I used only the practice checks (report-counts, report-ranges, report-processing).
- Skipped: all zbp, quantization, nonlocal, island, shapiro, kitaev, charge and chiral entries, plus local-probe-loophole (Majorana-specific signals; this paper has no tunneling peak, quantized conductance, Shapiro steps or interferometry). Also skipped:
  - field-enhanced-supercurrent-resonances: its signature is a Josephson supercurrent that grows with field, and this is a film diode with no junction.
  - micromagnet-stray-field: its signature is zero-bias peaks in dots. The stray-field physics is relevant, so it went in as an outside row with a diode-specific source.
  - protocol-parameter-sensitivity: there is no automated pass/fail protocol.
- Adapted: none. The diode family is in the library's scope.

## Status reasoning
- diode-vortex-screening: the paper concludes against it, but only by reference to the SM, which I could not see. In the text, the field dependence is shown for device #1 only (Fig. 2), with no width or edge series and no plain-film control. So it is Tested in part.
- Trapped vortices (outside): zero-field cooled (−15.2%) versus trained (−35.7%) in device #1 is a partial comparison, because the CrBr3 magnetic state also differs between the two. I marked it "part" for that reason. The paper does not discuss trapped flux.
- Stray field (outside): not mentioned as such. The paper's argument that the interfacial layer can oppose the net magnetization is aimed at the conventional proximity model. Fig. 2 together with the RMCD loop (SM) bears on it, so it is "data bear on it".
- fine-tuning-and-selection: three devices are named, device #3 is shown in Fig. 3(a), and device #2 is SM only. Totals and the selection basis are absent.

## Sources held out
- None of the matched entries' sources (Hou et al. 2205.09276, Frolov et al. 2309.09368, Akrap et al. 2501.18631) was found to discuss this paper. Hou and the Frolov preprint predate it. I did not open the Akrap v2 text, but used only the library's own quotes from it, and none cites 2608.19099. Nothing was skipped.

## Related work checks
All were opened on the export.arxiv.org abstract page. I confirmed the ID, title and first author, and checked each one-line description against the abstract. None was checked in full text.
- 2205.09276 Hou et al. (abstract): confirmed 1 Oe, Nb and V films, 65% with EuS, Meissner screening quote.
- 2205.12196 Golod and Krasnov (abstract): confirmed trapped Abrikosov vortex plus self-field, zero field, switch on/off by trapping and removing, above 70%.
- 2610.30556 Zapata et al. (abstract; dated 2026-10-22, later than the paper under review, described for its own results only): confirmed 50–60%, AlN spacer at 35–40%, and stray-field interpretation.
- 2110.15752 Bauriedl et al. (abstract): confirmed NbSe2 constrictions, up to 60%, out-of-plane field.
- 2406.14417 Xiong et al. (abstract): confirmed field-free electrical switching in Fe3GeTe2/NbSe2.
- Opened but not listed: 2506.17651 Li et al. (Pt/Co/Nb field-free diode from stray fields plus geometric asymmetry; it would also support the stray-field row) and 2609.38003 Krizek et al. (antiferromagnet-controlled field-free diode).
- arXiv API searches I ran: diode with vortex and memory; Golod and Krasnov; superconducting diode with remanent; with CrBr3 (no hits); NbSe2 with zero field; trapped vortices; trapped flux; residual field; remanent field; hysteretic vortex; NbSe2 with ferromagnet. I waited 3 s between calls.

## Library gaps
- No `diode` family in `checks`. Suggested checks: a plain-film or uncovered control, calibration of the magnet's remanent field near zero, and a trapped-flux reset (warm above Tc at zero field).
- Trapped vortices or flux after field training, as a source of field-free, history-dependent diodes (source: Golod and Krasnov, arXiv 2205.12196).
- Dipolar stray field of a magnetic overlayer versus interfacial exchange (sources: Zapata et al. 2610.30556, Li et al. 2506.17651; spacer control).
- Remanent field of the superconducting magnet after sweeps, which shifts the true zero. I found no arXiv paper on this through the API searches, so it appears only as a question and is not a table row.

## Unsure
- Whether stating the shown ranges counts as "partly" for report-ranges or as "not done". I chose partly.
- Whether the Fig. 2 field sweep counts toward "Effect followed against field, sample width or edge quality". I counted it as part, because only field and only device #1 are covered.
- Whether the device #2 and SM statements should count. They do not, because they are not shown in the text available.
- I did not recognize the paper.

## Skill issues
- The diode family has one library entry and no `checks` steps, so the checks section reduces to the practice checks. The skill does not say what to do when a family has no checks.
- The skill says to read the abstract page and PDF. This run's task forbade fetching the paper and gave text only, so the title and version could not be confirmed against the abstract page. The skill could say how to record that.
- Step 3 says controls "shown in SM" count only if shown. When the SM is not available, the skill does not say whether to mark "no" or "part". I used "no", and "part" only where main-text data exist.
- Outside rows need one source URL in flags, but the tests may come from several papers. I used one source per row.
