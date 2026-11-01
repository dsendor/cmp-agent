# Prior work: what to reuse

*AI only. Checked 2026-10-23. Repos were checked by cloning (last commit, license file);
packages by PyPI; papers by their arXiv abstract pages. Nothing here is human-checked.*

## Tools

| Tool | What it does | Fits? | Would replace | Setup | License | Other models | Status |
|---|---|---|---|---|---|---|---|
| [PaperQA2](https://github.com/Future-House/paper-qa) | Question answering with citations over a local folder of PDFs; metadata from Semantic Scholar and Crossref | Later. Useful once the library has a curated corpus to check "does paper X say Y" | Nothing now; later the claim check in step 5 | Medium: Python 3.11, an embedding model, API keys | Apache-2.0 | Yes (LiteLLM, local embeddings possible) | Real, active (last commit 2026-08-12, PyPI 2026.8.12) |
| [Ai2 ScholarQA](https://github.com/allenai/ai2-scholarqa-lib) | Literature review over Semantic Scholar's index (11M full texts), quote extraction, sectioned report | No. Heavy for a one-page report, and Semantic Scholar is blocked from this sandbox | Step 5 search | High: Semantic Scholar key, reranker model, Docker or Python | Apache-2.0 | Yes (LiteLLM) | Real, active (2026-10-13). Hosted version at scholarqa.allen.ai usable by hand |
| arXiv API | Search, metadata, PDFs | Yes, already used | Nothing | None | Free (arXiv terms) | Any | Works. Rate-limits bursts ("Rate exceeded" in two runs); needs a pause between calls |
| Semantic Scholar API | Search, citations, snippet search | Optional | Cited-by lookups | Free key | Free (S2 terms) | Any | Blocked from this sandbox (no response); works elsewhere |
| OpenAlex API | Works, DOIs, citations, no key | Yes, for link checks and DOI to arXiv mapping | Hand link checks in step 5 | None (plain HTTPS) | CC0 data | Any | Works from here |
| [Black Spatula](https://github.com/The-Black-Spatula-Project/black-spatula-project) | A GitHub-issue bot that sends a PDF and a prompt to OpenAI | No. The code is a stub; the lessons live in shared sheets | Nothing | Low | MIT | OpenAI only in code | Stale (last commit 2024-12-23). Drop |
| [OpenReviewer](https://github.com/maxidl/openreviewer) | Llama 3.1 8B fine-tuned on 79,000 ICLR and NeurIPS reviews | No. Generic machine learning reviews | Nothing | High (GPU) | No license file in repo | Own weights | Last commit 2025-06-21. Drop |
| [SPOT](https://arxiv.org/abs/2505.11855) | Benchmark: 83 papers, 91 errors that led to errata or retraction; best model 21.1% recall, 6.1% precision | Yes, for scoring | Our ad hoc hit/miss | None | Paper | Any | Borrow the scoring (precision, recall, pass@K over repeated runs) |
| [Topological gap protocol](https://arxiv.org/abs/2207.02472) and [critique](https://arxiv.org/abs/2502.19560) | A staged pass/fail test for zero-bias-peak devices, and a comment showing its outcome flips with data choices | Partly; see below | Nothing | None | Papers (TGP code public) | n/a | Both added to the library |
| [QCoDeS](https://github.com/microsoft/Qcodes) | Lab data acquisition and storage | Later phases only | n/a | n/a | MIT | n/a | Active (PyPI 0.61.1, 2026-10-20). No work now |
| [OpenAIReview](https://github.com/ChicagoHAI/OpenAIReview) (not on the list) | Reviews a paper passage by passage, each comment anchored to a quoted passage; ships a Claude Code skill | Yes, as the baseline to beat | Nothing; it's the comparison | Low (pip) | MIT | Yes (OpenRouter, OpenAI, Anthropic, Gemini, Mistral, local) | Active (2026-10-14) |
| [Dawes planted-error benchmark](https://github.com/Dawes-Institute/ai-peer-review-benchmark) (not on the list) | 100 errors planted in 10 papers, scored by fuzzy match plus a model judge | Yes, as the eval method | Part of eval.md | Low | MIT | Yes | Active (2026-08-09) |

Also found and judged low value for this task: coarse, PaperAudit, Rigorous, MARG, the AI
Scientist reviewer, DeepReviewer, AgentReview, ResearchTown, SEA, PaperBench, and the closed
tools (Refine, paperreview.ai, Reviewer3, YesNoError, scite, Elicit, Consensus, alphaXiv).
None checks a claim against a field's catalog of trivial explanations.

Evaluations worth knowing: [ReviewerGPT](https://arxiv.org/abs/2306.00622) (a pointed
question beats "write a review"), [Benchmarking Agentic Review Systems](https://arxiv.org/abs/2606.19749)
(the union of six models catches more injected errors than any one; users' main complaint is
false positives), [Hidden pitfalls of AI scientist systems](https://arxiv.org/abs/2509.08713)
(post-hoc selection bias is caught far better with logs and code than from the paper alone),
[WithdrarXiv](https://arxiv.org/abs/2412.03775) (14,000+ withdrawn arXiv papers with reasons,
a source of test cases).

## The topological gap protocol and our library

**The protocol** (Microsoft Quantum, Phys. Rev. B 107, 245423) is a decision procedure for
one family of signatures, zero-bias peaks in three-terminal nanowire devices. Stage 1 looks
for zero-bias peaks at both ends that stay put as the junction transparencies change. Stage 2
measures the nonlocal conductance to find a bulk gap and keeps only regions that are gapped
inside and gapless at the edge and that overlap across junction settings. Simulations set the
thresholds and give a false discovery rate (8% or less). The output is pass or fail.

**The critique** (Legg, arXiv 2502.19560, v2 October 2026) uses the released code and data:
the gap threshold in the code differs from the paper's definition; the outcome flips when the
field range, bias range, resolution or chosen cutter pairs change, and those vary without
explanation across devices; simulations and experiments ran different versions of the code;
and the definition of "topological" was weakened.

**Compared with our library.** The library is organized by lookalike: for each ordinary
effect, the check that tells it apart. The protocol is organized by signature: an ordered set
of checks, each of which excludes several lookalikes at once (both ends excludes `one-end-only`;
the nonlocal gap targets `quasi-majorana-smooth-confinement` and `disorder-induced-zbp`). The
critique shows the weak point of turning those checks into a binary verdict with thresholds:
the verdict inherits every data choice.

**Recommendation: borrow the checklist, not the verdict.** Add a short `checks` list per
family, each check naming the lookalikes it addresses. The report can then say "you did
checks 1 and 2; check 3 would address these three lookalikes," which reads better and
removes repeated controls across entries. Keep the status per lookalike and the questions;
no pass/fail, no thresholds. The critique's lesson is already an entry
(`protocol-parameter-sensitivity`), and its questions (which ranges, which resolution, which
settings were left out) go into step 6.
