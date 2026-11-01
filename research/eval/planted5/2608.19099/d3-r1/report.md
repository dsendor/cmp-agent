# Lookalike check: Field-free superconducting diode in NbSe2/CrBr3 (arXiv 2608.19099v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. I worked from the main text only. The Supplementary Material was not available to me, so I can't see any controls that are only in the SM. Where you write "as shown in SM", I have counted the test as argued in the main text, and moving it into the main text would settle that row.

**The claim, as I read it.** In device #1 at 200 mK, your critical currents differ by direction at zero applied field. After field training the difference reaches η = −35.7% (Figs. 1(d), 2(c)), and the polarity depends on the field-sweep history, with inverted sign-change fields Bcf < 0 and Bcb > 0 (Fig. 2). Device #3 rectifies at zero field after ±6 T training (Fig. 3(a)). You attribute the effect to interfacial exchange from layered ferrimagnetic CrBr3, acting through a cubic odd-in-q Ginzburg-Landau term (Fig. 4, Eqs. 1 to 3).

## Checks a careful reader will look for

The library has no ordered checks for the diode family, so only the practice checks apply here.

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside: Partly. Three devices are named: "Similar behavior is also observed in another device #2, as shown in Supplementary Material (SM) [40]." (p. 2). The text doesn't say how many devices were fabricated or measured, or why any were set aside.
2. Disclose the full parameter ranges measured and why each shown range was chosen: Partly. "as the field sweeps from −50 mT to 0 mT, the SDE efficiency first reaches a maximum positive value of 45.3% at around −10 mT" (p. 2). The training field before Fig. 2, the temperature range in Fig. 1(e), and the reasons for each range are not stated.
3. Give the processing steps from raw data to figures, with data and code: Partly. "The peaks in the differential resistance correspond to the critical current along the horizontal axis." (p. 2). The η formula is given. There is no statement on data or code.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Vortex barriers and Meissner screening in an ordinary film (diode-vortex-screening) | Tested in part | Plain film of the parent superconductor: no; effect followed against field, width or edges: part (field sweeps for device #1 only) | "Other trivial mechanisms for the zero-field SDE (e.g., self-fields, Meissner screening, and geometric asymmetry) are ruled out, as shown in SM [40]." (p. 4) | Show a bare NbSe2 flake, or a bare part of the same flake, with matched width and the same field history, next to Fig. 2(c). |
| Stray field from the magnetic layer (micromagnet-stray-field, adapted) | Tested in part | Magnet switching: part (transport hysteresis for device #1; RMCD is in the SM); stray field mapped or bounded: no; devices without magnets: no | "During the reverse sweep from 50 mT to −50 mT, the behavior mirrors that of the forward sweep, demonstrating a hysteretic SDE response" (p. 2, Fig. 2(c)) | Bound the dipolar field of each CrBr3 flake at the NbSe2 from its thickness and RMCD magnetization, and compare it with the few-mT scale of Fig. 2(c). |
| Fine-tuning and selection (fine-tuning-and-selection) | Tested in part | Counts: part; how shown data were chosen: no; second device: part (device #3 at zero field; device #2 only in the SM) | "Similar behavior is also observed in another device #2, as shown in Supplementary Material (SM) [40]." (p. 2) | Give counts and the selection rule, and show device #2's Fig. 2-style sweeps in the main text. |
| Trapped magnetic flux in the superconductor after a poling field (not in library) | Tested in part | Opposite poling fields compared: all; poling-field magnitude: no; field orientation: no | "Application of a 6 T perpendicular magnetic field for initial magnetization induced positive magnetization in the CrBr3 layer, establishing a state wherein the critical current \|Ic+\| > \|Ic−\|." (p. 3, Fig. 3(a)) | Set the CrBr3 state above the NbSe2 Tc, then cool in zero field. Also vary the training field below and above the CrBr3 switching fields. |
| Remanent field of the superconducting magnet (not in library) | Not tested (not mentioned) | Zero field calibrated in situ: no; raw and corrected field axes: no | Not discussed. | Check whether the forward and backward η(B) curves in Fig. 2(c) overlay after a rigid field shift. Then measure a Hall sensor or a graphene reference alongside the device. |

A note on two rows. Hou et al. obtained a non-volatile diode with 65% efficiency in an ordinary film next to a ferromagnet, from vortex barriers and Meissner currents. That makes a matched bare-NbSe2 control the most direct answer to rows 1 and 2. Your Fig. 2(c) argument already speaks to the stray-field reading: the polarity does not track the net magnetization, and a dipolar field would track it. It would be stronger if you also showed RMCD from the same flake.

The remanent-field row matters because of the numbers. Jiang et al. corrected a magnet hysteresis of about 15 mT after 1 T poling. Your Bcf and Bcb sit within roughly 10 mT of zero, and an offset of opposite sign to the previous field would shift the forward and backward crossings in the directions you report. The same offset would also mean that "zero field" after the 6 T training of Fig. 3(a) is not zero. Your zero-field-cooled value, "In contrast, the original efficiency after zero-field cooling is −15.2%, as shown in Fig. 1(d)." (p. 2), is useful here. If the cooldown came before any field excursion, it bears on both the magnet and the trapped-flux rows. Stating the sequence would help readers.

## Questions about devices and data

1. How many NbSe2/CrBr3 devices did you fabricate and measure, and how many showed a zero-field diode effect? The text names devices #1, #2 and #3.
2. Why were the others set aside, and how did you choose device #1 for Figs. 1, 2 and 3(b) and device #3 for Fig. 3(a)?
3. Which ranges of temperature, field (sweep amplitude and training field) and current did you measure beyond those shown, and what training field preceded the -35.7% value in Fig. 2?
4. What does the second-best device look like? Could device #2's field sweeps, with its Bcf and Bcb, move from the SM into the main text?
5. How did you fix zero applied field after the ±50 mT sweeps and the ±6 T training? A superconducting magnet can leave a remanent field of order 10 mT, the scale of your Bcf and Bcb; was a Hall sensor or reference sample measured alongside?
6. Did you measure a bare NbSe2 flake, or a part of the same flake without CrBr3, with the same geometry and field history, and how do the diode effect and its field dependence compare?
7. Was the training field applied with NbSe2 superconducting? If you set the CrBr3 state above the NbSe2 Tc (and below the CrBr3 ordering temperature) and then cool in zero field, does the zero-field polarity still follow the CrBr3 state?
8. Were the RMCD loops in the SM taken on the transport devices themselves and at what temperature, so that B0 and Bco can be compared with Bcf and Bcb of the same flake?

## Related work

- Hou et al. 2023, "Ubiquitous Superconducting Diode Effect in Superconductor Thin Films", <https://arxiv.org/abs/2205.09276>. Shows a diode effect in plain Nb and V films at fields near 1 Oe, and a non-volatile 65% diode with a EuS ferromagnet, both from vortex barriers and Meissner screening.
- Jiang et al. 2025, "Zero-field superconducting diode effect induced by magnetic flux in a van der Waals superconductor trigonal PtBi2", <https://arxiv.org/abs/2512.05427>. Shows a zero-field diode in a non-magnetic vdW superconductor whose sign is set by a prior poling field, attributed to trapped flux. It also corrects a magnet hysteresis of about 15 mT using a graphene reference.
- Golod and Krasnov 2022, "Demonstration of a superconducting diode-with-memory, operational at zero magnetic field with switchable nonreciprocity", <https://arxiv.org/abs/2205.12196>. Shows zero-field diodes above 70% efficiency in conventional Nb junctions, from self-field plus a trapped Abrikosov vortex, switched by trapping or removing the vortex.
- Narita et al. 2022, "Field-free superconducting diode effect in noncentrosymmetric superconductor/ferromagnet multilayers", <https://arxiv.org/abs/2206.00483>. Shows a zero-field diode in [Nb/V/Co/V/Ta] multilayers, with polarity set by the ferromagnet's magnetization direction.
- Xiong et al. 2024, "Electrical switching of Ising-superconducting nonreciprocity for quantum neuronal transistor", <https://arxiv.org/abs/2406.14417>. Shows field-free, electrically switchable nonreciprocity in an Fe3GeTe2/NbSe2 vdW heterostructure.

Happy to rerun this if you share the Supplementary Material or the figure data.
