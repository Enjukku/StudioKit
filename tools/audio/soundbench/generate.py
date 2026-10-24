"""`generate`: ask ElevenLabs' sound-effects API for one round of takes for a cue (editor-design.md sections 3 and 8;
build step 7).

Kit tool (universal). Author: feature-builder · claude-opus-5-5 · high · 2026-10-24 (J020 step 7)

Input, in the cue folder: `card.json` (its tier sets the takes per round) and `prompts.json` (written by the sound
designer for this round):
  {"cue": "SFX-COMBAT-HIT",
   "prompts": ["texture description 1", "texture description 2"],    the takes are spread over these in turn
   "duration_s": 0.8,              optional, 0.5-30; left out: the service chooses the length (55 credits flat)
   "prompt_influence": 0.6,        optional, 0-1; left out: the service default (0.3)
   "loop": false,                  optional
   "model": "eleven_text_to_sound_v2",   optional; or "eleven_text_to_sound_v3"
   "takes": 3,                     optional; another count than the tier's (J020-D9) is a warning
   "note": "what changed this round"}    optional, copied into every sidecar
  An important cue's layers are generated separately, one prompt set each (J020-D9): "layers" replaces "prompts":
   "layers": [{"name": "body", "prompts": ["..."], <any optional field above>}, ...]
  and each layer's takes are named `<cue>.<layer>.r<k>.t<n>`, with its own rounds.

What it does, refusing before any call when something is wrong:
  1. reads the card and prompts.json (every field checked; an unknown field is an error) and the key from the
     environment variable ELEVENLABS_API_KEY only (run through `python tools/keys.py run --only ELEVENLABS_API_KEY
     -- ...`); it never reads a key file;
  2. finds each sound's next round from the takes present (rejected ones count); round 4 is refused (J020-D7);
  3. plans the round (takes per tier: minor 3, frequent 4, important 6, J020-D9) and predicts each call's cost:
     ceil(11 x duration_s) credits with a duration, 55 without (measured 2026-10-24); a round predicted over the
     budget is refused; before every call (and every retry) it stops when spent + possibly spent + the call's
     prediction would pass the budget;
  4. asks for `wav_44100` first, then `mp3_44100_192`, then `mp3_44100_128` when a response refuses the format
     (a 4xx that names the format, or a 403 naming the subscription or tier); a refused format is skipped for the
     rest of the run. The received bytes decide the file type (RIFF WAV or MP3); a mismatch is a warning;
  5. retries 429, 5xx and network failures at most MAX_ATTEMPTS times per take and format, waiting Retry-After
     (at most 30 s) or 2 s, 4 s. Every attempt is logged with its status and charge: the `character-cost` header
     when present (an error that carries one is counted as spent), "unknown" for a network failure (counted at the
     prediction as possibly spent), so a retry never spends twice without a record;
  6. writes the take `takes/<sound>.r<k>.t<n>.wav|mp3` and its sidecar `.json` (never over an existing file), then
     decodes it once with `intake.decode_take(take, requested_ms=)`; bytes that are not audio, or a take intake
     refuses, move to `takes/rejected/` with their sidecar (the credits stay counted);
  7. writes the run log `report/<cue>.generate.<UTC time>.json`: the plan, every attempt, the credits predicted,
     spent and possibly spent, the formats refused, warnings, and why it stopped.
The key appears only in the request header: every text written or printed is passed through `redact` (the key and
anything shaped like an ElevenLabs key become `<redacted>`), and the sidecar keeps only named response headers.

Exit codes (CLI): 0 every planned take made and decoded; 1 stopped by the budget, or a take was rejected; 2 refused
before any call, or a call failed (auth, validation, every format refused, retries used up).

Usage:
  python tools/keys.py run --only ELEVENLABS_API_KEY -- python -m tools.audio.soundbench generate <cue-folder>
      [--budget CREDITS] [--dry-run] [--json]
"""

from __future__ import annotations

import datetime as dt
import json
import math
import os
import re
import shutil
import time
import urllib.error
import urllib.request
import wave
from dataclasses import dataclass, field
from pathlib import Path

