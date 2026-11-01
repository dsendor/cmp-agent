# Run notes: arXiv 2610.18817v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (updated 2026-10-24), 28 lookalike entries, checks for families zbp, shapiro, kitaev, charge, practice.
- Skill and template read once at the start: skill/SKILL.md and skill/report-template.md. scripts/read_mtx.py was not used because there are no ancillary .mtx files.

## What I read
- abs.html (the local copy of the arXiv abstract page): title, authors, date 2026-10-13, abstract, subject cond-mat.mes-hall. No comments field, and no ancillary files listed.
- paper.txt in full (24 pages: main text, Methods, Tables I to III, Extended Data Figs. 1 to 11).
- paper.pdf: I rendered and viewed pages 2 (Fig. 1) and 7 (Fig. 4) to check Fig. 1j (the datasets and fields) and Fig. 4e to g (the merging lines). I also rendered pages 6, 19 and 23 but did not view them.
- No data repository or code link appears in the paper. No data availability statement was found, so device and dataset counts come from the text only.
- I did not fetch the paper itself (local copies only, per the run instructions).
- I did not recognize the paper. It postdates my training data.

## Claims table (step 1)
| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| e/3 tunneling: resonance spacing at 1/3 and 2/3 about 3x smaller than at ν = 1 | Fig. 1h–j; Extended Data Figs. 3, 7 | one device, 90 nm hole | B = 5, 8.97, 13.4, 13.5 T (Fig. 1j, Table I); δ 250–300 mV at ν = 1 and 80–100 mV at 1/3 and 2/3; T 25–500 mK (Extended Data Fig. 3); VDC up to ±1.5 mV |
| Dot depleted to Nqp = 0; single-anyon regime; irregular addition for Nqp = 1–5 matched by DMRG | Fig. 3a–g; Extended Data Figs. 6, 8 | same | B = 4.5 T (ν = 1 calibration) and 13.5 T; VT about 0.04–0.12 V (Extended Data Fig. 6); Vdot −1.03 to 3.97 V (Fig. 3a); few-quasihole regime not reached ("We were unsuccessful in accessing the few quasihole regime in weak backscattering", p. 5) |
| Quantum Hall ferromagnet spin blockade at ν = 1 fixes the dot polarity | Fig. 2a–i | same | B = 5 T; Vdot about −3 to 4 V; EZ ≈ 0.58 meV |
| Regular spectra (1/3 quasiholes, 2/3 quasiparticles) against irregular ones (1/3 quasiparticles, 2/3 quasiholes) | Fig. 4a–d; Extended Data Figs. 9–11 | same | |Nqp| ≈ 10–20; B = 13.5 T; gates swept: VT, Vedge, Vqpc, D (Extended Data Figs. 9, 10) |
| Anyon binding: weak sectors vanish, dot charges in 2e/3 steps | Fig. 4e–g | same | B = 13.5 T; VT 0.040–0.050 V; Vdot 3.785–4.5 V; VDC = 55 µV (Fig. 4f) |
| Figures of merit: excitation energies 0.3–0.8 meV; charge noise | Fig. 2i; Extended Data Fig. 5; Table III | same | 15.5 h series; 10^-4 to 10^-2 Hz; three transitions at ν = 1 only |

- Counts found: 1 device presented; 2 cooldowns (lock-in in the first, DC in the second). Table I's frequency column suggests that Fig. 1j mixes both cooldowns and that Figs. 3 and 4 are DC, which would make them the second cooldown. That is my inference.
- Counts missing: devices fabricated (the contributions say "the devices", plural), devices measured, devices showing the effect, total datasets, and the gate space explored beyond Table I and Extended Data Figs. 9 to 11.
- Small inconsistencies (left out of the report except the first, which is question 5):
  - Table I gives νbulk = 2/5 for Fig. 1h, while the p. 3 text says νbulk = 1/3.
  - Table I lists lock-in frequencies of 13.77 and 17.77 Hz, while Methods says 13.333 or 17.777 Hz.

## Entries matched, skipped, adapted
- Matched:
  - charge-trap-fractional-shift (charge family). It covers both claims, the e/3 spacing and the even-odd and missing sectors.
  - fine-tuning-and-selection (always included).
