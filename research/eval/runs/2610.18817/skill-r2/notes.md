# Run notes: arXiv 2610.18817v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.4 (updated 2026-10-23), 28 lookalikes, checks for families zbp, shapiro, kitaev, charge, practice.
- Skill files read once at start: skill/SKILL.md, skill/report-template.md, the library (including `checks`). read_mtx.py not used (no figure data).
- Date of run: 2026-10-23. Label: AI only.

## What I read
- Abstract page: the local copy of abs.html (title "Single anyons and anyon binding in a quantum Hall dot", v1 submitted 13 Oct 2026, Valentini, Wang, Shapour Mohammadi et al., cond-mat.mes-hall). I did not fetch the paper or any version of it, per instructions.
- Full text: the local paper.txt, plus the local paper.pdf (24 pages), split page by page with pdftotext to assign page numbers. The page numbers are PDF pages, which match the printed page numbers. Every quote in the report was string-matched against its page's text (Fig. 4f caption quote: the PDF line-break hyphen in "charge-degeneracy" was restored).
- The supplementary material is in the PDF: Methods, Tables I to III, Extended Data Figs. 1 to 11. All were read.
- Ancillary files and data repository: the abstract page lists none, and the paper has no data or code availability statement that I could find. No figure data, so step 1's file listing does not apply. No repository was used.
- Could not open: nothing I tried failed.

## Claims table (step 1)
| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| Integer dot at ν = 1: Coulomb blockade backscattering, EC ≈ 2 meV, δ ≈ 250 to 300 mV | Fig. 1f, 1g, 1j; ED Fig. 2 | one device (monolayer graphene QPC with 90 nm hole) | B = 5 T (also 8.97, 13.4 T for QH in Fig. 1j); Vdot windows in Table I; gate maps ED Fig. 2 |
| Depletion to last quasihole, spin blockade for quasielectrons, magnon-assisted lifting above EZ ≈ 0.58 meV | Fig. 2a to 2f | same | B = 5 T; Vdot about -3 to 4 V; VDC about ±2.3 mV |
| DMRG matches δ trend vs Nqp at ν = 1 | Fig. 2g, 2h | same | DMRG Ne = 20 to 50 |
| Excited states 0.3 to 0.8 meV; charge noise Sq ≈ 1e-3 e/√Hz at 10 mHz | Fig. 2i; ED Fig. 5; Table III | same | 3 transitions; 15.5 h time trace; B = 5 T |
| e/3 tunneling at ν = 1/3 and 2/3 (δ 80 to 100 mV, about one third of ν = 1) | Fig. 1h, 1i, 1j; ED Fig. 3 (CLL fits with e* fixed to e/3) | same | B = 13.5 T (and 8.97, 13.4 T datasets in Fig. 1j); T 25 to 500 mK in ED Fig. 3; Te saturates near 110 mK |
| Nqp = 0 calibration via tripled field; quantum capacitance shift under one quasiparticle | Fig. 3b; ED Fig. 6 | same | 4.5 T and 13.5 T; ν = 1/3 at VT = 49 ± 1 mV, ν = 1 at 50 ± 2.5 mV |
| Single anyon dot, irregular addition energies for Nqp = 1 to 5 matching DMRG | Fig. 3d to 3g; ED Fig. 8 | same | DMRG Ne = 8 to 18, q up to 6; few-quasihole regime not reached ("We were unsuccessful in accessing the few quasihole regime in weak backscattering", p. 5) |
| Regular spectra for 1/3 QH and 2/3 QP, irregular for 1/3 QP and 2/3 QH at |Nqp| ≈ 10 to 20 | Fig. 4a to 4d; ED Figs. 9, 10, 11 | same | gate dependence over VT, Vedge, Vqpc, D; bias about 60 to 70 µV |
| Anyon binding: alternating sectors merge into 2e/3 steps as VT is lowered | Fig. 4e, 4f, 4g | same | VT in [0.040, 0.050] V, Vdot [3.785, 4.5] V, B = 13.5 T, VDC = 55 µV (Table I) |
| Bulk pair binding from segment DMRG (2/5 quasiparticles bind, 88 ± 5 µeV) | Table II | theory | Ly = 16 to 28 lB, χ up to 8192 |

