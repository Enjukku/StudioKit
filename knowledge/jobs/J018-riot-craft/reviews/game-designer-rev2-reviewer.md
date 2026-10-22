---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer game-designer · claude-opus-5-5 · high · 2026-10-22

# Review: game-designer books, rebuild round 2 (J018 stage 3, after repair round 1)

```text
<spec>
artifact: .agents/roles/game-designer.md (body) + .agents/skills/game-concept/ (SKILL.md, references/) + .agents/skills/preproduction/ (SKILL.md, references/) + .agents/skills/game-design/ (SKILL.md, references/ incl. new spaces.md), working tree on top of df13ff4, 2026-10-22 (after repair round 1)
reviewer: J018 reviewer game-designer (opus, high)
looked_at_first: [
  all 16 changed book files and the new spaces.md read in full (role file, 3 SKILL.md, 13 references), then git diff df13ff4 (every removed line walked),
  knowledge/reference/craft/riot/universal-principles.md (UP-01..UP-20, the "applies to" lists and each "design:" medium line),
  knowledge/reference/craft/riot/matrix.md (game column: 145 IDs, script-extracted) and the principle, apply and check of CF-13, CR-06, GD-19, GD-35, LC-01, RI-24, UI-10, VR-21, WL-20,
  tools run, not only --help: look_check.py silhouette on a busy-background test image in the scratchpad (result: verdict invalid-mask), thumb_check.py thumbnail on the same image (sheet written), clip_metrics.py source (FRAME_RE, summarise(): median background, visible = cov >= max(0.2 %, 0.1 x peak)),
  look_check.py silhouette / value --help, thumb_check.py thumbnail / icon --help,
  studio-mcp SKILL.md C-06 and C-13, marketing-craft references/image-pipeline.md:25-30 (tile size, --box), modeling-craft references/blender-recipes.md:66 (flat key for the black-fill),
  roblox-creator-docs StarterPlayer.yaml:274-339, GuiService.yaml:262,
  game-concept/evals/briefs.md briefs 1-5 (hidden key not opened),
  reviews/game-designer-rev1-reviewer.md (every earlier finding re-checked)
  ]   # the coverage and proposals files were read after the books
findings:
  - {id: F1, class: blocking, check: C3 + C4,
     where: "every black-fill measurement the repair added: .agents/skills/game-design/references/review.md:62, :63, :65 (character slot); systems-economy.md:67 (variant footprint band); .agents/skills/preproduction/references/documents.md:135 (role-card check); handoffs.md:258 (example brief C2); .agents/skills/game-design/SKILL.md:102 (core principle 5 check); and what the agent asks for: .agents/roles/game-designer.md:59 (studio-operator row)",
     expected: "A self-review line the agent can run with our tools on the input it asks for. `look_check.py silhouette` finds the subject only from a --mask, an alpha channel or a flat key-colour border (auto key needs >= 90 % of border pixels within --key-tol; look_check.py:341-362); the modeler's books carry this convention (modeling-craft/references/blender-recipes.md:66: flat grey or magenta #FF00FF background, or --mask)",
     observed: "The books run `look_check.py silhouette <capture>` (area, bbox, --component N, --compare IoU) on 'game-camera' play captures, and the role file asks the studio-operator only for play captures, lineups and busiest-moment captures. A Studio play capture has a scene behind the subject, so the tool returns no mask: no area, no IoU, and the written black-fill image is empty. The variant 10 % footprint band (systems-economy.md:67), the lineup size rank (review.md:63, SKILL.md:102) and the nearest-neighbour IoU flag (review.md:65, documents.md:135) cannot be measured as written; the agent will spend a capture round, get 'invalid-mask', and fall back to judging by eye",
     evidence: "scratchpad test: look_check.py silhouette busy.png -> \"verdict\": \"invalid-mask\", \"invalid_reason\": \"no subject mask found (no --mask, no alpha, no flat key-colour border)\"; look_check.py:368-376 mask_problem(); the same image through thumb_check.py thumbnail writes its sheet, so only the silhouette checks are affected",
     smallest_fix: "(1) Role file :59, studio-operator row, add: 'black-fill captures for lineups, variants and look-alikes: same game-camera angle and distance, against a flat key colour (a plain backdrop Part or a magenta #FF00FF sky), one subject per capture or units apart for --component'. (2) At the first use in each file (review.md §7 character intro line :62, systems-economy.md:67, documents.md:135, handoffs.md:258) add 'on a flat-key capture (or with --mask)'; SKILL.md:102 needs no change once review.md says it"}
  - {id: R1, class: recommendation, check: C3 (check fidelity),
     where: ".agents/skills/game-design/references/principles.md:73 (feedback checks) and .agents/skills/preproduction/references/documents.md:96 (feedback-stack Checks field)",
     expected: "The timing numbers mean what the books say they mean: `visible_ms` = how long the celebration layer stays, `onset_ms` = press to first change",
     observed: "clip_metrics.py takes the per-pixel median of all frames as the background and counts any pixel that differs by > 40 per channel (clip_metrics.py:51-57, 78-93). If the celebration fills more than half the frames, the median contains it and the layer partly vanishes from the mask; if the character idles, the HUD counts up or anything else moves, that change counts too and `visible_ms` stretches toward the whole clip. The books already note the 10 %-of-peak onset rule but not these two input conditions",
     evidence: "clip_metrics.py source lines cited; the books' wording 'visible_ms = how long the layer stays' (principles.md:73)",
     smallest_fix: "principles.md:73 after 'fixed-camera frame folder': '; still frames before and after the event make up more than half the clip, and nothing else moves (idle off, HUD outside the frame or masked), because the tool's background is the median frame and every other change counts'. documents.md:96 points to it"}
  - {id: R2, class: recommendation, check: C3 (first-image tile check),
     where: ".agents/skills/game-concept/references/hook-promise.md:29 (§3 item 7) and game-concept/SKILL.md:74 (self-check 'thumbnail with a measured --size')",
     expected: "The marketing books' rule for the same tool: the phone tile size has no Roblox doc and is measured once into `knowledge/design/marketing/surfaces.md`; a full-scene image needs `--box` around the hero and its action, otherwise the subject fields say 'not measured' (marketing-craft/references/image-pipeline.md:29-30)",
     observed: "The designer's books ask for 'a measured --size' and say the sheet shows 'the subject mask', but name neither where the measured size lives nor --box. A concept key art is a full scene: without --box the one-subject read is not measured, and without surfaces.md the agent invents a tile size or skips the check",
     evidence: "thumb_check.py thumbnail --help (--size required, --size-source, --box); scratchpad run on a full-scene image wrote the sheet with no subject",
     smallest_fix: "hook-promise.md:29: '... --size <WxH from knowledge/design/marketing/surfaces.md, or `not measured`> ... --box <hero and its action>' and one clause 'without --box the subject is not measured'"}
keep: [
  every keep item of rev1 still holds (review.md §7 per-recipe check lists; playtest-live.md §1b and the could-not-check list; documents.md §6-§9 contracts; spaces.md; handoffs.md §2 needs and examples §3.6-§3.7; the game-concept warm-up, hook sources, big swing, goal questions, closed doors; the four parts with an empty "decisions" line as a finding; G-17..G-23 and the §7 rows; WL-30 handled under the no-totals rule; PROPOSAL labels; honest coverage and proposals),
  repair round 1 itself: F1 odds wording now matches the Roblox MUST rules in both places (systems-economy.md:71, review.md:89 UI line); the eight F2 checks added as short clauses on the existing check lines, not as new sections,
  one source per number: documents.md §6-§7 point to principles.md §7-§8 instead of copying values; handoffs.md:247 names systems-economy §8 as the footprint's one source,
  `TBD (step N)` in the shared brief header (handoffs.md:6): a step-1 brief no longer invents a read rank or timing stages,
  the jump-height fix (spaces.md:18): measured in the place, JumpPower 50 governs by default, no wrong 7.2-stud rule,
  the two-client cost stated once per use with the Unproven fallback (role file :59, principles.md §9, review.md §7, handoffs.md:219),
  clip_metrics.py named with its real file pattern `f###_<ms>ms.jpg` and its onset caveat, and the tool bug sent as a proposal instead of being worked around silently,
  the growth order now gates feature specs on the loop's dated grey-box verdict (growth-order.md step 6), matching core principle 4
  ]
