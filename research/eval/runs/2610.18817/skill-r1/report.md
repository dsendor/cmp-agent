# Lookalike check: Single anyons and anyon binding in a quantum Hall dot (arXiv 2610.18817v1)

*AI only. Written by the lookalike assistant on 2026-10-23 from arXiv version v1, with
lookalike library version 0.4. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your device is a fractional quantum Hall dot, outside the library's
superconductor-hybrid core, so I adapted the fractional-charge entries and the even-odd
Coulomb spacing entry to it.

**The claim, as I read it.** Two signals from one graphene QPC device with an embedded
90 nm dot. First, Coulomb resonances at ν = 1/3 and 2/3 with a gate period about a third
of the ν = 1 period, read as e/3 tunneling through a single-anyon dot emptied to Nqp = 0
(Figs. 1h-j, 3). Second, at |Nqp| ≈ 10-20 in the 1/3 quasiparticle regime, an even-odd
spacing that turns into 2e/3 steps as VT is lowered, read as an anyon binding energy at
least as large as the charging energy (Figs. 4e-g).

## Checks a careful reader will look for

1. Map the oscillations in the field and gate plane and say which regime they are in : Partly. "the behavior is consistent with resonant backscattering via a dot tuned through a series of Coulomb blockade resonances corresponding to charge degeneracy within the dot" (p. 3, Fig. 1g); gate maps in Extended Data Figs. 2, 9, 10, field only at four values in Fig. 1j.
2. Show the effect is absent where the exotic state is not expected, and rule out charge traps and gate leakage : Partly. "For the integer quantum Hall state, δ ≈ 250 − 300mV, while at both fillings 1/3 and 2/3 δ is 80 − 100 mV, or approximately three times smaller than the integer case" (p. 3, Fig. 1j); the lever-arm test is at ν = 1 only, and leakage isn't discussed.
3. Repeat sweeps to separate reproducible shifts from stochastic charge jumps : Partly. "measured continuously for 15.5 hours" (Extended Data Fig. 5b, p. 18), at ν = 1; no repeats of the fractional maps.
4. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. "The device was measured during two separate cool downs." (p. 9). Device counts aren't given; Table I's frequencies suggest Fig. 1j mixes both cooldowns and Figs. 3-4 come from the second.
5. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. "Measurement parameters and gate configurations for all panels in the main text are listed in Table I." (p. 9); Extended Data Fig. 11 extends Figs. 4a-d.
6. Give the processing steps from raw data to figures, with data and code : Partly. "The differential conductance was subsequently obtained numerically from the measured current–voltage characteristics using a multipoint derivative." (p. 9); the dip-finding algorithm (Extended Data Figs. 9-10) isn't described, and I found no data or code statement.

## Lookalikes

| Lookalike | Status | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|
| Capacitively coupled side dot or charge trap (charge-trap-fractional-shift), adapted to the period and missing-sector claims | Partly addressed | "the resonances are nearly insensitive to the QPC gates, very weakly tuned by the edge gates, and very strongly tuned by both the center and bottom gate (see Extended Data Fig. 2)" (p. 3); shown at ν = 1. | Repeat the Extended Data Fig. 2 lever-arm maps at ν = 1/3 in the Fig. 4f configuration, and check that the merging lines in Fig. 4f share one VT/Vdot slope with no small jumps. |
| Ordinary orbital (shell) structure giving even-odd spacing (island-states-coulomb-spacing), adapted from hybrid islands | Partly addressed | "Short plateaus or an even/odd pattern in the widths do not imply binding (as they may due to attraction or orbital effects)." (p. 12) | Give the narrowest charge sector you could resolve in Figs. 4f-g, from Te ≈ 110 mK (Extended Data Fig. 3k), the 55 µV bias and the Vdot step, so "absent" carries an upper bound. |
| Apparent pairing from capacitive coupling to a second compressible region (not in library; Liang et al. 2025, Werkmeister et al. 2023) | Partly addressed | "Alternatively, the dot may form a uniform droplet of ν = 2/3 surrounded by the ν = 1/3 bulk. If charge enters via the expansion of the 2/3 − 1/3 edge state, the pairing could be interpreted as a property of the 2/3 − 1/3 edge." (p. 8) | Measure the tunneling charge in the 2e/3 regime in operando, as Liang et al. do, for example by refitting the Extended Data Fig. 3 Luttinger-liquid scaling with e* free on the Fig. 4g data. |
| Non-representative example after fine-tuning (fine-tuning-and-selection) | Partly addressed | "Fig. 4e focuses on a narrow range of gate voltage in which we observed a particularly pronounced even-odd effect" (p. 8); Extended Data Figs. 9-11 widen the gate ranges. | Report how often the missing sector appears across VT, Nqp and both cooldowns, and show the second-best example of the merger. |

## Questions about devices and data

1. How many devices did you fabricate and measure, and how many showed the e/3 resonances and the 2e/3 merger? The Methods mention one device and "two separate cool downs" (p. 9).
2. Why were the others set aside?
3. Which ranges of VT, Vdot and field did you measure beyond those in Table I, in particular VT outside 0.040 to 0.050 V in Fig. 4f, and other Nqp ranges where the merger could recur?
4. What does the second-best dataset look like, for example the ν = 2/3 quasihole regime of Fig. 4d tuned the same way, or the same regime in the first cooldown?
5. Do the merging lines in Fig. 4f keep one slope in the VT and Vdot plane, and do repeated sweeps of that map give the same merger point?
6. What is the narrowest charge sector you could resolve in Figs. 4f-g, given the electron temperature, the 55 µV bias and the Vdot step?
7. In the 2e/3 regime, does a chiral Luttinger-liquid fit with e* left free (Extended Data Fig. 3 fixes it to e/3) return 2e/3 or e/3?
8. For the factor of three in Fig. 1j, how did you check that Cd and α stay the same between the ν = 1 reference at 13.4 T (VT = 0.350 V, Vedge = −4.0 V) and ν = 1/3 at 13.5 T (VT = 0.080 V, Vedge = −1.25 V, Table I), for example from the diamond slopes in Figs. 1g and 1i?

## Related work

- Röösli et al. 2021, "Fractional Coulomb blockade for quasiparticle tunneling between edge channels", <https://arxiv.org/abs/2005.12723>. Extracts e*/e = 0.32 ± 0.03 in a GaAs dot by comparing with filling 2, using two compressible regions.
- Liang et al. 2025, "Single electron interference and capacitive edge mode coupling generates Φ0/2 flux periodicity in Fabry-Perot interferometers", <https://arxiv.org/abs/2502.00124>. A halved period that had been attributed to pairing comes from capacitive edge-mode coupling; e* = 1 is measured in operando.
- Werkmeister et al. 2023, "Strongly coupled edge states in a graphene quantum Hall interferometer", <https://arxiv.org/abs/2312.03150>. Repulsive edge-channel coupling plus charge quantization produces apparent pairing in graphene.
- Frolov et al. 2023, "\"Smoking gun\" signatures of topological milestones in trivial materials by measurement fine-tuning and data postselection", <https://arxiv.org/abs/2309.09368>. In Example 4, a capacitively coupled side dot produces jumps of about 1/3 of a period in a zero-field nanowire dot.
- Henzinger et al. 2026, "Controlled localization of anyons in a graphene quantum Hall interferometer", <https://arxiv.org/abs/2603.11182>. A gate-controlled dot in an interferometer gives phase slips consistent with discrete changes in the number of localized quasiparticles.

Happy to rerun this if you share the figure data, especially the raw Fig. 4f sweeps.
