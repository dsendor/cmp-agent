# Lookalike check: Time-domain braiding of non-Abelian anyons at ν = 5/2 (arXiv 2608.12897v1)

*AI only. Written by the lookalike assistant on 2026-10-23 from arXiv version v1, with
lookalike library version 0.4. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport: ordinary effects that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. Your paper is a shot-noise measurement of anyon braiding. The library mostly covers other kinds of experiment, so I adapted its fractional-charge and practice checks to your setup and added three lookalikes from the quantum Hall noise literature, each marked "not in library".

**The claim, as I read it.** In a two-QPC device at ν = 5/2, the excess noise at the detection QPC gives two results:

- a charge Fano factor above 1 (your Fig. 2b, data set 4);
- a neutral Fano factor (your Fig. 3b, data set 3).

Both match parameter-free predictions for time-domain braiding in the PH-Pf order, and the neutral case reflects the non-Abelian monodromy Mn = 0. Figs. S1 to S4 repeat the comparison for three devices and four datasets.

## Checks a careful reader will look for

1. Map the signal across the field and gate plane and say which regime it is in (adapted from `charge-regime-map`, which is written for interferometers): Not done. The paper gives no magnetic field value and shows neither the ν = 5/2 plateau nor how the noise depends on field.
2. Show the effect is absent where no anyons are expected, and rule out charge traps and gate leakage (`charge-control-regime`): Not done. The baseline Fano factor of 1 for free fermions comes from theory (p. 12). The ν = 3 data were "independently verified by shot-noise measurements of the outermost edge mode" on a separate device (p. 8), and that only calibrates the amplifier gain.
3. Repeat measurements to separate reproducible behavior from one-off changes (`charge-repeat-sweeps`): Partly. "One of the devices was subsequently thermally cycled, cooled again with a positive gate voltage (0.3V) applied, and remeasured" (p. 16).
4. Report the devices and datasets measured, how many showed the effect, and why any were set aside (`report-counts`): Partly. "Three devices were measured, fabricated with QPC gap widths of 1.2 μm (two devices) and 1.3 μm (one device)." (p. 8). The number fabricated, and whether any were set aside, aren't stated.
5. Give the full parameter ranges measured and why each shown range was chosen (`report-ranges`): Not done. The figures show bias up to about |e*VS/2kBT| = 5 or 6, at one temperature (10 mK) and one QPC setting per dataset. Other settings you measured aren't given.
6. Give the processing steps from raw data to figures, with data and code (`report-processing`): Partly. The Methods derive tunneling currents and Fano factors step by step (pp. 8 to 12) and say "Source data are provided with this paper." (p. 13). The arXiv version has no data files or code.

## Lookalikes

| Lookalike | Status | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|
| Fine-tuning and selection | Partly addressed | "Figures S1–S4 present four data sets obtained from three separate devices." (p. 16); how the QPC settings shown were chosen isn't stated. | State how the QPC settings and field were chosen, and what other cooldowns or settings gave. |
| Protocol-parameter sensitivity (adapted: the PH-Pf versus A-Pf call rests on fixed inputs) | Partly addressed | "remains robust against slight variations in the reduction factor or the details of the integration" (p. 28); temperature and bias window aren't varied. | Recompute both predictions on your existing data, varying T, the bias window, and binomial versus Poisson statistics. |
| Incoherent heating of the upstream neutral mode (not in library; Spånslätt et al. 2019) | Partly addressed | "For both edges, the heating model underestimates the measured excess noise by roughly a factor of two over the relevant voltage range." (Fig. S9, p. 39); this covers data set 4 in the neutral configuration only. | Run the heating estimate for all four datasets and for the charged configuration, and give its uncertainty. |
| Renormalized scaling dimensions (not in library; Schiller et al. 2024) | Partly addressed | "Other nonuniversal effects arising from a potentially non-ideal saddle-point potential in the detection QPC are also expected to cancel out" (p. 12); the data bear on it (RQPC versus bias, Figs. S1 to S4, panels a and e); the paper doesn't discuss it. | Extract the scaling dimension from RQPC(VS), and from other temperatures if you have them, then redo the PH-Pf versus A-Pf comparison. |
| Interaction-induced fractionalization among co-propagating channels (not in library; Glidic et al. 2024) | Not addressed | Not discussed. | Measure both configurations on an integer channel of the same device (for example at ν = 2 or 3) to see how big an interaction-induced braiding signal is, and estimate how strongly the ν = 1/2 channel couples to the outer integer channels. |

## Questions about devices and data

1. How many devices did you fabricate and cool down, and how many showed the excess noise? Your Methods (p. 8) and Supplementary Note 1 (p. 16) answer part of this: three devices measured, four datasets, all with the same behavior.
2. Were any devices, cooldowns or QPC settings set aside, and why?
3. Which ranges did you measure beyond the ones shown: QPC reflection settings, magnetic field across the ν = 5/2 plateau (the field value isn't given), temperature, and bias beyond |e*VS/2kBT| ≈ 6?
4. What does the second-best dataset look like? Figs. S1 to S3 show it; why do your Fig. 2b (data set 4) and Fig. 3b (data set 3) come from different datasets, when the outlook rests on their "simultaneous agreement" (p. 7)?
5. How did you determine the 10 mK electron temperature, how far do the PH-Pf and A-Pf predictions in Figs. 2b and 3b move for an error of a few mK, and what uncertainty sits behind "within experimental uncertainty" (p. 7)?
6. Can you extract the scaling dimension from the bias dependence of RQPC (nearly flat in Figs. S1 to S4, panels a and e) and recompute the Fano factors with it?
7. Did you run either two-QPC configuration on an integer channel of these devices, to size any braiding-like signal from interaction between co-propagating channels?
8. The main text says the heating noise is "far smaller than the measured noise" (p. 7) and Fig. S9 says the model "underestimates the measured excess noise by roughly a factor of two" (p. 39); how do these fit together, and is there a heating estimate for the charged configuration?

## Related work

- Lee et al. 2023, "Partitioning of Diluted Anyons Reveals their Braiding Statistics", <https://arxiv.org/abs/2209.15461>. The same dilute-beam autocorrelation method at ν = 1/3; the measured noise matches time-domain braiding with phase 2θ = 2π/3 and no fitting parameters.
- Glidic et al. 2024, "Signature of anyonic statistics in the integer quantum Hall regime", <https://arxiv.org/abs/2401.06069>. Coulomb coupling between two co-propagating integer channels splits electrons into fractional charges, and their dilute beams show a time-domain braiding signal.
- Ratnakar et al. 2026, "Effect of inter-edge interaction in a quantum Hall collider", <https://arxiv.org/abs/2606.17753>. Theory: interactions in a multi-mode collider split the anyon beam into correlated and uncorrelated parts, which can reverse the sign of the Fano factor, as observed at ν = 2/5.
- Schiller et al. 2024, "Scaling tunnelling noise in the fractional quantum Hall effect tells about renormalization and breakdown of chiral Luttinger liquid", <https://arxiv.org/abs/2403.17097>. At ν = 1/3, the scaling dimension extracted from tunnelling noise is heavily renormalized from the naive chiral Luttinger liquid value.
- Spånslätt et al. 2019, "Topological classification of shot noise on fractional quantum Hall edges", <https://arxiv.org/abs/1906.05623>. Theory: in the incoherent regime, heat carried along the edge produces shot noise at a QPC, and its length dependence falls into three classes set by the edge structure.

Happy to rerun this if you share the source data behind Figs. S1 to S4.
