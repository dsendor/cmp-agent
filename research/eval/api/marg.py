#!/usr/bin/env python3
"""MARG-S (D'Arcy et al. 2024, allenai/marg-reviewer) on Claude, for Step 3.

    python3 research/eval/api/marg.py --set marg10 [--limit 1] [--no-refine] [--budget 90]

A port of reviewgen_v26_specialized_multi_agent and MultiAgentGroup from the reference code,
with the MARG-S prompts kept verbatim in arms/marg_s.json. Per prompt set (experiments,
novelty, clarity): a leader with no paper text, one worker per paper chunk of about 4,096
tokens and one expert talk until the leader writes its comments; then each comment is refined
by a fresh leader-and-workers group. The paper reaches the agents as pdftotext text split
into paragraphs (the reference used GROBID paragraphs with section names).

Kept from the reference: the SEND MESSAGE / SEND FULL MESSAGE protocol, broadcast to every
agent, the irrelevant-reply filter, history pruning for leader, workers and experts, the
duplicate-message guard, the finalized-list check and the JSON retries, max 2,048 tokens per
turn in the reference. Changed: a turn may run to MAX_TOKENS (Opus writes longer comments than
GPT-4 did, and 2,048 tokens cut its JSON lists off); agent messages arrive as user turns (Claude has no mid-conversation system
role); calls run concurrently where the reference ran them in order; a leader stops after
MAX_TURNS turns; model settings are those of the other Step 3 arms (config.json).

--no-refine is MARG-S-NR from the same paper: the draft lists are the review (config
skip_refinement in the reference); its folder is margnr.<model>.

Output: referee/<id>/api/marg.<model>/r<k>.txt (the "all" list, numbered), r<k>.marg.json
(comments by set) and r<k>.marg.log.json.gz (every conversation). One costs.csv row per
group, at the synchronous price.
"""
import argparse
import collections
import gzip
import json
import re
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import providers  # noqa: E402
import run  # noqa: E402

M = json.loads((HERE / "arms" / "marg_s.json").read_text())
PRUNE_STRING = "This doesn't seem relevant to me, so I will stand by for further instructions."
MAX_TURNS = 60
MAX_TOKENS = 8192
GATE = threading.Semaphore(16)
LOCK = threading.Lock()


class Usage:
    def __init__(self):
        self.lock = threading.Lock()
        self.u = collections.Counter()
        self.calls = 0

    def add(self, msg):
        u = msg.usage
        with self.lock:
            self.calls += 1
            self.u.update(input=u.input_tokens, cache_write=u.cache_creation_input_tokens or 0,
                          cache_read=u.cache_read_input_tokens or 0, output=u.output_tokens)


class Bot:
    """GptChatBot: one agent's conversation. cache marks the message index that ends a stable prefix."""

    def __init__(self, client, model, settings, system, usage, max_tokens):
        self.client, self.model, self.settings = client, model, settings
        self.system, self.usage, self.max_tokens = system, usage, max_tokens
        self.messages = []
        self.cache_at = None
        self.agent_type = self.agent_name = self.paper_chunk = None
        self.extra_prompts = None

    def _payload(self):
        msgs = [dict(m) for m in self.messages]
        # Cache the chunk prefix for workers, else the last stable assistant turn.
        idx = self.cache_at if self.cache_at is not None and self.cache_at < len(msgs) - 1 else None
        if idx is None:
            idx = next((i for i in range(len(msgs) - 2, -1, -1) if msgs[i]["role"] == "assistant"), None)
        if idx is not None:
            msgs[idx]["content"] = [{"type": "text", "text": msgs[idx]["content"],
                                     "cache_control": {"type": "ephemeral"}}]
        p = {"model": self.model, "max_tokens": self.max_tokens, "system": self.system, "messages": msgs}
        if self.settings.get("effort"):
            p["output_config"] = {"effort": self.settings["effort"]}
        return p

    def chat(self, prompt):
        self.messages.append({"role": "user", "content": prompt})
        with GATE:
            msg = self.client.messages.create(**self._payload())
        self.usage.add(msg)
        text = "".join(b.text for b in msg.content if b.type == "text")
        self.messages.append({"role": "assistant", "content": text or "(no response)"})
        return text


