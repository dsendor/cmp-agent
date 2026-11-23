A. Must address

None. The main claims are supported by evidence a referee would accept: two field-separated texture families of opposite net polarity, textures confined to the CoFeB sublattice, and reproducible family-specific nucleation sites. One review placed the XMCD decomposition (item 1) here. The single-sublattice assignment can, however, be established without the fitted scaling factor, from the Fe-edge loop amplitude combined with the SQUID moment change. So the item is placed under B, as a change needed to make the paper's evidence rest on that argument.

B. Should address

1. The CoB-only loop depends on an empirically tuned scaling factor, fitted to a SQUID loop from a different sample (Eqs. 1–2; Fig. 3c,d; Methods, "Soft X-ray techniques", p. 17). The CoB loop is obtained as I_CoB = I_Co − a·I_Fe, with a = 0.35 "determined empirically by adjusting a until the reconstructed total loop matched the SQUID-VSM loop, with a closed central area." The agreement in Fig. 3c is therefore built in, not a validation. The squareness of the reconstructed CoB loop in Fig. 3d, which is the paper's only direct element-resolved evidence that "the CoB sublattice remains laterally uniform", also depends on a. That flatness above |μ0H| = 30 mT holds only if a also equals the ratio of the high-field slopes of I_Co and I_Fe. Further, one parameter is being asked to do two physically different jobs. It has to give (i) the fraction of the Co-edge signal that comes from Co in Co40Fe40B20, relative to the Fe-edge signal of the same layers. It also has to give (ii) the relative sensitivity of the Fe- and Co-edge measurements (dichroism per unit moment, absorption, detector response), which puts I_Fe and I_CoB on a common moment scale. Eq. 1 adds I_Fe and I_CoB with unit weight, which implicitly fixes (ii) as 1 − a, so the plateau-matching condition does not independently determine the Co-in-CoFeB contribution. The SQUID loop used for calibration was measured on the Si/SiO2 sister sample, not on the 200 nm Si3N4 membrane used for XMCD. In addition, transmitted intensity depends exponentially on absorption, so the linear relation I(H) ∝ m(H) assumed in Eqs. 1–2 and in the Fig. 3 caption needs a justification or a −ln(I/I0) treatment. Without these, "unequivocally attribute the observed textures to the CoFeB sublattice" (p. 4) is overstated. The DPC step cannot decide which sublattice reverses, because Ms·t is the same for both. A stronger argument that does not depend on a is available from the paper's own data. Fig. 3b shows I_Fe spanning its full range over about 30–130/160 mT. The two sublattice moments are equal (Table 1). The net SQUID moment (Fig. 1c) rises by 2m_CoFeB over the same window. The mean CoB moment therefore cannot change there, and since it is saturated at both ends, CoB stays uniform. The authors should:
   - state this a-independent argument explicitly and rest the claim on it;
   - show I_CoB(H) for a range of a (for example 0.25–0.45), say which features are robust (the high-field flatness, the square switching at ±30 mT), and give the largest CoB reversal fraction consistent with the noise (it looks like roughly 5% of the loop amplitude);
   - estimate a independently, from composition (Co40Fe40B20 against Co68B32), thicknesses (6.69 against 8.69 Å; about 7 nm against 9 nm in total) and tabulated or measured L3 dichroism, ideally by measuring both edges on the CoB-only and CoFeB-only reference multilayers already grown for the Keff measurements;
   - introduce a separate normalisation factor for Eq. 1;
   - justify linearity in m, or test the log-ratio conversion.

   Raised by: r1, r2, r3

