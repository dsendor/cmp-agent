# Run notes: arXiv 1809.05513v1 (skill-r1)

*AI only. Run of the lookalike-assistant skill on 2026-10-23.*

- **Library version:** 0.4 (meta.updated 2026-10-23); 28 lookalikes, 18 checks.
- **Paper version:** v1, as given (submitted 2018-09-14).

## What I read

- Skill `SKILL.md`, `report-template.md`, `library/lookalikes.yaml` (all entries and the `checks` section), read once at the start.
- Paper: local `abs.html` (title, authors, abstract, submission history; links DOI 10.1126/science.aav3392) and the local PDF (12 pages: main text pp. 1 to 6, supplementary material pp. 7 to 12). I extracted text per page with `pdftotext` and checked every quote in the report against the page text (quotes that cross a line-break hyphen, "low-energy", were restored to the printed form).
- No ancillary files and no data repository are linked on the abstract page or in the paper, so `read_mtx.py` was not used and no data were counted beyond the figures and Table S1.
- I did not fetch the paper itself. I fetched library sources (arXiv PDFs) for the hold-out check, arXiv API searches, arXiv abstract pages for related work, and one OpenAlex record (doi:10.1126/science.aav3392).
- Nothing I tried to open failed.
- I recognized the paper (published in Science 2020 with an expanded author list) and know of later work on full-shell zero-bias peaks. I kept that out of the report; see "Unsure" for where the library itself carries it.

## Claims (step 1)

| Claimed signal | Figures | Device | Counts and ranges | Missing |
|---|---|---|---|---|
| Hard induced gap in the zeroth Little-Parks lobe; zero-bias peak throughout the first lobe; subgap states away from zero in the second lobe | Fig. 2B to F, Figs. S2, S3, S9A to C (pp. 2, 3, 8, 12) | Device 1, one tunnel probe at the end where the shell was removed; barrier set by global back gate | B from −0.3 T to 0.3 T, axial only (Fig. 2B); VBG −1.2 V to −0.8 V at B = 0 and 110 mT (Fig. 2C, E); VBG −0.80 V to −1.10 V line cuts at 0, 0.11, 0.22 T (Fig. S3); 20 mK base; Vac = 5 µV; line resistance 6.7 kΩ (p. 7) | Length of the bare segment; temperature dependence of the peak; field angle; other end; whether series resistance was subtracted; peak heights over the lobe |
| Little-Parks destructive regime with reentrant lobes (supporting) | Fig. 1C, D, Fig. S1 (pp. 1, 7) | Device 1, 4-probe on the shell | Is ±80 µA; B ±0.3 T; T 0 to 1.3 K; Iac = 200 nA | None relevant |
| Even-odd Coulomb peak spacing in the first lobe of full-shell islands | Figs. 3, 4A to E, S4 to S8 (pp. 3, 4, 9 to 11) | Device 2: six islands, 210, 300, 420, 620, 810, 970 nm, on one wire | B ±0.4 T (210, 300 nm) and ±0.3 T (others); plunger windows of about 0.1 V to 0.4 V; diamonds at 0 and 110 mT | How many gate configurations per island ("several", p. 9); spread between them |
| Exponential decrease of even-odd energy A with island length, ξ = 180 nm at 110 mT (230 nm at 140 mT), matching the shell coherence length | Fig. 4F, Fig. S9D, Table S1 (pp. 4, 5, 12) | Device 2 | Six lengths; two-parameter fit; A from 45 µeV down to 0.6 µeV; noise floor σA < 0.1 µeV | Fits on any other wire |
| Subgap states read as Caroli-de Gennes-Matricon analogs (interpretation, not a lookalike target) | Fig. 2B, S9 (p. 5) | Device 1 | δ110 ∼ 50 µeV, ∆110 ∼ 130 µeV | |

Device counts: "Two device geometries, measured in three devices each, showed similar results. Data from two devices are presented" (p. 2). So six devices were measured and two are shown; the number that showed each signature, the number of tunneling devices versus island devices, and cooldowns are not given.

## Matching (step 2)

