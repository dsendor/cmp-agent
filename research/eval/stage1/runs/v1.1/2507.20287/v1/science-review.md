A. Must address

1. **The strong-coupling conclusion is fixed by setting δ_z = 0 by hand rather than computing it.** In the SBMF section (Sec. B, p. 5, left column) the paper states: "Due to absence of γ-pocket formed mainly by the d_z2 orbital, we have δ_z = 0, resulting in Δ^z_SC = 0." Because Δ^z_SC = δ_z Δ^z_spinon, this step alone removes d_z2 from superconductivity, so d_x2-y2 interlayer pairing dominates by construction. Having no γ-pocket means the *bonding* d_z2 band is full; it does not mean the d_z2 orbital is exactly half-filled. Fig. 2(b) shows substantial d_z2 weight on both the α and β pockets, so the antibonding d_z2 states are partly occupied, and the t^xz hybridization in Table I moves weight between orbitals. The SBMF's own spinon amplitudes (p. 4) are Δ^z_⊥ = 1.51 × 10⁻¹ eV and Δ^x_⊥ = 1.28 × 10⁻³ eV, about 100 times apart, so a d_z2 hole density of only about 1% would make δ_z Δ^z_⊥ comparable to or larger than δ_x Δ^x_⊥. The headline strong-coupling statements ("the d_x2-y2 orbital electrons form interlayer s-wave pairing", "the dominant superconducting channel becomes the interlayer pairing of the d_x2-y2 orbitals") and the claim that the strong-coupling result independently confirms the weak-coupling one would then not hold. The authors should compute the orbital-resolved fillings n_z and n_x from the TB model of Table I at the chemical potential and electron count used, report δ_x (never given numerically) and δ_z = 1 − n_z, and redo the SBMF with the computed δ_z, or show Δ^x_SC and Δ^z_SC, and the leading channel, over a plausible range of small δ_z. They should also state the total electron count per Ni used in both the RPA and SBMF.
Raised by: r1, r2, r3

2. **In the RPA, s± beats d-wave by a small margin that is never tested.** Fig. 3(b) shows λ_s and λ_d nearly degenerate over the whole range U = 1.10–1.25 eV (about 0.16 vs 0.15 at U = 1.25 eV; the text says λ_d is "slightly smaller"). This is at a single Hund's ratio J_H = U/6, with V fixed by U = V + 2J_H, at one filling, one TB parameter set and an unstated temperature and k-mesh. The final choice of s± then rests partly on an outside argument, the ARPES report of no node near the pocket-touching momentum (Ref. 106, p. 3), rather than on the calculation. A near-degeneracy like this is often reversed by modest changes in J_H/U, filling or the position of the bonding d_z2 band top, so the weak-coupling half of "both approaches give s±" (the abstract's "consistent results") is not yet established, and Sec. A's "s-wave pairing dominates over other pairing symmetries" overstates it. The authors should show λ_s and λ_d as functions of J_H/U (for example 0–0.25), of electron filling or hole doping (relevant because films are often oxygen-off-stoichiometric and Pr-substituted), and of a rigid shift of the bonding d_z2 band top (see concern 3); state the electron count, chemical potential, temperature and k-mesh, with convergence checks; report the s/d margin quantitatively, including how close U is to U_c in each case; and, if d-wave wins in part of the parameter space, say so in the abstract and conclusions.
Raised by: r1, r2, r3

B. Should address

