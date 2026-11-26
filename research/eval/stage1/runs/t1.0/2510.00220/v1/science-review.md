# Merged review

## A. Must address

1. **There is no direct structural evidence that the two transport states differ in stacking, or that the RB-mixed state contains rhombohedral tetralayer.** The central claim is a "sliding-induced first-order structural phase transition between Bernal and rhombohedral tetralayer graphene". It rests on three things: the R_xx hysteresis (Fig. 1c, Fig. 2), the absence of clear quantum oscillations in the hole-doped state (Extended Data Fig. 3), and qualitative agreement with a calculation (Fig. 3b), supported by analogy to imaging studies of other samples (Refs. 27, 28). The only real-space image, Fig. 1b, is taken from a separate twisted double-bilayer/hBN/graphite stack on SiO₂ with no gates (Extended Data Fig. 2a is from a stack still on the stamp). It shows that the starting material has mixed domains, not that gating changes them in device A. The main text nonetheless calls it "a typical real-space image of the domain configuration". Missing quantum oscillations are a weak discriminator, because domain-wall scattering, disorder, lower mobility or inhomogeneous current paths also suppress them. The switching is described as domain-wall motion within a fixed mixed-domain landscape, so the claim needs evidence that the rhombohedral area fraction actually changes between the states. Without it, the data are equally consistent with purely electronic bistability in a fixed domain landscape, such as hysteresis between competing correlated states, which is well documented in rhombohedral multilayers. Contact- or edge-related switching is also not excluded: the switching occurs "only in part of the device" (Extended Data Fig. 4), and the jumps change sign and magnitude between contact pairs (Extended Data Fig. 7). The authors should provide, roughly in order of strength:
   - (i) a direct structural probe of the transport device, or of an equivalent device, after it has been set into each state. Options are spatially resolved Raman 2D-band mapping (ABAB and ABCA have distinct line shapes), in-situ KPFM, nano-IR or near-field imaging through the top gate, or at minimum KPFM before and after switching. Devices with thin top hBN imaged at room temperature after a low-temperature switching cycle would still be informative.
   - (ii) a rhombohedral-specific electronic signature present in the RB-mixed state and absent in the B-dominant state. Examples are the large-|D| gap at charge neutrality (compare the neutrality resistance and its temperature dependence in Fig. 2b vs 2c inside the boxed regions), or Landau-level or oscillation features matching ABCA tetralayer. Fourier spectra of R_xx(1/B) in both states at comparable |n| would help: if the RB-mixed frequencies match rhombohedral and Bernal Fermi-surface areas, the "mixed" assignment becomes much firmer.
   - (iii) a quantitative estimate of how much rhombohedral area must change to produce the observed ΔR_xx.
   - (iv) an own control: a pure-Bernal region or device, fabricated and measured identically, that does not switch. At present the absence of switching in single-domain samples is supported only by citing literature (Refs. 20, 23, 40).

   Raised by: r1, r2, r3

2. **Gate-history artifacts such as charge trapping are not ruled out, and it is not shown that the two states have the same n and D at the same gate voltages.** The switch into the RB-mixed state happens only at the extreme of the gate range. In Fig. 1c the backward-sweep jump sits at n ≈ −15.5×10¹² cm⁻², essentially the left edge of the scan, and the Fig. 2 protocol resets the device by "doping to the maximum hole density". Large gate excursions are a classic cause of charge injection into, or trapping and detrapping in, the hBN, at graphite/hBN interfaces or at contacts. That shifts n₀ and D₀ and produces history-dependent, nonvolatile-looking transport and Hall signals that relax at a threshold. The n and D calibration (n₀, D₀, C_t, C_b) was done "from the Landau levels in the B-dominant state" only (Methods). The paper therefore does not show that "exactly the same gate voltages" (Fig. 4c vs 4d, 4g vs 4h) correspond to the same n and D in both states. That is the premise of the Fig. 4 comparison and of every boundary in Fig. 3a. The two stackings also have different quantum capacitance and layer polarization, which could shift n and D even without trapped charge. The authors should:
   - (a) show Landau fans, or Hall-slope carrier densities and the charge-neutrality-point position, in both states at the same gate voltages, demonstrating that n₀, D₀ and the capacitances do not change, and estimate the error from different quantum capacitance;
   - (b) show that −15.5×10¹² cm⁻² is an intrinsic switching density rather than the scan limit, by sweeping further or by showing how the threshold depends on D, sweep rate and dwell time;
   - (c) show that the threshold scales with n and D rather than with the absolute voltage on either gate, for example by plotting it against V_t and V_b separately (the Fig. 2a vs 2e comparison partly addresses this);
   - (d) report gate leakage currents at the extreme voltages;
   - (e) argue explicitly why trapped charge would not produce the mirror-symmetric multi-contour structure of Fig. 3a, if the constant-ΔF contours are meant as a discriminator.

   Raised by: r1, r2, r3

