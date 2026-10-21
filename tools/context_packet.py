#!/usr/bin/env python3
"""Context packet: rank the knowledge base for one task and print a small, cited reading list.

Kit tool (universal). Standard library only, deterministic output.

Usage:
    python tools/context_packet.py packet "<task>" [--role <role>] [--job <job-id>]
        [--budget 8000] [--max 12] [--docs 5] [--json] [--root DIR]

Exit codes: 0 ok, 2 bad input (empty task, bad budget, unknown role, unknown or ambiguous job).

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
    7. "## Roblox docs": up to --docs pages of the local Roblox docs mirror (own ranking, own cap,
       not part of the kit-note budget; see the "Roblox docs mirror" block) plus an API line for
       every exact Roblox class name in the task. Index cached in knowledge/generated/.
    8. --role <role> (a stem of .agents/roles/*.md, or `orchestrator` for the lead: ROLE_ALIASES): notes
       whose frontmatter `roles:` lists the role and the role's own book (its role file and the folders
       of its `skills:`) score x ROLE_BOOST; other roles' files score x OTHER_ROLE_FACTOR. A "For role"
       block lists the role file, its `skills:`, existing overlays knowledge/overlays/<role or skill>.md,
       its knowledge/reference/roblox/docs-map.md rows and its precedent rows (knowledge/design/
       precedents.md, Craft cell names the role) verbatim, and names knowledge/design/vocabulary.md.
    9. --job <job-id> (a folder of knowledge/jobs/, or a unique prefix such as J016): notes inside that
       folder score x JOB_BOOST, and a "Job" block listing the canonical job files (JOB_FILES order,
       searched through the whole folder) with their revision (frontmatter `revision:`, a line starting
       "> Revision:" or "Revision:", or a top-level "revision" key in a .json file).
    Both blocks sit outside the note budget, at most BLOCK_MAX_LINES lines each, before "## Ranked";
    --json carries them as keys `role` and `job`. Without both flags the output is unchanged
    (regression test: tools/tests/fixtures/context/golden/).
    10. Withheld context (rules/knowledge.md §3; `withheld()`): held-out keys (any path with "hidden"
       in a file or folder name, or a note with frontmatter `held_out: true`), direction proposals (`*/direction/proposal-*`), `_`-named material under
       knowledge/ (kit history, another game's notes) and skill eval briefs (`.agents/skills/*/evals/`)
       are never in the corpus, link neighbours, job blocks or read-next list, whatever kit.json says;
       a line that names a held-out file is never excerpted. kb_index.py uses the same rules.
    11. Sibling files that repeat one section (same folder, same heading, SIBLING_OVERLAP of its words in
       the kept one) take one ranked slot; distinct sections under a shared template heading all rank.
    12. With --role for a craft role (not orchestrator or doc-keeper), files under a job's reviews/ or
       exchange/ folder score x JOB_HISTORY_FACTOR (rules/knowledge.md §3: a craft step does not get the
       whole job history); briefs name the ones a step needs. A closed job's (not in knowledge/jobs/active.md)
       review and exchange files score x JOB_HISTORY_FACTOR for every role, unless --job names that job.

Search roots: kit.json key `context.search_roots` (list of repo-relative paths) when present,
else DEFAULT_ROOTS. `context.exclude` (list) replaces DEFAULT_EXCLUDE when present (never the withheld
rules of step 10).

Revised by feature-builder · claude-opus-5-5 · high · 2026-10-21, J016 G3 (audit D B1-B3, B6, R1, R12,
R13; audit E TT-01, TT-15-TT-18).
Other tools import this module (kb_index.py, eval_context.py).
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import math
import os
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
ROLES_DIR = ".agents/roles"
JOBS_DIR = "knowledge/jobs"
DOCS_MAP = "knowledge/reference/roblox/docs-map.md"
ROLE_BOOST = 1.5  # PROPOSAL (J016-T01): notes tagged `roles: [<role>]` and the role's own book, for the --role
JOB_BOOST = 1.5  # PROPOSAL (J016-T01): notes inside the --job folder
BLOCK_MAX_LINES = 25
JOB_FILES = ("job-card.md", "direction.md", "decisions.md", "crew.md", "evidence.md", "ledger.md", "beat-sheet.md", "contract*.md", "*.shots.json")
REVISION_LINE_RE = re.compile(r"^(?:>\s*)?Revision:\s*(.+?)\s*$")
ACTIVE_JOBS = "knowledge/jobs/active.md"  # lines `- <job-id> · <title>`, kept by the lead; read by tools/hooks/
ACTIVE_JOB_RE = re.compile(r"^- (\S+) · (.+)$")
PRECEDENTS = "knowledge/design/precedents.md"
VOCABULARY = "knowledge/design/vocabulary.md"
PRECEDENT_ROWS = 5  # newest rows of the role's craft in the role block
ROLE_ALIASES = {"orchestrator": ["orchestration"]}  # the lead has no role file; its book is this skill
OTHER_ROLE_FACTOR = 1 / ROLE_BOOST  # with --role, other roles' identity files
JOB_HISTORY_RE = re.compile(r"^knowledge/jobs/([^/]+)/(?:.*/)?(?:reviews|exchange)/")
JOB_HISTORY_FACTOR = 0.5  # PROPOSAL (J016 G3, audit D N1): a craft role's packet, review and exchange files
JOB_HISTORY_ROLES = frozenset({"orchestrator", "doc-keeper"})  # the lead and the filer read the job history at full weight
SIBLING_OVERLAP = 0.8  # a same-folder, same-heading section is a copy when this share of its words is in the kept one
PROPOSAL_RE = re.compile(r"(?:^|/)direction/proposal-[^/]*$")


# ---------------------------------------------------------------- withheld context (rules/knowledge.md §3)
#
# Never part of the packet corpus, link neighbours, job blocks or generated indexes, whatever kit.json
# `context.exclude` says. Lead decision LD8 (J016 G3): a held-out key is any path with "hidden" in a
# file or folder name (hidden-*, *-hidden.*, hidden-rerun/, ...), any case.


HELD_OUT_MENTION_RE = re.compile(
    r"\[\[[^\]\n]*hidden[^\]\n]*\]\]|[\w./-]*hidden[\w.-]*\.(?:md|json|jsonl|txt|luau?)\b|[\w.-]*hidden[\w.-]*/", re.IGNORECASE
)  # a link or path to a held-out file; the rule text "`hidden-*`" does not match


def held_out(rel: str) -> bool:
    """A held-out evaluation key: never opened, listed or excerpted by any tool."""
    return any("hidden" in part.lower() for part in rel.split("/"))


def names_held_out(line: str) -> bool:
    """True when a line of a visible note names a held-out file; such lines are never excerpted."""
    return bool(HELD_OUT_MENTION_RE.search(line))


def marked_held_out(meta: dict | None) -> bool:
    """Frontmatter `held_out: true`: a visibly named note that repeats held-out cases, keys, rubrics or
    answers (grade files, eval answers). Withheld exactly like a hidden-named file (J016 G3 repair, E N-01)."""
    return str((meta or {}).get("held_out", "")).strip().lower() in ("true", "yes")


def withheld(rel: str) -> str | None:
    """Why a repo-relative path is withheld from packets and generated indexes, or None."""
    parts = rel.split("/")
    if held_out(rel):
        return "held-out evaluation key"
    if PROPOSAL_RE.search(rel):
        return "direction proposal: the job lead reads it through the synthesis brief"
    if parts[0] == "knowledge" and any(part.startswith("_") for part in parts[1:]):
        return "kit history or another game's material (underscore name)"
    if rel.startswith(".agents/skills/") and "evals" in parts:
        return "skill eval brief (pass criteria)"
    return None


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


def as_list(value) -> list[str]:
    """A frontmatter list value: [a, b], a block list, or a comma-separated scalar."""
    if isinstance(value, list):
        return [str(v).strip() for v in value if str(v).strip()]
    if isinstance(value, str):
        return [part.strip() for part in value.split(",") if part.strip()]
    return []


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
    if SKIP_DIRS.intersection(parts) or withheld(rel):
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
        if base.is_file() and base.suffix == ".md" and not withheld(rel):
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
        self.marked: set[str] = set()  # notes with `held_out: true`, never ranked, linked or resolved
        for rel in corpus_files(root, self.config):
            note = load_note(root, root / rel)
            if marked_held_out(note.meta):
                self.marked.add(rel)
                continue
            self.notes[rel] = note
        self.sections: list[Section] = [s for n in self.notes.values() for s in n.sections]
        # Open job folders from knowledge/jobs/active.md; None when the file is missing (nothing counts as closed).
        self.active: set[str] | None = {_active_folder(root, j) for j, _ in active_jobs(root)} if (root / ACTIVE_JOBS).is_file() else None
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
                    if not SKIP_DIRS.intersection(rel.split("/")) and not withheld(rel) and rel not in self.marked:
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
            if resolved and resolved != note.path and not withheld(resolved) and resolved not in self.marked:
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
            or names_held_out(stripped)
        ):
            continue
        hits = len(set(tokenize(stripped)) & set(terms))
        candidates.append((-hits, offset, stripped))
    if not candidates:
        return []
    with_hits = [c for c in candidates if c[0] < 0]
    best = sorted(with_hits)[:limit] if with_hits else candidates[:1]
    return [clip(text) for _, _, text in sorted(best, key=lambda c: c[1])]


def role_book(corpus: Corpus, role: str) -> tuple[str, ...]:
    """Path prefixes of a role's own book: its role file and the folders of its frontmatter `skills:`."""
    note = corpus.notes.get(f"{ROLES_DIR}/{role}.md")
    skills = ROLE_ALIASES.get(role) or as_list((note.meta or {}).get("skills") if note else None)
    return (f"{ROLES_DIR}/{role}.md",) + tuple(f".agents/skills/{name}/" for name in skills)


