# Run notes: 2511.08466v1

AI only. Lookalike assistant run, 2026-10-25. Library version 0.5 (meta.updated 2026-10-24, 28 lookalike entries).

## What I read
- skill/SKILL.md, skill/report-template.md, library/lookalikes.yaml (all entries and the checks section), read once at the start.
- The paper from the local copies only: paper.txt in full (main text, Table 1, SI sections 1 to 9, Tables S1 to S3) and paper.pdf pages 13 to 16 (Figs. 1 to 4) and 34 to 38 (Figs. S1 to S8). I rendered p. 15 at 300 dpi and cropped Figs. 3b, 3c and 3f to read the axes.
- I did not fetch the paper online in any form. I took the title from the PDF (the arXiv abstract page was off limits for this run).
- No ancillary files and no data repository: data are "available from the corresponding author upon reasonable request" (p. 22). read_mtx.py was not needed.
- I didn't recognize this paper or know of any later history for it.

## Claims table (step 1)
| Claim | Figures | Devices | Counts and ranges |
|---|---|---|---|
| Lk,sq scales roughly as 1/d, 1.2 nH/sq in the thinnest device | Table 1, Fig. 4a, 4b | D1 to D12 in Table 1; Fig. 4a shows nine (D1 to D9, x axis 1 to 13 nm) | d = 1.99 to 52.12 nm by AFM; D1 taken as 1.5 layers from a weak Raman feature (p. 33, Fig. S7). Fabricated, cooled and failed counts not given. Cooldowns not given. All at about 10 mK. Error bars in Fig. 4a not explained. |
| Clean- to dirty-limit crossover with decreasing thickness | Fig. 4c, 4d, Table S3, Fig. S5 | Lk from D1, D2, D3, D4, D5 (twice), D8; Rs and Tc from separate DC devices (Table S1, seven devices) and from refs. 38, 39 | Slope 16.3, intercept 80 pH. The monolayer point uses literature Rs = 240 Ω, Tc = 3.5 K. The 7-layer row (Rs 25, Tc 6.0) matches no device in Table S1. |
| Small self-Kerr, −0.008 to −14.7 Hz/photon | Fig. 3b, 3c, Table 1, Eq. 8 | Sweeps for D6 only; K values listed for all twelve | Power −120 to −80 dBm at the sample (Fig. 3b), onset −100 dBm, bifurcation −82 dBm; photon number about 1e4 to 8e4 in Fig. 3c; calibration from nominal 70 dB attenuation and Eq. 5. Eq. 8 gives −3.8 vs measured −1.7 Hz/photon. |
| Quadratic Lk(IDC), "consistent with the anisotropic nodeless pairing" | Fig. 3e, 3f, Eq. 1 | D6 | Text says up to 30 µA, figures show 0 to 15 µA; I* = 0.4 mA fitted, Ic about 0.4 mA from a separate 8 nm DC device (Fig. S1e). |
| Contacts are superconducting and near-zero resistance | Fig. S1, Table S1 | Seven DC devices, 4 to 10 nm | Rc at the noise floor (0.01 Ω) for most ion-mill times. |
| Steeper than expected scaling may reflect Pearl-regime confinement | Fig. S6 | All | Argued only, with λ = 230 nm from ref. 66. |
| Qi | Table 1, Fig. S4c | Table 1 all; Fig. S4c shows five resonators (three NbSe2: 8, 25, 30 nm), though p. 26 says six | −150 to −80 dBm in Fig. S4c. |

## Entries matched, adapted, skipped
- Scope: the paper is a microwave resonator measurement of kinetic inductance, outside topological transport. Said so in one sentence under "What this is".
- Adapted: fine-tuning-and-selection (applies as written to any signature); series-resistance-subtraction, adapted from "subtracted series resistance moves the conductance" to "the Al reference resonator and uncalibrated contact and lead inductance move the extracted Lk". I kept the library test text in flags.json and gave the adapted wording in the report.
- Checks: only the practice checks (report-counts, report-ranges, report-processing). No zbp, shapiro, kitaev or charge check list applies.
- Skipped, no matching signature (no zero-bias peaks, quantized conductance, nonlocal conductance, islands, Shapiro steps, field-enhanced supercurrent, fractional charge, chiral plateaus, Kitaev chains or diode effect): abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, fine-tuned-plateau, one-end-only, trivial-andreev-band-gap-reopening, micromagnet-stray-field, full-shell-flux-andreev, chiral-plateau-superconductor-short, island-states-coulomb-spacing, shapiro-landau-zener, shapiro-nonlinear-resistance, field-enhanced-supercurrent-resonances, charge-trap-fractional-shift, spin-orbit-length-pinning, exceptional-point-zero-mode, transparent-junction-pi-crossing, switching-jump-blind-region, false-poor-mans-majorana, local-probe-loophole, coulomb-dominated-interferometer, diode-vortex-screening. Also protocol-parameter-sensitivity (no pass/fail protocol in the paper; its range and processing concerns are covered by the practice checks).

