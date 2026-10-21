---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J016 G3 audit, selective recheck of roles-templates-322c8ad-auditor-c.md
supersedes: []
---
> Author: auditor-c · claude-opus-5-5 · high · 2026-10-21

# Recheck: role files and job templates @763a11e, by auditor-c

This is a selective recheck (rules/company.md §7). It covers B1-B13, the keep list, and new contradictions the fixes introduced. I did not re-review the recommendations R1-R17 unless a fix made one worse.

All line numbers are at 763a11e. I opened the files before the commit message. Rules and recipe lines were read with `git show 763a11e:<path>`. After 763a11e, a parallel chat left uncommitted edits in job-types.md, orchestration SKILL.md, AGENTS.md and rules/knowledge.md. This file does not judge those edits; NR4 mentions them only as context.

```text
<spec>
artifact: .agents/roles/*.md (24) + README.md + templates/role.md + templates/jobs/* (13) @763a11e
reviewer: auditor-c (general-purpose, opus, high)
looked_at_first: [git diff --stat 322c8ad..763a11e; job-types.md, rules/company.md §4-§12, rules/messages.md §2-§9, rules/knowledge.md §1/§8 at 763a11e; every changed role file in full (art-director, environment-designer, film-director, vfx-designer, ui-ux-designer, reviewer, researcher, doc-keeper), the added lines of the other 16 roles and README, every template in templates/jobs/ and templates/role.md; then reference-images SKILL.md §4, orchestration SKILL.md §5/§9, job-*.js (as evidence only), tools/film/shotlist.py CUE_KINDS]
recheck:
  - {id: B1, state: closed, evidence: "art-director.md:25 now says the art-director makes direction images in the cutscene, character, stage and new-look effect recipes; in UI and marketing art the job lead makes them and the art-director gives notes in words. This matches job-types.md:70 and :109. art-director.md:29 adds the prompt route (reference-images SKILL.md:38, 'Who generates')."}
  - {id: B2, state: closed, evidence: "environment-designer.md:31 lists the gates as G1 (blueprint approved before building), G2 for L (the playable greybox), G3. :35 names the proof as the playable greybox at true scale with a dummy and zone volumes, before any art. This matches job-types.md:59-60."}
  - {id: B3, state: closed, evidence: "film-director.md:33 now says 'the board contact sheet and the timed Blender animatic with temporary sound and effect cues (on a greybox set where the set is missing)'. This matches job-types.md:25."}
  - {id: B4, state: closed, evidence: "vfx-designer.md:34 has a new step 3, 'Envelope with sound before you build', which comes before the layer plan (:35) and the spec (:37). :37 says the sound brief restates the agreed envelope. :24 now covers cutscenes and effects. This matches job-types.md:98."}
  - {id: B5, state: closed, evidence: "ui-ux-designer.md:48 now names 'progression-designer for prices and odds'. No 'economy designer' text is left in the role files (grep)."}
  - {id: B6, state: closed, evidence: "reviewer.md:43 now gives the path `knowledge/jobs/<job-id>/reviews/<artifact>-rev<N>-reviewer.md` from templates/jobs/review.md. This matches messages.md:152."}
  - {id: B7, state: closed, evidence: "reviewer.md:34 has findings in the §6 fields with severity in `evidence`, and minor problems as class recommendation. :35 has the verdict fix-first / ready for the next review. :46 maps the code-review fields onto §6 and adds `keep`."}
  - {id: B8, state: closed, evidence: "reviewer.md:39 now cites `rules/messages.md` §7 (Trust, messages.md:169)."}
  - {id: B9, state: closed, evidence: "researcher.md:20 says 'you have no shell, so the briefer runs the context packet ... and puts its output in your brief's refs'. This matches messages.md:81. The tool list is unchanged (:6), as the lead decided."}
  - {id: B10, state: closed, evidence: "doc-keeper.md:20 says the briefer runs the packet. :32 says 'the lead runs python tools/kb_index.py'. This matches orchestration SKILL.md:76 ('run python tools/kb_index.py yourself (the doc-keeper has no Bash)')."}
  - {id: B11, state: closed, evidence: "status-block.md:2 now reads '# Hand-back (STATUS is the first line of every hand-back)'. The STATUS line is at :6, before the spec block."}
  - {id: B12, state: closed, evidence: "job-card.md, crew.md, ledger.md, decision-digest.md, beat-sheet.md, review.md and exchange-note.md all have frontmatter on line 1 with type: job, and an Author line at :9-10. intent-brief.md:1 tells a brief saved as a file to add the same frontmatter. status-block.md is a message, not a job-folder file."}
  - {id: B13, state: closed, evidence: "beat-sheet.md:1-9 has frontmatter with revision: 1. :31 makes beat ids B01.. stable and adds an event-id column. :57-65 add a Consumers table. :67-71 add a change table with the messages §5 columns. This also closes R17. contract-header.md:11 points to it."}
keep_recheck:
  - {item: "Flow block in every role (packet with --role/--job, inputs with revisions + built_on, sideways bullet, §6 review bullet)", state: "still true, and changed on purpose: the sideways wording now follows each role's tools. All 11 roles whose tools list lacks SendMessage say 'Your tools cannot send direct messages'. All 11 roles with no tools list keep direct messages 'When the lead spawned you by hand'. researcher and doc-keeper have no sideways bullet. This matches company.md:77 (scripted cross-check over the 24 files)."}
  - {item: "Hand-back paragraph: STATUS first, coverage done/not done/skipped, built_on, evidence, no report* names", state: "still true. All 24 roles now say STATUS first, and all 24 name docs_read. R13 is fixed as a side effect: reviewer.md:48, qa-lead.md:47, researcher.md:35, explore.md:26 and studio-operator.md:37 use the three states and keep their own words in `why`."}
  - {item: "Frontmatter tier/effort match README; all skill entries exist; memory project", state: "still true. The diff 322c8ad..763a11e has no tier/effort/skills/memory/tools line changes, and all 77 skill entries resolve."}
  - {item: "All rules § references resolve", state: "still true. Every company §3/§4/§5/§7/§11, messages §1-§7, knowledge §3-§5/§8 and AGENTS §0/§3/§6 reference in scope points to an existing heading at 763a11e."}
  - {item: "Job lead and integrator lines match orchestration SKILL.md §2 and job-types.md", state: "still true."}
  - {item: "Cut decision rights the same in modeler, rigger, company §3, job-character.js", state: "still true: modeler.md:41, character-rigger.md:39, company.md:47 (now with a Must consult column), job-character.js:616."}
  - {item: "Route ownership the same in environment-designer and game-designer", state: "still true: environment-designer.md:22, :38; game-designer.md:23."}
  - {item: "Cutscene timing the same in sound-designer and vfx-designer", state: "still true and now symmetrical for effects: sound-designer.md:24, vfx-designer.md:24, :34."}
  - {item: "Animator stand-in handling (film-director) and 'give the brief to the lead' for planned roles", state: "still true: film-director.md:34. character-rigger.md:40 now has the same stand-in rule (closes R8)."}
  - {item: "No old gate names, hop counts, '3 concurrent', approval on the owner's behalf, reviewer edits", state: "still true. The grep over roles and templates gives only false positives (README history notes, 'shop' matching 'hop')."}
  - {item: "Templates match the rules field for field", state: "still true for review.md, exchange-note.md, intent-brief.md (22 keys; the peers comment added), ledger.md, contract-header.md (change table), direction-sheet.md (unchanged) and job-card.md (gates bound to revisions). handback.schema.json still puts the evidence fields before status/outcome and adds docs_read (required) and lesson (optional). Its new lesson.cause enum has one label that differs from the rule: see NB1."}
findings:   # new contradictions introduced by the fixes
  - {id: NB1, class: blocking, where: "templates/jobs/handback.schema.json:159",
     expected: "The lesson cause labels are the rules/knowledge.md §8 list word for word (knowledge.md:108 'defect found by the owner after internal review'). The fix aligned knowledge/inbox/README.md:32 and templates/jobs/evidence.md:25 to this list 'word for word'.",
     observed: "The lesson.cause enum value is 'found by the owner after internal review'. The word 'defect' is missing.",
     evidence: "In a workflow agent() call, the schema accepts only its own enum, so every lesson of this cause arrives with a label the rule and the inbox README do not use. /improve groups lessons by cause (knowledge.md §8 step 2), so this cause splits into two groups. The enum was added in this commit (schema $comment 'lead decision LD11').",
     smallest_fix: "Change :159 to 'defect found by the owner after internal review'."}
  - {id: NR1, class: recommendation, where: ".agents/roles/architect.md:22, :46",
     expected: "The recipe rows that changed name the architect as author of the cutscene player contract `contract-player.md` (job-types.md:27; job-cutscene.js:41) and the character wiring contract `contract-wiring.md` (job-types.md:42; job-character.js:42). They also put the architect in the cutscene needs round before the proof (:26) and have it run its D1 Studio probes before the animatic review (:25).",
     observed: ":22 names the feature, cutscene (feasibility) and UI recipes and does not mention character. It says the architect sets code file owners 'in the contract header's owns table', not that it writes these two contracts. The write scope at :46 covers `knowledge/jobs/<job-id>/architect/` and 'the code file owners table of a contract header', not a contract file at the job-folder root.",
     evidence: "In the workflows the brief's `owns` gives the file (job-character.js:456 owns: [WIRING]), so this is not blocking. A hand-run architect that follows its role file has no write scope for these contracts and no line saying it joins character jobs.",
     smallest_fix: "Add to :22 'character (playable): the wiring contract contract-wiring.md; cutscene: the player contract contract-player.md, the needs round before the proof and the D1 probes before the animatic review'. Add those two files to :46."}
  - {id: NR2, class: recommendation, where: "templates/jobs/contract-header.md:17, :28",
     expected: "One writer per file (rules/knowledge.md:10 'Writer (one per file)'; L3 row :15: 'job lead (direction, contract)')",
     observed: ":17 'Owner (one writer)'. :28 says the architect writes the 'Code file owners' section and adds a change-table row in the same file. For a feature contract (owner game-designer) or a UI spec (owner ui-ux-designer), two roles then write one file.",
     evidence: "company.md:60 and orchestration SKILL.md:52 both give this section to the architect, so the instructions agree with each other. Only the one-writer label and the knowledge.md L3 row do not state the exception.",
     smallest_fix: "Add '(the Code file owners section: the architect)' to :17 and to the knowledge.md L3 writer cell, or give the owners table its own file."}
  - {id: NR3, class: recommendation, where: "ui-ux-designer.md:27-29; vfx-designer.md:22-24; environment-designer.md:22-23; sound-designer.md:23-24",
     expected: "Changed recipe rows: the feature proof has 'the ui-ux-designer's target image and the vfx-designer's key frames ... made beside the prototype and shown at G2' (job-types.md:86). The cutscene adds 'Interfaces before the proof: animator, environment-designer, vfx-designer, sound-designer and architect state needs against the beat sheet draft' (:26).",
     observed: "No flow section names the feature-proof visual part. No craft flow section names the cutscene needs round before the proof. Only film-director.md:22 says it merges those needs.",
     evidence: "This is an omission, not a contradiction. The workflow briefs carry it, so a hand-run craft does not learn its part from its role file.",
     smallest_fix: "Add one clause to each flow section that names these two steps."}
  - {id: NR4, class: recommendation, where: ".agents/roles/vfx-designer.md:38; sound-designer.md:24",
     expected: "'Studio MCP captures stills, not video or sound: sync is judged from the Output log (event, VFX and cue start times on one clock) and labelled so; listening is an owner-confirmed line in the gate packet' (job-types.md:16, new in 763a11e)",
     observed: "vfx:38 asks for 'the one capture you need (effect, camera, dark test place, 30 fps)'. sound:24 says 'run the sound sync check in the review chain' and does not say that the check reads the Output log cue times.",
     evidence: "A 30 fps capture request cannot be met through Studio MCP, so the studio-operator returns stills or not verified. Within the recipe at 763a11e, :99 'one capture with temporary sound' and :101 'sound sync on the capture' also conflict with :16. Uncommitted working-tree edits after 763a11e reword :99 and :101 to the Output-log form; this recheck does not judge them.",
     smallest_fix: "vfx:38 '... dark test place; key stills plus the Output log cue times'. sound:24 '... the sound sync check from the Output log cue times (listening: owner-confirmed)'."}
keep:
  - "B1-B13 fixes, as cited above"
  - "The tools-based sideways wording, applied the same way in all 24 roles (company.md:77)"
  - "Per-recipe review positions (proof · final) in art-director.md:27 and game-designer.md:26, checked against all 7 recipes (closes R1 and R2)"
  - "beat-sheet.md and contract-header.md Consumers tables as the dependency map (company.md:72)"
  - "Lessons travel in the hand-back (status-block.md:19-24, messages.md:114, company.md:150). No role still writes to knowledge/inbox/ (grep)."
verdict: fix-first   # one new blocking finding (NB1, a one-word fix); B1-B13 all closed
</spec>
```