- Checks walked: the charge family (charge-regime-map, charge-control-regime, charge-repeat-sweeps), then the practice checks (report-counts, report-ranges, report-processing).
- Skipped:
  - coulomb-dominated-interferometer. Its signature is a Fabry-Perot interferometer read through Aharonov-Bohm interference. This device has no interference loop, and the claim rests on Coulomb blockade charging, which is the Coulomb-dominated mechanism by design. Its check (charge-regime-map) was still walked.
  - protocol-parameter-sensitivity: there is no pass/fail protocol. The dip-finding algorithm in Extended Data Figs. 9 and 10 is not one, and its reliability is raised under the outside row.
  - series-resistance-subtraction: there is no claim at 2e^2/h, and the voltage is measured across the device, so nothing is subtracted.
  - local-probe-loophole: the entry is Majorana-specific.
  - All zbp, quantization, nonlocal, island, shapiro, supercurrent, chiral, kitaev and diode entries: no superconductor and no Majorana claim.
- Adapted: none. The paper is in scope (quantum Hall dot transport, charge family). The sentence in "What this is" only says which part of the library applies.
- Judging: I treated Fig. 4e–g as the evidence presented for binding and Fig. 1h–j with Fig. 3 as the evidence for e/3. The charge-trap status covers both. The two-gate maps are shown for both claims. The gate-sensitive even-odd locations (Extended Data Fig. 10) are why I did not mark it ruled out.

## Sources held out
- None. The sources of the matched entries and checks are Frolov 2023 v1, Zhang 2021, Halperin 2011, and Akrap 2501.18631 v2 (v2 dated 25 Mar 2026, checked on its arXiv page). All predate the paper (13 Oct 2026), so none can cite it.

## Related work, how each was checked
- 1201.1600 (Kou et al.): abstract page opened; ID, title, first author and claim confirmed from the abstract.
- 2005.12723 (Röösli et al.): abstract page opened; confirmed from the abstract.
- 1409.4427 (Choi et al.): abstract page opened; confirmed from the abstract.
- 1709.04504 (Frigeri, Scherer, Rosenow): abstract page opened and full text read (intro, the pairing-scenario section, conclusion). The one-line description, including alternating addition to the inner and outer edges, is confirmed in the full text.
- 2309.09368 (Frolov et al.): abstract page opened; the description is confirmed from the abstract.
- cond-mat/0212489 (Elzerman et al., the outside lookalike source): abstract page opened and full text read. The control is in the text: "The important advantage of QPC charge detection is that it provides a signal even when the tunnel barriers of the dot are so opaque that IDOT is too small to measure [8, 9]."
- Opened but not listed: cond-mat/0007383 (Kataoka et al., compressible rings around an antidot, h/2e). I dropped it to stay at five.
- arXiv API searches were spaced about 3.5 s apart. No rate-limit errors.

## Library gaps
- No entry for a charge assigned from a gate-period ratio that assumes the same lever arm and capacitance at different fillings and fields. A capacitance-independent route uses the field period (as in Kou et al.). This went in as a question, not a row, because I opened no paper that shows the period ratio misleading.
- No entry for "missing charge sectors" or "pairing" signatures in Coulomb blockade (charge family). I added the outside row for transitions too weakly coupled to show in transport (Elzerman et al.).
- Candidate entry: apparent pairing from inter-edge Coulomb coupling in nested edges (Frigeri et al. 1709.04504; Choi et al. 1409.4427). Not added as a row, because its published mechanism halves periods in interferometers and does not plainly produce a missing sector in a closed dot.
- The charge family has no check for depleting the dot to a known charge state (calibrating the absolute occupation), which this paper does at length.

## Unsure
- Status of charge-trap-fractional-shift. It could be argued ruled out for the e/3 claim alone, since the ν = 1 spacing at matched field and the gate-independent 1/3 quasihole spacings both stand against it. I kept it at tested in part because the row also covers the binding claim and leakage is not shown.
- Whether gate leakage counts as a test the paper "doesn't show" or as data it doesn't show. I treated it as a test on the presented evidence.
- The outside row's only test (a charge detector) is new hardware. The suggested check (sector width against VT from the Fig. 4f data) is my adaptation and is not in Elzerman et al.

## Skill issues
- The skill says to write reports/<id>.md and notes; this harness asked for them in the reply. I followed the harness.
- charge-regime-map is phrased for interferometers ("Aharonov-Bohm or Coulomb-dominated"). For a closed Coulomb blockade dot, the regime is set by design, so grading "say which regime" is ambiguous. I graded Partly: regime named, no field-gate map.
- The skill doesn't say how to handle one lookalike covering two claims with different evidence (here e/3 and binding). One row with one status hides that the e/3 claim is closer to ruled out.
- The rule "take its tests from the control that paper describes" for outside rows can yield only new-hardware tests. Then "data bear on it" depends on my own analysis suggestion, which the skill doesn't explicitly allow as a test.
- The template doesn't say where an outside row's URL goes. I put it in the Lookalike cell.
- The template has no slot for a short paragraph after the table. I added one to reach the word target.
