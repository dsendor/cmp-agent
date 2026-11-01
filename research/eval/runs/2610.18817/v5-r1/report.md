# Lookalike check: Single anyons and anyon binding in a quantum Hall dot (arXiv 2610.18817v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your measurement sits in the library's fractional-charge family; I applied its side-dot entry to your missing charge sectors as well as to fractional periods, since the physics (an extra charge state that shifts or merges resonances) carries over.

**The claim, as I read it.** In one graphene device, a 90 nm gate-defined dot inside a QPC shows backscattering resonances at ν = 1/3 and 2/3 with about one third of the ν = 1 gate period, read as single e/3 anyons tunneling (Fig. 1h–j, Fig. 3). At |Nqp| ≈ 10–20, tuning VT removes alternate charge sectors so the dot charges in 2e/3 steps, read as an anyon binding energy at least as large as the charging energy (Fig. 4e–g).

## Checks a careful reader will look for

1. Map the oscillations in the field and gate plane and say which regime they are in : Partly. You name the regime from bias spectroscopy, "we again observe periodic conductance suppression dips (teal) associated with Coulomb diamonds in the nonlinear response (Fig. 1i)" (p. 2–3). Your gate-gate maps (Ext. Data Figs. 2, 9, 10) are there; a field-gate map is not.
2. Show the effect is absent where the exotic state is not expected, and rule out charge traps and gate leakage : Partly. "For the integer quantum Hall state, δ ≈ 250 − 300mV, while at both fillings 1/3 and 2/3 δ is 80 − 100 mV" (p. 3), and 1/3 quasiholes stay regular (Fig. 4a). Traps and leakage are not discussed.
3. Repeat sweeps to separate reproducible shifts from stochastic charge jumps : Partly. "Time evolution of the charge-transition position, measured continuously for 15.5 hours" (Ext. Data Fig. 5, p. 18). That is at ν = 1 only, with no repeats shown in the fractional even-odd regime.
4. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. "The device was measured during two separate cool downs." (p. 9). The number of devices fabricated is not given.
5. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. "Measurement parameters and gate configurations for all panels in the main text are listed in Table I." (p. 9), plus extended ranges in Ext. Data Fig. 11. You give a reason for the chosen range only for Fig. 4e.
6. Give the processing steps from raw data to figures, with data and code : Partly. "The differential conductance was subsequently obtained numerically from the measured current–voltage characteristics using a multipoint derivative." (p. 9). There is no data or code statement, and the dip-finding settings are not given.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Charge trap or capacitively coupled side dot | Tested in part | Shifts absent where the exotic state is not expected: all; Gate leakage checked: no; Map of where in two-gate space the shifts occur: all | "We observe an even–odd effect in all panels, although its exact locations depend strongly on the gate voltages." (p. 23, Ext. Data Fig. 10) | Report leakage on all seven gates, and fit every line slope in Fig. 4f and Ext. Data Fig. 10 for a second lever-arm family. |
| Fine-tuning and selection | Tested in part | Devices and datasets measured, and how many showed the effect: part; How the shown data were chosen: part; A second device or dataset shown: part | "Fig. 4e focuses on a narrow range of gate voltage in which we observed a particularly pronounced even-odd effect" (p. 8) | State the devices fabricated and measured, and show the second-best 2e/3 dataset, for example from the first cooldown. |
| Blockaded charge transition (not in library) | Tested in part | Bias dependence of the transport spectrum: all; Magnetic field dependence of the transport spectrum: no; Temperature dependence of the transport spectrum: no | "As VT decreases, neighboring charge-degeneracy lines merge" (p. 7, Fig. 4f), with Fig. 4g bias spectroscopy to ±1.5 mV | Take a temperature and field series at VT = 0.04 V, or count the charge with a sensor. |

