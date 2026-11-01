# Run notes: arXiv 2607.09511v1

AI only. Lookalike library version 0.4 (meta.updated 2026-10-23), 28 lookalikes, 18 checks.

## What I read
- The arXiv abstract page (local abs.html): title "Majorana parity qubit in coupled minimal Kitaev chains", 14 authors, first author Zatelli, Francesco. v1 submitted 10 Jul 2026. There are no ancillary files, so read_mtx.py was not needed.
- The full text of v1 (local paper.txt, 39 PDF pages): main text pp. 1-9, Extended Data Fig. ED1-ED12 pp. 11-21, Methods I-XII pp. 22-35, references pp. 35-39. I took page numbers from the form-feed page breaks in the extracted text and checked them against the printed page numbers. Every quote in the report was checked verbatim against the extracted text, with whitespace normalized.
- I did not view the figures as images. Axis ranges come from the extracted axis labels and the captions.
- I did not fetch the paper itself, as instructed.

## What I couldn't open
- The data repository https://zenodo.org/records/21280458. The proxy refused the tunnel (403). So I did not use it to count devices or datasets.

## Recognition
- I did not recognize the paper. Its v1 date (July 2026) is after my knowledge cutoff. No knowledge of later history was used.

## Claims table (step 1)

| Claimed signal | Figures | Device | Counts and ranges |
|---|---|---|---|
| Coherent parity oscillations between ee and oo (even manifold), driven by a coupler-dot pulse | Fig. 2a,b; ED7i | One InSb nanowire device ("the device presented in this work", p. 9) | f = 106.7 ± 0.4 MHz, T2Rabi = 26 ± 2 ns at VC = 9.8 mV (p. 5); VC about 9 to 11.25 mV used in the fits (p. 26); pulse duration 0 to about 80 ns; 2000-4000 repetitions per point (p. 26); leakage about 5% (p. 5) |
| Frequency inversely proportional to coupler detuning | Fig. 2c, ED7m | same | fit f = K/(V0 - VC) for VC < 10.8 mV (ED7m) |
| Phase dependence: oscillations suppressed near φ = π | Fig. 2e, ED7o | same | B⊥ about 9.5 to 17.5 mT, retuned at 9 fields (p. 24); period about 5 mT (p. 6); phase jump of about 2.5 mT and a charge jump before Fig. 2e (p. 24) |
| Odd-manifold oscillations with frequencies matching the even manifold to about 5% | Fig. 3a,b,h; ED8 | same | feven = 113.4 ± 0.5 MHz, fodd = 117.7 ± 0.4 MHz (Fig. 3h) |
| Diagonal and antidiagonal hybrid-gate patterns in the two manifolds | Fig. 3c-j; ED7j-l,p,q; ED8 | same | δVLH, δVRH about ±0.5 mV; pulse 18 ns, VC 9.8 mV |
| Detuning response: single dot gives p → 0.5, one chain gives p → 1, one dot per chain gives the charge-qubit comparison | Fig. 4a-h; ED7a-h | same | single-dot axes span about 0.6 mV per dot (from the axis labels) |
| Sweet-spot identification from pulsed charge-stability diagrams, crossings in both chains and both manifolds | Fig. 1f,g; ED4; ED5 | same | verified "before every measurement presented in the main text" (p. 31) |
| Second tuning (other dot orbitals and ABSs), even manifold only | ED9; ED6 | same device, different cooldown (p. 24) | odd manifold not assessed (p. 24) |

Missing counts: devices fabricated, devices measured, devices that showed the effect, total cooldowns (at least two are mentioned), number of tune-ups tried and kept. The only parallel field is B|| = 150 mT and the only temperature is base, about 20 mK (p. 4). Nothing is said about other ranges measured.

## Matching (step 2)
- Family: kitaev, plus practice.
- Matched:
  - false-poor-mans-majorana (direct match)
  - fine-tuning-and-selection (always included)
  - quasi-majorana-smooth-confinement (adapted)
  - local-probe-loophole (adapted)
- Adapted entries (scope: time-domain qubit data):
  - quasi-majorana-smooth-confinement: the signature was a pinned zero-bias peak. I adapted it to "decoupled but overlapping Majorana components giving the same effective qubit Hamiltonian", because the paper raises this itself (p. 29, citing Vuik et al.).
  - local-probe-loophole: the signature was a single local tunneling probe. I adapted it to one global quantum-capacitance readout plus an even/odd frequency comparison, which bounds only the product of the two chains' overlaps (p. 34).
