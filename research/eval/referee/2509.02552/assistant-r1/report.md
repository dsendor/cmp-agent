# Lookalike check: Interaction-limited conductivity of TBG from THz photoresistance (arXiv 2509.02552v1)

*AI only. Written by the lookalike assistant on 2026-10-25 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your paper is a hot-electron transport measurement in twisted bilayer graphene. That
is outside the library's topological scope, so I used only its general practice checks and its
selection entry, adapted its series-resistance entry to the ρ0 subtraction in your Fig. 3b,c,
and added two lookalikes from the published literature, marked "(not in library)".

**The claim, as I read it.** At a fixed lattice temperature of 2 K, 0.14 THz radiation raises
the electron temperature, and the resulting positive photoresistance in 2° TBG and two
magic-angle devices (Fig. 1d, Fig. 2a,b,d,e) shows that electron interactions set the
temperature-dependent resistivity, including where ρ is linear in T (Fig. 2c). Separately,
the 1.58° device shows T² resistivity at |ν| ≈ 0.1 and 3.8, below the umklapp threshold
(Fig. 3b to 3d), which you attribute to interpocket e-e scattering (Eq. 1).

The Supplementary Information is cited for the 70% figure, the Te estimate and the umklapp
prefactor. It is not in the v1 PDF, so I judged only what the eight pages show.

## Checks a careful reader will look for

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. Five devices are named (2°, MATBG1, MATBG2, 1.58°, MLG), and you write that the T² regime "is consistently reproduced in all our high-angle (θ = 1.6 − 3°) devices" (p. 5), with no total count.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. Power is given as "P = 0.03 (blue), 0.09, 0.19, 0.37, 0.57, 1 (orange) in units of Pmax" (Fig. 2a caption, p. 3), and lattice temperature runs to 80 K in Fig. 2e; there is one frequency, Pmax has no absolute value, and no range carries a reason.
3. Give the processing steps from raw data to figures, with data and code : Partly. The lock-in "was configured to measure Fourier component Vdm at fdm = fmod − fI, yielding a simple expression for ∆ρTHz" (Methods, p. 6); the ρ0 in Fig. 3b,c and a data or code statement are missing.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Fine-tuning and selection | Tested in part | Devices and datasets counted: part; how shown data were chosen: no; second device or dataset: part | "Figures 2a,b display examples of ∆ρTHz (n) for θ ≈ 2° and θ close to the magic-angle." (p. 3); two magic-angle devices back the photoresistance, one device (1.58°) backs T² below umklapp | State the device count and selection, and show one more 1.6 to 3° device in Fig. 3 form |
| Subtracted offset sets the extracted value (adapted from series-resistance-subtraction: here the residual ρ0 sets the apparent exponent) | Tested in part | ρ0 value and how it was obtained: no; raw data before subtraction: part (Fig. 3a gives raw ρ(ν) at only 4.2, 10, 20 and 50 K) | "Temperature-dependent change in resistivity, ∆ρ = ρ − ρ0, shown for representative ν values" (Fig. 3 caption, p. 4) | Give ρ0, plot raw ρ(T) at the four fillings, and show the local slope d ln(ρ − ρ0)/d ln T as ρ0 varies |
| Lattice heating, bolometric photoresistance (not in library) | Tested in part | Photoresistance against dρ/dT at each gate voltage: part (dρ/dT shown for one filling, Fig. 2c; the comparison is in the SI); electron and lattice rises extracted separately: no (Te is estimated, the lattice rise is not) | "we use terahertz (THz) excitation to selectively raise the electron temperature in TBG while keeping the lattice cold" (abstract, p. 1); MLG control: "This is evident from the data obtained on a sample made of monolayer graphene (MLG)" (p. 4, Fig. 2f) | Bound the channel lattice rise at Pmax, and plot ΔρTHz(n) against dρ/dT(n) for one device |
| Te-dependent screening of charged impurities (not in library) | Not tested (data bear on it) | Screening and energy-averaging estimate at the measured n and T/TF: no; resistivity change against T/TF across densities: no | Smearing is invoked only at the CNP: "THz-induced heating smears out the electronic distribution function, leading to a negative ∆ρTHz at the CNP." (p. 3); Fig. 3b,c hold the data | Estimate the impurity-screening T² term at \|ν\| ≈ 0.1 and 3.8, and replot Fig. 3b,c against T/TF |

A few notes on the rows.

