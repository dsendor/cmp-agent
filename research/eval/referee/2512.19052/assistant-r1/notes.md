# Run notes: arXiv 2512.19052v1

**AI only.** Lookalike assistant run, 2026-10-25. Library meta.version 0.5 (updated 2026-10-24, 28 lookalikes plus checks for zbp, shapiro, kitaev, charge and practice).

## What I read

- Skill: cmp-assistant/skill/SKILL.md and skill/report-template.md, read once at the start.
- Library: cmp-assistant/library/lookalikes.yaml, read in full.
- Paper: the supplied v1 PDF and its extracted text (main text pp. 1-15 with Figs. 1-4, Methods, and Supplementary Notes 1-5 with Supp. Figs. 1-5). Figures read from the PDF; Figs. 3, 4 and Supp. Fig. 5a also re-rendered at 250 dpi (pdftoppm) to read peak positions and trace shapes.
- I did not open the arXiv abstract page or any other version of the paper (task rule). The title comes from the PDF.
- No figure data or ancillary files were supplied; read_mtx.py not used. The paper links no data repository.
- By accident I printed the first five lines (docstring) of scripts/check.py while counting library entries; nothing from it was used.

## Claims table (step 1)

| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| Gate cycling imprints a Tc and Rs memory, stabilizing to a loop after about four cycles | Fig. 1c-f; Supp. Fig. 1 | One AlOx/KTaO3(111) sample, 2.5 x 2.5 x 0.5 mm, van der Pauw, Au back gate | Vg ±50 V (±40 V in Supp. Fig. 4); Tc at 50% Rn; Rs at 1.4 K; Tc about 1.02 K to 1.09 K at Vg = 0 (1.14 K at -50 V); n about 1.03-1.09e14 cm^-2; μ about 70-80 cm2/Vs. Samples fabricated, cooldowns, sweep rate: not given. |
| Loop size persists to about 100 K | Fig. 1g; Supp. Fig. 2 | same | 5-180 K, fourth cycle shown at each temperature (stated selection rule) |
| Asymmetric gate current marks irreversible charge exchange | Supp. Fig. 3 | same | 10-120 K; 10-minute holds at ±50 V; Ig to about -10 nA; sweep rate not given; leakage not separated |
| Red light (630 nm, 1.97 eV) erases the memory; switching between 795 and 840/856 Ohm repeats | Fig. 2b, c, h, i; Supp. Fig. 4 | same | Illumination mainly at 10 K; LED about 1 cm away, fixed V_L; periods 180-9000 s; one wavelength; LED heating visible at 2 K; sample temperature during light not given |
| Light raises n and μ, gate cycles lower them; sequence dependence of μ | Fig. 2d-g | same | Hall at B = ±6 T in separate repeated runs (Methods); no Hall data for the L0-L4 states of Fig. 2i |
| Two thermally activated loss peaks: PNR flipping (76 meV) and OV ionization (236 meV) | Fig. 3a-c | same, gate-to-2DEG capacitor | 0.1-4001 Hz, 7 frequencies, 5 V ac; Peak 1 about 29-47 K, Peak 2 about 89-139 K (my reading of Fig. 3c); curves vertically shifted; peak-picking method not described |
| ΔL linear in ε from 95 K to 35 K, steeper below | Fig. 3a, d | same | about 25 temperature points; 2 linear fits |
| Dark relaxation accelerated at 35 K and 95 K | Fig. 4; Supp. Fig. 5 | same | 10-180 K, about 25 temperatures; each maximum is one point; the Fig. 4a 35 K and 95 K traces differ in noise and size from neighbours and from Supp. Fig. 5a traces at the same temperatures |

Missing counts: number of samples fabricated and measured, number that showed each effect, cooldowns, gate sweep rate, LED power.

## Matching (step 2), entries skipped or adapted

- Scope: the paper is not topological transport (oxide 2DEG superconductivity under gate and light, plus dielectric spectroscopy). Said so in one sentence under "What this is".
- Used as is: fine-tuning-and-selection (applies to every signature); practice checks report-counts, report-ranges, report-processing.
- Adapted: none of the library entries were adapted; the family checks (zbp, shapiro, kitaev, charge) have no counterpart here.
- Skipped, with reason: all zbp, quantization, nonlocal, island, shapiro, supercurrent, chiral, kitaev, diode and charge entries (abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, fine-tuned-plateau, one-end-only, trivial-andreev-band-gap-reopening, micromagnet-stray-field, full-shell-flux-andreev, chiral-plateau-superconductor-short, island-states-coulomb-spacing, shapiro-landau-zener, shapiro-nonlinear-resistance, field-enhanced-supercurrent-resonances, charge-trap-fractional-shift, spin-orbit-length-pinning, exceptional-point-zero-mode, transparent-junction-pi-crossing, switching-jump-blind-region, false-poor-mans-majorana, local-probe-loophole, coulomb-dominated-interferometer, diode-vortex-screening): no tunneling spectroscopy, junction, island, Shapiro, chiral or interferometer signal in this paper. series-resistance-subtraction: Rs comes from a geometric FEM factor, and the claims rest on relative changes and on Tc at half Rn, which a fixed factor does not move; the analogous concern for the dielectric data is covered by the Maxwell-Wagner row. protocol-parameter-sensitivity: no pass/fail protocol. local-probe-loophole: no Majorana claim.

## Status reasoning

