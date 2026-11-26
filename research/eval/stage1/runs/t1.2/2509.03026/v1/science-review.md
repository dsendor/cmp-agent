**A. Must address**

1. **The two resistance states are not shown to be magnetic (octupole) states rather than resistive switching of the MgO barrier.** Every resistance change in the paper comes from two-terminal current-pulse loops (Fig. 2a–c, Extended Data Fig. 1). No device shows a field-swept R(H) loop, and no nonmagnetic reference junction is measured. The earlier PtMn3 and Mn3Sn AFMTJ work the paper cites (refs. 11–13) did use field loops. The operating conditions are the ones where bipolar filamentary or oxygen-vacancy switching of thin MgO is common. In Fig. 2a (100 nm pillar) the high state is about 2.4 kΩ at a switching current of about 0.85–1 mA, which puts about 2–2.4 V across the nominal 2 nm MgO, roughly 10–12 MV/cm, close to breakdown and soft breakdown. 100 nm devices in Extended Data Fig. 1c are pulsed to ±4–6 mA, which dissipates several mW and gives more than 5 V at about 1.3 kΩ. The STEM shows MgO that "did not indicate well-defined crystallization" and has a rough bottom interface (Fig. 1c, pp. 5–6), which makes barrier switching more plausible. Several features fit resistive switching: bipolar hysteresis that is square or gradual and multilevel, on/off ratios of several hundred percent, and a broad device-to-device spread (Fig. 2b: most devices below 100%, one at 363%). Without an independent magnetic reference, calling the effect "TMR" and the states "P" and "AP" is not supported, and neither is "OTT switching". The authors should do the following.
   - Show in-plane and out-of-plane R(H) loops, or states set by SOT as in ref. 13, on devices that also switch with current, reaching the same two resistance levels. Show that a current-set state can be reset by field, and the reverse.
   - Show the dependence of the switching current on applied field.
   - Show I–V and dI/dV curves and the bias dependence of the two states. Magnetic TMR should fall with bias, while filamentary states usually show a different I–V nonlinearity.
   - Report the read current or voltage (Methods gives only the 1 ms width).
   - Measure a control junction with matched RA under identical pulses, in which the effect should be absent. Options are Pt/MgO/Pt, one PtMn3 replaced by Pt or by a collinear antiferromagnet, or the same stack above 360 K.

   Raised by: r1, r2, r3

2. **Heating, spin-orbit torque from the leads, Oersted fields and thermoelectric effects are not excluded as the switching drive.** The stack has 5 nm Pt next to both PtMn3 layers, and the bottom electrode carries in-plane current into and out of the pillar. The authors' own earlier work (ref. 13) switched PtMn3 by SOT from Pt. Each pulse lasts 1 ms (up to 50 ms in Fig. 2d), long enough to reach thermal steady state. The dissipated power is about 0.5–2.4 mW in Fig. 2a and up to about 10 mW at 6 mA in Extended Data Fig. 1c, in a pillar of about 10⁻¹⁵ L. By the authors' own data, switching vanishes at 360 K, only about 65 K above the measurement temperature. Thermally assisted reordering near the transition is therefore a leading alternative to spin-transfer torque, with the final state then chosen by an Oersted field, lead SOT, a Seebeck/Peltier asymmetry between the electrodes, or exchange from the other layer. This would also explain the polarity scatter in concern 3. The authors should do the following.
   - Estimate the junction temperature during the pulse, for example by comparing the resistance during the pulse with the R(T) calibration from Fig. 2c.
   - Measure switching against pulse width down to the ns regime, where heating is much smaller.
   - Send in-plane current through the bottom lead alone, not through the junction, to test for lead-SOT switching.
   - Test whether the switching current scales with pillar area (constant J) rather than with lead current.
   - Vary or remove the Pt layers next to PtMn3, for example with a light-metal seed that still gives (111) texture.
   - Measure the switching current against an in-plane field, since Oersted- or SOT-assisted switching should depend on field differently from STT.
   - Compare switching at a lower base temperature.

   Raised by: r1, r2, r3

