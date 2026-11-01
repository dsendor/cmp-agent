# Lookalike check: Single anyons and anyon binding in a quantum Hall dot (arXiv 2610.18817v1)

*AI only. Written by the lookalike assistant on 2026-10-23 from arXiv version v1, with
lookalike library version 0.4. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. For your quantum Hall dot I used the library's fractional-charge entries and adapted
its even-odd island entry to orbital shell effects.

**The claim, as I read it.** In one graphene device with a 90 nm dot in a QPC, Coulomb
resonances at ν = 1/3 and 2/3 with a gate period about a third of that at ν = 1 (Fig. 1h
to 1j) are your evidence for e/3 tunneling into a dot emptied to the last quasiparticle
(Fig. 3), and the loss of alternate charge sectors as VT is lowered (Fig. 4e to 4g) is your
evidence for anyon binding.

## Checks a careful reader will look for

1. Field and gate map, and which regime : Partly. "consistent with resonant backscattering via a dot tuned through a series of Coulomb blockade resonances" (p. 3, Fig. 1g); Vdot is mapped against other gates (Ext. Data Figs. 2, 9, 10), with no field and Vdot map in the fractional regime.
2. Control regime, charge traps and gate leakage : Partly. "For the integer quantum Hall state, δ ≈ 250 − 300mV, while at both fillings 1/3 and 2/3 δ is 80 − 100 mV" (p. 3, Fig. 1j); the gate map locating the dot is at ν = 1 only, and gate leakage isn't discussed.
3. Repeated sweeps : Partly. "The small drift and fluctuations demonstrate the excellent long-term charge stability of the integer dot." (Ext. Data Fig. 5, p. 18); no repeated sweeps of Fig. 4e to 4g.
4. Device and dataset counts : Partly. "The device was measured during two separate cool downs." (p. 9); devices fabricated aren't counted.
5. Full ranges and why each was chosen : Partly. Table I (p. 10) gives every main-panel window and Ext. Data Fig. 11 extends Fig. 4a to 4d; the full ranges explored aren't stated.
6. Processing, data and code : Partly. "obtained numerically from the measured current–voltage characteristics using a multipoint derivative" (p. 9); no data or code statement, and the dip-finding algorithm (Ext. Data Figs. 9, 10) isn't described.

## Lookalikes

| Lookalike | Status | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|
| Integer charges in a capacitively coupled charge trap or side dot | Partly addressed | "the resonances are nearly insensitive to the QPC gates, very weakly tuned by the edge gates, and very strongly tuned by both the center and bottom gate" (p. 3, Ext. Data Fig. 2), shown at ν = 1 only. | Fit the slope of each line in Fig. 4f and repeat the Fig. 4e to 4g sweeps; a trap line has its own lever arms and may not repeat. |
| Even-odd spacings from the dot's orbital structure (library island entry, adapted) | Partly addressed | "Short plateaus or an even/odd pattern in the widths do not imply binding (as they may due to attraction or orbital effects)." (p. 12); the missing sector is shown in one VT window (Fig. 4f, 4g). | Show the Fig. 4g diamonds next to Fig. 4e at matched bias and Vdot resolution, so a weakly coupled, unresolved sector is excluded. |
| Fine-tuning and selection of the shown example | Partly addressed | "Fig. 4e focuses on a narrow range of gate voltage in which we observed a particularly pronounced even-odd effect" (p. 8). | Say how the window was found, how many windows lost a sector, and show the second best. |
| Capacitive coupling between nested edge modes or compressible regions (not in library) | Partly addressed | "If charge enters via the expansion of the 2/3 − 1/3 edge state, the pairing could be interpreted as a property of the 2/3 − 1/3 edge." (p. 8) | In the 2e/3 regime, get the charge per resonance from field and gate periods together, as Liang et al. do in operando. |

The e/3 reading of Fig. 1j holds "Assuming these phenomenological parameters are
determined primarily by geometry" (p. 3). Your 13.4 T data at ν = 1 help, though Table I
shows other gate settings and the lock-in cooldown; question 6 avoids the assumption.

## Questions about devices and data

1. How many devices did you measure, and how many showed e/3 resonances and a missing charge sector? The paper names one device (p. 9), while "M.V. fabricated the devices" (p. 8).
2. Why were the others set aside?
3. Which ranges of VT, Vdot, Vedge and field did you measure beyond the windows in Table I, and how wide a search led to the Fig. 4e window?
4. What does the second-best dataset look like: is there another gate configuration, or the other cooldown, where a charge sector disappears?
5. In Fig. 4f, do the merging lines share one slope in the VT and Vdot plane, and are the Fig. 4g diamonds about twice as tall as those in Fig. 4e?
6. Could you show field and Vdot maps at ν = 1/3 and at ν = 1, same field and cooldown, so field and gate periods give the charge without a fixed lever arm?
7. Table I lists Fig. 1h as "νbulk = 2/5, νdot = 1/3" and the text gives νbulk = 1/3 (p. 3); which applies to Fig. 1h, and to the 1/3 quasihole data in Figs. 1j and 4a?
8. Is "EC = 3e ∆VDC ≈ 300 µeV" (Fig. 1i caption) meant with e/3, and what is the diamond height ratio between Figs. 1g and 1i?

## Related work

- Byard et al. 2025, "Apparent fractional charge signatures in PbTe quantum dots due to capacitively coupled charge trap dynamics", <https://arxiv.org/abs/2504.05221>. Fractional shifts in nanowire dot stability diagrams at zero field, attributed to capacitively coupled charge traps.
- Liang et al. 2025, "Single electron interference and capacitive edge mode coupling generates Φ0/2 flux periodicity in Fabry-Perot interferometers", <https://arxiv.org/abs/2502.00124>. A halved flux period at ν = 2 and 3, earlier read as pairing, traced to capacitive edge-mode coupling, with interfering charge e.
- Röösli et al. 2020, "Fractional Coulomb blockade for quasiparticle tunneling between edge channels", <https://arxiv.org/abs/2005.12723>. A 1.4 µm dot modeled with two compressible regions, giving e*/e = 0.32 ± 0.03 by comparison with ν = 2.
- Kou et al. 2012, "Coulomb Oscillations in Antidots in the Integer and Fractional Quantum Hall Regimes", <https://arxiv.org/abs/1201.1600>. Field and gate periods together give tunneling charge (2/3)e at ν = 2/3 in antidots.
- Hamo et al. 2016, "Electron Attraction Mediated by Coulomb Repulsion", <https://arxiv.org/abs/1608.05721>. Nanotube devices where two electrons attract through an independent electronic system, with transport signatures of pairing.

Happy to rerun this if you share the figure data for Fig. 4e to 4g.
