---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J016 G3 recheck
supersedes: []
---
> Author: rechecker · claude-opus-5-5 · high · 2026-10-21

# Recheck: repair round 1 @d2d0601, by the rechecker

Selective recheck (brief J016-A6, `rules/company.md` §7). It covers only the repair-round items listed in the brief, a seam check of the shared labels, and the gate. I opened the files and ran the tools before I read any commit message. Line numbers are at d2d0601; the working tree was clean at the start and after the gate. Short paths: `cut`, `chr`, `stg`, `ui`, `fea`, `eff`, `mkt` = `.agents/workflows/jobs/job-<type>.js`; `SKILL` = `.agents/skills/orchestration/SKILL.md`; `jt` = its `references/job-types.md`. Harness = `node tools/workflows/wf_harness.mjs` with fake agents. I opened no file whose name contains "hidden" and no note marked `held_out: true`; held-out exclusion was checked on paths only (marked files identified from `git diff --numstat` path lists, not their content).

```text
<spec>
artifact: StudioKit@d2d0601 (repair round 1 of J016 G3; diff 763a11e..d2d0601, 88 files)
reviewer: rechecker (general-purpose, opus, high)
looked_at_first: [git diff 763a11e..d2d0601 of rules, skills, roles, templates, workflows and tools; the five 763a11e review files for the finding texts; harness runs (14 scenarios); eval_context runs; 4 packet runs as JSON and text; python tools/verify.py]
tests: "python tools/verify.py → PASS tests: Ran 641 tests · RESULT: PASS"

recheck:
  # auditor A (core rules)
  - {id: A-N01, state: closed, evidence: "SKILL:112 '`needs-decision`: the lead first decides what is its own (rules/company.md §3, §8); only scope, taste or budget goes into the owner digest'. Matches SKILL:67, SKILL:114 and company.md:107, :117. No other needs-decision routing line in SKILL."}
  - {id: A-N02, state: closed, evidence: "SKILL:62 'One Studio driver (read or write) at a time'. Matches company.md:64, :135 and AGENTS.md:46. The other files that still say 'writer' are RC-N2 (wording only)."}
  - {id: A-N03, state: closed, evidence: "AGENTS.md:21 'the lead uses `--role orchestrator`'. Matches rules/knowledge.md:38 and tools/context_packet.py:137 ROLE_ALIASES. Run: --role orchestrator exit 0."}
  - {id: A-N04, state: closed, evidence: "jt:99 'one capture at the game camera in a busy scene, with the temporary sound's cue times in the Output log (MCP captures are stills; listening is owner-confirmed)'; jt:101 'sound sync from the Output log cue times (listening: owner-confirmed)'. Both match jt:16. Residual: jt:31 (RC-N7, not in the N04 fix)."}
  # auditor B (workflows)
  - {id: B-F11, state: closed, evidence: "chr:375 '2-3 directions, each with pictures on disk or rows in a pending prompts file'; stg:435 '2-3 looks, each with pictures on disk or rows in a pending prompts file'; ui:305 '2-3 style targets, each with pictures on disk or rows in a pending prompts file'. This is the wording of cut:283 and eff:285."}
  - {id: B-N1, state: closed, evidence: "ui:504 'the stage stops after this step ... Nothing is implemented on placeholder art'; ui:509-510 pendingStop when figma.images.state is pending. Harness ui-screen build M, images pending → blocked after 6 agents, last label 'ui-ux-designer: B1-figma', images_pending [B1 Figma build and handoff]; no implementation, code review or capture ran."}
  - {id: B-N2, state: closed, evidence: "Every D3 sign intent now says 'Where pictures are still pending (prompt rows only), judge the prompt rows against the art bible and write in your sign file that the look is judged again on the images in the gate packet': cut:290, chr:382, stg:443, ui:312, eff:292, mkt:346 (mkt also: 'for roughs still pending, their prompt rows')."}
  - {id: B-N3 + E-N-03, state: closed, evidence: "chr:423 rule 'the stage stops after this step: nothing is built from an unapproved view'; chr:441-442 pendingStop('reference set') for L and M. cut:371-381: P4-boards runs first and alone, then pendingStop('storyboards') before probes, greybox, temp cues and animatic; jt:25 'storyboards first (a pending board batch stops the proof before the animatic)'. Harness, images pending: character build M → blocked, 2 agents (P1-reference-set, P1-gameplay-sheet); character proof L → blocked, 2 agents; cutscene build M → blocked, 7 agents (last P4-boards); cutscene proof L → blocked, 7 agents. 'at G2' text: only chr:1060 and cut:863, both inside the STAGE === 'proof' branch, which M cannot reach (chr:66, cut:52 refuse proof for M). The old chr 'the lead shows the pending batch at G2' line is gone. Same gap in fea M: RC-N1."}
  - {id: E-N-07, state: closed, evidence: "Every image step names image-prompts.md: cut:242, :373; chr:338, :417; stg:398, :658; ui:254, :503; fea:396, :405; eff:249; mkt:181 ('image-prompts.md next to this step's deliverable'). No 'prompts-art-director.md', 'refs/prompts.md' or 'prompts-build.md' is left in .agents/workflows, rules, templates or tools. Matches reference-images SKILL.md:38. Residual in skills the brief cites: RC-N3."}
  # auditor C (roles, templates)
  - {id: C-NB1, state: closed, evidence: "A script compared the lists: rules/knowledge.md:109, knowledge/inbox/README.md:33, templates/jobs/handback.schema.json:159 and the LESSON enum of all seven workflows (chr:110, cut:105, eff:102, fea:91, mkt:117, stg:101, ui:96) have the same 10 labels, with 'defect found by the owner after internal review'. templates/jobs/evidence.md:25 has the same 9 defect causes (no 'win', which is not a defect cause). The .claude/workflows copies match (sync_harness --check PASS)."}
  - {id: C-NR1, state: closed, evidence: "architect.md:22 names the cutscene needs round, the D1 probes before the animatic review, contract-player.md after G2, and contract-wiring.md beside rig-pipeline S0 in a playable character job. architect.md:46 write scope adds 'the job's code contracts (contract-player.md, contract-wiring.md) at the job folder root'. Matches jt:25-27, jt:42, chr P1-wiring-contract."}
  - {id: C-NR2, state: closed (template), evidence: "templates/jobs/contract-header.md:17 'Owner (one writer) | <role>; the one exception is the Code file owners section below, written by the architect (rules/company.md §4 step 4)'; company.md:60 step 4 gives that section to the architect. Residual: the rules/knowledge.md:15 L3 writer cell, which the NR2 smallest fix also named, is unchanged (RC-N6)."}
  - {id: C-NR3, state: closed, evidence: "environment-designer.md:23, sound-designer.md:24 and vfx-designer.md:24 name the cutscene needs round before the proof (jt:26). ui-ux-designer.md:30 and vfx-designer.md:24 name the feature-proof target image and key frames (jt:86). The animator is a planned role with no file."}
  - {id: C-NR4, state: closed, evidence: "sound-designer.md:24 'run the sound sync check in the review chain (cue times from the Output log; listening is owner-confirmed)'. vfx-designer.md:38 'the frames or times to grab: Studio MCP captures are stills' (the 30 fps request is gone). Both agree with jt:16."}
  # auditor D (context)
  - {id: D-B4, state: closed, evidence: "eval_context on the first 19 cases of knowledge/evals/retrieval.jsonl: '16/19 pass · recall@5 0.763 · recall@10 0.842 · MRR 0.703'; the failures are cases 1, 10 and 16 only, which is the pre-J016 set (auditor D's 322c8ad^ run: 16/19, recall@10 0.842, MRR 0.608). Case 3 (intent brief) is at rank 6 (was 55); case 17 (architecture) at rank 2 (was 182). Full run: '24/33 pass · recall@5 0.636 · recall@10 0.742 · MRR 0.554', 'RESULT: recall@10 held'. The saved run I made equals knowledge/logs/improve/2026-10-21-retrieval.json key for key (dates ignored). The one 'MRR 1.00 -> 0.50' line printed by --compare is a tool artefact: RC-N8."}
  - {id: D-N1, state: closed, evidence: "context_packet.py:139-141, :685-687: with --role, files under a job's reviews/ or exchange/ score ×0.5 (marked PROPOSAL), except for orchestrator and doc-keeper. Packet 'write the J016 pilot step for the cutscene' --job J016-orchestration: sound-designer, feature-builder, art-director and reviewer have no review or exchange file in the top 12; orchestrator and doc-keeper keep them at ranks 7-12. rules/knowledge.md:38 states the rule (wording note: RC-N9)."}
  - {id: D-N2, state: closed, evidence: "context_packet.py:703-722: a same-folder, same-heading section is dropped only when SIBLING_OVERLAP (0.8) of its words are in a kept one; test_distinct_sibling_sections_both_rank (tools/tests/test_context_tools.py:574) passes in the gate. Auditor D's example is a true copy: the two J011 inbox drafts' 'Owner corrections' sections have the same 41-token body (equal md5 of the token stream), so one slot is the correct result."}
  - {id: D-Q3 + E-N-01 + TT-01, state: closed, evidence: "21 visibly named notes carry the new frontmatter key (paths from git diff --numstat: the J003, J009, J011, J014 grades-g2.md; J004 grade-*, eval-answers*, eval-inputs.md; J007 eval-gaps.md; J009 T11-grader-brief.md and lead-notes.md; six J010 scores-*.md; knowledge/evals/skill-runs/2026-10-20.md; the J003-T08 inbox case readings; knowledge/reference/vfx/training/benchmark.md). Every visible grade-like path in git ls-files knowledge/ is in that set. Rule: rules/knowledge.md:51 and the §5 example key :72; code: context_packet.py:168, :476 (corpus), stem index and link neighbours, :1269, :1288 (job block); kb_index.py:119 (indexes). Packets as JSON and as text, scanned whole (excerpts included) for 'hidden', grades-, grade-, eval-answers, eval-gaps, scores-, evals/skill-runs/, grader, eval-inputs, case-readings, training/benchmark: (1) 'Add a daily reward chest that gives coins each day you log in' --role orchestrator → 0; (2) 'review the character model against the art bible anchors' --role art-director --job J016-orchestration → 0; (3) 'icon renders of the shipped model: archer-gold' --role modeler → 0. knowledge/generated/*.md name none of the 21 paths; the only 'hidden' words there are titles of two visible notes. Eval cases 32-33 (the R2 request and the R2 fix task) report forbidden: [] for all six patterns."}
  # auditor E (tabletop), other items
  - {id: E-N-02, state: closed, evidence: "SKILL:32 Mixed row: one owner job per shared interface, written 'in both job cards' \"Linked jobs\" row and in active.md', owner job's contract first, the other cites its revision. templates/jobs/job-card.md:28 'Linked jobs | <job-id: which shared interface it owns (saved fields, ids, who grants, who checks)>'. knowledge/jobs/active.md:13 '(a split request adds `· linked: <job-id>, owns: <shared interface>`)'. The hooks' parser (context_packet.py:133 ACTIVE_JOB_RE) reads such a line: id 'J020-gold-skin', the suffix stays in the title."}
  - {id: E-N-06, state: closed, evidence: "knowledge/jobs/J016-orchestration/decisions.md:26-41 rows J016-LD1..LD16. Each pointer holds the rule: LD1 company.md:77; LD2 reference-images SKILL.md:38 (§4); LD3 company.md:79; LD4 company.md:95; LD5 company.md:107, :117; LD6 SKILL:32 (§2); LD7 company.md:27-28; LD8 knowledge.md:51 (now wider); LD9 jobs README.md:10; LD10 company.md:60 (§4 step 4); LD11 messages.md:113-114 (§3); LD12 company.md:72; LD13 knowledge.md:79 (§5); LD14 AGENTS.md:56 (§4); LD15 company.md:100; LD16 SKILL:38 (§3). Note: briefs and README still cite 'LD2', not 'J016-LD2'; decisions.md:22 says so, so the source can be found."}
  - {id: knowledge-§3/§5, state: closed, evidence: "held_out rule knowledge.md:51 (with the named-grader exception for /build-agent); frontmatter example key :72; craft-role down-weight :38; knowledge/inbox/README.md:20 and knowledge/jobs/README.md:22 say the same."}
  - {id: jt-cutscene-proof, state: closed, evidence: "jt:25 matches cut:10 (meta detail) and cut:371-381."}
  - {id: architecture-description, state: closed, evidence: "390 characters in .agents/skills/architecture/SKILL.md and the .claude copy; gate 'skill descriptions: all <= 400 characters' PASS."}
  - {id: orchestration-§10, state: closed, evidence: "SKILL:86 '## 10. Intent briefs: what and why, never how', SKILL:87 example (cutscene beat → animator, intent + fixed/open). retrieval.jsonl anchor orchestration/SKILL.md#10 resolves; case 3 passes at rank 6."}

findings:   # new seams; each checked with the evidence below
  - id: RC-N1
    class: blocking
    where: ".agents/workflows/jobs/job-feature.js:391-411 (P3 targets), :465, :542-544; dispatcher :784-789; .agents/workflows/jobs/README.md:11, :48; ui-ux-designer.md:30, vfx-designer.md:24 ('shown at G2')"
    expected: "README.md:11 (rewritten in d2d0601): 'a pending batch that later steps in the same call build on ... stops the stage as blocked there, so nothing is built or reviewed on unapproved images'. reference-images SKILL.md:38: no craft builds visual work before the approved image exists. An M job has no G2 (company.md:27)."
    observed: "An M feature build runs proof() inside build (:784-789). When P3-ui-target or P3-vfx-keyframes returns pending, nothing checks results.images_pending; the only guard is :542 '!IMAGES.length', which passes as soon as args.images holds any path. The P3 intents (:397, :406), the proof outcome (:465), the :543 message, README:48 and the two role lines say the targets are 'shown at G2', which an M job does not have."
    evidence: "Harness job-feature build M, money false, numbers false, images ['a.png'], scenario images pending → status done, 24 agents, images_pending [P3 UI target image, P3 VFX key frames]; B4-ui, B5-vfx, B6-sound, B7-integrate and the whole review chain ran after the pending batch. Without args.images the same run stops correctly at :543 (blocked, 12 agents). Not on the cutscene pilot path."
    smallest_fix: "After the proof in an M build (or at the top of production), return blocked when results.images_pending names a P3 step, as chr:442 does; in the P3 intents, :465, :543, README:48 and the two role lines say 'shown at G2 (L) or before the build continues (M)'."
  - id: RC-N2
    class: recommendation
    where: "studioRule(false) in all seven workflows (e.g. cut:169 'do not write to Studio in this step; read-only captures only if `checks` ask for them'); .agents/workflows/jobs/README.md:20 'one Studio writer'; tools/workflows/wf_harness.mjs:109 (only 'you are the only Studio writer' counts as holding Studio); studio-operator.md:22 'one writer at a time'; feature-builder.md:24; performance-engineer.md:22; environment-designer.md:22; jt:62; templates/jobs/job-card.md:26"
    expected: "company.md:135 'Studio drivers (read or write) | 1 at a time per Studio instance'; SKILL:62 and AGENTS.md:46 now say the same."
    observed: "The workflows, their README, the harness, four role files, the recipe and the job card still say 'writer', and the non-writer rule permits read-only captures while another step writes."
    evidence: "Wording only today: for 7 harness runs (cutscene proof and build L; feature, stage, effect, character, UI-screen build M) a script over the timeline found 0 steps whose own checks ask for Studio running beside a Studio writer. A future step with a capture check would pass the harness while breaking company §9."
    smallest_fix: "studioRule(false): 'Studio: do not use Studio in this step (another step drives it)'; README:20 and the role lines 'one Studio driver'; the harness counts any brief whose checks name Studio as a holder."
  - id: RC-N3
    class: recommendation
    where: "ui:254 (`${UI}/refs/image-prompts.md`), ui:503 (`${UI}/image-prompts.md`) vs .agents/skills/ui-figma/references/image-generation.md:25, :59 (`content/ui/<screen-id>/refs/prompts.md`) and roblox-handoff.md:78 (`refs/` with `prompts.md`)"
    expected: "One prompts file name (E-N-07)."
    observed: "The E-N-07 rename moved the UI workflow off the name the UI designer's own skill uses; the D1 brief cites image-generation.md §2 and the B1 brief cites roblox-handoff.md §4."
    evidence: "grep: the two ui-figma references are the only kit files left that name a prompts.md other than image-prompts.md (messages.md:100 is a sound example). Risk: two prompt logs per screen; the lead's batch reads the brief's path from images_pending, so no stall."
    smallest_fix: "ui-figma image-generation.md:25, :59 and roblox-handoff.md:78: 'image-prompts.md'."
  - id: RC-N4
    class: recommendation
    where: "BASE_RULES in all seven workflows (cut:143 'Never open a file whose name starts with hidden-'); tools/hooks/subagent_context.py:36 ('any file with 'hidden' in its name: never open')"
    expected: "rules/knowledge.md:51: any name that contains 'hidden', and any note with held_out: true, is never opened, quoted or listed."
    observed: "The workflow rule covers only names that start with 'hidden-', so grades-hidden.md or evals-hidden.md style names are not named; neither the workflow rule nor the hook line names held_out: true notes. Packets and indexes withhold them (checked above), so the gap is an agent that opens a path it finds by listing a folder."
    evidence: "Present at 763a11e for the prefix (git show 763a11e:job-cutscene.js); the rule widened in d2d0601 and the agent-facing lines did not follow."
    smallest_fix: "BASE_RULES and the hook line: 'Never open a file or folder whose name contains hidden, or a note whose frontmatter says held_out: true (rules/knowledge.md §3).'"
  - id: RC-N5
    class: recommendation
    where: "ui:225 FILE_OWNERS ('listed under \"File owners\" in direction.md'), ui:299 ('a \"File owners\" section from the feature-builder's proposal') vs .agents/workflows/jobs/README.md:19, company.md:60, decisions.md J016-LD10, templates/jobs/contract-header.md:27"
    expected: "Code file owners live in a contract's Code file owners table, set by the architect."
    observed: "In the UI-screen workflow the code file owners are a direction-sheet section that the ui-ux-designer writes from the feature-builder's proposal; no architect and no contract header."
    evidence: "Unchanged since 763a11e (git show 763a11e:job-ui-screen.js has the same FILE_OWNERS line); the recipe allows 'feature-builder or architect (data and remotes)' (jt §4 Direction leads), so it may be intended, but README:19 and LD10 state no exception."
    smallest_fix: "README:19 and LD10: '(UI screen: the File owners section of direction.md, from the feature-builder or architect)', or move it into a contract header."
  - id: RC-N6
    class: recommendation
    where: "rules/knowledge.md:15 (L3 writer cell 'job lead (direction, contract)') vs templates/jobs/contract-header.md:17; architect.md:46"
    expected: "One writer rule with its exceptions in both places (C-NR2 smallest fix named both)."
    observed: "knowledge.md L3 gives contracts to the job lead only; the template gives the Code file owners section to the architect, and architect.md:46 makes the architect the writer of contract-player.md and contract-wiring.md."
    evidence: "In a cutscene job the job lead is the film-director (SKILL:23) and the architect writes contract-player.md (jt:27)."
    smallest_fix: "knowledge.md:15: 'job lead (direction, contract; code contracts and Code file owners sections: the architect)'."
  - id: RC-N7
    class: recommendation
    where: ".agents/skills/orchestration/references/job-types.md:31 ('**film-director** (staging, timing, camera, clarity, with sound) ... → sound sync check')"
    expected: "jt:16: MCP captures are stills; sync from the Output log; listening is owner-confirmed."
    observed: "The cutscene review row still asks the film-director to judge 'with sound'. cut:739 (film reviewer brief) correctly judges 'from the stills and the event times in output.log'."
    evidence: "A-N04 listed :31 in its 'where'; the fix changed only :99 and :101."
    smallest_fix: "jt:31: '... clarity, from the stills and the Output log cue times) ... → sound sync from the Output log (listening: owner-confirmed)'."
  - id: RC-N8
    class: recommendation
    where: "tools/eval_context.py --compare; knowledge/evals/retrieval.jsonl cases 17 and 29 (same task string, case 29 with role architect)"
    expected: "--compare reports a change only when a case's score changed."
    observed: "--compare keys cases by task, so it prints 'design a new quest system so adding quests is easy: R@10 1.00 -> 1.00, MRR 1.00 -> 0.50' although the current run equals the saved baseline key for key."
    evidence: "Saved current run vs knowledge/logs/improve/2026-10-21-retrieval.json: identical (script, dates ignored); the printed line pairs case 17 (MRR 0.50) with case 29 (MRR 1.00)."
    smallest_fix: "Key cases by (task, role, job) in --compare."
  - id: RC-N9
    class: recommendation
    where: "rules/knowledge.md:38 vs tools/context_packet.py:139, :685"
    expected: "The rule and the code describe the same down-weight."
    observed: "The rule: '--job ... with a craft role, the job's reviews/ and exchange/ files rank lower'. The code: any job's reviews/ and exchange/ files, with or without --job."
    evidence: "JOB_HISTORY_RE '^knowledge/jobs/[^/]+/(?:.*/)?(?:reviews|exchange)/'; history needs only bool(role)."
    smallest_fix: "knowledge.md:38: 'with a craft role, every job's reviews/ and exchange/ files rank lower'."

seam_check:   # files: git diff --name-only 322c8ad d2d0601 = 200 paths; content-grepped 164 (5 hidden-named, 21 held_out-marked and the J016 audit review files left out)
  - {term: "lesson cause labels", files: "rules/knowledge.md, knowledge/inbox/README.md, templates/jobs/evidence.md, templates/jobs/handback.schema.json, 7 workflows (+ .claude copies), .agents/workflows/improve.md", result: "same 10 labels; evidence.md lists the 9 defect causes (no win); improve.md:32 capitalises the row label"}
  - {term: "status words done · blocked · needs-decision · failed · stale", files: "rules/company.md §8, rules/messages.md, SKILL §12, templates/jobs/handback.schema.json, ledger.md, status-block.md, 7 workflows", result: "one spelling; all 7 TAIL_PROPS enums are ['done','blocked','needs-decision','failed']; stale is an output status only (company.md:120, ledger.md:23). Cosmetic: ledger.md:21 'no = needs decision' (prose, no hyphen)"}
  - {term: "images / images_pending / imagesApproved / images_approved / image-prompts.md", files: "7 workflows, README, reference-images SKILL.md, roles", result: "imagesApproved is the arg (README:33), images_approved the brief field set from it (cut:192 and peers); images_pending one spelling (79 uses); image-prompts.md everywhere in workflows; drift in ui-figma references (RC-N3)"}
  - {term: "held_out", files: "rules/knowledge.md, knowledge/inbox/README.md, knowledge/jobs/README.md, tools/context_packet.py, tools/kb_index.py, tests, CHANGELOG, pilot-plan.md", result: "frontmatter key spelled held_out: true everywhere; prose 'held-out'; agent-facing workflow and hook lines do not name it (RC-N4)"}
  - {term: "Code file owners", files: "company.md, contract-header.md, job-card.md, architect.md, feature-builder.md, README, cut, chr, fea", result: "'Code file owners table/section' and the `owns` column of it agree; UI screen uses a direction-sheet 'File owners' section (RC-N5); knowledge.md L3 writer cell (RC-N6)"}
  - {term: "Linked jobs", files: "SKILL:32, templates/jobs/job-card.md:28, knowledge/jobs/active.md:13", result: "agree"}
  - {term: "Studio driver vs Studio writer", files: "driver: company.md, AGENTS.md, SKILL:62, environment-craft, level-design; writer: 7 workflows, README, harness, studio-operator, feature-builder, performance-engineer, environment-designer, jt:62, job-card.md:26", result: "contradiction in wording; behaviour checked as one driver (RC-N2)"}

keep:
  - "pendingStop pattern (cut:160, chr:166, ui:151) with the BASE rule 'keep a deliverable that still matches its inputs' for reruns after a batch, in all seven workflows"
  - "boards first and alone in the cutscene proof (cut:371-381), matched by jt:25 and the meta detail"
  - "held_out: true withheld in corpus, stem index, link neighbours, job block and indexes, with a lint warning for a bad value (kb_index.py)"
  - "craft-role down-weight of job history, with the lead and the doc-keeper exempt"
  - "sibling dedupe by word overlap instead of heading alone"
  - "J016-LD1..LD16 recorded with pointers that hold"
  - "gate: 641 tests, sync, lint, index check, sizes all PASS"

notes:   # not findings; outside the item list
  - "The lead's packet for the R2 owner request ranks J016 audit review files at ranks 1, 5 and 10 (orchestrator is exempt from the history down-weight); E-N-04 is outside this recheck."
  - "Eval cases 32 and 33 (added for E-N-01) fail on recall (orchestration SKILL.md at rank 170; data-saving SKILL.md at rank 42), so their pass/fail does not show the forbid check; forbidden: [] is in the saved JSON."
  - "This file lands in knowledge/jobs/J016-orchestration/reviews/: the lead reruns python tools/kb_index.py before the next gate run."

verdict: "fix-first for the feature workflow (RC-N1, off the pilot path); ready for the cutscene pilot. All 24 recheck entries (every item in the brief) are closed."
</spec>
```