def rank(corpus: Corpus, query: str, role: str | None = None, job: str | None = None) -> tuple[list[Hit], list[dict]]:
    """Return (ranked hits, superseded strong matches). Deterministic.
    role: boost notes tagged `roles: [role]` and the role's own book (role file and skill folders),
    lower other roles' files; job: a resolved job folder name, boost notes inside it."""
    terms = query_terms(query)
    if not terms:
        raise ValueError("query needs at least one meaningful word")
    idf = {t: corpus.idf(t) for t in terms}
    job_prefix = f"{JOBS_DIR}/{job}/" if job else None
    book = role_book(corpus, role) if role else ()
    scored: list[tuple[float, Section, list[str], set[str]]] = []
    boosted: dict[str, str] = {}  # path -> why suffix, only when --role or --job applies
    for section in corpus.sections:
        value, matched, fields_hit = score_section(corpus, section, terms, idf)
        if value > 0:
            note = corpus.notes[section.path]
            value = value * corpus.note_boost(note)
            role_hit = bool(role) and role in as_list((note.meta or {}).get("roles"))
            own_book = bool(book) and note.path.startswith(book)
            job_hit = bool(job_prefix) and note.path.startswith(job_prefix)
            if role_hit or own_book:
                value *= ROLE_BOOST
            elif book and note.kind == "role":
                value *= OTHER_ROLE_FACTOR
            past = JOB_HISTORY_RE.match(note.path)
            history = bool(past) and bool(role) and role not in JOB_HISTORY_ROLES
            # A closed job's history is lower for every role (its lessons were filed at close), unless --job names it.
            closed = bool(past) and corpus.active is not None and past.group(1) not in corpus.active and not job_hit
            if history or closed:
                value *= JOB_HISTORY_FACTOR
            if job_hit:
                value *= JOB_BOOST
            if role_hit or own_book or job_hit or history or closed:
                boosted[note.path] = (
                    (f"; tagged for role {role}" if role_hit else "")
                    + (f"; own book of role {role}" if own_book and not role_hit else "")
                    + (f"; in job {job}" if job_hit else "")
                    + ("; job review or exchange file, lower for a craft role" if history else "")
                    + ("; closed job's review or exchange file, lower" if closed and not history else "")
                )
            scored.append((value, section, matched, fields_hit))
    scored.sort(key=lambda item: (-item[0], item[1].path.lower(), item[1].start))

    top = scored[0][0] if scored else 0.0
    hits: list[Hit] = []
    per_note: dict[str, int] = {}
    kept_copies: dict[tuple[str, str], list[set[str]]] = {}  # (folder, heading) -> word sets of kept sections (audit D R12, N2)
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
        copy_key = (section.path.rpartition("/")[0].lower(), section.heading.strip().lower())
        words = set(section.tokens["body"])
        kept = kept_copies.setdefault(copy_key, [])
        if any(len(words & other) >= SIBLING_OVERLAP * max(1, min(len(words), len(other))) for other in kept):
            continue  # a sibling file repeats this section: one slot for both
        kept.append(words)
        per_note[section.path] = per_note.get(section.path, 0) + 1
        where = "/".join(f for f in ("heading", "title", "path", "meta", "body") if f in fields_hit)
        why = f"matched {', '.join(matched)} in {where}"
        if note.type:
            why += f"; type {note.type}"
        why += boosted.get(note.path, "")
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
        if target is None and not withheld(overlay) and (corpus.root / overlay).is_file():
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
        if names_held_out(stripped):
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
            if not path.is_file() or SKIP_DIRS.intersection(rel.split("/")) or held_out(rel):
                continue
            hits = set(tokenize(rel.rsplit(".", 1)[0])) & set(terms)
            if hits:
                found.append({"path": rel, "matched": sorted(hits)})
    found.sort(key=lambda f: (-len(f["matched"]), f["path"].lower()))
    return found[:limit]


