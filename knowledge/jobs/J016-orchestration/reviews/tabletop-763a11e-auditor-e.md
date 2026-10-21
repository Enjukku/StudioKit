---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J016 G3 audit recheck (J016-A5)
supersedes: []
---
> Author: auditor-e · claude-opus-5-5 · high · 2026-10-21

# Tabletop recheck at 763a11e: blocking findings TT-01..TT-13, keep list, new issues

Scope (rules/company.md §7, selective recheck). I re-traced only the step where each blocking finding stalled or broke a rule, the keep list, and new problems on the R1-R3 paths. Evidence is from files at 763a11e and these runs:
- `wf_harness.mjs` runs with fake agents and explicit args, using the scenarios images:pending, newCast, blockLabel and dump.
- the packet sweep from the first audit: 110 task strings (the workflows' 107 plus the three owner requests), in JSON.

I did not open any file whose name contains "hidden". I did not call the Workflow tool.

Working tree: during the recheck another chat left uncommitted edits in `orchestration/SKILL.md` (lines 62 and 111), `references/job-types.md` (effect rows), `AGENTS.md:21` and `rules/knowledge.md:51`. None of the lines I cite changed, except AGENTS.md:21. I cite that line from `git show 763a11e:AGENTS.md`. Late in the recheck, more uncommitted edits appeared:
- one lesson-cause enum string in every workflow and in `handback.schema.json`: 'found by …' became 'defect found by …';
- small changes in five role files (architect, environment-designer, sound-designer, ui-ux-designer, vfx-designer);
- `contract-header.md`.

Some harness runs read those working-tree files. The edits change no control flow and no line I cite (`git diff`). I did not use the five role files or `contract-header.md` as evidence.

```text
<spec>
artifact: StudioKit@763a11e (workflows job-cutscene, job-feature, job-character; orchestration skill and job-types; company, messages, knowledge rules; reference-images; studio-operator role; context_packet.py; handback.schema.json)
reviewer: auditor-e
looked_at_first: [the harness runs and dumped briefs, the packet sweep, the files below; the commit message last]
recheck:
  - {id: TT-01, verdict: still open (narrowed), evidence: "Closed for hidden-named files. context_packet.py:150-170 withheld() drops every path with 'hidden' in a part, direction/proposal-* and skill evals/. In the 110-task sweep no hidden-named path appears in results or read_next. Still open for grade files that restate held-out rubrics: the R2 owner-text packet ranks knowledge/jobs/J011-progression-designer/grades-g2.md #3 and prints 'H1-1 spacing of usable rewards, not total | pass'. That is the same item the first audit saw in J011's evals-hidden.md ('H1-1 | Diagnoses spacing of USABLE rewards … not the total'). read_next tells working agents to open grades-g2.md (J011 L57-66 and L67-76 'H2 … daily-spin-policy', J014 L43-75 'Counts check (agent's tool output vs the key's)', J009 L46-57 'H3 …'). These appear in 17 of the 110 tasks, all on the R2 path (contract, build, tables, sign, fix). knowledge/evals/skill-runs/2026-10-20.md (graded eval rows) and J004 trend-scout eval-answers*.md are also ranked", see: N-01}
  - {id: TT-02, verdict: closed, evidence: "README.md:11; reference-images/SKILL.md:38 ('the lead runs pending batches in its own chat between stages'); orchestration/SKILL.md:16. The D1 art-director brief (dump) writes direction/prompts-art-director.md and returns images.state pending. The R1 direction run with images:pending ends 'done' with images_pending listing 4 steps. Proof without args.images returns blocked before any agent starts"}
  - {id: TT-03, verdict: closed, evidence: "job-cutscene.js:68, :716 (codeReviewer, effort high when risky); job-character.js:84, :881 (reviewer when playable). Harness: R1 build labels include 'reviewer: RV-candidate-r0-reviewer'; the R3 M build includes it too, with skills [code-review, networking-security, data-saving, platform-policy]"}
  - {id: TT-04, verdict: closed, evidence: "Cutscene: B1-player-contract (architect, job-cutscene.js:527) writes contract-player.md with the Code file owners table. PLY owns 'the code files the Code file owners table of contract-player.md@rev1 names' and returns blocked when it is empty (:486-488). Character: P1-wiring-contract (architect, job-character.js:451) feeds S7-wiring (:836) the same way. README.md:19"}
  - {id: TT-05, verdict: closed, evidence: "A missing size, money or numbers (feature), or variant, playable or base (character), returns blocked with a 'required' list before any agent starts (harness, three runs; job-feature.js:47). The args table is README.md:26-55; orchestration/SKILL.md:14 points to it"}
  - {id: TT-06, verdict: closed, evidence: "Timeline: feature B5-vfx ticks 8-9, then B6-sound 10-14. B6 inputs add content/vfx/<feature>/ (job-feature.js:627), and its intent keys sound to the frame scripts. Cutscene: B1-envelope-vfx (5-8) → envelope-sound (9-11), B5-vfx-proto (20-25) → sound-proto (26-27), B5-vfx (35-36) → B5-sound (37-38). README.md:12"}
  - {id: TT-07, verdict: closed, evidence: "Proof now makes P3-ui-target and P3-vfx-keyframes (job-feature.js:395, :404); the proof outcome says the G2 packet shows them. Build without args.images, when the plan has visible parts, returns blocked (:542). B4-ui refs carry the approved image"}
  - {id: TT-08, verdict: closed, evidence: "company.md:27-28. M now covers 'supporting crafts inside one output'; L covers 'several crafts that each produce separate outputs (… a feature with UI + VFX + sound)'. R2 (chest screen, effect, sound as separate outputs) → L. R3 is split (TT-09); each part is one output in the approved style → M. Residual: R2's crafts are still a prediction at intake; no rule says to resize at G1 if the contract drops a craft (no 'resize' in rules or skill). Not blocking"}
  - {id: TT-09, verdict: closed, evidence: "orchestration/SKILL.md:32 names this exact case: a character variant job + a shop-listing feature job with money; job-types.md:49 'Selling it is a second job'; company.md:57. The split opens a new interface with no owner: see N-02"}
  - {id: TT-10, verdict: closed, evidence: "handback.schema.json now has docs_read (required) and an optional lesson {type, cause, layer, what_happened, proposed_change}. Workflows collect results.lessons (job-feature.js:223). README.md:57; orchestration/SKILL.md:16 and :84; role files (film-director.md:51, art-director.md:56) send lessons through the hand-back"}
  - {id: TT-11, verdict: closed, evidence: "studio-operator.md:16 adds company.md §7; :30 now 'Checks are light (owner J005-D8)'. The R2 capture brief (dump) carries 'Check budget (owner J005-D8)' (job-feature.js:163) and asks for captures_made and captures_looked_at"}
  - {id: TT-12, verdict: closed, evidence: "job-cutscene.js:325 checks new_cast_needed after P1. The harness newCast run stops after 1 agent with needs-decision 'the animatic waits'. job-types.md:27 now matches"}
  - {id: TT-13, verdict: closed, evidence: "orchestration/SKILL.md:38 (prerequisites first: profile, art bible and anchors, released rigs, studio_id); company.md:57. The D1 art-director brief adds: 'If knowledge/design/art-bible.md does not exist yet, do not write it in this step: propose its locks … and add the G1 question'"}
keep_recheck:
  - {item: "STATUS, coverage, built_on, checks with evidence; evidence before status", state: still true, evidence: "handback.schema.json property order: coverage … questions, lesson, status, outcome"}
  - {item: "independent D1, one exchange, synthesis, signatures, one resolution round", state: still true, evidence: "R1 direction labels unchanged (11 agents); the packet now also withholds direction/proposal-* (context_packet.py:165)"}
  - {item: "bad args and missing studioId blocked before agents; one Studio writer", state: still true and stronger, evidence: "harness 'required' lists; the harness fails a run on two holders of Studio, Blender or the browser"}
  - {item: "recapture and refreeze after every repair round", state: still true, evidence: "blockLabel run (maker environment-designer): FIX-candidate-r0 → SCN-candidate-r0-fix → CAP-candidate-r0-fix → round 1 scripts first"}
  - {item: "unroutable maker → needs-decision", state: still true, evidence: "character run with maker 'nobody-role' → 'cannot route (nobody-role): the lead assigns them'"}
  - {item: "MONEY_RULES restated in full; reviewer harm order; code 3 rounds vs other 2", state: still true, evidence: "R2 dumps carry the Remotes and Saves rule text; README.md:15. The character wiring now restates the Saves rules too"}
  - {item: "explicit 'return blocked with the files you need' instead of a guess", state: still true (moved to the contracts' Code file owners tables), evidence: "job-cutscene.js:488; S7-wiring dump"}
  - {item: "contractIn() approved-revision pin", state: still true and extended, evidence: "B4/B6 inputs 'contract-daily-reward.md@<the revision approved at G2, named in decisions.md>'; cutscene B1 beat-sheet uses the same pattern"}
  - {item: "light-check line in every review chain; variant fixed items with needs-decision", state: still true, evidence: "J005-D8 count: cutscene 2, feature 2, character 4; job-character.js:245-247"}
  - {item: "cutscene check-ins; VFX and sound on the animator's timing list", state: still true, evidence: "B2-art-checkin before B2-set-final; B3-combined-checkin before B3-polish; B5 vfx then sound"}
  - {item: "packet Job block lists the canonical job files", state: still true, evidence: "packet --job J016 prints '## Job J016-orchestration' with job-card.md and crew.md"}
findings:
  - id: N-01
    class: blocking
    where: "tools/context_packet.py:150-152 (held_out = 'hidden' in a path part); rules/knowledge.md held-out row (committed: names only)"
    expected: "held-out rubrics never reach working agents (knowledge.md §3 'honest scores')"
    observed: "the rule is a filename rule. Grade files of held-out cases do not have 'hidden' in their names, so they stay indexed, excerpted and in read_next"
    evidence: "TT-01 recheck: R2 packet rank 3 = J011 grades-g2.md with the H1-1 rubric line; read_next 'open knowledge/jobs/J011-progression-designer/grades-g2.md L57-66' in 'fix findings and re-wire changes: daily-reward'; J014 grades-g2.md 'Counts check (… vs the key's)' in 'feature contract', 'build the feature', 'feature plan and builder brief'"
    smallest_fix: "withhold grade and eval-result files too (names grades-*, grade-*, eval-answers*, knowledge/evals/skill-runs/), or rename the held-out cases' grade files with 'hidden'; add one retrieval eval that fails when such a path is ranked"
  - id: N-02
    class: blocking
    where: "orchestration/SKILL.md:32; job-types.md:49; job-character.js:451 (P1-wiring-contract), :836 (S7-wiring); README.md:19"
    expected: "when one request becomes two jobs, the interface between them (the skin id, the saved ownership record, which job grants it and which checks it, the build order) has one owner and one contract (company.md §3: file owners are the architect's; §5.5 a contract names its consumers)"
    observed: "the split says only 'linked in knowledge/jobs/active.md'. active.md takes '- <job-id> · <title>' lines with no link field. The character job's wiring contract (architect) covers 'the ownership check before equip and the saved equip state'. The shop-listing feature job's own architect plan covers the purchase grant. Neither brief names the other job, and no file says which job owns the owned-skins save field or which one runs first"
    evidence: "R3 path: S7-wiring dump has no reference to a shop job (grep 'sibling|other job|second job' in job-character.js and job-feature.js = 0). Both architects will write a Code file owners table for the same entitlement data. The data-saving rules in both briefs ('a purchase … can never apply twice') then rest on two owners"
    smallest_fix: "one line in SKILL.md §2 'Mixed request': the first job's contract (here the character wiring contract) owns the shared ids and saved fields; the second job's brief cites it @rev as an input; the lead records the order in both job cards"
  - id: N-03
    class: blocking
    where: "job-character.js:419 ('Views still pending … the lead shows the pending batch at G2'), :1057-1060 (M runs proof() then production() in one call), :591 (S3 'from the approved reference set'); reference-images/SKILL.md:38 ('No craft builds visual work before the approved image exists')"
    expected: "a pending image batch reaches the owner before any craft builds from it"
    observed: "R3 is an M job, so there is no G2. When P1-reference-set returns pending, build goes on through blockout, S3 final geometry and textures, icons, wiring and the review chain. The pending batch shows up only in the final result's images_pending. The modeler's S3 brief says 'from the approved reference set' while the reference set is still prompt rows; the G1 image in refs keeps the 'no approved image → blocked' rule quiet"
    evidence: "harness: job-character M build with images:pending → status done, 21 agents, images_pending [{step: 'P1 reference set'}]. The same pattern in job-cutscene M build: done, 42 agents, images_pending [{step: 'P5 boards and animatic'}] (R1 itself is L, so not on its path)"
    smallest_fix: "in an M build, return blocked after the proof when results.images_pending is not empty ('run the batch, then resume build with args.images'), the way job-feature.js:542 already does for its images; change :419 'at G2' to 'before the build continues'"
  - id: N-04
    class: recommendation
    where: "knowledge/jobs/J016-orchestration/reviews/*.md (now committed); tools/context_packet.py ranking"
    expected: "a game task's packet ranks game and kit notes, not another job's audit"
    observed: "the R2 owner-text packet ranks my own tabletop-322c8ad-auditor-e.md #1 (score 39.4 against 15.4 for #2). It shows stale line numbers of kit internals to the game-designer"
    evidence: "packet 'Add a daily reward chest …' --role game-designer, rank 1"
    smallest_fix: "withhold knowledge/jobs/*/reviews/ of closed or kit jobs from packets without --job of that job, or mark audit reviews status: superseded at J016 close"
  - id: N-05
    class: recommendation
    where: "AGENTS.md:21 at 763a11e ('the lead has no role file, so it drops --role'); orchestration/SKILL.md:42 ('--role <role> --job <job-id>'); tools/context_packet.py (accepts --role orchestrator, exit 0)"
    expected: "one instruction for the lead's packet"
    observed: "the committed AGENTS.md says to drop --role, but the tool accepts --role orchestrator. An uncommitted edit in the working tree changes AGENTS.md:21 to '--role orchestrator'"
    evidence: "run: --role orchestrator exit 0; git diff AGENTS.md"
    smallest_fix: "commit the working-tree line"
  - id: N-06
    class: recommendation
    where: "README.md:10-21 and every workflow brief ('lead decision LD2', 'LD9', 'LD10' …); .agents/skills/environment-craft/references/studio-light-air.md:25 ('LD34-LD40' = paper line ids)"
    expected: "a rule's cited source can be found (messages.md §1: a value without a source is a defect)"
    observed: "LD1-LD16 are cited as the source in the README and in briefs, but no file records them (grep in knowledge/jobs/J016-orchestration finds no LD rows). The prefix LD is also the environment paper's line-id prefix"
    evidence: "grep -rln 'LD9' → only README.md, improve.md, inbox/README.md"
    smallest_fix: "add the 16 lead decisions as rows in knowledge/jobs/J016-orchestration/decisions.md (for example as J016-LD1 …) and cite those ids"
  - id: N-07
    class: recommendation
    where: "reference-images/SKILL.md:38 ('image-prompts.md next to its deliverable'); D1 brief 'knowledge/jobs/<job>/direction/prompts-art-director.md'; job-feature.js:395 'content/ui/<feature>/refs/prompts.md'"
    expected: "one name for the prompts file the lead's batch reads"
    observed: "the skill and the briefs name different paths. No stall, because images_pending carries the path the brief chose"
    evidence: "D1 dump; job-feature.js:395, :404"
    smallest_fix: "the skill says 'the prompts file the brief names (default image-prompts.md next to the deliverable)'"
keep: [all keep items above, the new required-args refusal, the files-only sideways order with VFX before sound, the scripts-first review rounds, the new-cast stop before the animatic]
verdict: fix-first
</spec>
```

Counts: TT-01..TT-13 → 12 closed, 1 open (TT-01, narrowed; tracked as N-01). New: 3 blocking (N-01 to N-03) and 4 recommendations (N-04 to N-07). Keep list: all 11 still true; none broken by a fix.
