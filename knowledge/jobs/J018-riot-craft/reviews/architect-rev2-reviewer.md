---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer architect · claude-opus-5-5 · high · 2026-10-22

# Review: architect books, rebuild round 2 (J018 stage 3)

```text
<spec>
artifact: .agents/roles/architect.md (body) + .agents/skills/architecture/ (SKILL.md 124 lines; references/module-contract.md, presentation-contract.md, review-checklist.md, worked-examples.md; evals/ excluded), working tree on top of df13ff4 after repair round 1, 2026-10-22
reviewer: J018 reviewer architect (opus, high)
looked_at_first: [
  all 6 book files read in full as they are now; git show df13ff4 of architect.md and SKILL.md; git diff df13ff4 of module-contract.md (removed lines: only the author line and items 3, 6, 7, 9, each replaced by a sharpened copy),
  my round 1 review (architect-rev1-reviewer.md): every finding F1-F3, R1-R8 re-checked in the books,
  matrix.md architect column extracted by script (24 findings, same 24 as the coverage table) and the principle, apply and check of all 24 in the topic files,
  universal-principles.md: the eight principles whose applies-to names the architect (UP-02, 07, 08, 13, 15, 16, 17, 19), engineering lines and general checks,
  partner books at their current state: engineering-craft references/presentation.md §1-§9 and handoffs.md §0-§1, code-review references/presentation.md PT-08 and S6, vfx-design camera-and-screen.md (B2, CA-07, tools row) and moment-recipes.md MO-09, animation-design game-timing.md §4-§5, templates/anim/timing-list.md, testing T-06 and T-10, performance F-01/F-03/F-09, modeling-design M-13, networking-security N-06/N-09/N-14, reviewer.md "Plan check", preproduction documents.md §6, §7, §9, the role files of animator, vfx-designer, sound-designer, ui-ux-designer, game-designer, qa-lead, performance-engineer,
  docs mirror: art/modeling/specifications.md:34 (20,000 triangles per mesh, as the new triangle row says),
  every proposals/*.md row that names the architect's books (grep), with file times,
  my own runs of the three Grep screening aids, exactly as review-checklist.md §3 prescribes (path = logic folder, glob *.{lua,luau}), on a new synthetic Rojo sample (scratchpad arch-rev2: a .luau presenter with an rbxassetid string, a bare 7-digit id, a concatenated id, a 6-digit rbxassetid, double/spaced/single/backtick/interpolated/variable marker names, task.delay(0.18) and TweenInfo.new(0.25); a .lua presenter with an id, "Hit" and task.delay(.2); a server service with task.delay, task.wait(), wait(0.5), task.wait(1), task.wait( 0.3 ) and an 8-digit seed; a Config data module),
  scripts: frontmatter byte compare with df13ff4, line and byte counts, description length, J018 header phrase per file, CR check, grep for library IDs, Riot names and "tips"
  ]   # the maker's coverage and proposals files were read after this
findings:
  - {id: F1, class: blocking, check: C8 V11 + V10,
     where: "knowledge/jobs/J018-riot-craft/proposals/feature-builder.md:35 (targets presentation-contract.md §3 step 4 and §5 hit-stop line); coverage/architect.md V11 table (lines 183-188) does not list it",
     expected: "Every proposal row another role wrote against the architect's books is adopted or declined with a reason (V11), and hand-offs agree with the partner books already rebuilt (V10)",
     observed: "The row landed at 08:55:56, after the architect's repair (coverage written 08:54:04), so the maker could not see it; the gap is real all the same. It asks for two things, both of which matter: (1) presentation-contract.md:130 lists the builder's test hooks as `Trigger`, `Rate`, `Reject`, `DelayMs`, `Reduced`, `Viewer`, `DebugShape`, `FxLog`; the builder's set (engineering-craft/references/presentation.md §9) now also has `Clarity`, `Outcome` / `Seed` and `Set`, so the contract cannot seed the clarity branch of its own comfort service (pc §4 'Effect clarity') or force a tier or denial on demand; the list is a copy that has already drifted (V6). (2) presentation-contract.md:155 says the presenter pauses the tracks 'then restores both', and RV-08 (review-checklist.md:84) passes on 'tracks restored' from 'a frame folder of a hit'. The builder's review found that restoring a saved previous speed leaves a track frozen when two stops overlap (presentation.md §4: one owner per track, a stop-until time, the base speed; code-review PT-08 checks the overlap sequence). A single-hit frame folder cannot show that defect, so an architect review can pass the code PT-08 fails",
     evidence: "proposals/feature-builder.md:35; ls --full-time (feature-builder.md 08:55:56, coverage/architect.md 08:54:04); presentation.md §4 line 52 and §9 table; code-review/references/presentation.md:31 (PT-08)",
     smallest_fix: "pc §3 step 4: replace the hook list with 'the test hooks and debug log lines the seeds need, by the names in `engineering-craft/references/presentation.md` §9' (one place, no copy). pc §5 hit-stop line: 'then restores both' -> 'and the hit-stop owner of each track and emitter sets the base speed back when the stop ends and on interruption (`engineering-craft/references/presentation.md` §4)'. RV-08 Input add 'the offline overlap test (two stops 50 ms apart; one cut by death)'; Pass add 'both end at base speed'. Add the row to the V11 table as adopted."}
  - {id: R1, class: recommendation, check: C7 + C4 (internal consistency) + V10,
     where: "SKILL.md:46 (R-05 'may predict, then reconciles'), SKILL.md:60 (R-19 'the outcome layer only on the server-confirmed result'), SKILL.md:74 (§5 'No outcome layer before the server confirms'); presentation-contract.md:114 (Layer list)",
     expected: "One rule for client prediction that the builder can cite. The builder's book allows prediction where the spec allows it, with rollback in the frame the denial arrives, never for money, rewards or paid reveals (presentation.md:28), and lets the attacker's own client start a predicted hit-stop on `contact_candidate` (presentation.md:53). The architect's own proposal (proposals/architect.md:25) asked the builder to tie that predicted stop to a contract row marked as such",
     observed: "R-05 permits prediction with no condition; R-19 and §5 forbid any outcome layer before confirmation; the contract's Layer list has no 'predicted' layer, so the builder has no row type to cite and a reviewer reading §5 will flag the builder's allowed prediction as a defect. Read cold, an architect may forbid prediction a shooter needs, or allow it for a purchase",
     evidence: "SKILL.md:46, :60, :74; presentation-contract.md:114, :129; engineering-craft/references/presentation.md:28, :53",
     smallest_fix: "pc §2 Layer: add 'predicted (only where the feature spec allows it; removed in the frame the denial arrives; never money, rewards or paid reveals)'. §5 rule: 'No outcome layer before the server confirms, except a predicted row the spec allows'. R-05: 'may predict (a predicted row in the contract, R-19), then reconciles'."}
  - {id: R2, class: recommendation, check: C7 + V10,
     where: "SKILL.md:93 (AR-13); presentation-contract.md:122 (Information field)",
     expected: "A check whose pass is unambiguous: under each condition (grayscale, sound off, reduced motion, lowest graphics quality) at least one channel of the fact remains",
     observed: "'names two or more channels that survive grayscale, sound off, reduced motion and the lowest graphics quality' can be read as every named channel surviving all four, which no sound channel can do; the worked examples list sound as one of the two (worked-examples.md:16-18, :62). An agent will either fail its own good rows or stop checking the sound-off case",
     evidence: "SKILL.md:93; presentation-contract.md:122; worked-examples.md:18 ('absence of spark + whiff')",
     smallest_fix: "AR-13: 'Every gameplay fact names two or more channels, so that grayscale, sound off, reduced motion and the lowest graphics quality each still leave at least one.' Same words in pc §2 Information."}
  - {id: R3, class: recommendation, check: C7 + V10,
     where: ".agents/roles/architect.md:44 (animator row: '... where each clip starts (server or owning client)')",
     expected: "The architect asks each craft for values that craft owns; where a clip starts is an engineering decision from the replication rules (pc §5 row 2: 'the contract says where each clip starts', Animator.yaml:217-232)",
     observed: "The animator's timing list (templates/anim/timing-list.md) has no such field and the animator's books never decide replication; the ask sends a question to the wrong owner and may come back empty",
     evidence: "templates/anim/timing-list.md:20-31; presentation-contract.md:149",
     smallest_fix: "Animator row: drop 'where each clip starts (server or owning client)'; add 'the clip list and which clips play on NPCs' (the architect then decides the start place in the contract, as pc §5 already says)."}
  - {id: R4, class: recommendation, check: C7 + V10,
     where: "role files .agents/roles/animator.md, vfx-designer.md, sound-designer.md, ui-ux-designer.md and their design and craft skills (rebuilt in waves 1-2)",
     expected: "A partner the architect asks before the presentation contract freezes knows to answer: its partner table names the architect and what to send",
     observed: "grep 'architect' and 'presentation contract' over those four role files and over animation-design, animation-craft, vfx-design, vfx-craft, sound-design and ui-design: 0 hits. The architect's partner table and the needs-round recipe proposal (proposals/architect.md:17) cover the architect's side; the receiving side has no row. The game-designer (game-designer.md:52), qa-lead (qa-lead.md:42), reviewer and performance-engineer do name the architect",
     evidence: "grep over .agents/roles and the six skills named",
     smallest_fix: "proposals/architect.md: one row for the lead (later round, or the four makers if they reopen): add to each of the four role files' partner table 'architect | the needs for the presentation contract: <the role's row of architect.md's partner table> | before the presentation contract freezes'."}
keep: [
  every round 1 finding is fixed in the books, not only in the coverage: F1 isolation by data with its spy or golden proof (SKILL step 9, AR-03, mc item 9; the role build comment is true again), F2 (AR-19 quotes the target line, AR-16 animation states with one state-machine owner, AR-21 naming, tool tickets and post-approval tickets with cost, AR-15 expensive features), F3 (both rows answered; the tell clause sits in R-21 once), R1 (hit-stop clients named in R-20, AR-09, RV-08, example A; probe 3 added), R2 (effective odds in R-21; windup row reads only the request in pc §3 step 3 and AR-07), R3 (losers carry reopen evidence; the lead files closed doors), R4 (UNKNOWN with the owner and go on), R5 (screening aids), R6 (triangle row, docs line checked), R8 (reviewer row matches reviewer.md:24 and :45; effort rule back),
  the presentation contract as the architect's own sheet, reading the crafts' documents by revision and never copying their values; the builder's sheet now cites its P-n rows (presentation.md §1), so the two sheets no longer drift,
  attempt on input, outcome on the confirmed result, pending, rejected shows nothing; per-viewer facts, not pictures; one truth source including the tell's server time; merge and cap in one presenter; one local comfort service,
  the worst-case design budget with a source per row and 'engine ceilings are not budgets' (now with triangles),
  §6 AR-01..AR-21 each with its input; RV-01..RV-12 with inputs and the three screening aids,
  the screening aids as prescribed give the right hits on my new sample: asset ids (the .lua id, the rbxassetid strings including the 6-digit one, the bare and the concatenated ids), marker names (all five literal forms, the template shown, the variable name missed as listed), timings (.2 and spaced forms found, task.wait() not matched, task.wait(1) shown as listed, TweenInfo missed as listed); no wrong number without a listed limit,
  §7 core principles: all eight master principles for the architect plus six more in engineering form, each with its own example and a check line; no contradiction with universal-principles.md,
  the four worked examples, each with what the old plan got wrong,
  nothing of the old books lost (C5 walk below); the owner-question rule from J010 word for word
  ]
could_not_check: [
  "whether the plans an agent writes with these books are better in practice: no eval run in this review (evals are read-only in J018; the maker's proposal row for E-05 and E-06 is the way to measure it)",
  "the three Studio probes the books name: no Studio instance in this review; the books mark them 'probe before relying', which is the right state"
  ]
verdict: fix-first
</spec>
```