def counter_jaccard(a, b):
    keys = set(a) | set(b)
    den = sum(max(a[k], b[k]) for k in keys)
    return sum(min(a[k], b[k]) for k in keys) / den if den else 0.0


def prune_history(messages, replace_content):
    """MultiAgentGroup.prune_history with skip_n 0: agent replies already answered become a placeholder."""
    pruned = []
    for i, msg in enumerate(messages):
        c = msg["content"]
        if msg["role"] == "assistant" and (c.startswith("SEND MESSAGE:") or c.startswith("SEND FULL MESSAGE:")) and i > 0:
            prev = next(((j, m) for j, m in reversed(list(enumerate(pruned)))
                         if m["role"] == "assistant" and j >= len(pruned) - 2), None)
            if prev and "SEND MESSAGE" in prev[1]["content"]:
                pc = prev[1]["content"]
                head = pc[: pc.index("SEND MESSAGE")]
                if counter_jaccard(collections.Counter(head.split()), collections.Counter(c.split())) > 0.9:
                    new = dict(prev[1])
                    new["content"] = head[pc.index("SEND MESSAGE"):] + "\n\n" + c[c.index(":") + 1:]
                    del pruned[prev[0]:]
                    pruned.append(new)
                    continue
        if msg["role"] == "user" and c.startswith("Message from Agent"):
            pruned.append({"role": "user", "content": replace_content})
        else:
            pruned.append(msg)
    return pruned


class Group:
    """MultiAgentGroup with master_chunk_type none: Agent 0 leads, workers hold chunks, experts last."""

    def __init__(self, client, model, settings, prompts, chunks, experts, usage, pool):
        self.pool = pool
        mk = lambda system: Bot(client, model, settings, system, usage, MAX_TOKENS)
        self.bots = []
        lead = mk(prompts["master_system_prompt"])
        lead.agent_type, lead.paper_chunk = "leader", ""
        self.bots.append(lead)
        for chunk in chunks:
            b = mk(prompts["worker_system_prompt"])
            b.agent_type, b.paper_chunk = "worker", chunk
            self.bots.append(b)
        self.experts = []
        for e in experts:
            b = mk(e["system_prompt"])
            b.agent_type, b.paper_chunk, b.extra_prompts = "extra", "", e
            self.bots.append(b)
            self.experts.append(b)
        for i, b in enumerate(self.bots):
            b.agent_name = f"Agent {i}"

        def ready(b):
            others = ", ".join(x.agent_name for x in self.bots if x is not b)
            tmpl = {"leader": prompts["master_chunk_prompt"], "worker": prompts["worker_chunk_prompt"],
                    "extra": (b.extra_prompts or {}).get("chunk_prompt")}[b.agent_type]
            b.chat(tmpl.format(source_paper_chunk=b.paper_chunk, num_agents=len(self.bots),
                               agent_name=b.agent_name, other_agent_names=others, taxonomy=""))
            if b.agent_type == "worker":
                b.cache_at = 1
        list(self.pool.map(ready, self.bots))
        self.turns = 0
        self.capped = False

    def _relay(self, b, msgline):
        if b.agent_type == "worker":
            msgs = b.messages
            b.messages = msgs[:4]
            if len(msgs) >= 6:
                b.messages[2:4] = msgs[4:6]
        elif b.agent_type == "extra":
            keep = []
            for i, m in enumerate(b.messages):
                nxt = b.messages[i + 1] if i < len(b.messages) - 1 else None
                if (m["role"] == "assistant" and m["content"].strip() == PRUNE_STRING) or (
                        nxt and nxt["role"] == "assistant" and nxt["content"].strip() == PRUNE_STRING):
                    continue
                keep.append(m)
            b.messages = keep
        return b.chat(f"Message from Agent 0: {msgline}")

    def ask(self, question):
        """ask_swarm_question: the leader talks until it writes a reply with no message to send."""
        lead = self.bots[0]
        rt = lead.chat(question)
        old = {rt}
        while True:
            if "SEND FULL MESSAGE" in rt:
                msgline = rt.replace("SEND FULL MESSAGE", "")
            else:
                i = rt.find("SEND MESSAGE")
                if i == -1 or (i > 0 and rt[i - 1] not in ("\n", " ")):
                    break
                msgline = rt[i + len("SEND MESSAGE: "):]
            self.turns += 1
            if self.turns > MAX_TURNS:
                self.capped = True
                break
            replies = list(self.pool.map(lambda b: (b, self._relay(b, msgline)), self.bots[1:]))
            parts = [f"Message from {b.agent_name}: {r.replace('SEND MESSAGE: ', '')}"
                     for b, r in replies if r.strip() != PRUNE_STRING]
            rtmsg = "\n\n".join(parts)
            if rtmsg.strip() == "":
                rtmsg = ("No messages were received from any agent; you may need to reword and double-check your "
                         "message so that the agents know who your message is intended for.")
            rtmsg += "\n\nSystem note: remember that if you need to send a message back, you need to prepend SEND MESSAGE"
            rt = lead.chat(rtmsg)
            while rt in old:
                rt2 = lead.chat("Error: you tried to send exactly the same message as before.  You have already "
                                "received a response to that message from all agents.  Note: If the conversation "
                                "is over, you should stop sending messages.")
                if rt2 == rt:
                    return rt2
                rt = rt2
            lead.messages = prune_history(
                lead.messages, "[ The agents responded to you, but their messages have been pruned from the history. "
                               "Your response below was created based on their real messages. ]")
            old.add(rt)
        return rt

    def log(self):
        return [{"agent": b.agent_name, "type": b.agent_type, "messages": b.messages} for b in self.bots]


