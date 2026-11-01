# Run notes: arXiv 2607.11721v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (updated 2026-10-24), 28 lookalike entries.
- Skill files read: skill/SKILL.md, skill/report-template.md, the library. read_mtx.py was not used because there are no .mtx or other figure data.
- Date of run: 2026-10-24.

## What I read

- The paper: the extracted text only (main text pp. 1-16 and Supplementary Information pp. 17-51), as the task instructed. I had no PDF and no abstract page, and I did not fetch the paper in any form. The title comes from the first line of the extracted text. Figure details come from the captions and the main and SI text only; I could not look at the plots themselves.
- Data repository: none. The paper says data are "available from the corresponding author upon reasonable request" (p. 16), so I counted nothing beyond the text.
- I did not recognize the paper and know nothing of its later history.

## Claims table (step 1)

| Claim | Figures | Devices | Counts and ranges |
|---|---|---|---|
| Ballistic, phase-coherent Josephson effect across the main Dirac band and the minibands | Fig. 1c-e, 1g; S5-S9, S12 | GH1 (main); GH2 (S12) | Ic(n) at 2 K; RN at 10 K; FP in Ic in minibands for GH1 and GH2, none in GH3/GH4. Gate up to ±80 V (maps use ±70 V); n/ns up to ∼±2.7 for low twist angles |
| Long-ballistic regime | Fig. S8 | GH1-GH4 | Ic(T) exponential fits; δE ∝ 1/L across 4 lengths (0.2, 0.3, 0.5, 0.6 µm); vF ≈ 0.34e6 m/s at n/ns ∼ 1.3 (FP gives 0.5e6) |
| Zero-resistance pockets with oscillating Ic up to ∼6 T in the minibands, past 2rc = L | Fig. 2a-c, 2e; S10, S11, S13 | GH1 (to ∼6 T), GH2 (to ∼5 T) | 100 mK only; perpendicular field only; magnet limit 8 T (Fig. S1c). Cuts: Fig. 2b n/ns ∼ 1.8 at several B (2.5 T trace, Ic ∼ 48 ± 2 nA); Fig. 2c n/ns ∼ 1.8 around 4.3 T; Fig. 2e B = 4.1 T; S11 at 2.5, 3.5, 4.5 T (two consecutive sweeps each); GH2 S13b n/ns = 1.6, S13c around 3.5 T. High-field periods 2.3 to 3.4 mT (GH1), 1.7 to 2.0 mT (GH2) |
| Not quantum Hall (chiral) supercurrent | Fig. S14 | GH1, GH2 | Normal-state fan at 200 nA dc bias; Ic magnitude argument for GH1 |
| Plain graphene stays below 2rc = L | Fig. S15 | one non-moiré junction, L ∼ 300 nm | same density range |
| Pockets coincide with large ⟨v²⟩/vF² from Hofstadter calculations | Fig. 3c-e; S18-S21 | GH1, GH2 (θ = 0.2°, 0.38°) | p/q from 1/3 to 1/20 (205 fields); colourbar limits "imposed by the Thouless energy"; S18 1/R cutoff 20 mS; threshold quoted as ∼0.17 (p. 7) and as 0.1 (p. 7) |

Counts that are missing: cooldowns per device, number of datasets or interference patterns taken at high field, how many chips or stacks the four junctions came from, and whether any other junctions were measured. Main text p. 3 says "multiple additional devices", while the SI shows high-field pockets in GH2 only. The paper names four devices fabricated and measured, two that showed the high-field effect, and one non-moiré control junction.

Measurement: two-probe ("semi 4-probe") with a 3447 Ω series resistance subtracted; 1 nA ac excitation at 17.777 Hz; dc current step 2 nA; Ic is defined at 50% of RN; field swept at ∼0.2 mT/s with three back-and-forth sweeps before each interference pattern.

## Entries matched, adapted, skipped

- Matched and adapted (this is a non-topological high-field Josephson measurement, so I adapted signatures by physics):
  - fine-tuning-and-selection: applies to every paper.
  - series-resistance-subtraction: adapted from "conductance near 2e^2/h" to "resistance reads zero after a subtracted series resistance" in a two-probe map (Fig. 2a, Fig. 3e 1/R).
  - field-enhanced-supercurrent-resonances: adapted from "supercurrent grows with field, read as triplet" to "supercurrent pockets survive at high field, read as Hofstadter-band transport". The lookalike is finite-bias resonances or switching dynamics producing low-dV/dI pockets.
- Skipped:
  - All zbp, nonlocal, island, kitaev and quantization entries other than series-resistance (abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, fine-tuned-plateau, one-end-only, trivial-andreev-band-gap-reopening, micromagnet-stray-field, full-shell-flux-andreev, spin-orbit-length-pinning, exceptional-point-zero-mode, local-probe-loophole, island-states-coulomb-spacing, false-poor-mans-majorana): there is no tunneling spectroscopy, zero-bias peak, nanowire, island or dot chain.
  - Shapiro entries (shapiro-landau-zener, shapiro-nonlinear-resistance, switching-jump-blind-region, transparent-junction-pi-crossing): there is no microwave irradiation.
  - charge-trap-fractional-shift, coulomb-dominated-interferometer: no fractional-charge claim. The Ic oscillations are Josephson interference, not a quantum Hall Fabry-Perot interferometer.
  - chiral-plateau-superconductor-short: no half-quantized plateau and no QAH film.
  - diode-vortex-screening: no nonreciprocity claim.
  - protocol-parameter-sensitivity: there is no automated pass/fail protocol. The data-window concern it raises (colour limits, 20 mS cutoff, 0.1 versus 0.17 threshold) became question 8.