## Check results

| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | pass | 24 tagged findings = matrix (script); 45 rows checked (24 tagged, 21 untagged), 0 failed. The 5 rows that failed in round 1 (CC-01, PP-20, PP-28, PP-30, PI-14) now land with their check (AR-19, AR-16, AR-21); PP-01 has its triangle row; partial rows give their reason; the GD-26 rejection is sound |
| C2 core principles | pass | §7 in the skill loaded first; UP-02, 07, 08, 13, 15, 16, 17, 19 plus 01, 06, 12, 14, 18, 20 in engineering form; no contradiction |
| C3 self-review | pass | every checkable architect finding has an AR line (own plan) or a seed and RV line (captures by qa-lead or studio-operator); each line names its input |
| C4 kit rules and engine | pass (recommendations) | new docs claim checked (specifications.md:34); every skill ID and section pointer checked exists; no invented tool modes; prediction rule unclear inside the books (R1) |
| C5 nothing lost | pass | old role Work method 1-8, Working with other agents, write scope, hand-back; old SKILL §3 steps 1-6, R-01..R-18, §5, §6; module-contract items 3, 6, 7, 9: each kept, moved or sharpened (isolation and effort restored in round 1) |
| C6 fixed rules | pass | role frontmatter byte-identical to df13ff4; SKILL.md 124 lines; description 399 characters; evals unchanged; J018 phrase in every changed header and the role comment; no library IDs, Riot names or tips section in bodies; LF endings; no section renumbered |
| C7 better work | better, with weak spots | see below |
| C8 brief v2/v3 | fail | V11 and V10: F1 (a builder row landed after the repair; hook list and hit-stop restore drift). V3 runs pass on my sample; V1, V2, V4, V6 (except the hook list), V8, V12, V13 pass; V7: §6 ends at 19.96 KB (about 5,000 tokens), accepted with the maker's reason and the §1 re-read rule |

**Judgment (C7).** Read as the agent at the start of eval E-01 (burst-fire weapon) and of a melee feature. The old books gave invariants, owners, lifecycles and a locality check, and nothing on where gameplay hands over to animation, VFX, sound and UI. The new books make the architect restate the game's parameters and the target line, spike the risky claim, write the hand-over row by row (source, payload, per viewer, comfort, rate, information, truth, check seed), set a worst-case budget on the baseline phone, brief builders with interface rows, and check its own plan line by line. For any feature players see or hear, the plans will be clearly better: the round 1 losses (isolation proof, missing self-review lines) are back. Back-end-only work is no worse: the contract is one n/a line. Weak spots: the prediction rule contradicts itself across R-05, R-19 and §5 (R1). AR-13's wording can fail every sound channel (R2). One ask goes to the wrong owner (R3). The receiving crafts do not know about the contract yet (R4). And plan length stays a risk the n/a rule only partly controls.