2. The value and meaning of J_RKKY are uncertain, and the effective-field mechanism is only qualitative (Methods p. 16; Table 1; Table 2; Eq. 4; Discussion pp. 12–13; Fig. 6). The central explanation is that the field on CoFeB, H_ext − H_RKKY, changes sign between the two families, and J_RKKY is fed directly into the simulations.
   - (a) J_RKKY = −0.034 mJ/m² comes from J = μ0Hs·Ms·t_FM/2 with μ0Hs = 125 mT. This is the bilayer expression. In a 20-layer stack, interior layers are coupled on both sides, and coherent saturation would give roughly half the |J| (about −0.017 mJ/m²). The outermost layers have only one neighbour. More fundamentally, the paper's own data show that this perpendicular SAF saturates through domain and skyrmion formation and collapse. The saturation field therefore also contains magnetostatic and domain-wall contributions and is not a coherent spin-flip field. The quoted Hs of 125 mT also differs from the saturation seen in Fig. 1c and MFM (about 150 mT, with skyrmions still present at 120 mT).
   - (b) With this J, the interlayer field on an interior CoFeB layer is 2|J|/(Ms t) ≈ 125 mT. On the paper's own picture (Fig. 6), the effective field on CoFeB should then vanish near 125 mT, where the maze should sit. Experimentally the maze is at about 80 mT and conventional skyrmions are at 120 mT. A quantitative accounting is needed: the RKKY field, the demagnetising field −μ0⟨M⟩ of the whole stack (which changes along the branch), and interlayer dipolar fields. It should place the zero of the effective field where the maze appears and explain why CoFeB does not fully reverse until about 125 mT.
   - (c) |J| = 0.034 mJ/m² is weak by RKKY standards. The spacer is Ru(6 Å)/Pt(9 Å), about 1.5 nm, not "0.7 nm Ru". The repeated description of "strong AFM RKKY" coupling, and the Methods statement that 6 Å Ru "maximize[s] the antiferromagnetic interlayer coupling", need qualifying.
   - (d) In Eq. 4, H_RKKY = −J m_j/(Ms t). With J < 0 (Table 2) this field points along the neighbour's magnetisation, which is ferromagnetic coupling, and μ0 is missing. Please check the sign convention used in the code.

   The authors should justify the formula or determine J independently, for example from an in-plane hard-axis loop, minor loops or the switching field of the plateau edge at ±30 mT, a CoB/Ru/Pt/CoFeB reference trilayer, or a fit of the full m(H) with the simulation. They should also show how the simulated field windows change for J within a plausible range.

   Raised by: r1, r2, r3

3. The cross-family RPM result has no chance baseline, and the mechanistic conclusion drawn from it goes beyond the data (Fig. 5c, pp. 10–12; Supplementary Note S5; Abstract). The cross-family RPM of 0.03–0.05 is read as "uncorrelated nucleation sites" and as evidence of "distinct pinning/formation mechanisms: external-field–driven for conventional-polarity skyrmions and RKKY–driven for inverse-polarity skyrmions." The RPM expected for two uncorrelated maps is not given. It depends on the overlap criterion and on the skyrmion area fraction, which for dense arrays of 60–80 nm objects in Fig. 2b,d looks like tens of percent. If the chance baseline is well above 0.03–0.05, the families are anticorrelated, for example inverse skyrmions sitting in the gaps of the conventional lattice or maze, which is a different physical statement. Anticorrelation is also expected on purely geometric grounds. Paths 2 and 4 start from the same maze. Conventional skyrmions are the shrunken remains of the down-CoFeB stripes and inverse skyrmions the remains of the up-CoFeB stripes, so they sit in complementary regions of a reproducible maze whatever the nucleation physics. In the CoFeB both families are reversed domains in a background set by the local effective field H + H_RKKY, so different pinning sites alone do not show a different mechanism. RPM probes pinning and nucleation, not "thermodynamic stability" (p. 10). The authors should:
   - report the chance-level RPM for each pair, by randomly shifting, rotating or shuffling one map, or by comparing maps from disjoint areas;
   - report the RPM of the maze state itself, and test whether inverse-skyrmion sites fall preferentially on former up-domains of the maze;
   - describe image registration and drift correction between the +120 mT and +40 mT maps;
   - define the error bars (standard deviation over skyrmions, sub-areas or registrations), say whether comparisons such as "1 with 3" and "3 with 1" in the Fig. 5c legend are symmetric, and give the number of skyrmions per map and the scan area;
   - narrow the "distinct mechanism" wording in the Abstract and Results to what the data show (reproducible, family-specific sites), or give a mechanism for why the pinning sites differ, and rephrase "thermodynamic stability" and "confirm independent nucleation pathways".

   Raised by: r1, r2, r3