3. **The stacking identity of the domains in device A, which supplies nearly all the data, is not established, and with a near-180° assembly they may be polar ABAC/ABCB rather than ABAB/ABCA.** Methods state that device A was assembled with "nearly-180°" rotation and that "one of the layers underwent an additional global shift". An AB bilayer on an AB bilayer at about 0° gives ABAB and ABCA interface registries. Rotating the top Bernal bilayer by 180° (the D3d bilayer has no C2z) turns it into its AC partner, and simple registry counting then gives ABAC/ABCB domains. These are the non-centrosymmetric, spontaneously polarized tetralayer polytypes discussed in the authors' own Ref. 37. The "global shift" invoked to recover ABAB/ABCA is asserted, not characterized, and domain identification rests on KPFM contrast alone, measured on a different sample. If polar regions are present, three interpretations change: (a) the 22 mV KPFM contrast, read as a work-function difference, could instead be a polarization contrast of the size expected for polar domains; (b) polar domains break inversion and would give a D-odd AHE without any domain-wall physics; (c) the switching could be sliding-ferroelectric motion rather than a Bernal–rhombohedral transition. The authors should:
   - (i) give the stacking-registry argument explicitly for the 0° and 180° assemblies and explain how the "global shift" was identified;
   - (ii) determine the domain stacking in device A directly, for example by Raman 2D line shape (which distinguishes ABAB, ABCA and ABCB), SHG (non-zero only for the polar stacking), or KPFM under applied D on the device;
   - (iii) state which domain types device A and device B each contain, and whether device B (0.03°, which naturally gives ABAB/ABCA) reproduces the full switching phase diagram and not only the AHE sign reversal;
   - (iv) check whether the charge-neutrality offset D₀ differs between the two states, which a polar stacking would shift.

   Raised by: r1, r2, r3

4. **In a strongly inhomogeneous, multi-domain conductor, the Hall data as presented cannot by themselves establish the "ferromagnet vs paramagnet" claim or the sign of the AHE.** The paper itself states that R_xx jumps differ "in magnitude and sign" between contact pairs (Extended Data Fig. 7, p. 5), that switching occurs "only in part of the device" (Extended Data Fig. 4), and that current paths are "complex". Under these conditions:
   - The transverse voltage at a single Hall pair mixes longitudinal and Hall components. A hysteretic Ryx can arise from the hysteretic magnetoresistance of a switching domain, mixed in through inhomogeneous current paths, and antisymmetrization removes this for hysteretic data only if the +B forward sweep is paired with the −B backward sweep. With R_xx ~10–100 Ω and comparable R_yx, a small contact misalignment matters.
   - In a Hall bar only partly covered by magnetic patches, the sign and magnitude of the signal at a given Hall pair depend on where the magnetic region sits relative to the probes. This could produce an apparent D-odd sign without intrinsic inversion breaking, and could explain why |R_yx| is "significantly larger" than in pure rhombohedral tetralayer.
   - The AHE is reported from a single Hall pair.
   - Field sweeps reach only ±0.15 T, just above the apparent coercive field of ~0.1 T (Fig. 4c,g). It is unclear whether the loops saturate or whether the anomalous part is separated from the ordinary Hall slope.
   - The maps in Fig. 4a,b,e,f were taken at a single field, B = 0.03 T, below the coercive field. They cannot have been antisymmetrized, and their sign depends on the prior field and magnetization history, which is not stated. Without the training protocol, the sign contrast between Figs. 4a and 4e cannot be read off the maps.
   - The "paramagnet" label for the B-dominant state rests on a linear R_yx at a few gate points at 1.5 K. "No detectable AHE or hysteresis at 1.5 K in this (n, D) window" is the accurate statement, unless supported by, for example, temperature-dependent Hall slopes.

   The authors should: state which Hall pair was used in Fig. 4; show R_yx(B) loops for both signs of D on at least two independent Hall pairs, including the opposite side of the Hall bar; show raw, unsymmetrized R_xx and R_yx loops together; describe the antisymmetrization procedure for hysteretic loops; extend the field range until the loops saturate and the high-field branches merge; show the B = 0 remanent R_yx after training at +B and −B at the diamond and star points; state the field-training protocol for each map; check Onsager reciprocity under current-direction or contact permutation; report σ_xy or the Hall angle, not only R_yx; and show the absence of hysteresis in the B-dominant state over the same field range at the identical gate point, at lower temperature if available. If the D-odd sign survives on several contact pairs and in device B with a different geometry, the conclusion becomes much stronger.

   Raised by: r1, r2, r3

