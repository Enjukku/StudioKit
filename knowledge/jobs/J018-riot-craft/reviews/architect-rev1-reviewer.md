---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer architect · claude-opus-5-5 · high · 2026-10-22

# Review: architect books, rebuild round 1 (J018 stage 3)

```text
<spec>
artifact: .agents/roles/architect.md (body) + .agents/skills/architecture/ (SKILL.md; references/module-contract.md, presentation-contract.md, review-checklist.md, worked-examples.md; evals/ excluded), working tree on top of df13ff4, 2026-10-22
reviewer: J018 reviewer architect (opus, high)
looked_at_first: [
  all 6 book files read in full; git show df13ff4 of architect.md, SKILL.md, module-contract.md; old vs new walked line by line,
  knowledge/reference/craft/riot/universal-principles.md (master, UP-01..UP-20, the engineering lines and applies-to lists),
  matrix.md architect column (script-extracted: 24 findings) and the principle + check of all 24 in the topic files,
  docs mirror lines the books cite (GuiService.yaml:262-277, accessibility.md:184-200, Animator.yaml:215-233, events.md:10-14, AnimationTrack.yaml:318-326, ParticleEmitter.yaml:960-970, improve.md:416-422 and 565-568, particle-emitters.md:210-213, highlighting.md:36-38, packages.md:13-20, studio/network-simulator.md),
  partner books: engineering-craft (SKILL EC-15, presentation.md, handoffs.md), animation-design game-timing.md §4-5, vfx-design camera-and-screen.md and moment-recipes.md (hit-stop), testing player-facing.md, qa-lead.md, reviewer.md, code-review presentation.md, networking-security N-06/N-14, performance F-01..F-09, platform-policy rules.md §A, orchestration gates-and-feedback.md §4 and job-types.md §5, rules/company.md (round limits),
  J010 scores-architect.md (why the old isolation rule exists),
  my own runs of the three Grep screening aids on a synthetic Rojo sample (scratchpad arch-rev1: .luau and .lua presenters, a server service, a Config data module)
  ]   # the maker's coverage and proposals files were read after this
findings:
  - {id: F1, class: blocking, check: C5,
     where: ".agents/roles/architect.md (old df13ff4 line 36, Work method 5) -> new books: nowhere",
     expected: "Every old rule kept, moved, replaced by something at least as good, or shown wrong. Old Work method 5 required 'isolation from unrelated content (by data, proved by a spy or golden test)'. This came from the J010 rework study (L03) and decided the J010 AR3 eval: the old arm lost a must-have for 'no call-spy proof that machine code runs 0 times for ordinary structures' (knowledge/jobs/J010-engineering-team/scores-architect.md:14, :27)",
     observed: "The coverage table (c, row 'roles/architect.md:29-39') says old 5 'moved to architecture §3 steps 7-10'. Steps 7-10 hold the presentation contract, the budget, the locality check and the briefs; none holds isolation by data or a spy/golden proof. Grep for 'isolat', 'spy', 'golden' over the six book files: 0 hits in any body. The role build comment (architect.md:12) still says 'Added from the rework study: ... isolation by data (L03)', which is now untrue. (The other half of old 5, 'one owner or one derived source for every shared list or registry', survives in engineering-craft EC-15, which the architect loads second: kept.)",
     evidence: "git show df13ff4:.agents/roles/architect.md line 36; grep over .agents/roles/architect.md and .agents/skills/architecture/**/*.md; coverage/architect.md:133",
     smallest_fix: "SKILL §3 step 9 (locality), add one sentence: 'Content the feature must not touch is kept apart by data (a field in its definition, not a code branch per item) and proved by a spy test (the feature's code runs 0 times for it) or a golden test (its results do not change).' Add to AR-03: '; the isolation proof (spy or golden test) is named in the test seeds.' Correct the coverage row."}
  - {id: F2, class: blocking, check: C1 + C3,
     where: "5 coverage rows whose finding landed as a standard but whose library check has no self-review line: CC-01 (AR-19, SKILL.md:102), PP-20 (module-contract.md:35; AR-16 SKILL.md:99 holds only the cleanup half), PP-28 and PI-14 (R-25, SKILL.md:66), PP-30 (module-contract.md:84)",
     expected: "Owner: 'Turn every checkable finding into a line in the role's self-review'. Each of these has a check the architect can run on its own plan or hand-back: CC-01 'every craft brief quotes the same target-experience line'; PP-20 'states, transitions and interruption rules fixed with the animator and builder before keying, one owner of the state machine'; PP-28 'a repeated manual step has a script or a tool ticket'; PI-14 'items added after the plan's approval appear as tickets with a cost'; PP-30 'naming and folder rules exist in the overlay before production'",
     observed: "The rules are present and correct. AR-01 quotes the target line only in the plan header; AR-19 (builder briefs) does not ask the briefs to quote it. No AR line checks the animation state list and its owner, tool tickets for repeated steps, scope tickets after approval, or the naming rule. The coverage 'As' column is honest ('standard'), so the gap is in the books, not in the record",
     evidence: "SKILL.md:82-103 (AR-01..AR-20) read line by line against each library check (cross-craft.md CC-01, pipeline-production.md PP-20/28/30, process-iteration.md PI-14)",
     smallest_fix: "AR-19 add '; each brief quotes the target-experience line'. AR-16 add '; for characters and creatures, the animation states, transitions and interruption rules agreed with the animator and builder, with one owner of the state machine'. Append AR-21 (no renumbering): 'Pipeline: the game's naming and folder rules are named (or proposed before production); every manual step the plan repeats per item has a script or a tool ticket; anything added after the plan's approval is a ticket with its cost. (plan, tickets)'. Optionally add 'each expensive feature with its reason' to AR-15's list (PP-15). Update the role file's 'AR-01 to AR-20' (architect.md:59) and SKILL §7 row 17's check."}
  - {id: F3, class: blocking, check: C8 V11,
     where: "knowledge/jobs/J018-riot-craft/coverage/architect.md:157 ('Proposal rows from other roles against my books (V11): none')",
     expected: "Every proposal row another role wrote against the architect's books is adopted or declined with a reason in the coverage file",
     observed: "Two rows target the architect's books and are not answered: proposals/feature-builder.md:27 (R-05: state the attempt/outcome split, the reason code, and 'a threat's tell is sent at wind-up start with the server time it resolves') and proposals/qa-lead.md:23 (presentation-contract.md §6: each seed is also a qa-lead protected acceptance row when the job has one). Both files were last written 08:31 and 08:32, the coverage at 08:33, so the rows likely landed while the maker worked in the same wave; the gap is real either way. Most of the feature-builder row is already true (R-19, R-13); the tell-timing rule is not stated as a rule anywhere (only implied by worked example C's 'slamAt')",
     evidence: "grep -n 'architecture' proposals/*.md; file times from ls --full-time",
     smallest_fix: "Add both rows to coverage table d. Feature-builder row: adopt the tell clause in one place (R-21: 'a threat's tell is sent at wind-up start with the server time it resolves, never together with the damage'); the rest is already R-19 and R-13 (say so). QA-lead row: add one line under pc §6: 'When the job has protected acceptance tests, the qa-lead turns the truth-overlay, reduced and lowest-quality seeds into protected rows with the same hooks.' or decline it with a reason."}
  - {id: R1, class: recommendation, check: C4 + C7,
     where: "SKILL.md:61 (R-20 'hit-stop pauses ... on each client'); worked-examples.md:12 and :16 (P-2 'bystanders ... no hit-stop on their camera'); presentation-contract.md:69",
     expected: "One clear rule for who runs hit-stop, matching vfx-design (moment-recipes.md:27 MO-09 'local client only'; camera-and-screen.md:94), and engine behaviour that is either documented or marked for a probe",
     observed: "R-20 says every client pauses the attacker's and target's tracks; example A's per-viewer column says bystanders get none. The docs state AdjustSpeed pauses a track (AnimationTrack.yaml:320-324) but say nothing about calling it on a track replicated from another client, or whether the owning client's speed change on its own character replicates to everyone (Animator.yaml:217-232 covers start replication only). The book marks two other undocumented behaviours 'probe before relying' but states this one as fact",
     evidence: "docs mirror grep for AdjustSpeed + replicat: no statement; vfx-design MO-09; worked-examples.md:16",
     smallest_fix: "R-20: 'hit-stop runs on the attacker's and the target's clients (the bystander column says whether bystanders see it); never on the server'. Add a third row to the probes named in pc §5: 'AdjustSpeed(0) on a replicated character track: does it hold on an observing client, and does the owner's own pause replicate? Probe before the contract relies on it.'"}
  - {id: R2, class: recommendation, check: C2 + V4,
     where: "SKILL.md:62 (R-21) and §7 row 19 (SKILL.md:124)",
     expected: "platform-policy/references/rules.md §A rows 13-14: shown odds MUST change while a modifier is active and after a once-only outcome is won. UP-19 general check: the lowest and highest paid-random results share an identical windup. Both are decided by the architecture (which odds the client reads; whether the presenter has the result during the windup); code-review's own worked example F1 is this defect (EggReveal colours the windup by result tier)",
     observed: "R-21 says odds come 'from the same data module or replicated value the server rule uses'. An agent can read that as the base table and show base odds while a luck boost is active. No row says the reveal windup must not branch on the result",
     evidence: "platform-policy rules.md:13-14; universal-principles.md UP-19 general check; code-review/references/worked-examples.md:11",
     smallest_fix: "R-21: replace 'odds' with 'odds (the player's effective odds, modifiers and once-only wins included, from the same function the server rolls with)'. pc §3 step 3 add: 'A paid-random reveal: the windup row's source is the request, identical for every outcome; only the reveal row reads the result tier.'"}
  - {id: R3, class: recommendation, check: C4 + C7,
     where: "SKILL.md:30 (step 4 'losers go to the job's closed doors'); module-contract.md:41 (item 12 'losers copied to the job's closed doors'); architect.md:35",
     expected: "The job's closed doors are the lead's table in the job's decisions.md, with gate, the owner's words and 're-proposed only with new owner words' (orchestration/references/gates-and-feedback.md:51-60). The architect's write scope (architect.md:62) does not include decisions.md",
     observed: "The book tells the architect to write its own technical rejections into a lead-owned file with a different meaning (owner gate decisions); SKILL step 4 also says 'not re-proposed without new evidence', the orchestration table says 'new owner words'",
     evidence: "gates-and-feedback.md:51-60; architect.md:62",
     smallest_fix: "Step 4 and item 12: 'losers are listed in the decision record with the evidence that would reopen them; the lead files them as closed doors when the gate drops them'."}
  - {id: R4, class: recommendation, check: C7,
     where: "architect.md:40 ('Ask before you fill the presentation contract ... two rounds at most, then needs-decision'); presentation-contract.md:42",
     expected: "A path for the common case today: the feature recipe has no needs round yet (the maker's own recipe proposal row; job-types.md §5 Production order), crafts may not be crewed when the plan starts, and inside a saved workflow there are no agent ids",
     observed: "The only fallback named is needs-decision after two rounds; an agent with no crafts to ask may stop the job for values that pc §1 already says to mark UNKNOWN with their owner",
     evidence: "orchestration/references/job-types.md §5; presentation-contract.md:21",
     smallest_fix: "Add to the partner-table lead line: 'When a craft is not in the crew or the stage sets no exchange order, read its documents if they exist, mark the missing values UNKNOWN with that owner, and go on; needs-decision only when an unknown blocks the build.'"}
  - {id: R5, class: recommendation, check: C8 V3 + V14,
     where: "review-checklist.md:27-33 (screening aids)",
     expected: "Known limits complete for the aids as prescribed (my runs on a synthetic sample: .luau presenter with a double-quoted, a spaced and a single-quoted marker name, a concatenated id; a .lua presenter with an id and a 'Hit' marker; a server service with task.delay(0.18), task.wait() and wait(0.5); a Config data module)",
     observed: "All three aids gave the right hits on .luau files (asset id 1 hit incl. the concatenated id; markers 'contact_candidate' and ' \"Hit\"'; timings task.delay(0.18) and wait(0.5)). Misses with no error: the .lua file is skipped entirely by glob *.luau (its id and its 'Hit' marker never show); the single-quoted 'swing_accel' marker is missed. task.wait() is listed as a false reading but the pattern cannot match it. Line 33 points a universal book at 'J018 coverage table d' for where to record runs. Each is a rare case for this kit (examples are .luau; double quotes dominate), so per the lead's severity rule these are known-limit additions",
     evidence: "Grep tool runs on scratchpad arch-rev1/src (paths in the review notes above)",
     smallest_fix: "Known misses: add '.lua source files (use glob *.{lua,luau} when the project has them)' and 'single-quoted or backtick names (or use the pattern [\"'`])'. Remove 'task.wait() yields' from false readings. Line 33: 'record the run in the job's coverage or evidence file'."}
  - {id: R6, class: recommendation, check: C1 (PP-01 landing),
     where: "module-contract.md:43-55 (Design budget)",
     expected: "PP-01 is 'triangle and texture budgets before building; phones first'. The coverage marks it fully landed",
     observed: "The budget has texture memory and frame time but no triangle or draw row, so a pet, crowd or debris system can pass AR-15 without counting what one client draws at peak. The per-asset triangle cap is the modeler's; the count at peak is a system number",
     evidence: "module-contract.md:46-55; pipeline-production.md PP-01 apply/check",
     smallest_fix: "Add one row: 'Triangles on one client at peak | asset class × live copies × triangles per mesh (20,000 per mesh is an import ceiling, not a budget) | modeler's budget per asset; game profile'."}
  - {id: R7, class: recommendation, check: C8 V7 + V6 + C7,
     where: "SKILL.md:60-66 (R-19..R-25) and §6 ending at byte 19,842",
     expected: "Steps, rules and self-check in roughly the first 18 KB; one rule in one place",
     observed: "§6 ends about 1.8 KB past the guide; the §1 re-read note covers it, but AR-15..AR-20 may drop out after a compaction. R-19..R-24 restate presentation-contract.md §2-§5 at length, and §5 rules 6-9 restate them again. J010 also showed longer plans scored no better (scores-architect.md: new plans twice as long, lost on routing, not substance); the new template adds a 12-field contract row and a 9-row budget",
     evidence: "byte offsets from the SKILL.md file; scores-architect.md:17-27",
     smallest_fix: "Cut R-19..R-24 to one line each with the pointer to pc (the depth stays in pc), which brings §6 under 18 KB. Add to §3 step 11: 'Rows or budget lines that do not apply are one n/a line with the reason.'"}
  - {id: R8, class: recommendation, check: C5,
     where: "architect.md:41-51 (partner table); SKILL.md:102 (AR-19)",
     expected: "Old architect.md:42 asked 'the reviewer for a design check'; old Work method 7 set 'the effort (high for money, saves, remotes)'",
     observed: "The partner table has no reviewer row although reviewer.md:24 now offers a plan check on the invariant cards and the contract rows for money, saves, remotes, paid random and trades. AR-19 keeps 'effort' but drops 'high for money, saves, remotes' (still shown only as a code comment example in handoffs.md:35)",
     evidence: "git show df13ff4:.agents/roles/architect.md lines 38, 43; reviewer.md:24",
     smallest_fix: "Partner table: 'reviewer | a plan check of the invariant cards and contract rows | before the build, when the plan touches money, saves, remotes, paid random or trades'. AR-19: 'effort (high for money, saves, remotes)'."}
