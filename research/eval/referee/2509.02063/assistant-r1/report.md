# Lookalike check: Reentrant superconductivity in an RF-tuned granular aluminum Josephson array (arXiv 2509.02063v1)

*AI only. Written by the lookalike assistant on 2026-10-25 from arXiv version v1, with lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport: ordinary effects that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. Your paper makes no topological claim, so I adapted the library's entries on missing Shapiro steps and on supercurrent that reappears as a tuning parameter rises, and I added two lookalikes from outside the library, each with a source.

**The claim, as I read it.** In one granular aluminum nanobridge driven at 24.5 MHz, RF power takes the device from superconducting (SC 1) to an insulating zero-bias resistance peak about ten times R_N (Fig. 1a, Fig. S4b). At higher temperature, about 2.1 to 2.2 K, a zero-resistance state (SC 2) reappears at fixed RF power (Figs. 1b, 2a-b, S3), and in field at 2.2 K (Fig. 4c-d). You read SC 2 as Efetov-type screening of the charging energy. The giant Shapiro steps with N_j = 430 (Fig. 3) place the low-temperature data in a single-junction regime.

## Checks a careful reader will look for

I walked the Shapiro checks, adapted to your use of the steps, then the practice checks.

1. Dc V(I) and dV/dI without irradiation, with the switching jump marked against the missing steps : Partly. "Fig. S4: (a) dV/dIb(Ib) measured at opposite current sweep directions in the absence of RF power." (SI p. 19). Fig. 2c also shows the no-RF map. Nobody marks where the missing steps fall on the switching jump.
2. Full frequency and power maps : Partly. "As the frequency decreases, more steps are hidden by the insulator peak, and only higher harmonic steps are visible." (p. 6, Fig. 3a-b). You show power maps at 24.5 MHz (Fig. 1a) and 67.5 MHz (Figs. 3c, S5), and a frequency map only along P_I(f).
3. The same measurement where the effect is not expected (here, with no RF) : Done. "For comparison, Fig. 2c shows measurements taken without RF power, displaying a conventional Ic(T) dependence without reentrance." (p. 6). Fig. S3b adds the no-RF R(T) trace.
4. Junction parameters measured and tuned on their own : Not done. You estimate E_J/E_C from the RCSJ fit, and the two estimates of Ω differ by "one order of magnitude" (SI Sec. III, p. 16).
5. Devices and datasets measured, how many showed the effect : Not done. "For the nanobridge device presented in the main text" (p. 10) is the only mention of a device count.
6. Full parameter ranges and why each range was chosen : Partly. The figures give their ranges, and one check is "not shown" (SI p. 19). The reasons for the chosen frequency and powers are not given.
7. Processing from raw data to figures, with data and code : Partly. "The voltage is evaluated by numerical integration and linear interpolation of the dV/dIb data in a." (Fig. 3 caption, p. 6). P is defined at the generator output (p. 10). No data or code are released.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Finite-bias resonances that move with temperature or field and raise the switching current (adapted from field-enhanced supercurrent) | Tested in part | Finite-bias dV/dI plotted with the switching current: part (temperature, Fig. 2a-b; not field, Fig. 4c-d); effect followed across RF power (standing in for gate voltage) and other devices: part (power only) | "At T = 2.16 K, the critical current Ic reappears, signaling the onset of a reentrant superconducting phase (SC 2)" (p. 5, Fig. 2a-b) | In Fig. 2b a resistive ridge leaves Ib = 0 near 1.8 K and moves to about 0.2 µA just below SC 2. You could follow it at several powers and show Ib maps in field at 2.2 K. |
| Sharp switching jump that hides the first steps (adapted to the missing first giant Shapiro steps) | Tested in part | Dc switching curve at the same settings: part (no RF, 50 mK only); first steps followed at higher frequency or in field: all (Figs. 3b, 4a-b) | "At a given frequency, the first consecutive Shapiro steps are missing. As the frequency decreases, more steps are hidden by the insulator peak" (p. 6, Fig. 3) | Show up and down sweeps under RF at 24.5 MHz, and mark where the missing steps' voltages fall relative to any jump. |
| Fine-tuning and selection | Not tested (not mentioned) | Devices and datasets counted: no; how shown data were chosen: no; second device shown: no | "For the nanobridge device presented in the main text" (p. 10) | State device and cooldown counts, how 24.5 MHz and -14.25 dBm were picked, and show a second device. |
| RF electron overheating (not in library) | Tested in part | Critical current and steps followed versus RF amplitude for jumps or hysteresis: part (Fig. 1a; P-sweep hysteresis "not shown"); RSJ model with an electron thermal balance: no | "the absence of hysteresis of R over P sweeps for frequencies fRF < 25 MHz (not shown)" (SI p. 19) | Show the P-sweep data, and fit the step evolution with a thermal-balance RSJ model as De Cecco et al. do. |
| Microwave-stimulated superconductivity near Tc (not in library) | Tested in part | Resistive transition with and without RF: part (Fig. S3c at 24.5 MHz; not for the field reentrance); frequency dependence: no | "we also include the R vs. T trace measured without applied RF power, which exhibits a single superconducting transition at a critical temperature of Tc = 2.25 K." (SI p. 18, Fig. S3) | Repeat Fig. S3c at two or three other frequencies. A frequency threshold for SC 2 would point to stimulation. |

