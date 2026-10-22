---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer architect · claude-opus-5-5 · high · 2026-10-22

# Review: architect books, rebuild round 3 (J018 stage 3)

```text
<spec>
artifact: .agents/roles/architect.md (body) + .agents/skills/architecture/ (SKILL.md 124 lines; references/module-contract.md, presentation-contract.md, review-checklist.md, worked-examples.md; evals/ excluded), working tree on top of df13ff4 after repair round 2 (files written 09:02-09:03, 2026-10-22)
reviewer: J018 reviewer architect (opus, high)
looked_at_first: [
  all 6 book files read in full as they are now; git show df13ff4 of architect.md and SKILL.md (old role body and old §1-§6 walked line by line); section headings old vs new (SKILL §1-§6 kept, §7 appended; module-contract sections added without numbers),
  both earlier reviews: rev1 F1-F3, R1-R8 and rev2 F1, R1-R4, each re-checked in the books,
  matrix.md architect column extracted by script (24 findings, same 24 as the coverage table); principle, apply and check of all 24 in the topic files; VR-22 and the library's prediction line (game-design-fun.md:462),
  universal-principles.md: applies-to lists of UP-01..UP-20, and the engineering and general-check lines of UP-13..UP-19,
  partner books at their current state: engineering-craft references/presentation.md §1-§12 (prediction §2, hit-stop §4, comfort module §6, test hooks §9), code-review references/presentation.md PT-08 and S6, review-method.md §7 (plan check), animation-design game-timing.md §1-§5, templates/anim/timing-list.md, reviewer.md (Plan check, partner rows), game-designer.md, qa-lead.md, feature-builder.md, performance-engineer.md partner rows; networking-security N-03, N-06, N-09, N-14; data-saving D-11,
  every cross-reference ID and path the books name (S-140, F-01..F-09, N-03..N-14, D-11, D-15, M-13, T-06, T-10, EC-01..EC-12, E-08, the reference files and sections): all exist,
  docs mirror: every cited line re-read (GuiService.yaml:262-277, Animator.yaml:217-232, AnimationTrack.yaml:320-324, ParticleEmitter.yaml:502-511 and 962-968, highlighting.md:37, particle-emitters.md:212, improve.md:418-421 and 567, packages.md:14 and 19, scripting/locations.md:36-40, accessibility.md:184-210, animation/events.md:12),
  my own runs (V3): the three Grep screening aids exactly as review-checklist.md §3 prescribes (Grep tool, glob *.{lua,luau}, path = a logic folder) on a new synthetic Rojo sample (scratchpad architect-rev3: a .luau presenter with a 7-digit rbxassetid, a bare 10-digit id, a 6-digit rbxassetid, double/spaced-single/backtick/variable marker names, task.delay(0.18), task.wait(.25), the deprecated global delay(0.2, f) and TweenInfo.new(0.3); a .lua presenter with an 8-digit id, "Hit" and wait(0.5); a server file with an 8-digit seed, task.wait(), task.wait(1), task.delay( 0.3 , fn) and :Wait(); a Config data module; a .txt file with an id); the context packet command the role file names (python tools/context_packet.py packet ... --role architect --job J018-riot-craft),
  scripts: frontmatter byte compare with df13ff4, line and byte counts, offsets of §6 and §7, description length, J018 header phrase per file, CR check, grep for library IDs, Riot and franchise names and "tips"; git status and diff --stat of the architecture folder and evals/,
  proposals/*.md rows naming the architect or the architecture books (grep), with file times against the coverage file (09:04)
  ]   # the maker's coverage and proposals files were read after this
findings:
  - {id: R1, class: recommendation, check: C7 + C4 (internal consistency) + V10,
     where: "references/presentation-contract.md:28 (§2 Layer, 'predicted ... small, never the confirmed outcome's layer') against :43 (§3 step 3, 'for example the attacker's hit-stop on `contact_candidate`')",
     expected: "The one prediction rule and its one example agree, so an architect (or the reviewer running the plan check) can tell from the rule alone whether a predicted hit-stop row passes AR-07",
     observed: "The Layer rule says a predicted row is 'never the confirmed outcome's layer'. The only example of a predicted row is the attacker's hit-stop, which the same book's worked example A puts inside the confirmed outcome row (worked-examples.md:16, P-2 'spark, hit sound, hit-stop' from `HitResolved`) and which the master principle counts as part of the confirmed response ('the big contact pose, hit-stop and follow-through scale with the confirmed hit's strength'). Read cold, the rule forbids its own example; a predicted stop also cannot be sized by a tier it does not know yet. The builder's book allows the predicted stop and ends it on denial (presentation.md:53), so the risk is a false finding in a plan check or an architect who forbids the stop in a game whose spec allows prediction, not a player-facing defect",
     evidence: "presentation-contract.md:28, :43; worked-examples.md:12, :16; engineering-craft/references/presentation.md:28, :53; universal-principles.md UP-19 motion line; library game-design-fun.md:462 ('a predicted hit that the server rejects never shows the confirmed-hit layer')",
     smallest_fix: "pc §2 Layer, predicted: 'small, never the confirmed outcome's tiered layer (spark burst, celebration, reward sound, shake); the attacker's own short hit-stop on `contact_candidate` is the allowed case, its tier length waits for the result'. No other place changes (AR-07 points to the Layer rule)."}
  - {id: R2, class: recommendation, check: C8 V3 + V14,
     where: "references/review-checklist.md:32 (§3 'Guessed timings' aid, Known misses column)",
     expected: "Every literal delay form the aid does not find is listed in its known misses, so a clean screen is not read as 'no guessed delays'",
     observed: "On my sample the aid finds task.delay(0.18), task.wait(.25), task.delay( 0.3 , fn), wait(0.5) and task.wait(1) (listed false reading), and skips task.wait() and :Wait() correctly; it misses the deprecated global `delay(0.2, f)` with no error. The pattern already covers the deprecated global `wait(`, so the gap reads as an oversight. The global form is deprecated and rare in `--!strict` code, so this is a known-limits item under the lead's severity rule, not blocking; every hit is still read in the code (§3 intro)",
     evidence: "Grep run on scratchpad architect-rev3/src, glob *.{lua,luau}: 6 hits, MeleePresenter.luau:13 `delay(0.2, function() end)` not among them",
     smallest_fix: "Pattern: append `\\|\\bdelay\\(\\s*[0-9.]+` (typed with a plain bar), or add 'the deprecated global `delay(n, f)`' to the Known misses cell. Record the re-run in the coverage file."}
  - {id: R3, class: recommendation, check: C7 + AGENTS.md §0 (Roblox docs before you design),
     where: "knowledge/reference/roblox/docs-map.md:17 (architect row; not the maker's file) via proposals/architect.md (no row)",
     expected: "The context packet sends the architect to the docs sections its rebuilt book now leans on",
     observed: "The presentation contract and the design budget rest on `animation/events.md`, `effects/particle-emitters.md`, `effects/highlighting.md`, `production/publishing/accessibility.md` and the Animator, AnimationTrack, ParticleEmitter and GuiService class pages. The architect's docs-map row (printed by the packet) names only `scripting/`, `luau/`, `physics/`, `workspace/`, `players/`, `input/`, `cloud-services/` and RemoteEvent, DataStoreService, MarketplaceService, Players, Workspace. An architect on a melee or VFX-heavy feature is pointed at none of the pages its contract needs; the book's cited lines carry it today, but a new engine question (a Beam, an AudioFader bus, a Highlight mode) has no map row",
     evidence: "context_packet.py output for --role architect (docs-map L17 row); presentation-contract.md §4-§5 citations; module-contract.md Design budget citations",
     smallest_fix: "proposals/architect.md: one row for the lead: add `animation/` (events.md), `effects/`, `production/publishing/accessibility.md` and the classes Animator, AnimationTrack, ParticleEmitter, GuiService, Highlight to the architect's docs-map row (L17)."}
  - {id: R4, class: recommendation, check: C4 (docs citation),
     where: "references/presentation-contract.md:52 (§4 Reduced motion row: 'tweens snap (time 0) or fade (`production/publishing/accessibility.md:186-188`)')",
     expected: "Each cited docs line says what the book claims",
     observed: "Lines 186-188 state the snap (TweenInfo time 0); the fade fallback is at lines 208-210. The claim is true, the line range is short",
     evidence: "accessibility.md:186-188 (snap only), :208 ('switches to fade-in for players who enable reduced motion'), :210",
     smallest_fix: "Cite `production/publishing/accessibility.md:186-188, 208-210`."}
keep: [
  every earlier finding is fixed in the books, not only in the coverage. Round 1: F1 isolation by data with its spy or golden proof (SKILL.md:35, AR-03, module-contract item 9), F2 (AR-15, AR-16, AR-19, AR-21), F3 and the V11 rows, R1 hit-stop clients (R-20, AR-09, pc §2 and §5, RV-08), R2 effective odds (R-21) and the windup row (pc §3 step 3, AR-07), R3 losers with reopen evidence, R4 UNKNOWN and go on, R5 screening aids, R6 triangle row (docs line re-checked), R7 accepted in part with its reason, R8 reviewer row and effort. Round 2: F1 hook list now a pointer to the builder's §9 (pc §3 step 4, mc 'Test hooks' and 'Settings read'), hit-stop restore through one owner per track and emitter with the base speed (pc §5, new seed 'Hit-stop', RV-08 with the offline overlap test as input, example A); R1 one prediction rule in pc §2 Layer, referred to from R-05, R-19, §5 and AR-07; R2 AR-13 and pc §2 Information now pass when each condition leaves at least one channel; R3 animator row asks for the clip list and NPC clips, the start place is the architect's decision; R4 the receiving-side partner rows are a proposal row for the lead,
  the presentation contract as the architect's own sheet: it reads each craft's document by path and revision, refers to values by key or id and never copies them; the builder's sheet cites its P-n rows, so the two sheets cannot drift,
  attempt on the input frame, outcome on the server result id (never a marker), pending when slow, nothing of the outcome for a rejected request; per-viewer facts, never pictures; one truth source including the tell's server time; merge and cap in one presenter; one local, read-only comfort and clarity service that matches the builder's five accessors,
  the worst-case design budget with a source per row and 'engine ceilings are not budgets' (particle Rate, Highlight 255, 20,000 triangles per mesh, all re-checked in the mirror),
  §6 AR-01..AR-21 each naming its input; RV-01..RV-12 with inputs and pass rules; three labelled screening aids with false readings and misses, and the rule that every hit is read in the code,
  §7 core principles: the eight master principles that name the architect (UP-02, 07, 08, 13, 15, 16, 17, 19) plus UP-01, 06, 12, 14, 18, 20 in their engineering form, each with its own example and a check line; the six 'no' rows give sound reasons; no contradiction with universal-principles.md,
  the role file's partner table (what to ask each craft, and when, two rounds at most) and the problem-behind-the-note rule; the owner-question rule from J010 word for word,
  the four worked examples, each with what the old plan got wrong and its check lines; re-read against the round 2 changes (A: no prediction, contact-pose hold, overlap-safe stop; B: balance never predicted; D: no purchase predicted)
  ]
could_not_check: [
  "whether plans written with these books are better in practice: no eval run in this review (evals are read-only in J018; proposals/architect.md row 'E-05, E-06' is the way to measure it)",
  "the three Studio probes the books name (marker signals on an observing client, a live ReducedMotionEnabled change, AdjustSpeed(0) on a replicated track): no Studio instance in this review; the books mark them 'probe before relying', which is the right state"
  ]
verdict: pass
</spec>
```

## Check results

| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | pass | 24 tagged findings = matrix (script); 45 rows checked (24 tagged, 21 untagged), 0 failed. Each landed-in location carries the rule and, where the finding has a check the architect can run, its AR or RV line. Partial rows (MD-05, PP-04, PP-24, VR-17) give sound ownership reasons; GD-26 rejection is sound (spawn-to-contact is level and game design; the match-phase owner and server clock stay in R-02 and R-04) |
| C2 core principles | pass | §7 in `architecture`, the skill loaded first; 14 principles in engineering form with example and check; the 6 not applied are about pictures and give their reason; no contradiction (R1 is an internal wording point, not a conflict with the master) |
| C3 self-review | pass | every checkable architect finding has an AR line on the agent's own plan or a seed plus RV line on named captures and test logs (qa-lead, studio-operator, performance-engineer); stills, device captures and recipes are named as what each can prove |
| C4 kit rules and engine | pass (recommendations R1, R4) | every docs line re-read; every cross-reference ID and path exists; shared-skill lines (N-03, N-06, N-09, N-14, D-11, platform-policy odds) agree; no invented tool mode; no rule, recipe, workflow or tool changed |
| C5 nothing lost | pass | old role body (Work method 1-8, Working with other agents, write scope, hand-back) and old SKILL §1-§6, R-01..R-18, module-contract items 1-9: each kept, moved or sharpened; the only removal is the J016 pointer, replaced by the books themselves |
| C6 fixed rules | pass | only the architect's books and the two job files for this role changed; role frontmatter byte-identical to df13ff4; SKILL.md 124 lines; description 399 characters; evals/ unchanged; J018 phrase in every changed header and the role comment; no library IDs, Riot names, transcript lines or tips section in the bodies (internal AR, RV, EC ids only); LF endings; no section renumbered |
| C7 better work | better | see below |
| C8 brief v2/v3 | pass (recommendations R2, R3) | V3: the three screening aids and the context packet run as prescribed and give the right answers on my sample, except one unlisted miss in a labelled aid (R2, recommendation under the lead's severity rule); V1, V2, V4, V6, V8, V10, V11, V12, V13 pass; V11: no proposal row against the architect's books arrived after the round 2 coverage (09:04); V7: §6 ends at 20.3 KB, above the 18 KB guide, accepted with the maker's reason and the §1 re-read rule after compaction |

**Judgment (C7).** I read the books as the agent would at the start of eval E-01 (burst-fire weapon) and of a melee feature. The old books gave invariants, owners, lifecycles and a locality check. They said nothing about where gameplay hands over to animation, VFX, sound and UI. The new books make the architect do more before it plans: restate the game's parameters and the target line, and spike the claim the design rests on. The burst gets the four timed-action invariants. The plan then writes the hand-over row by row (source, payload, per viewer, comfort, rate, information, truth, check seed) and sets a worst-case budget on the baseline phone. Builder briefs carry interface rows that point to the builder's own hook list, and the agent checks its own plan line by line before hand-back. For any feature players see or hear, the plans will be clearly better. Back-end-only work (E-02, E-03, E-04) is no worse: the contract becomes one n/a line, and the push-back on frameworks (R-09, R-15, §7 row 6) is stronger. Remaining weak spots: one wording that makes the prediction rule seem to forbid its own example (R1); one unlisted miss in a screening aid (R2); the docs map does not yet send the architect to the animation, effects and accessibility pages its contract uses (R3). Plan length is still a risk: 21 self-review lines and a twelve-field row per event can make a 100-line plan much longer. The n/a rule and the "as short as the builder needs" stop rule only partly control this, and an eval run would show it.
