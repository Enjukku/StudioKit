---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer game-designer · claude-opus-5-5 · high · 2026-10-22

# Review: game-designer books, rebuild round 1 (J018 stage 3)

```text
<spec>
artifact: .agents/roles/game-designer.md (body) + .agents/skills/game-concept/ (SKILL.md, references/) + .agents/skills/preproduction/ (SKILL.md, references/) + .agents/skills/game-design/ (SKILL.md, references/, new spaces.md), working tree on top of df13ff4, 2026-10-22
reviewer: J018 reviewer game-designer (opus, high)
looked_at_first: [
  all 16 changed book files and the new spaces.md read in full, then git diff df13ff4 (removed lines walked one by one),
  knowledge/reference/craft/riot/universal-principles.md (master, UP-01..UP-20),
  knowledge/reference/craft/riot/matrix.md (game column: 145 findings, script-extracted),
  principle + check of every tagged finding in the topic files,
  platform-policy/references/rules.md §A, roblox-creator-docs StarterPlayer.yaml / Humanoid.yaml / Workspace.yaml / GuiService.yaml,
  tools/art/thumb_check.py, look_check.py, tools/progression/sim.py, tools/vfx/clip_metrics.py (--help / source),
  orchestration/references/job-types.md, studio-mcp SKILL.md, J017 startup-cost.md and prompt-audit.md,
  game-concept/evals/briefs.md (briefs 1, 3, 4, 5; hidden keys not opened)
  ]   # the maker's coverage and proposals files were read after this
findings:
  - {id: F1, class: blocking, check: C4,
     where: ".agents/skills/game-design/references/systems-economy.md:71 (§9 Honest paid random reveals)",
     expected: "Roblox rule (platform-policy/references/rules.md §A, rows 3-5, from paid-random-items.md:53-59,75): odds for every outcome shown before purchase; a LONG list MAY sit in a pop-up behind a visible worded 'Info'/'Details' label (a bare icon is not enough); the shown odds MUST update for that player while a luck modifier is active and when a once-only outcome is won",
     observed: "'Odds for every outcome are shown before purchase, static, never covered by effects, behind a worded \"Details\" control'. 'static' contradicts the MUST-update rule and the same file's §6 table (line 34: 'odds update while a boost is active'); 'behind a Details control' reads as the default for every odds list, which Roblox allows only for long lists. An agent writing a reveal spec from §9 would specify a non-compliant odds panel",
     evidence: "systems-economy.md:34 vs :71; platform-policy/references/rules.md lines 12-15; the wording comes from library GD-35 'apply' (game-design-fun.md:470), so later makers will copy it too",
     smallest_fix: "Rewrite line 71: 'Odds for every outcome are visible before the buy button and sum to 100 %; effects never cover or animate them; they update for the player while a boost is active or after a once-only outcome is won; a long list may open in a pop-up from a visible worded \"Info\" or \"Details\" label, never a bare icon.' The lead puts the same wording into library GD-35 (game-design-fun.md:470) so the master stays the source"}
  - {id: F2, class: blocking, check: C1 + C3,
     where: "8 coverage rows whose finding landed as a rule without its check: CF-13 (spaces.md:49 rule; :51 check has no surprise item), WL-09 and WL-10 (spaces.md:20 rule; :21 check has no forward-path or entry-count item), WL-22 and WL-23 (spaces.md:47, :50 rules; :51 check has no story-fact or identity-symbol item), GD-08 (principles.md:29 rule; :31 check has no theme-family item), GD-19 (playtest-live.md:56 rule; no check), CD-17 (documents.md:129 rule; :135 check has no item)",
     expected: "Owner spec: 'Turn every checkable finding into a line in the role's self-review'; C1: the landing carries the rule and, where checkable, the check. Each of these 8 library findings has a runnable check (capture, count or document check)",
     observed: "The rule is present and correct; the check is not. The coverage table is honest about it (these rows say 'standard', not 'self-review check'), so the gap is in the books, not in the record",
     evidence: "library checks: CF-13 'grayscale capture: the surprise sits in a low-contrast area while the light is the top focus'; WL-09 'walk-through capture never turns the camera back'; WL-10 'count entries per team'; WL-22 'a fresh agent states at least one intended story fact'; WL-23 'identity prop visible from its entry at the game camera'; GD-08 'each item in a set belongs to a named theme family'; GD-19 'a balance pass list covering every unit exists for the new mode'; CD-17 'count parts and moving pieces of hero vs common items'",
     smallest_fix: "Append clauses to the existing check lines (about 6 short lines in total): spaces.md §3 check (:21) '+ a walk capture from spawn to each objective never turns the camera back; ways in counted per side per objective (default two)'; spaces.md §7 check (:51) '+ in the grayscale capture each planned surprise sits outside the top focus and testers do not spot it early; a fresh reader states at least one story fact per main area; each zone's identity symbol is visible from its entry at the game camera on a phone'; principles.md §3 check (:31) '+ every item in a set names its theme family (shared motif and palette)'; playtest-live.md §4 (:56) '+ check: the mode change ships with a balance-pass list covering every unit'; documents.md §8 check (:135) '+ the hero signature item has clearly more parts and moving pieces than common items of its class'"}
  - {id: R1, class: recommendation, check: C7 (size, compaction),
     where: ".agents/skills/game-design/SKILL.md §7 (lines 93-115); role file :18 ('Every task: game-design §7')",
     expected: "rules/assistants/claude.md Compaction row: an invoked skill keeps its first 5,000 tokens; 'Steps and rules sit at the top of SKILL.md'. Owner: 'better work, not longer books'. J017 cut this role's start by 6.9 k tokens (prompt-audit.md:118)",
     observed: "game-design SKILL.md is 24,987 bytes (about 6.2 k tokens); §7 starts at character 16,060 (about 4 k tokens in), so most of the core-principle rows sit past the 5 k cut after a compaction. Preloaded books grew from 29.0 KB to 55.4 KB plus the role file from 12.4 KB to 18.5 KB: about +8 k tokens at every start, more than J017 saved. Steps, rules and §6 are inside the first 5 k, so the binding parts survive",
     evidence: "wc -c and offset measured; git show df13ff4 sizes; J017 startup-cost.md table (game-designer 15.4 k preloaded before J017)",
     smallest_fix: "Role file Read first item 2: add 'after a compaction, re-read game-design §7'. Then shorten the §7 example and check cells to one short phrase each where they repeat G-17..G-23, §6 and the references (rows 1, 3, 7, 8, 19, 20 restate principles.md §7-§10 almost word for word)"}
  - {id: R2, class: recommendation, check: C7 (duplication, drift),
     where: "PROPOSAL numbers written in two or three places: reaction windows 0.6 s / 1.0 s / 0.23 s (principles.md:76, documents.md:104); pending state 100 ms (principles.md:65, documents.md:89); celebration under 2 s (principles.md:69, documents.md:92, SKILL.md:105); merge window 100 ms (principles.md:70, documents.md:93); variant footprint 10 % (systems-economy.md:67, handoffs.md:247)",
     expected: "One source per number (P-06 in the same books; AGENTS.md §2 content is data)",
     observed: "Each value is restated; the feedback rule as a whole is restated in G-19, §6, §7 row 19, principles.md §7, documents.md §6, loops.md §6 item 4, review.md §7 and the role file. A later test that changes one value will leave the copies stale",
     evidence: "grep of the five values across the three skills",
     smallest_fix: "Keep the values in principles.md §7-§9 and systems-economy.md §8 only; the documents.md templates and SKILL §7 example say 'PROPOSAL default: principles.md §7' instead of repeating the number"}
  - {id: R3, class: recommendation, check: C7 (eval brief 3),
     where: ".agents/skills/preproduction/references/handoffs.md:7 (shared header 'every brief')",
     expected: "A step-1 brief carries only what step 1 has settled (growth-order.md:22 item 6: finish only as far as the next step needs)",
     observed: "The header demands the read rank and the named timing stages in every brief; growth-order writes the read rank at step 3 and timed stages at step 4 (growth-order.md:28-29). Eval brief 3 (step 1 briefs to the art director and the architect) pushes the agent to invent them or leave the header incomplete",
     evidence: "handoffs.md:7; growth-order.md:27-29; game-concept/evals/briefs.md brief 3",
     smallest_fix: "Add to handoffs.md §1: 'An item a later growth step settles is written `TBD (step N)`, never invented.'"}
  - {id: R4, class: recommendation, check: C7 (eval briefs 4, 5),
     where: ".agents/skills/game-design/SKILL.md:30 step 1 ('no review starts without them'); review.md:6",
     expected: "Role file :35 'Missing fact that changes the result: state an assumption and continue'",
     observed: "Eval briefs 4 and 5 give no camera, device or player count; the hard wording can make the agent stop and ask instead of reviewing",
     evidence: "SKILL.md:30 vs game-designer.md:35; game-concept/evals/briefs.md briefs 4-5",
     smallest_fix: "SKILL.md:30: '... no review starts without them, or without assumed values written down as assumptions.'"}
  - {id: R5, class: recommendation, check: C7 (order),
     where: "SKILL.md:101 (§7 row 4 check 'no system spec before the loop passes') vs preproduction/references/growth-order.md:15-16",
     expected: "The growth order gates step 7 (features) on the core loop's grey-box verdict, as the core principle's check says",
     observed: "Step 6 settles only 'grey-box test plan'; step 7 writes feature specs with no verdict gate; only production art waits for the verdict (growth-order.md:31). The check and the steps disagree",
     evidence: "lines cited",
     smallest_fix: "growth-order.md step 6 'Settles': add 'the loop's dated grey-box verdict before step 7 specs features'; or change the row 4 check to 'no production art brief before the loop verdict'"}
  - {id: R6, class: recommendation, check: C3 (runnable with our tools),
     where: "black-fill and footprint checks (systems-economy.md:67, review.md:62-65, documents.md:135, SKILL.md:102); timing checks (principles.md:73, documents.md:96, review.md:80)",
     expected: "Checks name the kit tool that runs them where one exists",
     observed: "`tools/art/look_check.py silhouette` gives mask area, bbox and IoU with `--compare` (black-fill role read, nearest look-alike, the 10 % variant band); `tools/vfx/clip_metrics.py` gives onset, peak and visible duration from a `f###_<ms>.jpg` capture folder (press-to-first-change, celebration length). The books describe these checks by eye or as 'a short Python diff'",
     evidence: "look_check.py silhouette --help; clip_metrics.py docstring",
     smallest_fix: "Name `look_check.py silhouette --compare` in the four black-fill checks and `clip_metrics.py` in the two timing checks"}
  - {id: R7, class: recommendation, check: C4 (engine),
     where: ".agents/skills/game-design/references/spaces.md:18 ('jump height (default 7.2 studs)') and header line 1",
     expected: "The default that governs a new character's jump",
     observed: "StarterPlayer.CharacterJumpHeight defaults to 7.2, but CharacterUseJumpPower defaults to true (StarterPlayer.yaml:329-339), so JumpPower 50 governs; at Gravity 196.2 (Workspace.yaml:465) that is a rise of about 50²/(2 x 196.2) = 6.4 studs by plain physics (not verified in Studio). A 7-stud ledge planned as climbable may not be",
     evidence: "docs mirror lines cited; Humanoid.yaml:608-660",
     smallest_fix: "spaces.md:18: 'the game's jump height from the game profile, measured in the place (7.2 studs applies when UseJumpPower is false; with the JumpPower default measure it)'"}
  - {id: R8, class: recommendation, check: C3 (feasibility),
     where: "role file :59 (studio-operator: two-client captures for 'every verdict you sign'); principles.md:89; review.md:59, :93; handoffs.md:219",
     expected: "studio-mcp SKILL.md:37 (C-06): MCP starts a single-player test; multi-client local servers need the owner's click",
     observed: "The books ask for two-client captures routinely without saying they cost an owner action",
     evidence: "studio-mcp SKILL.md:37",
     smallest_fix: "Role file :59: ask for two-client captures only for effects and threats with per-viewer variants, batched in one request, noting the owner starts the local server; without one, the per-viewer check is Unproven"}
  - {id: R9, class: recommendation, check: C4 (recipe proposal missing),
     where: "loops.md:49 (plain-block test before art for each new enemy); SKILL.md G-05; preproduction SKILL.md:28, :63 (no production art brief for a mechanic before its grey-box verdict)",
     expected: "Where a book rule needs a recipe step that does not exist, a proposal (J018-D2 point 4)",
     observed: "The character recipe (orchestration/references/job-types.md:34-49) goes from G1 directions to a blockout and proxy rig with no behaviour test; for a new enemy the designer must either block the job or skip its own rule. proposals/game-designer.md adds a lineup capture to the character G2 but not a plain-block step",
     evidence: "job-types.md:42; proposals/game-designer.md row 3",
     smallest_fix: "Add a recipe row to proposals/game-designer.md: character recipe, direction stage, for a new enemy or creature with gameplay behaviour: a plain-block behaviour capture (studio-operator) judged by the game-designer before the modeler starts"}
  - {id: R10, class: recommendation, check: C6 (nit),
     where: ".agents/skills/game-concept/references/hook-promise.md:28-31",
     expected: "Kit rule (AGENTS.md §4): add or append, never renumber; counts in headers match the table",
     observed: "The new tile-size test was inserted as item 6 and the old item 6 moved to 7; the §4 header still says 'Hook check (10 items, O)' over 12 rows. No outside reference to the item number was found (grep), so nothing breaks today",
     evidence: "hook-promise.md:28-29, :31, :45-46",
     smallest_fix: "Restore the old item to 6 and append the tile-size test as item 7 or 8; header '(12 items, O)'"}
