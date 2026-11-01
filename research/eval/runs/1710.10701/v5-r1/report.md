# Lookalike check: Quantized Majorana conductance (arXiv 1710.10701v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first.

**The claim, as I read it.** A zero-bias peak in InSb-Al nanowires whose height stays at
2e²/h as the field (Fig. 1b, 0.75 to 0.92 T) and tunnel gate (Fig. 2a to 2e) change in
device A, with a second tunnel-gate plateau in device B (Fig. 4b), read as a Majorana zero
mode. Device C (Fig. 5) is your trivial comparison. All data are local tunneling from one end.

## Checks a careful reader will look for

1. Unintended quantum dots near the barrier : Partly. The tunnel-gate maps of A and B (Figs. 2a, 4b) show no level crossings near zero bias; a zero-field search above the gap is shown for device C only: "No localization effect (conductance resonances or quantum dot induced Coulomb blockade) is observed." (Ext. Data Fig. 4b, p. 22). Fig. 3b shows peaks that split and rejoin.
2. Peak over wide gate, field and field-angle ranges : Partly. Field and tunnel gate for A and B, super-gate for A (Fig. 3a, 3b); the back gate stays at 0 V in A, and "Magnetic field direction is aligned with the nanowire axis for all measurements." (Fig. 1 caption, p. 12).
3. Tunneling at both ends at the same settings : Not done.
4. Peak stays as the junction transparency changes : Done. "Fig. 2b shows that the ZBP-height remains close to the quantized value." (p. 5), and Fig. 4b for device B.
5. Nonlocal gap closing and reopening : Not done. You note "The gap re-opening is not visible in a measurement of the local density-of-states" (p. 4).
6. Series resistance and raw data : Not done. The paper doesn't say whether a series resistance was subtracted.
7. Device and dataset counts : Partly. "We fabricated and tested many (>60) devices out of which we selected 11 devices, which did show good basic transport with all gates being fully functional." (Ext. Data Fig. 7, p. 26). Cooldowns and datasets aren't counted.
8. Full ranges measured, and why each shown range was chosen : Not done.
9. Processing from raw data to figures, with data and code : Not done. The Methods describe the fits (p. 17); the step from measured signal to conductance is not described.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Andreev states in an unintended quantum dot | Tested in part | Dot signatures in the same device: part (tunnel-gate maps of A and B near zero bias; no above-gap or zero-field dot search for A or B); both ends: no | "The two different behaviours between back-gate and tunnel-gate are expected for ABSs that are localized near the tunnel barrier" (p. 9, Fig. 5) | Show zero-field tunnel-gate and bias maps of A and B up to above the gap, as you did for C in Ext. Data Fig. 4b |
| Quasi-Majorana states from smooth confinement | Not tested (argued, not tested) | Nonlocal gap closing and reopening: no; correlated zero modes at both ends: no | "Only a stable quantized tunnel-conductance plateau, robust against variations in all gate voltages and magnetic field strength, can uniquely identify a topological Majorana zero-mode as far as tunnelling spectroscopy is concerned." (p. 9) | Say whether any wider field or super-gate data of A show where the peak first appears relative to the bulk gap; a two-probe device would test it directly |
| Disorder-induced subgap states | Tested in part | End-to-end correlation: no; bulk gap closing and reopening: no; insensitivity to gates that should not matter: part (tunnel gate in A and B; back gate not varied) | "We emphasize that the robustness of the ZBP quantization to a variation in the tunnel barrier is an important finding of our work." (p. 5) | Sweep the back gate of A at the plateau settings and show the zero-bias height |
| Crowded trivial subgap states from several subbands | Tested in part | Field and gate range against the predicted topological range: part (field compared with simulation; gate to chemical potential unknown); subband model of the device: no | "While most of these devices show ZBPs after tuning gate voltages and magnetic field, only 2 devices (presented in the manuscript, Figs. 1,2,3 for device A and Fig.4 for device B) show a quantized ZBP-plateau." (Ext. Data Fig. 7, p. 26) | Tabulate where ZBPs appeared in the 11 devices against the field and gate range your model predicts |
| Kondo resonance | Tested in part | Even-odd occupancy: no; temperature dependence: part (device B only, Fig. 4d to 4f); Zeeman splitting in field: all (no peak at 0 T in A or B; it forms at finite field) | "As B increases, two levels detach from the gap edge (at ~0.2 meV), merge at zero bias, and form a robust ZBP." (p. 3, Fig. 1b) | Show the temperature series for device A as well |
| Weak antilocalization | Ruled out for the claim | Pikulin et al. barrier test: all (A and B); channel number or disorder: no. The barrier test alone separates it, since Pikulin et al. find a higher barrier suppresses the antilocalization peak and leaves the Majorana resonance | "the above-gap conductance measured at \|V\| = 0.2 meV varies by more than 50% (Fig. 2c and 2d), implying that the transmission is changing significantly over this range while the ZBP remains quantized." (p. 5) | None needed |
| Fine-tuned plateau | Tested in part | How the plateau was found: no; same peak over wider ranges: part (field and tunnel gate for A and B, super-gate for A; back gate and field angle fixed); peak heights from other regimes and devices: all (Fig. 3b, Fig. 4b, devices C and D) | "We find, however, from a rough estimate of this background contribution that the net ZBP-height (above background) never exceeds 2e2/h, consistent with Majorana theory9." (p. 7, Fig. 4b) | Show the background estimate behind Fig. 4b and extend the tunnel-gate scan of Fig. 2a past -7.65 V |
| Series resistance choice | Not tested (not mentioned) | Series resistance calibrated, with value: no; raw data before subtraction: no | Not discussed. | State the line, filter and contact resistance, whether it was subtracted, and show raw data for Figs. 2b and 4b |
| State at one end only | Not tested (argued, not tested) | Both ends at the same settings: no; nonlocal conductance: no | "A more negative gate voltage effectively pushes the nearby Majorana mode away, towards the remote Majorana on the other end of the wire" (pp. 5 to 6, Fig. 2d) | Say whether the drain end of any device can be tunneled into; a two-probe geometry would test it |
| Pinning from the spin-orbit length | Ruled out for the claim | Pinning tested against parameters other than field: all (tunnel gate in A and B, super-gate in A) | "For the Majorana case, instead of level crossing, the ZBP should remain non-split over sizable changes in tunnel-gate voltage13, as shown in Fig. 2a and Fig. 4b." (p. 9) | None needed |
| Exceptional-point zero mode | Not tested (not mentioned) | Overlap of the two Majorana components: no | Not discussed. | A nonlocal or dot-assisted overlap estimate, which needs a second probe or a dot in series |
| Local-probe loophole | Not tested (argued, not tested) | Nonlocal measurement: no; overlap through a quantum dot: no | "Only a stable quantized tunnel-conductance plateau, robust against variations in all gate voltages and magnetic field strength, can uniquely identify a topological Majorana zero-mode as far as tunnelling spectroscopy is concerned." (p. 9) | State in the text that a local probe cannot measure the separation of the two Majorana components |
| Fine-tuning and selection | Tested in part | Devices measured and how many showed it: part (devices counted, cooldowns and datasets not); how the shown data were chosen: no; second device shown: all (device B) | "Here we show the SEM images of all other 8 devices, which we have explored extensively, but without finding a quantized ZBP-plateau." (Ext. Data Fig. 7, p. 26) | Describe how the gate settings of Figs. 1b and 2a were found, and show the best ZBP of one of the other eight devices |

