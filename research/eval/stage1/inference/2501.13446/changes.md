# Changes from arXiv v1 to the accepted version: 2501.13446 (CrBr3 under pressure)

AI-generated change log. Referee reports were not available; every link to a referee is inferred.
Pages are PDF pages: "old" = arXiv v1, "new" = accepted version (new pp. 22-33 are the SI).

## Title, abstract and framing
- c1 (editorial): title now "Pressure-induced structure transformation and collapse of ferromagnetism in van der Waals insulator" (old p1, new p1).
- c2 (softened, likely referee-driven): abstract rewritten. "suggests an antiferromagnetic phase emerging" (old p1) is gone. New text says the collapse "is attributed to the increasing number of AFM-coupled Cr moments in AA stackings" (new p1). It adds intrinsic trimorphism, the paracrystal model, the 8.4 GPa limit and pc above 5.8 GPa.
- c17 (strengthened): trimorphism is now "intrinsic" (new p1). A new sentence says the P-3m1 fraction is "likely unintentionally" changed by mounting (new p6).
- c31 (softened): the conclusions no longer say the AFM phase is corroborated. Microscopic probes "will be essential to resolve the nature" of the phase (old p18, new p13).

## Introduction and references
- c10 (added): prior pressure work is given in more detail: Yoshida et al. (-2 K/GPa up to 1 GPa), Lis et al. (8.4 GPa by extrapolation), Raman at 9.5 GPa, and a strain-driven FM-to-AFM prediction for the monolayer. Monolayer TC values are added. The twisted-graphene paragraph is gone (old p1-2, new p1-2).
- The reference list was rebuilt (73 main references plus an SI list). New references include Kozlenko 2021 (negative thermal expansion), Kozlenko 2025 (2D-to-3D crossover), Hendricks-Teller/Guinier/Welberry (paracrystal), Vieira 2024 (stacking faults in Gd), Gibertini 2021 (bilayer stackings) and r2SCAN+rVV10. Duplicates remain: Refs. 15/29 and 17/38 (new pp17-18).

## Magnetization
- c3 (new_analysis): the fit TC = TC(0)(1 - p/pc)^(-1/3) and "pc = 6.5 GPa" (old p6) are removed. The new value, "pc = 5.8 GPa", comes from extrapolation (new p3).
- c4 (new_data): a new data set. M(T) at 0.01 T and loops at 2 K up to 1 T, at 0, 1.92, 3.57, 5.24, 5.60 and 6.24 GPa. TC is about 4 K at 5.6 GPa and there is no FM signal at 6.24 GPa. The 9.2 GPa curves and the 10 K / 2 T isotherms are gone. Old Figs. 1-3 are merged into new Fig. 1, which now shows Msat(p) too (old p6-7, new p3-4).
- c5 (added): low-pressure AC-susceptibility TC points are now in the main phase diagram (old p6 via Fig. S2, new p4).
- c7 (new_data): two runs are shown; pc differs by about 1 GPa and is "somewhat sample-dependent" (new p3, Fig. S1a p22).
- c8 (new_data): FM "recovers after decompression from 10 GPa" with unchanged TC and Msat (new p3, p13, Fig. S1b p22).
- c6 (added): horizontal error bars show the overpressure when each point was set. The SI describes the turnbuckle-cell overshoot and a redesigned, heavier cell used for the second run (new p4, p22).

## Interpretation of the pressure effect
- c9 (added): new paragraph with the Ehrenfest relation and Kozlenko et al.'s negative thermal expansion. It argues the thermodynamic picture does not apply to vdW magnets (new p3).

