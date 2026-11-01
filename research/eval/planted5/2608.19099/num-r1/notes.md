# Run notes: arXiv 2608.19099v1

- Library: lookalikes.yaml, meta.version 0.5 (28 lookalike entries). Template: skill/report-template.md.
- Read: extracted main text only (/tmp/.../planted2/blind/e89/paper.txt), per the task. No PDF, no abstract page, no Supplemental Material (SM [40] not included in the text). Figure details taken from captions. Title taken from the text header, since the abstract page was not to be fetched.
- Not opened: the paper itself (by instruction); SM; no data repository is linked, so none used. No figure data or code; read_mtx.py not used.
- Recognition: I do not recognize this paper or know any later history.

## Claims table (step 1)

| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| Field-free SDE, efficiency 35.7% at 0 mT | Fig. 1(c,d), Fig. 2(c), Fig. 3(b); abstract | #1 | Current sweeps 0 to ±300 µA (Fig. 1c caption); η after ZFC −15.2% (Fig. 1d); temperature of Fig. 1 not stated; Fig. 1(e) T range not stated |
| SDE persists through superconducting regime | Fig. 1(e) | #1 | T range not given in text |
| Polarity set by field history; nonmonotonic, hysteretic reversals, Bcf < 0, Bcb > 0 | Fig. 2(a-c) | #1 (#2 in SM) | 200 mK; field −50 to 50 mT perpendicular, both sweep directions; max +45.3% near −10 mT; field step not stated |
| Zero-field rectification, polarity programmed by ±6 T training | Fig. 3(a) | #3 | 705 µA excitation; Ic± of #3 not given; number of cycles not given |
| Mechanism: cubic odd-in-q GL term; interfacial FIM CrBr3 layer sets Bprox | Fig. 4, RMCD and micromagnetics in SM | n/a | Trilayer simulation; CrBr3 layer count of devices not given |
| Trivial mechanisms (self-fields, Meissner screening, geometric asymmetry) ruled out | SM only | ? | Not visible in main text |

Missing counts: devices fabricated, devices measured, devices showing the effect, cooldowns, number of training cycles, NbSe2 and CrBr3 thicknesses, temperature of Figs. 1 and 3, field step size, remanent-field calibration.

Internal numerical inconsistencies found (raised in question 5):
- p. 2: "after undergoing the magnetic field training, the field-free SDE efficiency reaches −71.4%." The same paragraph says the forward sweep ends at "−35.7% at 0 mT", and the abstract and Fig. 3(b) give 35.7% as the field-free efficiency. −71.4% is exactly twice 35.7%.
- p. 3: 705 µA excitation "between |Ic+| and |Ic−|" for device #3, while device #1's sweeps in Fig. 1(c) go only to ±300 µA. Different devices, so not a proven conflict; Ic± of device #3 are not stated.

## Matching (step 2)

Matched: diode-vortex-screening (diode family), fine-tuning-and-selection (always).
Skipped, signature does not apply (no tunneling spectroscopy, no Josephson junction, no Majorana, island, Shapiro, chiral, charge or Kitaev claim): abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, fine-tuned-plateau, series-resistance-subtraction, one-end-only, trivial-andreev-band-gap-reopening, full-shell-flux-andreev, chiral-plateau-superconductor-short, island-states-coulomb-spacing, shapiro-landau-zener, shapiro-nonlinear-resistance, charge-trap-fractional-shift, spin-orbit-length-pinning, exceptional-point-zero-mode, transparent-junction-pi-crossing, switching-jump-blind-region, false-poor-mans-majorana, local-probe-loophole, coulomb-dominated-interferometer.
Considered and skipped: micromagnet-stray-field (signature is ZBPs in dots; the stray-field route for a diode is covered by diode-vortex-screening, whose Hou et al. source includes a EuS ferromagnet layer); field-enhanced-supercurrent-resonances (signature is supercurrent growing with field read as triplet pairing; the claim here is nonreciprocity); protocol-parameter-sensitivity (no automated pass/fail protocol).
Adapted: none beyond reading the diode entry against a field-free claim; noted under "What this is".

## Checks (step 3)

The library has no `checks` block for the diode family, so only the practice checks (report-counts, report-ranges, report-processing) were walked. All three Partly.

## Status reasoning

- diode-vortex-screening: plain-film control is claimed in SM only ("ruled out, as shown in SM [40]"), which counts as a sentence pointing elsewhere, so "no". Field dependence shown for device #1 (Fig. 2), not for #3, so "part". Tested in part.
- fine-tuning-and-selection: three devices named, no totals (part); no statement of how shown data were chosen (no); device #3 shown in main text for rectification, device #2 only in SM (part). Tested in part.
- Outside, trapped vortex (Golod and Krasnov 2205.12196): ZFC η shown for device #1 only (part); warming test not shown (no). The paper does not discuss trapped vortices explicitly; it cites [23] (the same Golod and Krasnov work) under "current-induced self-fields". Tested in part.
- Outside, strain (Li et al. 2509.23707): polarity reversal by training shown for both main-text devices (all), but it does not by itself exclude a fixed strain offset under the magnetic part, so not ruled out. Bare NbSe2 control not shown in main text (no). Tested in part. Not mentioned by the paper.

## Sources held out

None. No library source cites this paper (all predate it).

## Related work checks

All five: ID, title and first author confirmed on the arXiv abstract page (citation_title and citation_author meta tags); description checked against the abstract (API summary) only, not full text.
- 2205.09276 Hou et al.: abstract.
- 2205.12196 Golod and Krasnov: abstract.
- 2509.23707 Li et al.: abstract.
- 2301.07121 Gutfreund et al.: abstract.
- 2610.30556 Zapata et al.: abstract (posted after the paper under review; described for its own results).
Searches: arXiv API queries on diode with CrBr3, NbSe2, trapped vortices, remanent, trapped flux, vortex diode; 3 s between calls; no rate limiting hit.

## Library gaps

- No `checks` block for the diode family. Candidate checks: plain-film control of the parent superconductor; measured remanent field at nominal zero; warming between Tc and the magnet's ordering temperature to clear trapped flux; fixed offset from averaging opposite trained states.
- Missing lookalikes: trapped Abrikosov vortex diode with memory (Golod and Krasnov, https://arxiv.org/abs/2205.12196); strain-induced field-free diode in NbSe2 (Li et al., https://arxiv.org/abs/2509.23707); possibly stray-field vortex landscape from magnetic domains (Zapata et al., https://arxiv.org/abs/2610.30556), currently only implicit in diode-vortex-screening.

## Unsure

- Whether a pointer to an unavailable SM should count as "no" or "part"; I used "no" for the plain-film control and said so in the report.
- Whether ZFC η counts as a trapped-vortex test: it covers only the untrained state.
- Page numbers come from page markers in the extracted text.

## Skill issues

- The skill says to read the abstract page and PDF; this run forbade both, so the title came from the text header. The skill does not say what to do when only main text is available and SM is referenced but missing.
- Step 3 does not say how to treat a test the paper says is "shown in SM" when the SM can't be read (sentence pointing elsewhere, or "unclear, mark part").
- The template's "What this is" fixes "in topological transport"; for a non-topological diode paper the scope sentence sits awkwardly inside it.
- The skill says to write reports/<id>.md and notes files; this run's harness refuses .md writes, so both are returned inline.
