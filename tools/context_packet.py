#!/usr/bin/env python3
"""Context packet: rank the knowledge base for one task and print a small, cited reading list.

Kit tool (universal). Standard library only, deterministic output.

Usage:
    python tools/context_packet.py packet "<task>" [--budget 8000] [--max 12] [--json] [--root DIR]

How it ranks (spec: rules/knowledge.md §2, §3, §6):
    1. Notes under the search roots are split into heading-level sections (#, ##, ###).
    2. BM25 over sections; the heading, note title, file path and skill/workflow
       `description` count as boosted fields. Sections covering more query words win.
    3. Frontmatter `type` boost (decision/system > lesson > log), small recency boost from
       `updated` (relative to the newest note, so output never depends on today's date).
    4. `status: superseded` notes are skipped; a strong match is reported as
       "superseded, see <replacement>".
    5. 1-hop [[wiki-link]] neighbours of the top notes join with a lower score.
    6. A matched skill or role with `knowledge/overlays/<name>.md` pulls that overlay in.
    Matching rows of knowledge/design/decisions.md, AGENTS.md section headings and
    src/ file-name hints are listed separately.

Search roots: kit.json key `context.search_roots` (list of repo-relative paths) when present,
else DEFAULT_ROOTS. `context.exclude` (list) replaces DEFAULT_EXCLUDE when present.
Other tools import this module (kb_index.py, eval_context.py).
"""

from __future__ import annotations

import argparse
import datetime
import json
import math
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

DEFAULT_ROOTS = ("rules", "knowledge", ".agents/skills", ".agents/roles", ".agents/workflows")
DEFAULT_EXCLUDE = ("knowledge/generated", "knowledge/inbox/processed", "knowledge/external")
ALWAYS_FILES = ("AGENTS.md",)
DECISIONS = "knowledge/design/decisions.md"
OVERLAYS = "knowledge/overlays"
CODE_ROOTS = ("src",)
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "Packages", "ServerPackages", "DevPackages"}

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
LINK_RE = re.compile(r"\[\[([^\[\]\n]+?)\]\]")
WORD_RE = re.compile(r"[a-z0-9]+")
CAMEL_RE = re.compile(r"(?<=[a-z0-9])(?=[A-Z])")
SPLIT_LEVEL = 3  # headings at this level or above start a new section

STOP_WORDS = frozenset(
    """a about above after again all also am an and any are as at be been before being below
    between both but by can could did do does doing done down during each few for from further
    get gets go goes had has have having he her here hers how i if in into is it its itself just
    me more most my no nor not now of off on once only or other our ours out over own same she
    should so some such than that the their theirs them then there these they this those through
    to too under until up very was we were what when where which while who whom why will with
    would you your yours""".split()
)

FIELD_WEIGHTS = {"body": 1.0, "heading": 3.0, "title": 1.5, "path": 1.5, "meta": 1.5}
K1 = 1.2
B = 0.75
TYPE_BOOST = {
    "decision": 1.25,
    "system": 1.25,
    "profile": 1.1,
    "failed": 1.1,
    "lesson": 1.1,
    "overlay": 1.05,
    "reference": 1.0,
    "job": 1.0,
    "index": 0.9,
    "log": 0.8,
}
KIND_BOOST = {"rule": 1.1}  # binding rules files carry no frontmatter type
RECENCY_MAX = 0.1  # at most +10% for the newest notes
RECENCY_DAYS = 60.0
PER_NOTE_CAP = 2  # sections per note in the ranked list
TOP_NOTES_FOR_LINKS = 5
LINK_FACTOR = 0.5
OVERLAY_FACTOR = 0.95
SUPERSEDED_STRONG = 0.6  # report a superseded note when it scores >= 60% of the top hit
CHARS_PER_TOKEN = 4
EXCERPT_CHARS = 160


# ---------------------------------------------------------------- text basics


def stem(word: str) -> str:
    """Light suffix stripping then truncation to 6 chars (cheap, stable, good enough for BM25)."""
    if len(word) > 4 and word.endswith("ies"):
        word = word[:-3] + "y"
    elif len(word) > 5 and word.endswith("ing"):
        word = word[:-3]
    elif len(word) > 4 and word.endswith("ed"):
        word = word[:-2]
    elif len(word) > 3 and word.endswith("s") and not word.endswith(("ss", "us", "is")):
        word = word[:-1]
    if len(word) > 4 and word.endswith("e"):
        word = word[:-1]
    if len(word) > 4 and word.endswith("ly"):
        word = word[:-2]
    return word[:6]