# ---------------------------------------------------------------- Roblox docs mirror
#
# A separate ranked list over the local Roblox Creator Docs mirror, shown after the kit notes with
# its own cap (DOCS_PAGES), so mirror pages never take kit-note slots or budget. How a page scores:
#   1. BM25F over one document per page; fields and their (weight, length normalisation b) in
#      DOCS_FIELDS. Code blocks, the mirror banner, link targets, URLs and the generated
#      "## Related Files" tail are left out; `Class.X` / `Enum.X` prefixes are dropped.
#   2. Times a coverage factor (share of query words the page matches), as the kit ranking does.
#   3. Times a folder prior (DOCS_FOLDER_PRIOR): project walkthroughs and showcase write-ups repeat
#      many words but are rarely the page that explains an engine system.
#   4. Times a small authority prior from incoming page-body links inside the mirror.
#   5. Plus a kit-citation term: mirror pages that the top-ranked kit sections cite (by path or
#      [[external/roblox-creator-docs/...]] link) gain up to DOCS_CITE_WEIGHT x the best page score.
#      The kit's own notes thereby route player words ("a streak behind the sword") to pages.
# Pages under underscore folders (_includes, _api-reference) and the mirror README are skipped.
# The page index is cached in DOCS_CACHE and rebuilt when any page's path, size or mtime changes.