3. **The γ-pocket-free band structure rests on one untested DFT+U choice and is not tied quantitatively to experiment.** Everything follows from a single DFT+U calculation (U = 3.5 eV, a fixed at the substrate value, c = 20.72 Å fixed with internal positions relaxed, pure La3Ni2O7 in a periodic bulk cell). It puts the bonding d_z2 band top about 300 meV below E_F at M (Fig. 1c) and gives t^z_⊥ = −0.6408 eV, larger than in earlier TB models (Refs. 95, 98). Whether the films have a γ-pocket is exactly what is disputed, and this band position is known to depend on U, the c-axis length, apical-oxygen relaxation and magnetism. The paper does not say whether the calculation is spin-polarized, does not explain why its t^z_⊥ differs from Refs. 95 and 98, which use similar film structures, omits the Pr substitution of the measured (La,Pr)3Ni2O7 and possible Sr interdiffusion from the substrate, and does not compare the 300 meV offset with the binding energy measured in the ARPES it cites as support (Refs. 102, 111). If the experimental band top is much closer to E_F, γ-band states near M still lie within the energy scales that matter for the RPA susceptibility and pairing kernel. The authors should show the band top at M and t^z_⊥ for several U values (for example 0–5 eV), compare directly with the ARPES binding energy, and, if the offset is overestimated, repeat the pairing calculation with the band placed at the experimental energy (by tuning t^z_⊥ or ε_z), stating what parts of the result survive.
Raised by: r1, r2, r3

4. **"γ-pocket not necessary" is asserted without a same-model comparison.** The Discussion concludes that "the presence of the γ-pocket is not necessary to the pairing mechanism". The paper shows that pairing occurs without the pocket, but not what the pocket changes when present within the same framework; the 30 GPa bulk comparison uses a different model and is in the Supplementary Material. The authors should take the film TB model, move the bonding d_z2 band top continuously from about −300 meV through E_F (rigid shift of ε_z, or a bulk-like t^z_⊥), and track λ_s, λ_d, the leading symmetry, the real-space amplitudes (against Figs. 3 and 4a) and the SBMF order parameters. This would turn "pairing without the γ-pocket" from one data point into a demonstrated trend, and would also make clear how the work differs from the earlier film calculations by this and other groups (Refs. 95, 98, 99–105, 110, 114), which the paper currently does not state.
Raised by: r1, r2, r3

5. **The STM comparison (Fig. 4b) has no stated parameters and does not discriminate s± from other states.** The abstract and Discussion say the results are consistent with STM (Ref. 108), and the text says the spectrum indicates "the possibility of the s±-wave pairing". But the RPA fixes only the gap's form, not its size, and the paper does not say how the gap amplitude Δ_km in Eq. (12) was chosen, what finite broadening replaces i0⁺ in Eqs. (12)–(13), or how the theory and experimental curves were normalized and aligned; these appear adjusted to match the data. The text does not say which sample and conditions Ref. 108 measured (film or bulk, pressure, temperature). Eq. (13) is a bulk k-summed DOS, ignoring STM's surface-layer selectivity and orbital-dependent tunnelling matrix elements, and such a DOS does not depend on the relative gap sign between α and β, so an s++ gap with the same magnitudes would give the same curve. The authors should list every parameter entering the curve and say which were adjusted; overlay spectra for the subleading d_x2-y2 state of Fig. 3(d) and a sign-preserving s++ state computed the same way; present the agreement as consistency with a nodeless gap rather than support for s± specifically; and, ideally, suggest a phase-sensitive test (quasiparticle-interference sign analysis, Josephson junctions).
Raised by: r1, r2, r3

6. **The SBMF gap scale is not reported and appears inconsistent with experiment.** The physical d_x2-y2 order parameter is δ_x Δ^x_⊥ with Δ^x_⊥ = 1.28 meV, so it is at most about 1 meV for any δ_x < 1. That is small next to T_c ≈ 40 K (k_B T_c ≈ 3.4 meV) and next to the 20–30 meV gap features on the Fig. 4b axis. The authors should give δ_x and the resulting gap in meV, comment on whether the SBMF scale (or the chosen J_⊥) is compatible with T_c and the measured gap, discuss whether the ~100-fold suppression of Δ^x_⊥ relative to Δ^z_⊥ is physical or an artefact of how J_⊥ enters the d_x2-y2 channel (concern 8), and, if the mean-field scale is known to be unreliable, say so and drop the quantitative statements.
Raised by: r1, r2, r3

