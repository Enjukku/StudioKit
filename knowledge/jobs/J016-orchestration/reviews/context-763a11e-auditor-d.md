---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J016 G3 audit recheck (selective, rules/company.md §7)
supersedes: []
---
> Author: auditor-d · claude-opus-5-5 · high · 2026-10-21

# Recheck: context system @763a11e, by auditor D

This recheck covers only B1-B7, the keep list, and new defects from the fixes (brief J016-A4 recheck). It builds on `context-322c8ad-auditor-d.md`.

Method: I ran the tools at HEAD 763a11e. Other chats left 4 uncommitted edits during the recheck: AGENTS.md, rules/knowledge.md L51 (1 line), and 2 orchestration skill files. The tool code was unchanged. I saved packet output without excerpt lines (`grep -v "^   >"`). I checked withheld paths in JSON output without printing excerpts. I opened no file with "hidden" in its name. Scratch work was in the session scratchpad (`r2/`, `fx2/`, `hooks/`).

```text
<spec>
artifact: context system (tools/context_packet.py, kb_index.py, eval_context.py, tools/hooks/*, improve.md, integrate.md, vault starters)@763a11e
reviewer: auditor-d (general-purpose, opus, high)
looked_at_first: [git diff 322c8ad..763a11e of the tools, hooks and workflows; then my own tool runs; the maker hand-back was not read]
blocking_status:
  - id: B1
    status: closed
    evidence: >
      context_packet.py:150-172 held_out()/withheld(); used in corpus_files L428,443, stem_index L534, link neighbours L555, overlays L729, job block L1253; excerpt guard names_held_out.
      kb_index.knowledge_notes skips cp.held_out; summary_of skips lines that name held-out files.
      I ran 10 packets as --json, 4 of them the old leak queries (modeler eval cases / environment designer eval prompts / analyst rerun q1 /
      "hidden test answers key grades held out" --job J007). In every run there were 0 paths with a "hidden" folder or file part, 0 such paths in the job blocks,
      0 Read-next lines that name one, and 0 excerpts that name one. Generated indexes: 0 rows whose path has a "hidden" part (it was 18).
      The "hidden" words left in the output are headings of visible notes (for example `J007-modeler/eval-gaps.md#hidden-test-gaps-...`).
  - id: B2
    status: closed
    evidence: >
      PROPOSAL_RE context_packet.py (`direction/proposal-*`) is in withheld(). Scratch fixture fx2 with J016-demo/direction/proposal-art-director.md:
      `packet "write the boss intro cutscene direction proposal and storyboard" --role film-director --job J016-demo` → 0 lines naming proposal-
      (rank 1 is now `.agents/roles/film-director.md ... own book of role film-director`).
  - id: B3
    status: closed
    evidence: >
      withheld() drops `_`-named parts under knowledge/. `packet "build a fireball effect and test it in the VFX lab place" --role vfx-designer` → 0 "_moved-from" lines.
      A scratch `knowledge/overlays/_moved-from-other.md` was not ranked either. Only one tracked file outside the docs mirror matches: knowledge/overlays/_moved-from-destruction-simulator.md.
      The docs mirror `_api-reference` still works: "- API: Camera → knowledge/external/roblox-creator-docs/_api-reference/classes/Camera.yaml".
  - id: B4
    status: still open (narrowed)
    closed_parts: >
      The 3 stale anchors are fixed (retrieval.jsonl line 2 `rules/knowledge.md#6`, line 3 `orchestration/SKILL.md#10`, line 7 `company.md#8` + `#12`).
      eval_context takes role/job/forbid per case (12 cases with role, 12 with forbid). A baseline is saved and --compare works:
      `eval_context.py --show 0 --compare knowledge/logs/improve/2026-10-21-retrieval.json` → "overall: 21/31 pass · recall@5 0.613 · recall@10 0.694 · MRR 0.511" / "RESULT: recall@10 held".
    open_part:
      expected: "rules/knowledge.md §9: keep a retrieval change only if the score holds. The baseline must not hide a fall that J016 caused."
      observed: >
        On the original 19 cases, the score is still below the pre-J016 tree. The baseline was saved after the fall, so "held" compares against the lower level.
      evidence: >
        Same 19 cases (`head -19 retrieval.jsonl` → scratch) @763a11e: "14/19 pass · recall@5 0.711 · recall@10 0.737 · MRR 0.670".
        `git archive 322c8ad^` tree: "16/19 pass · recall@10 0.842 · MRR 0.608" (failing there: 1, 10, 16 only).
        New failures since before J016: case 17 "design a new quest system so adding quests is easy" (expects .agents/skills/architecture/SKILL.md) is at rank 182, and it passed before.
        Case 3 "write an intent brief for an animator" (anchor fixed to orchestration §10) is at rank 55; the brief section was at rank 9 before J016.
      smallest_fix: "Find why the architecture skill and orchestration §10 fell (likely the shortened descriptions from J016-T02 or the §10 rename). Fix it, or write the fall down as an accepted trade-off in the J016 decision log. Re-save the baseline only after that."
  - id: B5
    status: closed
    evidence: "integrate.md:13 Inputs adds taste-log.md, precedents.md, vocabulary.md; :17 step 1 Diff covers their new rows. The generated .claude/commands/integrate.md:14,18 matches."
  - id: B6
    status: closed
    evidence: >
      context_packet.precedent_rows() + VOCABULARY line in role_info. precedents.md:13 now defines the Craft cell as kit roles.
      Scratch rows P1 (film-director), P2 (vfx-designer), P3 (film-director, sound-designer): `--role film-director` block →
      "- Precedents of this role (`knowledge/design/precedents.md` L17, L19):" with P1 and P3 only, then "- Vocabulary: `knowledge/design/vocabulary.md` ...".
      Hook on the same root: "Precedents for this role: `knowledge/design/precedents.md` L17, L19" and "Vocabulary: `knowledge/design/vocabulary.md` (use its names)".
  - id: B7
    status: closed
    evidence: >
      subagent_context.py WITHHELD line. Real repo, agent_type sound-designer → 883 chars, including "Withheld on purpose (rules/knowledge.md §3): other leads' direction proposals until synthesis,
      held-out keys (any file with 'hidden' in its name: never open), the maker's hand-back before your first look as a reviewer, other crafts' working files, other games' notes."
