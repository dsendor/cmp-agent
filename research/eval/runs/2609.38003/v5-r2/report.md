# Lookalike check: Field-free diode controlled by an antiferromagnet (arXiv 2609.38003v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper, "Reversible field-free superconducting diode effect controlled by an antiferromagnet", against a library of 28 known lookalikes in topological transport. A lookalike is an ordinary effect that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. The library is built for topological transport and your paper is a superconducting diode measurement, so I used its diode entry and its practice entries, adapted one stray-field entry from the zero-bias family, and added two explanations from a paper outside the library.

**The claim, as I read it.** You report a zero-field superconducting diode effect in a 5 µm by 180 µm CuMnAs/AlAs/Al bar: about 7% after zero-field cooling (Fig. 3a), with a sign that reverses after ±[100] preparation fields and responds weakly to [010] preparation (Fig. 3b,d,e). The same pattern appears on an orthogonal bar (Extended Data Fig. 4), and it matches the remanent nonlinear resistance of a reference CuMnAs bar at 5 K (Fig. 4). From this you conclude that the remanent Néel state controls the diode polarity.

## Checks a careful reader will look for

The library has no ordered checks for diode signals, so these are the practice checks that apply to every paper.

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Not done. Two diode bars appear (Fig. 3, Extended Data Fig. 4), and the paper gives no count of the bars or cooldowns measured.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. One choice is explained: "this value was chosen empirically to minimize premature switching associated with faster current ramping" (p. 8). The preparation ranges (±1 T along [100] in Fig. 3d, ±4 T along [010] in Fig. 3e) have no stated reason.
3. Give the processing steps from raw data to figures, with data and code : Partly. The switching current is "defined as the bias current at which the measured voltage first exceeded a threshold of 50 µV" (p. 8), with eight-sweep averages. The paper doesn't mention releasing data or code.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Asymmetric vortex barriers and Meissner screening in the Al film | Tested in part | Plain Al film or bar: no; effect against field, width or edges: part (preparation field on two bar orientations, with no applied-field, width or edge series) | "the anisotropic remanence itself originates in CuMnAs rather than from spurious flux trapping or vortex dynamics, both known to generate SDE" (p. 6) | Run the Fig. 3c protocol on an Al bar of the same width without CuMnAs, and measure η against small in-plane and out-of-plane fields near zero on your bar |
| Stray field from uncompensated moments (adapted from the micromagnet stray-field entry) | Tested in part | Magnet switching in field: part (reference bar at 5 K, Fig. 4a,c); stray field bounded: part (net moment of a millimeter-scale piece, Fig. 2b); device without the magnet: no | "this also disfavors a stray-field mechanism associated with uncompensated magnetization" (p. 6) | Estimate the local field from domain walls and bar edges using the domain sizes in Extended Data Fig. 5, and compare with the same protocol on an Al bar without CuMnAs |
| Trapped flux set by the preparation field (not in library; Jiang et al. 2025) | Tested in part | η against applied field after each poling sign: no; poling direction compared: part (two in-plane axes on two bars, no out-of-plane poling) | "Neither mechanism is naturally expected to track the Néel-vector anisotropy observed here." (p. 6) | Show η(H) near zero after +[100] and after −[100] preparation, and repeat the protocol with an out-of-plane preparation field |
| Superconducting magnet remanence at nominal zero field (not in library; Jiang et al. 2025, Appendix D) | Not tested (not mentioned) | Field at the sample calibrated at nominal zero after each excursion: no | Not discussed. | Calibrate the field at the sample after each excursion with a Hall or graphene sensor, as Jiang et al. do; Extended Data Fig. 4 already bears on the in-plane part, since [100] preparation runs along the current there |
| Fine-tuning and selection | Tested in part | Counts measured and showing the effect: no; how the shown data were chosen: no; second device: part (Extended Data Fig. 4 repeats Fig. 3d,e only) | "An orthogonal bar patterned along [100] displays the same qualitative dependence on the preparation-field axes (Extended Data Fig. 4)." (p. 4 to 5) | Report bar and cooldown counts, and show Fig. 3a,b for the [100] bar and for a second cooldown |

## Questions about devices and data

1. How many bars and cooldowns did you measure on the 2.0 nm AlAs wafer, and how many showed a zero-field diode effect that reverses with [100] preparation?
2. Why were the others set aside, if any were?
3. Which preparation-field ranges and temperatures did you measure beyond the ones shown? Fig. 3d stops at ±1 T, while Fig. 3e and Fig. 4c reach ±4 T and ±5 T.
4. What does the second-best bar or cooldown look like, including the zero-field-cooled efficiency of about 7% after separate cooldowns?
5. In Fig. 3d, η changes sign at preparation fields of roughly ±0.1 T, while the remanent Reven in Fig. 4c crosses zero near ±1.5 T (both read from the figures). How do you connect the two field scales, given that the reference bar comes from a different wafer and was measured at 5 K?
6. What is the field at the sample at nominal H = 0 after each excursion, including any out-of-plane part from sample tilt, and how was the magnet's remanent field measured or compensated? Were the [010] and [100] bars on the same chip and mount?
7. Did you measure η against small applied fields near zero, in plane and out of plane, after each preparation, and the same protocol on an Al bar without CuMnAs?
8. Could you share the switching-current sweeps and the code that computes η, so readers can see how the 50 µV threshold and the eight-sweep average shape Fig. 3d,e?

## Related work

- Hou et al. 2023 (Phys. Rev. Lett. 131, 027001), "Ubiquitous Superconducting Diode Effect in Superconductor Thin Films", <https://arxiv.org/abs/2205.09276>. Shows strong diode effects in plain Nb and V films at fields as small as 1 Oe, traced to asymmetric vortex barriers and Meissner screening, and a non-volatile diode with a EuS overlayer.
- Jiang et al. 2025, "Zero-field superconducting diode effect induced by magnetic flux in a van der Waals superconductor trigonal PtBi2", <https://arxiv.org/abs/2512.05427>. Shows a zero-field diode in a non-magnetic superconductor whose sign follows a ±1 T poling field, attributed to trapped flux, and corrects a superconducting-magnet hysteresis of about ±15 mT with a graphene field sensor.
- Sachin et al. 2026, "Altermagnetic Superconducting Diode Effect in Mn3Pt/Nb Heterostructures", <https://arxiv.org/abs/2601.03366>. Reports zero-field diode efficiencies up to 50% in Nb on compensated and nearly compensated Mn3Pt, with a complex field and temperature dependence.
- Sun et al. 2026, "Large Field-Free Superconducting Diode Effect with Nonmonotonic Polarity Reversals in NbSe2/CrBr3 Heterostructures", <https://arxiv.org/abs/2608.19099>. Reports a field-free diode whose polarity is set by field history, attributed to a history-dependent interfacial exchange field from layered ferrimagnetism.
- Cruz et al. 2026, "High-Efficiency Field-Free Superconducting Diodes in Mo2N/FePt Bilayers", <https://arxiv.org/abs/2610.16972>. Shows field-free diodes from remanent stripe-domain stray fields, tuned by the in-plane preparation angle and switched by reverse-field excursions.

Happy to rerun this if you share the switching-current data and the magnet calibration.