## B. Should address

5. **The domain-boundary origin of the D-odd AHE is an untested hypothesis, and simpler explanations of the sign reversal are dismissed too quickly** (abstract, p. 7, Fig. 4a,c,e,g). Specific issues:
   - (a) Non-mirrored points. The positive-D loop (diamond, about (n, D/ε₀) ≈ (1.3, +1.0)) and the negative-D loop (star, about (1.4, −1.13)) are not at mirrored points, and Fig. 4e shows both AHE signs within the negative-D region. Because the sign evidently varies with (n, D), the inversion argument needs loops at exactly mirrored (n, ±D) points, preferably several pairs.
   - (b) Different preparation paths. The RB-mixed state at +D and at −D is prepared along different gate paths (Fig. 2a vs 2e; Fig. 4 caption, "going along the edge of the gate boundary... for each line"). Because domain-wall motion is the switching mechanism, the two signs may belong to two different domain configurations rather than to one state under D → −D. The authors should reach ±D from the same prepared state (for example by sweeping D continuously through zero at fixed n inside the bistable window), or by paths related by exchanging top and bottom gates, and check that R_xx is the same at both.
   - (c) Extrinsic inversion breaking. The arguments against it are weak. The absence of moiré features in R_xx and the D-mirror symmetry of the R_xx boundary constrain the structural energetics, not the Berry-curvature sign of a magnetic state that may be sensitive to small layer-asymmetric perturbations. Reproduction in device B does not exclude a systematic asymmetry, because both devices were built the same way (graphite/hBN bottom gate, PC pickup, top gate). The authors should report the hBN–graphene alignment angles (from crystal edges or SHG), the top and bottom hBN thicknesses and C_t/C_b, and test whether the sign reversal occurs exactly at D = 0 or is offset, that is, whether it follows D or the layer that holds the carriers.
   - (d) Polar stacking. The polar-stacking explanation (Concern 3) must be ruled out before domain-wall physics is invoked.
   - (e) The domain-wall picture itself. No symmetry analysis shows that an ABCA/ABAB boundary (a partial dislocation at the 2–3 interface) breaks inversion in the relevant sense. There is also no estimate of how quasi-1D boundary regions could produce a Hall signal larger than that of pure rhombohedral tetralayer (Ref. 23).
   - (f) A falsifiable test. The intermediate domain states (the multiple jumps, blue dashed lines in Fig. 3a) offer one: if the D-odd AHE comes from domain walls, its magnitude should track the wall configuration and grow with each wall-motion step, while the D-even part (Fig. 4i) should track rhombohedral area. Domain-wall density across devices with different twist angles is another handle.

   The device-B reproduction (Extended Data Figs. 10–11), in particular a mirrored-point loop pair, should appear in the main text. Until such tests exist, the abstract and Discussion ("establishes domain boundaries ... as unique and pristine platforms") should present the domain-boundary origin as a conjecture.

   Raised by: r1, r2, r3

6. **The theory–experiment comparison in Fig. 3b is presented as "agree well" or "remarkable", but it is qualitative, and the way its parameters were fixed is unclear.** The model has two free parameters:
   - ΔΦ, taken from KPFM (22 mV) measured on a different sample, at room temperature, in ambient conditions, on SiO₂ or on the stamp;
   - ΔU(0,0), "explained in the Supplementary Information" (not provided). If it was fitted to the boundary, the agreement is partly by construction.

   It is also unclear which thermodynamic potential is compared. At fixed gate voltages the relevant potential includes the electrostatic work done by the gates, and because the two stackings have different quantum capacitance they do not have the same n and D at the same voltages. It is not stated whether ΔU is computed at fixed (n, D) or at fixed (V_t, V_b). The calculation appears to be a non-interacting tight-binding band energy. It is unclear whether it includes self-consistent interlayer screening of D (which strongly reduces the rhombohedral gap) or interaction-driven spin-valley-polarized states, which lower the rhombohedral energy by meV per carrier precisely near the black boxes in Fig. 3a. Only the RB → B boundary is modelled. The B → RB transition lies at or near the edge of the gate range, so the two spinodal-like boundaries cannot bracket ΔF = 0. The authors should:
   - state which parameters are fitted and how ΔU(0,0) was obtained;
   - plot the calculated ΔU along each experimental contour, with its spread, showing that each blue dashed line maps to a constant ΔU and that successive lines are ordered consistently;
   - show the sensitivity of the contours to ΔΦ (within the KPFM uncertainty), to ΔU(0,0) and to the tight-binding parameter set;
   - clarify the ensemble;
   - discuss how screening and interactions would modify ΔU, in particular in the predicted large-|D| rhombohedral pocket.

   Raised by: r1, r2, r3

