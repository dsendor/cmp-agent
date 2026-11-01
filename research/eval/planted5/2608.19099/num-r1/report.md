# Lookalike check: Large field-free superconducting diode effect in NbSe2/CrBr3 (arXiv 2608.19099v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. The library is built around topological transport; I used its superconducting diode entry and its practice checks, which fit a diode measurement directly. I worked from the main text only; the Supplemental Material [40] was not available to me, so anything shown only there is marked as not shown.

**The claim, as I read it.** A zero-field superconducting diode effect in NbSe2/CrBr3 with efficiency up to 35.7% (device #1, Figs. 1 to 3), whose polarity is set by field history (device #1, Fig. 2; device #3, Fig. 3(a)) and reverses nonmonotonically and hysteretically in perpendicular field, read as a cubic odd-in-q term driven by the interfacial exchange field of layered ferrimagnetic CrBr3.

## Checks a careful reader will look for

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. "Similar behavior is also observed in another device #2, as shown in Supplementary Material (SM) [40]." (p. 2). Three devices are named; totals fabricated and measured are not given.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. "as the field sweeps from −50 mT to 0 mT, the SDE efficiency first reaches a maximum positive value of 45.3% at around −10 mT" (p. 2). Shown ranges are stated; ranges beyond them and the reasons for them are not.
3. Give the processing steps from raw data to figures, with data and code : Partly. "The peaks in the differential resistance correspond to the critical current along the horizontal axis." (p. 2). The Ic and η definitions are given; there is no data or code statement.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Vortex edge barriers and Meissner screening (diode-vortex-screening) | Tested in part | Plain-film control: no; effect vs field, width or edges: part (field sweep for device #1 only) | "Other trivial mechanisms for the zero-field SDE (e.g., self-fields, Meissner screening, and geometric asymmetry) are ruled out, as shown in SM [40]." (p. 4); field sweep in Fig. 2 | Bring the SM control into the main text, with fine field steps within about ±1 mT of a measured zero |
| Fine-tuning and selection | Tested in part | Counts: part; how data were chosen: no; second device: part (device #3 in Fig. 3(a), device #2 in SM) | "Similar behavior is also observed in another device #2, as shown in Supplementary Material (SM) [40]." (p. 2) | A table of every device: zero-field-cooled η, trained η, Bcf and Bcb |
| Trapped Abrikosov vortex, diode with memory (not in library) | Tested in part | Zero-field-cooled η: part (device #1 only); warm above NbSe2 Tc, below CrBr3 ordering: no | "the original efficiency after zero-field cooling is −15.2%, as shown in Fig. 1(d)." (p. 2) | Warm above the NbSe2 Tc while keeping CrBr3 ordered, cool in zero field, remeasure η |
| Strain-induced polarity in NbSe2 (not in library) | Tested in part | Bare NbSe2 control: no; polarity reversed by training: all (devices #1 and #3) | "initial magnetization with a −6 T field reoriented the CrBr3 magnetization to a negative state" (p. 3, Fig. 3(a)) | Average η of the two trained states to extract any fixed offset; compare with a bare NbSe2 device |

A few notes on the table. Your Fig. 2 field sweep is a real strength: it follows the diode efficiency through ±50 mT in both sweep directions, which is the data a screening-current picture would need. Because it covers device #1 only, and the plain-film control sits in the SM, I counted it as part of what that entry asks for. Hou et al. find screening diodes at fields as small as about 1 Oe, so the actual field at nominal zero after a 6 T training matters; a Hall-sensor reading would settle it.

The trapped-vortex row comes from Golod and Krasnov, who show a zero-field diode with memory from a single trapped vortex, with efficiency above 70%, switched by trapping or removing it. Your zero-field-cooled value of −15.2% speaks to the untrained state; the trained states are where trapped flux could add. Warming between the two transition temperatures separates the two cleanly, since it clears vortices from NbSe2 and leaves CrBr3 magnetized.

The strain row comes from Li et al., who report a field-free diode in bare NbSe2 from strain. Your training-reversed polarity in devices #1 and #3 shows a magnetic part; a fixed strain offset could still sit underneath, and the −15.2% after zero-field cooling is where it would show. Half the sum of the two trained zero-field efficiencies, from data you already have, measures that offset.

Two numbers on p. 2 and p. 3 look worth a second look before submission; they are in question 5.

## Questions about devices and data

1. How many devices did you fabricate and measure, and how many showed a field-free diode effect? The paper names devices #1, #2 and #3.
2. Why were any others set aside, and how was device #1 chosen for Figs. 1, 2 and 3(b)?
3. Which field, temperature and training ranges did you measure beyond the ones shown (sweeps between -50 and 50 mT at 200 mK, training at plus and minus 6 T)?
4. What does the second-best device look like? Could the field sweep of device #2 and the zero-field efficiency of device #3 appear in the main text, next to device #1?
5. Your p. 2 gives the trained field-free efficiency as "−71.4%", while the same paragraph, the abstract and Fig. 3(b) give 35.7% at 0 mT. Which value is right, and which sweep or state does each describe? Relatedly, what are |Ic+| and |Ic−| for device #3, so a reader can place the 705 µA excitation of Fig. 3(a) between them, given that Fig. 1(c) sweeps only to 300 µA in device #1?
6. How was zero applied field set and checked after the 6 T training and the 50 mT sweeps? Was the magnet's remanent field measured, for example with a Hall sensor, given that Meissner-screening diodes appear at fields near 1 Oe?
7. Does the trained diode state survive warming above the NbSe2 Tc, staying below the CrBr3 ordering temperature, and cooling back in zero field? That would separate trapped vortices from the CrBr3 magnetization.
8. Could you show the control in SM [40] in the main text: a bare NbSe2 flake or a NbSe2 region without CrBr3 from the same process and contact geometry, measured the same way? It sets the baseline from strain, edges and geometry, and helps explain the −15.2% after zero-field cooling.

## Related work

- Hou et al. 2023, "Ubiquitous Superconducting Diode Effect in Superconductor Thin Films", <https://arxiv.org/abs/2205.09276>. Diode effect in plain Nb and V films at fields near 1 Oe from edge barriers and Meissner screening, and a non-volatile 65% diode with a EuS ferromagnet.
- Golod and Krasnov 2022, "Demonstration of a superconducting diode-with-memory, operational at zero magnetic field with switchable nonreciprocity", <https://arxiv.org/abs/2205.12196>. Zero-field diode above 70% efficiency from self-field plus a trapped Abrikosov vortex, switched by trapping or removing the vortex.
- Li et al. 2025, "Field-free superconducting diode effect of NbSe2 induced by strain", <https://arxiv.org/abs/2509.23707>. Field-free diode in NbSe2 with no magnet, attributed to strain, with B-odd or B-even field behavior varying between devices.
- Gutfreund et al. 2023, "Direct Observation of a Superconducting Vortex Diode", <https://arxiv.org/abs/2301.07121>. Scanning SQUID imaging of a tunable vortex diode in Nb/EuS superconductor/ferromagnet bilayers.
- Zapata et al. 2026, "Field-free superconducting diode and tunable vortex dynamics in NbN/FePt stripe-domain heterostructures", <https://arxiv.org/abs/2610.30556>. Field-free diode of 50 to 60% from asymmetric vortex transport in the stray field of magnetic domains, persisting with an insulating spacer that suppresses electronic proximity.

Happy to rerun this with the Supplemental Material or the figure data if you share them.