4. Which asymmetry produces single-sublattice confinement is not isolated, and key supporting simulations are "not shown" (pp. 10, 13–14; Discussion; Summary). Ms·t is equal for both sublattices, and the simulations use equal Ms and t. The Zeeman and RKKY fields per unit moment are therefore the same for the two sublattices, so the selectivity must come from Keff (0.22 against 0.11 MJ/m³) and/or D (1.00 against 1.10 mJ/m²). This makes the abstract's "external field and interlayer exchange act asymmetrically on the sublattices" imprecise. D is a free parameter, and the Discussion's attribution of selectivity to "the enhanced ratio Deff/Keff in CoFeB" rests on that fitted value. Several statements rest on simulations that are not presented:
   - that reducing the RKKY strength "restores texture formation in both layers, whereas stronger coupling localizes the non-collinear state";
   - that the top-layer size asymmetry disappears in a symmetric stack;
   - that the skyrmion Hall angle is finite and that the two families "deflect in opposite transverse directions".

   The J_RKKY dependence is the main support for the "general materials-design principle". The authors should show, in the SI at minimum, a J_RKKY (and ideally Keff or D asymmetry) phase diagram of where textures form, with the experimental point marked, and simulations with D swapped or set equal and with Keff equal. The Hall-angle statement should either be shown or removed, and in any case labelled a prediction, since it is untested experimentally.

   Raised by: r1, r2, r3

5. Element-resolved SAXS would test the CoFeB-only claim directly in the textured states, and the SAXS photon energy is not stated (Fig. 2f–j; Methods p. 17). The Methods and the Fig. 2 caption do not say at which edge the SAXS patterns were taken. Resonant scattering at the Fe L3 edge directly shows that CoFeB hosts the lateral modulation. Patterns at the Co L3 edge at the same fields would test the claim quantitatively: if only CoFeB scatters, the ratio of Co-edge to Fe-edge magnetic scattering should match the Co/Fe XMCD ratio of CoFeB, with no extra CoB contribution. This would turn the spatially averaged XMCD argument into a spatially resolved, element-specific one. The authors should state the energy used for Fig. 2f–j and, if both edges were recorded (or STXM or holography at both edges is available), show both.

   Raised by: r1, r2, r3

6. The comparisons across samples, techniques and field geometries need their conditions stated and checked (Fig. 2; Fig. 4; Methods p. 18). Field-matched comparisons are made across three substrates: Si/SiO2 for MFM and SQUID, 25 nm Si3N4 for LTEM, and 200 nm Si3N4 for XMCD and SAXS. MFM is shown at positive fields, while DPC and the simulations are at negative fields. The authors should:
   - show at least the m(H) or XMCD loop of the membrane samples against the Si/SiO2 SQUID loop, to establish that switching and saturation fields, and hence the field windows, transfer between substrates;
   - state the sweep history for each data set;
   - state the in-plane field during DPC at 17° tilt (about tan 17° × |H|, roughly 40 mT at −131 mT), and discuss whether it distorts the Néel textures, shifts the field windows of the weakly anisotropic CoFeB, or explains the roughly 25% smaller DPC diameters (58 against 81 nm, 48 against 64 nm);
   - explain the strongly anisotropic SAXS arcs at 80 mT (Fig. 2h) against the nearly isotropic MFM maze (Fig. 2c), which suggests a field misalignment or in-plane component in the SAXS setup;
   - give the sample temperature for each technique. The XMCD magnet is "cryo-cooled" with 30–400 K control, and Ms, K and J all depend on temperature.

   Raised by: r1, r2, r3

7. The simulated states are reached by field-cooling, while the experiment and the RPM argument concern states reached along a sweep (Micromagnetic modelling section, p. 9). Each simulated state is obtained by "field-cooling from randomised magnetisation" at a fixed field. In experiment the states are reached from saturation or from the SAF state, and the hysteresis, the hysteretic SAF flip at ±30 mT and the RPM results show that history matters. The authors should run at least one quasi-static simulated descending branch, from saturation to 0 mT, and show m(H) and the textures. This allows direct comparison with Fig. 1c and Fig. 3b and shows whether the same sequence and field windows appear.

   Raised by: r1, r2