## Outside rows (library gaps)
- Microwave pair breaking and quasiparticle heating: a power-dependent downshift can come from absorbed power creating quasiparticles, which is a different thing from a reactive Kerr term. Source opened: de Visser et al. 2014 (arXiv 1306.4992, abstract and full text). Tests taken from its control (fr and Q against both temperature and power; Q falls along with fr). Thomas et al. 2020 (arXiv 2001.02540, abstract and full text) supplies the Argand-plane check used in the suggestion. The paper's own wording (p. 6) gives pair breaking as the mechanism, while Eq. 8 treats the shift as current-driven Kerr. I marked "Qi followed with power" as part: Fig. S4c shows Qi against power for three NbSe2 devices, and I could not tell whether the "8nm" trace is D6 (8.81 nm) or D5 (7.98 nm).
- Conventional isotropic-gap current dependence: an ordinary s-wave film also gives an Lk(I) that rises from Lk(0) as I squared at small currents, so Fig. 3f doesn't single out anisotropic nodeless pairing. Source opened: Annunziata et al. 2010 (arXiv 1007.4187, abstract and full text), which fits Nb and NbN Lk(T) and Lk(I) with BCS. Clem and Kogan 2012 (arXiv 1207.6421, abstract and the relevant section) give the isotropic-gap calculation of Lk up to depairing. I opened it but didn't list it, to stay within five.
- Suggested library additions: a "microwave resonator / kinetic inductance" family with entries for reference-resonator mismatch and contact or parasitic inductance, photon-number calibration, heating vs Kerr, and pairing symmetry read from Lk(I) or Lk(T).

## Sources held out
- None. Before relying on any library source, I checked the two that have 2026 versions for mentions of this paper: Akrap, Frolov et al. (arXiv 2501.18631) and Legg (arXiv 2502.19560), latest versions, full-text searched for "NbSe", the arXiv ID and the first author: no hits. The other library sources I would have relied on are quoted from versions older than November 2025. In the end the report uses only library entries, and no library source is cited in it.

## Related work checks
All five abstract pages opened on arxiv.org; ID, title and first author confirmed from the page metadata; descriptions checked against the abstracts.
- 2503.03815 Fridman: abstract.
- 2609.19321 Zheng: abstract. It's later than the paper under review and shares an author (S. Zaman). I describe only its own abstract result.
- 1306.4992 de Visser: abstract and full text.
- 2001.02540 Thomas: abstract and full text (sections 2.5, 4, 5).
- 1007.4187 Annunziata: abstract and full text (results and conclusions).
Searches: export.arxiv.org API with 3 s waits. The paper under review didn't come up in any search.

## Things I was unsure of
- My estimate that Lk,sq for D10 to D12 sits two to three times above μ0λ²/d comes from Table 1 and the paper's λ ≈ 230 nm: 2.7, 2.2 and 1.3 pH/sq expected, against 8, 5 and 4 measured. It's my calculation, and I asked it as a question.
- Fig. 3c: the lowest y tick reads −1.15 MHz. The tick spacing suggests −0.15, and with that reading the slope is about 1.7 Hz/photon, which matches the stated K. I raised it as a typo question.
- Whether each Al-terminated control sits on the same chip as its NbSe2 resonator. The text says "a control resonator of the same geometry", and fr,Al spans 5.21 to 5.62 GHz across Table 1.
- The SI text gives input attenuators of 20, 20 and 30 dB (p. 25), while Fig. S2 shows 20, 10, 20 and 20 dB. Both total 70 dB. I didn't put this in the report.
- For "Qi followed with power" I counted the Fig. S4c traces as shown for part of the Kerr evidence.

## Skill issues
- Scope adaptation: the skill doesn't say how an adapted entry should appear in flags.json (library test text or adapted text). I used the library text there and gave the adapted wording in the report.
- When no family check list applies, the skill doesn't say whether to note that. I added one sentence and walked only the practice checks.
- An outside row gets a single "source" URL in flags.json, while its tests may draw on two opened papers (here de Visser and Thomas).
- Step 7 asks for the title "on the arXiv abstract page", and this run forbade opening it. I used the PDF title.
- Step 7 says to write reports/<id>.md; this run asked for inline output instead.
- Word target: with four mandatory questions plus paper-specific ones, the report lands near the 900 word ceiling once URLs are counted. The skill doesn't say whether URLs and headings count.
- The rule "a test counts only when the paper shows the measurement" conflicts a little with the outside-row rule to take tests from the cited paper's control: the paper's Eq. 8 comparison of DC and microwave nonlinearity is a real analysis, but it isn't one of de Visser's tests. I left it out of the tests and noted it here.
