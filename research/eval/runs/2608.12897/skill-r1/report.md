# Lookalike check: Time-domain braiding of non-Abelian anyons at ν = 5/2 (arXiv 2608.12897v1)

*AI only. Written by the lookalike assistant on 2026-10-23 from arXiv version v1, with
lookalike library version 0.4. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your paper is a shot-noise measurement of anyon statistics, at the edge of the
library's scope, so I adapted the anyon-statistics checks and the practice entries, and
added four lookalikes from the literature, marked "(not in library)", each with a paper I opened.

**The claim, as I read it.** In a GaAs device with two etched QPCs 1.4 µm apart, at
10 mK, the excess noise at the detection QPC exceeds ordinary partition noise for a dilute
charged beam (Fig. 2b) and for a dilute upstream neutral beam (Fig. 3b), and both agree
without fitting parameters with time-domain braiding in the PH-Pfaffian order, the neutral
case with the non-Abelian monodromy M_n = 0. Four data sets from three devices show the
same behavior (Figs. S1 to S4).

## Checks a careful reader will look for

1. Show the effect is absent where no braiding is expected, and rule out traps and gate leakage : Partly. "the measured noise SD1 is well described by Eq. (1), leading to the partitioned charge e∗ = e/4 (Fig. 1b)" (p. 3). The single-QPC case behaves ordinarily in the same device; there is no two-QPC run at a filling with no anyons, and no leakage statement.
2. Repeat sweeps to separate reproducible signals from stochastic jumps : Partly. "One of the devices was subsequently thermally cycled, cooled again with a positive gate voltage (0.3V) applied, and remeasured" (p. 16). Repeats within a cooldown, and their scatter, are not shown.
3. Report devices and datasets measured, how many showed the effect, and why others were set aside : Partly. "Three devices were measured" (p. 8), and all four data sets appear in Figs. S1 to S4; devices fabricated and QPC settings tried per device are not stated.
4. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. Bias up to about |e*V_S/2k_BT| = 5 to 6 and the QPC transmissions are shown (Figs. S1 to S4, panels a and e); the magnetic field, gate voltages and any temperature other than 10 mK are not given.
5. Give the processing steps from raw data to figures, with data and code : Partly. Methods give the steps (pp. 8 to 10), and "Source data are provided with this paper." (p. 13), though arXiv v1 carries no ancillary files and no code is linked.

## Lookalikes

| Lookalike | Status | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|
| Fine-tuning and selection of the shown example | Partly addressed | "Figures S1–S4 present four data sets obtained from three separate devices." (p. 16); how the QPC set points and field were chosen is not stated. | Say how set points were found and how many were tried; explain why Figs. 1b and 2b use data set 4 and Fig. 3b uses data set 3 (p. 17). |
| Calibration and normalization moving the extracted value (adapted from series-resistance subtraction) | Partly addressed | "The overall gain of the amplification chain was calibrated using the temperature dependence of the Johnson-Nyquist noise and independently verified by shot-noise measurements of the outermost edge mode at filling factor ν=3 on a separate device." (p. 8); no uncertainty is given for the gain or for T = 10 mK. | Propagate gain and electron-temperature uncertainty into F; the neutral predictions differ by about 15% (2.33 and 2.0, p. 12). Show raw S_D before normalization. |
| Heating at the injection QPC, carried by neutral or charge modes (not in library) | Partly addressed | "we estimate the noise produced by this incoherent heating and find it to be far smaller than the measured noise, thereby ruling out this mechanism" (p. 7); one model, plotted for data set 4 only (Fig. S9), neutral configuration only. | Measure the excess noise against fridge temperature (Bid et al. saw neutral-mode noise fall with temperature and distance); run the heating model for the charged configuration and all data sets. |
| Tunneling charge above e/4 at weak backscattering and low energy (not in library) | Partly addressed | "yielding QPs’ charge e∗ = e/4 (Supplementary Note 1)" (p. 5); the data bear on it; the paper doesn't discuss the detector's low-energy operating point. | Show each detector QPC's single-QPC charge at its detector transmission down to low bias, and what F_charge and F_neutral become with a detector charge of e/2. |
| An Abelian state in the QPC constriction (not in library) | Not addressed | Not discussed. The p. 12 remark on "a potentially non-ideal saddle-point potential" concerns nonuniversal parameters. | Extract each QPC's tunneling exponent from R(V_S) and its temperature dependence, compare it with the δ values in Table 1, and repeat at another QPC confinement. |
| Coulomb coupling to co-propagating channels on Edge2 (not in library) | Not addressed | Not discussed. | Say which channels run along Edge2 between the QPCs; model their coupling over 1.4 µm, or compare a device with a different QPC separation. |

## Questions about devices and data

1. You report three devices measured and four data sets, all shown (p. 8, p. 16). How many devices were fabricated or cooled, and how many QPC settings did you try on each before the ones shown?
2. Nothing appears to be set aside. Were any devices, settings or cooldowns dropped, and why?
3. Which magnetic fields across the 5/2 plateau, QPC transmissions and temperatures did you measure beyond the ones shown?
4. The second-best data sets are in Figs. S1 to S4, which answers the usual question. Why do Figs. 1b and 2b come from data set 4 and Fig. 3b from data set 3 (p. 17)?
5. Did you measure the excess noise at higher fridge temperatures? Braiding predicts a dependence through e*V_S/k_BT, and neutral-mode heating noise can scale differently.
6. What tunneling charge does each QPC show when it is biased directly at the transmission and low bias it has as the detector?
7. How was the electron temperature of 10 mK determined, and what uncertainty do the gain and temperature give on F_charge and F_neutral?
8. What would the theory in Fig. 3b give for an Abelian upstream neutral sector (M_n ≠ 0, for example the 331 order) and with braiding switched off? Showing those curves would show how far the data sit from each.

## Related work

- Bid et al. 2010, "Observation of neutral modes in the fractional quantum Hall regime", <https://arxiv.org/abs/1005.5724>. Injects upstream neutral modes at 5/2 (and 2/3, 3/5) onto a QPC and finds shot noise proportional to the injecting voltage with no net current; at 2/3 that noise falls with temperature and distance.
- Dolev et al. 2010, "Is the charge determined via shot noise measurements unique?", <https://arxiv.org/abs/0911.3023>. Finds the tunneling charge across a QPC at 5/2 well above e/4 at weak backscattering and low temperature and voltage.
- Fu et al. 2016, "Competing ν = 5/2 fractional quantum Hall states in confined geometry", <https://arxiv.org/abs/1611.07359>. Finds QPC tunneling exponents at 5/2 that move between Abelian and non-Abelian values as the confinement is tuned.
- Glidic et al. 2024, "Signature of anyonic statistics in the integer quantum Hall regime", <https://arxiv.org/abs/2401.06069>. Shows a time-domain braiding signal from fractional charges created by Coulomb coupling of co-propagating integer channels.
- Schiller, Oreg and Snizhko 2022, "Extracting the scaling dimension of quantum Hall quasiparticles from current correlations", <https://arxiv.org/abs/2111.05399>. Proposes reading the quasiparticle scaling dimension from thermal tunneling noise at a QPC, which helps separate PH-Pfaffian from anti-Pfaffian.

Happy to rerun this if you share the source data behind Figs. S1 to S4.