3. **The switching polarity changes between nominally identical devices, which is hard to reconcile with spin-transfer torque.** In a spin-transfer picture the current direction that favours P or AP is fixed by the stack sequence and by which layer is free. The OTT model (Eqs. 4–8, Extended Data Fig. 5) predicts one polarity for a given stack. In Fig. 2a, positive current switches low→high and negative current high→low. In Fig. 2c, positive current switches high→low, and Fig. 2d labels positive J as AP→P. Extended Data Fig. 1 contains both senses within single diameters. The 50 nm left panel and the fourth 100 nm panel switch low→high at positive current. The 75 nm left panel and the first three 100 nm panels switch high→low. The two 200 nm panels are opposite to each other. The paper does not comment on this. Polarity that varies at random is typical of filamentary or thermally driven switching. The authors should state the current-sign convention and tabulate the polarity for all 36 devices. They should then explain any variation within the OTT picture, for example by showing which electrode switches in each device, and show that the polarity is not set by lead geometry or by the history of the barrier.

   Raised by: r1, r2, r3

**B. Should address**

4. **The theory predicts no torque magnitude, so "confirmed by our density functional theory calculations" (p. 4) is overstated.** The DFT gives bulk k∥-resolved PtMn3 conduction channels (Fig. 3a,b; Eq. 3). The argument that β1 > β2 rests on a schematic of "a select band" at one k-point along Γ–K (Fig. 3c,d). The key quantity, β_eff = β1 − β2 integrated over the Brillouin zone, is never evaluated, and it is not shown that the net staggered polarization survives summing over all k∥. No transmission through MgO and no torque is calculated. In the LLG simulation β_eff is set to 1, the maximum possible value (Extended Data Table 1), and η = 0.53 is not traced to any calculation. The simulation is a zero-temperature macrospin that switches in about 3 ps at 10 MA/cm². It gives no critical current and is not compared with the ms-scale, thermally activated switching in Fig. 2d, so the claim of switching "consistent with the experimental observations" is not quantitative. The Discussion's hope that the results "will motivate the research community to develop a theory of OTT" (p. 10) also sits uneasily with "confirmed". The authors should:
   - compute the BZ-integrated intra- and inter-sublattice spin currents, or better, the non-equilibrium sublattice-resolved torque for a PtMn3/MgO/PtMn3 (111) junction including interfaces (for example by NEGF or Kubo);
   - use the resulting β_eff and η in finite-temperature LLG simulations to find the critical current and its pulse-width dependence, and compare these with Fig. 2d.

   If they do not, they should present the theory as a plausible mechanism rather than a confirmation.

   Raised by: r1, r2, r3

5. **The mechanism assumes coherent, k∥-conserving, sublattice-preserving tunnelling, which the measured junction structure does not support.** The OTT picture assumes ballistic transport with conserved k∥ ("in a crystalline AFMTJ operating in the ballistic transport regime", p. 7). It also assumes that electrons "preferentially retain their sublattice identity" across epitaxially registered (111) kagome planes (Fig. 3c–e). The devices have polycrystalline PtMn3 with only a predominant (111) texture, an MgO barrier without well-defined crystallization, and visible interface roughness (Fig. 1c,d, pp. 5–6). Across an amorphous barrier k∥ is not conserved, so the directional selectivity of Fig. 3 would largely average out. Grains on the two sides may also be rotated in-plane relative to each other. In that case sublattice i in one electrode has no fixed partner in the other, and the β1 (intra) versus β2 (inter) distinction behind Eqs. 5–8 is not defined grain by grain. The same problem applies to explaining a 363% TMR, larger than in epitaxial Mn3Pt AFMTJs (ref. 12), with such a barrier. The authors should show that the net staggered torque survives these features, or narrow the claim. Routes include a calculation with k∥ not conserved (the diffusive or amorphous-barrier limit), averaging over relative in-plane grain rotations, an explicit argument that the torque survives incoherent tunnelling, or a structural measurement showing in-plane grain registry across the barrier.

   Raised by: r1, r2, r3

6. **The paper does not establish which PtMn3 layer switches, or why the other one does not.** Neither electrode is pinned (no exchange bias and no synthetic structure). The two have the same composition and differ only in thickness (7 nm bottom, 10 nm top), so ΔV differs by only about 1.4×, and interface quality differs. In an STT picture both layers receive torques of opposite sense. The modelling is inconsistent on this point: the energy-barrier estimate takes the 7 nm bottom layer as free (Extended Data Fig. 3b, "100 nm × 7 nm"), while the LLG model uses d = 10 nm (Extended Data Table 1). The authors should state which layer they believe switches and give evidence. Options include thickness series of each layer, strongly asymmetric electrodes, pinning one electrode, or setting each layer independently by field or by SOT. They should also explain why the other layer is stable at a similar current density. This bears directly on concern 3.

   Raised by: r1, r2, r3