verdict: fix-first
</spec>
```

## Earlier findings (rev1): status

| Rev1 id | Status | Evidence |
| --- | --- | --- |
| F1 (blocking) | fixed | `systems-economy.md:71` (visible before the buy button, sum 100 %, never covered or animated, updated while a boost is active or after a once-only win, long list behind a worded label, never a bare icon); check line `:77` adds the boost capture; `review.md` §7 UI line says the same. Library GD-35 still says "static" (`game-design-fun.md`, GD-35 apply): proposal row filed for the lead |
| F2 (blocking) | fixed | CF-13, WL-22, WL-23: `spaces.md` §7 check; WL-09, WL-10: `spaces.md` §3 check; GD-08: `principles.md` §3 check; GD-19: `playtest-live.md` §4; CD-17: `documents.md` §8 check. Each is a runnable capture, count or document check |
| R1 | addressed (size growth remains) | role file :18 "after a compaction, re-read `game-design` §7"; §7 cells shortened; §7 now starts at character 15,715 of 22,263. Preloaded start (role file + 3 SKILL.md) is 71.6 KB vs 41.5 KB at df13ff4 (about +7.5 k tokens); accepted as the price of the new contracts, not re-raised |
| R2 | fixed | `documents.md:89, 92, 93, 104` point to `principles.md` §7-§8; SKILL §7 row 8 has no number; the example briefs keep written values with their source comment, which `rules/messages.md` §2 requires |
| R3 | fixed | `handoffs.md:6` `TBD (step N)` |
| R4 | fixed | `game-design/SKILL.md:30` "or without assumed values written down as assumptions" |
| R5 | fixed | `growth-order.md:15` (step 6 settles the dated verdict before step 7; a FAIL sends the loop back), `:31`; SKILL.md:101 |
| R6 | fixed, but see F1 and R1 above | tools named in every place rev1 listed; their input conditions are missing |
| R7 | fixed | `spaces.md:1` header and `:18`; StarterPlayer.yaml:334-339 (UseJumpPower defaults to true) |
| R8 | fixed | role file :59; `principles.md:89`; `review.md:59, :93`; `handoffs.md:219` |
| R9 | fixed | `proposals/game-designer.md` recipe row (character recipe, plain-block behaviour capture before the modeler) |
| R10 | fixed | `hook-promise.md` §3 old item 6 back at 6, tile test appended as 7; §4 header "(12 items, O)"; HC11-HC12 appended; no outside reference to the numbers (grep) |

## Check results

| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | pass | 145 tagged IDs (script against `matrix.md` game column) all have a row; 21 untagged rows also checked: 166 rows checked, 0 failed. Every "landed in" location opened (all book files read in full); each carries the rule and, where checkable, a check. 4 rejections (EX-05, SD-16, SS-19, WT-22) keep sound reasons (craft execution owned by animator, sound, art, marketing; the design side is named) |
| C2 core principles | pass | `game-design` §7 (preloaded every task; `game-concept` §1, `preproduction` §1 and the role file point to it): 18 rows = every UP whose "applies to" lists game-designer; UP-09 and UP-12 correctly excluded (their lists omit game-designer) with the design-side pointer. Each row has its own design example and check; each matches the master's "design:" medium line; no contradiction found |
| C3 self-review | fail (F1) | the black-fill checks cannot run on the captures the agent asks for; R1, R2 sharpen two tool-based checks. All other checks are runnable on studio-operator captures, `thumb_check.py`, `clip_metrics.py`, `sim.py`, Python on coordinates, or a fresh-context reader |
| C4 kit rules and engine | pass (F1 is a tool-input gap, counted under C3) | no conflict with AGENTS.md, `rules/`, J018-D2/D3/D4; protected `rules/`, `tools/`, `templates/`, `.agents/workflows/jobs/`, `orchestration`, `level-design`, `platform-policy` unchanged (git status); tool modes used all exist (`silhouette --component/--compare`, `value`, `thumbnail --size/--size-source`, `icon` 150x150 default, `clip_metrics` `onset_ms/peak_ms/visible_ms`); engine claims (walk speed 16, JumpPower default, PolicyService checks, MCP single-player limit) match the mirror and `studio-mcp` C-06 |
| C5 nothing lost | pass | every removed line in `git diff df13ff4` is kept inside a longer replacement, moved (role file "planned role" line to the partners table) or replaced by current names (art and marketing skills); matches the coverage table's "old book changes"; "Removed: nothing" is accurate |
| C6 fixed rules | pass | role frontmatter lines 1-10 identical to df13ff4; SKILL.md 115 / 79 / 82 lines; descriptions 377 / 368 / 373 characters, unchanged; no `##`/`###` section renumbered (only titles extended); J018 phrase in every changed skill file header and the role comment; no tips section; no library IDs, transcript lines, Riot games, champions or artists in any added line (grep of the diff); `evals/` unchanged. Outside the books only the job files and the lead's `crew.md` changed |
| C7 better work | yes, with the F1 gap and the size cost | see below |