7. **The "switching at constant ΔF" assumption, and the magnetic-susceptibility difference extracted from it, are not justified or not shown.** The text (pp. 3, 5) treats each R_xx jump as a ΔF = const contour. It then uses the field dependence of the boundary to extract the susceptibility difference between the two structures (Extended Data Fig. 5 and Supplementary Information, not included). This requires a domain-wall pinning barrier that does not depend on n, D or B, and quasi-static wall motion without rate-dependent thermally activated creep, and neither is justified. The authors should give, in the main text, the Clausius–Clapeyron-type relation used, its assumptions, and the resulting value with sign and uncertainty, compared with the expected orbital susceptibilities of ABAB and ABCA tetralayers. Otherwise they should remove the claim from the main text. Testing the assumption needs the rate and temperature data requested in Concern 8.

   Raised by: r1, r2, r3

8. **The temperature, sweep-rate and retention dependence of the switching is missing, and "nonvolatile" is not quantified.** All switching data are at 1.5 K. A first-order transition governed by domain-wall pinning predicts a hysteresis width and thresholds that depend on temperature, and possibly on sweep rate and dwell time. Retention is shown only over about 300 s, with about six or seven cycles (Fig. 1d). Extended Data Fig. 9 claims "many cycles" without a count, drift or failure rate. Fig. 3a and Fig. 4 also indicate that at V_t = V_b = 0 the device is B-dominant. The RB-mixed state therefore persists only while non-zero gate voltages are held inside the bistable window, which is weaker than the usual memory meaning of non-volatility. The authors should:
   - show the switching thresholds versus temperature, up to and above the ~8 K Curie temperature and ideally to tens of kelvin, to establish that the structure, not the magnetism, drives the bistability;
   - show the thresholds versus sweep rate and dwell time;
   - report retention over hours at the AHE operating point, and the cycle count and level drift;
   - show whether the RB-mixed state survives warming above T_C and recooling at fixed gates;
   - state explicitly which gate voltages must be held to retain each state.

   Raised by: r1, r2, r3

9. **Reproducibility across devices, regions and cooldowns is unclear.** All main-text data come from device A. The hysteresis "appears only in part of the device" (Extended Data Fig. 4), and the R_xx jumps differ in sign between contact pairs. Device B (0.03° twist) appears only for the AHE sign reversal. The text does not say whether device B shows the gate-driven switching, the Fig. 2/3 phase diagram, or the on/off AHE. The domain landscape is set by fabrication and relaxation, so device-to-device variation of the switching densities is central to the "on-demand toggling" claim. The authors should state how many devices and regions were measured and how many showed switching. They should give a table of devices, twist angles, cooldowns, the features each shows, and cycle counts. They should show the key Fig. 4 comparison (same gate voltages, hysteretic vs linear R_yx) in a second device or at a second Hall pair, and state whether the switching boundary and the AHE survive thermal cycling to room temperature.

   Raised by: r1, r2, r3

10. **The "negative D-even AHE" at the pentagon (Fig. 4i) and the Curie temperature need fuller support.** The pentagon data show only a nonlinear R_yx(B) without hysteresis over ±0.15 T. In a mixed-domain sample where Bernal and rhombohedral regions with different carrier types and mobilities conduct in parallel, multi-carrier ordinary Hall transport naturally produces such a nonlinearity, and a temperature dependence alone does not distinguish the two. The "around 8 K" Curie temperature (Extended Data Fig. 8, not included) is quoted without the criterion used (onset of hysteresis, remanent R_yx(B = 0), or an Arrott-type analysis) or an uncertainty. The authors should fit the pentagon data with a two-band ordinary Hall model over a wider field range as a null hypothesis, and show remanence if any. They should state the T_C criterion and uncertainty and bring the temperature dependence of the hysteresis loops (Fig. 4c,g) into the main text. If the "two-component AHE" summary on p. 7 is kept, its supporting data should appear in the paper.

    Raised by: r1, r2, r3

11. **The rhombohedral area fraction and wall length of each state are only qualitative.** The "B-dominant" state is said to possibly contain small rhombohedral patches and domain walls (p. 2), and the RB-mixed fraction is not quantified. The claimed physics depends on these quantities: the AHE magnitude "significantly larger" than in pure tetralayer, and the proposed proximity effect. The authors should estimate the area fractions, for example from quantum-oscillation amplitudes, the Hall density, or the KPFM domain statistics of a comparable sample. They should also discuss how a modest rhombohedral fraction can give an AHE larger than that of a pure rhombohedral device, which by itself suggests that the measured R_yx is not a simple area average (see Concern 4).

    Raised by: r1

