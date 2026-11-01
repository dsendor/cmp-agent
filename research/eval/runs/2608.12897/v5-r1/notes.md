# Run notes: arXiv 2608.12897v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (28 lookalike entries). Skill and template read once at the start.
- Date: 2026-10-24. Version assessed: v1 (the only version; submitted 13 Aug 2026).

## What I read
- arXiv abstract page (local copy abs.html): title, 10 authors (first author Tomer Alkalay), "15 pages, 3 figures". No ancillary files listed.
- Full text (local paper.txt, 41 PDF pages): main text pp. 1-12, references pp. 13-15, Supplementary Notes 1-3 pp. 16-39, supplementary references pp. 39-41.
- PDF pages rendered and looked at as images: p. 3 (Fig. 1), p. 4 (Fig. 2), p. 6 (Fig. 3), pp. 18-21 (Figs. S1-S4), p. 39 (Fig. S9).
- Data repository: none linked. "Source data are provided with this paper" (p. 13), but nothing is attached on arXiv, so I counted no data files and could not run read_mtx.py.
- Couldn't open: nothing I needed.

## Claims table (step 1)
| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| e* = e/4 from partition noise at the injection QPC | Fig. 1b; Figs. S1-S4 (b, f) | Fig. 1b: device C, data set 4 | Fit to Eq. (1) at T = 10 mK; bias about -5 to 5 in e*V_S/2k_BT |
| Charge Fano factor above 1, matching PH-Pf (time-domain braiding of Abelian charged anyons) | Fig. 2b; Figs. S1-S4 (c, d) | Fig. 2b: device C, data set 4 | F_charge = 1.54 measured at e*V_S/2k_BT = 4.6 vs 1.49 (PH-Pf), 0.94 (A-Pf) (p. 12); R_QPC about 0.1-0.27 |
| Neutral Fano factor matching M_n = 0 (non-Abelian Ising braiding), closer to PH-Pf | Fig. 3b; Figs. S1-S4 (g, h) | Fig. 3b: device C, data set 3 | F_neutral = 2.37 at 5.0 vs 2.33 (PH-Pf), 2.0 (A-Pf) (p. 12) |
| Incoherent heating ruled out | Fig. S9 (Supp. Note 3) | data set 4 only | Model underestimates by about 2x |

Counts: devices fabricated, not stated. Devices measured: 3 (A, B, C; QPC gaps 1.2 µm x2, 1.3 µm x1; QPC separation 1.4 µm in all; p. 8). Devices that showed the effect: 3 (p. 7, p. 17). Cooldowns: 4 (each device once with no gate voltage; device C again with +0.3 V applied during cooldown). Data sets: 4, each in both configurations. Electron temperature: 10 mK only. Noise detection: 720 and 690 kHz. Density 3.16e11 cm^-2. Missing: magnetic field and its position in the plateau, QPC gate voltages and how many settings were tried, any temperature series, error bars or uncertainty estimates.

## Entries matched, skipped, adapted
- Scope: this is a shot-noise / time-domain braiding experiment on quantum Hall edges, a kind of measurement the library has no family for. The nearest family is `charge`. I said so in one sentence under "What this is".
- Adapted: checks charge-regime-map (field-gate stripe map turned into a Fano factor map over bias and dilution), charge-control-regime (turned into "same two-QPC measurement where no anyons or neutral modes are expected"), and charge-repeat-sweeps (turned into repeat measurements and cooldowns). The practice checks (report-counts, report-ranges, report-processing) applied unchanged.
- Matched: fine-tuning-and-selection (always applies).
- Skipped:
  - charge-trap-fractional-shift: its signature is Coulomb blockade or interference pattern shifts, and no such pattern is claimed here.
  - coulomb-dominated-interferometer: there is no Fabry-Perot interferometer.
  - protocol-parameter-sensitivity: there is no automated pass/fail protocol.
  - local-probe-loophole: it is specific to Majorana modes.
  - All zbp, quantization, nonlocal, island, shapiro, supercurrent, chiral, kitaev and diode entries: the device is not a hybrid superconductor, Josephson or dot device.

## Sources held out
- None. The only library sources I used belong to fine-tuning-and-selection and the practice checks: Frolov et al. arXiv 2309.09368v1 (2023) and Akrap et al. arXiv 2501.18631 (v2 dated 25 Mar 2026, which I checked on the abstract page). Both predate this paper (13 Aug 2026), so neither can discuss it.
- The paper itself was not fetched, per instructions.