8. The decisive model parameters are partly fitted or simplified, and the comparison with data is qualitative (Methods pp. 19–20; Table 2; Discussion p. 13). D (1.00 and 1.10 mJ/m²) is a free parameter, and A is fixed at 8 pJ/m. The paper does not say what D was tuned to: field windows, domain period, skyrmion sizes or Néel character. The CoB is modelled with the CoFeB thickness and Ms, with Ku rescaled, so its intralayer dipolar and wall energies differ from those of the real CoB. The cell thickness is given as 6 Å, "same as the experimental value for CoFeB", but XRR gives 6.69 Å. The authors should:
   - state how D was chosen;
   - explain why modelling CoB with CoFeB's thickness and Ms does not affect the conclusion that only CoFeB textures;
   - compare simulated and measured quantities directly in the main text, for example in one table: field windows, skyrmion diameters per family (81/58 nm and 64/48 nm measured), and skyrmion density and size against field for both families (currently only in Supplementary Note S3).

   Raised by: r1, r2, r3

9. The Lorentz DPC evidence for the two skyrmion families is weaker than for the maze (Fig. 2k–n; p. 7). The −131 mT DPC image (Fig. 2k) shows very little discernible contrast, yet the text describes "bright features in k". The quantitative single-sublattice check (12.8 ± 0.7 against 13.6 T nm) is made only for the maze state (Fig. 2l,n), not for either skyrmion family, and those families are the headline result. The zero-deflection reference is "set by using assumptions informed primarily by the XMCD I(H) loops", which makes the DPC quantification partly dependent on the XMCD decomposition in item 1. The authors should show a contrast-enhanced or averaged profile across individual skyrmions in k and m, compared with the expected induction step, and state how the zero-deflection reference was set.

   Raised by: r3

10. The "general materials-design principle" rests on one stack (Discussion p. 13; Summary p. 14). "The mechanism reported here reflects a general materials-design principle rather than a peculiarity of the present stack" and "our results establish a general materials-design principle" are drawn from one composition, one Ru thickness and one thickness ratio. The Discussion's three requirements are strong AF exchange, moment compensation and engineered asymmetry, with Deff/Keff named as decisive. None is varied experimentally, and the DMI values entering Deff/Keff are simulation inputs, not measurements. The CoB-only and CoFeB-only reference multilayers used for Table 1 already exist. MFM field series on them, showing that the CoFeB stack textures readily and the CoB stack does not at comparable effective fields, would support the anisotropy argument at little cost. A symmetric SAF (CoFeB/CoFeB or CoB/CoB), or a stack with a different spacer thickness (hence a different J) or Keff contrast, would test the predicted trend, for example by showing textures in both sublattices or the loss of one family. Otherwise the generality should be presented as a model-based hypothesis.

   Raised by: r1, r2, r3

11. The advance over prior AF-coupled perpendicular multilayers is not set out (Introduction; Discussion; title). FM tubes in an AFM background and AFM tubes in an FM background along the AFM–FM transition of [Co/Pt]/Ru-type multilayers are discussed in Refs. 30–32. The authors' own PRB 2024 (Ref. 33) treats AFM–FM phase coexistence in a SAF. The idea that a layer in an AF-coupled stack sees a shifted effective field is not new in itself. Within the CoFeB layer, the "inverse-polarity" skyrmion is an ordinary chiral skyrmion whose core is antiparallel to the local effective field. It is a conventional skyrmion in a layer whose effective field has reversed, which is how the authors themselves explain it. The title ("Beyond conventional skyrmions") and abstract should state precisely what is new: chemical asymmetry under moment compensation, confinement of textures to one sublattice, their chirality, and two families of opposite topological charge in one sweep. A paragraph saying what Refs. 30–33 did and did not show would help.

    Raised by: r1, r2, r3

12. The topological character of both families is not shown in the main text (Supplementary Note S4). The Néel character and fixed chirality are said to be verified by tilt-series Fresnel imaging in the SI. The claim that the two families have opposite topological charge, and hence opposite Hall deflection, depends on it, and the paper uses "topologically protected". The main text should state explicitly that this was done for both families and summarise the evidence briefly.

    Raised by: r1, r2