DOCS_MIRROR = "knowledge/external/roblox-creator-docs"
DOCS_API_CLASSES = f"{DOCS_MIRROR}/_api-reference/classes"
DOCS_CACHE = "knowledge/generated/roblox-docs-index.json"
DOCS_CACHE_VERSION = 2
DOCS_PAGES = 5
DOCS_FIELDS = {"title": (4.0, 0.3), "description": (2.5, 0.5), "headings": (1.5, 0.5), "path": (2.0, 0.3), "body": (1.0, 0.75)}
DOCS_K1 = 2.0
DOCS_COVERAGE = 0.5  # score *= (1 - c) + c * matched / query words
DOCS_FOLDER_PRIOR = {"tutorials/": 0.5, "resources/": 0.7}
DOCS_INLINK_WEIGHT = 0.1  # score *= 1 + w * ln(1 + incoming links)
DOCS_CITE_SECTIONS = 10  # top kit sections scanned for mirror citations
DOCS_CITE_WEIGHT = 0.5
DOCS_SKIP_FILES = {"README.md"}  # the mirror's own index page, top level only
DOCS_TAIL_HEADINGS = {"Related Files"}  # generated link lists at the end of each page
DOCS_PREFIX_RE = re.compile(r"\b(?:Class|Enum|Datatype|Library|Global)\.")
DOCS_HTML_RE = re.compile(r"<[^>\n]+>")
DOCS_LINK_TARGET_RE = re.compile(r"\]\([^)\s]*\)")
DOCS_WIKI_RE = re.compile(r"\[\[([^\[\]|\n]+?)(?:\|([^\[\]\n]*))?\]\]")
DOCS_URL_RE = re.compile(r"https?://\S+")
DOCS_CITE_RE = re.compile(r"((?:[A-Za-z0-9_-]+/)+[A-Za-z0-9_-]+|[A-Za-z0-9_-]+(?=\.md))(\.md)?")
DOCS_MIRROR_LINK = "external/roblox-creator-docs/"
ACRONYM_RE = re.compile(r"(?<=[A-Z])(?=[A-Z][a-z])")
IDENT_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")


_DOCS_STEMS: dict[str, list[str]] = {}  # raw word -> its tokens
DOCS_RAW_WORD_RE = re.compile(r"[A-Za-z0-9]+")


def docs_tokenize(text: str) -> list[str]:
    """tokenize() plus acronym splits (UICorner -> UI Corner), so class-named pages match plain words.
    Same tokens as tokenize(); stems are memoised because the mirror is ~11 MB of text."""
    out: list[str] = []
    for raw in DOCS_RAW_WORD_RE.findall(text):
        cached = _DOCS_STEMS.get(raw)
        if cached is None:
            words = WORD_RE.findall(CAMEL_RE.sub(" ", ACRONYM_RE.sub(" ", raw)).lower())
            cached = _DOCS_STEMS[raw] = [stem(w) for w in words if w not in STOP_WORDS and (len(w) > 1 or w.isdigit())]
        out.extend(cached)
    return out


def _docs_page_files(mirror: Path) -> list[tuple[str, int, int]]:
    """(path relative to the mirror, size, mtime_ns) for every page, sorted."""
    found: list[tuple[str, int, int]] = []
    for folder, dirs, files in os.walk(mirror):
        dirs[:] = [d for d in dirs if not d.startswith("_") and d not in SKIP_DIRS]
        base = Path(folder)
        for name in files:
            if not name.endswith(".md") or name.startswith("_"):
                continue
            rel = (base / name).relative_to(mirror).as_posix()
            if rel in DOCS_SKIP_FILES:
                continue
            info = (base / name).stat()
            found.append((rel, info.st_size, info.st_mtime_ns))
    found.sort()
    return found


def _docs_clean(value: str) -> str:
    value = DOCS_WIKI_RE.sub(lambda m: f" {m.group(2) or ''} ", value)
    value = DOCS_LINK_TARGET_RE.sub("]", value)
    value = DOCS_URL_RE.sub(" ", DOCS_HTML_RE.sub(" ", value))
    return DOCS_PREFIX_RE.sub("", value)


def _docs_fields(rel: str, text: str) -> tuple[str, str, dict[str, list[str]], set[str]]:
    """(title, description, field tokens, mirror pages this page's body links to)."""
    meta, fm_len, _ = parse_frontmatter(text)
    meta = meta or {}
    lines = text.lstrip("﻿").splitlines()[fm_len:]
    headings: list[str] = []
    body: list[str] = []
    links: set[str] = set()
    in_fence = False
    for line in lines:
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        stripped = line.strip()
        if in_fence or stripped.startswith(("> [!info] Local Roblox", "> Mirrored from")):
            continue
        match = HEADING_RE.match(stripped)
        if match:
            if match.group(2).strip() in DOCS_TAIL_HEADINGS:
                break
            headings.append(match.group(2))
            continue
        body.append(line)
        for wiki in DOCS_WIKI_RE.finditer(line):
            target = wiki.group(1).split("#", 1)[0].strip()
            if target.startswith(DOCS_MIRROR_LINK):
                links.add(target[len(DOCS_MIRROR_LINK) :].removesuffix(".md") + ".md")
    title = str(meta.get("title") or "") or next((h for h in headings[:1]), "") or Path(rel).stem.replace("-", " ")
    description = _docs_clean(str(meta.get("description") or ""))
    path_words = rel.removesuffix(".md").removesuffix("/index").replace("/", " ")
    fields = {
        "title": docs_tokenize(_docs_clean(title)),
        "description": docs_tokenize(description),
        "headings": docs_tokenize(_docs_clean("\n".join(headings))),
        "path": docs_tokenize(path_words),
        "body": docs_tokenize(_docs_clean("\n".join(body))),
    }
    links.discard(rel)
    return title, description, fields, links


