# Lookalike check: Observation of the fractional ac Josephson effect (arXiv 1204.4212v2)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v2, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first.

**The claim, as I read it.** In JJ8, a Nb/InSb/Nb junction with a 40 nm gap irradiated at 3 GHz, the first Shapiro step at 6 µV disappears above an in-plane field (B∥I) of about 2 T while the 12 and 18 µV steps remain (Fig. 3 right, Fig. 4, Fig. S12). You read this doubling of the first step as the fractional ac Josephson effect carried by Majorana modes.

## Checks a careful reader will look for

1. Dc V(I) and dV/dI without rf at the same settings : Partly. Your Fig. 2 shows V(I) at B = 0 "with an abrupt appearance of a finite voltage" (p. 3), and Fig. S9 maps dV/dI in current and field; neither shows the dc curve above 2 T on the 6 µV scale.
2. Full frequency and power maps : Partly. "In Fig. S10 we show V (I) traces measured in the presence of rf field with frequencies f0 = 2, 3 and 4 GHz." (p. 12), where all steps are present; above 2 T only 3 GHz is shown.
3. The same measurement where no topological phase is expected : Done. "At B = 0 we observe steps with the height ∆V = 6 µV, consistent with the Cooper pair tunneling (q = 2e)." (p. 5, Fig. 3, Fig. S11).
4. Junction transparency measured and tuned : Partly. "At V < 0.5 mV the excess current is clearly seen." (Fig. 2 caption, p. 4); no transparency value is extracted or tuned.
5. Devices measured, how many showed the effect, why others were set aside : Not done. All rf data come from JJ8.
6. Full parameter ranges and why each was chosen : Partly. Fig. S12 covers 0 to 3.4 T in one field direction, and Fig. 3 shows "Vrf between 3 and 6 mV in 0.6 mV increments" (p. 4); reasons for these windows are not given.
7. Processing from raw data to figures : Partly. "Quantitative comparison of the width of the Shapiro steps ∆In (Vrf ) for different B extracted from dV /dI data is plotted in Fig. 4." (p. 5); the step-edge criterion, data and code are not given.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Landau-Zener transitions in a highly transparent trivial junction | Tested in part | Junction transparency measured: part (excess current shown, no transparency value); frequency dependence: part (Fig. S10, only where all steps are present); same measurement at zero field: all | "At B = 0 we observe steps with the height ∆V = 6 µV, consistent with the Cooper pair tunneling (q = 2e)." (p. 5); zero field alone can't separate this one, since your estimate of a 30 µeV gap at 2 T (p. 8) makes Landau-Zener transitions likelier at high field. | Extract the transparency from the Fig. 2 excess current at 0 T and above 2 T, and repeat the 2.2 T power series at 2 and 4 GHz. |
| Rounded steps on a bias-dependent resistance | Tested in part | Differential resistance versus bias without irradiation: part (Fig. S9, in current, not at the 6 µV scale); full frequency and power maps: part (power at 0, 1.0, 2.2 T; frequency at one regime); even steps missing in other regimes: part (Fig. S12, all steps gone above 3 T) | "While nonlinear effects can be present at high I and Vrf , we want to stress that the first step at the onset of the normal state is due to phase locking between the external and the Josephson frequencies" (p. 5) | Replot the Fig. S9 data as dV/dI against voltage at 2.2 T with 6 µV marked, and add a full dV/dI(I, Vrf) map at 2.2 T like Fig. 3 (left). |
| Switching jump hiding the first step | Tested in part | Dc switching curve at the same settings: part (B = 0 only, Fig. 2); first step followed as the jump softens: part (power at 2.2 T, Fig. 4; no temperature or frequency series) | "For B > 2 T the step at 6 µV vanishes at low Vrf , and re-appears at high Vrf > 10 mV for B = 2.2 T." (p. 5, Fig. 4) | Show the dc V(I) at 2.2 T without rf, sampled densely near switching, and follow the 6 µV step with temperature and frequency. |
| Accidental zero-energy crossing at phase pi in a transparent junction | Not tested (not mentioned) | Transparency or density tuned through the crossing: no | Not discussed. | Compare rf data from junctions with different gaps (20 to 120 nm), each with its transparency from the excess current. |
| Quasi-Majorana states from smooth confinement (not separated, trivial) | Not tested (not mentioned) | Bulk gap closing and reopening in nonlocal conductance: no; correlated zero modes at both ends: no | Not discussed. | Track the induced gap from the Fig. 2 (right) conductance through 2 T for a closing and reopening; Vuik et al. (https://arxiv.org/abs/1806.02801) show these states can give a 4pi-periodic current. |
| Fine-tuning and selection of the shown example | Tested in part | Devices and datasets measured, and how many showed the effect: no; how the shown data were chosen: no; a second device or dataset: part (several JJ8 field and power series, one device) | "with gaps ranging from 20 to 120 nm in different devices" (p. 2) | State how many junctions were measured under rf and how many showed the doubling, and show the second-best one. |

## Questions about devices and data

1. How many devices did you measure under rf, and how many showed the doubled first step? The text names JJ6, JJ7 and JJ8 and gaps "ranging from 20 to 120 nm in different devices" (p. 2); the Shapiro data come from JJ8.
2. Why were the others set aside?
3. Which ranges of field (magnitude and direction), rf frequency, rf power and temperature did you measure beyond the ones shown, and over how many cooldowns? For example, why Vrf between 3 and 6 mV for Fig. 3 (right)?
4. What does the second-best device or dataset look like?
5. What does the dc V(I) of JJ8 at B = 2.2 T look like without rf, on the microvolt scale: does the switching jump span 0 to 6 µV, and does the return of the 6 µV step above Vrf = 10 mV coincide with that jump softening?
6. Did you measure Shapiro steps at 2 or 4 GHz above 2 T, and does the first step stay missing there?
7. What transparency do you extract from the excess current in Fig. 2, at zero field and above 2 T, and do junctions with other gap widths show the same doubling?
8. Did you apply field along the spin-orbit field (perpendicular to the current), where your model expects no topological phase, and if so, is the 6 µV step present there above 2 T?

## Related work

- Domínguez, Hassler and Platero 2012, "Dynamical detection of Majorana fermions in current-biased nanowires", <https://arxiv.org/abs/1202.0642>. Theory of current-biased Shapiro steps: even steps dominate over a wide range, with extra odd and fractional steps.
- Sau, Berg and Halperin 2012, "On the possibility of the fractional ac Josephson effect in non-topological conventional superconductor-normal-superconductor junctions", <https://arxiv.org/abs/1206.4596>. A conventional SNS junction can show a half-frequency ac Josephson signal, and similar Shapiro features, through Landau-Zener processes.
- Le Calvez et al. 2018, "Joule overheating poisons the fractional ac Josephson effect in topological Josephson junctions", <https://arxiv.org/abs/1803.07674>. Bi2Se3 junctions missing only the first step; Joule overheating accounts for the surviving higher odd steps.
- Galaktionov and Zaikin 2021, "Fractional Shapiro steps without fractional Josephson effect", <https://arxiv.org/abs/2107.05293>. Trivial, highly transparent weak links reproduce missing Shapiro steps.
- Elfeky et al. 2022, "Evolution of 4π-periodic Supercurrent in the Presence of In-plane Magnetic Field", <https://arxiv.org/abs/2210.06502>. Missing odd steps in trivial Al-InAs junctions reappear at a crossover in-plane field, with a field-angle anisotropy.

Happy to rerun this if you share the dc V(I) and the dV/dI(I, Vrf) data above 2 T.