## C. Minor

12. The priority claim on p. 7, "the first realization of a magnet-to-non-magnet nonvolatile phase transition controllable entirely by electrostatic means", should be qualified. Gate-hysteretic switching between correlated magnetic and non-magnetic states, including AHE states, has been reported in moiré graphene and in graphene/hBN devices with ferroelectric-like gate hysteresis. Electrical switching of magnetic order has been reported in moiré Chern magnets, and Ref. 45 is ionic rather than purely electrostatic. The authors should discuss these and state precisely what is new: switching driven by a stacking change, which depends on Concern 1.

    Raised by: r1, r2, r3

13. "First-order quantum phase transition" (p. 2) is not an accurate description. The transition is a hysteretic, structural first-order transition between metastable configurations, driven by gate voltage at 1.5 K through domain-wall depinning, and no tuning to a T = 0 critical point is shown. "Gate-driven first-order structural transition" would be more accurate.

    Raised by: r1, r2, r3

14. The submission repeatedly cites Extended Data Figs. 1–11 and a Supplementary Information file that are not provided. They contain the quantum-oscillation evidence, the work-function measurement, the device-B data, the Curie temperature, the cycling endurance and the calculation details, so several key steps of the argument cannot be checked. These should be included, and the key evidence brought into the main text where the concerns above ask for it.

    Raised by: r1, r2

15. The Fig. 1b caption and the main text should state explicitly that the image comes from a different heterostructure from device A, as the Methods say, and whether that heterostructure has the same ~180° construction.

    Raised by: r1, r2, r3

16. Fig. 1:
    - Give the pulse durations and amplitudes in Fig. 1d, and the read-out density, stating that it lies inside the bistable window.
    - Give the sweep rate used in Fig. 1c.
    - Reconcile the 30 Ω and 11 Ω levels in Fig. 1d with Fig. 1c at the corresponding n.
    - The caption assigns the −4.1 and −15.5×10¹² cm⁻² thresholds to "forward and backward scans, respectively", while the text puts the −15.5 jump on the "blue curve". Check that these agree with the legend arrows.

    Raised by: r1, r3

17. Figs. 2 and 3:
    - Fig. 3a overlays blue contours from a different contact configuration on data from the main configuration. Mark them clearly as such or show them on their own map, and explain how they were extracted.
    - State how the black dashed boundary in Fig. 2d/2h and Fig. 3a was drawn: by eye, or by a threshold on ΔR_xx/R̄_xx.
    - Fig. 3b: give the definition, units and sign convention of ΔU (R minus B?), which color favors which stacking, and the reference density and displacement used to define the contours.
    - Fig. 3a: explain what the black-boxed regions near n ≈ 0 at large |D| represent.

    Raised by: r1, r2, r3

18. The Fig. 2 and Fig. 4 captions should spell out the exact gate path used to prepare each state at each (n, D) point. Because the domain configuration depends on history, readers need this to judge Concern 5.

    Raised by: r1

19. Methods:
    - The definition D = (−C_tV_t + C_bV_b)/2 − D₀ has units of charge per area, while the figures plot D/ε₀ in V/nm. Make the definitions consistent.
    - Give the values of C_t, C_b, n₀ and D₀ with uncertainties, and confirm that the same calibration applies in the RB-mixed state.
    - Give the hBN thicknesses and the Hall-bar dimensions.
    - State the electron-heating checks, for example current independence of the AHE at 0.5–10 nA.

    Raised by: r1, r2, r3

20. The KPFM measurement (Fig. 1b, Extended Data Fig. 2) enters the calculation directly. The authors should give its conditions (ambient or not, tip calibration) and the uncertainty of the 22 mV work-function difference. They should also comment on how well a ΔΦ measured at room temperature in ambient conditions on SiO₂ or on a stamp transfers to the encapsulated, gated device at 1.5 K.

    Raised by: r1, r2, r3

21. Fig. 4b,f: the B-dominant maps are noisy for n < 1×10¹² cm⁻². State whether this reflects contact resistance at low density, and give the measurement current (0.5 nA) in the caption.

    Raised by: r3

22. Typographical errors: "The Bernal regions is larger" (Fig. 1 caption) should read "are larger"; "Free energy" and "Helmholtz Free energy" (pp. 3, 5); "L.M.." (Contributions); "Keithly" should be "Keithley" (Methods).

    Raised by: r2, r3