findings:
  - id: N1
    class: recommendation
    where: "tools/context_packet.py:111 JOB_BOOST over knowledge/jobs/<job>/reviews/; knowledge/jobs/J016-orchestration/reviews/*.md (committed in 763a11e)"
    expected: "rules/knowledge.md §3 table: a craft step is not given the whole job history. With --job J016, the role's own book ranks first in the pilot."
    observed: "The audit review files quote the audit's own packet queries and paths. With --job J016 they now take the top slots for craft tasks during the J016 pilot."
    evidence: >
      rank 1 = `reviews/context-322c8ad-auditor-d.md#d2-packet-runs-...` for sound-designer (51.554), art-director (27.415) and feature-builder (49.282) with --job J016-orchestration.
      doc-keeper: ranks 3-4 are the same file, and inbox/README.md (rank 11 before) has dropped out of the top 12. Lead (--role orchestrator): ranks 3, 4, 8 and 10 are review files.
    smallest_fix: "Down-weight `*/reviews/*` and `*/exchange/*` unless the role is a reviewer or the task names the review. Or leave out the J016 audit reviews until the pilot ends."
  - id: N2
    class: recommendation
    where: "tools/context_packet.py rank(): seen_copies key (folder, heading) — the R12 fix"
    expected: "Only copies that really repeat are cut. Distinct notes that use the same template headings still rank."
    observed: "The dedupe key is folder + heading only. A distinct lesson draft is dropped when a sibling draft has the same heading. In the current corpus, 135 folder+heading keys are shared by more than one file (knowledge/inbox, .agents/roles, knowledge/reference/vfx and others)."
    evidence: >
      `packet "progression designer owner corrections in the lesson drafts"`: rank 4 = inbox/2026-10-21-J011-lead-build-progression-designer.md#owner-corrections (16.069).
      The sibling inbox/2026-10-21-J011-progression-designer.md "Owner corrections" scores 15.892, above ranks 5-12 (16.06 down to 12.77), but it is not in the list.
      Owner corrections are the most valuable taste data (design-context.md:121). /improve and the doc-keeper look for them.
    smallest_fix: "Cut a sibling only when its section text or excerpt equals the kept one's (the J009 bible-* copies), not on folder + heading alone. Add a test with two inbox drafts."
