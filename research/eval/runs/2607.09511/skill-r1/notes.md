# Run notes: arXiv 2607.09511v1 (skill-r1)

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.4 (updated 2026-10-23). 28 lookalikes.
- Date: 2026-10-23. AI only.

## What I read
- arXiv abstract page (local abs.html): title, 14 authors (first: Francesco Zatelli), v1 submitted 2026-07-10, no ancillary files listed.
- Full text (local paper.txt, 39 pages): main text, Extended Data captions Fig. ED1 to ED12, Methods I to XII, references. I read figure ranges from the extracted axis labels. I did not view rendered figures, so those ranges are approximate.
- Not opened: the data repository (https://zenodo.org/records/21280458). This run allowed fetches only from arxiv.org, export.arxiv.org and api.openalex.org, so I did not use it to count devices or datasets. read_mtx.py was not used (no .mtx data).
- I did not fetch the paper itself, per the run instructions.

## Claims table (step 1)
| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| Coherent parity oscillations in the even manifold | Fig. 2a-d, ED7i,m,n | the one device | VC pulse amplitude about 9 to 11.2 mV (fit uses VC < 11.25 mV); durations 0 to 50/80 ns; f = 106.7 ± 0.4 MHz, T2Rabi = 26 ± 2 ns at VC = 9.8 mV; Q = f·T2Rabi about 2 to 4; leakage about 5%; 2000 to 4000 repetitions per point; ramp 25 ns |
| Odd-manifold oscillations, even/odd frequency match | Fig. 3a,b,h, ED8 | same | agreement "to about 5%"; feven = 113.4 ± 0.5 MHz, fodd = 117.7 ± 0.4 MHz at sweet spot |
| Phase dependence, coupling vanishes near φ = π | Fig. 2e, ED7o | same | B⊥ about 9.5 to 17.5 mT (retuned at 9 fields for Fig. 2e; at 10.5 and 15.6 mT for ED7o); period about 5 mT; loop about 0.4 µm²; a phase jump of about 2.5 mT and a charge jump are disclosed |
| Sweet-spot identification | Fig. 1f,g, Fig. 3c, ED4, ED5 | same | plunger pulses ±5 mV; VLH about 1373.5 to 1374.5 mV, VRH about 1407.5 to 1408.5 mV |
| Detuning dependence (partial protection) | Fig. 4, ED7a-h | same | VC fixed at 9.8 mV; detuning spans of a few tenths of a mV around set points (from axis labels) |
| Second configuration | ED9, ED6 | same device, different cooldown | even manifold only, odd check not available; 5 µs waiting time; no off-resonant drive |
| Readout | ED2, ED3 | same | 500 µs integration; parity lifetimes ≳ 8 ms; ramp 0 to 100 ns explored |
Fixed: B|| = 150 mT; base temperature ≈ 20 mK (no temperature series).
Missing counts: devices fabricated, devices measured, devices showing the effect (one presented); total cooldowns (at least 2); tunings attempted and accepted; total datasets.

## Entries matched, adapted, skipped
- Family: kitaev, plus practice. Checks walked: kitaev-sweet-spots, kitaev-extend-chain, report-counts, report-ranges, report-processing.
- Matched: false-poor-mans-majorana (adapted to time-domain qubit evidence), fine-tuning-and-selection (always; adapted to tuning attempts), quasi-majorana-smooth-confinement (adapted from zbp to overlapping Majorana components in the effective qubit Hamiltonian; the paper raises it itself, citing Vuik et al. [49], which is the library source).
- Skipped as a separate row: local-probe-loophole. Readout here is global quantum capacitance, and the separation question it raises is covered in the adapted quasi-Majorana row.
- Skipped, no tunneling-spectroscopy peak or normal lead in the measured regime: abs-quantum-dot (dots are intentional here), disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, spin-orbit-length-pinning, exceptional-point-zero-mode.
- Skipped, no conductance values: fine-tuned-plateau, series-resistance-subtraction.
- Skipped, no end tunneling or nonlocal conductance: one-end-only, trivial-andreev-band-gap-reopening.
- Skipped, no such element or signal: micromagnet-stray-field, full-shell-flux-andreev (Al strips, no full shell), chiral-plateau-superconductor-short, island-states-coulomb-spacing, shapiro-landau-zener, shapiro-nonlinear-resistance, switching-jump-blind-region, transparent-junction-pi-crossing, field-enhanced-supercurrent-resonances, charge-trap-fractional-shift (no fractional-shift claim; the charge jump is disclosed), coulomb-dominated-interferometer, diode-vortex-screening.
- Skipped: protocol-parameter-sensitivity. There is no automated pass/fail protocol; the tuning criterion is qualitative, and its data-choice concern is under fine-tuning-and-selection.

## Hold-out
- No sources skipped. Every library source used in the matched entries and checks predates the paper (2026-07-10): 2408.10030 v3 (2025-03), 2504.06732 v1 (2025-04), 1806.02801 v3 (2019), 1207.3067 (2012, date from the ID), 2207.02472 v4 (2024), 1911.04512 v3 (2020), 1711.06256 (2017, date from the ID), 2309.09368 v1 (2023), 2501.18631 v2 (2026-03-25). Dates from the arXiv API.
- Legg 2502.19560 v2 is dated 2026-10-21, after the paper. It is only a source for protocol-parameter-sensitivity, which I skipped, so I did not use it and did not check whether it mentions the paper.
- I did not recognize the paper. It postdates my training data, and I used no knowledge of its later history.

## Related work, how checked
- All five related-work papers, plus the outside source: I opened the arxiv.org/abs page and confirmed ID, title and first author. I checked each one-line description against the abstract only, not the full text.
  - 2408.10030 Luethi (4 authors); 2504.06732 Luethi (4); 2408.03071 Luethi (4); 2306.16289 Tsintzis (5); 2407.16750 Pan (3).
  - Outside-row source: 1008.3089 Petersson et al., "Quantum Coherence in a One-Electron Semiconductor Charge Qubit". Its abstract reports pulse-driven coherent rotations in a GaAs double dot with about 7 ns coherence at the charge degeneracy point.
- Seen in search, not opened, not listed: 2609.25223 (Pan et al., Sept 2026, four- and six-dot Majorana qubits).

## Library gaps
- There is no time-domain or qubit family in the entries or checks (Rabi, Ramsey, parity qubits). Candidate entry: ordinary charge-qubit oscillations between subsystems (Petersson 2010, arXiv 1008.3089). Control: compare robustness to single-dot detuning with robustness to one-dot-per-chain detuning.
- Candidate entry or check: matching even/odd qubit frequencies constrains effective couplings, but by itself cannot show spatial separation. The paper says this itself (Methods VIII) and cites Samuelson et al., PRX Quantum 7, 020341 (not opened).
- The kitaev checks have no step for "the acceptance criterion for a tuning equals the headline signal", and none for phase-π overlap tests.
- The false-poor-mans-majorana control is phrased for conductance; it needs a qubit-readout analog.

## Uncertain
- Outside row "ruled out" versus "partly addressed". I chose ruled out because Fig. 4a-d against Fig. 4g,h is a direct comparison within the claimed tuning.
- report-processing "done" rests on the data-availability statement. The repository was not opened.
- report-counts "partly" versus "not done". The paper names one device and a second cooldown, but gives no device totals.
- Figure ranges come from text extraction.
- Word count outside the table is near the top of the 600 to 900 range (estimate, not measured).

## Skill issues
1. Step 7 says to write `reports/<id>.md` and `reports/<id>.notes.md`; this run asked for report.md and notes.md in an eval folder. I followed the run.
2. In this subagent environment the Write tool blocks .md report files. The skill assumes file writes always work, and doesn't say what to do when they are refused.
3. The scope rule says to adapt "matching entries" for a different kind of measurement, but not whether entries from another family (here zbp: quasi-Majorana) may be adapted into a kitaev paper. I adapted one.
4. The outside-lookalike rule says to judge "against the control that paper describes". The outside source (Petersson 2010) describes no control that separates it from Majorana physics, so I used the paper's own comparison. The rule is unclear for sources that only show the ordinary effect.
5. It is unclear whether a check can be "done" on a data-availability statement alone when the repository can't be opened.
6. The template's "What this is" is fixed text, and the scope sentence's placement isn't specified. I appended it to the end of that paragraph.
7. The data-repository instruction ("if you can reach it") conflicts with run-level host restrictions. The skill could say to record "not opened, host not allowed".
