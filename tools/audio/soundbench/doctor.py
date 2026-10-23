"""`doctor`: is this machine ready for soundbench? Pass, or the missing items.

Kit tool (universal). Author: feature-builder · claude-opus-5-5 · high · 2026-10-23 (J020 step 1-2)

Checks: Python 3.11+; numpy, scipy, soundfile (with FLAC), pyloudnorm, matplotlib (Agg); ffmpeg found (and how),
its version (tested on 9.0.2: another version is a warning), the filters design section 4 uses, the MP3 decoder for
intake; a live G-7 self-test (afftdn's lag measured and compensated to 0 on a fixture); the `ELEVENLABS_API_KEY`
entry in `knowledge/design/keys.json` with a path set and a file at that path. The key file is only checked to
exist (a stat call): it is never opened, read, printed or logged (AGENTS.md section 3 item 4).

Usage:
  python -m tools.audio.soundbench doctor [--root DIR] [--json]
"""

from __future__ import annotations

import importlib
import importlib.metadata
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FILTERS = ("afftdn", "adeclick", "rubberband", "chorus")  # design section 4 (anlmdn excluded: it crashed)
KEY_ENV = "ELEVENLABS_API_KEY"
LIBS = ("numpy", "scipy", "soundfile", "pyloudnorm", "matplotlib")


def checks(root: Path = ROOT) -> list[dict]:
    rows: list[dict] = []

    def add(name: str, status: str, detail: str) -> None:
        rows.append({"check": name, "status": status, "detail": detail})

    ok_py = sys.version_info >= (3, 11)
    add("python", "PASS" if ok_py else "FAIL", sys.version.split()[0] + ("" if ok_py else " (needs 3.11+)"))
    libs_ok = True
    for lib in LIBS:
        try:
            mod = importlib.import_module(lib)
            add(f"lib {lib}", "PASS", getattr(mod, "__version__", None) or importlib.metadata.version(lib))
        except ImportError:
            libs_ok = False
            add(f"lib {lib}", "FAIL", "missing: pip install " + lib)
    if libs_ok:
        import soundfile as sf

        has_flac = "FLAC" in sf.available_formats()
        add("libsndfile FLAC", "PASS" if has_flac else "FAIL", f"libsndfile {sf.__libsndfile_version__}")
        try:
            import matplotlib.backends.backend_agg  # noqa: F401
            add("matplotlib Agg", "PASS", "Agg canvas available")
        except ImportError as err:
            add("matplotlib Agg", "FAIL", str(err))

    from . import ffmpeg
    from .core import SoundbenchError

    try:
        loc = ffmpeg.find_ffmpeg()
    except SoundbenchError as err:
        loc = None
        add("ffmpeg found", "FAIL", str(err))
    else:
        add("ffmpeg found", "PASS" if loc else "FAIL",
            f"{loc.path} (via {loc.how})" if loc else f"not found: set {ffmpeg.ENV_VAR}, PATH, or winget install Gyan.FFmpeg")
    if loc:
        try:
            ver = ffmpeg.version(loc.path)
            add("ffmpeg version", "PASS" if ver == ffmpeg.TESTED_VERSION else "WARN",
                ver + ("" if ver == ffmpeg.TESTED_VERSION else f" (tested on {ffmpeg.TESTED_VERSION}: re-run the tests)"))
            have = ffmpeg.filters(loc.path)
            missing = [f for f in FILTERS if f not in have]
            add("ffmpeg filters", "FAIL" if missing else "PASS",
                ("missing: " + ", ".join(missing)) if missing else ", ".join(FILTERS))
            dec = ffmpeg.decoders(loc.path)
            add("ffmpeg mp3 decoder", "PASS" if {"mp3float", "mp3"} & dec else "FAIL",
                "mp3float" if "mp3float" in dec else ("mp3" if "mp3" in dec else "missing"))
            enc = ffmpeg.encoders(loc.path)
            add("ffmpeg mp3 encoder (tests only)", "PASS" if "libmp3lame" in enc else "WARN",
                "libmp3lame" if "libmp3lame" in enc else "missing: the MP3 round-trip tests skip")
            if libs_ok and not missing:
                add("G-7 self-test", *_self_test(loc.path))
        except SoundbenchError as err:
            add("ffmpeg run", "FAIL", str(err))

    add("keys.json " + KEY_ENV, *_key_entry(root))
    return rows


def _self_test(exe: Path) -> tuple[str, str]:
    import numpy as np

    from . import ffmpeg, fixtures, measures
    from .core import SoundbenchError

    rate = 44100
    x = fixtures.make("clean_hit", rate, 2).astype(np.float32)
    x += (np.random.RandomState(3).standard_normal(x.shape) * 0.003).astype(np.float32)
    try:
        res = ffmpeg.run_filter(x, rate, "afftdn", max_lag_ms=50, exe=exe)
    except SoundbenchError as err:
        return "FAIL", str(err)
    after = measures.lag(x, res.audio, rate, rate // 10)["lag_samples"]
    ok = after == 0 and res.audio.shape == x.shape
    return ("PASS" if ok else "FAIL",
            f"afftdn lag {res.lag_samples} samples ({1000 * res.lag_samples / rate:.1f} ms) compensated to {after}")


def _key_entry(root: Path) -> tuple[str, str]:
    path = root / "knowledge" / "design" / "keys.json"
    if not path.is_file():
        return "FAIL", f"no {path}"
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as err:
        return "FAIL", f"cannot read keys.json: {err}"
    entry = next((k for k in doc.get("keys", []) if isinstance(k, dict) and k.get("env") == KEY_ENV), None)
    if entry is None:
        return "FAIL", f"no {KEY_ENV} entry"
    key_path = str(entry.get("path") or "").strip()
    if not key_path:
        return "FAIL", f"{KEY_ENV} entry has no path (the owner fills it)"
    if not Path(key_path).is_file():  # existence only: the file is never opened
        return "FAIL", f"{KEY_ENV} entry set, but no file at its path"
    return "PASS", "entry present, path set, key file present (not opened)"


def main(root: Path = ROOT, as_json: bool = False) -> int:
    rows = checks(root)
    failed = any(r["status"] == "FAIL" for r in rows)
    if as_json:
        print(json.dumps({"rows": rows, "result": "FAIL" if failed else "PASS"}, indent=2))
    else:
        for r in rows:
            print(f"{r['status']:<4} {r['check']}: {r['detail']}")
        print(f"RESULT: {'FAIL' if failed else 'PASS'}")
    return 1 if failed else 0