def tokenize(text: str) -> list[str]:
    text = CAMEL_RE.sub(" ", text)
    return [stem(w) for w in WORD_RE.findall(text.lower()) if w not in STOP_WORDS and (len(w) > 1 or w.isdigit())]


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def clip(text: str, limit: int = EXCERPT_CHARS) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


# ---------------------------------------------------------------- frontmatter

FM_LINE_RE = re.compile(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$")
FM_ITEM_RE = re.compile(r"^\s+-\s*(.*)$")


def _scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    value = re.sub(r"\s+#.*$", "", value)  # trailing comment (unquoted values only)
    return value.strip()


def _value(raw: str):
    raw = raw.strip()
    if raw.startswith("[") and "]" in raw:
        inner = raw[1 : raw.rindex("]")]
        return [_scalar(item) for item in inner.split(",") if _scalar(item)]
    return _scalar(raw)


def parse_frontmatter(text: str) -> tuple[dict | None, int, list[str]]:
    """Return (meta or None, number of lines the frontmatter block uses, parse errors)."""
    lines = text.lstrip("﻿").splitlines()
    if not lines or lines[0].strip() != "---":
        return None, 0, []
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        return None, 0, ["frontmatter has no closing '---'"]
    meta: dict = {}
    errors: list[str] = []
    key = None
    for number, line in enumerate(lines[1:end], start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        item = FM_ITEM_RE.match(line)
        if item and key is not None:
            if not isinstance(meta.get(key), list):
                meta[key] = [] if meta.get(key) in ("", None) else [meta[key]]
            meta[key].append(_scalar(item.group(1)))
            continue
        match = FM_LINE_RE.match(line)
        if not match:
            if key is not None and line[:1].isspace() and isinstance(meta.get(key), str):
                meta[key] = (meta[key] + " " + line.strip()).strip()  # folded continuation
                continue
            errors.append(f"line {number}: cannot parse frontmatter line")
            continue
        key = match.group(1)
        meta[key] = _value(match.group(2))
    return meta, end + 1, errors


def parse_date(value) -> datetime.date | None:
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value.strip()):
        return None
    try:
        return datetime.date.fromisoformat(value.strip())
    except ValueError:
        return None


# ---------------------------------------------------------------- notes and sections


@dataclass
class Section:
    path: str
    heading: str
    level: int
    start: int  # 1-based, inclusive (heading line)
    end: int  # 1-based, inclusive
    lines: list[str]
    tokens: dict[str, list[str]] = field(default_factory=dict)
    length: int = 0

    @property
    def anchor(self) -> str:
        return slugify(self.heading)


@dataclass
class Note:
    path: str
    title: str
    kind: str  # rule | skill | role | workflow | knowledge | agents | other
    meta: dict | None
    fm_errors: list[str]
    lines: list[str]
    body_start: int  # 0-based index of the first line after frontmatter
    links: list[tuple[int, str]]  # (1-based line, raw target)
    sections: list[Section] = field(default_factory=list)

    @property
    def type(self) -> str:
        return str((self.meta or {}).get("type", "") or "")

    @property
    def status(self) -> str:
        return str((self.meta or {}).get("status", "") or "")

    @property
    def updated(self) -> datetime.date | None:
        return parse_date((self.meta or {}).get("updated"))

    @property
    def name(self) -> str:
        """Skill/role/workflow name used for overlay lookup."""
        parts = self.path.split("/")
        if self.kind == "skill" and len(parts) >= 3:
            return parts[2]
        return Path(self.path).stem


def kind_for(path: str) -> str:
    if path.startswith("rules/"):
        return "rule"
    if path.startswith(".agents/skills/"):
        return "skill"
    if path.startswith(".agents/roles/"):
        return "role"
    if path.startswith(".agents/workflows/"):
        return "workflow"
    if path.startswith("knowledge/"):
        return "knowledge"
    if path == "AGENTS.md":
        return "agents"
    return "other"


def extract_links(lines: list[str], offset: int = 0) -> list[tuple[int, str]]:
    """[[links]] outside code fences and inline code. offset = lines skipped before `lines`."""
    found: list[tuple[int, str]] = []
    in_fence = False
    for number, line in enumerate(lines, start=offset + 1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for match in LINK_RE.finditer(INLINE_CODE_RE.sub("", line)):
            found.append((number, match.group(1).strip()))
    return found


def load_note(root: Path, path: Path) -> Note:
    rel = path.relative_to(root).as_posix()
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.lstrip("﻿").splitlines()
    meta, fm_len, fm_errors = parse_frontmatter(text)
    body = lines[fm_len:]
    note = Note(rel, "", kind_for(rel), meta, fm_errors, lines, fm_len, extract_links(body, fm_len))
    note.sections = split_sections(note)
    note.title = next((s.heading for s in note.sections if s.level == 1), "") or Path(rel).stem.replace("-", " ")
    return note


def split_sections(note: Note) -> list[Section]:
    lines = note.lines
    heads: list[tuple[int, int, str]] = []  # (0-based index, level, text)
    in_fence = False
    for index in range(note.body_start, len(lines)):
        line = lines[index]
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = HEADING_RE.match(line)
        if match and len(match.group(1)) <= SPLIT_LEVEL:
            heads.append((index, len(match.group(1)), match.group(2).strip()))
    sections: list[Section] = []
    first = heads[0][0] if heads else len(lines)
    has_preamble = any(l.strip() for l in lines[note.body_start : first])
    opens_with_h1 = bool(heads) and heads[0][1] == 1
    if not heads or (has_preamble and not opens_with_h1):
        fallback = Path(note.path).stem.replace("-", " ")
        sections.append(Section(note.path, fallback, 1, note.body_start + 1, first, lines[note.body_start : first]))
    for position, (index, level, text) in enumerate(heads):
        end = heads[position + 1][0] if position + 1 < len(heads) else len(lines)
        # The preamble (author line, lead text) joins the title section when the file opens with an H1.
        start = note.body_start if position == 0 and opens_with_h1 else index
        sections.append(Section(note.path, text, level, start + 1, end, lines[start:end]))
    if sections and note.meta and note.meta.get("description"):
        sections[0].lines = [str(note.meta["description"])] + sections[0].lines  # skills/workflows
    return [s for s in sections if any(l.strip() for l in s.lines)]


# ---------------------------------------------------------------- corpus


def _is_heading(line: str, heading: str) -> bool:
    match = HEADING_RE.match(line)
    return bool(match) and match.group(2).strip() == heading


def load_config(root: Path) -> dict:
    path = root / "kit.json"
    if not path.is_file():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    context = data.get("context") if isinstance(data, dict) else None
    return context if isinstance(context, dict) else {}


def _excluded(rel: str, exclude: tuple[str, ...]) -> bool:
    parts = rel.split("/")
    if SKIP_DIRS.intersection(parts):
        return True
    return any(rel == ex or rel.startswith(ex.rstrip("/") + "/") for ex in exclude)


def corpus_files(root: Path, config: dict | None = None) -> list[str]:
    config = load_config(root) if config is None else config
    roots = tuple(config.get("search_roots") or DEFAULT_ROOTS)
    exclude = tuple(config.get("exclude") or DEFAULT_EXCLUDE)
    found: set[str] = set()
    for rel in ALWAYS_FILES:
        if (root / rel).is_file():
            found.add(rel)
    for rel in roots:
        base = root / rel
        if base.is_file() and base.suffix == ".md":
            found.add(rel)
        elif base.is_dir():
            for path in base.rglob("*.md"):
                prel = path.relative_to(root).as_posix()
                if path.is_file() and not _excluded(prel, exclude):
                    found.add(prel)
    return sorted(found, key=str.lower)


class Corpus:
    def __init__(self, root: Path, config: dict | None = None):
        self.root = root
        self.config = load_config(root) if config is None else config
        self.notes: dict[str, Note] = {}
        for rel in corpus_files(root, self.config):
            self.notes[rel] = load_note(root, root / rel)
        self.sections: list[Section] = [s for n in self.notes.values() for s in n.sections]
        self._index()

    def _index(self) -> None:
        self.df: dict[str, int] = {}
        for note in self.notes.values():
            title = tokenize(note.title)
            path = tokenize(note.path.replace(".md", ""))
            for index, section in enumerate(note.sections):
                lines = section.lines
                meta_tokens: list[str] = []
                if index == 0 and note.meta and note.meta.get("description"):
                    meta_tokens = tokenize(lines[0])
                    lines = lines[1:]
                body = tokenize("\n".join(l for l in lines if not HEADING_RE.match(l) or l.strip() != lines[0].strip()))
                section.tokens = {
                    "body": body,
                    "heading": tokenize(section.heading),
                    "title": title,
                    "path": path,
                    "meta": meta_tokens,
                }
                section.length = len(body) + len(meta_tokens)
                for term in {t for toks in section.tokens.values() for t in toks}:
                    self.df[term] = self.df.get(term, 0) + 1
        self.avg_length = sum(s.length for s in self.sections) / max(1, len(self.sections))
        dates = [n.updated for n in self.notes.values() if n.updated]
        self.newest = max(dates) if dates else None
        self._stems: dict[str, list[str]] | None = None

    def idf(self, term: str) -> float:
        n = len(self.sections)
        df = self.df.get(term, 0)
        return math.log(1 + (n - df + 0.5) / (df + 0.5))

    def note_boost(self, note: Note) -> float:
        boost = TYPE_BOOST.get(note.type, KIND_BOOST.get(note.kind, 1.0))
        if note.status == "draft":
            boost *= 0.9
        if note.updated and self.newest:
            age = (self.newest - note.updated).days
            boost *= 1 + RECENCY_MAX * math.exp(-max(0, age) / RECENCY_DAYS)
        return boost

    # -- links

    def resolve_link(self, target: str, from_path: str = "") -> str | None:
        """Resolve a [[link]] target to a repo-relative .md path, or None if dead."""
        target = target.split("|", 1)[0].split("#", 1)[0].strip().strip("/")
        if not target:
            return from_path or None
        candidates = []
        for base in ("", "knowledge/"):
            candidates.append(base + target)
            if not target.endswith(".md"):
                candidates.append(base + target + ".md")
        if from_path:
            parent = Path(from_path).parent.as_posix()
            candidates.append(f"{parent}/{target}" + ("" if target.endswith(".md") else ".md"))
        for candidate in candidates:
            if candidate in self.notes or (self.root / candidate).is_file():
                return candidate
        stem_name = Path(target).name.removesuffix(".md").lower()
        matches = self.stem_index().get(stem_name, [])
        return matches[0] if len(matches) == 1 else None

    def stem_index(self) -> dict[str, list[str]]:
        if self._stems is None:
            stems: dict[str, list[str]] = {}
            paths = set(self.notes)
            knowledge = self.root / "knowledge"
            if knowledge.is_dir():
                for path in knowledge.rglob("*.md"):
                    rel = path.relative_to(self.root).as_posix()
                    if not SKIP_DIRS.intersection(rel.split("/")):
                        paths.add(rel)
            for rel in sorted(paths):
                stems.setdefault(Path(rel).stem.lower(), []).append(rel)
            self._stems = stems
        return self._stems

    def replacement_for(self, note: Note) -> str | None:
        meta = note.meta or {}
        by = meta.get("superseded_by")
        if isinstance(by, list):
            by = by[0] if by else None
        if by:
            return str(by)
        for other in self.notes.values():
            sup = (other.meta or {}).get("supersedes") or []
            sup = sup if isinstance(sup, list) else [sup]
            if note.path in [str(s) for s in sup] and other.status != "superseded":
                return other.path
        for _, target in note.links:
            resolved = self.resolve_link(target, note.path)
            if resolved and resolved != note.path:
                return resolved
        return None


# ---------------------------------------------------------------- ranking


@dataclass
class Hit:
    path: str
    heading: str
    anchor: str
    start: int
    end: int
    score: float
    kind: str  # match | link | overlay
    why: str
    excerpt: list[str]


def query_terms(query: str) -> list[str]:
    seen: list[str] = []
    for term in tokenize(query):
        if term not in seen:
            seen.append(term)
    return seen


def score_section(corpus: Corpus, section: Section, terms: list[str], idf: dict[str, float]) -> tuple[float, list[str], set[str]]:
    norm = K1 * (1 - B + B * section.length / max(1.0, corpus.avg_length))
    total = 0.0
    matched: list[str] = []
    fields_hit: set[str] = set()
    for term in terms:
        tf = 0.0
        for name, weight in FIELD_WEIGHTS.items():
            count = section.tokens[name].count(term)
            if count:
                tf += weight * count
                fields_hit.add(name)
        if tf:
            matched.append(term)
            total += idf[term] * tf * (K1 + 1) / (tf + norm)
    if not matched:
        return 0.0, [], set()
    stream = section.tokens["heading"] + section.tokens["meta"] + section.tokens["body"]
    pairs = set(zip(stream, stream[1:]))
    bigrams = sum(1 for pair in zip(terms, terms[1:]) if pair in pairs)
    total += min(3, bigrams) * 0.5 * sum(idf[t] for t in matched) / len(matched)
    total *= 0.5 + 0.5 * len(matched) / len(terms)
    return total, matched, fields_hit


def excerpt_for(section: Section, terms: list[str], limit: int = 2) -> list[str]:
    candidates: list[tuple[int, int, str]] = []
    in_fence = False
    for offset, line in enumerate(section.lines):
        stripped = line.strip()
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if (
            not stripped
            or in_fence
            or HEADING_RE.match(stripped)
            or stripped.startswith("> Author")
            or re.fullmatch(r"\|?[\s:|-]+\|?", stripped)
        ):
            continue
        hits = len(set(tokenize(stripped)) & set(terms))
        candidates.append((-hits, offset, stripped))
    if not candidates:
        return []
    with_hits = [c for c in candidates if c[0] < 0]
    best = sorted(with_hits)[:limit] if with_hits else candidates[:1]
    return [clip(text) for _, _, text in sorted(best, key=lambda c: c[1])]


def rank(corpus: Corpus, query: str) -> tuple[list[Hit], list[dict]]:
    """Return (ranked hits, superseded strong matches). Deterministic."""
    terms = query_terms(query)
    if not terms:
        raise ValueError("query needs at least one meaningful word")
    idf = {t: corpus.idf(t) for t in terms}
    scored: list[tuple[float, Section, list[str], set[str]]] = []
    for section in corpus.sections:
        value, matched, fields_hit = score_section(corpus, section, terms, idf)
        if value > 0:
            note = corpus.notes[section.path]
            scored.append((value * corpus.note_boost(note), section, matched, fields_hit))
    scored.sort(key=lambda item: (-item[0], item[1].path.lower(), item[1].start))

    top = scored[0][0] if scored else 0.0
    hits: list[Hit] = []
    per_note: dict[str, int] = {}
    superseded: dict[str, dict] = {}
    for value, section, matched, fields_hit in scored:
        note = corpus.notes[section.path]
        if note.status == "superseded":
            if value >= SUPERSEDED_STRONG * top and section.path not in superseded:
                superseded[section.path] = {
                    "path": section.path,
                    "score": round(value, 3),
                    "see": corpus.replacement_for(note),
                }
            continue
        if per_note.get(section.path, 0) >= PER_NOTE_CAP:
            continue
        per_note[section.path] = per_note.get(section.path, 0) + 1
        where = "/".join(f for f in ("heading", "title", "path", "meta", "body") if f in fields_hit)
        why = f"matched {', '.join(matched)} in {where}"
        if note.type:
            why += f"; type {note.type}"
        hits.append(Hit(section.path, section.heading, section.anchor, section.start, section.end, value, "match", why, excerpt_for(section, terms)))

    # 1-hop link neighbours of the top notes.
    present = {h.path for h in hits}
    note_score: dict[str, float] = {}
    for hit in hits:
        note_score.setdefault(hit.path, hit.score)
    extra: list[Hit] = []
    for path in list(note_score)[:TOP_NOTES_FOR_LINKS]:
        for _, target in corpus.notes[path].links:
            resolved = corpus.resolve_link(target, path)
            neighbour = corpus.notes.get(resolved or "")
            if not neighbour or neighbour.path in present or neighbour.status == "superseded" or not neighbour.sections:
                continue
            first = neighbour.sections[0]
            present.add(neighbour.path)
            extra.append(Hit(neighbour.path, first.heading, first.anchor, first.start, first.end, note_score[path] * LINK_FACTOR, "link", f"linked from {path}", excerpt_for(first, terms)))

    # Game overlays for matched skills and roles.
    for hit in hits[:10]:
        note = corpus.notes[hit.path]
        if note.kind not in ("skill", "role"):
            continue
        overlay = f"{OVERLAYS}/{note.name}.md"
        target = corpus.notes.get(overlay)
        if target is None and (corpus.root / overlay).is_file():
            target = load_note(corpus.root, corpus.root / overlay)
        if target is None or target.status == "superseded" or not target.sections:
            continue
        score = hit.score * OVERLAY_FACTOR
        existing = next((h for h in hits + extra if h.path == overlay), None)
        if existing:
            existing.score = max(existing.score, score)
            continue
        first = target.sections[0]
        extra.append(Hit(overlay, first.heading, first.anchor, first.start, first.end, score, "overlay", f"game overlay for {note.kind} {note.name}", excerpt_for(first, terms)))

    merged = hits + extra
    merged.sort(key=lambda h: (-round(h.score, 9), h.path.lower(), h.start))
    return merged, sorted(superseded.values(), key=lambda s: (-s["score"], s["path"]))


# ---------------------------------------------------------------- side lists


def decision_rows(root: Path, terms: list[str], limit: int = 8) -> list[dict]:
    path = root / DECISIONS
    if not path.is_file():
        return []
    rows = []
    header_done = False
    for number, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), start=1):
        stripped = line.strip()
        if not stripped.startswith("|") or re.fullmatch(r"\|?[\s:|-]+\|?", stripped):
            continue
        if not header_done:
            header_done = True  # first table row is the header
            continue
        hits = set(tokenize(stripped)) & set(terms)
        if len(hits) >= min(2, len(terms)):
            rows.append({"line": number, "row": clip(stripped, 240), "matched": sorted(hits)})
    rows.sort(key=lambda r: (-len(r["matched"]), r["line"]))
    return rows[:limit]


