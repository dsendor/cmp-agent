# Run notes: 2609.01233v1, run v5-r2

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (28 lookalikes). I read the skill, the template and the library once at the start.
- Paper read: local abstract page (abs.html), extracted text (paper.txt, the full main text, Methods, Extended Data and Supplementary Notes 1 to 9), and PDF pages 2, 4, 5, 10 and 11 rendered as images to read Figs. 1, 2, 3, ED1 to ED4 and their FFT insets. I did not fetch the paper online. No ancillary files or data repository exist ("available from the corresponding author upon reasonable request"), so read_mtx.py wasn't used.
- Recognition: I did not recognize the paper and used no knowledge of its later history.

## Claims table (step 1)

| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| P-n interface MZIs detect channel spin (integer calibration) | Fig. 1e,f; ED1; ED2 | one device, 700 nm arm, 70 nm gate slit | (−2,1): B 8.00 to 8.20 T, Vright 1.095 to 1.135 V; (−2,2): B 8.05 to 8.25 T, Vright 1.66 to 1.75 V; (−1,1): B 10.4 to 10.6 T, Vleft −1.0 to −1.3 V |
| Spin transition of the 2/3 channel near 9.5 T | Fig. 2a,b | same | Landau fan B 6 to 13 T, Vright about 0.1 to 0.9 V; Fig. 2b B 8 to 11 T, Vright − αB 0.20 to 0.33 V; raw T and R at one gate value |
| Polarized 2/3 near 11 T | Fig. 2d; ED3; ED4b | same | (−2,2/3): B 11.00 to 11.10 T, Vleft −2.27 to −2.23 V; (−1,2/3): B 11.00 to 11.10 T, Vleft −1.10 to −1.30 V |
| Unpolarized 2/3 below 9.5 T, fnm combination frequencies, f11 two-electron term | Fig. 2c; Fig. 3a to c | same | Fig. 3a: B 8.35 to 8.45 T, VSi 31 to 32 V; Fig. 3b: B 8.35 to 8.60 T, Vleft about −2.115 to −2.065 V; Fig. 2c: B 7.70 to 8.80 T, Vleft −2.36 to −2.18 V (no FFT) |
| Spin-charge separation from thermal and bias decay | Fig. 3d,e; ED4; Fig. S3 | same | T 0.1 to 1.0 K in 0.1 K steps; Vdc about −1.3 to 1.3 mV; fit excludes the three lowest temperatures |

Missing counts: devices fabricated ("The devices", plural, SN1), devices measured, devices showing the effect, cooldowns, number of datasets. Base temperature about 10 mK, field up to 14 T (SN3).

## Entries matched, skipped and adapted

- Scope: the paper is a quantum Hall Mach-Zehnder measurement of edge spin structure, outside the Majorana-centred core of the library. Adapted entries: coulomb-dominated-interferometer (written for Fabry-Perot interferometers; applied to the B and gate maps of the MZI) and the charge-family checks charge-regime-map, charge-control-regime and charge-repeat-sweeps (read as: control regimes where the unpolarized signature should be absent). Practice checks used as written.
- Included: fine-tuning-and-selection (always), coulomb-dominated-interferometer (adapted).
- Skipped: charge-trap-fractional-shift (the paper claims no fractional shift or fractional period; "the AB period is set by the electron charge", p. 3); protocol-parameter-sensitivity (no automated pass/fail protocol); local-probe-loophole and every zbp, quantization, nonlocal, island, shapiro, supercurrent, chiral, kitaev and diode entry (no superconductor, no zero-bias peak, no Josephson junction).
- Outside rows (library gaps): (1) single-particle multi-path loops, source Song and Myoung 2025, arXiv 2508.07380 (abstract and full text; p. 9 quote: "although a higher-order loop enclosing area AnMZ + ApMZ can generate secondary harmonics of the MZ interference, its Fourier-peak amplitude remains negligible compared to the primary modes"). (2) valley-isospin selection at the beam splitters, source Trifunovic and Brouwer 2019, arXiv 1902.07975 (abstract: "the evolution of edge states into interface states and vice versa is governed by the conservation of valley isospin"), with Jo et al. 2021 (arXiv 2011.04958, abstract) for beam-splitter transmission tunable from zero to near unity. Tests for these rows come from the controls those papers describe.

## Judgments worth a second look

- Coulomb-dominated test "Regime and charging parameters reported" marked part: the paper names the AB regime and supports it with the integer area argument, but gives no charging estimate.
- Multi-path test "two-loop configuration checked for a summed-area peak" marked all: the Fig. 1f inset shows two labelled peaks only, (0.2, 2.7) and (0.1, 39.2), and the text says the total is TMZI,1 + TMZI,2. This is an integer geometry without the shared fractional arm, which is why the second test stays no.
- Valley test "valley pairing held fixed" marked part: ED1a labels the (−2,1) pair |K',↓> and |K,↓> (coupled), ED2a labels the (−1,1) pair |K',↑> and |K,↓> (blocked), so valley pairing is the same and spin differs in the integer calibration. No valley assignment is given for the 2/3 channel.
- FFT resolution in question 5: Φ0 × (1 / 0.25 T) = 4.14e-15 T m² × 4 T⁻¹ ≈ 0.017 µm²; Fig. 3c areas 0.082 and 0.087 µm². Gate frequencies (72.8 and 21.2 V⁻¹) are well separated for a 50 mV window (about 20 V⁻¹ resolution).
- Status of fine-tuning-and-selection quoted from the Fig. 2c caption; the paper doesn't discuss selection.

## Hold-out rule

Matched library sources: Halperin et al. 2011 (1010.4598; abstract page opened, predates the paper), Frolov et al. 2023 v1 (predates), Akrap, Frolov et al. 2026 v2 (2501.18631v2; full text grepped for "Ayache", "Roulleau", "2609.01233", "spin-singlet": no hits). No source held out.

## Related work, how each was checked

- 1307.4408 Amet et al.: abstract page opened; ID, title, first author and description confirmed from the abstract.
- 1703.00110 Wei et al.: abstract page opened; confirmed from the abstract.
- 2011.04958 Jo et al.: abstract page opened; confirmed from the abstract.
- 1902.07975 Trifunovic and Brouwer: abstract page opened; confirmed from the abstract.
- 2508.07380 Song and Myoung: abstract page opened and full text read (pp. 3 to 10).
- Also opened and not listed: 1808.05898 Lafont et al. (abstract; kept to five).
- arXiv API used with 3 s waits; no rate-limit errors.

## Skill issues

- The scope rule says to adapt entries for "a different kind of measurement"; it doesn't say how to treat a paper whose claim isn't a topological lookalike signature at all (here edge spin structure). I adapted the charge family and practice checks; a family for quantum Hall edge interferometry (MZI multi-path, valley and spin selection, Coulomb coupling) would help.
- The charge-family checks assume a fractional charge or statistics claim; "show the effect is absent where the exotic state is not expected" needed reinterpretation as control configurations.
- Step 6 fixes four general questions and a cap of eight, which left room for only four paper-specific ones; I dropped a Coulomb-charging question and kept it in the table's suggested check.
- The template has no slot for the paper's full title and authors; I added a "Paper." line after the header.
- Output files: the prompt asked for report and notes in the reply; the skill's step 7 asks for files under reports/. I followed the prompt.
