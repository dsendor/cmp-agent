# Lookalike check: Observation of the fractional ac Josephson effect: the signature of Majorana particles (arXiv 1204.4212v2)

*AI only. Written by the lookalike assistant on 2026-10-23 from arXiv version v2, with
lookalike library version 0.4. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first.

**The claim, as I read it.** In one Nb/InSb/Nb junction, JJ8 (40 nm gap), irradiated at
f0 = 3 GHz at 20 mK, the first Shapiro step at 6 µV disappears for in-plane fields above
about 2 T while the 12 and 18 µV steps survive to about 3 T (Fig. 3 right, Fig. 4,
Fig. S12). You read this doubling of the first step as the 4π-periodic fractional ac
Josephson effect from Majorana modes.

## Checks a careful reader will look for

1. dc V(I) and dV/dI without rf at the same settings, marking the switching jump and resistance peaks : Partly. Fig. 2 shows the dc curve at B = 0, which "exhibits a clear supercurrent region (V = 0), with an abrupt appearance of a finite voltage" (p. 3), and Fig. S9 maps dV/dI against I and B; neither resolves 0 to 12 µV at B > 2 T.
2. Show full frequency and power maps : Partly. Power maps cover 0 to 3.4 T (Fig. S12), and "In Fig. S10 we show V (I) traces measured in the presence of rf field with frequencies f0 = 2, 3 and 4 GHz" (p. 12); Fig. S10 gives no field, and the field series is at 3 GHz only.
3. The same measurement where no topological phase is expected : Partly. "At B = 0 we observe steps with the height ∆V = 6 µV, consistent with the Cooper pair tunneling (q = 2e)." (p. 5); there is no control junction and no second field direction.
4. Measure the junction transparency and tune it : Partly. "This excess current is a signature of Andreev reflection" (p. 5, Fig. 2 right); it isn't converted to a transparency or tuned.
5. Devices and datasets measured, how many showed the effect, why others were set aside : Not done. JJ6 and JJ7 appear only in the Tc data (Fig. S8); the rf data are all from JJ8.
6. Full parameter ranges measured, and why each shown range was chosen : Partly. "A detailed field dependence of step evolution is given in Fig. S12" (p. 14); field direction, temperature and the frequency range at high field aren't given.
7. Processing steps from raw data to figures, with data and code : Partly. "n-th step width ∆In is extracted from the dV /dI data" (Fig. S11 caption, p. 13); data and code aren't given.

## Lookalikes

| Lookalike | Status | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|
| Switching jump hides the first step in the blind region | Partly addressed | "Indeed, we observe no hysteresis for Vrf > 1.8 mV." (p. 5), shown for B = 0. | Show dc and low-power V(I) at 2.1 to 2.9 T at µV resolution; your note that the 6 µV step "re-appears at high Vrf > 10 mV for B = 2.2 T" (p. 5) is worth a temperature series too. |
| Rounded steps on a bias-dependent resistance | Partly addressed | "While nonlinear effects can be present at high I and Vrf" (p. 5); Fig. 2 right gives dI/dV at 0 and 3 T on a mV scale. | Plot dV/dI against V without rf at B > 2 T over 0 to 20 µV, and repeat the field series at 4 GHz or above. |
| Landau-Zener transitions in a transparent, trivial junction | Partly addressed | "At B = 0 we observe steps with the height ∆V = 6 µV, consistent with the Cooper pair tunneling (q = 2e)." (p. 5) | Extract transparency from the excess current against B (Fig. 2 inset), and measure the missing step's frequency dependence at B > 2 T. |
| Accidental zero-energy crossing at phase π in a transparent junction | Partly addressed | "The product RN Ic ≈ 1 mV> 2∆ indicates that JJ8 is in a clean limit" (p. 3); the data bear on it; the paper doesn't discuss it. | Compare JJ6 and JJ7 (20 and 30 nm gaps) under rf, since gap length sets transparency in a device with no gate. |
| Fine-tuning and selection | Partly addressed | "A detailed field dependence of step evolution is given in Fig. S12" (p. 14); device counts are absent. | State how many junctions were measured under rf and show the second-best one. |
| Period doubling from the circuit environment (shunt, capacitance, wiring inductance) (not in library) | Not addressed | Not discussed; your substrate shunt estimate (p. 3) is a start, and I picked the weaker status because it doesn't test the mechanism. | Model JJ8 with its shunt, capacitance and lead inductance (RCLSJ), per Liu et al. 2024, and check whether it removes the first step at the B > 2 T parameters. |
| Landau-Zener flips of a resonant impurity level next to a transparent channel (not in library) | Not addressed | Not discussed. | Sau and Setiawan propose Shapiro steps at low frequency (≲ 50 MHz) as the test; any frequency series at B > 2 T would help. |

## Questions about devices and data

1. How many junctions did you measure under rf, and how many showed the missing 6 µV step?
2. Why were the others set aside?
3. Which ranges of field direction, temperature, rf frequency and rf power did you measure beyond the ones shown?
4. What does the second-best junction or dataset look like?
5. At 2.1 to 2.9 T, what do the dc V(I) and dV/dI look like without rf at µV resolution, and does the 0 to 12 µV window fall inside a voltage jump?
6. At which field was Fig. S10 taken, and does the first step stay missing above 2 T at 2 and 4 GHz?
7. What are the junction capacitance and the lead inductance, and does a junction model with your measured shunt reproduce the field dependence of the first step?
8. Did you measure with the in-plane field along Bso, where your Fig. 1c picture expects no topological phase, and can you show the dc SQUID data that give "only 2π periodicity" (p. 2)?

## Related work

- Sau and Setiawan 2016, "Detecting topological superconductivity using low-frequency doubled Shapiro steps", <https://arxiv.org/abs/1609.00372>. An impurity level weakly coupled to a transparent channel gives a fractional ac Josephson effect through Landau-Zener processes; low-frequency doubled steps separate it from Majorana modes.
- Galaktionov and Zaikin 2021, "Fractional Shapiro steps without fractional Josephson effect", <https://arxiv.org/abs/2107.05293>. Trivial, highly transparent weak links show missing Shapiro steps at some intensities and frequencies.
- Elfeky et al. 2022, "Evolution of 4π-periodic Supercurrent in the Presence of In-plane Magnetic Field", <https://arxiv.org/abs/2210.06502>. Trivial missing odd steps in Al-InAs junctions reappear at a crossover in-plane field, with a field-angle anisotropy set by spin-orbit coupling.
- Liu et al. 2024, "Period-doubling in the phase dynamics of a shunted HgTe quantum well Josephson junction", <https://arxiv.org/abs/2408.06119>. Parasitic wiring inductance drives period doubling and emission at fJ/2; first and third steps go missing in one circuit, and a circuit without the wirebond inductance shows conventional steps.
- Xu et al. 2025, "Intrinsic Non-linearity of Josephson Junctions as an Alternative Origin of the Missing First Shapiro Step", <https://arxiv.org/abs/2510.20130>. In Al/WTe2 junctions the nonlinear I-V removes the first step through switching jumps, with zigzag step boundaries as a diagnostic.

Happy to rerun this if you share the figure data or the high-field dc sweeps.
