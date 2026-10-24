"""Tests for soundbench `generate` (J020 step 7; editor-design.md sections 3 and 8; J020-D7, D9).

No network: every test drives `generate` through a fake HTTP layer (`FakeAPI`) that answers like the real service did
on 2026-10-24 (probes in the step 7 hand-back): 200 with a 16-bit stereo WAV or an MP3 body, the `character-cost`
header (ceil(11 x duration) credits), `x-trace-id`; 400 `invalid_generation_settings` below 0.5 s. Oracles come from
the brief and the owner's decisions (takes per tier, three rounds, the budget rule, the format order), never from the
module's own output. The real requests run only in `test_soundbench_generate_live` style scripts outside the gate.
The planted-fault test at the end shows each named fault makes these tests FAIL (not error).
"""

import contextlib
import io
import json
import math
import os
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

try:
    import numpy as np
    import pyloudnorm  # noqa: F401
    import scipy  # noqa: F401
    import soundfile as sf
except ImportError:  # optional deps: the kit gate is standard library only
    raise unittest.SkipTest("needs numpy, scipy, soundfile and pyloudnorm")

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.audio.soundbench import __main__ as cli  # noqa: E402
from tools.audio.soundbench import ffmpeg as sbf  # noqa: E402
from tools.audio.soundbench import fixtures as fx  # noqa: E402
from tools.audio.soundbench import generate as gen  # noqa: E402
from tools.audio.soundbench import intake, rank  # noqa: E402
from tools.audio.soundbench.core import SoundbenchError, file_sha256  # noqa: E402

try:
    FOUND = sbf.find_ffmpeg()
except SoundbenchError:
    FOUND = None
HAS_LAME = bool(FOUND) and "libmp3lame" in sbf.encoders(FOUND.path)
needs_ffmpeg = unittest.skipUnless(FOUND, "ffmpeg not found: generate tests that decode takes skipped")
needs_lame = unittest.skipUnless(HAS_LAME, "ffmpeg with libmp3lame not found: MP3 fallback test skipped")

KEY = "sk_" + "0123456789abcdef" * 3  # a fake key shaped like a real one (sk_ + 48 hex)
KEY_LIKE = re.compile(r"sk_[0-9a-fA-F]{16,}")
ENV = {"ELEVENLABS_API_KEY": KEY}
R = 44100

CARD = {"cue": "SFX-G-HIT", "kind": "hit", "category": "sfx", "tier": "minor",
        "level": {"measure": "F-09", "target": -24.0, "tolerance": 1.0, "must": True},
        "targets": {"onset_ms": {"max": 5, "must": True}, "true_peak_dbtp": {"max": -1.0, "must": True}},
        "playback": {"space": "2D", "takes_room": False, "ducks": None}}
PROMPTS = {"cue": "SFX-G-HIT", "duration_s": 0.5, "prompt_influence": 0.6,
           "prompts": ["Single short wooden knock, dry, close-up, isolated one-shot, no music",
                       "Small knuckle rap on a pine board, dry, isolated one-shot, no music"]}


def wav_bytes(ms: float, rate: int = R, seed: int = 3) -> bytes:
    """A 16-bit stereo WAV like the service's (the realistic quiet hit, cut or padded to `ms`)."""
    x = fx.make_real("quiet_hit", rate, 2, seed=seed)
    n = int(round(ms * rate / 1000))
    x = x[:n] if len(x) >= n else np.vstack([x, np.zeros((n - len(x), 2))])
    buf = io.BytesIO()
    sf.write(buf, x.astype(np.float32), rate, format="WAV", subtype="PCM_16")
    return buf.getvalue()


_MP3_CACHE: dict = {}


def mp3_bytes(ms: float) -> bytes:
    if ms not in _MP3_CACHE:
        with tempfile.TemporaryDirectory() as t:
            w, m = Path(t) / "a.wav", Path(t) / "a.mp3"
            w.write_bytes(wav_bytes(ms))
            subprocess.run([str(FOUND.path), "-hide_banner", "-nostdin", "-y", "-loglevel", "error", "-i", str(w),
                            "-c:a", "libmp3lame", "-b:a", "192k", str(m)], check=True, capture_output=True)
            _MP3_CACHE[ms] = m.read_bytes()
    return _MP3_CACHE[ms]