## C7: will the agent make better work?

Read as the agent at the start of eval brief 3 ("Fly or Die": pre-production step 1, brief the art director and the architect) and brief 4 (click, multiplier, rebirth: "boring after an hour"). For brief 3 the new books make the agent write the parameters and target experience into the vision record first, show 2-3 rough options with a pick and a goal question, and send briefs with the full shared header where step-3 and step-4 items say `TBD (step N)` instead of invented values; the art-director brief now carries the read rank need, colour roles and role cards the old five-item header lacked. For brief 4 the review names the four parts, finds the empty "decisions" line, labels every input by what it can prove and ends with a could-not-check list, which the old books did not ask for. Pitches gain the warm-up round, a distinct hook source per candidate, one outside-games source, one big swing and equal finish: aimed straight at the old books' reskin problem. In craft-output reviews the agent now has a check list per recipe slot. So yes: better work than with the df13ff4 books. Weak spots: (1) the numeric black-fill checks fail on in-scene captures until F1 is fixed, so variant footprint, lineup size rank and look-alike checks fall back to eye judgement; (2) the clip timing numbers can mislead on a clip with other motion (R1); (3) the start is about 7.5 k tokens heavier and the feedback rule is still restated in several places, so the agent pays for reading the same rule more than once.

## Notes for the lead (not findings against the maker)
- Library GD-35 (`knowledge/reference/craft/riot/game-design-fun.md`, apply line) still says the odds panel is "static ... behind a worded Details control"; J018-D2 point 2 says later fixes go to the master first. The maker's proposal row has the replacement wording; later makers (vfx, ui, progression, live-ops) will copy the wrong line until it is applied.
- J003 citations naming Riot or a Riot game remain in book bodies (`hook-promise.md:14`, `systems-economy.md:16`, `preproduction` P-02, `playtest-live.md:55`). They cite the owner's J003 research paper, not the J018 transcripts; no decision on them exists in the J018 folder. The lead decides.
- Coverage record nit: its header lists `ReducedMotionEnabled` among engine facts used; the books say "reduced motion" but never name the property (GuiService.yaml:262 confirms it exists). No change needed in the books.
- Could not check: whether the studio-operator can produce 30 fps frame folders with 0 ms on the press through Studio MCP (the effect recipe already asks for frame sets named for `clip_metrics.py`, `job-effect.js:375`, so it is existing practice); the lowest-graphics capture stays a proposal to `studio-mcp`.
