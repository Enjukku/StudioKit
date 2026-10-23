"""The cue card (`card.json`) and the recipe (`recipe.json`): load, check, and map targets to measures.

Kit tool (universal). Author: feature-builder · claude-opus-5-5 · high · 2026-10-23 (J020 step 3)

Design: `editor-design.md` sections 2, 4 and 7. Every field is checked when the file is read: an unknown key, a wrong
type, a NaN or a min above its max is an error naming the field (a typo must never drop a target silently). Kinds and
scales come from `tables.json`. Playback fields (2D/3D, falloff, takes_room, ducks) are stored and passed through to
the log; the editor does not act on them (they are played in Roblox, J020-D8, D10, D11).

card.json:
  {"cue": "SFX-COMBAT-HIT", "kind": "hit", "category": "sfx", "tier": "minor",
   "level": {"measure": "F-09", "target": -12.0, "tolerance": 1.0, "must": true},
   "targets": {"onset_ms": {"max": 3, "must": true}, "true_peak_dbtp": {"max": -1.0, "must": true},
               "sound_ms": {"min": 150, "max": 400, "must": false}, ...},
   "key": {"root": "A", "scale": "major"},                                  (optional)
   "form": {"loop": false, "mono": false, "variants": 0},                   (optional)
   "family": {"id": "egg-reveal", "paid_reveal": true, "siblings": ["SFX-EGG-RARE"]},   (optional)
   "playback": {"space": "3D", "falloff": {"mode": "inverse", "max_studs": 80}, "takes_room": true,
                "ducks": null}}
  level.measure: "F-09" (one-shots), "F-13a" (a family of siblings), "LUFS-I" (only for 0.4 s or more).
  onset_ms may name "binds_to": "F-01" or "main_transient"; otherwise the kind's binding is used.

recipe.json:
  {"cue": "SFX-COMBAT-HIT", "take": "takes/SFX-COMBAT-HIT.r1.t2.mp3",
   "design": [{"op": "highpass", "hz": 80}, {"op": "eq", "bands": [...]}, {"op": "compress", ..., "why": "..."}],
   "edit": [{"op": "trim"}, {"op": "fade", "out_ms": 20}, {"op": "loudness"}, {"op": "peak"}]}
  The edit steps run in the fixed order trim, cut, fade, mono, loudness, peak, export whatever order they are
  listed in; export always runs.

Usage:
  from tools.audio.soundbench import card
  c = card.load_card(Path("content/audio/SFX-COMBAT-HIT/card.json"))
  r = card.load_recipe(Path(".../recipe.json"))
"""

from __future__ import annotations

import json
import math
from pathlib import Path

from .core import SoundbenchError

TABLES = json.loads((Path(__file__).with_name("tables.json")).read_text(encoding="utf-8"))
KINDS: dict = TABLES["kinds"]
SCALES: dict = TABLES["scales"]
CATEGORIES = ("sfx", "ui", "music", "ambience", "voice")
TIERS = ("minor", "frequent", "important")
LEVEL_MEASURES = ("F-09", "F-13a", "LUFS-I")
NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
EDIT_ORDER = ("trim", "cut", "fade", "mono", "loudness", "peak", "export")

# target name -> the key in the flattened measure record (`render` flattens with "."); onset_ms is resolved per card
TARGETS = {
    "onset_ms": None,
    "main_transient_ms": "main_transient_ms",
    "attack_rise_ms": "attack_rise_ms",
    "attack_share_5ms": "attack_share_5ms",
    "sound_ms": "F-12_length.sound_ms",
    "file_ms": "F-12_length.file_ms",
    "true_peak_dbtp": "F-03_peaks.true_peak_dbtp",
    "sample_peak_dbfs": "F-03_peaks.sample_peak_dbfs",
    "below_120": "F-06_bands.below_120",
    "band_120_500": "F-06_bands.120_500",
    "band_500_5k": "F-06_bands.500_5k",
    "above_5k": "F-06_bands.above_5k",
    "phone_loss_db": "phone_loss_db",
    "mono_drop_db": "F-07_mono_drop_db",
    "loop_seam": "F-08_loop_seam",
    "clicks": "clicks.count",
    "edge_clicks": "clicks.edge_count",
    "tail_snr_db": "tail_noise.snr_db",
    "roughness": "roughness",
    "flatness": "tonality.flatness",
}
ONSET_KEYS = {"F-01": "F-01_onset_ms", "main_transient": "main_transient_ms"}