from . import card as cardmod
from . import intake
from .core import SoundbenchError, file_sha256
from .rank import MAX_ROUNDS, TAKES_PER_ROUND  # J020-D7, J020-D9: one source with rank

API = "https://api.elevenlabs.io/v1/sound-generation"
ENDPOINT = "/v1/sound-generation"
KEY_ENV = "ELEVENLABS_API_KEY"
MODELS = ("eleven_text_to_sound_v2", "eleven_text_to_sound_v3")
DEFAULT_MODEL = MODELS[0]
FORMATS = ("wav_44100", "mp3_44100_192", "mp3_44100_128")  # design section 8: WAV first, then the MP3 fallbacks
DURATION_MIN_S, DURATION_MAX_S = 0.5, 30.0  # measured 2026-10-24: 0.1 answered 400 invalid_generation_settings
CREDITS_PER_SECOND = 11  # measured 2026-10-24: 0.5 s -> 6, 1 s -> 11, 2 s -> 22 (character-cost), = ceil(11 x d)
CREDITS_NO_DURATION = 55  # measured 2026-10-24: 55 on both requests without duration_seconds (about 1 s returned)
DEFAULT_BUDGET = 300  # PROPOSAL: credits per run; an important 3-layer round of 1 s takes predicts 198
MAX_ATTEMPTS = 3  # PROPOSAL: per take and format (429, 5xx, network)
BACKOFF_S = (2.0, 4.0)  # PROPOSAL: waits before attempts 2 and 3 when the response names no Retry-After
MAX_WAIT_S = 30.0
TIMEOUT_S = 120.0
RETRY_STATUSES = (429, 500, 502, 503, 504)
TRACE_HEADERS = ("character-cost", "content-type", "date", "x-trace-id", "request-id", "history-item-id", "x-region",
                 "retry-after")
LAYER_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,31}$")
KEY_LIKE_RE = re.compile(r"sk_[A-Za-z0-9]{16,}")
PROMPT_FIELDS = {"duration_s", "prompt_influence", "loop", "model", "takes", "prompts"}


@dataclass
class Response:
    status: int
    headers: dict
    body: bytes


class NetworkError(Exception):
    """No HTTP answer (connection reset, timeout): the service may or may not have charged the call."""


class _Stop(Exception):
    """Ends the run: a non-retryable answer, every format refused, or the retries used up."""


@dataclass
class Run:
    budget: float
    key: str
    spent: int = 0
    possibly: int = 0
    refused: list = field(default_factory=list)
    warnings: list = field(default_factory=list)


# ------------------------------------------------------------------------------------------------ secrets
def redact(text: str, key: str) -> str:
    """The key and anything shaped like an ElevenLabs key replaced by <redacted>."""
    if key:
        text = text.replace(key, "<redacted>")
    return KEY_LIKE_RE.sub("<redacted>", text)


def trace_headers(headers: dict) -> dict:
    """The response headers a take keeps for tracing and billing; never the rest."""
    low = {str(k).lower(): str(v) for k, v in headers.items()}
    return {k: low[k] for k in TRACE_HEADERS if k in low}


def _dump(path: Path, doc: dict, key: str, mode: str = "x") -> None:
    text = redact(json.dumps(doc, indent=2), key) + "\n"
    with open(path, mode, encoding="utf-8") as f:
        f.write(text)


# ------------------------------------------------------------------------------------------------ HTTP
def urllib_send(url: str, data: bytes, headers: dict, timeout: float) -> Response:
    req = urllib.request.Request(url, data=data, method="POST")
    for k, v in headers.items():
        req.add_header(k, v)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return Response(resp.status, dict(resp.headers), resp.read())
    except urllib.error.HTTPError as err:
        return Response(err.code, dict(err.headers or {}), err.read() or b"")
    except (urllib.error.URLError, TimeoutError, ConnectionError, OSError) as err:
        reason = getattr(err, "reason", err)
        raise NetworkError(f"{type(err).__name__}: {reason}") from None