## Questions about devices and data

1. Extended Data Fig. 7 gives the device count (more than 60 fabricated, 11 measured, 2 with a plateau). How many cooldowns and datasets lie behind A and B, and in how many did the plateau appear?
2. Extended Data Fig. 7 says the 11 were kept for working gates and nine showed no plateau. What peak heights did those nine reach, and was any set aside for another reason?
3. Which back-gate, field-angle and tunnel-gate ranges did you measure on A and B beyond those shown, in particular above -7.65 V, where Fig. 2a ends with the plateau still in place?
4. What does the second-best dataset look like, on A or B or on one of the other nine devices?
5. Was a series resistance (lines, filters, contacts) subtracted for Figs. 1 to 4? If so, what value, and how was it calibrated?
6. How was the background contribution in device B estimated (Fig. 4b), and could you show the zero-bias height with and without it?
7. In Fig. 3a the tunnel gate is adjusted while the super-gate is swept. What compensation rule did you use, and how does the plateau look without it?
8. How long did the search for the settings of Fig. 1b and Fig. 2a take, and how many settings were tried before the plateau appeared?

## Related work

- Yu et al. 2020, "Non-Majorana states yield nearly quantized conductance in superconductor-semiconductor nanowire devices", <https://arxiv.org/abs/2004.08583>. InSb nanowires with probes at both ends: nearly 2e²/h peaks at one end, dips at the other for the same settings.
- Liu, Sau, Stanescu and Das Sarma 2017, "Andreev bound states versus Majorana bound states in quantum dot-nanowire-superconductor hybrid structures: Trivial versus topological zero-bias conductance peaks", <https://arxiv.org/abs/1705.02035>. Theory: dot-induced Andreev states coalesce near zero energy, mostly in the trivial regime, with near-identical tunneling signatures.
- Kells, Meidan and Brouwer 2012, "Near-zero-energy end states in topologically trivial spin-orbit coupled superconducting nanowires with a smooth confinement", <https://arxiv.org/abs/1207.3067>. Theory: a smooth end potential gives trivial end states at exponentially small energy.
- Pikulin et al. 2012, "Zero-voltage conductance peak from weak antilocalization in a Majorana nanowire", <https://arxiv.org/abs/1206.6687>. Theory: disorder gives a zero-voltage peak of order e²/h without a topological phase, and raising the tunnel barrier suppresses it.
- Wang et al. 2022, "Plateau regions for zero-bias peaks within 5% of the quantized conductance value 2e²/h", <https://arxiv.org/abs/2205.06736>. In a thin InAs-Al nanowire, peak heights stay mostly within 5% of 2e²/h over gate and field sweeps, in a device the authors say has disorder and quantum dots.

Happy to rerun this if you share the figure data or the raw two-terminal measurements.
