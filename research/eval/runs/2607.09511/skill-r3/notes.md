# Run notes: arXiv 2607.09511v1

AI only. Lookalike assistant run on 2026-10-23.

## Library

- lookalikes.yaml meta.version 0.4 (updated 2026-10-23), 28 lookalike entries, plus the checks section. Read once at the start.
- Families used: kitaev (checks kitaev-sweet-spots, kitaev-extend-chain) and practice (report-counts, report-ranges, report-processing).

## What I read

- The arXiv abstract page (local copy abs.html): title "Majorana parity qubit in coupled minimal Kitaev chains", 14 authors (Zatelli first), v1 submitted 2026-07-10. This is the only version.
- The full extracted text (paper.txt), all 40 pages: main text, Extended Data Figs. ED1 to ED12, Methods I to XII and references. Page numbers come from form feeds in the text, checked against the printed page footers.
- PDF pages 3 to 8, rendered at 80 dpi, to read the figure axes for Figs. 2, 3 and 4.
- I did not fetch the paper itself from any URL.
- Data repository: the paper links https://zenodo.org/records/21280458 ("All raw data measured on the device presented in this work at the time of writing"). I tried the Zenodo API (metadata and file list only). The proxy refused it with "CONNECT tunnel failed, 403", so I couldn't use it to count devices, datasets or ranges. There are no arXiv ancillary files, so read_mtx.py was not used.
- Every quote in the report was string-checked against paper.txt with whitespace normalized and line-break hyphens removed. In the Zenodo quote, the text has a line break inside the URL ("https://zenodo.org/ records/21280458"); I joined it.

## Claims table (step 1)

| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| Coherent parity (Rabi) oscillations between ee and oo in the even manifold; frequency set by coupler-dot detuning, f proportional to 1/(V0 - VC) | Fig. 2a-d; ED7i,m,n | The one device | VC about 9 to 11.2 mV, fit only for VC < 11.25 mV (p. 26); pulse duration 0 to 50 ns (Fig. 2a), 0 to 80 ns (Fig. 2b); f = 106.7 ± 0.4 MHz, T2Rabi = 26 ± 2 ns at VC = 9.8 mV (p. 5); leakage about 5% |
| Phase dependence: about 5 mT period, frequency suppressed near phi = pi | Fig. 2e; ED7o | Same | B-perp about 9.5 to 17.5 mT, retuned at 9 fields (p. 24); a phase jump of about 2.5 mT between ED7o and Fig. 2e; a charge jump before Fig. 2e, "after which the device displayed increased instability" |
| Odd-manifold oscillations; even and odd frequencies agree "typically ... to about 5%"; 113.4 vs 117.7 MHz at the sweet spot | Fig. 3a,b,h; ED8a,g-i | Same | Same VC range |
| Hybrid-gate detuning: even-manifold mixing along the antidiagonal, odd along the diagonal | Fig. 3c-j; ED7j-l,p,q; ED8b-f | Same | VLH about 1373.5 to 1374.5 mV, VRH about 1407.5 to 1408.5 mV; delta about ±0.5 mV; fixed 18 ns pulse |
| Partial protection: one-dot detuning keeps p near 0.5, two-dot detuning within a chain gives p toward 1; the effective double-dot limit (Fig. 4g,h) is compared with a charge qubit | Fig. 4a-h; ED7a-h | Same | Dot pulse ranges about ±0.3 mV around the center; VC = 9.8 mV |
| Sweet-spot tuning from pulsed charge-stability diagrams in both manifolds | Fig. 1f,g; ED4; ED5; ED6 | Same | Retuned before each 2D sweep; most 2D maps take 1 to 4 hours |
| Second tuning configuration (other QD orbitals and ABS), even manifold only | ED9; ED6 | Same device, different cooldown | Odd-manifold comparison not done (p. 19, p. 24) |

Global settings: B-parallel = 150 mT only; base temperature about 20 mK only; 2000 to 4000 repetitions per point; 500 µs readout; parity lifetimes of at least 8 ms (ED3); 25 ns ramps (ED2 goes up to about 75 ns and beyond).

Missing counts: devices fabricated (not stated); devices measured (one presented, others not mentioned); devices showing the effect (1 of an unknown number); cooldowns (at least 2); sweet spots or tunings found versus kept (not stated); other parallel fields, field directions and temperatures (not stated); no Ramsey or echo data.

## Entries matched, adapted, skipped

- Matched and adapted for time-domain data, per the Scope rule:
  - false-poor-mans-majorana: the signature moved from zero-energy states in transport to parity-qubit oscillations. The kitaev checks' signal already covers "qubit behavior".
  - local-probe-loophole: there is no local probe here. I adapted it to "effective-Hamiltonian evidence read as spatially separated Majoranas", which is the paper's own caveat in Methods VIII.
