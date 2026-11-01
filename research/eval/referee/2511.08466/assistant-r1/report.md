# Lookalike check: Kinetic inductance of few-layer NbSe2 (arXiv 2511.08466v1)

*AI only. Written by the lookalike assistant on 2026-10-25 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. Your paper is a microwave kinetic inductance measurement, outside the library's scope, so I adapted the two entries that apply to any measurement (data selection, and a value that depends on a subtracted reference) and added two lookalikes from the resonator literature, marked (not in library). For each one, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first.

**The claim, as I read it.** An hBN-encapsulated NbSe2 flake terminating a λ/4 Al resonator lowers its frequency; the extracted sheet kinetic inductance scales roughly as 1/d and reaches 1.2 nH/□ in the thinnest device, D1 (Table 1, Fig. 4a; twelve devices, 2 to 52 nm). You read the thickness dependence as a clean- to dirty-limit crossover (Fig. 4c) and report self-Kerr coefficients of −0.008 to −14.7 Hz/photon (Table 1), with power and DC-bias sweeps for D6 (Fig. 3).

## Checks a careful reader will look for

None of the library's signal-specific check lists fits a resonator measurement, so the three practice checks apply.

1. Report devices measured, how many showed the effect, and why others were set aside : Partly. Table 1 lists twelve devices and Fig. 4a uses "nine NbSe2 devices" (p. 16); the number fabricated and set aside isn't given.
2. Disclose the full ranges measured and why each shown range was chosen : Partly. For D6, "observed over the power range from −100 dBm to −80 dBm" (p. 6); all microwave data are at 10 mK, and the text's "up to IDC = 30 µA" (p. 6) differs from the 15 µA axis of Fig. 3e,f.
3. Give the processing steps from raw data to figures, with data and code : Partly. The fits and the Lk extraction are written out (Eqs. 3, 5, 9 to 12, pp. 26 to 28); data are "available from the corresponding author upon reasonable request" (p. 22), with no code.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Data selection (fine-tuning-and-selection) | Tested in part | Devices counted, and how many showed the effect: part; how the shown data were chosen: no; second device shown: part | "Figure 3a shows a representative \|S21\| measurement from a λ/4-resonator terminated by a 9-nm-thick (determined by AFM) NbSe2 film (Device ID D6)." (p. 5); Table 1 gives numbers for all twelve devices, sweeps only for D6. | Say how many resonators were made and fitted, why D10 to D12 are absent from Fig. 4a, and show the Fig. 3 sweeps for D1 or D2. |
| Reference and contact inductance in the subtraction (series-resistance-subtraction, adapted) | Tested in part | Independent calibration, with its value: part (the Al control covers the resonator, the edge contacts and leads aren't calibrated); raw data before subtraction: all | "a control resonator of the same geometry that is terminated instead by a 250 nm-thick aluminum film (Fig. 2c)" (p. 5); Table 1 lists both raw frequencies for every device. | From Table 1 alone, fit total Lk against squares/d with a constant offset term, and give the fr,Al spread for identical control designs. |
| Microwave pair breaking and quasiparticle heating (not in library) | Tested in part | fr and Qi versus bath temperature as well as power: no; Qi followed with power: part (Fig. S4c, three NbSe2 devices) | "As the microwave power increases, enhanced Cooper-pair breaking leads to a reduction in the superfluid density (n0), resulting in a larger kinetic inductance" (p. 6) | Measure fr and Qi of D6 versus bath temperature at −120 dBm and compare with the power shift; fit the Fig. 3b traces in the IQ plane as Thomas et al. describe. |
| Conventional isotropic-gap current dependence (not in library) | Not tested (not mentioned) | Lk(I) toward the critical current of the same device, compared with the BCS form: no; Lk versus temperature compared with BCS: no | "consistent with the anisotropic nodeless pairing of NbSe2 reported in previous studies [43, 60]" (p. 7) | Extend Fig. 3f toward I* ≈ 0.4 mA, or measure Lk(T), and compare with the isotropic BCS form Annunziata et al. fit to Nb and NbN. |

## Questions about devices and data

1. How many NbSe2-terminated resonators did you fabricate and cool down, and how many gave a usable λ/4 resonance?
2. Why were the others set aside, and why are D10 to D12 absent from Fig. 4a and D6, D7 and D9 to D12 absent from Fig. 4c?
3. Which ranges did you measure beyond the ones shown: bath temperatures above 10 mK, powers above −80 dBm, and DC bias beyond the 15 µA in Fig. 3e,f (the text on p. 6 says up to 30 µA)?
4. What do the power and DC-bias sweeps of Fig. 3 look like for a second device, for example D1, which has the largest Kerr coefficient?
5. Is each Al-terminated control on the same chip as its NbSe2 resonator, how far does fr,Al spread for identical designs, and how much inductance do the edge contacts and leads add? D10 to D12 shift by only 20 to 30 MHz, and their Lk,sq sits two to three times above μ0λ²/d with your λ ≈ 230 nm (p. 9).
6. Which sample gives each row of Table S3 (I could not find the 7-layer row in Table S1), how does the Fig. 4c slope change without the literature monolayer point or with D1 at the 1.5 layers Raman gives, and what do the error bars in Fig. 4 represent?
7. How did you calibrate the photon number in Eq. 5 (line attenuation and Qc), with what uncertainty, and does the power shift of Fig. 3b separate from a bath-temperature shift? How do the rising Qi of Fig. S4c and the linewidth broadening reported on p. 27 fit together? (The lowest tick in Fig. 3c reads −1.15 MHz; from the spacing it looks like −0.15.)
8. Could you show Lk(I) closer to I* = 0.4 mA, or Lk versus temperature, so the reading of Fig. 3f as anisotropic nodeless pairing can be compared with an isotropic gap?

## Related work

- Fridman et al. 2025, "Anomalous Thickness Dependence of the Vortex Pearl Length in Few-Layer NbSe2", <https://arxiv.org/abs/2503.03815>. SQUID-on-tip Pearl lengths in 3 to 53 layer NbSe2 follow 1/d above 10 layers and sit a factor of three higher from 3 to 6 layers: an independent probe of 2D superfluid density over your thickness range.
- Zheng et al. 2026, "Encapsulation epitaxy of air-stable monolayer superconducting films for quantum circuits and qubits", <https://arxiv.org/abs/2609.19321>. Epitaxial monolayer NbSe2 (Tc near 1 K), edge-contacted in superconducting circuits, shows about 0.7 nH per square.
- de Visser et al. 2014, "Evidence of a nonequilibrium distribution of quasiparticles in the microwave response of a superconducting aluminium resonator", <https://arxiv.org/abs/1306.4992>. Below 200 mK, an Al resonator's quality factor and frequency both fall with microwave power, from quasiparticles created by absorbed microwaves.
- Thomas et al. 2020, "Nonlinear Effects in Superconducting Thin Film Microwave Resonators", <https://arxiv.org/abs/2001.02540>. Treats nonlinear kinetic inductance, two-level-system loss and quasiparticle heating together, and shows how the Argand-plane trajectory tells them apart.
- Annunziata et al. 2010, "Tunable superconducting nanoinductors", <https://arxiv.org/abs/1007.4187>. Nb and NbN nanowires show kinetic inductance versus temperature and current in reasonable agreement with BCS theory, a conventional baseline for Fig. 3f.

Happy to rerun this if you share the raw S21 sweeps and the Table 1 fit inputs.