def json_list(text):
    """The reference's rt[rt.index("["):].strip().strip("`"), parsed, with LaTeX backslashes repaired."""
    if "[" not in text:
        return None
    t = text[text.index("["):].strip().strip("`").strip()
    t = t[: t.rfind("]") + 1]
    for s in (t, re.sub(r'\\(?!["\\/bfnrtu])', r"\\\\", t)):
        try:
            v = json.loads(s)
            return v if isinstance(v, list) else None
        except ValueError:
            continue
    return None


def paper_chunks(pid, size):
    """make_chunked_paper_diff in source mode, on pdftotext paragraphs; tokens estimated as chars / 4."""
    paras = [re.sub(r"\s*\n\s*", " ", p).strip() for p in re.split(r"\n\s*\n", run.v1_text(pid))]
    paras = [p for p in paras if p]
    blocks = [f"section: unknown\nparagraph id: {i}\n{p}" for i, p in enumerate(paras)]
    chunks, cur, n = [], [], 0
    for b in blocks:
        t = len(b) / 4 + 2
        if cur and n + t > size:
            chunks.append("\n\n".join(cur))
            cur, n = [], 0
        cur.append(b)
        n += t
    if cur:
        chunks.append("\n\n".join(cur))
    return chunks


def review(pid, model_name, k, pool, client, refine_on=True):
    mc = run.CFG["models"][model_name]
    chunks = paper_chunks(pid, M["paper_chunk_size"])
    logs, by_set, rows = [], {}, []
    d = run.REF / pid / "api" / f"{'marg' if refine_on else 'margnr'}.{model_name}"
    d.mkdir(parents=True, exist_ok=True)

    def log_group(label, g, usage):
        rid = f"marg|{pid}|{model_name}|{k}|{label}"
        res = {"usage": dict(usage.u), "stop": f"calls={usage.calls}" + (" capped" if g.capped else ""), "error": None}
        with LOCK:
            rows.append((rid, res))
            logs.append({"group": label, "turns": g.turns, "capped": g.capped, "agents": g.log()})
            run.log_cost(rid, res, model_name, "", True)

    # Drafts are kept as they finish, so a failed refinement does not repeat them.
    saved = d / f"r{k}.drafts.json"
    other = run.REF / pid / "api" / f"{'margnr' if refine_on else 'marg'}.{model_name}" / saved.name
    drafts = json.loads(saved.read_text()) if saved.exists() else json.loads(other.read_text()) if other.exists() else {}

    def draft(p, pset):
        experts = pset.get("experts", [])
        usage = Usage()
        g = Group(client, mc["id"], mc.get("settings", {}), p, chunks, experts, usage, pool)
        names = {e["name"]: g.experts[i].agent_name for i, e in enumerate(experts)}
        rt = g.ask(p["task_prompt_set1_v1"].format(comment_type="", **names))
        check = Bot(client, mc["id"], mc.get("settings", {}), M["final_list_check_prompt"], usage, MAX_TOKENS)
        rt2 = check.chat("Output:\n" + rt)
        if rt2.strip().strip('"') == "No comments.":
            rt = g.ask(p["task_prompt_set1_v2"])
            if json_list(rt) is None:
                rt = g.ask(p["task_prompt_set1_v2"] + "\n\nMake sure to use the specified JSON format.")
        else:
            rt = rt2
        log_group(f"{pset['name']}|draft", g, usage)
        return json_list(rt) or []

    def refine(p, pset, i, c):
        u = Usage()
        g2 = Group(client, mc["id"], mc.get("settings", {}), p, chunks, [], u, pool)
        g2.ask(p["task_prompt_set2_v1"].format(comment_type="", review_comments=c))
        out = g2.ask(p["task_prompt_set2_v2"])
        log_group(f"{pset['name']}|refine{i}", g2, u)
        try:
            obj = run.parse_json(out)
        except Exception:
            return []
        if not isinstance(obj, dict):
            return []
        if "revised_comments" in obj:
            return [x for x in obj["revised_comments"] if x]
        return [obj["revised_comment"]] if obj.get("revised_comment") else []

    def one_set(pset):
        p = dict(M["default_prompts"])
        p.update(pset)
        comments = drafts.get(pset["name"]) or draft(p, pset)
        with LOCK:
            drafts[pset["name"]] = comments
            saved.write_text(json.dumps(drafts, indent=1))
        if not refine_on:
            by_set[pset["name"]] = {"draft": comments, "final": comments}
            return
        with ThreadPoolExecutor(8) as ex:
            refined = [x for r in ex.map(lambda ic: refine(p, pset, *ic), enumerate(comments)) for x in r]
        by_set[pset["name"]] = {"draft": comments, "final": refined}

    with ThreadPoolExecutor(3) as ex:
        list(ex.map(one_set, M["prompt_sets"]))
    allc = [c for s in M["prompt_sets"] for c in by_set[s["name"]]["final"]]
    (d / f"r{k}.marg.json").write_text(json.dumps({"chunks": len(chunks), "by_set": by_set, "all": allc}, indent=1))
    with gzip.open(d / f"r{k}.marg.log.json.gz", "wt") as f:
        json.dump(logs, f)
    (d / f"r{k}.txt").write_text("\n\n".join(f"{i}. {c}" for i, c in enumerate(allc, 1)) + "\n")
    price = run.CFG["models"][model_name]["batch_price"]
    cost = sum(res["usage"].get(x, 0) * price[x] for _, res in rows for x in price) / 1e6 * 2
    print(f"{pid}: {len(chunks)} chunks, {len(allc)} comments, {len(rows)} groups, ${cost:.2f}", flush=True)
    return cost


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--set", required=True)
    ap.add_argument("--model", default="opus")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--papers", type=int, default=4, help="papers in parallel")
    ap.add_argument("--no-refine", action="store_true")
    ap.add_argument("--budget", type=float, default=90, help="start no new paper once this run has spent this much")
    a = ap.parse_args()
    arm = f"{'margnr' if a.no_refine else 'marg'}.{a.model}"
    pids = [p for p in run.paper_set(a.set) if not (run.REF / p / "api" / arm / "r1.txt").exists()]
    pids = pids[: a.limit] if a.limit else pids
    import anthropic
    client = anthropic.Anthropic(api_key=providers._key("CMP_EVAL_ANTHROPIC_KEY"),
                                 base_url="https://api.anthropic.com", max_retries=8)
    pool = ThreadPoolExecutor(64)
    spent = []

    def one(pid):
        if sum(spent) >= a.budget:
            print(f"{pid}: skipped, budget ${a.budget:.0f} reached", flush=True)
            return
        try:
            spent.append(review(pid, a.model, 1, pool, client, refine_on=not a.no_refine))
        except Exception as e:  # keep the other papers going; the drafts already saved are kept
            print(f"{pid}: failed: {e}", flush=True)

    with ThreadPoolExecutor(a.papers) as ex:
        list(ex.map(one, pids))
    print(f"total ${sum(spent):.2f} for {len(spent)} papers")


if __name__ == "__main__":
    main()
