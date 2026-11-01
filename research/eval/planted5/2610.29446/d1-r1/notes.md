# Run notes: arXiv 2610.29446v1

- Library version: 0.5 (meta.version, updated 2026-10-24), 28 lookalike entries.
- Date of run: 2026-10-24.

## What I read

- skill/SKILL.md, skill/report-template.md, library/lookalikes.yaml (all entries, tests and the checks section).
- The paper: the extracted text only (main text pp. 1 to 4, supplement pp. S1 to S8, references), as the task instructed. I did not open the abstract page, PDF or HTML. The title comes from the paper text, so I could not check it against the arXiv abstract page as the skill asks.
- Figures: details from captions and main text only. I could not see the images, so the bias ranges, color scales and line cuts of Figs. 2, 4, S1, S3, S4 and S5 are unknown to me.
- No figure data or ancillary files were given; read_mtx.py was not used. No data repository is linked in the text, so I counted nothing beyond the text.
- Page numbers come from page markers in the extracted text. Subscript spacing in quotes is normalized ("Cr4 ," in the extraction written "Cr4,").

## Claims table (step 1)

| Claimed signal | Figures | Chains | Counts and ranges | Missing |
|---|---|---|---|---|
| Length-driven closing and reopening of the in-gap spectrum | Fig. 2(a) data, Fig. 2(b) calculation | One "representative" chain each of Cr4, Cr5, Cr8, Cr12 (Fig. 1(c-f)) | Lengths 4, 5, 8, 12; T = 30 mK; lock-in 30 µV at 330 Hz; imaging V = 3 mV, I = 50 pA | Chains built per length, other lengths, bias range and setpoint of the maps, cooldowns, number of tips |
| Zero-bias modes at both ends of Cr12 | Fig. 2(a), Fig. 4(b), Fig. S1(a,c) | Cr12 (apparently one chain) | Zero-bias profile along the chain; clear end imbalance | Second Cr12 chain; field series; temperature series |
| Reopened gap Δtopo = 204 ± 50 µeV | Fig. S3 (raw and subtracted chain-center curve) | Cr12 | Subtraction of clean-surface dI/dV | How the ±50 µeV is set; calculated gaps are 84 and 146 µeV (Sec. S7) |
| End asymmetry from a 6% variation of J | Fig. 4(c,d), Fig. S1(d,e) | Calculation | J from 2.5 eV to 2.35 eV over half the chain | Whether the variation was fitted to the data |
| Electron-hole exchange and spin texture | Fig. 3, Fig. S2 | Calculation only | αR given as 1.8 eV·Å (S2) and 3.6 eV·Å (S4) | No spin-polarized measurement |
| ξM ≃ 10.5 Å, about three sites | Eq. (1), Sec. S5 | Calculated splitting 16.8 µeV at ΓD = 5 µeV | L = 57 Å, kF = 0.18 a0^-1, cos(kF L) set to 1 | Experimental splitting; my arithmetic gives 9.5 µeV at 10.5 Å, and 11.1 Å for 16.8 µeV |
| RF response consistent with compact end modes | Fig. S4, Fig. S5 | Cr12 (written "Cr*12"), third and sixth atoms | 44 GHz; VRF up to 0.22 mV in Fig. S5; larger in Fig. S4 | Whether this is the same chain as Fig. 4 |

## Scope and adaptation

The paper is STM spectroscopy of chains assembled atom by atom, not transport, so I adapted entries and said so in "What this is". Adapted: abs-quantum-dot (trivial Andreev or YSR state at a chain end), quasi-majorana-smooth-confinement, disorder-induced-zbp (strain or coupling inhomogeneity), kondo-resonance (end adatom), trivial-andreev-band-gap-reopening (length series in place of field), one-end-only and local-probe-loophole (two chain ends), and the zbp checks (tip height in place of barrier transparency; chain-center gap versus length in place of nonlocal gap).

## Entries skipped and why