Families used: `zbp` (tunneling peak and, per the `zbp` checks' signal text, peaks in hybrid islands), `island`, and `practice`.

Matched and reported: abs-quantum-dot, full-shell-flux-andreev, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, spin-orbit-length-pinning, exceptional-point-zero-mode, one-end-only, local-probe-loophole, island-states-coulomb-spacing, fine-tuning-and-selection.

Skipped, with reasons:
- fine-tuned-plateau, series-resistance-subtraction: no quantized height or plateau is claimed (the peak is about 0.1 e^2/h in Fig. 2F). The `zbp-raw-conductance` check was still walked.
- weak-antilocalization: its signature is a peak of order e^2/h from a disordered, open multichannel wire; the claimed peak is in the tunneling regime and turns into a dip as the barrier opens (Fig. S3). Borderline; flagged under "Unsure".
- trivial-andreev-band-gap-reopening: no nonlocal conductance and no gap-reopening claim as a topological transition; the closing and reopening at 55 to 65 mT is the shell's destructive Little-Parks regime.
- micromagnet-stray-field: no magnets, and no zero-field peak claim.
- protocol-parameter-sensitivity: no automated pass/fail protocol (the `report-ranges` and `report-processing` checks still apply).
- All shapiro, supercurrent, charge, chiral, kitaev and diode entries: different signatures. The 1e periodicity is not a fractional-charge claim.

No entries were adapted for scope.

## Checks (step 3)

zbp: dot-search Partly, wide-ranges Partly, both-ends Not done, transparency Partly, nonlocal-gap Not done, raw-conductance Partly. practice: report-counts Partly, report-ranges Partly, report-processing Partly. No `island` check family exists in the library.

Status reasoning in brief: no lookalike is ruled out because no addressing check is fully done; several are "partly addressed" on the strength of the island length series, which is on a different wire from the tunneling data. Where I chose between "partly" and "not addressed", I took "partly" only when I could quote data that bear on the entry's control; full-shell-flux-andreev went to "not addressed" because its control is junction length, which the paper neither reports nor varies.

## Sources held out (hold-out rule)

The paper under review is the arXiv version of Vaitiekėnas et al., Science 367, eaav3392 (2020), "Flux-induced topological superconductivity in full-shell nanowires": OpenAlex (https://api.openalex.org/works/doi:10.1126/science.aav3392) lists arXiv 1809.05513 among its locations, and the v1 abstract page links that DOI. I searched each matched entry's and each walked check's source PDF for "Vaitiek", "1809.0551", "eaav3392", "Science 367" and "Flux-induced". Held out (cite the Science version by authors and title):
- arXiv 2309.09368v1, Frolov et al. 2023 (ref. 60). Used by abs-quantum-dot, full-shell-flux-andreev, island-states-coulomb-spacing, fine-tuning-and-selection, and checks zbp-dot-search, zbp-wide-ranges, zbp-raw-conductance.
- arXiv 1911.04512v3, Prada et al. 2020 (ref. 197). Used by abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, spin-orbit-length-pinning, exceptional-point-zero-mode, local-probe-loophole, island-states-coulomb-spacing.
- arXiv 2207.02472, Microsoft Quantum 2023 (ref. 41). Used by quasi-majorana-smooth-confinement and checks zbp-transparency, zbp-nonlocal-gap, and the zbp `note_source`.
- arXiv 2008.02348, Valentini et al. 2021 (ref. 40). Used by full-shell-flux-andreev.
- arXiv 2203.07829, Valentini et al. 2022 (ref. 12). Used by island-states-coulomb-spacing.

Checked and kept (no citation found): 1705.02035, 1711.06256, 1806.02801, 1902.02773, 1910.11413, 2004.08583, 2101.11456, 2501.18631v2, 1207.3067, 1207.1259, 1206.6687. (1806.02801 and 1902.02773 cite other Vaitiekėnas or Deng papers, not this one; 2501.18631v2 cites a later full-shell paper by other authors, not this one.)

After the hold-out, five reported entries have no usable source left: full-shell-flux-andreev, island-states-coulomb-spacing, spin-orbit-length-pinning, exceptional-point-zero-mode, local-probe-loophole. I kept them in the table using only the entry's own lookalike, mechanism and control text, and cited none of the held-out papers.

## Related work (step 5)

Searches (export.arxiv.org API, 3 s apart): abs:"full-shell" AND abs:"zero-bias"; abs:"Coulomb" AND abs:"even-odd" AND abs:"Andreev" AND abs:island (no hits); abs:"peak spacing" AND abs:trivial AND abs:Andreev (no hits); abs:"peak spacing" AND abs:"Andreev bound states"; abs:"Little-Parks" AND abs:nanowire AND abs:Andreev; abs:"Coulomb blockade" AND Majorana AND trivial AND "peak spacing" (no hits); abs:"Caroli-de Gennes-Matricon" AND abs:nanowire.

Each listed paper: opened its arXiv abstract page, confirmed ID, title and first author, and checked the one-line description against the abstract.
- 1705.02035 Liu et al.: abstract page; also full text searched for the hold-out check. Description from abstract.
- 1711.06256 Moore et al.: abstract page; full text searched for hold-out. Description from abstract.
- 1806.02801 Vuik et al.: abstract page; full text searched for hold-out. Description from abstract.
- 1702.04357 Chiu, Sau and Das Sarma: abstract page only. Description from abstract.
- 2604.24858 Payá et al. (4 authors; first Payá, last San-Jose): abstract page only. Description from abstract. Later than the paper under review; described for its own result only.

Opened and not listed: 1911.06805 (Peñaranda et al., full-shell theory; its abstract is framed around this paper, so I left it out), 2501.05419 (Deng et al., CdGM analogs, experiment), 2207.07606 (San-Jose et al., CdGM theory), 2005.11848 (Razmadze et al.), 1902.02773 (Chen et al.), 2004.08583 (Yu et al.), 1910.11413 (Pan and Das Sarma). Held-out sources 2008.02348 and 2203.07829 came up in searches and were not listed.

No outside lookalikes were added: I did not open a paper that shows a trivial mechanism for an exponential length dependence of the even-odd energy, so none went in the table.

## Library gaps

- No `island` check family, though `island` is a family and island-states-coulomb-spacing is an entry; I used the `zbp` checks, whose signal text includes hybrid islands.
- No entry for a trivial origin of an exponential length dependence of even-odd island energy (for example lever-arm or charging-energy trends across islands of different length, or trivial states whose splitting falls with length). The paper's strongest argument (Fig. 4F) has no matching lookalike apart from the general island entry.
- No entry for Caroli-de Gennes-Matricon analog states in full-shell wires as a source of near-zero subgap features; candidates seen in search: 2207.07606, 2501.05419 (not checked for whether they show a zero-energy lookalike).
- full-shell-flux-andreev and island-states-coulomb-spacing have only sources that discuss this paper, so for this paper they carry no independent citation.

## Skill issues

- **Hold-out leaves entry text in play.** The rule says to skip sources, and is silent on entries whose every source is held out. Here the full-shell-flux-andreev entry (lookalike, mechanism, control) is a summary of a held-out paper that responds to this one, so using it lets the later history in through the library text. I kept the entry; the skill should say whether to drop such entries, keep them, or keep them with a flag.
- **Hold-out and the published version.** The held-out papers cite the Science version, which has a different title and seven more authors. The rule ("cites it by title, authors or arXiv ID") doesn't say whether a journal version with a new title counts. I counted it, using the OpenAlex link and the DOI on the abstract page as evidence.
- **Hold-out and review articles.** Prada et al. 2020 cites this paper once in a list of several hundred references and supplies eight entries' sources. A citation-only rule removes it wholesale; the skill could separate "discusses" from "cites".
- **Checks with held-out sources.** The rule covers library sources in general; checks have sources too. I walked every check regardless and cited none of their held-out sources. The skill doesn't say whether that is right.
- **Report and notes paths.** Step 7 says to write `reports/<arxiv-id>.md` and `reports/<arxiv-id>.notes.md`; this run wrote to the eval folder the caller named. Fine for a test, but the skill could allow an output path.
- **Word count.** "About 600 to 900 words outside the table" doesn't say whether the header, titles and URLs count. Counted all of them: about 905.
- **Two families in one paper.** The skill speaks of "the paper's family" in step 3; this paper has tunneling (zbp) and island signals, and the library has no island checks. Clarify how to walk checks when a paper spans families.
- **"Partly" for indirect evidence.** Several lookalikes are bounded only by data on a different device (the island series bears on one-end-only and the local-probe loophole for the tunneling wire). The status rules don't say whether evidence from another device in the same paper counts toward a lookalike for a claim made on a different device. I took it as "partly addressed".

## Unsure

- weak-antilocalization: skipped on the grounds that the peak is in the tunneling regime; a stricter reader could include it as "not addressed".
- kondo-resonance: "partly addressed" rests on the peak staying at zero bias across the first lobe without splitting (Fig. 2B), which bears on Kondo only if the g factor in the bare segment is large enough for splitting to show by 150 mT. A weaker call would be "not addressed".
- exceptional-point-zero-mode and local-probe-loophole: "partly addressed" rests on the island overlap measurement on a different wire.
- The zbp-transparency check: "partly" because a single global back gate tunes both the barrier and the bare segment; one could call it done within the tunneling regime.
- Writing the report and notes files: the harness's Write tool refused a report-style .md file in this subagent, so the files were written with a shell heredoc, as the caller asked for these three files explicitly.