7. **The chemical order, composition, texture and magnetic state of the device PtMn3 are not characterised.** The noncollinear T1g octupole state and its 360 K transition, used as evidence on p. 7, belong to chemically ordered L1₂ Mn3Pt near the 3:1 composition. The device stack is deposited at room temperature without annealing (Methods), which usually gives a chemically disordered A1 phase with a different magnetic structure. The structural evidence is local FFTs of two grains (Fig. 1d), which index only fundamental (111) reflections and so do not distinguish L1₂ from A1. Apart from the 360 K disappearance in Fig. 2c, there is no magnetic evidence for the device films. The authors should provide, for the device stack itself:
   - L1₂ superlattice reflections such as (100) or (110) in XRD or electron diffraction, with an order parameter;
   - the composition, by EDS, RBS, XRF or XPS;
   - the wafer-level texture fraction and in-plane variant distribution, from XRD rocking curves or pole figures;
   - intermixing or oxidation at the MgO interfaces, from EELS or EDS;
   - a magnetic signature of the noncollinear order in an unpatterned film, such as the anomalous Hall effect or the temperature of the transition.

   Without these, the assumptions of a T1g state and of k∥-conserving tunnelling cannot be assessed.

   Raised by: r1, r2, r3

8. **The energy-barrier analysis (Fig. 2d, Extended Data Fig. 3) is ambiguous, and its agreement with theory is circular.**
   - The two branches give different values. Reading the fitted lines in Fig. 2d gives J_c0 ≈ 190 MA/cm² with Δ ≈ 25–30 kT for AP→P, and J_c0 ≈ 130 MA/cm² with Δ ≈ 45–55 kT for P→AP. The quoted 39 kT appears to be an average, and the asymmetry is not discussed.
   - Taken at face value, the AP→P line reaches J ≈ 0 near ln(tp/t0) ≈ 26, about 0.2 s. That implies an AP state that relaxes on its own within about a second, which conflicts with "moderately large thermal stability".
   - Δ depends on the assumed t0 = 1 ps, an antiferromagnetic attempt time, rather than the ~1 ns usual for ferromagnets.
   - The Koch et al. model (ref. 50) assumes a single-domain free layer, a barrier lowered linearly by STT, and no heating. The authors themselves invoke multidomain switching, the paper's NV data suggest domains of about 100–170 nm, and ms pulses at mW power make heating likely, which also produces a pulse-width dependence.
   - The Methods (p. 23) obtain Keff = 1 kJ/m³ by "matching the numerics to Δ = 39 kT evaluated from OTT switching currents". The statement on p. 7 that 39 kT is "consistent with our theoretical estimation" is therefore circular.
   - This Keff is about three orders of magnitude below the giant single-ion anisotropy expected for L1₂ Mn3X (ref. 51). It also differs from the Ku = 10 kJ/m³ used in the LLG simulation.
   - The device (diameter) is not identified, and the error bars are not defined.

   The authors should report Δ for each branch with fit uncertainties and its sensitivity to t0, show results on more than one device, and either derive Keff independently or remove the claim of agreement.

   Raised by: r1, r2, r3

9. **The quoted switching current density does not match the data shown.** The abstract and p. 6 give J ≈ 11 MA/cm² and say that pillars from 50 to 200 nm switch "at similar J values". Fig. 2a (100 nm, about 1 mA) does give about 12 MA/cm². The other figures disagree.
   - Fig. 2d gives about 50 to −80 MA/cm² at ln(tp/t0) ≈ 20.7 (1 ms), with the full range spanning about 10–90 MA/cm².
   - In Extended Data Fig. 1, 50 nm pillars at about 0.4–0.6 mA give about 20–30 MA/cm².
   - 100 nm devices give about 13 MA/cm² (1 mA), about 50 MA/cm² (4 mA) and about 75 MA/cm² (−6 mA).
   - 200 nm devices at about 2.5–4 mA give about 8–19 MA/cm².

   This order-of-magnitude spread at fixed diameter matters for both the mechanism and the efficiency claim. The authors should plot J_c for both polarities against diameter and RA for all switching devices, with medians and spread, state whether J_c depends on diameter, and revise the headline number.

   Raised by: r1, r2, r3