# ------------------------------------------------------------------------------------------------ rules
def predict(duration_s: float | None) -> int:
    return CREDITS_NO_DURATION if duration_s is None else math.ceil(CREDITS_PER_SECOND * duration_s - 1e-9)


def budget_allows(spent: float, predicted: float, budget: float) -> bool:
    return spent + predicted <= budget


def format_refused(resp: Response, fmt: str) -> bool:
    """A refusal of the asked format, read from the response (never from a guess about the plan)."""
    if resp.status not in (400, 401, 402, 403, 422):
        return False
    text = resp.body.decode("utf-8", "replace").lower()
    if "output_format" in text or fmt.lower() in text:
        return True
    return resp.status == 403 and ("subscription" in text or "tier" in text)


def attempt_record(status: int | None, headers: dict, predicted: int, error: str | None = None) -> dict:
    """One call's record. charged: yes (character-cost > 0), no (none or 0), unknown (no answer: counted at the
    prediction as possibly spent)."""
    if status is None:
        return {"status": None, "error": error, "charged": "unknown", "credits": None, "counted_credits": predicted}
    raw = {str(k).lower(): v for k, v in headers.items()}.get("character-cost")
    credits = int(raw) if raw is not None and str(raw).strip().isdigit() else None
    rec = {"status": status, "charged": "yes" if credits else "no", "credits": credits,
           "counted_credits": credits or 0}
    if status == 200 and credits is None:  # a success with no cost header: count the prediction, say so
        rec.update(charged="unknown", counted_credits=predicted, note="no character-cost header: prediction counted")
    if error:
        rec["error"] = error
    return rec


def sniff(body: bytes) -> dict | None:
    """What the bytes are: a RIFF WAV (with its header fields) or an MP3; None for anything else."""
    if body[:4] == b"RIFF" and body[8:12] == b"WAVE":
        try:
            import io

            with wave.open(io.BytesIO(body)) as w:
                return {"container": "wav", "codec": f"pcm_s{8 * w.getsampwidth()}le", "rate": w.getframerate(),
                        "channels": w.getnchannels(), "frames": w.getnframes()}
        except (wave.Error, EOFError):
            return None
    if body[:3] == b"ID3" or (len(body) > 1 and body[0] == 0xFF and (body[1] & 0xE0) == 0xE0):
        return {"container": "mp3"}
    return None


def _wait_s(resp: Response | None, attempt: int) -> float:
    if resp is not None:
        ra = {str(k).lower(): v for k, v in resp.headers.items()}.get("retry-after")
        try:
            if ra is not None and math.isfinite(float(ra)) and float(ra) >= 0:
                return min(MAX_WAIT_S, float(ra))
        except ValueError:
            pass
    return BACKOFF_S[min(attempt - 1, len(BACKOFF_S) - 1)]


# ------------------------------------------------------------------------------------------------ input
def _check_sound(obj: dict, where: str, allowed: set, inherit: dict) -> dict:
    extra = set(obj) - allowed
    if extra:
        raise SoundbenchError(f"{where}: unknown field(s) {sorted(extra)} (allowed: {sorted(allowed)})")
    s = {**inherit, **{k: v for k, v in obj.items() if k in PROMPT_FIELDS}}
    prompts = s.get("prompts")
    if not isinstance(prompts, list) or not prompts or not all(isinstance(p, str) and p.strip() for p in prompts):
        raise SoundbenchError(f"{where}.prompts: needs a list of one or more non-empty texts")
    d = s.get("duration_s")
    if d is not None and (isinstance(d, bool) or not isinstance(d, (int, float)) or not math.isfinite(d)
                          or not DURATION_MIN_S <= d <= DURATION_MAX_S):
        raise SoundbenchError(f"{where}.duration_s: {d!r} is outside {DURATION_MIN_S}-{DURATION_MAX_S} s (the service "
                              "refused 0.1 s on 2026-10-24); leave it out to let the service choose")
    pi = s.get("prompt_influence")
    if pi is not None and (isinstance(pi, bool) or not isinstance(pi, (int, float)) or not 0 <= pi <= 1):
        raise SoundbenchError(f"{where}.prompt_influence: needs a number from 0 to 1, got {pi!r}")
    if not isinstance(s.get("loop", False), bool):
        raise SoundbenchError(f"{where}.loop: needs true or false, got {s.get('loop')!r}")
    if s.get("model", DEFAULT_MODEL) not in MODELS:
        raise SoundbenchError(f"{where}.model: {s.get('model')!r} is not one of {list(MODELS)}")
    t = s.get("takes")
    if t is not None and (isinstance(t, bool) or not isinstance(t, int) or not 1 <= t <= 12):
        raise SoundbenchError(f"{where}.takes: needs a whole number from 1 to 12, got {t!r}")
    return s


