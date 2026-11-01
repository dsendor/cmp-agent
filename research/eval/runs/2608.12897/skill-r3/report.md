# Lookalike check: Observation of Time-Domain Braiding of Non-Abelian Anyons at ν = 5/2 State (arXiv 2608.12897v1)

*AI only. Written by the lookalike assistant on 2026-10-23 from arXiv version v1, with
lookalike library version 0.4. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your experiment is shot noise on quantum Hall edges, outside the library's core of
superconducting devices, so I adapted its anyon (`charge`) entries to a noise measurement
and added two lookalikes from outside the library.

**The claim, as I read it.** In two-QPC devices at ν = 5/2, partitioning a dilute beam gives
a charge Fano factor near 1.5 (your Fig. 2b) and a neutral Fano factor near 2.4 (your
Fig. 3b), matched without fitting parameters to time-domain braiding in the PH-Pf order,
with M_n = 0 read as non-Abelian braiding (three devices, Figs. S1 to S4).

## Checks a careful reader will look for

1. Show the effect is absent where no anyons are expected, and rule out charge traps and gate leakage (adapted: a trivial-regime run of the same two-QPC sequence) : Partly. The gain was checked "by shot-noise measurements of the outermost edge mode at filling factor ν=3 on a separate device" (p. 8); the two-QPC sequence isn't run in a trivial regime.
2. Repeat sweeps to separate reproducible effects from stochastic jumps : Partly. "Figures S1–S4 present four data sets obtained from three separate devices." (p. 16), one of them a second cooldown.
3. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. "Three devices were measured" (p. 8); the number fabricated and any set aside aren't given.
4. Disclose the full parameter ranges measured and why each shown range was chosen : Not done. Each dataset shows one bias window (about ±6 in e*V_S/2k_BT); field, temperature and QPC settings explored aren't given.
5. Give the processing steps from raw data to figures, with data and code : Partly. The Methods give the noise subtraction and current integration, and "Source data are provided with this paper." (p. 13); no code is mentioned.

## Lookalikes

| Lookalike | Status | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|
| A representative example picked after tuning (fine-tuning-and-selection) | Partly addressed | "Figures 1(b) and 2(b) in the main text were obtained from measurement data set 4 in Fig. S4, whereas Fig. 3(b) was obtained from measurement data set 3 in Fig. S3." (p. 17); how QPC settings were chosen isn't stated. | Say how each QPC setting and field point was picked, and show both configurations from one dataset side by side. |
| Charge switching near the QPCs (charge-trap-fractional-shift, adapted to noise) | Partly addressed | "This fabrication scheme was adopted to improve device stability, as purely gate-defined QPCs are typically unstable in this heterostructure" (p. 8); the data bear on it; the paper doesn't discuss switching as a noise source. | Transmission switching adds noise growing as the current squared, so show repeated sweeps at one setting, gate leakage, and the Fano factor at the largest bias in all four datasets. |
| Incoherent heating of the upstream neutral mode (not in library) | Partly addressed | "For both edges, the heating model underestimates the measured excess noise by roughly a factor of two over the relevant voltage range." (p. 39, Fig. S9); one model and one dataset. | Run the model on all four datasets and the charged configuration, and vary the assumed length hierarchy and heat split. |
| Coulomb coupling between co-propagating edge channels (not in library) | Not addressed | Not discussed. | Estimate the coupling between the active ν = 1/2 channel and the outer integer channels over L = 1.4 µm; a device with a different QPC separation would test it. |

The two outside rows come from Bid et al. (2010), who saw noise at a constriction from an
injected upstream neutral mode at 5/2, and Ratnakar et al. (2026), who find inter-edge
interaction in a multi-mode collider can change the sign of the Fano factor.

## Questions about devices and data

1. Your Methods say "Three devices were measured" (p. 8), and p. 7 says "Measurements on the other devices show the same behavior". How many two-QPC devices were fabricated or cooled down in total, and how many reached a stable 5/2 plateau with QPCs usable for these measurements?
2. If any devices, cooldowns or QPC settings were set aside, why?
3. Which ranges did you measure beyond the ones shown: QPC reflection settings, magnetic field positions on the 5/2 plateau, temperature, and source bias beyond about ±6 in e*V_S/2k_BT?
4. Figs. 1b and 2b come from data set 4 and Fig. 3b from data set 3 (p. 17), and for data set 1 you note that "the A-Pf prediction lies closer to the measured values" (p. 17). How were the main-text datasets chosen, and what do Figs. 2b and 3b look like for the second-best dataset in each configuration?
5. Could you run the same two-QPC sequence where no anyons are expected (for example partitioning an integer channel at ν = 2 or 3 in the same device), to show that both Fano factors come out at their trivial values with your normalization?
6. What neutral Fano factor would an edge with an Abelian upstream neutral mode (M_n different from 0) predict for your measured R_QPC1(V_S), and how far is it from the data in Fig. 3b? Both curves you show have M_n = 0.
7. How was the 10 mK electron temperature (p. 3) determined, and how far do the theoretical curves in Figs. 2b and 3b move for a 1 to 2 mK change?
8. Fig. S9 compares the heating model with data set 4 only. Does it fall short by a similar factor for data sets 1 to 3 and for the charged-anyon configuration, and how sensitive is it to the length hierarchy of Eq. (S56) and the heat split by central charge in Eq. (S61)?

## Related work

- Lee et al. 2022, "Partitioning of Diluted Anyons Reveals their Braiding Statistics", <https://arxiv.org/abs/2209.15461>. Your method at ν = 1/3, matched to a braiding phase 2π/3 without fitting parameters.
- Lee and Sim 2022, "Non-Abelian Anyon Collider", <https://arxiv.org/abs/2202.03649>. Theory: braiding with an anyon excited at the splitter dominates and distinguishes Ising from Laughlin anyons.
- Bid et al. 2010, "Observation of neutral modes in the fractional quantum Hall regime", <https://arxiv.org/abs/1005.5724>. Injected upstream neutral modes, including at 5/2, produce shot noise at a constriction.
- Glidic et al. 2024, "Signature of anyonic statistics in the integer quantum Hall regime", <https://arxiv.org/abs/2401.06069>. Coupled co-propagating integer channels give fractional charges and a time-domain braiding signal.
- Ratnakar et al. 2026, "Effect of inter-edge interaction in a quantum Hall collider", <https://arxiv.org/abs/2606.17753>. Inter-edge interaction reverses the Fano factor sign at ν = 2/5 for long junctions.

Happy to rerun this if you share the source data for Figs. S1 to S4.