10. **The TMR values and the "record-high" claim rest on one device, and the transport reporting is incomplete.** The 363% value comes from one of 36 devices. Fig. 2b shows that 23 of the 36 devices have TMR below 100%, and the Fig. 2c device shows about 50–55%. RA computed from R_P and the nominal diameter varies systematically with size: about 1.5 Ω·μm² at 50 nm (Extended Data Fig. 1a), about 2–4 Ω·μm² at 100 nm, and about 5–7 Ω·μm² at 200 nm. This points to series resistance, lithographic size deviation or pinholes, any of which affects both J and TMR. The read bias, the bias dependence of TMR, and the lead and electrode series resistance in the two-terminal geometry are not reported. The authors should:
    - give R_P, RA, TMR and J_c for every device, how many of the 36 switch, and how many wafers or dies the devices come from;
    - state typical and median TMR alongside the maximum in the abstract, title and introduction;
    - discuss why a junction with an amorphous barrier and polycrystalline electrodes would exceed the TMR of epitaxial Mn3Pt AFMTJs (ref. 12);
    - temper "record-high" until the magnetic origin is confirmed (concern 1).

    Raised by: r1, r2, r3

11. **The temperature evidence (Fig. 2c) is too sparse to tie the switching to the noncollinear–collinear transition.** Fig. 2c shows one device at four temperatures (300, 330, 360 and 400 K), with nothing between 330 and 360 K. Several things are not reported:
    - the switching currents at 330 K compared with those at 300 K;
    - R_P(T) and R_AP(T);
    - whether the TMR itself vanishes at 360 K, or only the ability to switch;
    - the transition temperature of these films, measured independently;
    - whether switching and TMR come back on cooling to 300 K.

    The last point matters because barrier degradation or interdiffusion after heating to 400 K would also remove the hysteresis. Losing a metastable high state at 360 K is also consistent with a small Δ. If heating drives the switching, J_c should fall steeply as the base temperature approaches about 360 K. The authors should provide a finer temperature series of J_c(T) and TMR(T) on several devices, a reversibility check, an independent measurement of the film's transition by magnetometry or AHE, and an estimate of the temperature during the pulse.

    Raised by: r1, r2, r3

12. **The NV-magnetometry domain argument uses an unrepresentative film and is contradicted by the device data.** The NV sample (Extended Data Fig. 2; Methods, p. 19) is an epitaxial (100) PtMn3 film, co-sputtered on an MgO(100) substrate annealed at 850 °C. The device layers are polycrystalline, (111)-textured and grown at room temperature on Pt, without annealing, so domain sizes can differ greatly. The paper does not say how "~100–170 nm" was extracted from the Fourier spectrum (Extended Data Fig. 2b). It does not show that the stray-field contrast comes from octupole domains rather than from Mn termination, grain-scale surface moments, roughness or uncompensated Mn, and it has no nonmagnetic or above-transition control scan. The device data also contradict the claim that only pillars comparable to or smaller than the domain size switch abruptly (p. 6): in Extended Data Fig. 1, some 200 nm pillars switch sharply and some 50–75 nm pillars switch gradually. The authors should image domains or measure grain sizes in the (111) device stack, ideally before and after current switching or in a field (or at least give plan-view TEM grain-size statistics), or soften the argument.

    Raised by: r1, r2, r3

13. **Reproducibility, yield and endurance are not quantified.** The paper asserts "reversible, repeatable" switching (p. 6), and Fig. 2a shows a single loop. The paper does not report:
    - the number of consecutive cycles per device;
    - cycle-to-cycle distributions of R_high, R_low and I_c;
    - switching probability against pulse amplitude at fixed width;
    - yield, meaning how many devices were made, how many switch, and how many switch abruptly rather than in multiple levels;
    - retention of both states;
    - endurance, and whether devices degrade or break down after repeated multi-volt pulses or after thermal cycling to 400 K.

    These data bear on both the mechanism and the MRAM claims in the Discussion. Abrupt bipolar switching that degrades or drifts with cycling would point to a barrier origin.

    Raised by: r1, r2, r3

14. **Material parameters disagree between the energy-barrier model and the LLG model.** The barrier calculation uses Ms = 1110 emu/cm³ (1110 kA/m), Keff = 1 kJ/m³ and J = 280 MJ/m³ with J > 0. Extended Data Table 1 uses Ms = 153 kA/m, Ku = 10 kJ/m³, and A_AB = −10 pJ/m with a0 = 0.5 nm. The PtMn3 lattice parameter is about 0.38–0.39 nm, and it is unclear whether the two exchange values describe the same exchange field. The free-layer thickness is 7 nm in one model and 10 nm in the other. The simulated switching speed and threshold depend on Ku and Ms. The authors should use one consistent parameter set, justify it against literature values for Mn3Pt, and state which results depend on it.

    Raised by: r1, r2, r3

