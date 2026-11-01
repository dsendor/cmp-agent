# Lookalike check: Single anyons and anyon binding in a quantum Hall dot (arXiv 2610.18817v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Most of the library covers superconducting hybrids. The entries for fractional charge in quantum dots and quantum Hall devices apply here, and I added one lookalike from outside the library.

**The claim, as I read it.** There are two signals. First, Coulomb blockade resonances of a 90 nm graphene quantum Hall dot at ν = 1/3 and 2/3 sit about three times closer in Vdot than at ν = 1 (Fig. 1h–j). You read this as e/3 tunneling, with the dot calibrated down to Nqp = 0 (Fig. 3, Extended Data Fig. 6). Second, for 1/3 quasiparticles at |Nqp| ≈ 10–20, an even-odd pattern loses its weak charge sectors as VT is lowered (Fig. 4e–g). You read this as anyon binding with EB > EC. All data come from one device over two cooldowns.

## Checks a careful reader will look for

1. Map the oscillations in the field and gate plane and say which regime they are in : Partly. You name the regime ("transport is governed by the physics of fractional Coulomb blockade", p. 2) and give spacings at 5, 8.97, 13.4 and 13.5 T (Fig. 1j). There is no field versus Vdot map.
2. Show the effect is absent where the exotic state is not expected, and rule out charge traps and gate leakage : Partly. "For the integer quantum Hall state, δ ≈ 250 − 300mV, while at both fillings 1/3 and 2/3 δ is 80 − 100 mV" (p. 3), and the gate maps of Extended Data Figs. 2, 9 and 10 place the dot. Gate leakage isn't reported.
3. Repeat sweeps to separate reproducible shifts from stochastic charge jumps : Partly. You show a 15.5 hour series at ν = 1 (Extended Data Fig. 5) and temperature series at 1/3 (Extended Data Figs. 3 and 7g). No repeats are shown for Fig. 4e–g.
4. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. "The device was measured during two separate cool downs." (p. 9). The number of devices fabricated and measured isn't given.
5. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. Table I (p. 10) lists the window of every main-text panel, and Extended Data Fig. 11 extends Fig. 4a–d. The ranges explored beyond these aren't stated.
6. Give the processing steps from raw data to figures, with data and code : Partly. "The differential conductance was subsequently obtained numerically from the measured current–voltage characteristics using a multipoint derivative." (p. 9). No data or code release is mentioned.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Integer charges in a nearby charge trap or side dot, capacitively coupled to the dot | Tested in part | Shifts absent where the exotic state is not expected: all (ν = 1 in Fig. 1j; regular spectra in Fig. 4a,b); Gate leakage checked: no; Map of where in two-gate space the shifts occur: all (Extended Data Figs. 2, 9, 10; Fig. 4f) | "Variations in Vqpc and Vedge have little effect on the resonance positions, consistent with a dot confined by the saddle-point potential surrounding the etched hole." (p. 15, Extended Data Fig. 2) | Report leakage on all seven gates at the Fig. 4 settings. Look in the Extended Data Fig. 10 maps for a second set of lines with a different lever arm, which would mark a second charging region. |
| A non-representative example picked after fine-tuning | Tested in part | Devices and datasets measured, and how many showed the effect: part; How the shown data were chosen: part; A second device or dataset shown: part (several gate settings, one device) | "Fig. 4e focuses on a narrow range of gate voltage in which we observed a particularly pronounced even-odd effect" (p. 8) | State the device count. Show how often the merged 2e/3 regime appears across the gate space of Extended Data Fig. 10. |
| Charge transitions too weakly coupled to show in transport (not in library; Elzerman et al., https://arxiv.org/abs/cond-mat/0212489) | Not tested (data bear on it) | Charge state read out independently of transport (charge detector): no | "As VT decreases, neighboring charge-degeneracy lines merge" (p. 7, Fig. 4f) | From the Fig. 4f data, plot the weak sector's width and the dip depth of both bounding lines against VT. A width that shrinks to zero while both lines stay visible separates a merge from a line that fades out. |

Your strongest data against the charge-trap reading are already in the paper. At ν = 1 you measure the integer spacing at a matched field (13.4 T against 13.5 T in Fig. 1j). The dip spacings for 1/3 quasiholes are "independent of the gate voltages" (Extended Data Fig. 9, p. 22). For the binding claim, the even-odd locations "depend strongly on the gate voltages" (Extended Data Fig. 10, p. 23). That is where a coupled second region, or a weakly coupled transition, would show up. A short analysis of the Fig. 4f data would help readers most here.

## Questions about devices and data

1. You present one device over two cooldowns ("The device was measured during two separate cool downs.", p. 9), and the author contributions mention "the devices" (p. 8). How many devices did you fabricate and measure, and how many showed fractional Coulomb blockade and the even-odd pattern?
2. Why were the other devices set aside?
3. Which ranges of VT, VBG, Vqpc, Vedge and magnetic field did you measure beyond Table I and Extended Data Figs. 9 to 11, and in how much of that space does the merged 2e/3 regime of Fig. 4g appear?
4. What does the second-best example of the merging in Fig. 4f look like, for example at another |Nqp| range, in the other cooldown, or for 2/3 quasiholes?
5. Table I lists Fig. 1h as "νbulk = 2/5, νdot = 1/3" (p. 10), while the text says "For νedge ≈ νbulk = ν = 1/3, Vdot has no measurable effect on the conductance" (p. 3). Which bulk filling applies to Fig. 1h–j and Fig. 4a, and does it change the e/3 reading of the spacing?
6. Did you check leakage on all seven gates at the Fig. 4 settings, and did you repeat the Fig. 4e–g sweeps to show the merging recurs at the same VT?
7. The e/3 assignment from the spacing ratio rests on "Assuming these phenomenological parameters are determined primarily by geometry, and therefore ignoring any dependence on Nqp or ν" (p. 3). Did you measure the magnetic-field period of the resonances at fixed gates, which would give the tunneling charge without that assumption?
8. Could a transition with weak edge-to-dot coupling go unseen in the merged regime? You note the coupling can be "too small to resolve the backscattering current" (p. 5) and that the dip finding "may miss resonances as they emerge" (Extended Data Fig. 10, p. 23). Does the weak sector's width in Fig. 4f shrink to zero while both lines stay visible?

## Related work

- Kou, Marcus, Pfeiffer and West 2012, "Coulomb Oscillations in Antidots in the Integer and Fractional Quantum Hall Regimes", <https://arxiv.org/abs/1201.1600>. Assigns the tunneling charge from both field and gate-voltage periods in micron-scale antidots, finding e at ν = 2 and (2/3)e at ν = 2/3.
- Röösli et al. 2020, "Fractional Coulomb blockade for quasiparticle tunneling between edge channels", <https://arxiv.org/abs/2005.12723>. Models a 1.4 µm quantum Hall dot as two compressible regions separated by an incompressible stripe, and extracts e*/e = 0.32 ± 0.03 by comparing with ν = 2.
- Choi et al. 2014, "Robust Electron Pairing in the Integer Quantum Hall Effect Regime", <https://arxiv.org/abs/1409.4427>. Reports h/2e Aharonov-Bohm periodicity and an interfering charge near 2e in Fabry-Perot interferometers, tied to interaction with an adjacent edge channel.
- Frigeri, Scherer and Rosenow 2017, "Subperiods and apparent pairing in integer quantum Hall interferometers", <https://arxiv.org/abs/1709.04504>. A model with an interfering edge, a non-interfering edge and the bulk gives halved periods through alternating charge addition to the two edges, and finds no evidence that pair tunneling matters.
- Frolov et al. 2023, "\"Smoking gun\" signatures of topological milestones in trivial materials by measurement fine-tuning and data postselection", <https://arxiv.org/abs/2309.09368>. Shows that confinement and charge dynamics in trivial nanostructures, fine-tuned and selected, reproduce accepted signatures that include fractionalized particles.

Happy to rerun this if you share the figure data behind Fig. 4f and Extended Data Fig. 10.