def load_prompts(path: Path, cue: str, tier: str) -> list[dict]:
    """[{name, layer, prompts, duration_s, prompt_influence, loop, model, takes, note}] for each sound to generate."""
    if not path.is_file():
        raise SoundbenchError(f"no prompts.json in the cue folder: {path}")
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as err:
        raise SoundbenchError(f"{path}: not valid JSON ({err})") from err
    if not isinstance(doc, dict):
        raise SoundbenchError(f"{path}: needs an object")
    if doc.get("cue") != cue:
        raise SoundbenchError(f"prompts.json: cue {doc.get('cue')!r} differs from card.json's {cue!r}")
    note = doc.get("note")
    if note is not None and not isinstance(note, str):
        raise SoundbenchError("prompts.json.note: needs a text")
    top = PROMPT_FIELDS | {"cue", "note", "layers"}
    if ("prompts" in doc) == ("layers" in doc):
        raise SoundbenchError("prompts.json: give either prompts (one sound) or layers (one prompt set each)")
    if "prompts" in doc:
        sounds = [(None, _check_sound(doc, "prompts.json", top, {}))]
    else:
        layers = doc["layers"]
        if not isinstance(layers, list) or not layers:
            raise SoundbenchError("prompts.json.layers: needs a list of one or more layers")
        if tier != "important":
            raise SoundbenchError(f"prompts.json.layers: layers are generated separately for important cues "
                                  f"(J020-D9); this card's tier is {tier}")
        inherit = {k: v for k, v in doc.items() if k in PROMPT_FIELDS - {"prompts"}}
        _check_sound({**inherit, "prompts": ["x"]}, "prompts.json", top, {})
        sounds, names = [], set()
        for i, lay in enumerate(layers):
            where = f"prompts.json.layers[{i}]"
            if not isinstance(lay, dict) or not isinstance(lay.get("name"), str) or not LAYER_RE.match(lay["name"]):
                raise SoundbenchError(f"{where}.name: needs a short lower-case name (a-z, 0-9, -)")
            if lay["name"] in names:
                raise SoundbenchError(f"{where}.name: {lay['name']!r} given twice")
            names.add(lay["name"])
            sounds.append((lay["name"], _check_sound(lay, where, PROMPT_FIELDS | {"name"}, inherit)))
    out = []
    for layer, s in sounds:
        out.append({"name": cue if layer is None else f"{cue}.{layer}", "layer": layer, "prompts": s["prompts"],
                    "duration_s": None if s.get("duration_s") is None else float(s["duration_s"]),
                    "prompt_influence": s.get("prompt_influence"), "loop": s.get("loop", False),
                    "model": s.get("model", DEFAULT_MODEL), "takes": s.get("takes"), "note": note})
    return out


def rounds_present(takes_dir: Path, name: str) -> set[int]:
    """Rounds that have a take of this sound, kept or rejected (a rejected take used its round)."""
    pat = re.compile(r"^" + re.escape(name) + r"\.r(\d+)\.t\d+\.(?:mp3|wav|bin)$", re.IGNORECASE)
    found = set()
    for folder in (takes_dir, takes_dir / "rejected"):
        if folder.is_dir():
            for p in folder.iterdir():
                m = pat.match(p.name)
                if m:
                    found.add(int(m.group(1)))
    return found