def agents_headings(root: Path) -> list[str]:
    path = root / "AGENTS.md"
    if not path.is_file():
        return []
    heads = []
    in_fence = False
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        match = HEADING_RE.match(line)
        if match and not in_fence and len(match.group(1)) == 2:
            heads.append(match.group(2).strip())
    return heads


def code_hints(root: Path, terms: list[str], limit: int = 6) -> list[dict]:
    found = []
    for code_root in CODE_ROOTS:
        base = root / code_root
        if not base.is_dir():
            continue
        for path in base.rglob("*"):
            rel = path.relative_to(root).as_posix()
            if not path.is_file() or SKIP_DIRS.intersection(rel.split("/")):
                continue
            hits = set(tokenize(rel.rsplit(".", 1)[0])) & set(terms)
            if hits:
                found.append({"path": rel, "matched": sorted(hits)})
    found.sort(key=lambda f: (-len(f["matched"]), f["path"].lower()))
    return found[:limit]


# ---------------------------------------------------------------- packet


def build(root: Path, query: str, budget: int = 8000, max_items: int = 12) -> dict:
    corpus = Corpus(root)
    terms = query_terms(query)
    hits, superseded = rank(corpus, query)
    limit_chars = budget * CHARS_PER_TOKEN
    used = 600  # header, side lists and read-next reserve
    chosen: list[Hit] = []
    for hit in hits:
        if len(chosen) >= max_items:
            break
        size = len(hit.path) + len(hit.heading) + len(hit.why) + sum(len(e) for e in hit.excerpt) + 60
        if used + size > limit_chars:
            break
        chosen.append(hit)
        used += size

    read_next: list[str] = []
    seen: set[str] = set()
    for hit in chosen:
        if hit.path in seen:
            continue
        seen.add(hit.path)
        note = corpus.notes.get(hit.path)
        if note and note.kind == "skill":
            read_next.append(f"load skill `{note.name}` ({hit.path})")
        elif hit.kind == "overlay":
            read_next.append(f"apply overlay `{hit.path}` with its skill")
        else:
            read_next.append(f"open `{hit.path}` L{hit.start}-{hit.end} ({hit.heading})")
        if len(read_next) >= 4:
            break
    areas = []
    for hit in chosen[:5]:
        parts = hit.path.split("/")
        if parts[0] == "knowledge" and len(parts) > 2 and parts[1] not in areas:
            areas.append(parts[1])
    for area in areas:
        index = f"knowledge/generated/index-{area}.md"
        if (root / index).is_file():
            read_next.append(f"browse `{index}` for nearby {area} notes")
    for item in superseded:
        if item["see"]:
            read_next.append(f"`{item['path']}` is superseded: read `{item['see']}` instead")
    if not chosen:
        read_next.append("nothing matched: start from `knowledge/index.md`")

    return {
        "query": query,
        "terms": terms,
        "searched": {"files": len(corpus.notes), "sections": len(corpus.sections)},
        "budget_tokens": budget,
        "results": [
            {
                "rank": i + 1,
                "ref": f"{h.path}#{h.anchor}",
                "path": h.path,
                "heading": h.heading,
                "lines": [h.start, h.end],
                "score": round(h.score, 3),
                "kind": h.kind,
                "why": h.why,
                "excerpt": h.excerpt,
            }
            for i, h in enumerate(chosen)
        ],
        "superseded": superseded,
        "decisions": decision_rows(root, terms),
        "code_hints": code_hints(root, terms),
        "agents_sections": agents_headings(root),
        "read_next": read_next,
    }