## Related work, how each was checked
- 1005.5724 Bid et al.: abstract page opened (ID, title, first author confirmed). Full text grepped for the distance and temperature dependence (about 10% and 40% noise reduction over 80 µm at 10 and 25 mK).
- 1810.06871 Park et al.: abstract page opened (ID, title, first author Jinhong Park confirmed; he is also a coauthor of the paper under review). Full text grepped for the length dependence.
- cond-mat/0106071 Rosenow and Halperin: abstract page opened (ID, title, first author confirmed). Full text grepped.
- 2401.06069 Glidic et al.: abstract page opened (ID, title, first author confirmed). Full text read for its control (energy distribution spectroscopy at the analyzer QPC to set the coupling regime).
- 2606.17753 Ratnakar et al.: abstract page opened (ID, title, first author confirmed; dated 16 Jun 2026, before the paper). Full-text introduction and model read.
- Also opened and not listed: 1312.7553 (Inoue et al., neutral modes in many states and through the bulk) and 2311.15094 (Iyer et al., finite anyon width). Both abstracts confirmed; I left them out to stay within five.
- arXiv API calls were spaced by about 3 seconds, and I hit no rate limit.

## Library gaps
- No family for shot-noise / collider / time-domain braiding experiments, and no checks for them, for example a plotted trivial baseline for every configuration, or a dilution (R_QPC) sweep.
- Missing lookalikes I added as outside rows:
  - Incoherent heating of upstream neutral modes (Park et al. 2018; Bid et al. 2010).
  - Nonuniversal tunneling exponents from edge reconstruction (Rosenow and Halperin 2001).
  - Coulomb coupling between co-propagating channels changing the braiding signal (Ratnakar et al. 2026; Glidic et al. 2024).
- Candidate for a later version: finite anyon width (Iyer et al. 2023).

## Things I was unsure of
- I read figure values by eye from the rendered pages. My claim that F_neutral sits above both predictions at e*V_S/2k_BT of about 1 to 3 in Figs. S1h and S4h is an eyeball reading.
- Heating row: I marked the heating-model test "part" because Fig. S9 covers one data set and one configuration, and the text claims the rest without showing it. The heating model rests on one assumed length hierarchy (Eq. S56), so I did not treat it as enough on its own to rule out the lookalike.
- Exponent row: the paper does say "the effects of nonuniversal parameters ... cancel out in the Fano factors" (p. 12). That argument covers velocities and the saddle-point potential, not the scaling dimension, which the Fano factors depend on. So I chose "data bear on it" (R_QPC versus bias is plotted) over "argued, not tested".
- Coupling row: the paper mentions "inter-mode equilibration lengths" (p. 7) within its edge model, but never Coulomb coupling to the outer integer channels, so I marked it "not mentioned".
- report-counts marked done even though the fabricated count is missing; I asked about it in Q1.
- Recognition: I did not recognize this paper (it postdates my training). I know the earlier ν = 1/3 work it cites ([24], Lee et al. 2023) and did not use any outside knowledge of this paper's later history.

## Skill issues
- Scope: the skill says to adapt matching entries, but no entry's signature matches this kind of signal. It is unclear whether checks from a family whose signature does not fit (charge-regime-map is Fabry-Perot specific) should be adapted or skipped. flags.json needs library check ids, so I adapted them and said how.
- Outside rows: the skill asks for "a paper you opened" and flags.json allows one `source` URL per row, but two of my rows rest on two papers. I listed one in flags and named both in the report.
- Step 6 says to ask the standard questions "unless the paper already answers them (then say where)". It doesn't say whether the answered question should still appear in the numbered list. I kept it and said where it is answered (Q4).
- The "Done" bar for report-counts is unclear when devices measured are reported but devices fabricated are not.
- The prompt said the paper text was "extracted text"; it has heavy duplicated-glyph artifacts in math (for example "𝜈𝜈"). I fixed those in quotes to ν, which is a small departure from verbatim.
- Shared scratchpad: the folder `work/` already held other files, and I wrote p.txt there before moving to a private folder. Runs may need their own scratch folder named in the prompt.
