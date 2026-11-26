# Project advisor

Choose between your own research ideas, as a Claude Code plugin. Version 0.1, early: built
to try with a few researchers and to measure against a plain prompt before trusting it.

```text
/plugin marketplace add dsendor/cmp-agent
/plugin install project-advisor@cmp-agent
```

Then say "help me choose between my project ideas", or run `/project-advisor:choose`.
Needs Python 3, nothing else.

## What happens

1. **You dictate your ideas**, rough is fine, plus your stage, your time horizon and your
   setup. It restates each in two lines and asks only the questions that matter
   (what's new, what's the first check it's working, how long).
2. **It lists each idea's assumptions**, about nature ("the signal is above the noise") and
   about capability ("we can make the device"). You give each a risk from 1 to 5 and the
   months until you'd know.
3. **Meanwhile it searches arXiv** for the closest prior work to each idea, comparing
   question, system and method separately, and counts papers per year on the idea's core
   terms (how crowded, how fast growing).
4. **You give four ranges per idea**: odds of success, impact if it works, what you'd still
   have if it fails, and months.
5. **A dashboard opens**: odds against impact for every idea, the trade-off frontier, a
   sortable table, and for each idea its assumptions, closest papers, cheapest test and
   fallback. At the top: which idea your own estimates favour, whether that holds if any
   estimate moves 20%, and **the one uncertainty that would most change your choice**, with
   the cheapest test that resolves it.

## What it promises

- **The ranking is yours.** Every number that ranks anything is your estimate; the ranking
  is arithmetic on those (`skills/choose/scripts/decide.py`), not the model's opinion. If you
  ask it to guess an estimate, the dashboard marks that guess. This is deliberate: in a
  large study, ideas that judges rated highly before execution did worse once executed
  ([Si et al. 2025](https://arxiv.org/abs/2506.20803)).
- **It never says an idea is novel.** It shows the closest papers it found and how they
  differ. "Someone did this, here's the paper" can be checked; "nobody did this" can't.
- **AI-drafted, and labeled.** Assumptions, searches, cheapest tests and questions for your
  PI are drafted by Claude and marked so.
- **Time-boxed.** One pass, ending in the dashboard. It should take under an hour of your
  time for up to ten ideas.

## Your data

Everything is written to `project-choice/<date>/` in your project: `advisor.json` (your ideas
and estimates), `decision.json`, `prior-work/` and `dashboard.html`. Your ideas are sent to
the model, as in any Claude Code session; the arXiv searches send only search terms. Nothing
else leaves your machine.

## How the numbers work

- Value of an idea = odds × impact + (1 − odds) × value if it fails, on your 0 to 10 scale.
  If time is your binding constraint, it can be per year of work instead.
- Each estimate is a range; the script draws 20,000 times from each (triangular: low, best
  guess, high) and reports the expected value and how often each idea comes out on top.
- **Robustness:** each estimate of each idea is moved 20% up and down; if any move changes
  the top idea, the dashboard says which.
- **Value of information:** for each estimate, the script asks how often learning its true
  value would change your pick, and how much that is worth on average (expected value of
  partial perfect information). The highest is the uncertainty to resolve first. This is
  the real-options idea from business: buy information before committing.
- **Red flags** from the assumptions (Fischbach and Walsh 2024): a high-risk assumption that
  reads out after 18 months, more than two high-risk assumptions, work past your horizon.

## Is it any good?

Not measured yet. The plan, before anyone relies on it: researchers run it and a plain
"help me choose between these ideas" prompt on their own real ideas, blind to which is which,
and say which sharpened their thinking, which prior-work hits were real and new to them, and
how long each took. Then, three to six months later: what did they pick, and did the
cheapest test happen? The referee-preview plugin's lookalike library lost to a plain prompt
(`research/README.md`), so the baseline is a real bar. The protocol, forms and the script that makes the blind pages
are in [`eval/`](eval/).

## Tests

```bash
python3 project-advisor/tests/run_tests.py            # offline, on a made-up example
python3 project-advisor/tests/run_tests.py --network  # plus a live arXiv search
```

## Credits

The assumption analysis is adapted from Anthropic's
[`scientific-problem-selection`](https://github.com/anthropics/knowledge-work-plugins/tree/main/bio-research/skills/scientific-problem-selection)
skill (Apache-2.0), which follows Fischbach and Walsh, "Problem choice and decision trees in
science and engineering", Cell 2024. The two-axis view is from Alon, "How to choose a good
scientific problem", Mol Cell 2009. The intake is the Heilmeier Catechism. The prior-work
loop is modelled on [AI-Researcher](https://github.com/NoviScl/AI-Researcher) (MIT) and the
facet comparison of the [Idea Novelty Checker](https://aclanthology.org/2025.sdp-1.9)
(method only). See `NOTICE` at the repository root.