- Checks: the library's `checks` section has no `supercurrent` family, so only the three `practice` checks applied.

## Sources held out

None. No library source discusses this paper as far as I can tell. All library sources predate July 2026 except the 2026 v2 revisions of arXiv 2502.19560 (TGP comment) and 2501.18631 (reproducibility report), whose topics don't touch graphene Josephson junctions. I did not open library sources to confirm this, since none was needed for related work.

## Related work: how each was checked

- 1504.03286 (Ben Shalom et al.): ID, title and first author confirmed via the arXiv API; abstract read; full text (v2 PDF) read for the near-edge mechanism, the 2rc = L cutoff and the Fraunhofer-envelope test (Supplementary Sections 7-9). This is also the source for the outside row "near-edge Andreev states".
- 1512.09083 (Amet et al.): ID, title and first author confirmed via the API; abstract read; full text (v1 PDF) searched for the dc-bias plateau check (IDC = 3 nA and 6 nA) and the regular period. This is the source for the outside row "chiral Andreev edge states".
- 1801.01447 (Draelos et al.): API, abstract only.
- 1805.10184 (Indolese et al.): API, abstract only.
- 2402.14451 (Barrier et al.): API, abstract only.
- arXiv API calls were spaced about 3 s apart; none were rate-limited.

## Library gaps

- No `checks` steps for the `supercurrent` family. A check list for high-field or unusual supercurrent would help: normal-state quantum Hall check, current distribution at the field of interest, and a full-bias dV/dI.
- No entry for chiral Andreev edge-state supercurrent in the quantum Hall regime (Amet et al. 2016, arXiv 1512.09083) as a lookalike for high-field supercurrent.
- No entry for near-edge or edge-carried supercurrent in graphene junctions (Ben Shalom et al. 2016, arXiv 1504.03286; Indolese et al. 2018, arXiv 1805.10184), with the Fraunhofer-envelope (Dynes-Fulton) test.
- series-resistance-subtraction is written only for conductance near 2e^2/h. A zero-resistance reading in two-probe maps after subtraction is the same mechanism and could be named in the signature.
- Possibly missing: flux creep or trapped vortices changing high-field interference patterns. The paper addresses this itself (Fig. S11), but I had no opened source, so I did not add a row.

## Things I was unsure of

- series-resistance-subtraction, first test: the value (3447 Ω) is stated, but no calibration is shown. Under "a sentence alone doesn't count" I marked it "no", which made the status "Not tested (data bear on it)". A reader who counts the stated value as part of the test would mark "part" and "Tested in part".
- Chiral edge-state row: I set "Ruled out for the claim" using the one-test rule (Fig. S14 in both devices). The bias used, 200 nA, is far above the 3 to 6 nA Amet et al. used, and at a few kΩ it is of order 1 mV, which could smear small Hofstadter gaps. That is why the suggested check mentions a lower bias. "Tested in part" is the defensible alternative.
- Near-edge row: the paper doesn't argue against edges explicitly, but the 2rc = L comparison bears on it. I marked it "Tested in part" because one test is shown.
- Internal inconsistencies I noticed. These are not used for statuses; I asked about the ones tied to evidence:
  - p. 3 says "multiple additional devices", but the SI shows one additional device with the effect.
  - p. 6 has a garbled sentence: "ranging from ETh ∼ 2.6 meV at the main Dirac band, to ETh ∼ 1.6 meV at the moiré minibands is ETh ∼ 2.6 meV".
  - p. 7 gives a ⟨v²⟩/vF² threshold of ∼0.17 and then uses 0.1.
  - vF is 0.34e6 m/s from Ic(T) and 0.5e6 m/s from Fabry-Pérot.
  - SI p. 20 writes "6.0 × 10−12 cm-2", a sign typo in the exponent.
- Figure-level judgments (for example whether Fig. 2a covers the hole-side minibands at high field) rest on captions and text only.

## Skill issues

- SKILL.md says to read the arXiv abstract page and PDF, and to take the report title from the abstract page. In this test neither was allowed, so the title comes from the text. The skill has no fallback for text-only input.
- The `checks` section has no entry for the `supercurrent` family, yet that family exists in meta.families. The skill doesn't say what to do when a family has no checks; I ran only the practice checks.
- It is unclear whether a stated numerical value (here the series resistance) counts as "shown" for a test phrased "calibrated independently, with its value". The skill's "a sentence alone doesn't count" pushes to "no", but the test text partly matches.
- For the "Ruled out for the claim" one-test route, the skill says to "say in one clause why it is enough" but not where in the table. I put it in the suggested-check cell.
- The scope rule says to adapt entries for a different kind of measurement. It doesn't say whether adapted signatures may cross families (I used `quantization` and `supercurrent` entries for a zero-resistance claim).
- Step 7 says to write reports/<id>.md and the notes file. This environment refuses .md writes from subagents, so both are returned inline, as the task asked.
- The template's checks line format "<check> : Done / Partly / Not done" uses a space before the colon. I kept it as written.
