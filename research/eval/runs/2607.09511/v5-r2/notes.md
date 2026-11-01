# Run notes: arXiv 2607.09511v1

## Library and inputs
- Library meta.version 0.5 (updated 2026-10-24), 28 lookalike entries, checks for zbp, shapiro, kitaev, charge and practice.
- Read: skill/SKILL.md, skill/report-template.md, library/lookalikes.yaml, all of them.
- Paper: the local abs.html (title "Majorana parity qubit in coupled minimal Kitaev chains", Zatelli et al., v1 posted 10 Jul 2026) and all of paper.txt (main text, Extended Data captions ED1-ED12, Methods I-XII, references). I rendered PDF pages 5, 7, 8, 17 and 19 to check Figs. 2, 3, 4, ED7 and ED9 by eye. PDF page numbers equal the printed page numbers. The Extended Data and Methods are inside the PDF; there is no separate supplement.
- I did not fetch the paper, its abstract page or any version of it.
- Data repository: https://zenodo.org/records/21280458. The Zenodo API gave no response through the proxy (HTTP 000), so it was not used. There are no arXiv ancillary files, so read_mtx.py was not run.
- I did not recognize the paper: it postdates my training data.

## Claims table (step 1)
| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| Sweet spot found in both chains, both parity manifolds, from pulsed charge-stability diagrams | Fig. 1f,g; ED4; ED5; ED6 | one InSb nanowire device, 2 chains + coupler QDC + parity-switch dot | pulse amplitudes about ±5 mV on VR1, VR2 and VL1, VL2; three VRH settings in Fig. 1f; ED4 VLH about 1374-1375 mV, VRH about 1407-1409 mV |
| Coherent even-manifold oscillations | Fig. 2a-d; ED7i,m,n | same | VC pulse 9-11.2 mV; durations 0-50 ns (2a), 0-80 ns (2b); f = 106.7 ± 0.4 MHz, T2Rabi = 26 ± 2 ns at VC = 9.8 mV; leakage about 5%; 2000-4000 repetitions per point |
| Coupling depends on phase and vanishes near φ = π | Fig. 2e; ED7o; ED6i-n | same | B⊥ about 10-17 mT, period about 5 mT; retuned at 9 fields for Fig. 2e and at 2 fields for ED7o; a phase jump and a charge jump between the two sweeps (p. 24) |
| Odd-manifold oscillations with matching frequency | Fig. 3a,b,h; ED8 | same | agreement "typically" to about 5%; f_even = 113.4 ± 0.5 MHz, f_odd = 117.7 ± 0.4 MHz |
| Hybrid-gate detuning pattern (diagonal or antidiagonal) | Fig. 3c-j; ED7j-l,p,q; ED8b-f | same | δVLH and δVRH ±0.5 mV; pulse fixed at 18 ns for the maps |
| QD detuning shows partial protection | Fig. 4; ED7a-h | same | single-dot and pair detuning windows of about 0.6 mV; VC = 9.8 mV |
| Second dataset, other orbitals and ABS | ED6, ED9 | same device, different cooldown | even manifold only, odd manifold not compared |
| Simulations reproduce the observations | ED10, ED11, Table 1 | model | no fitting; quasistatic Gaussian noise, N = 1000 |

Fixed or single values: B|| = 150 mT only; T about 20 mK only; readout 500 µs; parity lifetimes at least 8 ms (ED3).
Missing: devices fabricated, devices measured, devices that showed the effect, number of cooldowns (at least 2), number of sweet spots tried.

## Matching (step 2)
- Family: kitaev. Checks walked: kitaev-sweet-spots, kitaev-extend-chain, then practice report-counts, report-ranges, report-processing.
- Entries matched: false-poor-mans-majorana and local-probe-loophole (both adapted), plus fine-tuning-and-selection (always).
- Adapted for time-domain data (Scope rule):
  - false-poor-mans-majorana: the signature moves from transport zero-energy states to parity oscillations; the tests are unchanged.
  - local-probe-loophole: the readout is a quantum-capacitance parity readout of each chain, not a local conductance probe. I took the even/odd frequency comparison through the coupler dot (Eq. 22) as the equivalent of "overlap estimated through a quantum dot in series". I counted the single-site detuning of Fig. 4 and the φ ≈ π data as partial nonlocal evidence.
  - kitaev checks: applied to time-domain tuning.