- Skipped, and why:
  - abs-quantum-dot, kondo-resonance, full-shell-flux-andreev, spin-orbit-length-pinning: these are tunneling-spectroscopy signatures of unintended dots or nanowire segments. Here the dots are intended and there is no zero-bias-peak claim.
  - disorder-induced-zbp, crowded-trivial-subgap-states, weak-antilocalization: no conductance-peak signature.
  - fine-tuned-plateau, series-resistance-subtraction: no conductance values.
  - one-end-only: the device has no end-tunneling probes in the qubit regime. The closest analog is covered under local-probe-loophole.
  - trivial-andreev-band-gap-reopening: no nonlocal gap claim.
  - exceptional-point-zero-mode: the device is pinched off from the leads during the experiment.
  - micromagnet-stray-field: no magnets.
  - protocol-parameter-sensitivity: no automated pass/fail protocol. The tuning criterion is qualitative.
  - chiral, island, shapiro, supercurrent, charge, diode entries: none apply.
  - charge-trap-fractional-shift: charge jumps are reported (p. 24), but there is no fractional-shift claim. I raised it as a data question for Fig. 2e instead.

## Checks walked (step 3)
- kitaev-sweet-spots: partly.
- kitaev-extend-chain: not done.
- report-counts: partly.
- report-ranges: partly.
- report-processing: done.

## Sources held out
- None of the library sources I relied on discusses the paper under review. I checked arXiv version dates through the API:
  - 2408.10030v3: 2025-03-24
  - 2504.06732v1: 2025-04-09
  - 2501.18631v2: 2026-03-25
  - 1806.02801v3: 2019
  - 2309.09368v1: 2023
- All of these predate 10 Jul 2026, so none can cite it.
- 2502.19560v2 (Legg comment, updated 2026-10-21) postdates the paper. I did not use it (its entry was skipped) and did not check its text for a mention.

## Related-work checks (step 5)
All five were opened on arxiv.org/abs, and I confirmed the ID, title and first author. I checked each one-line description against the abstract only, not the full text.
- 2504.06732: Luethi, Melina; title matches; abstract supports "the most stable PMMs ... appear in a region ... that also has a large ratio of false to true PMMs".
- 2408.10030: Luethi, Melina; title matches; abstract supports "some PMMs evolve into trivial highly localized low-energy states" and "no clear conductance signature".
- 2408.03071: Luethi, Melina; title matches; abstract supports "highly, but not perfectly, localized".
- 2407.16750: Pan, Haining (3 authors, matching ref. 8); title matches; abstract supports the longer dephasing compared with charge qubits.
- 1008.3089: Petersson, K. D.; title matches; abstract supports "maximum coherence time of ~7 ns at the charge degeneracy point".

Considered and not listed: 2609.25223 (Pan et al.) and 2610.17198 (Miles et al.). Both are later than the paper and likely discuss this experiment, so I left them out to keep the related work about their own results.

## Library gaps
- Conventional charge qubit oscillations (double quantum dot, Petersson et al. 2010, https://arxiv.org/abs/1008.3089) are not in the library. The paper raises the comparison itself (p. 9).
- The kitaev family has no time-domain checks. Useful ones would be:
  - compare even and odd manifold frequencies;
  - the φ = π test of overlap;
  - splitting against single-dot detuning, quadratic or linear;
  - a coherence-time bound for the charge-qubit control.
- false-poor-mans-majorana is written for conductance signatures. A qubit-oriented signature line would help.

## Unsure
- Charge-qubit lookalike: the call was between ruled out and partly addressed. Fig. 4g,h is a direct comparison at the shown tuning. I picked partly addressed because it is shown at one VC with 25 ns ramps, and a nanosecond-coherence charge qubit might go unresolved.
- Questions 5 and 6 rest on my reading of an apparent tension between p. 8 and p. 9, and of Methods XI (p. 34). They may reflect wording, not a gap.
- Fig. 4 axis spans come from extracted text labels and may be misassigned between panels.

## Skill issues
- Step 7 says to write reports/<id>.md and notes files. This run was told to return them inline, which overrides the skill.
- The template says "a library of <n> known lookalikes". It is unclear whether n is all entries (I used 28) or the matched ones.
- local-probe-loophole is family "practice", but only fine-tuning-and-selection is named as always included. It is unclear whether every practice lookalike should be matched by default.
- The report-ranges and report-processing checks address protocol-parameter-sensitivity, which I skipped. The skill doesn't say how a check's status should be read when one of the lookalikes it addresses was skipped.
- The skill says the four standard questions must always be asked, and also caps the list at eight. When the paper invites many specific questions, the cap leaves four slots.
- The "no contrast phrasing" rule makes it hard to describe tests with two outcomes (quadratic or linear). I used "whether ... or ...".
- Data repository use: the skill allows reaching it, but the run instructions list only arXiv and OpenAlex hosts. It was unreachable anyway.