def _body(sound: dict, text: str) -> dict:
    body = {"text": text, "model_id": sound["model"]}
    if sound["duration_s"] is not None:
        body["duration_seconds"] = sound["duration_s"]
    if sound["prompt_influence"] is not None:
        body["prompt_influence"] = sound["prompt_influence"]
    body["loop"] = sound["loop"]
    return body


def plan(cue_dir: Path) -> tuple[dict, list[dict], list[dict], list[str]]:
    """(card, sounds with their round, planned calls, warnings); refuses round 4 and existing files."""
    card = cardmod.load_card(cue_dir / "card.json")
    sounds = load_prompts(cue_dir / "prompts.json", card["cue"], card["tier"])
    want = TAKES_PER_ROUND[card["tier"]]
    takes_dir = cue_dir / "takes"
    calls, warnings = [], []
    for s in sounds:
        present = rounds_present(takes_dir, s["name"])
        s["round"] = max(present, default=0) + 1
        if s["round"] > MAX_ROUNDS:
            raise SoundbenchError(f"{s['name']}: rounds {sorted(present)} are done; a cue has at most {MAX_ROUNDS} "
                                  f"rounds (J020-D7): it goes to the owner with its numbers, round {s['round']} refused")
        n = s["takes"] or want
        if n != want:
            warnings.append(f"{s['name']}: {n} takes this round; a {card['tier']} cue gets {want} per round (J020-D9)")
        for t in range(1, n + 1):
            stem = f"{s['name']}.r{s['round']}.t{t}"
            for suffix in (".wav", ".mp3", ".json", ".master.wav", ".bin"):
                for folder in (takes_dir, takes_dir / "rejected"):
                    if (folder / (stem + suffix)).exists():
                        raise SoundbenchError(f"{folder / (stem + suffix)} exists: takes are never overwritten; "
                                              "refused before any call")
            calls.append({"cue": card["cue"], "sound": s["name"], "layer": s["layer"], "round": s["round"], "take": t,
                          "stem": stem,
                          "body": _body(s, s["prompts"][(t - 1) % len(s["prompts"])]),
                          "requested_ms": None if s["duration_s"] is None else round(1000 * s["duration_s"], 3),
                          "predicted": predict(s["duration_s"]), "note": s["note"]})
    return card, sounds, calls, warnings


# ------------------------------------------------------------------------------------------------ the calls
def _call_take(call: dict, run: Run, send, sleep) -> tuple[Response, str, list[str], list[dict]]:
    """One take: through the format order and the retries. Returns (response, format used, formats refused here,
    attempts). Raises _Stop with the attempts when the run must end."""
    attempts, refused_here = [], []
    formats = [f for f in FORMATS if f not in run.refused]
    headers = {"xi-api-key": run.key, "Content-Type": "application/json", "Accept": "audio/*"}
    data = json.dumps(call["body"]).encode("utf-8")
    for fmt in formats:
        last = None
        for attempt in range(1, MAX_ATTEMPTS + 1):
            if not budget_allows(run.spent + run.possibly, call["predicted"], run.budget):
                raise _Stop(f"budget: {run.spent + run.possibly} spent or possibly spent + {call['predicted']} "
                            f"predicted for {call['stem']} would pass the budget of {run.budget:g} credits",
                            attempts, "budget")
            if attempt > 1:
                wait = _wait_s(last, attempt - 1)
                attempts[-1]["waited_s_after"] = wait
                sleep(wait)
            try:
                resp = send(f"{API}?output_format={fmt}", data, headers, TIMEOUT_S)
            except NetworkError as err:
                rec = attempt_record(None, {}, call["predicted"], redact(str(err), run.key))
                rec.update(n=len(attempts) + 1, format=fmt)
                attempts.append(rec)
                run.possibly += rec["counted_credits"]
                last = None
                continue
            body_text = redact(resp.body[:600].decode("utf-8", "replace"), run.key) if resp.status != 200 else None
            rec = attempt_record(resp.status, resp.headers, call["predicted"], body_text)
            rec.update(n=len(attempts) + 1, format=fmt, headers=trace_headers(resp.headers))
            attempts.append(rec)
            if rec["charged"] == "unknown":
                run.possibly += rec["counted_credits"]
            else:
                run.spent += rec["counted_credits"]
            if resp.status == 200:
                return resp, fmt, refused_here, attempts
            if format_refused(resp, fmt):
                refused_here.append(fmt)
                run.refused.append(fmt)
                break
            if resp.status in RETRY_STATUSES:
                last = resp
                continue
            hint = ""
            if "authentication" in (body_text or "").lower() or "api_key" in (body_text or "").lower():
                hint = (f"; the key is read from {KEY_ENV}: a value already set in the Windows environment wins over "
                        "the file in keys.json (tools/keys.py run)")
            raise _Stop(f"{call['stem']}: HTTP {resp.status} {body_text}{hint}", attempts, "failed")
        else:
            raise _Stop(f"{call['stem']}: no answer after {MAX_ATTEMPTS} attempts in {fmt} (last: "
                        f"{attempts[-1].get('status') or attempts[-1].get('error')})", attempts, "failed")
    raise _Stop(f"{call['stem']}: every format refused ({', '.join(FORMATS)}); see the response bodies in the log",
                attempts, "failed")


