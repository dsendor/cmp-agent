# Lookalike check: Single anyons and anyon binding in a quantum Hall dot (arXiv 2610.18817v1)

*AI only. Written by the lookalike assistant on 2026-10-23 from arXiv version v1, with
lookalike library version 0.4. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your paper is Coulomb blockade spectroscopy of a quantum Hall dot, so I used the
library's fractional-charge entries and adapted its hybrid-island even-odd entry to your
anyon dot.

**The claim, as I read it.** In one graphene QPC with an embedded 90 nm gate-defined dot,
Coulomb resonances at ν = 1/3 and 2/3 with a gate spacing about one third of the ν = 1
spacing (Fig. 1h to 1j) are read as e/3 tunneling, down to the last quasiparticle (Fig. 3).
At |Nqp| ≈ 10 to 20, alternating charge-sector widths for ν = 1/3 quasiparticles that merge
into 2e/3 steps as VT is lowered (Fig. 4e to 4g) are read as anyon binding with EB > EC.

## Checks a careful reader will look for

1. Map the oscillations in the field and gate plane and say which regime they are in : Partly. "the behavior is consistent with resonant backscattering via a dot tuned through a series of Coulomb blockade resonances" (p. 3); Vdot is mapped against VT, VB, Vqpc, Vedge and D (Extended Data Figs. 2, 9, 10), field only at fixed values (Table I).
2. Show the effect is absent where the exotic state is not expected, and rule out charge traps and gate leakage : Partly. "For νedge ≈ νbulk = ν = 1/3, Vdot has no measurable effect on the conductance" (p. 3), and ν = 1 gives the threefold spacing (Fig. 1j); gate leakage isn't reported.
3. Repeat sweeps to separate reproducible features from stochastic charge jumps : Partly. "Time evolution of the charge-transition position, measured continuously for 15.5 hours." (Extended Data Fig. 5, p. 18), at ν = 1 only; none is shown for Fig. 4f.
4. Report devices and datasets measured, how many showed the effect, and why others were set aside : Partly. "The device was measured during two separate cool downs." (p. 9); the device count isn't stated.
5. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. "Measurement parameters and gate configurations for all panels in the main text are listed in Table I." (p. 9); the range explored around Fig. 4e and 4f isn't given.
6. Give the processing steps from raw data to figures, with data and code : Partly. "The differential conductance was subsequently obtained numerically from the measured current–voltage characteristics using a multipoint derivative." (p. 9); the offset calibration and dip-finding algorithm aren't described, and I found no data or code statement.

## Lookalikes

| Lookalike | Status | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|
| Integer charges in a nearby trap or side dot (charge-trap-fractional-shift) | Partly addressed | "To ensure that the dot is in the intended location, we track the response of the charge degeneracy points as a function of different gate voltages." (p. 3; Extended Data Fig. 2) | Repeat the Fig. 4f VT sweep in both directions and over hours at ν = 1/3, and report gate leakage; stochastic jumps would not repeat. |
| Ordinary confined (orbital) states giving even-odd spacing (island-states-coulomb-spacing, adapted) | Partly addressed | "We note that the disappearance of a charge sector places a finite lower bound on the strength of attraction: it implies EB > EC" (p. 8); DMRG covers only Nqp up to 5. | Show whether the merging in Fig. 4f recurs at the same Nqp across the gate settings of Extended Data Fig. 10 and at a second field. |
| A non-representative window picked after tuning (fine-tuning-and-selection) | Partly addressed | "Fig. 4e focuses on a narrow range of gate voltage in which we observed a particularly pronounced even-odd effect" (p. 8) | Report how many VT sweeps like Fig. 4f you took, how many showed a vanishing sector, and show the second-best. |
| Capacitive coupling to an isolated inner edge or puddle, giving apparent pairing (not in library) | Partly addressed | "As VT decreases, neighboring charge-degeneracy lines merge, evolving from the alternating spacings observed in e to a charging periodicity corresponding to 2e/3." (Fig. 4f, p. 7); the data bear on it; the paper doesn't discuss it. | Check whether all lines in Fig. 4f share one slope, look for a second slope or anticrossings, and measure the tunneling charge in the 2e/3 regime (Fig. 4g diamond height). |

## Questions about devices and data

1. How many devices did you fabricate and measure, and how many showed the e/3 resonances and the 2e/3 steps? The contributions say "M.V. fabricated the devices" (p. 8).
2. If other devices were measured, why were they set aside?
3. Which ranges of field, VT and Vdot did you measure beyond those in Table I, in particular around the VT window of Fig. 4f?
4. What does the second-best example of a vanishing charge sector look like, for instance at another gate configuration from Extended Data Fig. 10?
5. Are the merging lines in Fig. 4f the same on repeated sweeps and in both sweep directions, and did you measure gate leakage at ν = 1/3?
6. In Fig. 4f, do all charge-degeneracy lines share one slope, or do you see a second slope or anticrossings that would point to a second compressible region? What diamond height do you find in Fig. 4g?
7. Fig. 1j assumes lever arm and capacitance "determined primarily by geometry" (p. 3), and the Luttinger fits fix "the quasiparticle charge fixed to e∗ = e/3" (Extended Data Fig. 3, p. 16). Does a fit with e* free return e/3, and what ∆VDC lies behind "EC = 3e ∆VDC ≈ 300 µeV" (Fig. 1, p. 2)?
8. How many gate windows did you scan before choosing the "particularly pronounced even-odd effect" of Fig. 4e (p. 8), and could you share the data and the dip-finding code behind Extended Data Figs. 9 and 10?

## Related work

- Liang et al. 2025, "Single electron interference and capacitive edge mode coupling generates Φ0/2 flux periodicity in Fabry-Perot interferometers", <https://arxiv.org/abs/2502.00124>. A halved flux period at ν = 2 and 3 traced to capacitive coupling between isolated edge modes and the interfering edge, with e* = 1.
- Frigeri, Scherer and Rosenow 2017, "Subperiods and apparent pairing in integer quantum Hall interferometers", <https://arxiv.org/abs/1709.04504>. Theory: inter-edge interaction halves the flux period, with no link to electron pairing found.
- Choi et al. 2014, "Robust Electron Pairing in the Integer Quantum Hall Effect Regime", <https://arxiv.org/abs/1409.4427>. h/2e periodicity and e* ≈ 2e in shot noise, dephased by the adjacent edge channel.
- Röösli et al. 2020, "Fractional Coulomb blockade for quasiparticle tunneling between edge channels", <https://arxiv.org/abs/2005.12723>. A quantum Hall dot modeled as two compressible regions, with e*/e = 0.32 ± 0.03 from comparison with filling factor 2.
- Kou et al. 2012, "Coulomb Oscillations in Antidots in the Integer and Fractional Quantum Hall Regimes", <https://arxiv.org/abs/1201.1600>. Gate and field periods together give tunneling charge 2e/3 with one charged edge at ν = 2/3.

Happy to rerun this if you share the figure data.