- Matched as written: fine-tuning-and-selection (always applies).
- Skipped:
  - All zbp entries (abs-quantum-dot, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, micromagnet-stray-field, full-shell-flux-andreev, spin-orbit-length-pinning, exceptional-point-zero-mode): there is no zero-bias conductance peak claim. The hybrid-segment ABSs are by design here, not a lookalike.
  - quasi-majorana-smooth-confinement: it needs smooth confinement in a continuous wire. The paper mentions quasi-Majoranas (Methods VIII, citing Vuik et al.), and that concern is covered by the adapted local-probe-loophole row.
  - quantization entries (fine-tuned-plateau, series-resistance-subtraction): there is no quantized-conductance claim.
  - nonlocal (one-end-only, trivial-andreev-band-gap-reopening), island, shapiro (4 entries), supercurrent, charge (2 entries), chiral and diode entries: the signatures are absent.
  - protocol-parameter-sensitivity: the paper has a tuning procedure, not an automated pass/fail protocol.
- Checks: only the kitaev and practice families apply. The zbp and shapiro checks were not used.

## Status reasoning

- I used no "ruled out" anywhere. The paper addresses each row in part. Where I was unsure, I took the weaker status per the skill.
- report-processing is marked "done" from the paper's statement, without opening the Zenodo record.
- The outside row (charge-qubit oscillations) is judged against the comparison Pan et al. describe (coherence time and quality factor of the Majorana qubit against a conventional charge qubit) and against Petersson et al.'s coherence-versus-detuning baseline.
- I left one small tension in the paper's wording out of the report. p. 8 says one-dot detuning shows "no sizable longitudinal splitting"; p. 9 says single-dot detuning "removes the sweet spot protection and suppresses the oscillations". Both describe dephasing, so this is likely not a conflict.

## Hold-out

- No library source I used discusses the paper under review. Luethi 2024 (2408.10030, v3 March 2025), Luethi 2025 (2504.06732, v1 April 2025), Prada 2020, Frolov 2309.09368v1 (2023) and Akrap 2501.18631 (v2 dated 2026-03-25) all predate 2026-07-10. Their abstract pages do not mention 2607.09511.
- Legg 2502.19560 has a v2 dated 2026-10-21, after the paper. I did not use it (protocol-parameter-sensitivity was skipped). Its abstract page does not mention 2607.09511, but I did not read its full text.
- No sources were skipped under the hold-out rule.

## Related-work checks (all on arXiv abstract pages, fetched 2026-10-23, about 3 s apart)

- 2408.10030: ID, title and first author (Luethi) confirmed. The abstract states the result described.
- 2504.06732: ID, title and first author (Luethi) confirmed. The abstract states the stability-versus-false-ratio finding.
- 2306.16289: ID, title and first author (Tsintzis) confirmed. The abstract proposes coupling two PMM systems into a qubit and says it "requires some extra care, appropriately modified protocols". This is the arXiv title of the paper's ref. 6 (PRX Quantum 5, 010323).
- 2407.16750: ID, title and first author (Pan) confirmed. The abstract states the Rabi and Ramsey simulation with charge noise and the comparison with charge qubits.
- 1008.3089: ID, title and first author (Petersson) confirmed. The abstract states the GaAs double-dot charge qubit with about 7 ns coherence at degeneracy.
- Found but not listed:
  - 2609.25223 (Pan and Das Sarma, 2026-09-21). Its abstract names this paper ("following the recent experimental realization arXiv:2607.09511"). I left it out to keep later reception out of the report.
  - 2510.20538 (Samuelson et al.). Relevant to the locality question; I left it out to stay at five.

## Library gaps

- Conventional charge-qubit (or Andreev-qubit) oscillations in coupled dots, as a lookalike for parity-qubit oscillations. Sources: Petersson et al. 2010 (https://arxiv.org/abs/1008.3089) and Pan, Das Sarma and Liu 2024 (https://arxiv.org/abs/2407.16750).
- There are no time-domain checks for the kitaev family: readout fidelity and leakage, Ramsey or echo coherence, phase dependence (cos(phi/2) suppression at phi = pi) and per-chain overlap bounds.
- local-probe-loophole has no wording for global or effective-Hamiltonian probes. The same loophole applies to them, and the paper states it itself (Methods VIII).

## Recognition and uncertainty

- I did not recognize the paper; it postdates my training data. While searching I saw the abstract of a later paper that cites it (2609.25223). I did not use that in the report.
- I am unsure whether a single sentence plus Fig. 4g,h should count as "partly addressed" or "ruled out at that tuning" for the charge-qubit row. I picked the weaker status because no numbers are extracted for that configuration.
- The 600 to 900 word aim: the report is about 915 words outside the table, mostly because the quotes are long.

## Skill issues

- Step 7 says to write reports/<id>.md and reports/<id>.notes.md. This run's instructions forbid .md writes, so both are returned inline.
- The input section says to use a linked data repository "if you can reach it". The run prompt lists allowed hosts only for related work, so it is unclear whether Zenodo was allowed. I tried it and the proxy blocked it.
- The Scope rule says to adapt entries for time-domain qubit data, but the checks section has no time-domain steps. It is unclear whether to invent adapted checks; I did not.
- The template's "library of <n> known lookalikes" doesn't say whether n is all entries (28) or the matched ones. I used 28.
- The rule for outside rows ("judge it against the control that paper describes") assumes the cited paper describes a control. Petersson et al. report a baseline, not a control, so I paired it with Pan et al.
- The hold-out rule doesn't say how to check library sources with versions newer than the paper (Legg v2) when only the abstract page is readable.
- For report-processing, it is unclear whether "done" needs the repository to be verified or only the paper's statement.
