# Run notes: arXiv 2607.09511v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (updated 2026-10-24), 28 lookalike entries.
- Skill: cmp-assistant/skill/SKILL.md with skill/report-template.md. Run date 2026-10-24.

## What I read
- Local abs.html (title, authors, abstract, v1 submitted 10 Jul 2026) and paper.txt (full text, 39 pages: main text pp. 1-9, Extended Data Figs. ED1-ED12 pp. 11-21, Methods I-XII pp. 22-35, references). Page numbers taken from form-feed breaks in paper.txt, matching the printed page numbers. I did not open the PDF itself; figures were read from captions and main text only, so panel-level details (exact axis ranges) rest on the text.
- No ancillary files on the abstract page. Data repository https://zenodo.org/records/21280458 is linked; zenodo.org was refused by the egress proxy (CONNECT 403), so I could not count datasets or ranges from it.
- I did not recognize the paper or its later history. A later paper (Pan and Das Sarma, arXiv 2609.25223) surfaced in an arXiv search and names this paper in its abstract; I did not use or list it.

## Claims table (step 1)
| Claimed signal | Figures | Device | Counts and ranges |
|---|---|---|---|
| Coherent parity (Rabi) oscillations between ee and oo, frequency set by coupler VC | Fig. 2a-d, ED7i,m,n | one device, main tuning | VC pulse ~9-11.25 mV fitted (fit limit VC < 11.25 mV, p. 26); pulse duration 0-80 ns; ramp 25 ns (ED2: up to ~75 ns); f = 106.7 ± 0.4 MHz, T2Rabi = 26 ± 2 ns at VC = 9.8 mV (Fig. 2b); 2000-4000 repetitions per point; leakage ~5% |
| Phase dependence, suppression near φ = π | Fig. 2e, ED7o, ED9b, ED6i-n | same device; ED6, ED9 from a different cooldown | B⊥ ~9.5-17.5 mT, period ≈ 5 mT; retuned at 9.5 to 17.5 mT in 1 mT steps; a phase jump (~2.5 mT shift) and a charge jump before Fig. 2e |
| Equal even and odd frequencies at the sweet spot | Fig. 3a,b,h, ED8 | main tuning | agreement "to about 5%"; f_even 113.4 ± 0.5, f_odd 117.7 ± 0.4 MHz |
| Detuning response following PMM partial protection; charge-qubit comparison | Fig. 3c-j, Fig. 4a-h, ED7, ED9 | main tuning plus ED9 tuning | VLH ~1374-1374.5 mV, VRH ~1408-1408.5 mV; plunger pulses ±~1.5 mV in Fig. 4; VC fixed 9.8 mV |
| Sweet spot identified by crossings in both manifolds for both chains | Fig. 1f,g, ED4, ED5, ED12 | main tuning | plunger pulse amplitudes ±5 mV |
| Model reproduces observations | ED10, ED11, Table 1 | theory | 1000 quasistatic noise realizations; parameters chosen, no fitting |

- Fixed parameters: B|| = 150 mT only, T ≈ 20 mK only, readout integration 500 µs.
- Missing counts: devices fabricated, devices measured, devices showing the effect, total cooldowns (at least two), number of tunings tried and kept.

