# Run notes: 2610.18817v1

- Library version: 0.5 (meta.updated 2026-10-24), 28 lookalike entries.
- Date of run: 2026-10-24. Label: AI only.

## What I read
- The arXiv abstract page (local copy abs.html) gave the title, 13 authors, the date 2026-10-13 and the abstract. It has no ancillary files and no data link.
- I read the full extracted text (paper.txt, 24 pages): main text, Methods, Tables I–III and Extended Data Figs. 1–11. I rendered PDF pages 2 and 7 as images to check the Fig. 1 and Fig. 4 captions.
  - The text extraction garbled the Fig. 1 caption to "EC = 3e ∆VDC". The PDF reads EC = (e/3)∆VDC ≈ 300 µeV.
- I did not fetch the paper itself. One arXiv API search for related work listed 2610.18817v1 among its results; I did not open it.
- Data repository: none linked, so I counted devices and ranges from the text and Table I only.
- I did not recognize the paper. It is dated after my training data.

## Claims table (step 1)
| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| Integer dot: Coulomb blockade at ν = 1 with e∆VDC ≈ 2 meV; dot sits in the QPC saddle point | Fig. 1f–g, Ext. Data Fig. 2 | one device, 90 nm hole | B = 5 T; Vdot −2.5 to −0.5 V; gate maps over Vqpc, Vedge, VT, VB |
| Spin blockade of quasielectrons, magnon-assisted lifting above EZ; Nqp assigned by counting; DMRG comparison | Fig. 2 | same | Vdot about −3 to 4 V; VDC to ±2.3 mV; B = 5 T |
| Charge noise and stability | Ext. Data Fig. 5, Table III | same | 3 transitions; 15.5 h trace; 10^-4 to 10^-2 Hz |
| e/3 resonances: δ ≈ 80–100 mV at 1/3 and 2/3 vs 250–300 mV at ν = 1 | Fig. 1h–j | same | datasets at 5, 8.97, 13.4, 13.5 T (Table I); 2/3 at 8.97 T is lock-in (first cooldown), 1/3 at 13.5 T is DC (second cooldown) |
| Chiral Luttinger liquid leads | Ext. Data Fig. 3 | same | 25–500 mK; Te saturates near 110 mK |
| Nqp = 0 calibrated by tripling B from ν = 1 at 4.5 T to 1/3 at 13.5 T; single-anyon regime; irregular addition for Nqp = 1–5 matching DMRG | Fig. 3, Ext. Data Figs. 6–8 | same | Vdot −1.03 to 3.97 V; VDC ±1.5 mV; few-quasihole regime not reached ("We were unsuccessful in accessing the few quasihole regime in weak backscattering", p. 5) |
| Regular spectra for 1/3 QH and 2/3 QP, irregular for 1/3 QP and 2/3 QH at |Nqp| ≈ 10–20 | Fig. 4a–d, Ext. Data Figs. 9–11 | same | sweeps over VT, Vedge, Vqpc, D; 13.5 T only |
| Anyon binding: alternate sectors vanish as VT is lowered, giving 2e/3 steps | Fig. 4e–g | same | VT 0.040–0.050 V; Vdot 3.785–4.5 V; VDC 55 µV for the map; 13.5 T; DC (second cooldown) |

Missing counts:
- Devices fabricated is not given; the text says "M.V. fabricated the devices".
- Datasets showing the 2e/3 regime: only Fig. 4f–g, plus a mention in Ext. Data Fig. 7b.
- Field range for the binding: 13.5 T only.
- No temperature series in the binding regime.

## Entries matched, skipped and adapted
- Matched:
  - charge-trap-fractional-shift. Adapted: its signature is fractional shifts, and I applied it to the even-odd pattern and the missing sectors as well, on the physics of a capacitively coupled side dot.
  - fine-tuning-and-selection (always).
- Checks walked: the charge family (charge-regime-map, charge-control-regime, charge-repeat-sweeps) and the practice family (report-counts, report-ranges, report-processing).
- Skipped:
  - coulomb-dominated-interferometer: the device is a Coulomb-blockaded dot, not a Fabry-Perot interferometer read as AB interference. Coulomb charging is the paper's own model, so this entry offers no alternative to the claim.
  - island-states-coulomb-spacing: its signature and its only test (open the junctions and look for a zero-bias peak) are Majorana-specific. The ordinary alternative it points at, orbital level structure giving even-odd spacings, is addressed by the authors with DMRG and their missing-sector criterion. Recorded as a gap below.
  - protocol-parameter-sensitivity: no automated pass/fail protocol.
  - local-probe-loophole: about Majorana separation.
  - All zbp, quantization, nonlocal, shapiro, supercurrent, chiral, kitaev and diode entries: the device has no superconductor, and the signatures do not match.

## Sources held out
- None. The sources used by the matched entries are arXiv 2309.09368v1 (2023), 2101.11456 (2021) and 2501.18631 (v2, 2026).
- I checked the first by text search and found no mention of this paper.
- The other two predate or cannot cite a paper posted 2026-10-13; I judged this by date and did not open them.

## Related work, how checked
- 2005.12723 Röösli et al.: abstract page opened; ID, title, first author and the e*/e = 0.32 claim confirmed from the abstract.
- 1201.1600 Kou et al.: abstract page opened; confirmed from the abstract.
- 1409.4427 Choi et al.: abstract page opened; confirmed from the abstract.
- cond-mat/0109104 Huettel et al.: abstract page opened; confirmed from the abstract.
- 2309.09368 Frolov et al.: abstract page opened and the full v1 text read for Example 4 (side dot, 1/3 period jumps).
- 1608.05721 Hamo et al.: abstract opened, not listed (limit of five).

## Library gaps
- Blockaded charge transition: a transition that occurs but is invisible in transport (spin or orbital blockade), which can mimic a missing charge sector. Source: Huettel et al., cond-mat/0109104, with tests from its bias, field and temperature dependence. Added as an outside row.
- Orbital shell structure, or near-degenerate orbitals, giving even-odd spacings or sectors below resolution in non-superconducting dots. The library has this only in its Majorana island form.
- Lever-arm or capacitance changes between fillings as an alternative reading of a fractional gate period. I found no source I could open in time, so I raised it as a question only (Q7).
- Apparent pairing from coupling to an adjacent edge channel (Choi et al.). The authors raise the 2/3–1/3 edge possibility themselves, so I listed it as related work, not as a row.

## Unsure
- For the charge-trap test "Shifts absent where the exotic state is not expected" I marked all. The ν = 1 spacing (Fig. 1j) and the regular 1/3 quasihole spectra (Fig. 4a) are shown, but at other gate voltages from the irregular window, so a trap active only near Vdot 3.4–4.4 V is not excluded by that test alone.
- For "How the shown data were chosen" I counted the Fig. 4e sentence as part, because the skill says a sentence alone does not count for tests, while this test is about disclosure.
- Cooldown assignment comes from the Table I frequency column (DC = second cooldown, per Methods). Methods quote 13.333 and 17.777 Hz while Table I lists 13.77 and 17.77 Hz.

## Skill issues
- The skill says to write reports/<id>.md and .notes.md. This run's prompt said to return them inline, so I followed the prompt.
- The charge-family checks and the charge-trap entry are phrased for fractional shifts. It is unclear how far matching "on the physics" should reach for fractional periods and missing sectors.
- Outside rows: "take its tests from the control that paper describes". Huettel et al. describe diagnostics, not a control, so I used those.
- The hold-out rule can only be checked by opening every source; the skill does not say whether a date check is enough.
- "What this is" uses the full library count (28), although most entries cannot apply to this paper.
