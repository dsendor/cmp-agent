# Lookalike check: Field-free diode controlled by an antiferromagnet (arXiv 2609.38003v1)

*AI only. Written by the lookalike assistant on 2026-10-23 from arXiv version v1, with
lookalike library version 0.4. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your signal, a superconducting diode in a hybrid film, sits at the edge of the library, so I adapted two entries (stray fields from magnets, data-processing choices) to it. I worked from the v1 text and figure captions.

**The claim, as I read it.** A CuMnAs/AlAs/Al bar along [010] shows a zero-field diode efficiency of about 7% after zero-field cooling (Fig. 3a), which reverses sign after ±1 T preparation along [100] and approaches ±20% (Fig. 3b, d), with a weak, non-reversing response for [010] preparation (Fig. 3e). You tie the polarity to the remanent Néel state through an orthogonal bar (Extended Data Fig. 4), nonlinear resistance of a reference CuMnAs bar (Fig. 4) and XMLD-PEEM (Extended Data Fig. 5).

## Checks a careful reader will look for

The library has no diode-specific checks yet, so these are its three checks for every paper.

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. Two diode bars: "An orthogonal bar patterned along [100] displays the same qualitative dependence on the preparation-field axes (Extended Data Fig. 4)" (pp. 4 to 5). Totals and cooldowns aren't stated.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. Methods give "the switching current for each polarity was averaged over eight sweeps" (p. 8). I found no diode data above 20 mK, no η near zero applied field, and no reason given for the preparation ranges in Fig. 3d and 3e.
3. Give the processing steps from raw data to figures, with data and code : Partly. Switching is defined at "the bias current at which the measured voltage first exceeded a threshold of 50 µV" (p. 8). I found no data or code statement.

## Lookalikes

| Lookalike | Status | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|
| Vortex edge barriers and Meissner screening in a small residual field (`diode-vortex-screening`) | Partly addressed | "preparation along [010] produces a weaker response and leaves η predominantly of the same sign" (p. 4, Fig. 3 caption); the data bear on it; the paper doesn't discuss it. | Run the protocol on an Al bar without CuMnAs, and map η against a few Oe of perpendicular field after each preparation. |
| Trapped flux or magnet remanence set by the preparation field (not in library; Jiang et al., arXiv 2512.05427) | Partly addressed | "suggesting that the anisotropy is not determined simply by the relative orientation of the applied field and current, but is instead tied to the underlying crystallographic axes of CuMnAs" (p. 11, Extended Data Fig. 4); flux and magnet remanence aren't discussed. | After each preparation, warm the Al above 350 mK at compensated zero field and recheck the sign of η. |
| Stray fields from uncompensated moments or domain walls in CuMnAs (`micromagnet-stray-field`, adapted) | Partly addressed | "which place an upper bound of (3×10−3 µB /Mn)" (p. 3, Fig. 2b), for the as-measured film. | By my estimate the bound still allows 4πM near 8 G, above Hou et al.'s 1 Oe scale; an AlAs thickness series (2.0, 2.5, 3 nm) would separate proximity from stray fields. |
| Switching-current extraction choices (`protocol-parameter-sensitivity`, adapted) | Partly addressed | "this value was chosen empirically to minimize premature switching associated with faster current ramping" (p. 8, Methods). | Recompute η from existing sweeps at other thresholds and show raw V(I) for both polarities after each preparation. |
| A non-representative example picked from many (`fine-tuning-and-selection`) | Partly addressed | "An orthogonal bar patterned along [100] displays the same qualitative dependence on the preparation-field axes (Extended Data Fig. 4)" (pp. 4 to 5). | State how many bars and cooldowns were measured and how many showed the reversal. |

## Questions about devices and data

1. How many bars did you pattern from the 2.0 nm heterostructure, over how many cooldowns, and how many showed the reversal of Fig. 3d? I can see the bars of Fig. 3 and Extended Data Fig. 4.
2. Why were any other bars or cooldowns set aside?
3. Which ranges did you measure beyond the ones shown: temperatures up to the 350 mK transition, [100] preparation beyond ±1 T, and small applied fields near zero?
4. What does the second-best device or dataset look like, for example a second cooldown of the [010] bar?
5. What residual field does your magnet leave at the sample after each excursion, are [100] and [010] set by different coils or by rotating the sample, and do the reset fields drive the Al normal?
6. If you warm the Al above its transition (say 1 K, far below the 480 K Néel temperature) at compensated zero field after a preparation, does η keep its sign? And is the sign of the 7% zero-field-cooled η the same in every cooldown?
7. Have you run the same protocol on an Al bar without CuMnAs (for example Al/AlAs on GaP), with η mapped against a few Oe of perpendicular field?
8. Fig. 4 comes from a different wafer at 5 K. Can you measure the remanent moment or Reven on the diode film itself after the same preparations?

On questions 5 to 8: your reference list includes Hou et al. [28] and Jiang et al. [29], and I couldn't find where the text cites them. Domain imbalance (Fig. 4c) and any domain-linked stray field follow the same preparation history, so a sentence on how your data separate them would help.

## Related work

- Hou et al. 2023 (arXiv 2022), "Ubiquitous Superconducting Diode Effect in Superconductor Thin Films", <https://arxiv.org/abs/2205.09276>. Plain Nb and V films show a strong diode at fields as small as 1 Oe, from asymmetric vortex barriers and Meissner screening.
- Jiang et al. 2025, "Zero-field superconducting diode effect induced by magnetic flux in a van der Waals superconductor trigonal PtBi2", <https://arxiv.org/abs/2512.05427>. In a non-magnetic superconductor, the zero-field diode sign follows a ±1 T in-plane poling field, attributed to trapped flux, with magnet remanence calibrated out by a graphene sensor.
- Golod and Krasnov 2022, "Demonstration of a superconducting diode-with-memory, operational at zero magnetic field with switchable nonreciprocity", <https://arxiv.org/abs/2205.12196>. Nb planar junctions give a switchable zero-field diode from a trapped Abrikosov vortex plus self-field.
- Sachin et al. 2026, "Altermagnetic Superconducting Diode Effect in Mn3Pt/Nb Heterostructures", <https://arxiv.org/abs/2601.03366>. Nb on compensated and nearly compensated Mn3Pt shows a zero-field diode up to 50%, sensitive to the magnetic order, with signs of several contributing mechanisms.
- Zapata et al. 2026, "Field-free superconducting diode and tunable vortex dynamics in NbN/FePt stripe-domain heterostructures", <https://arxiv.org/abs/2610.30556>. A zero-field diode in NbN persists through an AlN spacer that reduces proximity and keeps stray-field coupling.

Happy to rerun this if you share the figure data, especially the raw V(I) sweeps behind Fig. 3d and 3e.