## Crystal structure under pressure
- c12 (softened): the R-3 fraction plot (old Fig. 5b, p8) is removed. DAC data "does not allow for a precise quantitative analysis" of the ratio; only trends are reliable (new p5).
- c13 (new_analysis): the fraction is now explained. It comes from relative intensities of the 1/3 maxima, assuming pure phases, and is a lower bound (new p8). The fractions sit in Table S4 (ambient 0.60(5); new p32). The Methods still give ~80% for the best sample (new p14).
- c11 (new_data): XRD after decompression from 21.5 GPa (new Fig. 3d) keeps P-3m1, which is called metastable. Table S4 runs to 21.5 GPa (new p5, p32).
- c18 (new_analysis): measured and calculated a, c and the Cr-Br-Cr angle are overlaid in Fig. 2e. Old Fig. 11 showed only the calculation. Saturation of c above 11.8 GPa is attributed to 3D character (new Ref. 40) (old p15, new p5).
- Unchanged: c = 19.0(2) Å at 0.7 GPa, the negative 8.4 GPa fraction and the 6.4-8.4 GPa volume drop (new p32).

## Stacking analysis
- c15 (softened): "only one viable option which is the the A-A type stacking fault" (old p12) becomes two scenarios: randomized Cr occupancies or randomized stacking of whole planes. The authors say "we are unable to distinguish between these two scenarios" (new p6).
- c14 (new_data): reciprocal-space maps of 10-1.13 and 30-3.15 before and after mechanical deformation. A paracrystal (Hendricks-Teller) model with Poisson block lengths gives a mean block size of (10 ± 2) nm (new p7-8, Fig. 4c-h, Fig. S4 p24).
- c16 (editorial fix): the conclusions' "1/3 occupation of the Cr 1a site" (old p18) becomes 2/3 (new p13).

## Raman
- c26 (reframed): the link between the 11 GPa intensity loss and the XRD pc is removed (old p14). The change in slope is put near 10 GPa and compared with 15 GPa in Ref. 40. Hard modes are tied to a less compressible 3D P-3m1 phase (new p9). The A2g label, the metallization claim and the "polarized" description are unchanged.

## DFT
- c19 (new_analysis): U_eff is changed from 2 to 2.8 eV. Exchange is now computed with r2SCAN + rVV10, and MAE with spin-orbit coupling (old p4-5, new p15). D3 is still called a "non-local vdW functional".
- c20 (new_analysis): J1(p) and JL(p) for ABC and AA stacking (Fig. 6a). J1 first rises slightly, then falls. AA is antiparallel only "above 2 GPa". The single values JL = 0.83 / -0.35 meV are dropped (old p16-17, new p10-11).
- c21 (new_analysis): MAE(p) falls by a factor of two up to 8 GPa (new p10, Fig. S7 p26).
- DOS moved to the SI (Fig. S6). The 1.67 to 1.39 eV gap values are unchanged.

## Atomistic simulations
- c22 (new_analysis): an ABC-only Monte Carlo with pressure-dependent parameters. TC never falls below its ambient value, so "the description based on a single-phase is insufficient" (new p10, Fig. 6b).
- c23 (new_analysis): the concentration simulation is redone with 5 GPa exchange and moved to Fig. S8. TC now vanishes at 73% AA (old p16-17 stopped at 45%; new p11, p27). The leftover sentence about 45% P-3m1 remains on new p12.
- c24 (new_analysis): a "stacking variation model" has the AA fraction rise linearly up to a critical pressure. It gives a simulated TC(p) compared with experiment (new p12, Fig. 6b).
- c25 (added): new discussion of model limits. Site-random disorder is called "a standard modeling strategy". Stacking boundaries, finite-size effects and domains are discussed, and the TC-fraction relation is "rather complex" (new p11-12).

## Pressure conditions and methods
- c27 (softened/corrected): the MEW hydrostatic limit changes from ~14 to ~10.5 GPa. The remarks move to the SI with photos of samples in Daphne 7474 and MEW (old p4, new p28-30).
- c28 (added): every DAC was loaded at room temperature and read with the ruby scale (new p14).
- c29 (editorial): reformatted for the journal. Methods moved to the end; Tables 1-3, powder XRD (old Fig. 9) and the simulation M(T) (old Fig. 13a) went to the SI; figures were renumbered.
- c30 (editorial): copy fixes. "Burker" became Bruker; "badges", "subscribed", "Figure Figure" and "X-diffraction" are gone; the Fig. 4 caption (now Fig. 3) refers to pressures; stacking is labelled ABC. Still present: "space group 150", two equations numbered (1), "We have invented the identical procedure", and 289 K vs 296 K in Table S1.