## Role × recipe rows changed at 763a11e (job-types.md) and their role-file status

| Recipe row (line) | Role | Change | Role file at 763a11e |
| --- | --- | --- | --- |
| Cutscene proof (:25) | architect | runs its D1 Studio probes before the animatic review | partly covered: architect.md:38 'the feasibility probe the recipe names' (NR1) |
| Cutscene interfaces before proof (:26) | animator, environment-designer, vfx-designer, sound-designer, architect | needs round on the beat sheet draft; film merges | film-director.md:22 has the merge; the crafts are silent (NR3) |
| Cutscene interfaces after G2 (:27) | architect | writes `contract-player.md` with code file owners | not in architect.md:22 or :46 (NR1) |
| Cutscene review order (:31) | reviewer | beside qa-lead and perf, for the player code | reviewer.md:23 has it |
| Character interfaces (:42) | architect | writes `contract-wiring.md` when playable | not in architect.md (NR1) |
| Character review order (:47) | reviewer | beside the chain when wired | reviewer.md:23 has it |
| Stage proof and review (:59, :63) | game-designer, studio-operator | gd judges the studio-operator's play captures | game-designer.md:26 and studio-operator.md:22 have it |
| Feature proof (:86) | studio-operator, game-designer, ui-ux-designer, vfx-designer | operator plays, gd judges; target image and key frames beside the prototype | gd and operator: covered (game-designer.md:26, :38). ui-ux and vfx: not covered (NR3) |
| Feature review (:89) | game-designer | judges the play captures | game-designer.md:26 has it |
| Effect review (:101) | reviewer | beside the chain when wiring code changed | reviewer.md:23 has it; quick-builder.md:22 says its patch goes to the reviewer |
| All recipes (:16) | vfx-designer, sound-designer, studio-operator | MCP gives stills; sync is read from the Output log | studio-operator.md:30 'checks are light' fits. vfx and sound do not (NR4) |
