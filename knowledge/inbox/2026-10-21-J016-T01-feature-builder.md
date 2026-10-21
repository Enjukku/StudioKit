---
type: lesson
scope: universal
status: draft
updated: 2026-10-21
source: J016-T01 (context packet --role/--job, hooks, workflow sync, verify check f)
supersedes: []
---
> Author: feature-builder · claude-opus-5-5 · high · 2026-10-21

# J016-T01 lessons (context tools and hooks)

| What | Evidence | Lesson |
| --- | --- | --- |
| "Output unchanged without the new flags" was proved two ways: goldens recorded from the pre-change tool on a fixture repo, and old-vs-new runs of `git show HEAD:tools/context_packet.py` on the live repo | `tools/tests/fixtures/context/golden/` (4 files); live repo 15/15 identical | For a "no change by default" rule, record goldens with the old code before the first edit; compare against the HEAD copy on the live repo because parallel chats change the corpus |
| The live gate drifted for reasons outside the change (other chats edited skills, a new job workflow appeared) | old and new `sync_harness --check` gave the same drift report | Before you blame or credit your change for a gate result, run the HEAD version of the tool on the same tree |
| Two planted faults survived the first suite: an off-by-one at exactly 26 lines, and a role check whose removal was hidden by the hook's catch-all | mutation run 21/23, then 23/23 after two tests | Boundary tests at the exact limit; for never-fail code, also assert that a normal skip writes nothing to stderr, or the safety net hides the bug |
| The Bash tool rewrote `\\n` to a newline inside a quoted heredoc and `\\` in echoed JSON | SyntaxError in sync_harness.py; hook got invalid JSON | Write generated files and test payloads with Python files or the Write tool, not shell heredocs |
| A SubagentStop check of `last_assistant_message` cannot see a hand-back sent through a tool | design reading; this harness hands back through `SubagentHandback` | The hand-back hook allows a stop with no message text; test on one real job before turning it on |