Counts: devices fabricated, not stated ("M.V. fabricated the devices", p. 8, plural). Devices measured: one, implied ("The device was measured during two separate cool downs.", p. 9). Cooldowns: 2 (lock-in in the first, DC with DAC/ADC in the second). Devices that showed the effect: not stated. Datasets: Table I lists configurations for all main-text panels, and the ED figures add gate sweeps. Missing: total devices, the number of VT sweeps or windows taken for Fig. 4e and 4f, and the field ranges beyond the listed fixed values. Which cooldown each figure comes from is only implicit (Table I's "DC" vs lock-in frequency column).

## Entries matched, skipped, adapted
- Matched: charge-trap-fractional-shift (charge family; a side dot or trap could mimic fractional periodicity, irregular spacing or missing sectors), fine-tuning-and-selection (always).
- Adapted: island-states-coulomb-spacing. Its signature is even-odd Coulomb blockade spacing in a hybrid superconducting island read as Majorana modes. I matched it on the physics: even-odd spacing in a confined dot read as an exotic pairing mechanism, with ordinary confined (orbital) states as the lookalike. Its control (open the junctions and look for a zero-bias peak) does not apply. I adapted it to testing whether the pattern tracks parameters the binding picture says should not matter (gate configuration, field), from its `data_that_reveals_it`. The library has no `checks` for the island family, so no check steps go with it.
- Skipped: coulomb-dominated-interferometer. Its signature is Fabry-Perot oscillations read as Aharonov-Bohm interference. This device is a Coulomb-blockaded dot, and the paper already reads its oscillations as Coulomb blockade, so the lookalike is the paper's own framework. I still walked its check (charge-regime-map), adapted to "state the regime and map in two parameters".
- Skipped as not applicable to this device: every zbp, quantization, nonlocal, shapiro, supercurrent, chiral, kitaev and diode entry (no superconductor, no zero-bias peak, no Josephson junction). Also skipped: series-resistance-subtraction (no conductance value is claimed as quantized evidence; the paper notes suppression below e2/3h), protocol-parameter-sensitivity (no pass/fail protocol) and local-probe-loophole (Majorana-specific).
- Scope adaptation (one sentence in "What this is"): the paper is quantum Hall dot charge spectroscopy, which falls under the library's `charge` family. Only the island entry needed adapting.

## Hold-out
- No library source was skipped. All library sources predate the paper (submitted 13 Oct 2026) or are on unrelated topics (Legg comment v2 2026 on the topological gap protocol; Akrap, Frolov et al. v2 2026 on reproducibility). I judged this from titles and dates and did not open each source to search for the arXiv ID. All related-work papers I opened predate the paper, so none can discuss it.
- I did not recognize this paper (it is dated after my training data), so no later history was used.

## Related work: how each was checked
All five came from arXiv API searches (export.arxiv.org, with about 3 s between calls). For each one I opened the arXiv abstract page and confirmed the ID, title and first author, and checked the one-line description against the abstract only (no full text read).
- 2502.00124: Liang, Nakamura, Gardner (+1), 2025. Abstract confirms the Φ0/2 period at ν = 2 and 3 from capacitive coupling between isolated edge modes and the interfering edge, with e* = 1. This is also the source for the outside lookalike row.
- 1709.04504: Frigeri, Scherer, Rosenow, 2017. Abstract confirms the halved flux period from inter-edge interaction, also as a subperiod in the CD regime, and "no evidence for a connection between a reduced flux period and electron pairing".
- 1409.4427: Choi, Sivan, Rosenblatt et al., 2014. Abstract confirms the h/2e periodicity, e* ~ 2e from shot noise, and dephasing by the adjacent channel.
- 2005.12723: Röösli, Hug, Nicolí et al., 2020. Abstract confirms the two-compressible-region model of a 1.4 µm dot and e*/e = 0.32 ± 0.03 by comparison with ν = 2.
- 1201.1600: Kou, Marcus, Pfeiffer, West, 2012. Abstract confirms 2e/3 tunneling charge and one charged edge at ν = 2/3, from gate and field periods.
- Considered but not listed: 1608.05721 (Hamo et al. 2016, electron attraction in nanotubes, abstract opened); 1602.06944 (Sivan et al. 2016, area modulations, abstract opened); 2007.00551 (Frigeri and Rosenow 2020, seen in search results only).
- The matched entries' own sources (Frolov 2023, Zhang 2021, Halperin 2011, Valentini 2022, Prada 2020) are about Majorana or interferometer systems. They did not give similar-system papers here, so I searched arXiv.

## Library gaps
- Apparent pairing, or period halving, from capacitive coupling between an isolated edge or puddle and the tunneling edge (Liang et al. 2025, arXiv 2502.00124; Frigeri et al. 2017, arXiv 1709.04504). It is relevant to any "charge enters in 2e*" or "h/2e" claim in the charge family. It went in the table as "(not in library)", judged against Liang's control (independent measurement of the tunneling charge, and designs with measurable edge-edge coupling).
- Fractional charge inferred from period ratios across fields or fillings, assuming a fixed lever arm and capacitance. I had no opened paper showing it as a lookalike, so I raised it as a question only (Q7).
- There are no `checks` for the island family, and the charge-family checks assume an interferometer (charge-regime-map is phrased as AB vs CD). A "quantum dot charge spectroscopy" check set would fit papers like this one (repeat sweeps, two-gate stability diagrams, independent charge calibration).

## Unsure
- All six checks came out "partly". report-counts could arguably be "not done", since the device count is only implied. I picked "partly" because the cooldowns are reported and the single device is implicit.
- Statuses: all four lookalikes are "partly addressed". For the island entry, the paper's convexity argument (a missing sector requires EB > EC) addresses the orbital lookalike in Fig. 4f and 4g. But DMRG does not reach Nqp ≈ 10 to 20, and ED Fig. 10 says the even-odd locations "depend strongly on the gate voltages", so I chose the weaker status.
- Q7: the Fig. 1 caption formula "EC = 3e ∆VDC" looks like it may mean (e/3)∆VDC. With the Fig. 1i bias axis near ±1 mV, (e/3) × 0.9 mV ≈ 300 µeV. I asked a neutral question and did not assert a typo.
- Word count: about 960 words outside the table, a little over the 600 to 900 aim. About 100 of those are template boilerplate.

## Skill issues
- Output locations conflict: the skill says to write reports/<id>.md and reports/<id>.notes.md. This run's instructions forbid .md writes, so the report and notes are in the reply and only flags.json was written.
- Hold-out rule: it asks to skip library sources that discuss the paper, but checking that strictly means opening every library source and searching it. The skill doesn't say whether a date or topic judgment is enough.
- The charge-regime-map check is written for interferometers. The skill doesn't say how to treat a check whose physics only partly fits (this one is a dot). I adapted it and said so.
- When an entry is adapted to a family with no `checks` (island), the skill doesn't say whether to borrow checks from another family.
- Step 5 says to start related work from the matched entries' sources, which here are Majorana-focused. It doesn't say what to do when they don't fit the system.
- The word target "600 to 900 words outside the table" doesn't say whether questions and related work count. I counted them.
- The template's check line format "<check> : Done" has a space before the colon. I copied it as written.
- The flags.json status vocabulary can't carry the "data bear on it; the paper doesn't discuss it" nuance for partly addressed rows.
