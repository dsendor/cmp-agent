"""One interface over the Claude, Gemini and OpenAI APIs for the eval scripts.

A request is {"id": str, "parts": [...], "max_tokens": int}, where each part is
{"pdf": path}, {"text": str} or {"text": str, "cache": True}. A part marked cache ends the
prefix shared by many requests (the paper, the library); Claude caches it explicitly, the
others cache prefixes on their own. Batch providers also answer progress(batch_id) -> {"state", "done", "total"} (done counts
finished requests of any outcome; None where the API does not say) and cancel(batch_id).
Every provider returns, per request id,
{"text": str, "usage": {"input", "cache_write", "cache_read", "output"}, "error": str | None}.

Keys come from the environment, read here and nowhere else:
  Claude  CMP_EVAL_ANTHROPIC_KEY (kept apart from ANTHROPIC_API_KEY, which would switch
          interactive Claude Code to API billing)
  Gemini  GEMINI_API_KEY
  OpenAI  OPENAI_API_KEY
A provider whose key is unset falls back to a placeholder, for hosts where a proxy injects
the credential.
"""
import hashlib
import json
import os
import time
from pathlib import Path

CACHE = Path.home() / ".cache" / "cmp-assistant"
UPLOADS = CACHE / "uploads.json"


def _sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()[:16]


def _uploads():
    return json.loads(UPLOADS.read_text()) if UPLOADS.exists() else {}


def _remember(key, handle):
    u = _uploads()
    u[key] = handle
    CACHE.mkdir(parents=True, exist_ok=True)
    UPLOADS.write_text(json.dumps(u, indent=1))


def _key(var):
    return os.environ.get(var) or "proxy-injected"


class Claude:
    name = "anthropic"

    def __init__(self, model, settings):
        import anthropic
        self.model, self.settings = model, settings
        # Explicit base URL: the session may set ANTHROPIC_BASE_URL for its own traffic.
        self.client = anthropic.Anthropic(api_key=_key("CMP_EVAL_ANTHROPIC_KEY"),
                                          base_url="https://api.anthropic.com", max_retries=4)

    def _file(self, path):
        k = f"anthropic:{_sha(path)}"
        u = _uploads()
        if k in u and u[k]["expires"] > time.time() + 86400:
            return u[k]["id"]
        f = self.client.files.upload(file=Path(path), expires_in_seconds=30 * 86400)
        _remember(k, {"id": f.id, "expires": time.time() + 30 * 86400})
        return f.id

    def _params(self, req):
        content = []
        for p in req["parts"]:
            if "pdf" in p:
                content.append({"type": "document", "source": {"type": "file", "file_id": self._file(p["pdf"])}})
            else:
                content.append({"type": "text", "text": p["text"]})
            if p.get("cache"):
                content[-1]["cache_control"] = {"type": "ephemeral", "ttl": "1h"}
        params = {"model": self.model, "max_tokens": req["max_tokens"],
                  "messages": [{"role": "user", "content": content}]}
        if self.settings.get("effort"):
            params["output_config"] = {"effort": self.settings["effort"]}
        return params

    @staticmethod
    def _out(msg):
        u = msg.usage
        return {"text": "".join(b.text for b in msg.content if b.type == "text"),
                "usage": {"input": u.input_tokens, "cache_write": u.cache_creation_input_tokens or 0,
                          "cache_read": u.cache_read_input_tokens or 0, "output": u.output_tokens},
                "stop": msg.stop_reason, "error": None}

    def sync(self, req):
        with self.client.messages.stream(**self._params(req)) as s:
            return self._out(s.get_final_message())

    def submit(self, reqs):
        # custom_id must match ^[a-zA-Z0-9_-]{1,64}$, so send the position; results() maps it back
        # through the ids list run.py keeps in batches.json.
        from anthropic.types.messages.batch_create_params import Request
        b = self.client.messages.batches.create(
            requests=[Request(custom_id=f"q{i}", params=self._params(r)) for i, r in enumerate(reqs)])
        return b.id

    def done(self, batch_id):
        return self.client.messages.batches.retrieve(batch_id).processing_status == "ended"

    def progress(self, batch_id):
        b = self.client.messages.batches.retrieve(batch_id)
        c = b.request_counts
        done = c.succeeded + c.errored + c.canceled + c.expired
        return {"state": b.processing_status, "done": done, "total": done + c.processing,
                "succeeded": c.succeeded, "errored": c.errored, "canceled": c.canceled, "expired": c.expired}

    def cancel(self, batch_id):
        return self.client.messages.batches.cancel(batch_id).processing_status

    def results(self, batch_id, ids=None):
        out = {}
        for r in self.client.messages.batches.results(batch_id):
            if ids and r.custom_id.startswith("q") and r.custom_id[1:].isdigit():
                r.custom_id = ids[int(r.custom_id[1:])]
            if r.result.type == "succeeded":
                out[r.custom_id] = self._out(r.result.message)
            else:
                err = getattr(r.result, "error", None)
                out[r.custom_id] = {"text": "", "usage": None, "error": f"{r.result.type}: {err}"}
        return out