def render(packet: dict) -> str:
    out = [
        "# Context packet",
        "",
        f"- Task: {packet['query']}",
        f"- Terms: {', '.join(packet['terms'])}",
        f"- Searched: {packet['searched']['files']} files, {packet['searched']['sections']} sections; budget {packet['budget_tokens']} tokens",
        "- Locations only: source priority (AGENTS.md §0) and decision status still apply.",
        "",
        "## Ranked",
        "",
    ]
    if not packet["results"]:
        out.append("No matching section.")
    for item in packet["results"]:
        out.append(f"{item['rank']}. `{item['ref']}` L{item['lines'][0]}-{item['lines'][1]} · {item['score']} · {item['why']}")
        for line in item["excerpt"]:
            out.append(f"   > {line}")
    if packet["superseded"]:
        out += ["", "## Superseded (strong matches, skipped)", ""]
        for item in packet["superseded"]:
            out.append(f"- `{item['path']}`: superseded, see `{item['see'] or 'no replacement linked'}`")
    if packet["decisions"]:
        out += ["", f"## Matching decisions ({DECISIONS})", ""]
        out += [f"- L{row['line']}: {row['row']}" for row in packet["decisions"]]
    if packet["code_hints"]:
        out += ["", "## Code hints (file names)", ""]
        out += [f"- `{c['path']}` ({', '.join(c['matched'])})" for c in packet["code_hints"]]
    if packet["agents_sections"]:
        out += ["", "## Always on: AGENTS.md sections", "", "; ".join(packet["agents_sections"])]
    out += ["", "## Read next", ""]
    out += [f"- {line}" for line in packet["read_next"]]
    return "\n".join(out).rstrip() + "\n"


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description="Rank the knowledge base for one task.")
    result.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent, help="repository root")
    sub = result.add_subparsers(dest="command", required=True)
    packet = sub.add_parser("packet", help="print a task-sized reading list")
    packet.add_argument("task", help="plain-language task or question")
    packet.add_argument("--budget", type=int, default=8000, help="token budget (4 chars/token)")
    packet.add_argument("--max", type=int, default=12, help="maximum ranked entries")
    packet.add_argument("--json", action="store_true", help="machine-readable output")
    return result


def main(argv: list[str] | None = None) -> int:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    args = parser().parse_args(argv)
    try:
        if args.budget < 200 or args.max < 1:
            raise ValueError("--budget must be >= 200 and --max >= 1")
        packet = build(args.root.resolve(), args.task, args.budget, args.max)
    except (OSError, ValueError) as error:
        print(f"context_packet: {error}", file=sys.stderr)
        return 2
    sys.stdout.write(json.dumps(packet, indent=2, ensure_ascii=False) + "\n" if args.json else render(packet))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
