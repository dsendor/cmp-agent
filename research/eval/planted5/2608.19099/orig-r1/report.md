# Lookalike check: Field-free superconducting diode in NbSe2/CrBr3 (arXiv 2608.19099v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport: ordinary effects that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. I worked from the extracted text of v1 and its figure captions. The Supplementary Material was not available to me, so I could not count controls that appear only there.

**The claim, as I read it.** You report unequal critical currents at zero applied field in a NbSe2/CrBr3 heterostructure, reaching η = −35.7% after field training in device #1 (Figs. 1(d), 2(c), 3(b)). The diode polarity depends on field history (Fig. 2, and Fig. 3(a) for device #3 after ±6 T). You attribute the nonmonotonic, hysteretic sign reversals (Bcf < 0, Bcb > 0) to an interfacial exchange field from layered ferrimagnetic CrBr3, acting through a cubic odd-in-q Ginzburg–Landau term (Fig. 4).

## Checks a careful reader will look for

The library has no diode-specific checks, so these are the practice checks that apply to every paper.

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. "Similar behavior is also observed in another device #2, as shown in Supplementary Material (SM) [40]." (p. 2). Three devices are named. Totals fabricated and measured, and how many showed the effect, are not given.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. "as the field sweeps from −50 mT to 0 mT" (p. 2) and "at 200 mK (device #1)" (Fig. 2 caption) give the shown ranges. Ranges measured beyond these, and the reasons for each choice, are not stated.
3. Give the processing steps from raw data to figures, with data and code : Partly. "The peaks in the differential resistance correspond to the critical current along the horizontal axis." (p. 2). The η formula is given. How dV/dI was obtained, and whether data and code are available, are not stated.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Meissner screening and asymmetric vortex barriers | Tested in part | Same measurement on a plain film of the parent superconductor: no; Effect followed against field, sample width or edge quality: part (field sweep for device #1 only, Fig. 2) | "Other trivial mechanisms for the zero-field SDE (e.g., self-fields, Meissner screening, and geometric asymmetry) are ruled out, as shown in SM [40]." (p. 4) | Put the SM control in the main text: a bare NbSe2 flake, or an uncovered segment, taken through the same field history, plus fine field steps near zero with the magnet offset calibrated |
| Trapped vortices after field training (not in library) | Tested in part | Trapped vortices present versus removed: part (one zero-field-cooled point, device #1, with the CrBr3 state also different); Different bias configuration: no | "the original efficiency after zero-field cooling is −15.2%, as shown in Fig. 1(d)" (p. 2) | After training, warm at zero field above the NbSe2 transition but below the CrBr3 ordering temperature, cool again, and remeasure η |
| Dipolar stray field of the CrBr3 layer (not in library) | Not tested (data bear on it) | Insulating spacer between NbSe2 and CrBr3: no; Current direction relative to domain structure: no | "The micromagnetic simulations reproduce the RMCD hysteresis" (p. 4) | Overlay η(B) from Fig. 2(c) on the measured RMCD loop: a stray field tracks net magnetization. An hBN-spacer device would separate the two |
| Fine-tuning and data selection | Tested in part | Devices and datasets measured, and how many showed the effect: part; How the shown data were chosen: no; A second device or dataset shown: part (device #3 in Fig. 3(a); device #2 only in the SM) | "our NbSe2 /CrBr3 devices consistently exhibit the opposite condition, Bcf < 0 and Bcb > 0" (p. 3) | A table of every device with η after zero-field cooling and after training, Bcf, Bcb, and the layer thicknesses |

A note on the first row. Your Fig. 2(c) shows η going from +45.3% at about −10 mT to −35.7% at 0 mT, so the diode is very steep in field near zero. Hou et al. find a screening-driven diode in plain films at fields as small as about 1 Oe. That makes the true field at the sample during the "zero field" points worth stating, including any remanent field of the magnet after the ±50 mT and ±6 T excursions.

On the second row, Golod and Krasnov show a zero-field diode in plain Nb junctions from a trapped Abrikosov vortex, switched on and off by trapping and removing the vortex. Your perpendicular training fields could leave flux in NbSe2. Your zero-field-cooled value (−15.2%) already helps here, because a diode is present before any training. The warm-and-recool step above would say whether the jump to −35.7% after training lives in the superconductor or in the magnet. It can be done on device #1 as it is.

On the third row, Zapata et al. separate stray-field and proximity effects with a thin insulating spacer that keeps the stray field and cuts the exchange coupling. Your argument that the interfacial layer can oppose the net magnetization predicts that the sign changes do not follow the net-magnetization loop, and a stray field predicts that they do. Your RMCD data and Fig. 2(c) are the data that bear on this.

## Questions about devices and data

1. How many NbSe2/CrBr3 devices did you fabricate and measure, and how many showed the field-free diode effect and the inverted sign-change fields (Bcf < 0, Bcb > 0)?
2. Why were the others set aside?
3. Which ranges of field (sweep amplitude and step), temperature and bias current did you measure beyond the ones shown, for example beyond the ±50 mT sweeps at 200 mK in Fig. 2?
4. What does the second-best device or dataset look like? Device #2 is in the SM; for device #3 in Fig. 3(a), what are |Ic+| and |Ic−| at zero field, and how was the 705 µA bias chosen?
5. What is the remanent field of your magnet at nominal zero after the ±50 mT sweeps and after the ±6 T training, and how did you measure it? Since η goes from 45.3% at about −10 mT to −35.7% at 0 mT, an offset of a few mT would matter.
6. If you train device #1, then warm it at zero field above the NbSe2 transition but below the CrBr3 ordering temperature and cool again, does the −35.7% survive, or does η return toward the −15.2% you see after zero-field cooling?
7. Have you measured a bare NbSe2 flake, an uncovered part of the same flake, or a NbSe2/hBN/CrBr3 stack through the same field history, and could the self-field, Meissner and geometric-asymmetry controls from the SM appear in the main text?
8. What are the NbSe2 and CrBr3 thicknesses (layer numbers) in each device, and how do you extract Ic from the dV/dI peaks (lock-in or numerical derivative, current step); could you share the raw V(I) data behind Figs. 1(d) and 2(c)?

## Related work

- Hou et al. 2023, "Ubiquitous Superconducting Diode Effect in Superconductor Thin Films", <https://arxiv.org/abs/2205.09276>. A strong diode in plain Nb and V films at fields as small as 1 Oe, from asymmetric vortex barriers and Meissner screening, and a non-volatile diode of up to 65% with a EuS ferromagnet.
- Golod and Krasnov 2022, "Demonstration of a superconducting diode-with-memory, operational at zero magnetic field with switchable nonreciprocity", <https://arxiv.org/abs/2205.12196>. A zero-field diode in conventional Nb junctions from a trapped Abrikosov vortex plus self-field, with polarity and on/off set by vortex trapping and bias configuration.
- Zapata et al. 2026, "Field-free superconducting diode and tunable vortex dynamics in NbN/FePt stripe-domain heterostructures", <https://arxiv.org/abs/2610.30556>. A field-free diode of about 50 to 60% from magnet stray fields that persists, at about 35 to 40%, with an AlN spacer that suppresses proximity coupling.
- Bauriedl et al. 2022, "Supercurrent diode effect and magnetochiral anisotropy in few-layer NbSe2", <https://arxiv.org/abs/2110.15752>. A diode of up to 60% in NbSe2 constrictions, driven by an out-of-plane field component.
- Xiong et al. 2024, "Electrical switching of Ising-superconducting nonreciprocity for quantum neuronal transistor", <https://arxiv.org/abs/2406.14417>. Field-free, electrically switchable nonreciprocity in Fe3GeTe2/NbSe2 heterostructures.

Happy to rerun this if you share the Supplementary Material and the figure data.
