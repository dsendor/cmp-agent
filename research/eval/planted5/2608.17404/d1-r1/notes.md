# Run notes: arXiv 2608.17404v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (28 lookalike entries). Skill and template read once at the start.
- Date: 2026-10-24.

## What I read
- The extracted text of 2608.17404v1 only (main text, Methods, Supplementary Information S1.A to S1.G), as instructed. No PDF, no abstract page, no HTML. The title is taken from the paper text, since no abstract page was available. Figure details come from captions and axis labels in the extraction.
- Zenodo data (10.5281/zenodo.21988906): not accessed, to stay within the test constraints. I did not count devices or ranges from it. There are no ancillary .mtx files, so read_mtx.py was not used.
- Extraction gaps I noticed and did not fill in by inference:
  - the Fig. 4 caption stops after panel k, with no text for panels c, f, i, l;
  - the main-text paragraph on end-to-end correlation stops after "significant overlap in our devices." and its outcome is missing;
  - p. 5 jumps from "...in our TI nano-SQUID architecture." to "This disparity highlights...";
  - SI E has the fragment "peaks upon entering".
  The device C correlation result in the S3l caption is also not described in prose. So I treated the correlation analysis as shown (the panels exist) but could not read its outcome. This affects the "part" marks for end-to-end tests: I marked them "part" because device A has a single probe.
- I did not recognize this paper (it is after my training data). I know the group's earlier nano-SQUID preprint (2412.07993) only in outline and did not use it.

## Claims table (step 1)
| Claim | Figures | Devices | Counts and ranges |
|---|---|---|---|
| Ic oscillations with h/2e period, near-complete revival at integer flux | Fig. 1e, 3a, S2a | A, B, C | A: Bx about ±6 T (Fig. S1 axes); B: about -1 to 4 T; C: about -1 to 4 T. Base temperature about 30 mK. |
| Diode effect, η about 20%, sign reversal at half-integer flux | Fig. 1e, 3a, S2a, S4 | A, B, C (S4: B and C vs VG) | S4: VG about -75 to 25 V, Bx 0 to 4 T. |
| Local spectral jumps at the diode-reversal flux | Fig. 1f-g, 3b-c, S2b-c | A (one TJ), B and C (two TJs) | Bias ±1 mV. A at VG = 10 V; S1 at three more gate voltages. |
| Nonlocal jumps at expected phase boundaries | Fig. 3d-e, S2d-e, S5 | B, C | S5: VG about ±40 V, bias ±1 (units on axis read µV, likely mV; unclear). Measurement-circuit correction per Martinez et al. |
| ZBP appears in the topological window and persists (device A), stable in VG | Fig. 1f-g, S1 | A | VG limited by a leaky gate. S1 panel labels (0, 10, 20 V) disagree with the caption and text (-10, 0, 20 V). |
| ZBPs also in trivial windows and at zero field; VG dependence the same across regimes | Fig. 3b-c, 4a-k, S3 | B, C (C: "zero-bias conductance peak was mostly absent") | Fig. 4: VG ±30 V, bias ±500 µV, Bx = 0, 1, 2 T (B); S3: Bx = 0, 2.5, 4 T (C). |
| End-to-end correlation | Fig. 4c, f, i, l; S3c, f, i, l | B, C | Fraction of gate voltages with correlated peaks, correlated dips or no correlation, vs Bx 0 to 4 T. Threshold not stated. |
- Counts missing: devices fabricated, devices measured ("all examined devices", "a series of devices"), cooldowns, number of datasets, field-angle range, lock-in frequency and excitation. Given: TJ yield below 50%. Device dimensions in Table S1 (A 1.9 µm, B 1.3 µm, C 2.5 µm long; widths 70 to 80 nm; thickness 16 to 36 nm).
- Tunnel resistances are stated as "typically exceeding 100 kΩ", but the shown conductances (up to about 2 e^2/h in Fig. S1) imply lower values. This became a question.