A few notes on the rows. Your Fig. S4a already shows a large gap between the switching current (about 7 µA) and the retrapping current (about 1 µA) without RF. That is why the switching-jump row and the overheating row are worth one figure each. De Cecco et al. tie this kind of hysteresis to electron heating. In Fig. S3c the RF traces reach zero resistance at or below the no-RF transition, which is useful evidence for the stimulation row at 24.5 MHz. A frequency series would complete it. The SC 2 window sits within about 0.1 K of Tc, where the contacts' share of the resistance changes. So the RF current that actually reaches the bridge near Tc is worth stating (question 8).

## Questions about devices and data

1. How many grAl nanobridge devices did you measure, and how many showed the insulating peak or the SC 2 dome? Your Methods refer to "the nanobridge device presented in the main text" (p. 10).
2. Why were the others set aside?
3. Which ranges of RF frequency, power, temperature and field did you measure beyond the ones shown, in particular for SC 2 at frequencies other than 24.5 MHz?
4. What does the second-best device or cooldown look like?
5. Which bias sweep direction was used for the RF maps in Figs. 1a, 2 and 3, and are those maps hysteretic, given the large gap between the switching and retrapping currents in Fig. S4a?
6. Could you show the P-sweep data at fRF < 25 MHz described as "not shown" (SI p. 19), and the same check at 67.5 MHz?
7. Could you show dV/dIb versus Ib in field at T = 2.2 K, so the finite-bias features in Fig. 4c-d can be followed next to the reappearing supercurrent?
8. How does the RF current that reaches the bridge change with temperature near Tc, given that P is set at the generator output and the contacts add resistance above Tc (SI Sec. V.B.1)?

## Related work

- Klapwijk and de Visser 2020, "The discovery, disappearance and re-emergence of radiation-stimulated superconductivity", <https://arxiv.org/abs/1911.02793>. A review of microwave-enhanced critical current and Tc in aluminum strips and weak links: an ordinary way for RF to help superconductivity near Tc.
- De Cecco et al. 2016, "Interplay Between Electron Over-Heating and ac Josephson Effect", <https://arxiv.org/abs/1601.04434>. Shows that electron overheating makes dc characteristics hysteretic and reshapes Shapiro steps as the drive amplitude grows.
- Le Calvez et al. 2018, "Joule overheating poisons the fractional ac Josephson effect in topological Josephson junctions", <https://arxiv.org/abs/1803.07674>. An RSJ model with Joule overheating accounts for which Shapiro steps survive.
- Wu et al. 2024, "Ubiquitous missing first Shapiro step in Al-InSb nanosheet Josephson junctions", <https://arxiv.org/abs/2403.07370>. The missing first step coincides with a sharp switching jump and returns at higher power, temperature, field or frequency.
- Bøttcher et al. 2017, "Superconducting, Insulating, and Anomalous Metallic Regimes in a Gated Two-Dimensional Semiconductor-Superconductor Array", <https://arxiv.org/abs/1711.01451>. A gated island array that crosses superconducting, metallic and insulating regimes, with saturating low-temperature resistance.

Happy to rerun this if you share the figure data or a second device.
