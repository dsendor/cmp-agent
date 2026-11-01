# Lookalike check: Field-free diode controlled by an antiferromagnet (arXiv 2609.38003v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. The library has one diode entry and no diode checks, so I adapted a stray-field
entry written for zero-bias peaks to a small net moment in your CuMnAs layer, and added
one explanation from outside the library (trapped flux or magnet remanence).

**The claim, as I read it.** A 5 µm by 180 µm CuMnAs/AlAs(2 nm)/Al bar switches at
unequal currents for the two current directions at H = 0 after zero-field cooling (η about
7%, Fig. 3a), and the sign of η reverses with the sign of a preparation field along [100]
(Fig. 3b, d). You tie this to the remanent Néel state through the matching anisotropy and
field history of the nonlinear resistance of a reference CuMnAs bar (Fig. 4) and
XMLD-PEEM (Extended Data Fig. 5).

## Checks a careful reader will look for

The library has no checks for diode signals, so these are the practice checks that apply
to every paper.

1. Report devices and datasets measured, how many showed the effect, and why the others
   were set aside : Partly. "An orthogonal bar patterned along [100] displays the same
   qualitative dependence on the preparation-field axes (Extended Data Fig. 4)" (p. 4 to 5).
   The number of bars made and measured is not given.
2. Disclose the full parameter ranges measured and why each shown range was chosen :
   Partly. The ranges appear on the figure axes, and you give one reason: the 0.2 s delay
   "was chosen empirically to minimize premature switching associated with faster current
   ramping" (p. 8). Other temperatures and fields are not discussed.
3. Give the processing steps from raw data to figures, with data and code : Partly. The
   switching current is "defined as the bias current at which the measured voltage first
   exceeded a threshold of 50 µV" (p. 8), averaged "over eight sweeps" (p. 8). I found no
   data or code statement.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Asymmetric vortex barriers and Meissner screening in the Al film | Not tested (data bear on it) | Same measurement on a plain film or junction of the parent superconductor: no; Effect followed against field, sample width or edge quality: no | "suggesting that the anisotropy is not determined simply by the relative orientation of the applied field and current, but is instead tied to the underlying crystallographic axes of CuMnAs" (p. 11, Extended Data Fig. 4) | Run the reset, prepare, measure protocol of Fig. 3c on a plain Al bar of the same width, and record η against a small applied field around zero after each preparation polarity. |
| Trapped flux or magnet remanence after the preparation field (not in library) | Tested in part | True zero field calibrated after each preparation field: no; Diode effect followed against applied field after each preparation polarity: no; A field configuration that traps no flux compared under the same protocol: part, since the [010] axis may use another coil and its residual field is not given | "a substantially weaker response which shows no systematic reversal of the sign of the diode effect (Fig. 3e)" (p. 4) | Calibrate the residual field after each preparation with a sensor whose response is even in field; after preparing, warm above the Al Tc at H = 0 and cool again, which erases flux in the Al and keeps the Néel state. |
| Stray or exchange field from a small net moment of the magnetic layer (adapted from the micromagnet entry) | Tested in part | Magnet switching (hysteresis in field): part; Stray field mapped or bounded: part; Comparison with devices without magnets: no | "which place an upper bound of (3×10−3 µB /Mn)" (p. 3, Fig. 2b) | Turn the bound into a field at the Al (my estimate gives µ0M up to about 0.8 mT), compare it with the field a plain Al bar needs for η of 7 to 20%, and give the SQUID temperature. |
| A non-representative example picked after fine-tuning | Tested in part | Devices and datasets measured, and how many showed the effect: part; How the shown data were chosen: no; A second device or dataset shown: all | "An orthogonal bar patterned along [100] displays the same qualitative dependence on the preparation-field axes (Extended Data Fig. 4)" (p. 4 to 5) | State how many bars and cooldowns you measured, and show the zero-field-cooled η and a repeat of the Fig. 3d protocol for each. |

## Questions about devices and data

1. How many bars did you pattern and measure from the 2.0 nm heterostructure, and how many showed a field-free diode effect? You show two (Fig. 3 and Extended Data Fig. 4).
2. Why were the others set aside, if any were?
3. Which ranges did you measure beyond the ones shown: η against temperature up to the 350 mK Tc, η in small applied fields around zero, [100] preparation beyond ±1 T, and step delays or voltage thresholds other than 0.2 s and 50 µV?
4. What does the second-best dataset look like, for example a second cooldown of the [010] bar, and what sign did η take after each zero-field cooldown?
5. How did you set H = 0 after each preparation field? Was the residual field of the magnet measured, and do the [100] and [010] preparations use different coils or a rotated sample?
6. Does a polarity written by the preparation field survive warming the bar above the Al Tc at H = 0 and cooling again? Flux trapped in the Al would be erased by that step, while the Néel state (TN = 480 K) should be kept.
7. Did you measure a plain Al bar of the same width with the same protocol, and how does the SQUID bound of 3×10−3 µB/Mn (about 0.8 mT in µ0M by my estimate) compare with the applied field at which such a bar shows a diode effect?
8. The Néel-state readout in Fig. 4 comes from a different wafer with a 3 nm oxidized Al cap, measured at 5 K. Have you read out the Néel state on the superconducting heterostructure itself after the same protocol, and what couples the sign of the preparation field to L+ or L− in a magnet with zero net moment?

## Related work

- Hou et al. 2023, "Ubiquitous Superconducting Diode Effect in Superconductor Thin Films", <https://arxiv.org/abs/2205.09276>. A strong diode effect in plain Nb and V films at fields as small as 1 Oe, from asymmetric vortex barriers and Meissner screening.
- Jiang et al. 2025, "Zero-field superconducting diode effect induced by magnetic flux in a van der Waals superconductor trigonal PtBi2", <https://arxiv.org/abs/2512.05427>. A zero-field diode whose sign follows a ±1 T poling field, attributed to trapped flux; a graphene sensor reveals about 15 mT of magnet remanence.
- Golod and Krasnov 2022, "Demonstration of a superconducting diode-with-memory, operational at zero magnetic field with switchable nonreciprocity", <https://arxiv.org/abs/2205.12196>. Nb planar junctions with a zero-field diode set by a trapped Abrikosov vortex, switched by trapping or removing it.
- Narita et al. 2022, "Field-free superconducting diode effect in noncentrosymmetric superconductor/ferromagnet multilayers", <https://arxiv.org/abs/2206.00483>. A zero-field diode in [Nb/V/Co/V/Ta] multilayers whose polarity follows the Co magnetization.
- Sachin et al. 2026, "Altermagnetic Superconducting Diode Effect in Mn3Pt/Nb Heterostructures", <https://arxiv.org/abs/2601.03366>. A zero-field diode in Nb on compensated and nearly compensated Mn3Pt, with efficiencies up to 50% and several contributing mechanisms.

Happy to rerun this if you share the figure data or the full set of bars and cooldowns.