class FakeAPI:
    """Stands in for the HTTP layer. `script` is a list of answers used in call order; when it runs out, every call
    is answered like the real service: 200, a body in the asked format, character-cost = ceil(11 x duration)."""

    def __init__(self, script=None, cost=None, refuse=()):
        self.script = list(script or [])
        self.calls = []
        self.cost = cost  # a fixed cost per success, else the real rule
        self.refuse = set(refuse)  # formats answered 403 "output_format not allowed on your plan"

    def default(self, fmt, body):
        if fmt in self.refuse:
            return gen.Response(403, {"content-type": "application/json"}, json.dumps(
                {"detail": {"status": "output_format_not_allowed",
                            "message": f"output_format {fmt} requires a higher subscription tier"}}).encode())
        d = body.get("duration_seconds")
        if d is not None and d < 0.5:
            return gen.Response(400, {"content-type": "application/json"}, json.dumps(
                {"detail": {"status": "invalid_generation_settings", "message": "duration_seconds >= 0.5"}}).encode())
        ms = (d * 1000 - 20) if d is not None else 1000
        audio = wav_bytes(ms) if fmt.startswith("wav") else mp3_bytes(ms)
        cost = self.cost if self.cost is not None else (math.ceil(11 * d - 1e-9) if d is not None else 55)
        return gen.Response(200, {"content-type": "audio/wav" if fmt.startswith("wav") else "audio/mpeg",
                                  "character-cost": str(cost), "x-trace-id": f"trace{len(self.calls):04d}",
                                  "date": "Sat, 24 Oct 2026 03:58:15 GMT"}, audio)

    def __call__(self, url, data, headers, timeout):
        fmt = re.search(r"output_format=([a-z0-9_]+)", url).group(1)
        body = json.loads(data.decode("utf-8"))
        self.calls.append({"url": url, "body": body, "headers": dict(headers), "format": fmt})
        if self.script:
            ans = self.script.pop(0)
            if isinstance(ans, Exception):
                raise ans
            if ans is not None:
                return ans(fmt, body) if callable(ans) else ans
        return self.default(fmt, body)


def stub_decode(take, requested_ms=None):
    """Stands in for intake when a test is about the money or the files, not the audio."""
    side = take.with_suffix(".json")
    doc = json.loads(side.read_text(encoding="utf-8"))
    doc["intake"] = {"stub": True, "requested_ms": requested_ms}
    side.write_text(json.dumps(doc), encoding="utf-8")
    return doc["intake"]


class Base(unittest.TestCase):
    def setUp(self):
        self._t = tempfile.TemporaryDirectory()
        self.d = Path(self._t.name)
        self.waits = []

    def tearDown(self):
        self._t.cleanup()

    def cue(self, card=None, prompts=None):
        card = card or CARD
        cue = self.d / card["cue"]
        cue.mkdir(parents=True, exist_ok=True)
        (cue / "card.json").write_text(json.dumps(card), encoding="utf-8")
        (cue / "prompts.json").write_text(json.dumps(prompts or PROMPTS), encoding="utf-8")
        return cue

    def run_gen(self, cue, api, budget=gen.DEFAULT_BUDGET, decode=stub_decode, env=ENV, **kw):
        return gen.generate(cue, budget, send=api, sleep=self.waits.append, env=env, decode=decode, **kw)

    def takes(self, cue, pattern="*"):
        return sorted(p.name for p in (cue / "takes").glob(pattern) if p.suffix in (".wav", ".mp3")
                      and not p.name.endswith(".master.wav"))

    def side(self, cue, name):
        return json.loads((cue / "takes" / name).with_suffix(".json").read_text(encoding="utf-8"))

    def all_text(self):
        out = []
        for p in self.d.rglob("*"):
            if p.is_file():
                out.append(p.read_bytes().decode("latin-1"))
        return "\n".join(out)


