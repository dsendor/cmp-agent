# Lookalike check: Mixed triplet-singlet order in decoupled 1H-TaS2 (arXiv 2509.13303v1)

*AI only. Written by the lookalike assistant on 2026-10-25 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport. A lookalike is an ordinary effect that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your paper is scanning tunneling spectroscopy, ARPES and transport on a bulk
superconductor, which is outside the library's device focus. Only the practice checks and the
selection entry apply directly, so I added two lookalikes from outside the library, each
with a source I opened.

**The claim, as I read it.** On the 1H-TaS2 termination of cleaved (SnS)1.15(TaS2), the
tunneling spectrum at 0.3 K shows two gaps, 490 and 300 µeV (Fig. 4a and 4c, Supp. Figs. 2
and 3). Alongside it is a concave Hc2(T) fitted by a two-gap model (Fig. 2b). A tight-binding
model reproduces two gaps as singlet-triplet mixing when interlayer hopping vanishes
(Fig. 5).

## Checks a careful reader will look for

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Not done. "Electrical transport measurements were performed on single crystals in a four-probe configuration" (p. 2) gives no count; nor do the STM sections.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. Transport ranges are given ("in the range 1.7 K ≥ T ≥ 300 K", Fig. 2a caption; fields to 14 T in Supp. Fig. 1). The 1H gap is shown at one temperature ("T=0.3K", Fig. 4 caption) over ±1.5 mV, with no reason given for the shown ranges.
3. Give the processing steps from raw data to figures, with data and code : Partly. The fit functions are written out ("The two gap model which was used is given by:", Supp. p. 3) and the Hc2 criterion is stated (p. 2). The fitted weights, effective temperature and lock-in modulation for Fig. 4a are missing, and no data or code are linked.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Fine-tuning and selection | Tested in part | Devices and datasets measured, and how many showed the effect: no; How the shown data were chosen: part; A second device or dataset shown: part | "The superconducting gap in the 1H layer taken as an average of 150 different points." (Supp. Fig. 3, Supp. p. 4) | State crystals, cleaves and tips measured, and show the 1H spectrum from a second cleave or crystal. |
| Conventional multiband or anisotropic s-wave gap, with gaps on different Fermi pockets (not in library) | Not tested (argued, not tested) | Gap features assigned to Fermi-surface sheets: no; Temperature dependence of both gap features up to Tc: no | "However, unlike in the singlet-triplet mixing scenario, this type of mixing is not expected to depend strongly on interlayer coupling." (Supp. p. 10) | Track both d2I/dV2 features from 0.3 K to Tc, and place each gap on a pocket (quasiparticle interference, or field dependence of each feature). |
| Proximity coupling of the surface 1H layer to the superconducting SnS layer, giving a McMillan two-feature spectrum (not in library) | Not tested (argued, not tested) | Joint coupled-layer (McMillan) fit of the 1H and SnS spectra: no; Same layer compared with a weakly coupled neighbour: no | "the absence of a second proximity gap, and the high anisotropy of transport all argue against a proximity scenario." (p. 7) | Fit Fig. 4a and 4b together with a two-layer McMillan model, coupling free, and report the bound on the coupling. |

## Questions about devices and data

1. How many crystals did you measure by transport and how many cleaves, tips and areas by STM, and how many of these showed the two-gap spectrum on the 1H termination?
2. Why were the others set aside, if any were?
3. Which ranges did you measure beyond the ones shown, in particular a temperature series of the 1H spectrum between 0.3 K and Tc, fields between 0 and 1 kG, and spectra on other 1H areas?
4. What does the second-best dataset look like? The zero-field 1H spectrum in Supp. Fig. 4b seems, by my reading, to have coherence peaks nearer ±0.45 mV than the ±0.53 mV of Fig. 4a; does it show the 300 µeV kink, and what differs between the two (tip, area, cooldown, setpoint)?
5. What are the fitted weights N1 and N2, the effective temperature and the lock-in modulation for Fig. 4a, and how much do Δ2 and the fit quality change if the broadening is fixed at the value that fits the SnS spectrum? The single-gap fit in Supp. Fig. 2 needed an effective temperature of 900 mK.
6. Since the SnS gap (440 µeV) sits between your two 1H gaps, have you fit the 1H and SnS spectra together with a coupled-layer McMillan model, and what interlayer coupling does such a fit allow?
7. Can you place each gap on a Fermi pocket, for example with quasiparticle interference or the field dependence of each d2I/dV2 feature, so that a K/K′ imbalance can be told apart from a Γ-versus-K multiband gap? A region with different interlayer coupling in the same crystal would test the predicted t⊥ dependence.
8. You write that for the concave Hc2(T) "alternative explanations have also been proposed [63–66]" (p. 2); which of these did you compare with your data, and do the Hc2 fits constrain the ratio of the two gaps seen by STM?

## Related work

- Guillamon et al. 2008, "Superconducting density of states and vortex cores of 2H-NbS2", <https://arxiv.org/abs/0807.1809>. Two STM gap features in a bulk 2H dichalcogenide, both closing at Tc, read as gaps on different Fermi-surface sheets.
- Tao et al. 2022, "Multi-Band Superconductivity in Strongly Hybridized 1T'-WTe2/NbSe2 Heterostructures", <https://arxiv.org/abs/2203.05171>. A multi-band McMillan fit of STM spectra on a layer coupled to a superconducting substrate.
- Kohen et al. 2004, "Two regimes in the magnetic field response of superconducting MgB2", <https://arxiv.org/abs/cond-mat/0403700>. In STM the π-band gap fills fast up to 0.5 T and slowly after, which the authors read as intrinsic and interband-induced parts of a two-band density of states.
- Kuzmanović et al. 2021, "Tunneling spectroscopy of few-monolayer NbSe2 in high magnetic field: Ising protection and triplet superconductivity", <https://arxiv.org/abs/2104.00328>. A single tunneling gap in flakes up to about 15 layers, and bilayer behavior near the critical field explained with equal-spin triplet pairs.
- Devarakonda et al. 2019, "Clean 2D superconductivity in a bulk van der Waals superlattice", <https://arxiv.org/abs/1906.02065>. A bulk 2H-NbS2 superlattice with strongly enhanced two-dimensionality, a structural analogue of your crystal.

Two small things I noticed while reading. Tc appears as 3.05 K (p. 2), 3.1 K (abstract) and 3.14 K (Fig. 2 caption), and the vortex coherence length as 35 ± 5 nm (p. 4) and 45 ± 10 nm (Supp. p. 5). The Fig. 4 caption also points to Figs. 1c and 1e for the topographies.

Happy to rerun this if you share the spectra and fit files.