- weak-antilocalization: multichannel disordered nanowire physics; no conductance peak of order e^2/h claimed.
- fine-tuned-plateau, series-resistance-subtraction: no quantized conductance is claimed. The background subtraction for Δtopo is covered under the processing checks.
- crowded-trivial-subgap-states: considered, since β-Bi2Pd is multiband (ref. 32), but the entry is about how common peaks are across many devices, and the paper has no multi-device statistics to judge it against; noted as unsure.
- micromagnet-stray-field, full-shell-flux-andreev, chiral-plateau-superconductor-short, island-states-coulomb-spacing, all shapiro, supercurrent, charge and diode entries, coulomb-dominated-interferometer: different device or signal.
- spin-orbit-length-pinning: about pinning against field; the paper has no field data.
- exceptional-point-zero-mode: needs strong coupling to a normal lead; the STM tip is weakly coupled and the chain sits on a superconductor.
- false-poor-mans-majorana: quantum dot Kitaev chains at sweet spots; not this system, although its "extend the chain" test is close to my outside row.
- protocol-parameter-sensitivity: no automated protocol.

## Sources held out

None. No library source cites this paper; all predate it.

## Related work: how each was checked

All five: found with the export.arxiv.org API, abstract read through the API (id_list), then the arxiv.org/abs page opened to confirm the title and first author. Checked against the abstract only, not the full text.
- 2104.11503, Schneider (first author), title confirmed; abstract: "We find periodic lengths where their interaction is tuned to zero within the experimental energy resolution."
- 2211.00561, Schneider, confirmed; abstract describes the one-end defect test.
- 2112.05708, Küster, confirmed; abstract: end modes "identified as topologically trivial Shiba states".
- 2204.02324, Hess, confirmed; abstract: zero-energy bound states "far less prevalent" than in nanowires.
- 1412.0151, Peng, confirmed; abstract: velocity renormalization and strong localization.

## Library gaps

- Oscillating end-mode splitting with length (source 2104.11503): a single length near a zero of the oscillation looks like suppressed hybridization. Tests: end-mode energy over consecutive lengths at both ends; splitting measured or bounded within resolution.
- Trivial end states in a trivial minigap of magnetic chains, with the one-end defect test (source 2211.00561).
- No checks family for STM on spin chains or adatom systems (tip height, superconducting tip resolution, spin-polarized tip, chain-length series, defect at one end).
- No entry for background subtraction of a reference spectrum (the Δtopo extraction).

## Things I was unsure of

- Whether "Cr*12" (main text p. 4) marks a different chain or is an extraction artifact; this decided the "part" on the second-dataset test.
- Cross-references that look off: Sec. S6 cites "Fig. 3" for the edge asymmetry (Fig. 4 or S1 seems meant); Sec. S8 cites "the microwave study of Fig. 4" (Fig. S5 seems meant); Fig. S4 caption says "see Suppl. Information for details" from inside the supplement. L = 12 × 4.75 Å counts 12 spacings for 12 atoms (11 spacings give 52.25 Å). I left these out of the report except where they feed a question.
- Equation (1) arithmetic: with ħ²/m for the free electron and a0 as the Bohr radius I get 9.5 µeV at ξM = 10.5 Å; the paper may use another mass or kF. Phrased as a question.
- cos(kF L) is about 0.86 at 57 Å and about 0.47 at 52.25 Å by my numbers, so "≃ 1" depends on the length used.
- Whether the closing and reopening counts as "done" for check 5: I marked it partly because the closing is inferred from a single feature shift in the data shown, not because of lengths not shown.
- I did not recognize this paper and used no knowledge of its later history.

## Skill issues

- The skill says to use the title on the arXiv abstract page; this run gave text only. I used the title in the text.
- flags.json needs the library test text verbatim, but adapted entries test something different (for example "Dot signatures searched" read as end-state tracking for a chain). The adapted meaning appears only in the report.
- The rule that gaps about data not shown count only under fine-tuning-and-selection clashes with checks that are about range by nature (zbp-wide-ranges). I marked it partly on the parameters missing outright (field, temperature), and left the unshown lengths to fine-tuning.
- The skill does not say whether calculations count as "the paper shows the analysis". I counted a calculation only for the test that asks for a model (trivial-andreev-band, part), and did not count the calculated splitting as a measured overlap.
- Unclear whether an outside row may overlap an adapted library row (trivial end states). I kept both because the outside source gives a different, spin-chain-specific test.
- No checks family fits STM spin chains, so I walked the zbp checks adapted.