**Lattice heating.** Freitag et al. separate a bolometric photoresponse, caused by lattice
heating through electron-phonon cooling, by comparing it with the measured temperature
coefficient across gate voltage and then extracting electron and lattice temperatures
separately. The sign pattern in your Fig. 2a,b (negative at the CNP, ν = ±4 and ν ≈ 2,
positive in metallic regions) is the sign of dρ/dT, which a warm lattice would also
produce. Your MLG control speaks to hot-electron phonon emission, and at 2 K doped MLG
resistivity barely depends on lattice temperature. A modest lattice rise would therefore give
a small MLG signal too. Mehew et al. report picosecond electron-phonon cooling near the magic
angle, against nanoseconds in graphene, so energy may reach the TBG lattice faster than in
the MLG control. A bound on the channel lattice temperature at Pmax would close this.

**Impurity screening.** Hwang and Das Sarma find a purely electronic, phonon-free
temperature dependence from screened Coulomb impurities. In graphene its leading low-T
correction is quadratic in T/TF, with no e-e current relaxation involved. At |ν| ≈ 0.1 your
Fermi energy is "∼ 20 meV" (p. 5), and Fig. 3b marks TF/2 within the fitted range, so T/TF
is not small there. An estimate of this term at your densities would show how much of the
T² prefactor and of ΔρTHz is left for Eq. 1.

**Small things.** The text cites "Figure 1a" for the ρ(T) data and "Fig. 1b" for the dark and
illuminated ρ(n) (p. 3); these appear as Fig. 1c and 1d in the PDF.

## Questions about devices and data

1. How many TBG devices did you measure in total, and in the 1.6 to 3° range, and how many showed positive photoresistance and T² resistivity below the umklapp threshold?
2. Why were the other devices or datasets set aside, if any were?
3. Which ranges did you measure beyond the ones shown: frequencies other than 0.14 THz, the absolute value of Pmax, lattice temperatures above 2 K for the photoresistance in Fig. 2a,b, and fillings and temperatures for Fig. 3b,c?
4. What does the second-best device look like for the T² claim, for example ρ − ρ0 against T at |ν| ≈ 0.1 in another 1.6 to 3° device?
5. What value of ρ0 did you subtract in Fig. 3b,c, how was it chosen, and does a fit with a free exponent (or the local slope d ln(ρ − ρ0)/d ln T) still give 2 when ρ0 is varied within its uncertainty?
6. How large is the lattice temperature rise in the TBG channel at Pmax, and does ΔρTHz(n) follow dρ/dT(n) times a single temperature rise across all fillings, including where ρ is linear in T?
7. What does ΔρTHz look like in the 1.58° device at |ν| ≈ 0.1 and 3.8, where you report T² resistivity, given that the 2° inset of Fig. 2a shows a negative response near the CNP?
8. Have you estimated the Te-dependent screening of charged impurities at |ν| ≈ 0.1, where your T_F/2 marker in Fig. 3b puts T/T_F near 0.5 at the top of the fitted range?

## Related work

- Freitag, Low, Xia and Avouris 2012, "Photoconductivity of biased graphene", <https://arxiv.org/abs/1202.5342>. Separates photovoltaic and bolometric (lattice heating) photoresponse in biased graphene using the measured temperature coefficient, and extracts electron and lattice temperatures separately.
- Hwang and Das Sarma 2008, "Screening induced temperature dependent transport in 2D graphene", <https://arxiv.org/abs/0811.1212>. Shows a phonon-free, purely electronic temperature dependence from screened Coulomb impurities, quadratic in T/TF at low T in graphene.
- Hubmann et al. 2022, "Infrared photoresistance as a sensitive probe of electronic transport in twisted bilayer graphene", <https://arxiv.org/abs/2207.14223>. Reports sign-alternating photoresistance in TBG at 57.1 THz, captured by a bolometric model of electron and hole gas heating.
- Mehew et al. 2023, "Ultrafast Umklapp-assisted electron-phonon cooling in magic-angle twisted bilayer graphene", <https://arxiv.org/abs/2301.13742>. Finds hot-carrier cooling of a few picoseconds near the magic angle down to 5 K, against nanoseconds in pristine graphene.
- Jaoui et al. 2021, "Quantum critical behavior in magic-angle twisted bilayer graphene", <https://arxiv.org/abs/2108.07753>. Reports linear-in-T resistivity in screened MATBG and Fermi-liquid behavior near charge neutrality, near full filling and away from the magic angle.

Happy to rerun this with the Supplementary Information or the figure data.
