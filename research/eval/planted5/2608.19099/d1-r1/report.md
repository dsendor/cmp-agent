# Lookalike check: Field-free diode in NbSe2/CrBr3 (arXiv 2608.19099v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper "Large Field-Free Superconducting Diode Effect with Nonmonotonic Polarity Reversals in NbSe2/CrBr3 Heterostructures" against a library of 28 known lookalikes in topological transport: ordinary effects that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. I worked from the main text only. Your Supplementary Material was not available to me, so where you point to the SM I count the item as shown in part.

**The claim, as I read it.** In a NbSe2 flake proximitized by CrBr3, the critical currents in the two directions differ at zero applied field (efficiency -15.2% after zero-field cooling and up to 35.7% in size after field training; device #1, Figs. 1(c) to 1(e), 2, 3(b)). The diode polarity is set by field history (device #1, Fig. 2; device #3 after plus or minus 6 T, Fig. 3(a)). Its sign-change fields fall at Bcf < 0 and Bcb > 0, which you attribute to layered ferrimagnetism in CrBr3 (Fig. 4).

## Checks a careful reader will look for

The library has no checks for the diode family, so these are the practice checks that apply to every paper.

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. "Similar behavior is also observed in another device #2, as shown in Supplementary Material (SM) [40]." (p. 2). Devices #1 and #3 appear in Figs. 1 to 3. The number fabricated and measured, and the reasons any were set aside, are not given.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Not done. The captions give the shown ranges (plus or minus 300 µA, plus or minus 50 mT, 200 mK). The ranges measured beyond these, and the reasons for choosing them, are not stated.
3. Give the processing steps from raw data to figures, with data and code : Partly. "The peaks in the differential resistance correspond to the critical current along the horizontal axis." (p. 2). You also give the efficiency formula. The number of sweeps per value is not given, and I found no data or code link.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Vortex barriers and Meissner screening in the film (diode-vortex-screening) | Tested in part | Plain film of the parent superconductor: no; effect followed against field, width or edges: part (field sweep for device #1 only) | "nonreciprocal signals can also arise from extrinsic mechanisms such as Meissner screening [18–20] or current-induced self-fields [21–23], complicating the identification of intrinsic diode behavior." (p. 1); field dependence in Fig. 2 | Run the same history protocol on a bare NbSe2 device, or an uncovered part of the same flake. Measure the magnet's remanent field at the sample. A thin hBN spacer between NbSe2 and CrBr3 would cut the exchange field and keep the stray field. |
| Fine-tuning and selection (fine-tuning-and-selection) | Tested in part | Counts: part; how shown data were chosen: no; second device shown: part (device #2 in SM, device #3 in Fig. 3(a) only) | "Similar behavior is also observed in another device #2, as shown in Supplementary Material (SM) [40]." (p. 2) | State all devices and cooldowns. Show device #2's and device #3's field sweeps in the main text with their Bcf, Bcb and zero-field efficiency. |
| Trapped vortices set by field history (not in library) | Tested in part | Flux removed (warm above Tc, cool at zero field): part (one zero-field-cooled value, device #1, zero field not calibrated); bias configuration changed: no | "the original efficiency after zero-field cooling is −15.2%, as shown in Fig. 1(d)." (p. 2) | Warm above Tc between trainings and cool in a calibrated zero field. Repeat the zero-field-cooled point over several cooldowns. Swap the current leads to see whether the polarity follows the bias geometry. |
| Strain-induced field-free diode in NbSe2 (not in library) | Tested in part | Symmetry under reversal of field or magnetization: all (Fig. 2, device #1; Fig. 3(a), device #3); bare NbSe2 made the same way: no | "initial magnetization with a −6 T field reoriented the CrBr3 magnetization to a negative state, This inverts the critical current asymmetry" (p. 3, Fig. 3(a)) | Compare the sizes of the zero-field efficiencies after opposite trainings. Their mean gives any history-independent part. Add a bare NbSe2 flake made by the same dry transfer. |

## Questions about devices and data

1. How many NbSe2/CrBr3 devices did you fabricate and measure, and how many showed a field-free diode effect? Your text names devices #1, #2 and #3.
2. Why were any other devices set aside?
3. Which ranges did you measure beyond the ones shown: field sweeps wider than plus or minus 50 mT, in-plane field, temperatures, and current sweep rates?
4. What does the second-best device look like? Your SM shows device #2; could you give its zero-field efficiency and its Bcf and Bcb next to device #1, and a field sweep for device #3?
5. How did you establish zero field at the sample? What is the magnet's remanent field after the plus or minus 50 mT sweeps and after the plus or minus 6 T training, and was it measured with a Hall sensor or calibrated against a reference?
6. Did you measure a bare NbSe2 device, or a part of the same flake not covered by CrBr3, with the same protocol, and where do the CrBr3 edges sit relative to the channel and voltage probes?
7. How many current sweeps go into each critical current value in Figs. 1 and 2, and how wide is the switching distribution compared with the difference in critical currents?
8. After opposite trainings, are the zero-field efficiencies equal in size and opposite in sign, and does the -15.2% zero-field-cooled value repeat after warming above Tc in other cooldowns?

A note on question 5. Your inverted sign-change fields (Bcf < 0, Bcb > 0) are the key evidence for the ferrimagnetic picture. A small field offset that changes sign with sweep direction would shift both crossings the same way. So a measured value for the remanent field at the sample would make that evidence much stronger. A reader will also ask about the stray field of the CrBr3 flake. Near a flake edge that field can point opposite to the flake's magnetization. Your SM sign-convention check is useful, and an edge map or spacer device would add to it.

## Related work

- Hou et al. 2023, "Ubiquitous Superconducting Diode Effect in Superconductor Thin Films", <https://arxiv.org/abs/2205.09276>. Diode effects in plain Nb and V films at fields near 1 Oe from vortex barriers and Meissner screening, and a non-volatile 65% effect with the ferromagnetic insulator EuS.
- Golod and Krasnov 2022, "Demonstration of a superconducting diode-with-memory, operational at zero magnetic field with switchable nonreciprocity", <https://arxiv.org/abs/2205.12196>. Zero-field diodes above 70% efficiency in Nb junctions, from self-fields plus a trapped Abrikosov vortex, with polarity switched by trapping or removing the vortex.
- Li, Jiaxu et al. 2025, "Field-Free Superconducting Diode Enabled by Geometric Asymmetry and Perpendicular Magnetization", <https://arxiv.org/abs/2506.17651>. A large field-free effect in Pt/Co/Nb from stray fields of a perpendicular magnet, through asymmetric vortex entry and pinning.
- Zapata et al. 2026, "Field-free superconducting diode and tunable vortex dynamics in NbN/FePt stripe-domain heterostructures", <https://arxiv.org/abs/2610.30556>. Field-free efficiencies of 50 to 60% that persist at 35 to 40% with an AlN spacer cutting electronic proximity, read as vortex transport in the magnet's stray field.
- Li, Jiajun et al. 2025, "Field-free superconducting diode effect of NbSe2 induced by strain", <https://arxiv.org/abs/2509.23707>. A field-free effect in strained NbSe2 with no magnet, whose field dependence is B-odd in some devices and B-even in others.

Happy to rerun this if you share the Supplementary Material and the field-sweep data.
