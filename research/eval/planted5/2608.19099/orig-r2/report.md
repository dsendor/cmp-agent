# Lookalike check: Field-free diode in NbSe2/CrBr3 (arXiv 2608.19099v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**Paper:** "Large Field-Free Superconducting Diode Effect with Nonmonotonic Polarity Reversals in NbSe2/CrBr3 Heterostructures" (title taken from the paper text).

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport. A lookalike is an ordinary effect that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. The library has one diode entry and no diode-specific checks, so I walked the general practice checks and added two lookalikes from the diode literature (marked "not in library"). I worked from the main text only. Your Supplementary Material was not available to me, so anything shown only there counts here as stated, not shown.

**The claim, as I read it.** Device #1 shows a zero-field diode effect with efficiency −35.7% after field training (−15.2% after zero-field cooling; Figs. 1(d), 2(c)). Its polarity follows the field history, with sign-change fields Bcf < 0 and Bcb > 0 (Fig. 2, 200 mK, ±50 mT). Device #3 shows zero-field rectification after ±6 T training (Fig. 3(a)). You attribute this to an interfacial exchange field from layered ferrimagnetic CrBr3 acting through a cubic Ginzburg–Landau term (Fig. 4).

## Checks a careful reader will look for

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside: Partly. "Similar behavior is also observed in another device #2, as shown in Supplementary Material (SM) [40]." (p. 2). Three devices are named. The total fabricated and measured is not given.
2. Disclose the full parameter ranges measured and why each shown range was chosen: Partly. "The forward sweep (blue) refers to current swept from 0 µA to +300 µA and the backward sweep (red) refers to current swept from 0 µA to −300 µA." (p. 2, Fig. 1(c)). You state the shown ranges, but not the wider ranges you measured or why you chose these.
3. Give the processing steps from raw data to figures, with data and code: Partly. "The peaks in the differential resistance correspond to the critical current along the horizontal axis." (p. 2). The Ic definition and the η formula are given. I found no data or code statement.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Vortex edge barriers and Meissner screening (diode-vortex-screening) | Tested in part | Plain NbSe2 film control: no; effect followed against field, width or edge: part (field sweeps for device #1, Fig. 2; device #3 only at zero field) | "Other trivial mechanisms for the zero-field SDE (e.g., self-fields, Meissner screening, and geometric asymmetry) are ruled out, as shown in SM [40]." (p. 4) | Show a bare NbSe2 flake, or an uncovered NbSe2 region, with the same contacts and fine field steps near zero in the main text |
| Fine-tuning and selection (fine-tuning-and-selection) | Tested in part | Devices measured and how many showed it: part; how shown data were chosen: no; second device shown: part (device #3 in Fig. 3(a); device #2 only in SM) | "our NbSe2/CrBr3 devices consistently exhibit the opposite condition, Bcf < 0 and Bcb > 0" (p. 3) | State how many devices were made and measured, and move device #2's field sweeps into the main text |
| Trapped vortex and self-field set by field history (not in library; Golod and Krasnov) | Tested in part | With and without trapped vortex (zero-field-cooled versus trained): part (device #1 only, Fig. 1(d)); bias configuration changed: no | "In contrast, the original efficiency after zero-field cooling is −15.2%, as shown in Fig. 1(d)." (p. 2) | After training, warm above the NbSe2 Tc and stay below the CrBr3 ordering temperature, then cool in zero field and remeasure; swap current contacts |
| Stray field of the CrBr3 layer acting on vortices (not in library; Zapata et al.) | Not tested (not mentioned) | Nonmagnetic spacer (exchange cut, stray field kept): no; domain orientation relative to current varied: no | Not discussed. | A NbSe2/hBN/CrBr3 device: a diode that survives the spacer points to stray fields |

## Questions about devices and data

1. How many NbSe2/CrBr3 devices did you fabricate and measure, and how many showed a zero-field diode effect? Your text names devices #1, #2 and #3.
2. Why were the others set aside, if any were?
3. Which ranges of field sweep amplitude, training field, temperature and current did you measure beyond the ones shown, and do Bcf and Bcb move when the sweep amplitude changes (for example ±50 mT versus ±6 T)?
4. What does the second-best device look like? Could device #2's Fig. 2-style sweeps and device #3's field dependence go in the main text?
5. How did you set the true zero of field at the sample, including the magnet's remanent field after the ±50 mT and ±6 T sweeps? Your Fig. 2(c) shows η moving from 45.3% to −35.7% between about −10 mT and 0 mT, so an offset of a few mT would shift Bcf, Bcb and the zero-field efficiency.
6. Did you measure a bare NbSe2 flake, or NbSe2 with a nonmagnetic spacer such as hBN under the CrBr3, with the same contacts and field sweeps?
7. For the zero-field-cooled state (−15.2%, Fig. 1(d)), from which temperature did you cool, and does the trained −35.7% survive warming above the NbSe2 Tc (staying below the CrBr3 ordering temperature) and cooling back in zero field?
8. Were the RMCD loops in the SM taken on the same flakes as the transport, and do the measured switching fields bracket the measured Bcf and Bcb?

## Notes on the suggestions

Your strongest asset is the field-sweep map in Fig. 2. The inverted sign-change fields (Bcf < 0, Bcb > 0) are the observation that separates your picture from the simple ferromagnet one, so readers will want that pattern to be robust.

A remanent field in the magnet after a sweep would shift the apparent zero against the sweep direction. That shift would also give Bcf < 0 and Bcb > 0. A Hall probe or a known-symmetric reference sample at the same position would settle this (question 5).

The zero-field-cooled value of −15.2% already shows a diode with no field history in NbSe2. A warm-up above the NbSe2 Tc after training would show how much of the −35.7% comes from flux held in the NbSe2 and how much from the CrBr3 magnetic state. You can run it on device #1 as it stands.

If you have a flake region without CrBr3, or a device with an hBN spacer, the same field sweeps would separate Meissner screening and stray fields from the interfacial exchange field. Those are the two classes of explanation a diode reader checks first.

Your Eq. (2) predicts α3 ∝ cos 3θ. Devices with different current directions relative to the NbSe2 axes would test the mechanism directly, if you have such devices.

## Related work

- Hou et al. 2023, "Ubiquitous Superconducting Diode Effect in Superconductor Thin Films", <https://arxiv.org/abs/2205.09276>. Shows a strong diode effect in plain Nb and V films at fields near 1 Oe, and a non-volatile 65% diode with ferromagnetic EuS, from vortex barriers and Meissner screening.
- Golod and Krasnov 2022, "Demonstration of a superconducting diode-with-memory, operational at zero magnetic field with switchable nonreciprocity", <https://arxiv.org/abs/2205.12196>. Zero-field Nb diodes from self-field plus a trapped Abrikosov vortex, with polarity switched by bias configuration and by trapping or removing the vortex.
- Zapata et al. 2026, "Field-free superconducting diode and tunable vortex dynamics in NbN/FePt stripe-domain heterostructures", <https://arxiv.org/abs/2610.30556>. A field-free diode of about 50 to 60% that persists through an AlN spacer, which the authors read as a stray-field and vortex origin.
- Li et al. 2025, "Field-Free Superconducting Diode Enabled by Geometric Asymmetry and Perpendicular Magnetization", <https://arxiv.org/abs/2506.17651>. A field-free diode in Pt/Co/Nb from stray fields of a perpendicular magnet combined with geometric asymmetry.
- Xiong et al. 2024, "Electrical switching of Ising-superconducting nonreciprocity for quantum neuronal transistor", <https://arxiv.org/abs/2406.14417>. A field-free, switchable nonreciprocity in an Fe3GeTe2/NbSe2 heterostructure: a similar signature in an Ising superconductor with a vdW magnet.

Happy to rerun this with the Supplementary Material or the figure data.