- fine-tuning-and-selection: tested in part; one selection rule stated (fourth cycle, Supp. Note 2) and repeat switching runs on the same sample (Supp. Fig. 4); no sample count, no second sample.
- Irreversible escape into traps (outside, Biscaras): the paper does not conclude against it; it adopts a close version ("irreversible charge exchange") and adds PNRs. Tests taken from Biscaras' protocol (sweeps to growing maximum voltage; time-resolved R after gate steps; warm-up at Vg = 0 showing release temperatures). Max-voltage test marked part (±40 vs ±50 V after light reset, Rs only); step-relaxation marked part because Rs traces exist in Supp. Fig. 4 but are not analysed as a step response (unclear, so part per the skill).
- Tc set by disorder/mobility (outside, Chen): tests from Chen's procedure (Hall n and μ measured at each Tc state; layer thickness from critical fields, their Fig. S10). Part: Supp. Fig. 1 gives Tc, n, μ for gate cycles; L0-L4 have Tc only. My own reading: within each loop Tc is highest where μ is lowest, and light raises μ while lowering Tc; I put this in the suggestion, framed as a check.
- Maxwell-Wagner (outside, Lunkenheimer): no test shown; the multi-frequency spectra in Fig. 3a, b could be fitted, so "data bear on it". Quote given is the Methods approximation that neglects stray resistance.

## Sources held out

None. No library source I used (Frolov et al. arXiv 2309.09368 and Akrap et al. arXiv 2501.18631, via the fine-tuning-and-selection entry and the practice checks) discusses this paper as far as the library's quotes show; I did not open those sources, so I could not confirm they do not cite it (Akrap v2 and the Science version of Frolov are 2026).

## Related work: how each link was checked

- 2506.16298 (Zhang et al. 2025): arXiv abstract page opened; ID, title, first author Meng Zhang and the description confirmed from the abstract. It is ref. 30 of the paper.
- 1206.1198 (Biscaras et al. 2012): abstract page opened, full text read (pp. 2-4 and supplementary Figs. 9, 10) for the threshold escape, Tc saturation and the 280 K warm-up recovery. OpenAlex shows a 2014 Sci. Rep. paper by the same group ("Limit of the electrostatic doping..."), but did not link it to this arXiv ID, so I cite the arXiv record as itself.
- 2009.05896 (Chen et al. 2020): found via OpenAlex for DOI 10.1126/science.abb3848 (ref. 17 of the paper); abstract page opened, full text read (pp. 2-5) for the disorder and mobility statements. The arXiv title differs from the Science title; I used the arXiv title.
- 2203.05867 (Liu et al. 2022): found via OpenAlex for DOI 10.1038/s41467-023-36309-2 (ref. 18); abstract page opened; description from the abstract only.
- cond-mat/0201146 (Lunkenheimer et al. 2002): found via OpenAlex for DOI 10.1103/PhysRevB.66.052105; abstract page opened and full text read (pp. 1-2) for the Maxwell-Wagner mechanism and the controls (geometry, contacts, equivalent circuit, light intensity).
- No search result was the paper under review or a version of it.

## Library gaps

- No family for oxide-interface or gate-controlled superconductivity, ferroelectric or quantum-paraelectric memory, or persistent photoconductivity.
- Candidate entries from this run: irreversible escape of electrons out of a gated well into traps (Biscaras et al., arXiv 1206.1198); Tc tracking the gate-tuned disorder level (Chen et al., arXiv 2009.05896); Maxwell-Wagner contact relaxations mimicking dipolar loss peaks (Lunkenheimer et al., arXiv cond-mat/0201146).
- Not added, for lack of an opened source: LED heating as a lookalike for optical erasure (kept as question 7); gate leakage versus displacement current (kept as question 8, partly raised by Biscaras).

## Unsure

- Peak temperatures and the Arrhenius extrapolation in question 6 are read off Fig. 3c by eye (Peak 1 about 1/T = 0.021-0.035 K^-1, Peak 2 about 0.0072-0.0112 K^-1); with the paper's activation energies, extending to f = 1/(2πτ) or 1/τ for τ about 10^3 s gives about 24-25 K and 74-78 K. Comparing an ac loss peak with a dark-relaxation time is itself an assumption, so I framed it as a question.
- Question 5 rests on how the Fig. 4a and Supp. Fig. 5a traces look; the two figures use different normalizations (R1 against ΔR0), so the magnitudes are not directly comparable, but the noise and shape difference is visible.
- Whether Rs traces in Supp. Fig. 4 count as a step-relaxation test: marked part.
- I did not recognize the paper and know nothing of its later history.

## Skill issues

- Step 7 says to use the title on the arXiv abstract page, and the Input section says to read the abstract page; this run forbids opening it, so the title came from the PDF.
- The skill's scope rule says to adapt matching entries for out-of-field papers, but gives no guidance when no family check matches at all; I used only the practice checks and said so. A line on how many outside rows are acceptable would help.
- Writing rules forbid "instead of" and "rather than" in my words; the Status rules use "argued, not tested", which is fine, but the template's "What this is" text is boilerplate that pushes the 600-900 word target when a scope sentence is added (this report is about 900 words outside the table).
- The template's check line format "<check> : Done" leaves it open whether to use the library's check text verbatim or a short name; I used the library text.
- Step 6 asks for "how many devices", which reads oddly for a single bulk heterostructure; I wrote "heterostructures".