def _build_docs_index(mirror: Path, files: list[tuple[str, int, int]]) -> dict:
    pages: list[dict] = []
    per_page: list[dict[str, list[str]]] = []
    incoming: dict[str, int] = {}
    for rel, _, _ in files:
        title, description, fields, links = _docs_fields(rel, (mirror / rel).read_text(encoding="utf-8", errors="replace"))
        pages.append({"path": rel, "title": clip(title, 120), "description": clip(description, 200)})
        per_page.append(fields)
        for target in links:
            incoming[target] = incoming.get(target, 0) + 1
    for page in pages:
        page["inlinks"] = incoming.get(page["path"], 0)
    count = max(1, len(per_page))
    avg = {name: max(1.0, sum(len(f[name]) for f in per_page) / count) for name in DOCS_FIELDS}
    postings: dict[str, list[str]] = {}
    for doc, fields in enumerate(per_page):
        weighted: dict[str, float] = {}
        for name, (weight, b) in DOCS_FIELDS.items():
            tokens = fields[name]
            if not tokens:
                continue
            norm = 1 - b + b * len(tokens) / avg[name]
            counts: dict[str, int] = {}
            for term in tokens:
                counts[term] = counts.get(term, 0) + 1
            for term, tf in counts.items():
                weighted[term] = weighted.get(term, 0.0) + weight * tf / norm
        for term, value in weighted.items():
            postings.setdefault(term, []).append(f"{doc}:{value:.3f}")
    return {"pages": pages, "postings": {term: " ".join(items) for term, items in postings.items()}}


class DocsIndex:
    """Page index of the Roblox docs mirror (cached). `load` returns None when there is no mirror."""

    def __init__(self, root: Path, data: dict):
        self.root = root
        self.pages: list[dict] = data["pages"]
        self.postings: dict[str, str] = data["postings"]
        self.by_path = {page["path"]: doc for doc, page in enumerate(self.pages)}
        classes = root / DOCS_API_CLASSES
        self.classes = {p.stem for p in classes.glob("*.yaml")} if classes.is_dir() else set()

    @classmethod
    def load(cls, root: Path) -> "DocsIndex | None":
        mirror = root / DOCS_MIRROR
        if not mirror.is_dir():
            return None
        files = _docs_page_files(mirror)
        digest = hashlib.sha1(f"v{DOCS_CACHE_VERSION}\n".encode())
        for rel, size, mtime in files:
            digest.update(f"{rel}|{size}|{mtime}\n".encode())
        signature = digest.hexdigest()
        cache = root / DOCS_CACHE
        try:
            data = json.loads(cache.read_text(encoding="utf-8"))
            if isinstance(data, dict) and data.get("signature") == signature:
                return cls(root, data)
        except (OSError, ValueError):
            pass
        data = _build_docs_index(mirror, files)
        data = {"signature": signature, "note": f"generated by tools/context_packet.py from {DOCS_MIRROR}; safe to delete", **data}
        try:
            cache.parent.mkdir(parents=True, exist_ok=True)
            temp = cache.with_suffix(".tmp")
            temp.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
            os.replace(temp, cache)
        except OSError:
            pass  # read-only checkout: rank from memory this run
        return cls(root, data)

    def cited(self, corpus: Corpus, hits: list[Hit]) -> dict[int, float]:
        """Mirror pages cited by the top kit sections: page -> sum of (section score / top score) / pages cited there."""
        matches = [h for h in hits if h.kind == "match"][:DOCS_CITE_SECTIONS]
        if not matches:
            return {}
        top = matches[0].score
        strength: dict[int, float] = {}
        for hit in matches:
            text = "\n".join(corpus.notes[hit.path].lines[hit.start - 1 : hit.end])
            found: list[int] = []
            for match in DOCS_CITE_RE.finditer(text):
                rel, in_mirror = match.group(1), False
                if "roblox-creator-docs/" in rel:
                    rel, in_mirror = rel.split("roblox-creator-docs/", 1)[1], True
                doc = self.by_path.get(rel + ".md")
                if doc is None and in_mirror and not match.group(2):
                    doc = self.by_path.get(rel + "/index.md")  # [[external/roblox-creator-docs/x]] for a folder index
                if doc is not None and doc not in found:
                    found.append(doc)
            for doc in found:
                strength[doc] = strength.get(doc, 0.0) + (hit.score / top) / len(found)
        return strength

    def rank(self, query: str, limit: int = DOCS_PAGES, cited: dict[int, float] | None = None) -> list[dict]:
        terms = query_terms(ACRONYM_RE.sub(" ", query))
        if not terms or not self.pages:
            return []
        total = len(self.pages)
        scores: dict[int, float] = {}
        matched: dict[int, list[str]] = {}
        for term in terms:
            raw = self.postings.get(term)
            if not raw:
                continue
            items = raw.split(" ")
            idf = math.log(1 + (total - len(items) + 0.5) / (len(items) + 0.5))
            for item in items:
                doc, _, value = item.partition(":")
                tf = float(value)
                key = int(doc)
                scores[key] = scores.get(key, 0.0) + idf * tf * (DOCS_K1 + 1) / (tf + DOCS_K1)
                matched.setdefault(key, []).append(term)
        final: dict[int, float] = {}
        for doc, value in scores.items():
            page = self.pages[doc]
            prior = next((w for prefix, w in DOCS_FOLDER_PRIOR.items() if page["path"].startswith(prefix)), 1.0)
            prior *= 1 + DOCS_INLINK_WEIGHT * math.log1p(page.get("inlinks", 0))
            final[doc] = value * (1 - DOCS_COVERAGE + DOCS_COVERAGE * len(matched[doc]) / len(terms)) * prior
        cited = cited or {}
        if cited:
            best = max(final.values(), default=1.0) or 1.0
            most = max(cited.values())
            for doc, value in cited.items():
                final[doc] = final.get(doc, 0.0) + DOCS_CITE_WEIGHT * best * value / most
        ranked = sorted(final.items(), key=lambda item: (-round(item[1], 9), self.pages[item[0]]["path"]))
        out = []
        for doc, value in ranked[:limit]:
            page = self.pages[doc]
            words = matched.get(doc, [])
            title_terms = set(docs_tokenize(page["title"]))
            reasons = []
            if words:
                in_title = [t for t in words if t in title_terms]
                reasons.append(f"matched {', '.join(words)}" + (f" (title: {', '.join(in_title)})" if in_title else ""))
            if doc in cited:
                reasons.append("cited by top kit notes")
            out.append({"path": f"{DOCS_MIRROR}/{page['path']}", "title": page["title"], "score": round(value, 3), "why": "; ".join(reasons)})
        return out

    def api(self, query: str) -> list[dict]:
        """Exact (case-sensitive) Roblox class names in the task text, in order of first mention."""
        found: list[dict] = []
        for word in IDENT_RE.findall(query):
            if word in self.classes and all(f["class"] != word for f in found):
                found.append({"class": word, "path": f"{DOCS_API_CLASSES}/{word}.yaml"})
        return found