def _save_take(cue_dir: Path, call: dict, resp: Response, fmt: str, refused_here: list, attempts: list, run: Run,
               decode) -> dict:
    got = sniff(resp.body)
    asked = fmt.split("_")[0]
    takes_dir = cue_dir / "takes"
    takes_dir.mkdir(parents=True, exist_ok=True)
    charged = sum(a["counted_credits"] for a in attempts if a["charged"] == "yes")
    success = attempts[-1]
    side = {"tool": "soundbench generate", "provider": "ElevenLabs", "endpoint": ENDPOINT, "cue": call["cue"],
            "sound": call["sound"], "layer": call["layer"],
            "round": call["round"], "take": call["take"], "request": call["body"], "query": {"output_format": fmt},
            "format_asked": attempts[0]["format"], "formats_refused": refused_here, "format_used": fmt, "format_received": got,
            "requested_ms": call["requested_ms"], "credits": success["credits"], "credits_predicted": call["predicted"],
            "credits_all_attempts": charged, "response": {"status": resp.status, "headers": trace_headers(resp.headers)},
            "attempts": attempts, "bytes": len(resp.body), "sha256": None,
            "generated": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "note": call["note"],
            "status": "not auditioned (an agent cannot listen; the owner judges in play-tests, J020-D3)"}
    if got is None:
        return _reject(takes_dir, call["stem"], ".bin", resp.body, side, "the bytes are neither a WAV nor an MP3", run)
    if got["container"] != asked:
        run.warnings.append(f"{call['stem']}: asked {fmt}, received {got['container']} bytes (saved as received)")
    take = takes_dir / f"{call['stem']}.{got['container']}"
    with open(take, "xb") as f:
        f.write(resp.body)
    side["sha256"] = file_sha256(take)
    _dump(take.with_suffix(".json"), side, run.key)
    try:
        decode(take, requested_ms=call["requested_ms"])
    except SoundbenchError as err:
        rej = takes_dir / "rejected"
        rej.mkdir(exist_ok=True)
        side["rejected"] = f"intake refused: {redact(str(err), run.key)}"
        take.with_suffix(".json").unlink()
        shutil.move(str(take), str(rej / take.name))
        intake.master_path(take).unlink(missing_ok=True)
        _dump(rej / (call["stem"] + ".json"), side, run.key)
        return {"stem": call["stem"], "rejected": side["rejected"], "file": str(rej / take.name)}
    return {"stem": call["stem"], "file": str(take), "format_used": fmt, "credits": side["credits"]}