7. **The film-versus-bulk comparison and other key results are deferred to a Supplementary Material that is not provided.** The p. 5 claim that "the superconducting gap in the film system at AP is significantly smaller than that in the bulk … consistent with experimental observations" is stated without numbers, and the two-factor explanation (reduced hoppings and the missing γ-pocket; the x orbital becoming "more overdoped") cannot be checked without δ_x for both systems. "The complete set of obtained mean-field spinon order parameters" is also deferred. The authors should give, in a main-text table, the film and 30 GPa bulk gaps, orbital fillings (δ_x, δ_z) and main hoppings, the ratio of the gaps compared with the ratio of experimental T_c values, and say which experimental observations these are consistent with.
Raised by: r1, r2, r3

8. **The Hund's-transmitted interlayer exchange on d_x2-y2 is put in by hand.** In Eq. (3) the full J_⊥ is applied to the d_x2-y2 spins as if Hund's coupling passed it on without loss, effectively the same J_⊥ ≈ 2J_∥ ≈ 0.4 eV used for d_z2; it is unclear whether "J_⊥" in that expression refers to the x or z channel. In a strong-coupling derivation the transmitted coupling depends on J_H/U, on how localized d_z2 is and on the d_x2-y2 occupation, and should be reduced. The model has no explicit on-site S_x·S_z interorbital coupling encoding the Hund's constraint and no intralayer J for d_z2, and the J_⊥ ≈ 2J_∥ estimate via J ∝ t² uses (t^z_⊥/t^x_1)² ≈ 1.8 from Table I (which should be said explicitly) but neglects t^xz. Combined with δ_z = 0, a large x-channel J_⊥ makes an interlayer s-wave d_x2-y2 state close to guaranteed. The authors should justify the size of the transmitted coupling (for example from second-order perturbation theory in t^z_⊥ with J_H, or a citation that derives it) and show how Δ^x_⊥, the Δ^x_⊥/Δ^x_∥ hierarchy and the s± result change as the x-channel J_⊥ and J_∥ vary around the chosen values, ideally as a phase diagram in the (δ_z, J^x_⊥) plane.
Raised by: r1, r2, r3

9. **The interaction scales are inconsistent across the three calculations.** The DFT+U uses U = 3.5 eV, the RPA uses U ≈ 1.1–1.25 eV (just below U_c = 1.33 eV), and the t-J model uses J_∥ ≈ 0.2 eV and J_⊥ ≈ 0.4 eV. Using U in DFT+U and again in the RPA also raises a double-counting question. The authors should briefly justify why the RPA U is a reasonable effective interaction for this band structure, and how the t-J exchange values follow from the same microscopic parameters (for example J = 4t²/U with which U).
Raised by: r2

10. **The model is a bulk crystal at film lattice constants, not a film.** The DFT uses a periodic bulk cell with in-plane strain from SrLaAlO4, but the films are a few unit cells thick. The interface and surface, possible oxygen off-stoichiometry and the resulting doping, and Pr substitution are not discussed; the title and text say La3Ni2O7 while the cited experiments are on (La,Pr)3Ni2O7. At minimum the paper should state these are left out and estimate how a modest doping (say ±0.05 holes per Ni) would shift the α and β pockets and the RPA result.
Raised by: r1, r3

11. **The real-space RPA pairing amplitudes (Fig. 4a) need context.** The RPA eigenvector is defined only up to normalization, and its real-space decomposition depends on basis and gauge. The authors should say how Δ^x_⊥, Δ^z_0 and the other amplitudes were extracted (Fourier transform of the orbital-basis gap on the Fermi surface or over the whole Brillouin zone), and check that the dominance of Δ^x_⊥ persists for the other U values in Fig. 3(b).
Raised by: r2

