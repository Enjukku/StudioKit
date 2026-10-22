---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer game-designer · claude-opus-5-5 · high · 2026-10-22

# Review: game-designer books, round 3 (J018 stage 3, after repair round 2)

```text
<spec>
artifact: .agents/roles/game-designer.md (body) + .agents/skills/game-concept/ (SKILL.md, references/) + .agents/skills/preproduction/ (SKILL.md, references/) + .agents/skills/game-design/ (SKILL.md, references/ incl. new spaces.md), working tree on top of df13ff4 (HEAD 2c54520 touches no book file), 2026-10-22, after repair round 2 (files saved 03:39-03:41)
reviewer: J018 reviewer game-designer (opus, high)
looked_at_first: [
  the books before the maker's files: role file and the 3 SKILL.md read in full; game-design references principles.md, review.md, loops.md, systems-economy.md, playtest-live.md, spaces.md read in full; preproduction documents.md, growth-order.md, handoffs.md read in full; game-concept references read through the full diff,
  git diff df13ff4 for all 16 changed files (every removed line walked) and a section-heading diff per file,
  knowledge/reference/craft/riot/universal-principles.md (UP-01..UP-20: "applies to" lists and each "design:" line), matrix.md (game column, script: 145 IDs), library entries VR-21, WT-21, EX-07, RI-24, UI-10, VH-07, SD-09, WT-24 read against their landing places,
  tools: look_check.py silhouette / value --help and source (estimate_border_key :234-250, key_mask :220-223, subject_mask, mask_problem, DEFAULT_KEY_TOL 40, MASK_MAX_FRAC 0.98), thumb_check.py thumbnail --help (--size, --size-source, --box, --bottom-band), clip_metrics.py (median background :100, summarise :78-93),
  marketing-craft references/image-pipeline.md:25-32 (surfaces.md, bottom band), level-design SKILL.md:38 and :58,
  roblox-creator-docs StarterPlayer.yaml:243-249, 272-278, 329-357, 358-364; Lighting.yaml:389 (GlobalShadows),
  game-concept/evals/briefs.md briefs 1-5 (hidden key not opened),
  reviews/game-designer-rev1-reviewer.md and rev2 (every earlier finding re-checked), job-card.md, decisions.md (no decision after J018-D5)
  ]   # coverage/game-designer.md and proposals/game-designer.md were read after the books
findings:
  - {id: R1, class: recommendation, check: C3 (check fidelity),
     where: ".agents/skills/game-design/references/review.md:59 (flat-key capture definition); .agents/roles/game-designer.md:59 (studio-operator row points to it); knowledge/jobs/J018-riot-craft/proposals/game-designer.md:35 (studio-mcp flat-key recipe row)",
     expected: "A black-fill measure (lineup size rank, look-alike IoU, variant 10 % footprint band) measures the subject only. The tool counts every pixel more than 40 per channel away from the key colour as subject (look_check.py:220-223), so a shadow the subject casts on the key surface becomes part of the black-fill",
     observed: "The definition asks for a flat colour filling the frame border and, for a top-down camera, a backdrop under the subject, but says nothing about shadows. Under the place's sun the subject's shadow falls on that floor (top-down) or on the key floor in front of a key wall (the angled third-person game camera, whose lower border is ground). The border can still key flat, so the tool reports a valid mask and an area that includes the shadow: a variant can pass or fail the 10 % band on its shadow, and a lineup rank can follow sun angle instead of size. No `invalid-mask` warns the agent",
     evidence: "look_check.py key_mask (diff > tol = subject), estimate_border_key (only the border strip must be flat); Lighting.GlobalShadows exists and is on by default (roblox-creator-docs _api-reference/classes/Lighting.yaml:152, :389); not probed in Studio, so the size of the error is unknown",
     smallest_fix: "review.md:59 after 'one subject per capture or units spaced apart for `--component`': 'shadows off for the capture (Lighting.GlobalShadows false), because a shadow on the key surface counts as subject; for an angled camera the floor and the backdrop both carry the key colour'. Add the same two conditions to the studio-mcp proposal row (proposals :35) so the probe checks them"}
  - {id: R2, class: recommendation, check: C4 (engine) + C7 (contradiction the agent reads),
     where: ".agents/skills/level-design/SKILL.md:38 (L-07) vs .agents/skills/game-design/references/spaces.md:1, :18; knowledge/jobs/J018-riot-craft/proposals/game-designer.md:21-22 (the two level-design rows)",
     expected: "The books the agent loads for a space give one answer on jump height. The role file loads `level-design` for every space (role file :18); the maker found and fixed the wrong default in its own book in repair round 1 (rev1 R7), so the shared skill that says the opposite should get a proposal row",
     observed: "spaces.md says CharacterUseJumpPower defaults to true, JumpPower 50 governs, measure the jump in the place; level-design L-07 still says 'default jump height is 7.2 studs, so a ledge above it is a wall'. The two level-design proposal rows cover map mechanics, cover, collision and re-rating checks, not this line. In a stage review (eval brief 5 is a level review) the agent meets both statements",
     evidence: "StarterPlayer.yaml:329-339 ('Defaults to `true`'; JumpHeight shown only when false); level-design/SKILL.md:38; proposals rows 21-22",
     smallest_fix: "Add one row to proposals/game-designer.md: target `.agents/skills/level-design/SKILL.md` L-07; change: 'CharacterUseJumpPower defaults to true, so JumpPower 50 governs; 7.2 studs applies only when it is false; a ledge is checked against the jump height measured in the place and written in the game profile'; why: contradicts `game-design/references/spaces.md` §3 and the docs mirror; evidence: StarterPlayer.yaml:329-339"}
  - {id: R3, class: recommendation, check: C5 (navigation lost),
     where: ".agents/skills/game-design/SKILL.md:17 ('Read this file when' row for references/principles.md); coverage/game-designer.md table c row 'game-design/SKILL.md:16-18 ... sharpened'",
     expected: "The row still names every part of principles.md, because the role file says 'Open references only through each skill's Read this file when table' (role file :18)",
     observed: "The df13ff4 row ended '... mechanics that carry the theme, where experts disagree'; the new row drops 'where experts disagree' (principles.md §6, still present: mastery vs wider experience, quests vs exploration) and does not name §10 'one code for the whole game'. The content is kept, but the pointer to §6 is gone, so an agent judging a quest-heavy or exploration design will not open it. The coverage record calls the row 'sharpened'",
     evidence: "git show df13ff4:.agents/skills/game-design/SKILL.md line 22 vs current :17; principles.md:59-61, :91-95",
     smallest_fix: "SKILL.md:17 append ', one code for the whole game, where experts disagree'"}
keep: [
  every keep item of rev1 and rev2 still holds (review.md §7 per-recipe check lists; playtest-live.md §1b and the could-not-check list; documents.md §6-§9 contracts; spaces.md; handoffs.md §2 needs and examples §3.6-§3.7; the game-concept warm-up, hook sources, big swing, goal questions, closed doors; four parts with an empty "decisions" line as a finding; G-17..G-23 and the §7 rows; PROPOSAL labels; honest coverage and proposals),
  repair round 2 itself: one definition of the flat-key capture (review.md:59) used at every black-fill measure (review.md:62, :63, :65, :68; systems-economy.md:67; documents.md:135; handoffs.md:258; SKILL.md:102) and asked for in the role file's studio-operator row with the reason; the explicit "on invalid-mask ask for a recapture or a --mask, never judge by eye and call it measured",
  the same gap found and fixed by the maker on the stage line (review.md:75: `look_check.py value --box` on an in-scene capture),
  the clip conditions for clip_metrics.py written once (principles.md:73: median background, still frames for more than half the clip, nothing else moving, onset from a tenth of the peak) and pointed to from documents.md:96 and the role file,
  the tile check (hook-promise.md:29): size and bottom band from `knowledge/design/marketing/surfaces.md` (the same source the marketing books use, image-pipeline.md:29-31), `--box` on the hero, `not measured` instead of an invented size,
  the small size of the repair: clauses on existing lines, no new section, SKILL.md line counts unchanged
  ]
verdict: pass
</spec>
```