questions:
  - "Q3: knowledge/jobs/J007-modeler/eval-gaps.md, J014 grades-g2.md '§9 what the key or rubric got wrong' and inbox/2026-10-20-J003-T08-game-designer-case-readings.md ('reading held-out Roblox cases') are visible under LD8, because their names have no 'hidden'. They still rank for eval-shaped queries. Do they quote held-out answers? I did not judge their content; the owner of the held-out sets should."
keep_status:
  - {item: "hooks never fail on bad input", status: holds, evidence: "empty, array, null agent_type, truncated JSON, 0xFF bytes → all 3 scripts rc 0, no stdout, 1 stderr line on decode errors"}
  - {item: "hook output shapes and size", status: holds, evidence: "SubagentStart 883 chars, SessionStart 472 chars; same JSON keys; the 2-job fixture adds 'Several jobs are open. Use the job your brief names; ignore the others.'"}
  - {item: "README settings snippet valid", status: holds, evidence: "snippet block unchanged in the 763a11e diff; it parses as JSON with events SubagentStart, SessionStart, SubagentStop"}
  - {item: "handback_check honours stop_hook_active / non-kit / empty", status: holds, evidence: "st-active, st-gp, st-empty, st-nomsg → no output. Now also passes '**STATUS:', '## STATUS:', '> STATUS:', 'coverage:' as YAML, list item, bold or JSON. Blocks 'Test coverage is low' and 'Line coverage: 80%' prose."}
  - {item: "compact hook open tickets (R3)", status: "holds, new", evidence: "templates/jobs/ledger.md + rows working/done/needs-decision → 'Open tickets: 2'; left out when the job has no ledger.md (J016)"}
  - {item: "packet blocks ≤ 25 lines, clear errors", status: holds, evidence: "sound-designer role block 17 lines; --job J999-nothing → rc 2 'unknown job ... before it exists, omit --job'"}
  - {item: "doc-keeper filing packet ranked well", status: "holds, weaker", evidence: "design §5, rules §7, orchestration §9, doc-keeper role in the top 10; inbox README pushed out by review files (N1)"}
  - {item: "kb_index --lint --check clean", status: holds, evidence: "'check: indexes current', 'lint: 0 errors, 63 warnings'"}
  - {item: "vault starter columns", status: holds, evidence: "precedents.md:15 '| ID | Craft (kit roles) | What it is | Why it was accepted (owner's words) | Path @ revision | Decision | Date |'"}
  - {item: "tests", status: holds, evidence: "`python -m unittest tools.tests.test_context_tools tools.tests.test_hooks -v` → 'Ran 86 tests in 8.859s' / 'OK'"}
  - {item: "--role now ranks the role's own book (R1)", status: "holds, new", evidence: "sound-designer rank 12 `.agents/roles/sound-designer.md ... own book of role sound-designer`; ranks 2, 3, 5, 7 are sound-design references. The film-director role file has left the top 12."}
verdict: fix-first (B4 open part); N1 and N2 can wait until after the pilot
</spec>
```

## Coverage

| Item | Status | How |
| --- | --- | --- |
| B1 | closed | code diff; 10 packet runs as JSON, path checks; generated index scan |
| B2 | closed | scratch fixture with a proposal file |
| B3 | closed | vfx packet; scratch `_moved-from-other.md`; docs `_api-reference` still listed |
| B4 | open (narrowed) | eval at HEAD, 19-case subset vs `git archive 322c8ad^` |
| B5 | closed | integrate.md:13,17 and the generated copy |
| B6 | closed | scratch precedents rows; role block and hook |
| B7 | closed | hook on the real repo |
| keep list | 11 items: 9 hold, 1 holds but weaker, 1 new | see keep_status |
| new defects | N1, N2 (recommendation) | packet runs, section scoring script |
| tests | ran | 86 tests OK |

Packet runs (repo root): sound-designer, film-director, feature-builder, doc-keeper and art-director with `--job J016-orchestration`; film-director without --job; `--job J999-nothing`; vfx-designer; 5 eval-shaped queries (including `--job J007`, `--job J008`, `--job J014`); `--role orchestrator --job J016-orchestration`. All gave rc 0, except J999, which gave rc 2 as expected.

built_on: [763a11e]