def roblox_docs(root: Path, query: str, limit: int = DOCS_PAGES, index: DocsIndex | None = None, corpus: Corpus | None = None, hits: list[Hit] | None = None) -> dict:
    """The packet's "Roblox docs" part. Pass the kit corpus and its ranked hits to use kit citations."""
    index = index or DocsIndex.load(root)
    if index is None or limit < 1:
        return {"pages": [], "api": []}
    cited = index.cited(corpus, hits) if corpus is not None and hits else {}
    return {"pages": index.rank(query, limit, cited), "api": index.api(query)}


# ---------------------------------------------------------------- role and job blocks
#
# Small, fixed blocks for --role and --job. They read only a few files (no corpus), so the
# SubagentStart hook (tools/hooks/subagent_context.py) can call them on every subagent start.


def cap_lines(lines: list[str], limit: int = BLOCK_MAX_LINES) -> list[str]:
    if len(lines) <= limit:
        return lines
    rest = len(lines) - (limit - 1)
    return lines[: limit - 1] + [f"- … {rest} more lines not shown"]


def role_names(root: Path) -> list[str]:
    """Kit roles: stems of .agents/roles/*.md except README."""
    base = root / ROLES_DIR
    if not base.is_dir():
        return []
    return sorted(p.stem for p in base.glob("*.md") if p.is_file() and p.name.lower() != "readme.md")


def docs_map_rows(root: Path, role: str) -> list[dict]:
    """Rows of the docs map whose first cell names the role (comma-separated names), verbatim."""
    path = root / DOCS_MAP
    if not path.is_file():
        return []
    rows = []
    for number, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), start=1):
        stripped = line.strip()
        if not stripped.startswith("|") or re.fullmatch(r"\|?[\s:|-]+\|?", stripped):
            continue
        first = stripped.strip("|").split("|", 1)[0]
        if role in [name.strip() for name in first.split(",")]:
            rows.append({"line": number, "row": line.rstrip()})
    return rows


def precedent_rows(root: Path, role: str, limit: int = PRECEDENT_ROWS) -> list[dict]:
    """The newest `limit` rows of the precedents register whose Craft cell names the role, verbatim."""
    path = root / PRECEDENTS
    if not path.is_file():
        return []
    rows: list[dict] = []
    craft_at: int | None = None
    for number, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), start=1):
        stripped = line.strip()
        if not stripped.startswith("|") or re.fullmatch(r"\|?[\s:|-]+\|?", stripped):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if craft_at is None:
            craft_at = next((i for i, cell in enumerate(cells) if cell.lower().startswith("craft")), -1)
            continue
        if 0 <= craft_at < len(cells) and role in [name.strip() for name in cells[craft_at].split(",")]:
            rows.append({"line": number, "row": line.rstrip()})
    return rows[-limit:]


