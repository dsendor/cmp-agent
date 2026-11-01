# Lookalike check: Field-free superconducting diode controlled by an antiferromagnet (arXiv 2609.38003v1)

*AI only. Written by the lookalike assistant on 2026-10-23 from arXiv version v1, with
lookalike library version 0.4. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your claim is antiferromagnetic control of a field-free diode, which sits next to the library's diode entry (read there as exotic pairing), so I adapted that entry and added three ordinary mechanisms from papers I opened, marked "(not in library)".

**The claim, as I read it.** A 5 µm by 180 µm CuMnAs/AlAs/Al bar at 20 mK shows unequal switching currents at H = 0 (about 7% after zero-field cooling, Fig. 3a), and the sign of the diode efficiency reverses with the sign of an in-plane preparation field along [100] (up to about ±20%, Fig. 3b,d) but not along [010] (Fig. 3e). You tie this to the remanent Néel state through the same anisotropy and hysteresis in R_even of a separate, non-superconducting CuMnAs bar at 5 K (Fig. 4), XMLD-PEEM (Extended Data Fig. 5) and a SQUID bound on net moment (Fig. 2b).

## Checks a careful reader will look for

The library has no checks written for diode signals yet, so these are the three that apply to every paper.

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. "An orthogonal bar patterned along [100] displays the same qualitative dependence on the preparation-field axes (Extended Data Fig. 4)." (p. 4 to 5). Two superconducting bars are shown; the total fabricated and measured, and the number of cooldowns, are not stated.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. "ranging from −5 to 5 T, Reven shows pronounced hysteresis" (p. 5, Fig. 4c); the preparation ranges are visible in Fig. 3d,e (±1 T along [100], ±4 T along [010]), with no reason given for the difference and no temperature series.
3. Give the processing steps from raw data to figures, with data and code : Partly. "defined as the bias current at which the measured voltage first exceeded a threshold of 50 µV" (p. 8, Methods), with eight-sweep averages; I found no data or code availability statement.

## Lookalikes

| Lookalike | Status | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|
| Meissner screening and asymmetric vortex edge barriers in an ordinary film (diode-vortex-screening) | Partly addressed | "rather than from spurious flux trapping or vortex dynamics, both known to generate SDE28,29" (p. 6); the argument rests on a non-superconducting reference bar. | Measure η versus a small out-of-plane field near zero on the same bar, and run a plain Al (or thick-barrier) bar through Fig. 3c's protocol. |
| Selection of a non-representative device or run (fine-tuning-and-selection) | Partly addressed | "An orthogonal bar patterned along [100] displays the same qualitative dependence" (p. 4, Extended Data Fig. 4). | Report all bars and cooldowns, and show the zero-field-cooled η and its sign for each. |
| Trapped flux written by the preparation field (not in library) | Partly addressed | "the anisotropic remanence itself originates in CuMnAs rather than from spurious flux trapping" (p. 6); inferred from a 5 K bar on another wafer. | After preparing L+ or L−, warm above the Al transition at H = 0 and recool; flux leaves, the Néel state stays (T_N 480 K, p. 3). |
| Remanent field of the superconducting magnet after an excursion (not in library) | Partly addressed | "produces a substantially weaker response which shows no systematic reversal" (p. 4, Fig. 3e); the data bear on it; the paper doesn't discuss it. | Calibrate the residual field after each excursion with a Hall sensor or a non-hysteretic reference, and rotate the chip 90° relative to the magnet. |
| Stray field from uncompensated magnetization (not in library) | Partly addressed | "this also disfavors a stray-field mechanism associated with uncompensated magnetization30" (p. 6, Fig. 2b SQUID). | Check whether η versus small out-of-plane field shifts between prepared states, which would point to an effective local field at the patterned bar. |

## Questions about devices and data

1. How many devices did you measure, and how many showed the reversible field-free diode? Your p. 4 and Extended Data Fig. 4 show two bars, one along [010] and one along [100]; were there others, on this chip or other chips, and over how many cooldowns?
2. Why were the others set aside?
3. Which ranges did you measure beyond the ones shown: preparation fields along [100] beyond ±1 T (Fig. 3d stops there while Fig. 3e goes to ±4 T), temperatures above 20 mK, and small applied fields near zero, in plane and out of plane?
4. What does the second-best device or dataset look like, for example the [100] bar's zero-field-cooled efficiency and its switching-current distributions, and the sign of the 7% zero-field-cooled efficiency in other cooldowns?
5. After you prepare one remanent state, if you warm the bar above the Al transition at H = 0 and cool again, does η keep its sign and size?
6. What is the residual field of your magnet at the sample after the ±1 T and ±4 T excursions, and how did you calibrate it? Does η versus a small out-of-plane field near zero shift between the two prepared states?
7. Were both bars on the same chip and mounting, so that the [100] crystal axis sat along the same magnet axis for both? Have you rotated the chip by 90° relative to the magnet and repeated Fig. 3d,e?
8. Can you read the Néel state on the superconducting wafer itself, for example R_even on the bar above the Al transition, so that the Fig. 4 comparison comes from the same film and device as Fig. 3?

A note on questions 5 to 8. Your strongest argument is the shared crystal-axis anisotropy (p. 6: "Neither mechanism is naturally expected to track the Néel-vector anisotropy observed here."). A thin film in an in-plane field picks up an out-of-plane component from any small tilt, and that tilt can differ between two magnet axes. If both bars shared a mounting, the [100] crystal axis and one magnet axis coincide for both, so the orthogonal-bar test (Extended Data Fig. 4) would not yet separate the two. The thermal cycle in question 5 is quick to run on the setup you have and speaks directly to trapped flux. The Fig. 4 reference comes from "a CuMnAs wafer with 3 nm fully oxidized Al cap" (p. 8, Methods) measured at 5 K, which is why question 8 asks for a readout on the same film.

## Related work

- Hou et al. 2023, "Ubiquitous Superconducting Diode Effect in Superconductor Thin Films", <https://arxiv.org/abs/2205.09276>. Shows strong diodes in plain Nb and V films at fields as small as 1 Oe, from asymmetric vortex barriers and Meissner screening, plus a non-volatile diode with a ferromagnetic EuS layer.
- Jiang et al. 2025, "Zero-field superconducting diode effect induced by magnetic flux in a van der Waals superconductor trigonal PtBi2", <https://arxiv.org/abs/2512.05427>. A zero-field diode whose sign is set by a prior ±1 T in-plane poling field, attributed to trapped flux; they calibrate the magnet's residual field with a graphene reference.
- Golod and Krasnov 2022, "Demonstration of a superconducting diode-with-memory, operational at zero magnetic field with switchable nonreciprocity", <https://arxiv.org/abs/2205.12196>. Conventional Nb junctions give a switchable zero-field diode from a trapped Abrikosov vortex plus self-field, turned on and off by trapping or removing the vortex.
- Li et al. 2025, "Field-Free Superconducting Diode Enabled by Geometric Asymmetry and Perpendicular Magnetization", <https://arxiv.org/abs/2506.17651>. A field-free diode in Pt/Co/Nb driven by stray fields from the Co layer together with asymmetric vortex entry and pinning.
- Sachin et al. 2026, "Altermagnetic Superconducting Diode Effect in Mn3Pt/Nb Heterostructures", <https://arxiv.org/abs/2601.03366>. A zero-field diode up to 50% in Nb on compensated Mn3Pt, with field and temperature dependence that the authors say hints at several contributing mechanisms.

Happy to rerun this if you share the switching-current data behind Fig. 3 and the cooldown log.