class Gemini:
    name = "gemini"

    def __init__(self, model, settings):
        from google import genai
        self.model, self.settings = model, settings
        self.client = genai.Client(api_key=_key("GEMINI_API_KEY"))

    def _file(self, path):
        # Gemini keeps uploads for 48 hours.
        k = f"gemini:{_sha(path)}"
        u = _uploads()
        if k in u and u[k]["expires"] > time.time() + 3600:
            return u[k]["uri"]
        f = self.client.files.upload(file=str(path), config={"mime_type": "application/pdf"})
        _remember(k, {"uri": f.uri, "expires": time.time() + 47 * 3600})
        return f.uri

    def _req(self, req):
        parts = [{"file_data": {"file_uri": self._file(p["pdf"]), "mime_type": "application/pdf"}}
                 if "pdf" in p else {"text": p["text"]} for p in req["parts"]]
        cfg = {"max_output_tokens": req["max_tokens"]}
        if self.settings.get("thinking_level"):
            cfg["thinking_config"] = {"thinking_level": self.settings["thinking_level"]}
        return {"contents": [{"role": "user", "parts": parts}], "config": cfg}

    @staticmethod
    def _out(resp):
        m = resp.usage_metadata
        cached = m.cached_content_token_count or 0
        return {"text": resp.text or "",
                "usage": {"input": (m.prompt_token_count or 0) - cached, "cache_write": 0, "cache_read": cached,
                          "output": (m.candidates_token_count or 0) + (m.thoughts_token_count or 0)},
                "stop": str(resp.candidates[0].finish_reason) if resp.candidates else None, "error": None}

    def sync(self, req):
        r = self._req(req)
        return self._out(self.client.models.generate_content(model=self.model, contents=r["contents"],
                                                             config=r["config"]))

    def submit(self, reqs):
        self._order = [r["id"] for r in reqs]
        src = [dict(self._req(r), metadata={"id": r["id"]}) for r in reqs]
        job = self.client.batches.create(model=self.model, src=src)
        return job.name

    def done(self, batch_id):
        s = str(self.client.batches.get(name=batch_id).state)
        return any(x in s for x in ("SUCCEEDED", "FAILED", "CANCELLED", "EXPIRED"))

    def progress(self, batch_id):
        job = self.client.batches.get(name=batch_id)
        st = getattr(job, "batch_stats", None)
        total = getattr(st, "request_count", None)
        pend = getattr(st, "pending_request_count", None)
        return {"state": str(job.state), "done": total - pend if total is not None and pend is not None else None,
                "total": total}

    def cancel(self, batch_id):
        self.client.batches.cancel(name=batch_id)
        return str(self.client.batches.get(name=batch_id).state)

    def results(self, batch_id, ids=None):
        job = self.client.batches.get(name=batch_id)
        out = {}
        for i, r in enumerate(job.dest.inlined_responses or []):
            rid = (getattr(r, "metadata", None) or {}).get("id") or (ids[i] if ids and i < len(ids) else str(i))
            out[rid] = self._out(r.response) if r.response else {"text": "", "usage": None, "error": str(r.error)}
        return out


