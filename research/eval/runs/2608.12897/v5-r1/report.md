# Lookalike check: Time-domain braiding of non-Abelian anyons at ν = 5/2 (arXiv 2608.12897v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. The library is built mostly for hybrid superconductor devices and interferometers, so for this shot-noise experiment I adapted its anyon checks to noise data and added three explanations from the literature, each marked "(not in library)".

**The claim, as I read it.** In a two-QPC GaAs device at ν = 5/2, partitioning a dilute beam of e/4 quasiparticles produces excess noise at the detection QPC. Its charge Fano factor (Fig. 2b) and neutral Fano factor (Fig. 3b) match no-fit predictions for time-domain braiding in the PH-Pf order, and you read the neutral result as braiding of non-Abelian Ising anyons with M_n = 0. Figs. 1b and 2b come from device C, second cooldown (data set 4). Fig. 3b comes from device C, first cooldown (data set 3). Figs. S1 to S4 show all four data sets from devices A, B and C.

## Checks a careful reader will look for

1. Regime map (adapted: the Fano factor shown across bias and dilution, and the regime named) : Partly. You sweep bias in every data set, and "the experimental Fano factors approach the corresponding PH-Pf theoretical values at large source voltages" (p. 17). Dilution stays near R_QPC of 0.1 to 0.2 in each set (Figs. S1 to S4, panels a and e) and is never varied. Bias reaches e*V_S/2k_BT of about 5 to 6.
2. Control regime (adapted: the same two-QPC measurement where no anyons or upstream neutral modes are expected, with leakage ruled out) : Not done. Your ν = 3 measurement calibrates the gain: "independently verified by shot-noise measurements of the outermost edge mode at filling factor ν=3 on a separate device" (p. 8).
3. Repeat measurements : Partly. "One of the devices was subsequently thermally cycled, cooled again with a positive gate voltage (0.3V) applied, and remeasured" (p. 16). Repeated sweeps within one cooldown aren't reported.
4. Device and dataset counts : Done. "Three devices were measured" (p. 8), and "Figures S1–S4 present four data sets obtained from three separate devices" (p. 16). The number fabricated isn't given.
5. Full parameter ranges : Partly. Bias ranges are shown for every data set. The field position within the 5/2 plateau, the QPC gate settings tried, and any temperature other than 10 mK aren't given.
6. Processing, data and code : Partly. Methods give the excess-noise definition, the gain calibration and the current integration, and "Source data are provided with this paper" (p. 13). I found no data or theory code attached to the arXiv record.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Fine-tuning and selection | Tested in part | Devices and datasets measured, and how many showed the effect: all; How the shown data were chosen: part; A second device or dataset shown: all | "Figures 1(b) and 2(b) in the main text were obtained from measurement data set 4 in Fig. S4, whereas Fig. 3(b) was obtained from measurement data set 3 in Fig. S3." (p. 17); the reason for each choice isn't given. | State how the field and QPC settings were chosen for each data set and how many settings were tried; a table of every setting measured would do. |
| Incoherent heating of the upstream neutral mode (not in library) | Tested in part | Heating model compared with the measured noise, every data set and both configurations: part (data set 4, neutral configuration only, Fig. S9); Noise versus distance or temperature: no | "the heating model underestimates the measured excess noise by roughly a factor of two over the relevant voltage range" (Fig. S9, p. 39) | Run the Supplementary Note 3 model on data sets 1 to 3 and on the charged configuration, and draw it in Fig. 3b; noise at a second temperature or QPC separation would test the distance and temperature dependence Bid et al. report. |
| Nonuniversal tunneling exponents (not in library) | Not tested (data bear on it) | Tunneling exponent measured and compared with the scaling dimension used: no | "This difference originates from their distinct total scaling dimensions" (p. 5); R_QPC versus bias is already plotted in Figs. S1 to S4 (a, e). | Compare the bias dependence of R_QPC you already have with the dependence the δ values for PH-Pf and A-Pf imply, or extract δ from a temperature series of the QPC conductance. |
| Coulomb coupling between co-propagating edge channels (not in library) | Not tested (not mentioned) | Inter-channel coupling estimated and included in the prediction: no; Energy distribution of the incoming edge measured at the detection QPC: no | Not discussed. | Estimate the coupling of the ν = 1/2 channel to the outer integer channels over 1.4 µm and include it in the prediction; the two-QPC measurement with an integer channel partitioned would give an ordinary baseline. |

## Questions about devices and data

1. How many devices did you measure, and how many showed the excess noise? You state three measured and show four data sets from them (p. 8, p. 16); how many were fabricated or cooled down in all?
2. Why were the others set aside? If any device or cooldown did not reach a usable 5/2 state or stable QPCs, a line saying so would help.
3. Which ranges did you measure beyond the ones shown: the magnetic field position within the 5/2 plateau, the QPC gate settings and reflection values, temperatures above 10 mK, and bias beyond e*V_S/2k_BT of about 6?
4. What does the second-best device or dataset look like? Your Figs. S1 to S3 answer this for devices A, B and C; thank you for including them.
5. How did you choose the field and QPC settings for each data set, and why does Fig. 2b come from data set 4 and Fig. 3b from data set 3? Does the cross-validation in your Outlook hold within a single data set?
6. What experimental uncertainty sits behind "within experimental uncertainty" (p. 7), and could you add error bars to the Fano factors, especially where F_neutral in Figs. S1h and S4h lies above both predictions? Does "the A-Pf prediction lies closer to the measured values" (p. 17) mean closer to the PH-Pf curve?
7. Fig. 2b shows the trivial baseline F_charge = 1; could Fig. 3b show the matching ordinary baseline (trivial partitioning alone, or the heating model of Fig. S9) for data set 3, and have you run the heating model on data sets 1 to 3 and on the charged configuration?
8. Does the bias dependence of R_QPC in Figs. S1 to S4 (a, e) agree with the scaling dimensions you use, and how strongly could the ν = 1/2 channel couple to the outer integer channels over 1.4 µm?

## Related work

- Bid et al. 2010, "Observation of neutral modes in the fractional quantum Hall regime", <https://arxiv.org/abs/1005.5724>. Detects upstream neutral modes at 5/2 as shot noise at a constriction that grows with the injecting voltage; the excess noise falls with distance and temperature.
- Park, Mirlin, Rosenow and Gefen 2018, "Noise on complex quantum Hall edges: Chiral anomaly and heat diffusion", <https://arxiv.org/abs/1810.06871>. Theory showing noise generated away from the hot spot by heat that diffuses, including upstream; your Supplementary Note 3 builds on this model.
- Rosenow and Halperin 2001, "Nonuniversal behavior of scattering between fractional quantum Hall edges", <https://arxiv.org/abs/cond-mat/0106071>. A smooth edge profile can give nonuniversal tunneling exponents while the shot-noise charge stays the same.
- Glidic et al. 2024, "Signature of anyonic statistics in the integer quantum Hall regime", <https://arxiv.org/abs/2401.06069>. Coulomb coupling between co-propagating integer channels produces fractional charges and a time-domain braiding signal in dilute-beam cross-correlations.
- Ratnakar et al. 2026, "Effect of inter-edge interaction in a quantum Hall collider", <https://arxiv.org/abs/2606.17753>. Theory: interaction between co-propagating modes in a multimode collider changes the time-domain braiding signal and can reverse the sign of the Fano factor for long junctions.

Happy to rerun this if you share the source data behind Figs. S1 to S4.