C. Minor

13. Fig. 2 caption, panel n: "line profile taken from the marked position in g". Panel g is a SAXS pattern. The text says the profile is from the maze state, so this should be panel l, where the box is drawn. Also say what the dashed line in k marks.

    Raised by: r1, r2, r3

14. The spacer thickness is inconsistent. The Fig. 6 caption and p. 12 say "0.7 nm Ru". Fig. 1a, Methods and XRR give 6.03 Å Ru, and the full spacer between CoB and CoFeB is Ru(6 Å)/Pt(9 Å). Please make these consistent, and clarify which interfaces set the DMI sign in each layer.

    Raised by: r1, r2, r3

15. "Deff = D/t" is called the "DMI energy density" (p. 13), and the Discussion argues that the thinner CoFeB compensates for a "potentially reduced intrinsic DMI". In the convention of Eq. 5 and Table 2, D in mJ/m² is already the thickness-normalised constant (the surface DMI is Ds = D·t), and the layers have equal thickness, with CoFeB having the larger D. Please reconcile the notation and say whether any DMI was measured for these layers.

    Raised by: r1, r2, r3

16. Polarity terminology. The Fig. 2 caption and abstract describe conventional skyrmion cores as "antiparallel to the external field". MFM and DPC sense the thickness-integrated moment, in which the core is a zero-moment AFM region in an FM background (Fig. 6). The "antiparallel" statement holds only for the CoFeB layers, which is established later by XMCD. The "polarity" convention, defined relative to the external field rather than the local background, should be explained early.

    Raised by: r1, r3

17. Simulation numerics and geometry. State whether the 400 × 400 nm box uses periodic or open boundaries; it holds only a few 50–80 nm textures, which affects densities and the maze. State how the non-magnetic spacers enter the magnetostatics (layer pitch). The 4 nm in-plane cells compare with wall widths √(A/Keff) ≈ 8.5 nm (CoFeB) and 6 nm (CoB), so please state the convergence check. Comment on how T = 0 simulations compare with room-temperature field windows.

    Raised by: r1, r2, r3

18. MFM tip perturbation. A Co-coated tip (6.5 nm Co, about 20 nm lift) over a soft CoFeB layer whose effective field is near zero in the maze window could nucleate or move textures, which matters for the RPM data. Repeated scans at fixed field without cycling, or RPM with and without intermediate scans, would show whether it does.

    Raised by: r1, r2, r3

19. Overstated wording. "We unequivocally attribute" (p. 4), "Return-point memory measurements confirm independent nucleation pathways" (Abstract) and "topologically protected" are stronger than the evidence shown in the main text; see items 1, 3 and 12.

    Raised by: r1, r2, r3

20. p. 13: "at zero external field, the strong AFM RKKY interaction saturates the CoFeB layers in the up state". Fig. 6 and the rest of the argument have CoB up and CoFeB down at zero field. Please correct.

    Raised by: r2

21. Fig. 4a–b: the background in the cross-sections appears as alternating red and blue rows. At −130 mT a conventional-polarity state should have a uniformly blue FM background. Check the colour scale or panel, and mark the CoB and CoFeB rows.

    Raised by: r2

22. Fig. 1c axis label reads "m (×10⁸ Am²)". It should read 10⁻⁸, consistent with Fig. 5a and 8.85·10⁻⁸ Am² per sublattice.

    Raised by: r1

23. Statistics for the quoted skyrmion diameters (81 ± 4, 58 ± 6, 64 ± 4, 48 ± 5 nm): give the number of skyrmions measured, whether the uncertainty is a standard deviation or a standard error, and the fitting procedure. Also give the SAXS ring-to-size conversion.

    Raised by: r3

24. Table 1 Ms values are derived on the assumption that the two sublattice moments are identical. State this as an assumption, supported by the 1% remanence, not as a measurement.

    Raised by: r2

25. Typos: "gemeotry" (Methods, SAXS, p. 17), "negligble" (p. 3), "for of each sub-lattice" (Table 2 caption), Table 1 header spacing, and the Data Availability DOI placeholder.

    Raised by: r1, r2

Verdict: minor revision
