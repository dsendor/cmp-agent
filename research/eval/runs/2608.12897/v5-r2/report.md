# Lookalike check: Observation of Time-Domain Braiding of Non-Abelian Anyons at ν = 5/2 State (arXiv 2608.12897v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport: ordinary effects that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. Your paper is a shot-noise braiding measurement, which the library covers only through its anyon checks and its selection entry, so I adapted those and added two lookalikes from the literature.

**The claim, as I read it.** A dilute e/4 beam partitioned at a second QPC 1.4 µm away gives excess noise matching parameter-free time-domain braiding predictions for the PH-Pfaffian edge: a charge Fano factor above 1 (your Fig. 2b) and a neutral Fano factor matching the non-Abelian monodromy M_n = 0 (your Fig. 3b). Both come from device C (Fig. 2b second cooldown, Fig. 3b first); Figs. S1 to S4 show four datasets from three devices.

## Checks a careful reader will look for

1. Map the signal against its control parameters and name the regime (adapted to bias, dilution and temperature) : Partly. "In both configurations, the experimental Fano factors approach the corresponding PH-Pf theoretical values at large source voltages" (p. 17); dilution and temperature sit at one value per dataset.
2. Show the effect is absent where the exotic state is not expected (adapted: the same two-QPC noise at a filling with no anyons) : Not done. The trivial line in Fig. 2b is computed; the ν = 3 noise on a separate device serves gain calibration (p. 8).
3. Repeat the measurement to separate reproducible signal from switching (adapted) : Partly. "One of the devices was subsequently thermally cycled, cooled again with a positive gate voltage (0.3V) applied, and remeasured" (p. 16).
4. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Done. "Figures S1–S4 present four data sets obtained from three separate devices" (p. 16), and "The remaining data sets, shown in Figs. S2–S4, exhibit the same overall behavior" (p. 17).
5. Disclose the full parameter ranges measured and why each shown range was chosen : Not done. Field and plateau position, QPC gate settings, and ranges beyond the figures aren't given.
6. Give the processing steps from raw data to figures, with data and code : Partly. Methods give the steps, and "Source data are provided with this paper" (p. 13); arXiv v1 carries no data files or theory code.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Fine-tuning and selection of the shown data | Tested in part | Devices and datasets measured, and how many showed the effect: all; how the shown data were chosen: no; a second device or dataset shown: all | "for one representative device (corresponding measurements from other devices presented in Supplementary Note 1)" (p. 5) | Say why data set 4 feeds Figs. 1b and 2b and data set 3 feeds Fig. 3b, and list every QPC tuning and cooldown measured. |
| Incoherent heating of the upstream neutral mode (not in library) | Tested in part | Measured noise compared with a quantitative heating estimate: part (data set 4 only); apparent temperature of the detection QPC checked with the neutral beam on: no | "For both edges, the heating model underestimates the measured excess noise by roughly a factor of two over the relevant voltage range." (Fig. S9, p. 39) | Run the Note 3 model on data sets 1 to 3, and extract the detection QPC's noise temperature from the rounding near zero bias with QPC1 biased, as Bid et al. did. |
| Bunched tunneling charge at weak backscattering (not in library) | Tested in part | Charge of each QPC at its detection transmission and temperature: part (measured in its injector role, at a different transmission in some datasets); charge followed as transmission and temperature change: no | "Each figure includes measurements of the reflection probabilities of quantum point contacts (QPCs), the fractional quasiparticle (QP) charge, and time-domain braiding" (p. 16) | Measure each QPC's shot-noise charge at the gate setting used for detection, then over transmissions of about 0.7 to 0.95 and a few temperatures. |

## Questions about devices and data

1. Your Methods and Note 1 report three devices and four datasets, all shown. Were other devices fabricated or cooled down, for example ones with unstable QPCs, and how many showed the excess noise?
2. If any devices, cooldowns or QPC tunings were set aside, why?
3. Which ranges did you measure beyond the ones shown: field across the 5/2 plateau, QPC transmissions outside about 0.75 to 0.95, bias beyond |e*V_S/2k_BT| of about 6, temperatures above 10 mK?
4. What does the tuning that agrees least with the PH-Pf curves look like, and did any tuning give Fano factors outside both predictions?
5. Were the QPC gate voltages the same in both configurations? In Fig. S1, R_QPC1 is about 0.2 in panel (a) and about 0.1 in panel (e), so QPC1's e/4 charge in panel (f) comes from a different transmission than its detection role in panel (c).
6. Could you run the Note 3 heating model on data sets 1 to 3 (Fig. S9 uses set 4; Fig. 3b uses set 3), and say how it changes if more of the dissipated power enters the neutral sector than the central-charge split assumes?
7. How did you determine the 10 mK electron temperature, and how far do the curves in Figs. 2b and 3b move for a few mK of error? Did you vary the dilution at the injection QPC, whose effect your theory predicts?
8. What would an Abelian 5/2 order with an upstream neutral mode, or no braiding, predict for F_neutral in Fig. 3b? Both curves shown carry M_n = 0.

## Related work

- Lee et al. 2022, "Partitioning of Diluted Anyons Reveals their Braiding Statistics", <https://arxiv.org/abs/2209.15461>. The same method at ν = 1/3: autocorrelation agreeing with time-domain braiding phase 2π/3, with no fitting parameters.
- Lee and Sim 2022, "Non-Abelian Anyon Collider", <https://arxiv.org/abs/2202.03649>. Theory: braiding with an anyon excited at the collider dominates, and the dependence on injection current distinguishes Ising, SU(2)_k and Laughlin anyons.
- Bid et al. 2010, "Observation of neutral modes in the fractional quantum Hall regime", <https://arxiv.org/abs/1005.5724>. Upstream neutral modes at 5/2, 2/3 and 3/5 hitting a QPC produce shot noise proportional to the injecting voltage.
- Dolev et al. 2009, "Is the charge determined via shot noise measurements unique?", <https://arxiv.org/abs/0911.3023>. At 5/2, very weak backscattering and low excitation energy give a tunneling charge well above e/4, attributed to bunching.
- Park et al. 2018, "Noise on complex quantum Hall edges: Chiral anomaly and heat diffusion", <https://arxiv.org/abs/1810.06871>. Theory of noise generated away from the hot spot by ballistic charge and diffusive heat that can travel upstream.

Happy to rerun this if you share the source data behind Figs. S1 to S4.
