# Run notes: 2603.12092v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (updated 2026-10-24), 28 entries.
- Read: the v1 PDF (28 pages; figures on pp. 14 to 18 rendered at 110 and 300 dpi; Extended Data on p. 28) and its extracted text. The arXiv abstract page and other versions were not fetched, per the task; the title comes from the PDF metadata and title page.
- Could not open: the Supplementary Information (SI 1 to SI 14, the supplementary video), which the main text cites heavily and which is not in the v1 PDF. Fetching it was out of bounds for this run. No data repository is linked in the PDF; no ancillary figure data, so read_mtx.py was not used.
- I did not recognize the paper.

## Claims table (step 1)

| Claim | Figures | Device | Counts and ranges in the PDF |
|---|---|---|---|
| ϕ12 ≈ π from opposite chirality in the two arms | Fig. 3a, 3b; Ext. Data Fig. 2 | one 45° SQUID, 20 K | 5 bias values 41 to 59 µA (3a, 10 µT in-plane) and 7 values 22 to 48 µA (3b, 0 µT); in-plane −20 to 20 µT in 10 µT steps, up and back (10 intercepts); "another device" in SI 14 (absent); intercept error bars not given |
| Broken TRS at B = 0 (η′ ≠ 0) | Fig. 4a, 4b | 45° at 60 K (η′ ∼ 4%), 40° at 74 K (η′ ∼ 8%) | perpendicular field ±75 µT and ±40 µT; 0° control stated in SI 9 (absent) |
| Second harmonic from co-tunneling | Fig. 4c, 4d; SI 12 (absent) | 45° at 60 K; 40° at 74, 66, 60 K | A2/A1 = 0.20, 0.37, 0.27 |
| Interfacial Josephson inductance and stiffness T dependence | Fig. 2f | 45° | 20 to ∼75 K |
| SQUID operation and flux noise ∼1.5 µΦ0/√Hz | Figs. 1, 2, 5; Ext. Data Fig. 1 | 45° and 40° | period 3.3 and 2.2 µT, about seven times below Φ0/Ageo |

Devices: twist angles 0°, 40°, 42°, 44°, 45° listed (p. 4); number fabricated, measured, and showing each effect not given; cooldowns not stated; Table V (SI 7) for other periods is absent.

## Matching (step 2)

- Families: diode (zero-field η′ claim) and practice. No library family covers the SQUID phase (ϕ12) claim or the CPR harmonic claim; the library has no `checks` for diode or supercurrent families, so only practice checks were walked.
- Adapted: diode-vortex-screening (signature "exotic pairing" read as chiral TRS-broken order; test "plain film or junction of the parent superconductor" taken as the nominally 0° twisted SQUID); fine-tuning-and-selection (always).
- Skipped: all zbp, quantization, nonlocal, island, chiral, kitaev entries (no tunneling spectroscopy, no nanowire, no QAH); shapiro entries (no microwave irradiation); field-enhanced-supercurrent-resonances (no supercurrent growing with field); charge-trap-fractional-shift and coulomb-dominated-interferometer (no dot or quantum Hall interferometer; I considered adapting charge-trap to a vortex trap shifting the pattern by a fraction of a period, but the mechanism is electrostatic, so I used an outside entry with its own source); protocol-parameter-sensitivity (no automated pass/fail protocol); series-resistance-subtraction (four-probe, no conductance quantization claim); local-probe-loophole (no Majorana claim).
- Hold-out: no library source cites this paper as far as I can tell (all library sources predate March 2026 except the v2 of 2501.18631 and 2502.19560; I did not open them and used only the library quotes, none of which mention this paper). No source skipped.

## Status reasoning

- fine-tuning-and-selection: counts part (twist angles listed, effect counts missing); selection no; second dataset part (TRS and harmonic shown in two devices; phase in one device in the PDF).
- diode-vortex-screening: 0° control marked part because the statement points to SI 9, which is not in the PDF (rule: unclear, mark part with a clause). Field dependence of η′ shown for both devices: all.
- Outside rows all "data bear on it": Ext. Data Fig. 2 (spread 0.75π to 0.95π, sweep-direction dependence), Fig. 4a (traces look like shifted copies), Fig. 4c (cusp-like maxima). The authors invoke Abrikosov vortices only as a mechanism for the claimed physics, so I did not call it "argued".
- My readings of Fig. 3 slopes (about 0.05 and 0.07 period per µA) and intercepts (about −2.0 and −0.45) come from the 300 dpi render and are approximate.

## Related work checks

- 2108.13455 (Zhao), 1903.07965 (Zhu): API abstract and arXiv abstract page (title, first author) checked; abstract only.
- 1003.1033 (Golod 2010), 2205.12196 (Golod and Krasnov 2022), 2302.02705 (Babich): abstract page and full text read for the control passages used as tests.
- Also opened 2305.15472 (Yuan et al., inhomogeneity-induced TRSB) abstract; not listed, to keep five.
- One arXiv search (abs: twisted AND BSCCO AND SQUID) returned nothing; no result was this paper.

## Library gaps

- No entry or check for phase-sensitive SQUID experiments: vortex or trapped-flux phase shifts (Golod 2010, 1003.1033), intercept extrapolation uncertainty.
- No entry for zero-field diode from trapped vortex stray fields with nonuniform bias (Golod and Krasnov 2022, 2205.12196), or for residual-field offsets in nominal B = 0 asymmetry.
- No entry for CPR harmonics read from an asymmetric SQUID (Babich 2023, 2302.02705), including inductance β ∼ 1.
- No `checks` for diode or supercurrent families.

## Skill issues

- When the SI is cited but absent from the PDF and fetching other versions is forbidden, the skill does not say whether a test stated as "shown in SI" counts as part or no. I used part with a clause.
- The skill asks to use the title "on the arXiv abstract page", which this run could not open; I used the PDF title.
- Step 7 says to write report files; this run returns them in the reply per the task.
- "Not tested (argued, not tested)" vs "data bear on it" is ambiguous when the authors invoke the lookalike's ingredient (vortices) as part of their own mechanism.

## Unsure

- Whether the 45° device of Fig. 3 (20 K) is the one in Figs. 1c, 2d, 4a (60 K).
- The flux-offset reading of Fig. 4a is visual; I did not digitize the traces.
