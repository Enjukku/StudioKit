---
type: job   # brief said "review"; rules/knowledge.md §5 has no such type (kb_index --lint ERROR). Lead decides.
scope: universal
status: active
updated: 2026-10-21
source: J016 G3 audit
supersedes: []
---
> Author: auditor-d · claude-opus-5-5 · high · 2026-10-21

# Review: context system @322c8ad, by auditor D

Read-only audit. The tools were run from the repo root, and the scratch inputs were kept in the session scratchpad. Excerpt lines from `hidden-*` files were filtered out of the packet output (`grep -v "^   >"`), so only paths and ranks were seen. No hidden file was opened. Other chats changed the working tree during the audit (`crew.md`, `pilot-plan.md` and C22 in `capability-check.md` were added around 17:00). These changes are not judged here.

```text
<spec>
artifact: context system (rules/knowledge.md, tools/context_packet.py, tools/kb_index.py, tools/eval_context.py, tools/hooks/*, .agents/workflows/improve.md, vault starters)@322c8ad
reviewer: auditor-d (general-purpose, opus, high)
looked_at_first: [design-context.md, rules/knowledge.md, the hook scripts and the packet code, then my own runs of the tools; no maker hand-back read]
findings:
  - id: B1
    class: blocking
    where: "tools/context_packet.py:56-57,378-394 (corpus_files, DEFAULT_EXCLUDE); tools/kb_index.py:58-73,80-92 (knowledge_notes, summary_of)"
    expected: "rules/knowledge.md:51: held-out keys (`hidden-*`) are never opened or listed by content"
    observed: "Neither tool excludes hidden-*. The packet ranks and quotes held-out answers and tells the agent to open them. The generated index lists them with content summaries."
    evidence: >
      `packet "review the character model against the art bible anchors" --role art-director --job J016-orchestration` →
      "1. `knowledge/jobs/J007-modeler/hidden-answers.md#1-diagnosis-separate-defects` L232-240 · 22.476" and Read next
      "- open `knowledge/jobs/J007-modeler/hidden-answers.md` L232-240". `packet "environment designer eval prompts cases"` →
      ranks 1, 2, 3 = J008 hidden-cases.md, hidden-eval-prompts.md, hidden-answers.md. `packet "analyst rerun q1 illustration conversion"` →
      rank 1 `J013-analyst/analyst/hidden-rerun/q1.md`. knowledge/generated/index-jobs.md: 18 hidden-* rows, each with a summary cell of 18-140 chars
      taken from the note's first sentence. grep "hidden" in context_packet.py, kb_index.py, eval_context.py: no match. No test covers it (grep in test_context_tools.py: none).
    smallest_fix: "Skip any path with a part that starts with `hidden-` in corpus_files and in Corpus.stem_index. In kb_index, list such notes by path only (no summary), or skip them. Add one test per tool."
  - id: B2
    class: blocking
    where: "tools/context_packet.py:111,595-599 (JOB_BOOST on the job folder) with .agents/workflows/jobs/job-character.js:151,122,280-282 (same pattern in all 7 job-*.js)"
    expected: "rules/knowledge.md:47 and rules/messages.md:89: a direction lead does not get the other leads' proposals during D1"
    observed: "Every D1 brief carries `packet ... --job <job>` and the rule 'Run the context packet'. Proposals are written in parallel to `<job>/direction/proposal-<role>.md`. The packet gives that folder a 1.5x boost and has no exclusion, so a lead that runs the packet after a peer has written its proposal gets that proposal at the top."
    evidence: >
      Scratch copy of tools/tests/fixtures/context/repo plus `knowledge/jobs/J016-demo/direction/proposal-art-director.md`:
      `context_packet.py --root <scratch> packet "write the boss intro cutscene direction proposal and storyboard" --role film-director --job J016-demo` →
      "1. `knowledge/jobs/J016-demo/direction/proposal-art-director.md#direction-proposal-art-director` L9-13 · 16.821 · ... in job J016-demo"
      and Read next "- open `knowledge/jobs/J016-demo/direction/proposal-art-director.md` L9-13".
    smallest_fix: "Never rank `*/direction/proposal-*.md` in the packet. The D2 exchange brief already names these files by path in `inputs` (job-character.js:292). Add a test."
  - id: B3
    class: blocking
    where: "knowledge/overlays/_moved-from-destruction-simulator.md:1-6 (scope: game, source: moved from DestructionSimulator); tools/context_packet.py (no scope filter)"
    expected: "rules/knowledge.md:52: every game is withheld other games' facts (scope: game)"
    observed: "A game-scoped note from another game is in the kit corpus. The packet ranks it first for a normal VFX task. When a game copies the kit, the note goes with it."
    evidence: >
      `packet "build a fireball effect and test it in the VFX lab place" --role vfx-designer` →
      "1. `knowledge/overlays/_moved-from-destruction-simulator.md#moved-from-destructionsimulator-game-specific-lines-removed-from-the-vfx-and-sound-material` L9-16 · 19.001".
    smallest_fix: "Move the file out of the packet corpus (for example under an excluded kit-history path), or exclude `knowledge/overlays/_*` in DEFAULT_EXCLUDE. Owner or lead picks the place."
  - id: B4
    class: blocking
    where: "tools/eval_context.py (whole file); knowledge/evals/retrieval.jsonl:2,3,7"
    expected: "design-context.md:85,157: eval_context gets per-role cases and --role/--job. rules/knowledge.md:113: run the eval before and after any change to retrieval; keep the change only if the score holds."
    observed: "eval_context.py has no role or job input (grep role|job: no match), and retrieval.jsonl has 0 cases with a role. J016 renumbered sections but did not update the expected anchors. The score fell and no record of a before/after run was found."
    evidence: >
      `python tools/eval_context.py --show 0` @322c8ad → "overall: 12/19 pass · recall@5 0.632 · recall@10 0.684 · MRR 0.541".
      Same tool on `git archive 322c8ad^` (scratch) → "overall: 16/19 pass · recall@5 0.711 · recall@10 0.842 · MRR 0.608".
      Cases that changed from pass to fail: 2 (expects rules/knowledge.md#4; §4 is now "Passing context", the placement table is §6), 3 (expects orchestration SKILL.md#3; §3 is now "Opening a job",
      briefs are §10), 7 (expects rules/company.md#5 + orchestration#6; statuses are now company §8, orchestration §12). grep "recall@" in knowledge/: no saved result for J016.
    smallest_fix: "Fix the 3 stale anchors (#6, #10, #8/#12) and re-run. Then let a case carry `role`/`job` and pass them to cp.build, and add one case per pilot role (this is the J016-T01 ticket the design names)."
  - id: B5
    class: blocking
    where: ".agents/workflows/integrate.md:12-14 (Inputs)"
    expected: "rules/knowledge.md:102 and design-context.md:125: /integrate turns new decisions, taste and precedents into overlays. taste-log.md:13: '/integrate turns repeated entries into overlays'."
    observed: "The /integrate inputs are game-profile.md, decisions.md, design notes and owner-profile.md. taste-log.md, precedents.md and vocabulary.md are not named, so the step that moves taste into overlays does not exist. J016 did not change integrate.md (git show --stat 322c8ad)."
    evidence: "grep -n 'taste|precedent|vocabulary' .agents/workflows/integrate.md → only L19 'Style and taste for this game' (an overlay section heading, not an input)"
    smallest_fix: "Add `knowledge/design/taste-log.md`, `precedents.md` and `vocabulary.md` (rows since the last run) to Inputs and to step 1 Diff."
  - id: B6
    class: blocking
    where: "knowledge/design/precedents.md:13; tools/context_packet.py:1045-1067 (role_info); .agents/roles/*.md"
    expected: "precedents.md:13 'Agents read the rows of their craft before they start'. design-context.md:71: the --role packet adds the precedents tagged with that role. Vocabulary is 'one name per thing across crafts' (design-context.md:118)."
    observed: "Nothing carries this: precedents.md is one table, so its rows cannot carry a `roles:` tag. role_info adds no precedents or vocabulary. The hook does not name them. Only 2 role files name precedents (art-director, doc-keeper), and vocabulary.md is named only by doc-keeper.md and the orchestration skill."
    evidence: "grep -l precedents .agents/roles/*.md → art-director.md doc-keeper.md; grep -l vocabulary.md .agents/roles/*.md .agents/skills/*/SKILL.md → doc-keeper.md, orchestration/SKILL.md"
    smallest_fix: "In role_info, add the precedents.md rows whose Craft cell names the role (same pattern as docs_map_rows), plus one line that names vocabulary.md. The hook reuses role_info, so it gets both."
  - id: B7
    class: blocking
    where: "tools/hooks/subagent_context.py:101-123; tools/hooks/README.md:9"
    expected: "design-context.md:91: the SubagentStart hook injects '... the withheld-context rule for that step'"
    observed: "The injected text has the overlays, the docs-map line, the job files and the Run line, but no withheld-context line"
    evidence: "SubagentStart input {agent_type: sound-designer} → 554 chars: 'Studio Kit context for role sound-designer ... Role overlays: none / Docs map row: ... L25 / Active job J016-orchestration ... / Run: python tools/context_packet.py packet \"<your task>\" --role sound-designer --job J016-orchestration'"
    smallest_fix: "Add one static line: 'Withheld on purpose (rules/knowledge.md §3): other leads' proposals, hidden-* files, the maker's hand-back before your first look, other games' notes.'"
  - id: R1
    class: recommendation
    where: "tools/context_packet.py:110,594-597 (ROLE_BOOST only for `roles:` tags)"
    expected: "design-context.md:16 (§0 line 2): 'a context packet built for its role and job'"
    observed: "No vault note has a `roles:` tag (grep '^roles:' → only the examples in inbox/README.md and rules/knowledge.md), so --role changes nothing in the ranking. Other roles' identity files rank above the role's own book."
    evidence: "diff of the ranked lines for 'design the boss entrance stinger and reveal cue sounds' with and without --role sound-designer → IDENTICAL. With --role: rank 3 `.agents/roles/film-director.md`, rank 5 `.agents/skills/film-direction/SKILL.md`, and Read next '- open `.agents/roles/film-director.md` L10-14'."
    smallest_fix: "When --role is set, boost the role file and its frontmatter skills x ROLE_BOOST and down-weight other `.agents/roles/*.md` files. Measure with B4's per-role cases."
  - id: R2
    class: recommendation
    where: "tools/hooks/subagent_context.py:112-122"
    expected: "one job pointer, the agent's job (design-context.md:91 'active job id')"
    observed: "Every kit role gets one block and one Run line for each active job. With parallel jobs, the agent cannot tell which job is its own."
    evidence: "scratch fixture with 2 lines in active.md → 'Run: ... --job J016-demo' and 'Run: ... --job J017-other' in one SubagentStart output"
    smallest_fix: "When more than 1 job is listed, add a lead line: 'Use the job your brief names; ignore the others.'"
  - id: R3
    class: recommendation
    where: "tools/hooks/compact_context.py:231-258"
    expected: "design-context.md:92: after compaction, open jobs, gate states, open tickets, next step"
    observed: "Status row + undated gate rows + re-load line; no open tickets from ledger.md"
    evidence: "SessionStart {source: compact} → 472 chars: Job J016 · Status row · 'Open gate: | G3 audit + pilot | | |' · 'Re-load the orchestration skill before the next step.'"
    smallest_fix: "Add 'open tickets: n (ledger.md)' per job, or record in README.md:10 that the scope is narrower on purpose."
  - id: R4
    class: recommendation
    where: "tools/hooks/handback_check.py:323-326"
    expected: "a hand-back with a `coverage` list (rules/messages.md §3)"
    observed: "Any 'coverage' substring passes. A markdown-bold first line is sent back."
    evidence: "last_assistant_message 'STATUS: done. Test coverage is low, I skipped the list.' → no output (stop allowed); '**STATUS: done.** ...\\n\\ncoverage: all' → {\"decision\": \"block\", ...}"
    smallest_fix: "Match `(?im)^\\s*[-*]*\\s*coverage\\s*:` and strip leading `*`/`#` from the first line before the STATUS test"
  - id: R5
    class: recommendation
    where: "knowledge/jobs/README.md:42; knowledge/jobs/active.md:13; knowledge/index.md:22"
    expected: "true statements about which tools read active.md"
    observed: "All three say context_packet.py --job reads active.md. It does not: --job resolves the folder (context_packet.py:1077-1088). Only the hooks call active_jobs."
    evidence: "grep 'active_jobs(' → context_packet.py:1090 (def), compact_context.py:77, subagent_context.py:43,62"
    smallest_fix: "Change the text to 'the hooks read it'"
  - id: R6
    class: recommendation
    where: ".agents/workflows/improve.md:5; tools/kb_index.py:16"
    expected: "cross-references to the current section numbers"
    observed: "improve.md:5 'learning loop (`rules/knowledge.md` §5)'; the loop is §8 and §5 is Notes. kb_index.py:16 'Lint (rules/knowledge.md §3)'; the lint is in §9."
    evidence: "rules/knowledge.md:60 '## 5. Notes', :104 '## 8. The learning loop', :111 '## 9. Retrieval and context health'"
    smallest_fix: "Edit the two section numbers"
  - id: R7
    class: recommendation
    where: ".agents/workflows/improve.md:16 (step 1.4 'score vs last week')"
    expected: "a saved score to compare with"
    observed: "No path for the saved result. eval_context.py already has --save/--compare (eval_context.py:169-170)."
    evidence: "knowledge/logs/ does not exist; grep 'recall@' in knowledge → no saved result"
    smallest_fix: "Step 1.4: `eval_context.py --compare <last>.json --save knowledge/logs/improve/<date>-retrieval.json`"
  - id: R8
    class: recommendation
    where: "rules/knowledge.md:109; .agents/workflows/improve.md:19"
    expected: "an agent can find 'the capability record' and the probe steps"
    observed: "No path is named, and no probe procedure is written. The only record is knowledge/jobs/J016-orchestration/capability-check.md, which is an L3 job file. The probes exist only as prose in C01/C03."
    evidence: "grep 'capability record|capability probe' → only rules/knowledge.md:109, improve.md:19,34, rules/assistants/claude.md:34; no file in tools/ matches 'probe'"
    smallest_fix: "Name the path. At J016 close, file capability-check.md to knowledge/reference/studio/ and give it a 3-line probe recipe."
  - id: R9
    class: recommendation
    where: "rules/knowledge.md:105; knowledge/inbox/README.md:30; templates/jobs/evidence.md:25; .agents/workflows/improve.md:25-39"
    expected: "one cause vocabulary that maps 1:1 to the routing rows"
    observed: "The labels drift: 'defect found by the owner after internal review' (rules), 'found by the owner after internal review' (inbox, evidence), 'Interface conflict found late' (improve). The improve step 2 table has no `win` row; wins are handled in step 3 2b (improve.md:48)."
    evidence: "see the lines cited"
    smallest_fix: "Copy the rules list word for word into the improve table, and add a `win` row → 'step 3 2b'"
  - id: R10
    class: recommendation
    where: "knowledge/design/decisions.md:5; knowledge/index.md:5"
    expected: "`updated:` is the date of the last edit (rules/knowledge.md §5)"
    observed: "Both files show 2026-10-20, but commit 322c8ad (2026-10-21) edited them"
    evidence: "git show --stat 322c8ad → knowledge/design/decisions.md | 6 +-, knowledge/index.md | 6 +"
    smallest_fix: "Set updated: 2026-10-21"
  - id: R11
    class: recommendation
    where: "knowledge/index.md:15-34"
    expected: "rules/knowledge.md:26: index.md → area index → note"
    observed: "index.md has no link to knowledge/generated/index-<area>.md"
    evidence: "grep generated knowledge/index.md → none"
    smallest_fix: "Add one row: 'Area indexes | generated/index-<area>.md'"
  - id: R12
    class: recommendation
    where: "tools/context_packet.py:617-623 (PER_NOTE_CAP per note only)"
    expected: "12 ranked slots that are not near-duplicates"
    observed: "Four sibling files with the same section use 4 of the 12 slots"
    evidence: "art-director packet ranks 9-12: J009-art-director/art/style-probe/bible-{anime,b-screenshot,cartoon,claytoy}.md#families, each 18.478"
    smallest_fix: "Drop a hit whose score and heading equal an earlier hit's"
  - id: R13
    class: recommendation
    where: "tools/context_packet.py:56 (.agents/skills is in the corpus, evals/ included)"
    expected: "eval prompts do not act as task context"
    observed: "The skill eval briefs rank high for real tasks"
    evidence: "feature-builder packet rank 1 `.agents/skills/orchestration/evals/briefs.md#e-02-brief-a-builder-on-money-code`; art-director rank 7 `.agents/skills/art-review/evals/briefs.md`"
    smallest_fix: "Down-weight or exclude `*/evals/*` (do it with B1)"
  - id: R14
    class: recommendation
    where: "rules/knowledge.md:29; design-context.md:95 '(exists)'"
    expected: "the path-rules layer exists"
    observed: ".claude/rules/ does not exist"
    evidence: "ls .claude/rules → No such file or directory"
    smallest_fix: "Add '(none yet)' to the row"
  - id: R15
    class: recommendation
    where: "rules/knowledge.md:14,80-97,102; .agents/skills/orchestration/SKILL.md:80"
    expected: "a path for each asset catalog (models, sounds, VFX textures, kit pieces; design-context.md:59)"
    observed: "§6 has no catalog row. The only catalog is content/vfx/library/catalog.json, so the doc-keeper has no target for models, sounds or kit pieces."
    evidence: "git ls-files | grep -i catalog → content/vfx/library/catalog.json, tools/vfx/vfxlib_catalog.py only (outside the docs mirror)"
    smallest_fix: "Add a §6 row 'Asset catalogs | content/<kind>/library/catalog.json (created with the first asset of a kind)'"
  - id: R16
    class: recommendation
    where: "rules/knowledge.md:15; knowledge/jobs/README.md:44-56; context_packet.py:113 JOB_FILES"
    expected: "every L3 file named in §1 has a file name"
    observed: "'dependency map' has no file name, no template and no JOB_FILES entry"
    evidence: "ls templates/jobs → no dependency file"
    smallest_fix: "Name it (for example a section of direction.md) or remove it from the L3 row"
  - id: R17
    class: recommendation
    where: "tools/verify.py:6-14"
    expected: "design-context.md:93: 'steps and rules in the first 5,000 tokens' has a gate check"
    observed: "No check exists. The rule holds today: every SKILL.md is under 20,000 chars (the largest is orchestration at 13,690)."
    evidence: "wc -c .agents/skills/*/SKILL.md > 20000 → none"
    smallest_fix: "Add a gate check that warns when a SKILL.md is over 20,000 chars, or mark the rule as manual"
  - id: R18
    class: recommendation
    where: "rules/knowledge.md:107; .agents/workflows/improve.md:32"
    expected: "a named place for 'seeded faults for reviewer evals'"
    observed: "No store is named. The reviewer's evals are at .agents/skills/code-review/evals/briefs.md."
    evidence: "grep -i 'seeded fault' → only rules/knowledge.md:107 and improve.md:32"
    smallest_fix: "Name `.agents/skills/code-review/evals/briefs.md` (or the craft's art-review evals) as the place"
questions:
  - "Q1: Are `grades-hidden.md`, `evals-hidden.md` and `grade-J013-hidden.md` held-out keys? The names do not start with `hidden-`, but `J007-modeler/grades-hidden.md` ranks 3rd for 'modeler eval cases answers grades'. If yes, the B1 pattern must be `*hidden*`."
  - "Q2: Do kit job folders (e.g. J003 g2/concepts/*.md, scope: game) travel into each new game? If yes, B3 also covers them."
keep:
  - "All 3 hooks never fail: empty, malformed, array, null agent_type and non-UTF-8 input each give exit 0, no stdout, at most one stderr line. Each run takes about 0.15 s."
  - "Hook output shapes match the docs: hookSpecificOutput.additionalContext for SubagentStart/SessionStart, top-level decision/reason for SubagentStop. Output is under the 2,000-char preview (554 and 472 chars on the real repo)."
  - "The README settings snippet is valid for the current docs (code.claude.com/docs/en/hooks, read 2026-10-21): exec form with `args`, `${CLAUDE_PROJECT_DIR}` passed with no quoting, `.exe` needed on Windows, `shell` ignored with args. `py -3` also runs the scripts."
  - "handback_check honours stop_hook_active and skips non-kit agents and empty messages (for SubagentHandback-style hand-backs)."
  - "Packet role and job blocks are capped at 25 lines. An unknown role, an unknown job or an ambiguous prefix gives exit 2 with a helpful list. Superseded notes are skipped. Output is 7.1-8.4 K chars."
  - "The doc-keeper packet for filing a job is ranked very well (design §5, rules §7, orchestration §9 and inbox README all in the top 11)."
  - "kb_index --lint --check: 0 errors, indexes current."
  - "Vault starters match rules §5-§7: decisions has 'revisit when', tried-and-failed has 'retry only if', precedents has what / why (owner's words) / path@revision. Types match the §6 table. The active.md shape matches ACTIVE_JOB_RE."
  - "The evidence.md metrics table matches orchestration §9.7 and improve step 1.5."
verdict: fix-first
</spec>
```

## Coverage

| Check | Status | How |
| --- | --- | --- |
| D1 rule owners | checked | Each section of rules/knowledge.md §1-§9 traced to its tool, template or step (table below) |
| D2 packet triples | checked | 9 runs on the real repo + 1 on a scratch fixture; outputs saved in the scratchpad (p-*.txt) |
| D3 hooks | checked | 13 realistic and 6 malformed inputs; README snippet compared with code.claude.com/docs/en/hooks (2 fetches). Not applied. |
| D4 improve.md | checked | Every step's tools exist and the flags match (improve_scan --since, agent_scorecard --days --json, eval_context, kb_index --lint). Gaps: R6-R9. |
| D5 vault files | checked | Columns, frontmatter and types vs §5-§7; R10, R11 |
| D6 indexes current | checked | `python tools/kb_index.py --lint --check` → "check: indexes current", "lint: 0 errors, 71 warnings", rc 0 (no-write mode, read in kb_index.py:246-273) |
| D7 tests | checked | `python -m unittest tools.tests.test_context_tools tools.tests.test_hooks -v` → "Ran 64 tests in 5.452s" / "OK" |

### D1: rules/knowledge.md, rule → owner

| Rule (line) | Owner | State |
| --- | --- | --- |
| §1 L12-16 writers per layer | orchestration §9 + doc-keeper.md:19 (L2 filing); integrate.md (overlays); improve step 3 (lessons) | overlays partly: B5 |
| §1 L19 memory as dated topic files | rules/assistants/claude.md Memory table (L0) | manual, honest |
| §2 L25 always ≤ 200 lines; L28 SKILL ≤ 500, description ≤ 400 | verify.py checks d, e, f | ok |
| §2 L28 steps in the first 5,000 tokens | none | R17 (holds today) |
| §2 L26 index routing | knowledge/index.md | R11 |
| §2 L29 path rules | none exist | R14 |
| §3 L38 --role / --job packet | context_packet.py role_info / job_info | works; ranking is inert: R1, B6 |
| §3 L42 SubagentStart pointer | subagent_context.py | works; B7, R2 |
| §3 L47 no other leads' proposals | brief rule (messages.md:89, job-*.js avoid) | the packet leaks them: B2 |
| §3 L48 reviewer sees the artifact first | orchestration §7.2, review template `looked_at_first` | ok (hand-backs are not files) |
| §3 L49 creative review by a fresh instance | recipes | not checked (outside scope_files) |
| §3 L50 no other crafts' working files | none; the packet surfaces J015 brief-vfx.md / cue-sheet.md for sound-designer | no tool; mentioned under R1 |
| §3 L51 hidden-* | none | B1 |
| §3 L52 other games' facts | none | B3 |
| §4 L55-58 revisions, built_on, stale, compaction | messages.md §2-§5, handback.schema.json (built_on ×3), compact_context.py | ok; R3 |
| §5 frontmatter, superseded, revision | kb_index lint; packet skips superseded; file_revision() | ok |
| §6 placement | vault starters exist | catalogs: R15 |
| §7 filing at close | orchestration §9, doc-keeper.md:19 | ok; /integrate: B5 |
| §8.1 capture with cause and layer | inbox/README.md:30-31, templates/jobs/evidence.md §3-§4 | ok; R9 |
| §8.2 routing table | improve.md step 2 | ok; R9 |
| §8.3 retrieval case per "context missed" | improve.md:27 | ok; per-role eval missing: B4 |
| §8.3 seeded faults | improve.md:32 | no store named: R18 |
| §8.3 scorecard | tools/agent_scorecard.py, improve step 6b | ok |
| §8.4 kit-sync | .agents/workflows/kit-sync.md | ok |
| §8.5 probes after an update | improve.md step 1.7 | no path or recipe: R8 |
| §9 kb_index lint | kb_index.py + verify b | ok |
| §9 eval before/after | eval_context.py | score fell, cases stale: B4 |

### D2: packet runs (repo root, PYTHONIOENCODING=utf-8)

| # | Command (`python tools/context_packet.py packet ...`) | rc | chars / lines | Judgment |
| --- | --- | --- | --- | --- |
| 1 | "audit the context system" --job J016-orchestration | 0 | — | J016 decisions, job card, design §5 ranked 1-3; good |
| 2 | "design the boss entrance stinger and reveal cue sounds" --role sound-designer --job J016-orchestration | 0 | 8395 / 79 | Role block ok (docs row L25). Ranks 3 and 5 belong to the film-director role and skill (R1). The role's own skill is at rank 2. |
| 3 | "storyboard the boss entrance cutscene and time the animatic" --role film-director --job J016-orchestration | 0 | 8325 / 77 | Good: role file, J015 decisions, film-craft |
| 4 | "add a server-validated shop purchase remote with receipt saving" --role feature-builder --job J016-orchestration | 0 | 8010 / 77 | Rank 1 is an eval brief (R13). Otherwise handoffs, networking-security, data-saving: good. |
| 5 | "file the job into the vault: precedents vocabulary taste log" --role doc-keeper --job J016-orchestration | 0 | 7372 / 78 | Very good |
| 6 | "review the character model against the art bible anchors" --role art-director --job J016-orchestration | 0 | 8362 / 80 | Rank 1 is hidden-answers.md (B1). Ranks 9-12 are duplicates (R12). |
| 7 | "storyboard the boss entrance cutscene" --role film-director (no --job) | 0 | 7108 / 69 | Role block present, no job block; good |
| 8 | same task, --job J999-nothing | 2 | 0 | "unknown job `J999-nothing`: no folder knowledge/jobs/J999-nothing*"; good |
| 9 | --role animator / --job J01 | 2 | 0 | unknown role lists 24 roles; ambiguous prefix lists 7 jobs; good |
| 10 | "build a fireball effect and test it in the VFX lab place" --role vfx-designer | 0 | — | Rank 1 is another game's overlay (B3) |
| 11 | 3 eval-shaped queries (paths only) | 0 | — | hidden-* files at ranks 1-5 (B1) |
| 12 | scratch fixture, --role film-director --job J016-demo | 0 | — | Rank 1 is another lead's proposal (B2); hidden-answers at rank 6 |

### D3: hook runs (stdin JSON in the scratchpad hooks/ folder)

| Script | Input | rc | stdout | Matches README / C15 / C17 |
| --- | --- | --- | --- | --- |
| subagent_context | agent_type sound-designer / film-director / doc-keeper (full common fields, Windows backslash paths) | 0 | JSON, 554 / 552 / 568 chars | yes (B7: withheld line missing) |
| subagent_context | general-purpose, Explore, null, `[1,2]`, empty, truncated JSON, 0xFF bytes | 0 | none; stderr 1 line for the decode errors | yes |
| compact_context | source compact | 0 | JSON, 472 chars, re-load line last | yes (R3) |
| compact_context | startup, resume, array, empty, bad JSON | 0 | none | yes |
| handback_check | STATUS + coverage | 0 | none | yes |
| handback_check | no STATUS; STATUS without coverage; bold STATUS | 0 | decision block | yes; bold is strict (R4) |
| handback_check | "coverage" only as prose | 0 | none | weak (R4) |
| handback_check | stop_hook_active true; general-purpose; empty message; no message | 0 | none | yes |
| settings snippet | README:19-45 vs docs | — | — | valid (exec form, args, timeout); not applied |

built_on: [322c8ad]