def role_info(root: Path, role: str) -> dict:
    """The --role block. Raises ValueError for a name that is not a kit role (or ROLE_ALIASES)."""
    names = role_names(root)
    if role in ROLE_ALIASES and role not in names:
        rel = None
        skills = list(ROLE_ALIASES[role])
    elif role in names:
        rel = f"{ROLES_DIR}/{role}.md"
        meta, _, _ = parse_frontmatter((root / rel).read_text(encoding="utf-8", errors="replace"))
        skills = as_list((meta or {}).get("skills"))
    else:
        known = names + sorted(ROLE_ALIASES)
        raise ValueError(f"unknown role `{role}`; kit roles ({ROLES_DIR}/): {', '.join(known) or 'none'}")
    overlays = [f"{OVERLAYS}/{name}.md" for name in [role] + skills if (root / OVERLAYS / f"{name}.md").is_file()]
    rows = docs_map_rows(root, role)
    precedents = precedent_rows(root, role)
    lines = [
        f"## For role {role}",
        "",
        f"- Role file: `{rel}`" if rel else "- Role file: none (the lead); its book is the skill below",
        f"- Skills (role frontmatter): {', '.join(skills) or 'none'}",
        f"- Overlays: {', '.join(f'`{o}`' for o in overlays) or 'none'}",
    ]
    if rows:
        lines.append(f"- Docs map rows (`{DOCS_MAP}` L{', L'.join(str(r['line']) for r in rows)}):")
        lines += [r["row"] for r in rows]
    else:
        lines.append(f"- Docs map: no row names this role (`{DOCS_MAP}`)")
    if precedents:
        lines.append(f"- Precedents of this role (`{PRECEDENTS}` L{', L'.join(str(r['line']) for r in precedents)}):")
        lines += [r["row"] for r in precedents]
    if (root / VOCABULARY).is_file():
        lines.append(f"- Vocabulary: `{VOCABULARY}` (use its names for states, events, cues and assets)")
    return {"role": role, "file": rel, "skills": skills, "overlays": overlays, "docs_map": rows, "precedents": precedents, "lines": cap_lines(lines)}


def job_folders(root: Path) -> list[str]:
    base = root / JOBS_DIR
    if not base.is_dir():
        return []
    return sorted(p.name for p in base.iterdir() if p.is_dir() and not p.name.startswith((".", "_")))


def resolve_job(root: Path, job: str) -> str:
    """A job folder name from an exact name or a unique prefix. Raises ValueError otherwise."""
    names = job_folders(root)
    if job in names:
        return job
    matches = [name for name in names if job.strip() and name.startswith(job)]
    if len(matches) == 1:
        return matches[0]
    if not matches:
        raise ValueError(
            f"unknown job `{job}`: no folder {JOBS_DIR}/{job}*. Check the id against {JOBS_DIR}/, or create the job folder first "
            "(orchestration skill §3); before it exists, omit --job"
        )
    raise ValueError(f"ambiguous job `{job}`: {', '.join(matches)}; give more of the id")


def _active_folder(root: Path, job: str) -> str:
    """The job folder an active.md id names (exact or unique prefix, as --job); the id itself when no folder matches."""
    try:
        return resolve_job(root, job)
    except ValueError:
        return job


def active_jobs(root: Path) -> list[tuple[str, str]]:
    """(job id, title) for each `- <job-id> · <title>` line of knowledge/jobs/active.md, in file order."""
    path = root / ACTIVE_JOBS
    if not path.is_file():
        return []
    found: list[tuple[str, str]] = []
    in_fence = False
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        match = ACTIVE_JOB_RE.match(line)
        if match and not in_fence:
            found.append((match.group(1), match.group(2).strip()))
    return found


def file_revision(path: Path) -> str | None:
    """Revision of a job file: frontmatter `revision:`, a "> Revision:" / "Revision:" line, or JSON "revision"."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    if path.suffix == ".json":
        try:
            data = json.loads(text)
        except ValueError:
            return None
        value = data.get("revision") if isinstance(data, dict) else None
        return str(value) if isinstance(value, (str, int, float)) and not isinstance(value, bool) else None
    meta, _, _ = parse_frontmatter(text)
    value = (meta or {}).get("revision")
    if value not in (None, "", []):
        return clip(", ".join(value) if isinstance(value, list) else str(value), 80)
    for line in text.lstrip("﻿").splitlines():
        match = REVISION_LINE_RE.match(line)
        if match:
            return clip(match.group(1), 80)
    return None


def file_marked(path: Path) -> bool:
    """`held_out: true` in a markdown file's frontmatter (JSON job files carry no frontmatter)."""
    if path.suffix != ".md":
        return False
    try:
        return marked_held_out(parse_frontmatter(path.read_text(encoding="utf-8", errors="replace"))[0])
    except OSError:
        return False