## Coverage

| Item | State | Main evidence |
| --- | --- | --- |
| A-N01, A-N02, A-N03, A-N04 | closed | SKILL:112, :62; AGENTS.md:21; jt:99, :101 |
| B-F11, B-N1, B-N2 | closed | chr:375, stg:435, ui:305; ui:509-510 + harness; six sign intents |
| B-N3 + E-N-03 | closed | chr:441-442, cut:381; harness character M/L and cutscene M/L blocked |
| E-N-07 | closed | every workflow image step names image-prompts.md |
| C-NB1, C-NR1, C-NR2, C-NR3, C-NR4 | closed | script over 10 lists; architect.md:22, :46; contract-header.md:17; role lines |
| D-B4, D-N1, D-N2 | closed | 16/19 (1, 10, 16 fail); baseline equal; packet ranks; overlap rule + test |
| E-N-01 / TT-01 / D-Q3 | closed | 21 marked notes; 3 packets and the indexes name none |
| E-N-02, E-N-06 | closed | SKILL:32, job-card.md:28, active.md:13; LD rows and pointers |
| knowledge.md §3/§5, jt cutscene proof, architecture description, orchestration §10 | closed | knowledge.md:38, :51, :72; jt:25; 390 chars; SKILL:86-87 |
| New | 1 blocking (RC-N1), 8 recommendations (RC-N2 to RC-N9) | findings |
| Seam check | 7 terms | seam_check |
| Gate | PASS, 641 tests | python tools/verify.py |