keep: [
  the presentation contract as the architect's own sheet (presentation-contract.md §1-§3: reads the crafts' documents by revision, never copies values, UNKNOWN with the owner),
  attempt on input / outcome on the confirmed result / pending / rejected shows nothing (R-19, R-06, R-13 with reason codes, AR-07),
  per-viewer facts not pictures, camera channels only for the local player (R-20, §5 rule 7, AR-09),
  one truth source for drawn values and the server timer for countdowns (R-21, worked example C),
  frequent events merged and capped in one presenter (R-24, worked example B),
  the worst-case design budget with sources and 'engine ceilings are not budgets' (module-contract.md Design budget),
  builder brief interface rows, adopted by the feature-builder's handoffs.md and presentation.md (one rule, one place),
  §6 self-review with an input per line and not verified when missing; the review checklist RV-01..RV-12 with inputs,
  the partner table (what to ask each craft, and when),
  the four worked examples, each with what the old plan got wrong,
  §7 core principles: covers every principle the master lists for the architect (UP-02, 07, 08, 13, 15, 16, 17, 19) plus 01, 06, 12, 14, 18, 20 in engineering form; no contradiction found,
  every docs line I checked says what the book claims; the two undocumented behaviours are marked 'probe before relying',
  the owner-question rule from J010 kept word for word (architect.md:30-31)
  ]