class OpenAI:
    name = "openai"

    def __init__(self, model, settings):
        import openai
        self.model, self.settings = model, settings
        self.client = openai.OpenAI(api_key=_key("OPENAI_API_KEY"), max_retries=4)

    def _file(self, path):
        k = f"openai:{_sha(path)}"
        u = _uploads()
        if k in u:
            return u[k]["id"]
        f = self.client.files.create(file=open(path, "rb"), purpose="user_data")
        _remember(k, {"id": f.id, "expires": 0})
        return f.id

    def _body(self, req):
        content = [{"type": "input_file", "file_id": self._file(p["pdf"])} if "pdf" in p
                   else {"type": "input_text", "text": p["text"]} for p in req["parts"]]
        body = {"model": self.model, "max_output_tokens": req["max_tokens"],
                "input": [{"role": "user", "content": content}]}
        if self.settings.get("reasoning_effort"):
            body["reasoning"] = {"effort": self.settings["reasoning_effort"]}
        return body

    @staticmethod
    def _out(d):
        u = d.get("usage") or {}
        cached = (u.get("input_tokens_details") or {}).get("cached_tokens", 0)
        text = "".join(c.get("text", "") for o in d.get("output", []) if o.get("type") == "message"
                       for c in o.get("content", []))
        return {"text": text, "usage": {"input": u.get("input_tokens", 0) - cached, "cache_write": 0,
                                        "cache_read": cached, "output": u.get("output_tokens", 0)},
                "stop": d.get("status"), "error": None}

    def sync(self, req):
        return self._out(self.client.responses.create(**self._body(req)).model_dump())

    def submit(self, reqs):
        lines = [json.dumps({"custom_id": r["id"], "method": "POST", "url": "/v1/responses", "body": self._body(r)})
                 for r in reqs]
        CACHE.mkdir(parents=True, exist_ok=True)
        p = CACHE / f"openai-batch-{int(time.time())}.jsonl"
        p.write_text("\n".join(lines) + "\n")
        f = self.client.files.create(file=open(p, "rb"), purpose="batch")
        return self.client.batches.create(input_file_id=f.id, endpoint="/v1/responses", completion_window="24h").id

    def done(self, batch_id):
        return self.client.batches.retrieve(batch_id).status in ("completed", "failed", "expired", "cancelled")

    def progress(self, batch_id):
        b = self.client.batches.retrieve(batch_id)
        c = b.request_counts
        return {"state": b.status, "done": (c.completed + c.failed) if c else None, "total": c.total if c else None}

    def cancel(self, batch_id):
        return self.client.batches.cancel(batch_id).status

    def results(self, batch_id, ids=None):
        b = self.client.batches.retrieve(batch_id)
        out = {}
        for fid in (b.output_file_id, b.error_file_id):
            if not fid:
                continue
            for line in self.client.files.content(fid).text.splitlines():
                d = json.loads(line)
                resp = d.get("response") or {}
                if resp.get("status_code") == 200:
                    out[d["custom_id"]] = self._out(resp["body"])
                else:
                    out[d["custom_id"]] = {"text": "", "usage": None, "error": json.dumps(d.get("error") or resp)[:500]}
        return out


PROVIDERS = {"anthropic": Claude, "gemini": Gemini, "openai": OpenAI}


def make(model_cfg):
    return PROVIDERS[model_cfg["provider"]](model_cfg["id"], model_cfg.get("settings", {}))