def _num(v, where: str) -> float:
    if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v):
        raise SoundbenchError(f"{where}: needs a finite number, got {v!r}")
    return float(v)


def _keys(obj, allowed: set[str], required: set[str], where: str) -> dict:
    if not isinstance(obj, dict):
        raise SoundbenchError(f"{where}: needs an object, got {type(obj).__name__}")
    extra = set(obj) - allowed
    if extra:
        raise SoundbenchError(f"{where}: unknown field(s) {sorted(extra)} (allowed: {sorted(allowed)})")
    missing = required - set(obj)
    if missing:
        raise SoundbenchError(f"{where}: missing field(s) {sorted(missing)}")
    return obj


def _bool(v, where: str) -> bool:
    if not isinstance(v, bool):
        raise SoundbenchError(f"{where}: needs true or false, got {v!r}")
    return v


def _choice(v, options, where: str):
    if v not in options:
        raise SoundbenchError(f"{where}: {v!r} is not one of {list(options)}")
    return v


def _cue_id(v, where: str) -> str:
    if not isinstance(v, str) or not v.strip() or any(c in v for c in '/\\:*?"<>|'):
        raise SoundbenchError(f"{where}: needs a cue id usable as a file name, got {v!r}")
    return v


def check_card(doc: dict) -> dict:
    _keys(doc, {"cue", "kind", "category", "tier", "level", "targets", "key", "form", "family", "playback", "_about"},
          {"cue", "kind", "category", "tier", "level", "playback"}, "card")
    _cue_id(doc["cue"], "card.cue")
    _choice(doc["kind"], KINDS, "card.kind")
    _choice(doc["category"], CATEGORIES, "card.category")
    _choice(doc["tier"], TIERS, "card.tier")
    lv = _keys(doc["level"], {"measure", "target", "tolerance", "must"}, {"measure", "target", "tolerance", "must"},
               "card.level")
    _choice(lv["measure"], LEVEL_MEASURES, "card.level.measure")
    _num(lv["target"], "card.level.target")
    if _num(lv["tolerance"], "card.level.tolerance") < 0:
        raise SoundbenchError("card.level.tolerance: must be 0 or more")
    _bool(lv["must"], "card.level.must")
    if not isinstance(doc.get("targets", {}), dict):
        raise SoundbenchError("card.targets: needs an object of target name -> {min, max, must}")
    for name, spec in doc.get("targets", {}).items():
        where = f"card.targets.{name}"
        if name not in TARGETS:
            raise SoundbenchError(f"{where}: unknown target (known: {sorted(TARGETS)})")
        _keys(spec, {"min", "max", "must", "binds_to"} if name == "onset_ms" else {"min", "max", "must"}, {"must"},
              where)
        _bool(spec["must"], where + ".must")
        if "min" not in spec and "max" not in spec:
            raise SoundbenchError(f"{where}: needs min, max or both")
        lo = _num(spec["min"], where + ".min") if "min" in spec else None
        hi = _num(spec["max"], where + ".max") if "max" in spec else None
        if lo is not None and hi is not None and lo > hi:
            raise SoundbenchError(f"{where}: min {lo} is above max {hi}")
        if "binds_to" in spec:
            _choice(spec["binds_to"], ONSET_KEYS, where + ".binds_to")
    if "key" in doc:
        k = _keys(doc["key"], {"root", "scale", "must"}, {"root", "scale"}, "card.key")
        _choice(k["root"], NOTE_NAMES, "card.key.root")
        _choice(k["scale"], SCALES, "card.key.scale")
        if "must" in k:
            _bool(k["must"], "card.key.must")
    if "form" in doc:
        f = _keys(doc["form"], {"loop", "mono", "variants"}, set(), "card.form")
        for b in ("loop", "mono"):
            if b in f:
                _bool(f[b], f"card.form.{b}")
        if "variants" in f and (isinstance(f["variants"], bool) or not isinstance(f["variants"], int) or f["variants"] < 0):
            raise SoundbenchError("card.form.variants: needs a whole number, 0 or more")
        if f.get("variants", 0) > 0 and KINDS[doc["kind"]]["no_variants"]:
            raise SoundbenchError(f"card.form.variants: a {doc['kind']} has no variants (SC-12: the same attack always "
                                  "has the same tell)")
    if "family" in doc:
        fam = _keys(doc["family"], {"id", "paid_reveal", "siblings"}, {"id", "paid_reveal", "siblings"}, "card.family")
        _cue_id(fam["id"], "card.family.id")
        _bool(fam["paid_reveal"], "card.family.paid_reveal")
        if not isinstance(fam["siblings"], list) or not all(isinstance(s, str) for s in fam["siblings"]):
            raise SoundbenchError("card.family.siblings: needs a list of cue ids")
        for s in fam["siblings"]:
            _cue_id(s, "card.family.siblings[]")
        if doc["cue"] in fam["siblings"]:
            raise SoundbenchError("card.family.siblings: lists the cue itself")
    pb = _keys(doc["playback"], {"space", "falloff", "takes_room", "ducks"}, {"space", "takes_room"}, "card.playback")
    _choice(pb["space"], ("2D", "3D"), "card.playback.space")
    _bool(pb["takes_room"], "card.playback.takes_room")
    if pb["space"] == "3D" and not isinstance(pb.get("falloff"), dict):
        raise SoundbenchError("card.playback.falloff: a 3D cue names its falloff (mode and range, workflow map section 6)")
    if "ducks" in pb and pb["ducks"] is not None and not isinstance(pb["ducks"], dict):
        raise SoundbenchError("card.playback.ducks: needs an object (what, how much, why) or null")
    return doc