def _reject(takes_dir: Path, stem: str, suffix: str, body: bytes, side: dict, why: str, run: Run) -> dict:
    rej = takes_dir / "rejected"
    rej.mkdir(parents=True, exist_ok=True)
    path = rej / (stem + suffix)
    with open(path, "xb") as f:
        f.write(body)
    side.update(sha256=file_sha256(path), rejected=why)
    _dump(rej / (stem + ".json"), side, run.key)
    return {"stem": stem, "rejected": why, "file": str(path)}


def generate(cue_dir: Path, budget: float = DEFAULT_BUDGET, *, send=None, sleep=None, env=None, decode=None,
             dry_run: bool = False) -> tuple[dict, int]:
    """One round for the cue (every sound in prompts.json). Returns (run log, exit code); raises SoundbenchError when
    refused before any call."""
    cue_dir = Path(cue_dir)
    send = urllib_send if send is None else send
    sleep = time.sleep if sleep is None else sleep
    env = os.environ if env is None else env
    decode = intake.decode_take if decode is None else decode
    if isinstance(budget, bool) or not isinstance(budget, (int, float)) or not math.isfinite(budget) or budget <= 0:
        raise SoundbenchError(f"budget: needs a positive number of credits, got {budget!r}")
    card, sounds, calls, warnings = plan(cue_dir)
    predicted = sum(c["predicted"] for c in calls)
    doc = {"tool": "soundbench generate", "cue": card["cue"], "tier": card["tier"], "budget": budget,
           "predicted_credits": predicted, "cost_model": {"credits_per_second": CREDITS_PER_SECOND,
                                                          "credits_no_duration": CREDITS_NO_DURATION},
           "sounds": [{"name": s["name"], "round": s["round"], "rounds_left_after": MAX_ROUNDS - s["round"]}
                      for s in sounds],
           "plan": [{k: c[k] for k in ("stem", "predicted", "requested_ms")} | {"text": c["body"]["text"]}
                    for c in calls],
           "warnings": warnings, "formats_order": list(FORMATS)}
    if dry_run:
        doc.update(dry_run=True, spent_credits=0, possibly_spent_credits=0)
        return doc, 0
    key = str(env.get(KEY_ENV, "")).strip()
    if not key:
        raise SoundbenchError(f"{KEY_ENV} is not set: run `python tools/keys.py run --only ELEVENLABS_API_KEY -- "
                              "python -m tools.audio.soundbench generate ...` (the tool never reads a key file)")
    if not budget_allows(0, predicted, budget):
        raise SoundbenchError(f"the round predicts {predicted} credits ({len(calls)} calls) and the budget is "
                              f"{budget:g}: refused before any call (raise --budget or plan fewer or shorter takes)")
    run = Run(budget=budget, key=key, warnings=warnings)
    made, rejected, failed, stopped, code = [], [], [], None, 0
    started = dt.datetime.now(dt.timezone.utc)
    for call in calls:
        try:
            resp, fmt, refused_here, attempts = _call_take(call, run, send, sleep)
        except _Stop as stop:
            msg, attempts, why = stop.args
            stopped = redact(msg, key)
            if attempts:
                failed.append({"stem": call["stem"], "attempts": attempts})
            code = 1 if why == "budget" else 2
            break
        res = _save_take(cue_dir, call, resp, fmt, refused_here, attempts, run, decode)
        (rejected if "rejected" in res else made).append(res)
    if rejected and code == 0:
        code = 1
    doc.update(spent_credits=run.spent, possibly_spent_credits=run.possibly, formats_refused=run.refused,
               takes=made, rejected=rejected, failed=failed, stopped=stopped, exit_code=code,
               started=started.strftime("%Y-%m-%dT%H:%M:%SZ"),
               finished=dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))
    rep = cue_dir / "report"
    rep.mkdir(parents=True, exist_ok=True)
    base = f"{card['cue']}.generate.{started.strftime('%Y%m%dT%H%M%S%fZ')}"
    doc["log"] = str(rep / f"{base}.json")
    _dump(rep / f"{base}.json", doc, key)
    return json.loads(redact(json.dumps(doc), key)), code