# ---------------------------------------------------------------------------------------------- a normal round
class RoundTest(Base):
    def test_minor_round_writes_three_takes_with_full_sidecars(self):
        cue, api = self.cue(), FakeAPI()
        doc, code = self.run_gen(cue, api)
        self.assertEqual(code, 0)
        self.assertEqual(len(api.calls), 3)  # J020-D9: minor 3
        self.assertEqual(self.takes(cue), [f"SFX-G-HIT.r1.t{i}.wav" for i in (1, 2, 3)])
        for i, call in enumerate(api.calls, 1):
            self.assertEqual(call["url"], "https://api.elevenlabs.io/v1/sound-generation?output_format=wav_44100")
            self.assertEqual(call["headers"]["xi-api-key"], KEY)
            self.assertEqual(call["body"], {"text": PROMPTS["prompts"][(i - 1) % 2], "model_id": "eleven_text_to_sound_v2",
                                            "duration_seconds": 0.5, "prompt_influence": 0.6, "loop": False})
            s = self.side(cue, f"SFX-G-HIT.r1.t{i}.wav")
            self.assertEqual((s["cue"], s["sound"], s["round"], s["take"]), ("SFX-G-HIT", "SFX-G-HIT", 1, i))
            self.assertEqual(s["request"], call["body"])
            self.assertEqual(s["query"], {"output_format": "wav_44100"})
            self.assertEqual(s["format_used"], "wav_44100")
            self.assertEqual(s["format_received"]["container"], "wav")
            self.assertEqual((s["format_received"]["rate"], s["format_received"]["channels"]), (R, 2))
            self.assertEqual((s["credits"], s["credits_predicted"]), (6, 6))
            self.assertEqual(s["requested_ms"], 500.0)
            self.assertEqual(s["response"]["headers"]["x-trace-id"], f"trace{i:04d}")  # the fake counts from 1
            self.assertEqual(s["sha256"], file_sha256(cue / "takes" / f"SFX-G-HIT.r1.t{i}.wav"))
            self.assertRegex(s["generated"], r"^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
            self.assertEqual(s["intake"]["requested_ms"], 500.0)  # decoded once, with the requested length
        self.assertEqual(doc["spent_credits"], 18)
        self.assertEqual(doc["predicted_credits"], 18)
        log = json.loads(Path(doc["log"]).read_text(encoding="utf-8"))
        self.assertEqual(log["spent_credits"], 18)
        self.assertEqual(len(log["takes"]), 3)

    def test_takes_per_round_follow_the_tier(self):
        for tier, n in (("minor", 3), ("frequent", 4), ("important", 6)):
            with self.subTest(tier=tier):
                card = dict(CARD, cue=f"SFX-{tier.upper()}", tier=tier)
                cue = self.cue(card, dict(PROMPTS, cue=card["cue"]))
                api = FakeAPI()
                doc, code = self.run_gen(cue, api)
                self.assertEqual((code, len(api.calls), len(self.takes(cue))), (0, n, n))
                self.assertEqual(doc["warnings"], [])

    def test_a_take_count_off_the_tier_is_a_warning(self):
        cue, api = self.cue(prompts=dict(PROMPTS, takes=2)), FakeAPI()
        doc, code = self.run_gen(cue, api)
        self.assertEqual((code, len(api.calls)), (0, 2))
        self.assertTrue(any("J020-D9" in w for w in doc["warnings"]), doc["warnings"])

    def test_layers_of_an_important_cue_one_prompt_each(self):
        card = dict(CARD, cue="SFX-BOSS", tier="important")
        prompts = {"cue": "SFX-BOSS", "duration_s": 1.0,
                   "layers": [{"name": "body", "prompts": ["Deep stone slab thud, dry, isolated one-shot"]},
                              {"name": "crack", "prompts": ["Sharp dry rock crack, isolated one-shot"],
                               "duration_s": 0.5, "prompt_influence": 0.7}]}
        cue, api = self.cue(card, prompts), FakeAPI()
        doc, code = self.run_gen(cue, api)
        self.assertEqual(code, 0)
        self.assertEqual(self.takes(cue, "SFX-BOSS.body.*"), [f"SFX-BOSS.body.r1.t{i}.wav" for i in range(1, 7)])
        self.assertEqual(self.takes(cue, "SFX-BOSS.crack.*"), [f"SFX-BOSS.crack.r1.t{i}.wav" for i in range(1, 7)])
        self.assertEqual([c["body"]["text"] for c in api.calls[:6]], [prompts["layers"][0]["prompts"][0]] * 6)
        self.assertEqual([c["body"]["text"] for c in api.calls[6:]], [prompts["layers"][1]["prompts"][0]] * 6)
        self.assertEqual({c["body"]["duration_seconds"] for c in api.calls[6:]}, {0.5})
        s = self.side(cue, "SFX-BOSS.crack.r1.t1.wav")
        self.assertEqual((s["sound"], s["layer"], s["request"]["prompt_influence"]), ("SFX-BOSS.crack", "crack", 0.7))
        self.assertEqual(doc["spent_credits"], 6 * 11 + 6 * 6)

    def test_no_duration_lets_the_service_choose_and_predicts_the_flat_cost(self):
        p = {k: v for k, v in PROMPTS.items() if k != "duration_s"}
        cue, api = self.cue(prompts=p), FakeAPI()
        doc, code = self.run_gen(cue, api)
        self.assertEqual(code, 0)
        self.assertNotIn("duration_seconds", api.calls[0]["body"])
        s = self.side(cue, "SFX-G-HIT.r1.t1.wav")
        self.assertIsNone(s["requested_ms"])
        self.assertEqual((s["credits"], s["credits_predicted"]), (55, gen.CREDITS_NO_DURATION))

    def test_dry_run_calls_nothing_and_needs_no_key(self):
        cue, api = self.cue(), FakeAPI()
        doc, code = self.run_gen(cue, api, env={}, dry_run=True)
        self.assertEqual((code, len(api.calls), self.takes(cue) if (cue / "takes").exists() else []), (0, 0, []))
        self.assertEqual(doc["predicted_credits"], 18)
        self.assertEqual(len(doc["plan"]), 3)


# ---------------------------------------------------------------------------------------------- rounds (J020-D7)
class RoundsTest(Base):
    def test_next_round_gets_new_files_and_old_takes_never_change(self):
        cue = self.cue()
        self.run_gen(cue, FakeAPI())
        before = {n: file_sha256(cue / "takes" / n) for n in self.takes(cue)}
        doc, code = self.run_gen(cue, FakeAPI())
        self.assertEqual(code, 0)
        self.assertEqual(self.takes(cue, "*.r2.*"), [f"SFX-G-HIT.r2.t{i}.wav" for i in (1, 2, 3)])
        self.assertEqual({n: file_sha256(cue / "takes" / n) for n in before}, before)
        self.assertEqual(doc["sounds"][0]["round"], 2)

    def test_round_four_is_refused_before_any_call(self):
        cue = self.cue()
        for _ in range(3):
            self.assertEqual(self.run_gen(cue, FakeAPI())[1], 0)
        api = FakeAPI()
        with self.assertRaisesRegex(SoundbenchError, "J020-D7"):
            self.run_gen(cue, api)
        self.assertEqual(len(api.calls), 0)
        self.assertEqual(self.takes(cue, "*.r4.*"), [])

    def test_a_rejected_take_still_uses_its_round(self):
        cue = self.cue()
        (cue / "takes" / "rejected").mkdir(parents=True)
        for k in (1, 2, 3):
            (cue / "takes" / "rejected" / f"SFX-G-HIT.r{k}.t1.bin").write_bytes(b"x")
        api = FakeAPI()
        with self.assertRaisesRegex(SoundbenchError, "J020-D7"):
            self.run_gen(cue, api)
        self.assertEqual(len(api.calls), 0)

    def test_an_existing_file_at_a_take_path_is_refused_before_spending(self):
        cue = self.cue()
        (cue / "takes").mkdir()
        (cue / "takes" / "SFX-G-HIT.r1.t2.master.wav").write_bytes(b"orphan")
        api = FakeAPI()
        with self.assertRaisesRegex(SoundbenchError, "never overwritten"):
            self.run_gen(cue, api)
        self.assertEqual(len(api.calls), 0)


# ---------------------------------------------------------------------------------------------- the budget
class BudgetTest(Base):
    def test_a_round_predicted_over_the_budget_is_refused_before_any_call(self):
        cue, api = self.cue(), FakeAPI()
        with self.assertRaisesRegex(SoundbenchError, "budget"):
            self.run_gen(cue, api, budget=17)  # 3 x 6 = 18 predicted
        self.assertEqual(len(api.calls), 0)

    def test_stops_before_the_call_that_would_pass_the_budget(self):
        cue, api = self.cue(), FakeAPI(cost=8)  # each take costs 8, predicted 6
        doc, code = self.run_gen(cue, api, budget=20)
        # take 1: 0 + 6 <= 20, spent 8; take 2: 8 + 6 <= 20, spent 16; take 3: 16 + 6 > 20 -> stop
        self.assertEqual((code, len(api.calls), doc["spent_credits"]), (1, 2, 16))
        self.assertIn("budget", doc["stopped"])
        self.assertEqual(len(self.takes(cue)), 2)

    def test_budget_exactly_met_is_allowed(self):
        cue, api = self.cue(), FakeAPI()
        doc, code = self.run_gen(cue, api, budget=18)
        self.assertEqual((code, len(api.calls), doc["spent_credits"]), (0, 3, 18))

    def test_bad_budget_and_bad_prompt_values_are_refused(self):
        cue = self.cue()
        for b in (0, -5, float("nan"), True):
            with self.subTest(budget=b), self.assertRaises(SoundbenchError):
                self.run_gen(cue, FakeAPI(), budget=b)
        for change in ({"duration_s": 0.1}, {"duration_s": 31}, {"prompt_influence": 1.5}, {"model": "v9"},
                       {"prompts": []}, {"prompts": [""]}, {"extra": 1}, {"cue": "OTHER"}, {"takes": 0},
                       {"loop": "yes"}, {"layers": [{"name": "a", "prompts": ["x"]}]}):
            with self.subTest(change=change):
                cue = self.cue(prompts=dict(PROMPTS, **change))
                api = FakeAPI()
                with self.assertRaises(SoundbenchError):
                    self.run_gen(cue, api)
                self.assertEqual(len(api.calls), 0)


# ---------------------------------------------------------------------------------------------- formats
class FormatTest(Base):
    @needs_lame
    def test_wav_refused_falls_back_to_mp3_192_and_remembers(self):
        cue, api = self.cue(), FakeAPI(refuse={"wav_44100"})
        doc, code = self.run_gen(cue, api)
        self.assertEqual(code, 0)
        self.assertEqual([c["format"] for c in api.calls], ["wav_44100", "mp3_44100_192", "mp3_44100_192",
                                                            "mp3_44100_192"])
        self.assertEqual(self.takes(cue), [f"SFX-G-HIT.r1.t{i}.mp3" for i in (1, 2, 3)])
        s = self.side(cue, "SFX-G-HIT.r1.t1.mp3")
        self.assertEqual((s["format_used"], s["formats_refused"]), ("mp3_44100_192", ["wav_44100"]))
        self.assertEqual(s["format_received"]["container"], "mp3")
        self.assertEqual(doc["formats_refused"], ["wav_44100"])

    @needs_lame
    def test_both_refused_falls_back_to_mp3_128(self):
        cue, api = self.cue(), FakeAPI(refuse={"wav_44100", "mp3_44100_192"})
        doc, code = self.run_gen(cue, api)
        self.assertEqual(code, 0)
        self.assertEqual([c["format"] for c in api.calls[:3]], ["wav_44100", "mp3_44100_192", "mp3_44100_128"])
        self.assertEqual(self.side(cue, "SFX-G-HIT.r1.t3.mp3")["format_used"], "mp3_44100_128")

    def test_every_format_refused_stops_with_no_take(self):
        cue, api = self.cue(), FakeAPI(refuse=set(gen.FORMATS))
        doc, code = self.run_gen(cue, api)
        self.assertEqual((code, len(api.calls), self.takes(cue) if (cue / "takes").exists() else []), (2, 3, []))
        self.assertIn("refused", doc["stopped"])

    def test_an_auth_error_is_not_a_format_refusal(self):
        """The real answer to a key ID used as a key (2026-10-24): 400 authentication_error, no format named."""
        ans = gen.Response(400, {}, json.dumps({"detail": {"type": "authentication_error", "code": "invalid_api_key",
                                                           "message": "API key ID used as API key"}}).encode())
        cue, api = self.cue(), FakeAPI(script=[ans])
        doc, code = self.run_gen(cue, api)
        self.assertEqual((code, len(api.calls)), (2, 1))
        self.assertIn("400", doc["stopped"])
        self.assertIn("environment", doc["stopped"])  # names that a Windows variable wins over keys.json

    def test_received_bytes_decide_the_extension(self):
        """Asked for WAV, got MP3 bytes: saved as .mp3, logged as a mismatch."""
        if not HAS_LAME:
            self.skipTest("needs libmp3lame")
        mp3 = gen.Response(200, {"character-cost": "6", "content-type": "audio/mpeg"}, mp3_bytes(480))
        cue, api = self.cue(), FakeAPI(script=[mp3])
        doc, code = self.run_gen(cue, api)
        self.assertEqual(self.takes(cue)[0], "SFX-G-HIT.r1.t1.mp3")
        self.assertTrue(any("asked wav_44100" in w for w in doc["warnings"]), doc["warnings"])

    def test_unreadable_bytes_go_to_rejected_with_their_cost(self):
        bad = gen.Response(200, {"character-cost": "6", "content-type": "audio/wav"}, b"not audio at all")
        cue, api = self.cue(), FakeAPI(script=[bad])
        doc, code = self.run_gen(cue, api)
        self.assertEqual(code, 1)
        self.assertTrue((cue / "takes" / "rejected" / "SFX-G-HIT.r1.t1.bin").is_file())
        rej = json.loads((cue / "takes" / "rejected" / "SFX-G-HIT.r1.t1.json").read_text(encoding="utf-8"))
        self.assertEqual(rej["credits"], 6)
        self.assertIn("rejected", rej)
        self.assertEqual(doc["spent_credits"], 18)


# ---------------------------------------------------------------------------------------------- errors and retries
class RetryTest(Base):
    def test_429_then_success_waits_and_logs_the_attempt(self):
        r429 = gen.Response(429, {"retry-after": "3"}, b'{"detail":{"status":"too_many_concurrent_requests"}}')
        cue, api = self.cue(), FakeAPI(script=[r429])
        doc, code = self.run_gen(cue, api)
        self.assertEqual((code, len(api.calls)), (0, 4))
        self.assertEqual(self.waits[0], 3.0)  # Retry-After honoured
        s = self.side(cue, "SFX-G-HIT.r1.t1.wav")
        self.assertEqual([a["status"] for a in s["attempts"]], [429, 200])
        self.assertEqual(s["attempts"][0]["charged"], "no")
        self.assertEqual(doc["spent_credits"], 18)

    def test_server_errors_retry_a_bounded_number_of_times_and_write_no_take(self):
        r500 = gen.Response(500, {}, b'{"detail":"internal"}')
        cue, api = self.cue(), FakeAPI(script=[r500] * gen.MAX_ATTEMPTS)
        doc, code = self.run_gen(cue, api)
        self.assertEqual((code, len(api.calls)), (2, gen.MAX_ATTEMPTS))
        self.assertEqual(self.takes(cue) if (cue / "takes").exists() else [], [])
        self.assertIn("500", doc["stopped"])
        self.assertEqual(len(self.waits), gen.MAX_ATTEMPTS - 1)
        self.assertEqual([a["status"] for a in doc["failed"][0]["attempts"]], [500] * gen.MAX_ATTEMPTS)

    def test_a_charged_error_is_counted_and_logged_before_the_retry(self):
        r500 = gen.Response(500, {"character-cost": "6"}, b'{"detail":"internal"}')
        cue, api = self.cue(), FakeAPI(script=[r500])
        doc, code = self.run_gen(cue, api)
        self.assertEqual((code, len(api.calls)), (0, 4))
        s = self.side(cue, "SFX-G-HIT.r1.t1.wav")
        self.assertEqual([(a["status"], a["charged"], a["credits"]) for a in s["attempts"]],
                         [(500, "yes", 6), (200, "yes", 6)])
        self.assertEqual(doc["spent_credits"], 24)  # the take cost twice and both are counted

    def test_a_network_failure_counts_as_possibly_charged(self):
        cue, api = self.cue(), FakeAPI(script=[gen.NetworkError("timed out after the request was sent")])
        doc, code = self.run_gen(cue, api)
        self.assertEqual((code, len(api.calls)), (0, 4))
        s = self.side(cue, "SFX-G-HIT.r1.t1.wav")
        self.assertEqual([a["charged"] for a in s["attempts"]], ["unknown", "yes"])
        self.assertEqual(s["attempts"][0]["counted_credits"], 6)
        self.assertEqual((doc["spent_credits"], doc["possibly_spent_credits"]), (18, 6))

    def test_possible_spend_counts_against_the_budget(self):
        cue, api = self.cue(), FakeAPI(script=[gen.NetworkError("reset")] * 2)
        doc, code = self.run_gen(cue, api, budget=20)
        # attempt 1: 0+6 ok (unknown, 6 counted); attempt 2: 6+6 ok (unknown, 12); attempt 3: 12+6 ok -> 200 (18);
        # take 2: 18 + 6 > 20 -> stop before the call
        self.assertEqual((code, len(api.calls)), (1, 3))
        self.assertEqual((doc["spent_credits"], doc["possibly_spent_credits"]), (6, 12))

    def test_one_success_is_exactly_one_call(self):
        cue, api = self.cue(), FakeAPI()
        self.run_gen(cue, api)
        self.assertEqual(len(api.calls), 3)
        for n in self.takes(cue):
            self.assertEqual(len(self.side(cue, n)["attempts"]), 1)

    def test_missing_key_is_refused_before_any_call(self):
        cue, api = self.cue(), FakeAPI()
        with self.assertRaisesRegex(SoundbenchError, "keys.py run --only ELEVENLABS_API_KEY"):
            self.run_gen(cue, api, env={"ELEVENLABS_API_KEY": "  "})
        self.assertEqual(len(api.calls), 0)


# ---------------------------------------------------------------------------------------------- the key never leaks
class SecretTest(Base):
    def leaky_api(self):
        """A hostile service: the key echoed in an error body, a success header and a network error."""
        echo_err = gen.Response(500, {"x-echo": KEY}, json.dumps({"detail": f"bad key {KEY}"}).encode())
        net = gen.NetworkError(f"connection reset (header xi-api-key: {KEY})")

        def ok(fmt, body):
            r = FakeAPI().default(fmt, body)
            r.headers["x-echo"] = KEY
            r.headers["x-trace-id"] = KEY
            return r

        auth = gen.Response(401, {"x-echo": KEY}, json.dumps({"detail": {"message": f"invalid key {KEY}"}}).encode())
        return FakeAPI(script=[echo_err, net, ok, ok, auth])

    def test_no_key_like_value_reaches_any_output(self):
        cue = self.cue()
        out, err = io.StringIO(), io.StringIO()
        with mock.patch.object(gen, "urllib_send", self.leaky_api()), mock.patch.object(gen.time, "sleep"), \
                mock.patch.dict("os.environ", ENV), contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = cli.main(["generate", str(cue), "--json"])
        self.assertEqual(code, 2)  # stopped at the 401 on take 3
        text = self.all_text() + out.getvalue() + err.getvalue()
        self.assertIn("SFX-G-HIT.r1.t1", text)  # the outputs exist and were scanned
        self.assertNotIn(KEY, text)
        self.assertEqual(KEY_LIKE.findall(text), [])
        self.assertIn("<redacted>", text)  # the echoes were seen and replaced, not dropped silently
        sides = "".join(p.read_text(encoding="utf-8") for p in (cue / "takes").glob("*.json"))
        self.assertIn('"x-trace-id"', sides)
        self.assertNotIn("x-echo", sides)  # a sidecar keeps only the named trace headers, never what else came back

    def test_the_key_is_sent_only_in_its_header(self):
        cue, api = self.cue(), FakeAPI()
        self.run_gen(cue, api)
        for c in api.calls:
            self.assertNotIn(KEY, c["url"])
            self.assertNotIn(KEY, json.dumps(c["body"]))
            self.assertEqual([k for k, v in c["headers"].items() if v == KEY], ["xi-api-key"])

    def test_error_messages_are_redacted(self):
        self.assertEqual(gen.redact(f"a {KEY} b", KEY), "a <redacted> b")
        self.assertEqual(gen.redact("token sk_" + "ab" * 12, KEY), "token <redacted>")


# ---------------------------------------------------------------------------------------------- real decode and rank
@needs_ffmpeg
class IntakeAndRankTest(Base):
    def test_intake_decodes_a_service_wav_that_states_no_start_time(self):
        """ffprobe 9.0.2 states no start_time for a PCM WAV (real take p01, 2026-10-24); intake must still decode it
        and check its length against the stated one."""
        take = self.d / "x.r1.t1.wav"
        take.write_bytes(wav_bytes(480))
        info = intake.decode_take(take, requested_ms=500)
        self.assertEqual((info["codec"], info["rate"], info["channels"], info["samples"]), ("pcm_s16le", R, 2, 21168))
        self.assertEqual(info["decoded_ms"], 480.0)
        self.assertEqual(len(info["warnings"]), 1)  # 480 for 500: logged, never refused

    def test_generate_decodes_every_take_once_and_rank_takes_over(self):
        cue, api = self.cue(), FakeAPI()
        doc, code = self.run_gen(cue, api, decode=None)
        self.assertEqual(code, 0)
        for n in self.takes(cue):
            s = self.side(cue, n)
            self.assertEqual(s["intake"]["take_sha256"], s["sha256"])
            self.assertEqual((s["intake"]["decoded_ms"], s["intake"]["requested_ms"]), (480.0, 500.0))
            self.assertTrue(intake.master_path(cue / "takes" / n).is_file())
        rdoc, rcode = rank.rank(cue)
        self.assertIn(rcode, (0, 1))
        self.assertEqual(rdoc["takes_found"], 3)
        self.assertEqual(sorted(rdoc["order"]), [f"SFX-G-HIT.r1.t{i}.wav" for i in (1, 2, 3)])
        self.assertEqual(rdoc["warnings"], [])
        from tools.audio.soundbench import render
        recipe = {"cue": "SFX-G-HIT", "take": "takes/SFX-G-HIT.r1.t2.wav", "design": [],
                  "edit": [{"op": "trim"}, {"op": "loudness"}, {"op": "peak"}]}
        (cue / "recipe.json").write_text(json.dumps(recipe), encoding="utf-8")
        rend, rc = render.render(cue)
        self.assertIn(rc, (0, 1))
        self.assertTrue((cue / "out" / "SFX-G-HIT.flac").is_file())
        self.assertEqual(rend["take"]["take"], "SFX-G-HIT.r1.t2.wav")

    def test_an_intake_refusal_moves_the_take_to_rejected(self):
        with mock.patch.object(intake, "decode_take", side_effect=SoundbenchError("decoded length differs")):
            cue, api = self.cue(), FakeAPI()
            doc, code = self.run_gen(cue, api, decode=None)
        self.assertEqual(code, 1)
        self.assertEqual(self.takes(cue), [])
        self.assertEqual(sorted(p.name for p in (cue / "takes" / "rejected").glob("*.wav")),
                         [f"SFX-G-HIT.r1.t{i}.wav" for i in (1, 2, 3)])
        self.assertEqual(doc["spent_credits"], 18)


# ---------------------------------------------------------------------------------------------- live (never in the gate)
LIVE = os.environ.get("SOUNDBENCH_LIVE_GENERATE") == "1" and bool(os.environ.get("ELEVENLABS_API_KEY", "").strip())


@unittest.skipUnless(LIVE and FOUND, "live ElevenLabs check: set SOUNDBENCH_LIVE_GENERATE=1 and run through "
                     "`python tools/keys.py run --only ELEVENLABS_API_KEY -- ...` (spends about 18 credits)")
class LiveTest(Base):
    def test_one_real_minor_round(self):
        cue = self.cue(dict(CARD, cue="SFX-LIVE"), dict(PROMPTS, cue="SFX-LIVE"))
        doc, code = gen.generate(cue, 20)
        self.assertEqual(code, 0, doc.get("stopped"))
        self.assertEqual(len(doc["takes"]), 3)
        for t in doc["takes"]:
            s = json.loads(Path(t["file"]).with_suffix(".json").read_text(encoding="utf-8"))
            self.assertEqual(s["credits"], s["credits_predicted"])
            self.assertEqual(s["intake"]["take_sha256"], s["sha256"])
            self.assertIn("x-trace-id", s["response"]["headers"])
        key = os.environ["ELEVENLABS_API_KEY"].strip()
        self.assertNotIn(key, self.all_text())
        self.assertEqual(KEY_LIKE.findall(self.all_text()), [])
        print(f"\nlive: spent {doc['spent_credits']} credits, formats {[t['format_used'] for t in doc['takes']]}")


# ---------------------------------------------------------------------------------------------- planted faults
def _fault_budget_off():
    return mock.patch.object(gen, "budget_allows", lambda spent, predicted, budget: True)


def _fault_round_four():
    return mock.patch.object(gen, "MAX_ROUNDS", 4)


def _fault_key_in_sidecar():
    return mock.patch.object(gen, "trace_headers", lambda h: dict(h))


def _fault_no_redaction():
    return mock.patch.object(gen, "redact", lambda text, key: text)


def _fault_fallback_skipped():
    return mock.patch.object(gen, "format_refused", lambda resp, fmt: False)


def _fault_charged_error_not_counted():
    real = gen.attempt_record

    def fake(status, headers, predicted, error=None):
        rec = real(status, headers, predicted, error)
        if status not in (None, 200):
            rec.update(charged="no", credits=0, counted_credits=0)
        return rec
    return mock.patch.object(gen, "attempt_record", fake)


def _fault_network_not_counted():
    real = gen.attempt_record

    def fake(status, headers, predicted, error=None):
        rec = real(status, headers, predicted, error)
        if status is None:
            rec.update(charged="no", counted_credits=0)
        return rec
    return mock.patch.object(gen, "attempt_record", fake)


FAULTS = {
    "budget check off": (_fault_budget_off, [(BudgetTest, "test_a_round_predicted_over_the_budget_is_refused_before_any_call"),
                                             (BudgetTest, "test_stops_before_the_call_that_would_pass_the_budget")]),
    "round 4 allowed": (_fault_round_four, [(RoundsTest, "test_round_four_is_refused_before_any_call")]),
    "key leaked into the sidecar": (_fault_key_in_sidecar, [(SecretTest, "test_no_key_like_value_reaches_any_output")]),
    "redaction off": (_fault_no_redaction, [(SecretTest, "test_no_key_like_value_reaches_any_output"),
                                            (SecretTest, "test_error_messages_are_redacted")]),
    "format fallback skipped": (_fault_fallback_skipped, [(FormatTest, "test_every_format_refused_stops_with_no_take")]
                                + ([(FormatTest, "test_wav_refused_falls_back_to_mp3_192_and_remembers")]
                                   if HAS_LAME else [])),
    "retries spend twice unlogged (charged error)": (_fault_charged_error_not_counted, [
        (RetryTest, "test_a_charged_error_is_counted_and_logged_before_the_retry")]),
    "retries spend twice unlogged (network)": (_fault_network_not_counted, [
        (RetryTest, "test_a_network_failure_counts_as_possibly_charged"),
        (RetryTest, "test_possible_spend_counts_against_the_budget")]),
}


class PlantedFaultTest(unittest.TestCase):
    """Each planted fault must make at least one of its named tests FAIL (an assertion, not an error)."""

    def test_every_planted_fault_is_caught(self):
        survived, errored = [], []
        for name, (patcher, tests) in FAULTS.items():
            suite = unittest.TestSuite(cls(t) for cls, t in tests)
            with patcher():
                res = unittest.TextTestRunner(stream=io.StringIO(), verbosity=0).run(suite)
            if not res.failures:
                survived.append(name)
            if res.errors:
                errored.append((name, [str(e[0]) for e in res.errors]))
        self.assertEqual(survived, [], "planted faults that survived")
        self.assertEqual(errored, [], "planted faults that errored instead of failing")

    def test_the_correct_build_passes_the_fault_tests(self):
        tests = {(cls, t) for _, ts in FAULTS.values() for cls, t in ts}
        res = unittest.TextTestRunner(stream=io.StringIO(), verbosity=0).run(
            unittest.TestSuite(cls(t) for cls, t in sorted(tests, key=lambda p: p[1])))
        self.assertTrue(res.wasSuccessful(), res.failures + res.errors)


if __name__ == "__main__":
    unittest.main()
