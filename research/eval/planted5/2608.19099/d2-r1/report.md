# Lookalike check: Field-free diode effect in NbSe2/CrBr3 (arXiv 2608.19099v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your signal falls in the library's superconducting diode family, which has no
ordered checks of its own yet, so the checks below are the general practice checks.

**The claim, as I read it.** A field-free superconducting diode effect in an NbSe2/CrBr3
heterostructure, reaching η = −35.7% at zero applied field after field training (device
#1, Figs. 1(c), 1(d) and 2(c), 200 mK), with a polarity set by field history (Fig. 2(c);
device #3, Fig. 3(a)) and nonmonotonic, hysteretic polarity reversals with Bcf < 0 and
Bcb > 0, which you attribute to an interfacial exchange field from layered ferrimagnetic
CrBr3 acting through a cubic odd-in-q term (Fig. 4).

## Checks a careful reader will look for

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. "our NbSe2/CrBr3 devices consistently exhibit the opposite condition, Bcf < 0 and Bcb > 0" (p. 3); devices #1 and #3 are shown, and the total measured and the number that showed the effect are not given.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Not done. The shown ranges are stated (−50 to 50 mT at 200 mK in Fig. 2, ±6 T training in Fig. 3(a)); the ranges measured beyond them, and why these were chosen, are not.
3. Give the processing steps from raw data to figures, with data and code : Partly. "The peaks in the differential resistance correspond to the critical current along the horizontal axis." (p. 2); the current step, any threshold, and a data or code link are not given.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Meissner screening and asymmetric vortex barriers (diode-vortex-screening) | Tested in part | Same measurement on a plain film of the parent superconductor: no; effect followed against field, sample width or edge quality: part (field sweep for device #1 in Fig. 2, device #3 only at zero field) | "Other trivial mechanisms for the zero-field SDE (e.g., self-fields, Meissner screening, and geometric asymmetry) are ruled out, as shown in SM [40]." (p. 4) | Bring the SM control into view: a bare NbSe2 device, or a bare part of the same flake, under the same ±50 mT sweeps and ±6 T training, with the zero of field calibrated after each excursion. |
| Trapped vortex plus self-field, a diode with memory (not in library; Golod and Krasnov 2022) | Tested in part | Diode response after removing trapped flux (zero-field cooling from above Tc): part (device #1, Fig. 1(d)); bias configuration changed: no | "the original efficiency after zero-field cooling is −15.2%, as shown in Fig. 1(d)." (p. 2) | On devices #1 and #3, warm above Tc and cool in a calibrated zero field after each training, then swap the current and voltage contacts and compare η. |
| Strain-induced field-free diode (not in library; Li et al. 2025, Zhu et al. 2026) | Tested in part | Polarity reversed by reversing the magnetization: all (Figs. 2(c), 3(a)); field-even and field-odd parts of ΔIc separated: no | "initial magnetization with a −6 T field reoriented the CrBr3 magnetization to a negative state, This inverts the critical current asymmetry to \|Ic−\| > \|Ic+\|" (p. 3, Fig. 3(a)) | From your Fig. 2(c) data, combine the forward sweep at B with the backward sweep at −B to split ΔIc into its even and odd parts, and report the even part at zero field. |
| Fine-tuning and selection (fine-tuning-and-selection) | Tested in part | Devices and datasets measured, and how many showed the effect: part; how the shown data were chosen: no; a second device or dataset shown: part (device #3, Fig. 3(a) only) | "Zero-field rectification of NbSe2/CrBr3 heterostructure after applying perpendicular magnetic fields of 6 T and −6 T in device #3." (Fig. 3(a) caption, p. 4) | Give the device counts, and show the Fig. 2 field sweep for device #3 and any other devices in the SM. |

## Questions about devices and data

1. How many devices did you fabricate and measure, and how many showed a field-free diode effect with Bcf < 0 and Bcb > 0? Your text says "our NbSe2/CrBr3 devices consistently exhibit the opposite condition" (p. 3), and the figures show devices #1 and #3.
2. Why were the others set aside, including device #2 if it was measured?
3. Which ranges of field, temperature and training field did you measure beyond the ones shown (Fig. 2 covers −50 to 50 mT at 200 mK), and how fine was the field step near zero?
4. What does the second-best device or dataset look like, for example the Fig. 2 field sweep on device #3?
5. How did you set and check zero applied field after the ±6 T and ±50 mT excursions? Your η moves from 45.3% at around −10 mT to −35.7% at 0 mT (p. 2), so a remanent field of a few mT in the magnet would matter.
6. Which SM figure shows the control that rules out Meissner screening and self-fields, and does it include a bare NbSe2 device or region measured with the same field training?
7. What sets the sign of the −15.2% efficiency after zero-field cooling, and how large is the field-even part of ΔIc when you compare positive and negative training at zero field?
8. How did you extract |Ic+| and |Ic−| from dV/dI (peak position or a threshold, current step, number of sweeps), and will you share the raw V(I) data?

## Related work

- Hou et al. 2023, "Ubiquitous Superconducting Diode Effect in Superconductor Thin Films", <https://arxiv.org/abs/2205.09276>. Shows strong diode effects in plain Nb and V films at fields as small as 1 Oe from asymmetric vortex barriers and Meissner screening, and a non-volatile diode reaching 65% with a ferromagnetic EuS layer.
- Golod and Krasnov 2022, "Demonstration of a superconducting diode-with-memory, operational at zero magnetic field with switchable nonreciprocity", <https://arxiv.org/abs/2205.12196>. Shows zero-field diodes in conventional Nb planar junctions from self-field plus a trapped Abrikosov vortex, with efficiency above 70% and polarity switched by bias configuration or by trapping and removing the vortex.
- Li et al. 2025, "Field-free superconducting diode effect of NbSe2 induced by strain", <https://arxiv.org/abs/2509.23707>. Reports a field-free diode effect in NbSe2 attributed to strain, with ΔIc showing B-odd or B-even field dependence in different devices.
- Zhu et al. 2026, "Pressure induced magnetic-field-free superconducting diode effect in NbSe2 flake", <https://arxiv.org/abs/2608.03072>. Reports a field-free diode effect in NbSe2 flakes under pressure with no heterostructure, even in out-of-plane field.
- Xiong et al. 2024, "Electrical switching of Ising-superconducting nonreciprocity for quantum neuronal transistor", <https://arxiv.org/abs/2406.14417>. Reports field-free, electrically switchable nonreciprocal Ising superconductivity in Fe3GeTe2/NbSe2 heterostructures, a ferromagnet and Ising superconductor comparison point.

Happy to rerun this if you share the figure data and the Supplemental Material.