15. **The novelty framing overstates the prior consensus.** The abstract says STT in AFMTJs "has been assumed non-existent". The paper itself cites theoretical predictions of spin-transfer torque in noncollinear antiferromagnetic junctions (refs. 44–47, 60). Ref. 46 (Ghosh et al.) explicitly predicts robust STT in such junctions. Current-induced switching in AFM-based tunnel junctions has also been reported (for example ref. 26). The authors should state exactly what is new, especially relative to ref. 46's torque mechanism, and temper "first experimental observation" until concerns 1–3 are resolved.

    Raised by: r1, r3

**C. Minor**

16. **The DFT methods need correcting or justifying.** The Methods say PBE but cite ref. 64, which is PBEsol; state which functional was used. Justify U = 2 eV for metallic Mn in PtMn3 and show that the conduction-channel anisotropy is robust to U. SOC is included, yet the mechanism is called non-relativistic, so show the maps without SOC to separate the two contributions. State whether the T1 configuration is the computed ground state, and whether the lattice and magnetic structure were relaxed (with SOC), with the resulting moments. The spin polarization is "extrapolated from VASP calculations and interpolated onto the 120×120×80 k-mesh", while the site projections come from the Wannier model; explain how the two are made consistent, and give the Wannier k-mesh and the convergence of the projected channels.

    Raised by: r1, r2, r3

17. **Fig. 3 is hard to read quantitatively, and its colour scale is unclear.** Fig. 3a,b and Extended Data Fig. 4 show absolute channel counts, from which the claimed dominance of one sublattice along each Γ–K axis is hard to judge. Add difference maps (each sublattice minus the average) and integrated β1 and β2 values. The Fig. 3b colour bar runs from 0 to 15, but the plotted quantity is a spin polarization N(i↓) − N(i↑), and the minority channel is said to dominate along Γ–M, which should give negative values. Give the sign convention and fix the colour bar. Label Fig. 3c–e as schematic, say which band and energy the "select band" is, and explain in the Fig. 3c caption what the triangles and arrow colours denote.

    Raised by: r1, r2, r3

18. **The majority and minority notation is confusing.** Majority is written N(i↓) and minority N(i↑) (p. 8, Extended Data Fig. 4), and "octupole minority" is T₊ (p. 9, Methods). Define the conventions once.

    Raised by: r2

19. **The devices and error bars in Fig. 2 are not specified.** Give the pillar diameter and RA for the devices in Fig. 2c and Fig. 2d. State how J was computed (nominal or SEM-measured area), the read-current magnitude, and whether the quoted TMR includes series lead and electrode resistance. Define the Fig. 2d error bars: number of repetitions, and whether they are a standard deviation or a range.

    Raised by: r1, r2, r3

20. **Extended Data Fig. 5 is hard to follow.** In panels b and c, the initial and final states are hard to reconcile with the stated initialization along −e_i; for example, the solid m_y3 trace appears to start near +1 and end at −1. Mark the initial and final configurations, and confirm that the final state is the other energy minimum of Extended Data Fig. 3, a full reversal of m_i.

    Raised by: r3

21. **The equations and notation have errors.** In Eq. 9 the torque term T_i sits inside the bracket multiplied by μ0, which mixes field and torque units. Eq. 11 is written as a scalar, 2Ku/Ms m_i·e_i, but should be the vector 2Ku/Ms (m_i·e_i) e_i. State the sign convention for A_AB = −10 pJ/m. J stands for both current density and exchange (Methods Eqs. 1–2), and Eq. 4 calls J "the applied current"; use distinct symbols and state units. Ms is given in emu/cm³ in the barrier calculation and in kA/m in Extended Data Table 1; use one unit system.

    Raised by: r1, r2, r3

22. **There are cross-reference, citation and typographical errors.**
    - The Micromagnetic Methods (p. 26) refer to "Extended Data Fig. 1a with the green arrows"; this should be Extended Data Fig. 5a.
    - Reference 34 is missing from the list, which jumps from 33 to 35.
    - Ref. 56 is cited in the main text before refs. 51–55.
    - Refs. 60 and 61, cited for Keff literature values, do not obviously report PtMn3 anisotropy.
    - "theorectical" in the author contributions is a typo.

    Raised by: r1, r2, r3

23. **The NV Methods description of the filter is unclear.** The Gaussian filter (σ = 16 nm) is smaller than the 20 nm scan step, so the statement that it acts almost as an identity needs explaining. Give the domain-size extraction from the power spectrum (Extended Data Fig. 2b) explicitly.

    Raised by: r1

24. **Some outlook statements go beyond the data.** "Fully eliminating dipole interaction" ignores that a thin PtMn3 film may carry a small net moment. The abstract's "room-temperature terahertz technologies" is not supported, since no dynamics were measured. Tone both down.

    Raised by: r2