12. **The layer-parity character of the α and β pockets, which sets the s± sign structure, is not explained.** In the SBMF an interlayer s-wave pairing gives a sign change only if α and β have opposite bonding/antibonding (k_z = 0/π) character, but Fig. 2(b) shows only d_z2/d_x2-y2 orbital weight. The authors should show or state the layer-parity character of each pocket; this would make clear why the RPA and SBMF sign structures agree and why the RPA spin susceptibility peaks at Q ≈ (0.64π, 0.64π).
Raised by: r3

C. Minor

13. **Missing calculation details.** State the electron filling per Ni and chemical potential of the TB model, and give E_F or μ on the same scale as the absolute Wannier on-site energies in Table I (ε_z = 9.0974 eV, ε_x = 9.8963 eV) so the orbital splitting and filling can be read off; note that t^x_⊥1 = t^x_⊥2 = 0. For the RPA give the temperature, k-mesh and number of pairing eigenvectors examined; for the SBMF the temperature, k-mesh, convergence tolerance and whether χ order parameters are kept for both orbitals. For the DFT state whether it is spin-polarized, whether spin–orbit coupling is included, which DFT+U flavour (Dudarev or Liechtenstein) is used, and show that the coarse 8 × 8 × 2 k-mesh converges the band edge ~300 meV below E_F and the Wannier fit.
Raised by: r1, r2, r3

14. **Fig. 4(b) labelling and legend.** Label the vertical axis (normalized dI/dV or A(ω), arbitrary units) and state the normalization; the legend should cite Ref. [108] rather than "arXiv:2506.01788".
Raised by: r1, r2, r3

15. **Equations for the STM calculation.** In Eq. (12), "ε_kα is the m-th eigenvalue" should read ε_km; u_km and v_km are introduced with a site-diagonal sum but no normalization; and the connection between the band-resolved Δ_km and the real-space RPA gap of Fig. 4(a) should be stated.
Raised by: r1, r3

16. **Section lettering and duplicate equations.** Sections A and B under Results run straight into C–G under Methods; relabel the Methods subsections separately. Eqs. (2) and (9) are identical; refer back instead.
Raised by: r2, r3

17. **Wording of the γ-pocket on p. 2.** "The d_z2 band does not cross the Fermi level at the Γ point, and thus forms no electron pocket" conflicts with the bulk γ-pocket being a hole-like pocket around M, as the preceding sentence about the band top at M implies. Please correct or clarify.
Raised by: r1

18. **Eq. (1) notation.** The V term has no spin indices and the J_H term mixes orbital labels; state the conventions, including the meaning of α in n_iμα.
Raised by: r1

19. **Spinon amplitude definition.** On p. 4, "Δ^α_spinon = (3/8)J⟨…⟩" does not say which J (J_∥ or J_⊥) belongs to which channel; make it consistent with Eqs. (15)–(16).
Raised by: r1

20. **Colour scales in Figs. 3 and 6.** Fig. 3(a) should state the quantity plotted (largest eigenvalue of the χ matrix, or the trace) and label its 4–12 colour scale. Figs. 3(c,d) and 6(b) should say whether the gaps are normalized. The α/β signs in Fig. 3(c) are the reverse of those in Fig. 6(b); note this as a global phase so readers do not see a contradiction.
Raised by: r1, r2

21. **Order of the Fig. 3(d) / Ref. 106 argument.** State once, early, why the d-wave solution of Fig. 3(d) is shown and how Ref. 106 rules it out; at present "This is inconsistent with the ARPES results" (p. 3) appears before the reader knows which state is being ruled out.
Raised by: r3

22. **Fig. 1(c) caption.** The caption refers to "red and blue markers" while the legend uses squares and circles; make them match.
Raised by: r3

23. **Language and typos.** "a lot of interests", "Then some teams study", "it is needed to explain", "pairing nature"; "spionon" → "spinon" (p. 4); "ab inito" → "ab initio" (p. 5).
Raised by: r2, r3

24. **Reference list.** Refs. [92]–[114] mix arXiv and journal formats and some are incomplete (for example Ref. [94], "Nature Materials, 1 (2025)"); please complete them.
Raised by: r1

Verdict: major revision