A few notes on the table. A side dot that charges in parallel with your dot can make resonances jump or pair up. Your two-gate maps and your regular quasihole spectra already speak to this. A fit of line slopes in Fig. 4f would make that explicit. The fit uses data you already have: one lever-arm family points to a single dot, and a second family would point to a trap.

Your own ν = 1 data show that a real charge transition can vanish from low-bias transport (spin blockade, Fig. 2). At ν = 1/3, orbital or angular-momentum changes between ground states could in principle do the same. The merging lines in Fig. 4f already bear on this: a blockaded line would fade in place, and your lines converge. A temperature or field series at the merged point would close it. The same series would also cover a sector that has shrunk below your resolution.

## Questions about devices and data

1. How many devices did you fabricate and measure, and how many showed the e/3 resonances, the even-odd effect and the 2e/3 regime? Methods describe one device over two cooldowns (p. 9), and the author contributions say "M.V. fabricated the devices" (p. 8).
2. Why were the other devices set aside?
3. Which ranges of VT, Vdot, bias and field did you measure beyond the windows in Table I, and over how much of that space does the 2e/3 periodicity of Fig. 4f appear?
4. What does the second-best dataset of the 2e/3 regime look like? Table I suggests all of Fig. 4 comes from the second (DC) cooldown; did the first cooldown show the even-odd effect or the merging?
5. Did you check gate leakage in the fractional regime, and in Fig. 4f and Extended Data Fig. 10 do all resonance lines share one slope, as a single dot would give, or is there a second family that could come from a nearby trap?
6. Could the missing sector in Fig. 4g be a transition that still happens but is blockaded in transport, as the quasielectron transitions are at ν = 1, or a sector narrower than your resolution? A temperature or field series at VT = 0.04 V, or a charge sensor, would tell.
7. Do the diamond heights and slopes at ν = 1/3 give the same lever arm α and capacitance Cd as at ν = 1? Fig. 1 quotes e∆VDC ≈ 2 meV at ν = 1 and EC = (e/3)∆VDC ≈ 300 µeV at ν = 1/3, and an independent α at each filling would test the fixed-geometry assumption behind the e/3 reading of δ.
8. Was the Fig. 4e alternation reproducible on repeated sweeps at the same settings, and how was the dip-finding algorithm set up for the δ traces, given that Extended Data Fig. 10 notes it "may miss resonances as they emerge"?

## Related work

- Röösli et al. 2020, "Fractional Coulomb blockade for quasiparticle tunneling between edge channels", <https://arxiv.org/abs/2005.12723>. In a 1.4 µm dot near 2/3 and 1/3 it extracts e*/e = 0.32 ± 0.03 by comparing with filling factor 2. Its model has two compressible regions separated by an incompressible stripe.
- Kou et al. 2012, "Coulomb Oscillations in Antidots in the Integer and Fractional Quantum Hall Regimes", <https://arxiv.org/abs/1201.1600>. It uses both field and gate-voltage periods in micron-scale antidots, and finds a tunneling charge of e at ν = 2 and (2/3)e at ν = 2/3.
- Choi et al. 2014, "Robust Electron Pairing in the Integer Quantum Hall Effect Regime", <https://arxiv.org/abs/1409.4427>. Fabry-Perot interferometers at 2 < ν_B < 5 show h/2e periodicity and a shot-noise charge near 2e, tied to interaction with an adjacent edge channel.
- Huettel et al. 2001, "Spin blockade in ground state resonance of a quantum dot", <https://arxiv.org/abs/cond-mat/0109104>. In a dot of about 50 electrons, certain ground-state resonances are suppressed by spin blockade. The authors identify this from the bias, field and temperature dependence.
- Frolov et al. 2023, "Smoking gun signatures of topological milestones in trivial materials by measurement fine-tuning and data postselection", <https://arxiv.org/abs/2309.09368>. In a nanowire dot at zero field, Coulomb blockade patterns jump by about 1/3 of a period. The paper explains the jumps with a capacitively coupled side dot (Example 4).

Happy to rerun this if you share the figure data.