def job_info(root: Path, job: str) -> dict:
    """The --job block. `job` is an id or unique prefix; raises ValueError when unknown or ambiguous."""
    name = resolve_job(root, job)
    folder = root / JOBS_DIR / name
    found: list[str] = []
    for pattern in JOB_FILES:
        matches = []
        for path in folder.rglob(pattern):
            rel = path.relative_to(root).as_posix()
            if path.is_file() and not SKIP_DIRS.intersection(rel.split("/")) and not withheld(rel) and rel not in found and not file_marked(path):
                matches.append(rel)
        found += sorted(matches, key=lambda rel: (rel.count("/"), rel.lower()))
    files = [{"path": rel, "revision": file_revision(root / rel)} for rel in found]
    lines = [f"## Job {name}", "", f"- Folder: `{JOBS_DIR}/{name}/`"]
    lines += [f"- `{f['path']}`" + (f" · revision {f['revision']}" if f["revision"] else "") for f in files]
    if not files:
        lines.append(f"- No canonical job files yet ({', '.join(JOB_FILES)})")
    return {"job": name, "folder": f"{JOBS_DIR}/{name}/", "files": files, "lines": cap_lines(lines)}


# ---------------------------------------------------------------- packet


def build(root: Path, query: str, budget: int = 8000, max_items: int = 12, docs: int = DOCS_PAGES, role: str | None = None, job: str | None = None) -> dict:
    role_part = role_info(root, role) if role is not None else None
    job_part = job_info(root, job) if job is not None else None
    corpus = Corpus(root)
    terms = query_terms(query)
    hits, superseded = rank(corpus, query, role, job_part["job"] if job_part else None)
    docs_index = DocsIndex.load(root) if docs > 0 else None
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
            entry = f".agents/skills/{note.name}/SKILL.md"
            where = "" if hit.path == entry else f"; the match is `{hit.path}` L{hit.start}-{hit.end}"
            read_next.append(f"load skill `{note.name}` ({entry}){where}")
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
    docs_part = roblox_docs(root, query, docs, docs_index, corpus, hits) if docs_index else {"pages": [], "api": []}
    if docs_part["pages"]:
        top_page = docs_part["pages"][0]
        read_next.append(f"open Roblox docs `{top_page['path']}` ({top_page['title']}) before using that engine system")

    packet = {
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
        "roblox_docs": docs_part,
        "decisions": decision_rows(root, terms),
        "code_hints": code_hints(root, terms),
        "agents_sections": agents_headings(root),
        "read_next": read_next,
    }
    if role_part is not None:
        packet["role"] = role_part
    if job_part is not None:
        packet["job"] = job_part
    return packet


def render(packet: dict) -> str:
    out = [
        "# Context packet",
        "",
        f"- Task: {packet['query']}",
        f"- Terms: {', '.join(packet['terms'])}",
        f"- Searched: {packet['searched']['files']} files, {packet['searched']['sections']} sections; budget {packet['budget_tokens']} tokens",
        "- Locations only: source priority (AGENTS.md §0) and decision status still apply.",
        "",
    ]
    for key in ("role", "job"):
        if packet.get(key):
            out += packet[key]["lines"] + [""]
    out += ["## Ranked", ""]
    if not packet["results"]:
        out.append("No matching section.")
    for item in packet["results"]:
        out.append(f"{item['rank']}. `{item['ref']}` L{item['lines'][0]}-{item['lines'][1]} · {item['score']} · {item['why']}")
        for line in item["excerpt"]:
            out.append(f"   > {line}")
    docs_part = packet.get("roblox_docs") or {}
    if docs_part.get("pages") or docs_part.get("api"):
        out += ["", "## Roblox docs", ""]
        for i, page in enumerate(docs_part["pages"], start=1):
            out.append(f"{i}. `{page['path']}` · {page['title']} · {page['why']}")
        out += [f"- API: {item['class']} → {item['path']}" for item in docs_part["api"]]
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
    packet.add_argument("--docs", type=int, default=DOCS_PAGES, help="Roblox docs mirror pages to list (0 = none)")
    packet.add_argument("--json", action="store_true", help="machine-readable output")
    packet.add_argument("--role", help="kit role (.agents/roles/<role>.md) or orchestrator: boost its book and tagged notes, add a 'For role' block")
    packet.add_argument("--job", help="job id or unique prefix (knowledge/jobs/<job-id>/): boost its notes, add a 'Job' block")
    return result


def main(argv: list[str] | None = None) -> int:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    args = parser().parse_args(argv)
    try:
        if args.budget < 200 or args.max < 1:
            raise ValueError("--budget must be >= 200 and --max >= 1")
        packet = build(args.root.resolve(), args.task, args.budget, args.max, args.docs, args.role, args.job)
    except (OSError, ValueError) as error:
        print(f"context_packet: {error}", file=sys.stderr)
        return 2
    sys.stdout.write(json.dumps(packet, indent=2, ensure_ascii=False) + "\n" if args.json else render(packet))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