## Matching (step 2)
- Included: diode-vortex-screening, trivial-andreev-band-gap-reopening, abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, spin-orbit-length-pinning (device A peak persists over a large Bx range), exceptional-point-zero-mode, full-shell-flux-andreev (matched on physics: a flux-tuned superconductor around the wire and a dot at the tunnel junction; not a full shell), one-end-only (device A has one probe), local-probe-loophole, fine-tuning-and-selection. Plus one outside row.
- Skipped:
  - fine-tuned-plateau and series-resistance-subtraction: no quantization claim. The zbp-raw-conductance check was still walked.
  - micromagnet-stray-field: no magnets, and the zero-field peaks are not read as topological.
  - protocol-parameter-sensitivity: no pass/fail protocol.
  - field-enhanced-supercurrent-resonances: Ic oscillates and revives but is not claimed to grow above its zero-field value.
  - transparent-junction-pi-crossing: no measured Andreev crossing at phase π is offered as evidence.
  - All shapiro, island, chiral, kitaev and charge entries, and false-poor-mans-majorana: they don't apply to this device.
- Adapted: none in the scope sense. The ZBP checks were applied to the tunnelling data. The diode and nonlocal claims have no family checks in the library.

## Status decisions
- No row is "ruled out": the paper does not conclude against any specific lookalike. For the ZBP rows, the paper itself reports peaks in trivial regimes and leaves their origin ambiguous ("local tunnel spectroscopy is substantially more ambiguous", p. 5). I did not use "left open by the authors", because no sentence names a specific lookalike as possible. The generic "trivial states that obscure them" (p. 5) seemed too unspecific to count.
- Kondo "Zeeman splitting": marked part. Fig. 3b-c show the zero-field peaks evolving with field, with no splitting analysis.
- Quasi-Majorana "gap closing and reopening": marked part. The nonlocal data show jumps at the expected boundaries, not a closing and reopening as such.
- Crowded subgap "subband model": marked part. The Fig. 2 model is an idealized 150 nm long wire.

## Sources held out
- None. No library source cites 2608.17404 as far as the quoted passages and titles show. I did not open every source's full text to confirm this.

## Related work checks
All were checked on the arXiv abstract page (https://arxiv.org/abs/<id>) for ID, title and first author, with the description confirmed against the abstract. 2205.04469 and 2208.10856 were also read via the export API.
- 2208.10856 Fominov and Mikhailov: abstract. Asymmetry vanishes at integer or half-integer flux. This is the source for the outside row.
- 2306.12765 Greco, Pichard and Giazotto: abstract. About 20% efficiency in an Al dc-SQUID.
- 2205.09276 Hou et al.: abstract.
- 2210.03507 Hess et al.: abstract (also a library source).
- 2008.02348 Valentini et al.: abstract (also a library source).
- Also opened but not listed: 2205.04469 (Souto, Leijnse, Schrade, interferometer diodes with non-sinusoidal CPRs).

## Library gaps
- No entry for a trivial SQUID or interferometer diode with higher harmonics, where flux-periodic η with zeros at integer and half-integer flux mimics the "sign reversal at half-integer flux" signature. Sources: 2208.10856, 2306.12765, 2205.04469.
- No checks section for the diode or nonlocal families.
- Possible entry, not included because I opened no source for it: vortex entry and flux trapping in the Nb leads producing spectral jumps at high field. The paper raises this itself (p. 4).

## Unsure
- The S5 bias axis units (µV in the extraction vs mV elsewhere).
- Whether device A's conductance scale is purely tunnelling.
- The outcome of the end-to-end correlation analysis (text missing in the extraction).

## Skill issues
- Step 3 says to walk "the checks for the paper's family". This paper's main claim is diode plus nonlocal, which have no checks, while its ZBP data fall under zbp checks. The skill doesn't say what to do when the main claim's family has no checks.
- The status rules assume the paper offers the signal as evidence. Here the paper offers ZBPs in device A as consistent with theory, yet reports ZBPs in trivial regimes in device B. It's unclear how to set "ruled out" or "left open" when the authors themselves disclaim the signal.
- "Left open by the authors" needs a sentence saying "this explanation is possible". It's unclear whether a generic sentence about trivial states counts.
- The template's one-quote, one-clause cell rule clashes with the "Tests shown" column for entries with three tests.
- Step 7 says to write reports/<id>.md. This run followed the prompt's output instructions.