def onset_binding(doc: dict) -> str:
    """Which onset the card's onset target and `trim` use: the target's binds_to, else the kind's."""
    spec = doc.get("targets", {}).get("onset_ms", {})
    return spec.get("binds_to", KINDS[doc["kind"]]["binds_to"])


def target_key(doc: dict, name: str) -> str:
    return ONSET_KEYS[onset_binding(doc)] if name == "onset_ms" else TARGETS[name]


def _step(step, where: str) -> dict:
    if not isinstance(step, dict) or not isinstance(step.get("op"), str):
        raise SoundbenchError(f"{where}: each step is an object with an \"op\" name")
    if "why" in step and (not isinstance(step["why"], str) or not step["why"].strip()):
        raise SoundbenchError(f"{where}.why: needs a non-empty reason")
    return step


def check_recipe(doc: dict) -> dict:
    _keys(doc, {"cue", "take", "design", "edit", "_about"}, {"cue", "take", "design", "edit"}, "recipe")
    _cue_id(doc["cue"], "recipe.cue")
    take = doc["take"]
    if not isinstance(take, str) or not take.lower().endswith(".mp3") or Path(take).is_absolute() or ".." in Path(take).parts:
        raise SoundbenchError("recipe.take: needs the take's .mp3 path inside the cue folder, e.g. takes/<cue>.r1.t1.mp3")
    for part in ("design", "edit"):
        if not isinstance(doc[part], list):
            raise SoundbenchError(f"recipe.{part}: needs a list of steps")
        for i, step in enumerate(doc[part]):
            _step(step, f"recipe.{part}[{i}]")
    names = [s["op"] for s in doc["edit"]]
    for n in names:
        if n not in EDIT_ORDER:
            raise SoundbenchError(f"recipe.edit: {n!r} is not an edit step (edit steps: {list(EDIT_ORDER)})")
    dup = {n for n in names if names.count(n) > 1}
    if dup:
        raise SoundbenchError(f"recipe.edit: {sorted(dup)} listed more than once")
    for s in doc["design"]:
        if s["op"] in EDIT_ORDER:
            raise SoundbenchError(f"recipe.design: {s['op']!r} is an edit step; it belongs in recipe.edit")
    return doc


def _read(path: Path, what: str) -> dict:
    if not Path(path).is_file():
        raise SoundbenchError(f"no {what}: {path}")
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except json.JSONDecodeError as err:
        raise SoundbenchError(f"{path}: not valid JSON ({err})") from err


def load_card(path: Path) -> dict:
    return check_card(_read(path, "card.json"))


def load_recipe(path: Path) -> dict:
    return check_recipe(_read(path, "recipe.json"))