## Matching, skipped and adapted entries
- Family: kitaev (checks kitaev-sweet-spots, kitaev-extend-chain) plus practice checks.
- Matched: false-poor-mans-majorana; fine-tuning-and-selection (always).
- Adapted (scope rule, time-domain qubit data): quasi-majorana-smooth-confinement (the paper itself raises quasi-Majoranas in Methods VIII; the smooth-confinement mechanism does not map onto dots, so I kept the physics of overlapping trivial components; the bulk-gap test cannot apply to a two-site chain and is marked "no" with that clause); local-probe-loophole (no local tunneling probe here; the matching physics is that overlap of Majorana components is not directly measured; the even/odd comparison through the coupler dot is the library's "overlap through a quantum dot in series" test).
- Skipped: abs-quantum-dot, kondo-resonance, disorder-induced-zbp, crowded-trivial-subgap-states, weak-antilocalization, spin-orbit-length-pinning, micromagnet-stray-field, full-shell-flux-andreev (no zero-bias tunneling peak is offered as evidence; dots are intentional and the device is pinched off); exceptional-point-zero-mode (needs coupling to a normal lead; leads are pinched off); fine-tuned-plateau, series-resistance-subtraction (no conductance quantization claim); one-end-only, trivial-andreev-band-gap-reopening (no transport end or nonlocal data offered as evidence); protocol-parameter-sensitivity (the sweet-spot procedure is not an automated pass/fail protocol; its selection aspect is covered under fine-tuning-and-selection); all shapiro, supercurrent, charge, chiral, island, diode entries (different signals).

## Status reasoning notes
- false-poor-mans-majorana: "Microscopic model" marked part. The paper's model (Eq. 5) is a microscopic Kitaev Hamiltonian of the device but in the ideal t, Δ form; Luethi et al. need ABS, spin and interaction physics to produce false PMMs. Unsure whether a stricter reader would mark "no".
- quasi-Majorana: Fig. 4 single-dot versus two-dot detuning taken as an equivalent of the both-ends test, part because readout is total chain parity and single-dot detuning still decays toward 0.5. Note a wording tension the authors may want to look at: p. 8 says single-dot detuning shows "no sizable longitudinal splitting", while p. 9 says it "removes the sweet spot protection and suppresses the oscillations". I did not raise it as a question to stay within eight.
- fine-tuning-and-selection: the tuning acceptance criterion (similar even/odd frequencies and contrast, p. 23) overlaps with the headline signal; raised as question 5.
- Outside row (library gap): conventional charge qubit in the same dots. Source Pan, Das Sarma and Liu 2024 (arXiv 2407.16750, full text checked): their simulated double-dot charge qubit shows Rabi oscillations (T2 ≈ 2.5 ns, Q ≈ 38, Fig. 3 table) and "the system we consider is equivalent to semiconductor charge qubits if all superconductivity is removed". Test taken from that comparison. Marked tested in part since the paper's double-dot configuration is reached at fixed VC and few-ns oscillations may sit near the timing resolution.
- Hold-out: no library source cites this paper. Checked version dates of Akrap et al. (2501.18631, v2 25 Mar 2026) and Luethi et al. (2408.10030, v3 24 Mar 2025); all other used sources predate July 2026. No sources held out.

## Related work checks
- 2408.10030: abstract page opened (v3), ID, title, first author Luethi confirmed; abstract supports the line.
- 2504.06732: arXiv API abstract read (v1), ID, title, first author confirmed; abstract supports the line.
- 2407.16750: abstract page and full text (v2 PDF) read; ID, title, first author Pan confirmed; text supports charge-qubit comparison.
- 2306.16289: arXiv API abstract read; arXiv title differs from the published PRX Quantum title cited in the paper as ref. [6]; first author Tsintzis confirmed.
- 1911.02582: arXiv API abstract read; ID, title, first author Mishmash confirmed.

## Library gaps
- No entry for the conventional charge (double-dot) qubit as a lookalike for parity oscillations in Kitaev-chain qubits.
- The kitaev family has no time-domain tests (even/odd frequency comparison, phase dependence, single-dot versus two-dot detuning); quasi-Majorana and local-probe entries had to be adapted.
- No check on tuning acceptance criteria that coincide with the headline signal.

## Skill issues
- Step 7 says to write reports/<id>.md and notes files; this run returns them in the reply per the caller's instructions.
- For library rows whose test cannot apply to the device (bulk gap in a two-site chain), the skill gives no option beyond "no"; an "n/a" value would be clearer.
- The scope rule says to adapt matching entries but does not say whether adapted entries count toward "the evidence presented" rule or how to phrase test text when an equivalent test is used; I kept library test text and named the equivalent in the cell.
- Page numbering: the skill asks for page numbers but does not say whether to use PDF page or printed page; here they coincide.