keep: [
  review.md §7: one check list per recipe review slot (character, stage, feature, UI, effect, marketing, cutscene); the old books had no way to judge another craft's output,
  playtest-live.md §1b 'what each input can prove' and the could-not-check list,
  documents.md §6-§9: feedback stack, threat and hazard sheets, role card, read rank and information list as exact contracts for the crafts,
  spaces.md: maps as the board, routes in seconds, hazards with written rules, art inside the blockout (fills a real gap),
  handoffs.md §2 'what each craft needs from me' and worked examples §3.6 (dodgeable threat) and §3.7 (variant),
  game-concept warm-up round, distinct hook sources, outside-games source, big swing, goal questions, closed doors,
  four parts one line each with an empty 'decisions' line as a finding,
  G-17..G-23 and the §7 core-principle rows: design-side examples (lava moat edge, rebirth stages, sell flow) and checks, 9 and 12 correctly marked as not applying,
  WL-30 handled well: fixed checks and re-rate every check, the 0-2 total rejected under the kit's no-totals rule,
  PROPOSAL labels on every inference number; engine defaults taken from the docs mirror,
  honest coverage table (rows that landed only as a standard say so) and a proposals file with reasons and evidence
  ]
verdict: fix-first
</spec>
```

## Check results

| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | fail (F2) | 145 tagged rows + 21 untagged rows = 166 checked; every tagged ID has a row (script against matrix.md); 8 fail on the check part only (F2); 4 rejections (EX-05, SD-16, SS-19, WT-22) have sound reasons |
| C2 core principles | pass | `game-design` §7 (preloaded every task; `game-concept` §1 and `preproduction` §1 point to it); 18 rows = every UP whose applies-to lists game-designer; UP-09 and UP-12 correctly excluded with the design-side pointer; each row has its own design example and check; no contradiction with the master found |
| C3 self-review | fail (F2) | runnable checks on studio-operator captures, `thumb_check.py`, `look_check.py`, `sim.py` (modes verified); gaps: F2; R6 (name the tools), R8 (two-client cost) |
| C4 kit rules and engine | fail (F1) | F1 contradicts a Roblox MUST; R7 engine default; R9 missing recipe proposal; no invented tool modes (`thumb_check.py thumbnail --size/--size-source`, `icon` 150x150, `look_check.py value`, `sim.py --skill --seed --runs` all exist); protected `rules/`, `.agents/workflows/jobs/`, `tools/`, `templates/` unchanged |
| C5 nothing lost | pass | every removed line in the diff is kept inside a longer replacement or replaced by current names (art-director, marketing skills); the coverage table's 'old book changes' matches the diff |
| C6 fixed rules | pass (nit R10) | role frontmatter lines 1-10 byte-identical to df13ff4 (md5); SKILL.md 115 / 79 / 82 lines; descriptions 377 / 368 / 373 characters, unchanged; J018 phrase in every changed file header and the role comment; no tips section; no library IDs, transcript lines, Riot games, champions or artists in J018 text; `evals/` unchanged |
| C7 better work | yes, with weak spots | see below; R1-R5, R9 |

## C7: will the agent make better work?

Read as the agent at the start of eval brief 4 ("click, multiplier, rebirth: boring after an hour") and brief 1 (pitch three games). With the new books the economy review names the four parts and finds the empty "decisions" and "opposition" lines, not only G-04's "bigger multiplier"; it labels every input by what it can prove and closes with a could-not-check list. The pitch work gets a labelled warm-up round, a different hook source per candidate, one outside-games source and one big swing, equal finish and a goal question, which aims straight at the old books' weak spot (reskins). Specs now give the crafts exact contracts (feedback stack, threat and hazard sheets, role cards, read rank), and the designer can for the first time judge a craft's output in its recipe slots. Weak spots: the books doubled in size and repeat the same rules and numbers in up to eight places (R1, R2); the core principles sit past the compaction cut; three wording or order conflicts can stall or pad a real job (R3, R4, R5); some checks do not name the tool that already runs them (R6); the plain-block rule has no recipe slot in character jobs (R9).

## Notes for the lead (not findings)
- Old J003 research-paper citations still name Riot or a Riot game in book bodies (`hook-promise.md:14`, `preproduction` P-02 "Riot", `systems-economy.md:16`, `playtest-live.md:55` "2XKO", `social.md:15,21`). They predate J018, cite the owner's research paper (D15, D21-D23, S09), not the transcripts, and carry fact-checked evidence; removing them would lose sourced material. The lead decides whether the C6 wording ("no 'Riot' in book bodies") covers J003 text.
- Could not check: whether the studio-operator can set the lowest graphics quality through Studio MCP (asked for in role file :59 and spaces.md:51; the library asks for it too); whether frontmatter-preloaded skills are cut to 5 k tokens after compaction like invoked skills (R1 assumes the same rule).
