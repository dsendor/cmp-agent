# Lookalike check: Trapping e/4 quasiparticles in bilayer graphene (arXiv 2608.27444v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. The library's charge entries are written for quantum dots and Fabry-Perot
interferometers, so I adapted them to an antidot driven by an air-bridge gate.

**The claim, as I read it.** In one gate-defined bilayer graphene antidot near 14 T, the
antidot-gate (ADG) period normalized to the ν = −1 electron period is ΔV/ΔV1 ≈ 0.25 at
ν = −5/2, −1/2 and 3/2. You read this as localized e/4 charge added one at a time in the
Coulomb-dominated (CD) regime, with e/3 at ν = 2/3 (Fig. 2, p. 4). A second result is a
crossover to about twice that period as the side gates raise the antidot-edge coupling.
The crossover is absent at ν = −4/3 and −1/3 (Fig. 3, Figs. S6 and S7).

## Checks a careful reader will look for

1. Map the oscillations in the field and gate plane and say which regime they are in : Done. Each claimed state has a Vadg-B map and 2D-FFT, with periods "consistent with measurements in the CD regime" (p. 4, Fig. 2e–h). The doubled regime is left open (p. 7).
2. Show the effect is absent where the exotic state is not expected, and rule out charge traps and gate leakage : Partly. Control fillings behave as expected, "∆V /∆V1 = 0.37 ± 0.04, in agreement with the value q/e = 1/3" at ν = −4/3 (p. 4, Fig. 1g–h), and ν = −1, −2 give e (Fig. S3). Traps and leakage aren't discussed.
3. Repeat sweeps to separate reproducible shifts from stochastic charge jumps : Partly. At ν = 2/3 you "repeated the same sweep multiple times" (p. 25, Fig. S13); not shown at the e/4 states.
4. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Not done. The Methods describe one device ("The device was fabricated", p. 9), with no counts.
5. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. The side-gate limit of "approximately 6 V" (p. 13) and the field step (p. 10) are given; the windows explored at each filling are not.
6. Give the processing steps from raw data to figures, with data and code : Partly. "Both the raw and background-subtracted data are shown in the Supp. Material for all data included in the paper." (p. 9). Data are "available from the corresponding author upon reasonable request" (p. 10); no code is linked.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Charge trap or side state near the antidot (adapted: a capacitively coupled trap or puddle adds or shifts resonances) | Tested in part | Shifts absent where the exotic state is not expected: all (control fillings ν = −1, −2, −4/3, −1/3); Gate leakage checked: no; Map of where in two-gate space the shifts occur: part (ADG-TG maps only at ν = −1 and −4/3, Fig. S5) | "This data set shows substantial gate instability, therefore we validate the periodicity with a second, independent method" (p. 4, Fig. 2c) | Repeat the e/4 sweeps as in Fig. S13, report leakage at the gate voltages used, and add one ADG-TG map at an e/4 state. |
| Coulomb-dominated versus Aharonov-Bohm or mixed regime (adapted to an antidot: outside the CD limit the gate period stops counting localized charge) | Tested in part | Field and gate map with stripe slope and spacing: all; Regime and charging parameters reported: part (regime stated, no charging energy); the maps fit the CD limit, and ΔB errors up to 44% leave a mixed regime unseparated | "Although the fits cannot therefore identify the transport regime, they still constrain the electron temperature of our setup." (p. 30, Fig. S17) | Extract a charging energy from Figs. S8c–S11c and take a longer field window at ν = −5/2; the same would help the doubled regime you leave open (p. 7). |
| Fine-tuning and selection | Tested in part | Devices and datasets measured, and how many showed the effect: no; How the shown data were chosen: part (weak-coupling regime and excitation current stated, p. 5, p. 9); A second device or dataset shown: part (second minimal-regime traces at ν = −1/2, 2/3, 3/2 in Fig. 3) | "Figures 3d,g,j show the transmitted resistance oscillations as a function of the ADG voltage at ν = −1/2, 2/3 and 3/2 respectively, measured in the same minimal excitation regime." (p. 6) | State device and cooldown counts, and show a second minimal-regime map at ν = −5/2 at another side-gate setting or field. |
| Field-dependent charging energy from the constrictions (not in library; Hajigeorgiou et al. 2026, https://arxiv.org/abs/2606.19187) | Left open by the authors | Charging energy followed as a function of magnetic field: no; Charging energy correlated with the constriction magnetoconductance: no | "We therefore cannot exclude additional modifications of the edge structure or the formation of lower density fractional regions between the side gates and the AD, which could further alter the antidot electrostatics and charging energy [51]." (p. 8) | For the doubled regime at ν = −1/2, plot the diagonal conductance against B beside Fig. 3m and track the DC-bias charging energy over the same window. |

## Questions about devices and data

1. How many devices did you measure, and how many showed the e/4 period? The Methods describe one device (p. 9), and Fig. 1b shows "a device with the air-bridge".
2. If there were others, why were they set aside, and how many cooldowns do the data span?
3. Which ADG, side-gate and field windows did you measure at each filling beyond those shown (Fig. 2a spans 35 mT and 0.7 V), and how many side-gate settings did you try before reaching the minimal-excitation regime?
4. What does a second minimal-regime dataset at ν = −5/2 look like? Those oscillations are "considerably weaker than at the other fillings" (Fig. S8, p. 20), and the spacing histogram gives 51.56 ± 23 mV next to 62.8 mV from the FFT.
5. The ADG windows run from about −3.6 V to +3.4 V across fillings (Fig. 2a–d), and ΔV1 comes from ν = −1 at 10 T. Is the ADG lever arm the same across those windows?
6. Did you check gate leakage from the air bridge and side gates up to 5 V, and do repeated sweeps at the e/4 states reproduce as at ν = 2/3 (Fig. S13)?
7. Could you extract the charging energy from the DC-bias maps (Figs. S8c–S11c), and remeasure ν = −5/2 over a longer field window? Its 5.9 ± 2.6 mT period has about six 1 mT steps per period over 35 mT (Fig. 2a).
8. Your earlier antidot doubled its period at integer ν = 2 and 4 as coupling grew (arXiv 2504.16750). Did you tune the side gates at ν = −1 or −2 here? At ν = −5/2 the minimal and doubled maps sit in different ADG windows (Fig. S8a, g); was that doubling reached by side gates alone?

One small thing: the Fig. 3 panels label d–f as ν = 2/3 and g–i as ν = −1/2, and the caption and p. 6 text assign d–f to ν = −1/2. On p. 7, "ν = −2/3" looks like it means 2/3.

## Related work

- Di Luca et al. 2025, "Tunable inter-edge interactions in a bilayer graphene quantum Hall antidot", <https://arxiv.org/abs/2504.16750>. Stronger antidot-edge coupling doubles the period at integer ν = 2 and 4 and moves the field period from φ0/ν to φ0, read as a CD to Aharonov-Bohm crossover.
- Di Luca et al. 2025, "Quantum Hall Antidot as a Fractional Coulombmeter", <https://arxiv.org/abs/2509.04209>. A CD-regime bilayer graphene antidot gives e/3 at ν = 4/3, 5/3, 7/3 and 2e/3 at ν = 2/3.
- Kou et al. 2012, "Coulomb Oscillations in Antidots in the Integer and Fractional Quantum Hall Regimes", <https://arxiv.org/abs/1201.1600>. GaAs antidots identified as Coulomb type from field-period scaling with the number of bound edges, with tunneling charge 2e/3 at ν = 2/3.
- Kim et al. 2024, "Aharonov-Bohm Interference in Even-Denominator Fractional Quantum Hall States", <https://arxiv.org/abs/2412.19886>. A bilayer graphene interferometer at two even-denominator states shows a 2Φ0 period and e/4 bulk quasiparticles when the filling is detuned.
- Alkalai et al. 2026, "Observation of e/4 charge at ν=1/2 in GaAs", <https://arxiv.org/abs/2602.08468>. Shot noise gives e/4 at ν = 1/2 in two nominally identical devices on two setups.

Happy to rerun this if you share the figure data or the analysis code.