## Earlier findings: status

| Id | Status | Evidence |
| --- | --- | --- |
| rev2 F1 (blocking) | fixed | flat-key capture defined once (`review.md:59`) and used at every black-fill measure: `review.md:62, :63, :65, :68`, `systems-economy.md:67` (`--mask` fallback), `documents.md:135`, `handoffs.md:258`, `SKILL.md:102`; role file `:59` asks the studio-operator for flat-key captures and says why; tool behaviour re-read (`estimate_border_key`: a lit, non-pure magenta still keys when the border is uniform, so the default works if lighting is even; the remaining gap is shadows, R1 above) |
| rev2 R1 | fixed | `principles.md:73` states what `visible_ms` measures and the two clip conditions, matching `clip_metrics.py:78-100`; `documents.md:96` points to it; role file `:59` asks for those frames |
| rev2 R2 | fixed | `hook-promise.md:29` names `surfaces.md` for `--size` and `--bottom-band`, `--box` on the hero, `not measured` without a row; `game-concept` SKILL `:74` the same in short; matches `marketing-craft/references/image-pipeline.md:29-31` |
| rev1 F1, F2, R1-R10 | still fixed | re-checked at their lines (`systems-economy.md:71`, `spaces.md:18, :21, :51`, `principles.md:31`, `playtest-live.md:56`, `documents.md:135`, `handoffs.md:6`, `SKILL.md:30`, `growth-order.md:15`, `hook-promise.md:28-29, :31, :45-46`, role file `:18, :59`, proposals rows 30-33) |
| rev1/rev2 lead notes | open for the lead, not the maker | library GD-35 "static" wording (proposal row 31); J003 citations naming Riot or 2XKO in `hook-promise.md:14`, `preproduction` SKILL `:36`, `systems-economy.md:16`, `playtest-live.md:55`, `social.md:15, :21` (all present at df13ff4, cite the owner's J003 paper; no J018 decision on them) |

## Check results

| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | pass | 145 tagged IDs (script against `matrix.md` game column) all have a row, plus 21 untagged rows: 166 rows checked, 0 failed. All landing files read in full this round; sampled library entries (VR-21, WT-21, EX-07, RI-24, UI-10, VH-07, SD-09, WT-24) carry their design-side rule and, where checkable, a check; rows repaired in rounds 1-2 re-opened. 4 rejections (EX-05, SD-16, SS-19, WT-22) keep sound reasons |
| C2 core principles | pass | `game-design` §7 (every task; `game-concept` §1, `preproduction` §1 and role file `:18` point to it): 18 rows = every UP whose list names game-designer; UP-09 and UP-12 correctly excluded with the design-side pointer; each row has its own design example and check; each matches the master's "design:" line; no contradiction (row 4 lets cheap reference images precede the grey-box verdict, which follows AGENTS.md §3 item 5 and only production art waits) |
| C3 self-review | pass (R1) | every black-fill, timing and tile check now names its input conditions and runs on the captures the role file asks for; R1 would stop shadows inflating black-fill areas |
| C4 kit rules and engine | pass (R2) | no conflict with AGENTS.md, `rules/`, J018-D2..D5; protected `rules/`, `tools/`, `templates/`, `.agents/workflows/`, `orchestration`, `level-design`, `platform-policy`, `.claude/` unchanged since df13ff4; tool flags used all exist (`silhouette --mask/--component/--compare`, `value --box`, `thumbnail --size/--size-source/--box/--bottom-band`, `icon`, `clip_metrics` `onset_ms/peak_ms/visible_ms`); engine claims match the mirror (walk speed 16, UseJumpPower default true, JumpPower 50); R2 is a stale claim in a shared skill the agent also loads |
| C5 nothing lost | pass (R3) | every removed line of the diff is kept inside a longer replacement, moved, or replaced by current names; "Removed: nothing" holds for rules; R3 is a lost pointer, not lost content |
| C6 fixed rules | pass | role frontmatter lines 1-10 identical to df13ff4; SKILL.md 115 / 79 / 82 lines; descriptions 377 / 368 / 373 characters, unchanged; no numbered section renumbered (new sections appended at the end; the role file's two new unnumbered sections inserted); J018 phrase in every changed skill file header, spaces.md and the role comment; no library IDs, transcript lines, Riot games, champions or artists in any added body line (grep of the diff: only header lines match); no tips section; `evals/` unchanged; outside the books only the job's coverage, proposals, reviews and the lead's `crew.md` changed |
| C7 better work | yes | see below |

## C7: will the agent make better work?

Read as the agent at the start of eval brief 5 (lobby review: "new players don't find the shop") and brief 1 (pitch three games). For brief 5 the new books add what the old ones lacked for this exact failure: the first view after spawn must frame the goal, one orientation convention across maps ("the shop always right of spawn"), routes timed in seconds with something to see on the way, every check judged on a phone-size capture at the game camera, and fixes ranked by cause before signs and arrows (G-15); the agent states its parameters as assumptions instead of stopping (SKILL.md:30). For brief 1 the pitch work now has a labelled warm-up round, a hook source per candidate with one from outside games and one big swing, equal finish, a goal question, and a first-image tile check that reports `not measured` rather than inventing a tile size. In craft-output reviews the agent has a check list per recipe slot and now asks for the right captures (flat-key, still-framed clips, two-client only where needed), so its numbers mean what the books say. Against df13ff4 this is clearly better work. Remaining weak spots: shadows can still distort the black-fill numbers until R1 is written down; the agent meets two jump-height answers in a stage review until `level-design` is fixed through a proposal (R2); the preloaded start is about 72 KB vs 41.5 KB before (about +7.5 k tokens, accepted in rev2), and the feedback rule is still restated in several places, so the agent reads the same rule more than once.

## Notes for the lead (not findings against the maker)
- Library GD-35 "static ... behind Details" still contradicts the Roblox MUST rule (proposal row 31); later makers will copy it until the master is fixed.
- The J003 citations naming Riot or 2XKO in book bodies (listed above) need the lead's call on whether the C6 wording covers pre-J018 sourced text.
- Could not check: whether a backdrop Part keys flat under a real place's lighting and how large the shadow error is (needs the studio-mcp probe the maker proposed); whether Studio MCP can produce 30 fps frame folders with 0 ms on the press (existing practice in the effect recipe).