- Skipped, and why:
  - abs-quantum-dot, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, spin-orbit-length-pinning, micromagnet-stray-field, full-shell-flux-andreev: these are zero-bias-peak tunneling signatures, and there is no zero-bias-peak claim here.
  - quasi-majorana-smooth-confinement: its mechanism is a smooth confinement at a nanowire end, and its tests are nonlocal-conductance gap reopening, which doesn't fit a two-dot chain. The paper's own quasi-Majorana caveat (p. 29) is handled under local-probe-loophole.
  - exceptional-point-zero-mode: needs a coupling to a normal lead, and the leads are pinched off.
  - fine-tuned-plateau, series-resistance-subtraction: the paper claims no conductance values.
  - one-end-only, trivial-andreev-band-gap-reopening: there is no nonlocal-conductance or gap-protocol claim.
  - protocol-parameter-sensitivity: there is no automated pass/fail protocol. The sweet-spot criterion is applied by hand.
  - island, shapiro (4 entries), supercurrent, charge (2), chiral, diode: other signals.

## Hold-out
- No library source discusses this paper.
- Library sources with versions after 10 Jul 2026: only 2502.19560v2 (updated 2026-10-21). I fetched the full text of v2: no "2607.09511", "Zatelli" or "parity qubit" in it. Its entry was skipped in any case.
- 2501.18631v2 (updated 2026-03-25) predates the paper. 2309.09368 quotes come from v1 (2023).
- Nothing was held out.

## Related work checks
- 2408.10030 (Luethi): abstract page and API abstract.
- 2504.06732 (Luethi): abstract page and API abstract.
- 2306.16289 (Tsintzis): abstract page and full text. Both quotes confirmed on PDF p. 13.
- 2407.16750 (Pan, Das Sarma, Liu): abstract page and full text. Quote confirmed on PDF p. 5.
- 2510.20538 (Samuelson): abstract page. v2 is dated 2026-05-29, before the paper. Its authors overlap with the paper (Torres Luna, Miles, Wimmer); it is listed for its own results.
- Also opened, not listed: 1008.3089 (Petersson et al., charge qubit), abstract only. I considered it as the source for the outside row and used Pan et al. instead, because Pan et al. compare directly with Kitaev-chain qubits.
- Seen in search results only, not opened, not listed: 2408.03071 (imperfect PMMs) and 2609.25223 (Pan and Das Sarma, Sept 2026).
- The arXiv API was spaced about 3 s apart; no rate errors.
- My downloads are in /tmp/claude-0/-home-user/24b43eef-50bb-5f66-84b8-aad72ef55ba1/scratchpad/r2607/.
- The scratchpad folder rel/ already held files from earlier runs. I did not use them.

## Library gaps
1. Ordinary double-dot charge qubit as a lookalike for Kitaev-chain qubit oscillations. Source: Pan et al. 2407.16750, p. 5, "is equivalent to semiconductor charge qubits if all superconductivity is removed from considerations". Its tests are mine, taken from that paper's comparison: the same Rabi experiment in a charge-qubit configuration, and dephasing time and quality factor.
2. The kitaev checks have no steps for time-domain qubit data. Missing steps: compare frequencies in both parity manifolds; show suppression near φ = π; contrast single-dot and whole-chain detuning (Tsintzis 2306.16289 p. 13).
3. There is no Kitaev-specific entry for overlapping Majorana components or quasi-Majoranas in dot chains, or for imperfect PMMs (2408.03071). I had to adapt local-probe-loophole.

## Unsure
- I counted the second-cooldown ED6 and ED9 data as evidence presented ("coherent parity oscillations measured in a different tuning configuration", p. 8). That turned several tests from all to part.
- "Microscopic model of the device": I marked it part. The Eq. 5 Kitaev model is microscopic for dots, but it is spinless with t and Δ as inputs, so it can't produce false PMMs. "No" would also be defensible.
- Charge-qubit row "Ruled out": this rests on the one-separating-test clause for the Fig. 4g,h and ED9k,l comparison. The dephasing and Q test is only part, since ED9 was not fitted.
- report-counts: "partly" or "not done". The paper releases all data on this device but says nothing about other devices.
- The report runs about 900 words outside the table, at the top of the target.

## Skill issues
1. The Scope rule says to adapt matching entries but gives no rule for adapting their tests. It is unclear when a different-modality measurement (the even/odd frequency match) counts as the "equivalent test" of a transport test.
2. "Evidence the paper presents" is ambiguous for Extended Data datasets from other cooldowns that the main text cites as support. Including them changes all to part across rows.
3. kitaev-sweet-spots asks "how many were found and kept". That overlaps with the rule that selection gaps are counted once under fine-tuning-and-selection, and it is unclear whether missing counts should make this check "partly".
4. For outside rows, "take its tests from the control that paper describes" fits poorly when the source paper is a theory comparison without a stated control. I paraphrased the tests from Pan et al.'s comparison.
5. The template's "What this is" text is fixed to "topological transport". The adaptation sentence has to be appended, which pushes the word count.
6. The 600 to 900 word target is tight once the template boilerplate, five checks, eight questions and five related-work lines are in.
7. Step 7 writes the report to reports/; this run's prompt overrode that. No conflict.