verdict: fix-first
</spec>
```

## Check results

| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | fail | 24 tagged findings match the matrix (script count); 45 finding rows checked (24 tagged, 21 untagged); 5 failed (F2: CC-01, PP-20, PP-28, PP-30, PI-14, the check missing); PP-01 partly landed (R6); GD-26 rejection sound |
| C2 core principles | pass | §7 in the first skill; all 8 master-listed principles plus 6 more in engineering form; no contradiction; paid-random windup worth adding (R2) |
| C3 self-review | fail | F2; the other AR/RV lines are runnable with our tools and name their input |
| C4 kit rules and engine | pass (recommendations) | docs claims verified; no invented tool modes; hit-stop rule and engine gap (R1); closed-door meaning and write scope (R3) |
| C5 nothing lost | fail | F1 (isolation by data with a spy or golden test lost); R8 (reviewer ask, effort rule) |
| C6 fixed rules | pass | frontmatter byte-identical (script); SKILL.md 125 lines; description 399 chars; evals unchanged; J018 phrase in every changed header and the role comment; no Riot names, library IDs or transcript lines in bodies; no tips section; LF endings |
| C7 better work | better, with weak spots | see the judgment below |
| C8 brief v2/v3 | fail | V11 (F3); V3 runs pass with known-limit additions (R5); V7 borderline (R7); V1, V2, V4 (R2 tightens), V6, V8, V10, V12, V13 pass |

**Judgment (C7).** Read as the agent at the start of eval E-03 (daily quest rewards) and of a melee feature: the old books gave invariants, owners and lifecycles but nothing on where gameplay hands over to animation, VFX, sound and UI. The new books make the architect write that hand-over (source, payload, per-viewer, comfort, rate, truth, check seeds), ask each craft for its inputs, size the budget at the worst case on the baseline phone, and check its own plan line by line. The plans will be clearly better for any feature players see or hear, and no worse for pure back-end work. Weak spots: the lost isolation proof (F1), a few checks without a self-review line (F2), hit-stop ownership unclear and undocumented (R1), paid-random odds and windup (R2), and plan length (R7).
