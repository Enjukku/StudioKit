---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer art-director · claude-opus-5-5 · high · 2026-10-22

# J018 stage 3 review: art-director books, round 2

Scope: `.agents/roles/art-director.md` (body), `.agents/skills/art-direction/` (SKILL.md, references), `.agents/skills/art-review/` (SKILL.md, references; not evals), working tree on 2026-10-22, against df13ff4 and against round 1 (`reviews/art-director-rev1-reviewer.md`). I read all 14 book files in full before the coverage table. Then I read the full diff against df13ff4 (every removed line), `universal-principles.md` (the master), the topic-file lines of the findings I opened, `matrix.md`, `coverage/art-director.md`, `proposals/art-director.md`, the other roles' proposal rows against these books, `stage2-brief-v2.md`, `tool-modes.md`, the orchestration recipes and the partner role files. I ran every command line and tool mode the books name on synthetic inputs in my scratchpad (`ad-rev2/`, script `make_samples_adrev2.py`). I changed nothing in the repo except this file.

```text
<spec>
artifact: .agents/roles/art-director.md (body) + .agents/skills/art-direction/** + .agents/skills/art-review/** (not evals) @ working tree 2026-10-22 (after repair round 1)
reviewer: J018 reviewer art-director (opus, high), round 2
looked_at_first: [all 14 book files in full (role body; art-direction SKILL, clarity-cohesion, identity-variants, worked-examples, platform-evolution-marketing, precedents unchanged; art-review SKILL, self-review, look-check, exploration, art-bible, feedback-briefs); git diff df13ff4 of every changed file; look_check.py source (value_stats, exclusion_mask, run_value --min-ratio, thumb sheet) and -h; thumb_check.py icon/thumbnail -h; synthetic inputs: a 1600x720 in-scene frame (sky, noisy ground 70-90, a hero with a bright upper body and lower body either the ground's colour or dark) with its magenta mask capture; an environment-only cut; the same with a 30x30 pure-black patch (PNG and JPEG); an effects-off cut with 10 characters and a white HUD bar; a busy frame with a 200x100 white sign, a 10x10 accent and three 91 px reserved-red patches; a clean busy frame with 5 white HUD icons and a 60x60 sun disk; an environment-only cut with a high-contrast far band and its layer cut; an environment-only cut with saturated decoration above head height and the same with 12 saturated avatars in the player band; a frame with a red HUD health bar and a red enemy; a 512 magenta icon; a 1920x1080 thumbnail with a hero mask]
findings:
  - id: F1
    class: blocking
    where: "art-review/references/self-review.md:72 (RD9 input 'cuts'), :102 (CL1 input 'busy and cuts'), :110 (CL9); look-check.md:89 (K20 '§5 lines 4-5 on the busiest and layer-cut captures'), :115 (§5 line 4 input 'the busiest or a layer-cut capture'), :120-124 (§5 line 5, no input named, no layer trap listed); art-direction/SKILL.md:107 (§7 P3 check 'layer bands measured on layer-cut captures')"
    expected: "Round 1 F2 fixed for every measure that asks about the environment layer: a measure of the environment (its contrast by depth, its decoration's reserved-hue share, its player-band saturation, its band) runs on the environment-only capture or with the other layers excluded, as look-check.md:26 now says ('Layer cuts ... cannot prove a layer's own band: other layers are still in the frame')."
    observed: "The repair moved RD3, K19 and §5 line 8 to the environment-only capture, but four other environment measures still read composed or single-cut captures, and the §7 core principle P3 (re-read after every compaction) still tells the agent to measure layer bands on layer cuts. Characters, effects and the HUD then change the number with no error: RD9 passes a scene where distance does not lower contrast, CL9 fails a correct calm player band because avatars stand in it, CL1 fails decoration that has no reserved hue because the HUD's health bar is red."
    evidence: "RD9 (value --box per depth band): environment-only cut with a busy far band: far p5-p95 spread 0.502, near 0.041 → fail (right); its effects-off cut with characters and a HUD bar in the near rows: near spread 0.931 → pass (wrong, no error). CL9 (§5 line 5): environment-only cut: above 46.9, player band 7.0 → pass (right); the same with 12 saturated avatars in the player band: player 59.5 → fail (wrong, no error). CL1 (§5 line 4, enemy excluded as the gameplay object): environment-only 0 px; the same frame with a red HUD health bar: share 0.0094 (10 800 px) → fail (wrong, no error). Library checks: WL-25 'near and far bands', LC-18 'saturation in the player band lower than above it', LC-01 'outside gameplay objects' are all about the environment."
    smallest_fix: "RD9, CL9 and the decoration half of CL1: input = the environment-only capture (CL1 may keep the busiest capture with a black-fill of characters, effects and HUD as `<exclude>`). K20: name the same inputs. §5 lines 4 and 5: add 'a frame that still holds characters, effects or the HUD' to 'wrong with no error'. P3 check: 'layer bands measured on the environment-only capture and mask captures (look-check.md §1)'. Re-read WE §2 step 2 (CL1 2.8 %) against the new input."
  - id: F2
    class: blocking
    where: "art-review/references/self-review.md:68 (RD5 input 'the busiest capture's whole frame for clipped white'; pass 'clipped share outside the accents ≤ 0.0005'); look-check.md:131 (§5 line 9 input), :135 (its 'wrong with no error' list names sky only for the environment box); art-direction/references/worked-examples.md:22 ('on the busiest capture the fountain spray holds 1.9 % clipped white')"
    expected: "RD5 asks whether pure white sits only on the named accents (VC-07: 'on the peak frame or the hero view'), and the books give the extremes to UI and VFX (AD C-19, CC §2 item 4). So the clipped count leaves out the HUD and the sky and fails only on world or effect whites outside the accents."
    observed: "The busiest capture has the HUD on by definition (EV4), and a Roblox sky often holds a clipped sun. Both count as 'clipped outside the accents', so RD5 fails almost every clean frame and the worked example teaches the same input. The marked image shows red on the HUD, so a careful agent can see it, but the pass column says fail and the brief that follows goes to the environment or VFX designer."
    evidence: "Clean busy frame (no clipped world surface), 5 white HUD icons 40x40 and a 60x60 sun disk, the 10x10 accent excluded: clipped share 0.0101 (11 600 px), 20 times the 0.0005 pass value → fail. The effects-off cut with a white HUD bar gives p95 1.0 on line 8 for the same reason (look-check.md:53 already records it)."
    smallest_fix: "RD5 and §5 line 9 (clipped half): input = the UI-off layer cut (effects and characters stay on, since effects must not blow out either), the box below the horizon or `<exclude>` = sky + named accents; add 'HUD or sky in the frame' to line 9's 'wrong with no error'. WE §2 step 2: say the 1.9 % was read on the UI-off cut with the sky excluded."
  - id: F3
    class: recommendation
    where: "art-review/references/art-bible.md:63-80 (§7 has no separation row); self-review.md:69 (RD6 'about 3:1'), :76 (RD13 '≥ 1.5'); proposals/environment-designer.md:36"
    expected: "V11: every proposal row other roles wrote against these books is adopted or declined with a reason."
    observed: "The environment designer's row 36 (a 'Separation targets' row in the bible's §7: character vs environment ring 1.5:1, critical marker vs floor 3:1, the player-band neutral-chroma limit and flat-fill limits, or a pointer to whoever sets them) is not in the coverage file's V11 list. It was written at 05:37, after the coverage file (05:36), so the maker could not see it. Today the two ratios live as starting values in self-review lines and in the environment books (V6: the bible is meant to be the one place)."
    evidence: "File times; coverage §d 'V11, repair round 1' list; `environment-design/references/light-and-air.md:45` VB-a (1.5:1 and 3:1)."
    smallest_fix: "Add a 'Separation targets' row to art-bible.md §7 (character 1.5, marker 3:1, both PROPOSAL; the player-band chroma limit: environment designer proposes, owner decides); RD6 and RD13 point to it; record the adoption in the coverage file."
  - id: F4
    class: recommendation
    where: "art-review/references/self-review.md:76 (RD13 pass 'upper p50 > lower p50')"
    expected: "The same quality bar as the modeler's VL2 (`modeling-design/references/review.md:113`: lower body 15-20 % lower in grey-view value, a luminance ratio of about 0.6-0.7, PROPOSAL) and the library's VC-08 default; the coverage says the lower-body rule 'keeps the modeler's VL2 unit'."
    observed: "Any difference passes (upper 0.401 vs lower 0.400). The art director's review is weaker than the maker's own self-check, so a model the modeler should send back can pass the art director's check-in."
    evidence: "Lines cited; VC-08 apply line ('lower-body mean value 15-20 % below upper body [inference]')."
    smallest_fix: "RD13 pass: 'lower p50 ÷ upper p50 about 0.6-0.7 or lower (starting value, PROPOSAL; the modeler's VL2, the bible's value wins)'."
  - id: F5
    class: recommendation
    where: "art-review/references/self-review.md:190 (MK2 `thumb_check.py thumbnail --size <tile> --bottom-band 20`); look-check.md:46 (§2 row)"
    expected: "V2/V3: each tool mode named with the flags it needs."
    observed: "`thumb_check.py thumbnail --size` refuses to run without `--size-source` ('--size needs --size-source (where the small size comes from)'): a safe error, but the line as written does not run. The marketing book's line has the flag (`marketing-craft/references/image-pipeline.md:32`)."
    evidence: "Run on a 1920x1080 thumbnail with a hero mask: error without the flag; with `--size-source \"measured tile\"` it measures (subject share in the 20 % band 0.06)."
    smallest_fix: "MK2 and LK §2: add `--size-source \"<capture id, device>\"`."
  - id: F6
    class: recommendation
    where: "art-review/references/exploration.md:30 (§3 item 5 packet); partner ask: `.agents/roles/game-designer.md:51` ('2-3 style directions as reference images answering the 6 concept-art questions'); `preproduction/SKILL.md:37` P-03"
    expected: "V10: the hand-off the rebuilt game-designer book asks for is what the art director's packet delivers."
    observed: "The packet lists shape, value, colour roles, material, light, hierarchy, appeal and risks; three of the six questions (scale, character relationships, the signature moment) are not asked, and the books never name the list, so the game designer's ask cannot be checked."
    evidence: "P-03: 'silhouette and role, scale, readability in the real camera, key materials, character relationships, the signature moment'."
    smallest_fix: "Exploration §3 item 5: 'and answers the six concept-art questions of `preproduction` P-03 (silhouette and role, scale, readability at the game camera, key materials, character relationships, the signature moment)'; DR5 checks it."
  - id: F7
    class: recommendation
    where: "art-review/references/exploration.md:79 (§8 'at most 9 ... max 2 regenerations each'); art-direction/SKILL.md:41"
    expected: "V1: one image budget per round that cannot be read two ways."
    observed: "Read literally, a round may make 9 roughs plus 18 regenerations (27 images). The worked example counts the regeneration inside the cap (8 + 1 = 9), which is the right reading, but the table does not say so."
    evidence: "Lines cited; WE §1 steps 4 and 9."
    smallest_fix: "§8 row: 'at most 9 images per round including regenerations (max 2 per image)'; the same words in AD §3 step 4."
  - id: F8
    class: recommendation
    where: "art-direction/SKILL.md:60 (C-07 '2-5 identity anchors'), references/identity-variants.md:32 ('2-5'), art-review/references/art-bible.md:77 ('2-5'), self-review.md:85 (SH2 '2-4 identifying elements'), clarity-cohesion.md:45 ('2-4 elements'); recipe `orchestration/references/job-types.md:38` ('2-3 identity anchors')"
    expected: "V6: one count, one place; agreement with the character recipe's G1 deliverable."
    observed: "Three counts for nearly the same thing (2-3 in the recipe, 2-4 for identifying elements, 2-5 for anchors). Not a conflict (2-3 sits inside 2-5), but a maker reading SH2 and the bible gets two numbers."
    evidence: "grep of the cited lines."
    smallest_fix: "Keep the count only in art-bible.md §7 Identity anchors (say 'G1 shows 2-3, the bible may hold up to 5'); SH2, C-07, IV §3 and CC §3 point to it."
  - id: F9
    class: recommendation
    where: "art-review/references/exploration.md:3 ('Checks: DR1-DR9'), feedback-briefs.md:3 ('Checks: FB1-FB7'); feedback-briefs.md:112 (§5 example check C2 'the slam core stays the brightest warm region in the frame (look_check palette, role \"danger\")')"
    expected: "Header pointers name the lines that exist; an example brief's check names a measure that can answer it."
    observed: "DR10-DR11 and FB8 exist but the headers stop short. `palette` reports cluster shares and ΔE to role swatches, not where the brightest region is (this C2 line is unchanged from df13ff4, but the example is what makers copy)."
    evidence: "look_check.py palette_stats source; the headers."
    smallest_fix: "Headers: DR1-DR11, FB1-FB8. C2: 'the slam core's p95 is the highest warm region (look_check value --compare-subjects with the core and the other warm regions as named boxes from the mask capture)'."
keep: [Every round-1 finding except the spread of F2 is fixed and checked: RD13 now runs only on the in-scene capture with the upper body excluded and a real starting value (my run: legs the ground's colour 1.04 fail, dark legs 2.29 pass; a flat render is ruled out); the environment-only capture kind with its 'cannot prove' column; §5 line 9 (900 px black patch found while p5 stayed 0.069; the JPEG trap named); the paint-over budget in R-16, FBK §6 and FB2; the owner sheet shows only options that passed the grey pass, matching the recipe's 2-3; R-02 vision limits, R-03 and R-05 needs-decision clauses and WO8 completeness restored; the compaction line names §5-§7; no studio name outside precedents.md; icon rounding removed and PEM §3 points to marketing-design M-15..M-23 and marketing-craft K-14; the one-sun scope in CC §4 and the bible; the job-type table at the top of self-review §3; the contrast command form. Kept from round 1: the direction stages (research board, hooks with the warm-up, 3-4 equal-finish roughs with one radical, grey and black-fill pass before colour, cheap proof in the engine), the bible §7 standards every craft measures against, the partner ask table (now with what the art director gives first), the cold read before the hand-back and the fixed big-to-small order, look-check §2 mask rules (the symmetric-ratio and ring notes are new and right), the three worked examples, identity-variants.md, core principles P1-P20 without P8 and P19.]
verdict: fix-first
</spec>
```

## Check results

| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | fail (4 rows) | 287 rows: all 277 tagged findings present (script against `matrix.md`), 10 untagged, 22 rejections each with a sound owner or duplicate reason. Opened in depth this round: 44 landed rows (every row round 1 flagged or the repair touched, plus 24 drawn at random) and the 22 rejections = 66. The content is there for all of them; 4 rows land on a check that gives a wrong number on its stated input: WL-25 (RD9), LC-18 (CL9), LC-01 (CL1), all F1; VC-07 (RD5, F2). Partial but acceptable as in round 1: WL-13, CD-23, CD-09. |
| C2 core principles | pass with one wrong line | `art-direction` §7 covers UP-01..07, 09..18, 20 with an example and a check each; UP-08 and UP-19 correctly not the art director's (the master's applies-to lists agree). No contradiction with the master. One check line inside the section is wrong: P3 still sends layer bands to layer cuts (F1). |
| C3 self-review | fail (F1, F2) | Every line names its input; the job-type table maps every recipe to K rows and lines. RD9, CL1, CL9 and RD5 give wrong answers on their named inputs (F1, F2); RD13's upper-vs-lower half has no starting value (F4). |
| C4 kit rules and engine | pass | No conflict with AGENTS.md, rules or the job card's decisions; the role file's review order matches every recipe in `job-types.md`; recipe and workflow changes are proposal rows only. Engine: one sun per place, post effects global under Lighting and per player under the Camera, badge and pass circles, thumbnail bottom band (`production/publishing/thumbnails.md:215` via thumb_check) all hold. No invented tool mode; one missing required flag (F5). |
| C5 nothing valuable lost | pass | Every removed line in the diff walked. Studio names moved to precedents.md; "View every image" replaced by the light-check rule; R-02, R-03, R-05 and R-11 restored. Small, acceptable losses: "stop exploring when new images test no real uncertainty" (P18 and the round budget cover it), environment test "traversal" in EXP §6 item 5, R-13 "with and without sound" (the agent hears nothing; cue cards and Output cue times replace it). |
| C6 fixed rules | pass | Only the role body, the two skills and the two job files are this maker's (other modified files belong to other makers and the lead); frontmatter byte-identical to df13ff4; SKILL.md 137 and 86 lines; descriptions 389 and 383 characters; LF in every file; no section renumbered (list items inside sections only; no outside reference broken: the only external pointers are to `art-bible.md` §7 and PEM §3); the J018 header phrase in every changed file and the role comment; no library IDs, transcript lines, Riot names or "tips" section in bodies; evals and precedents.md unchanged. |
| C7 better work | yes, after F1-F2 | See below. |
| C8 brief v2 | fail (V3: F1, F2) | V1 inputs named; direction-round and paint-over budgets stated (regeneration wording, F7). V2 real modes only. V3: all 9 §5 lines and every named mode ran and wrote their files; the wrong-with-no-error cases are F1 and F2; MK2 stops on a missing flag (F5). V4 paid random tiers defer to `platform-policy` (no conflict). V6 band numbers and the ΔE now in one place; anchor counts still spread (F8). V7: §5 at 17.0 KB, §6 at 18.3-19.5 KB, §7 after; line 21 names §5-§7 and art-review §6 for re-reading. V8 findings became the bible's §7 sheet, the partner ask table, K19-K25 and the self-review. V10: consistent with the modeler (units, key-tol 4, region masks; F4 is the gap), the environment designer (environment-only input, near-black 0.004, 1.5 and 3:1 ratios), the animator, VFX, UI, film, sound, marketing and rigger role files' asks; the game designer's "6 concept-art questions" are not answered (F6). V11: every row adopted with a reason except the environment designer's late row 36 (F3). |

## Commands run (C8 V3)

| Line or mode | Input | Runs | Files written | Right answer | Wrong number with no error when |
| --- | --- | --- | --- | --- | --- |
| `silhouette` | magenta mask capture | yes | `.silhouette.png`, JSON | yes | — |
| §5 line 1 region masks + RD13 `value --mask lower --exclude upper --min-ratio 1.5` | in-scene frame + mask capture | yes | `lower/upper.mask.png`, JSON with verdict | yes: ground-coloured legs 1.04 fail, dark legs 2.29 pass; 320 upper px excluded | masks 12 px off still gave the right verdict here; a moving pose between the two captures could break it (same frame is implied, not said) |
| §5 line 2 squint + `contrast --sample` pairs | busy frame with a bright objective | yes | `.squint.png`, JSON | yes: objective 5.45, hero 4.85 (rank order kept) | a box crossing an edge (the book says so) |
| §5 line 3 mirror | busy frame | yes (Windows path inside the Python string) | `.mirror.png` | yes | — |
| §5 line 4 reserved share | busy frame; frame with a red HUD bar | yes | `.reserved.png` | 273 px = 3 x 91 exact; HUD frame 0.0094 | HUD or characters in the frame (F1) |
| §5 line 5 chroma bands | environment-only vs avatars in the player band | yes | stdout JSON | environment-only yes | avatars in the player band: 7.0 → 59.5 (F1) |
| §5 line 6 contact sheet | 3 images | yes | `sheet.png` 2400x720 | yes | — |
| §5 line 7 `thumb --mask --size 800x360` | in-scene frame + mask | yes | thumb, sheet with nearest x4 panel, JSON | scale 0.5 | — |
| §5 line 8 `value --box` environment band | environment-only; effects-off cut | yes | JSON | 0.069-0.108 on environment-only | the cut gives p95 1.0 (the book now says so) |
| §5 line 9 near-black / clipped | env-only with a black patch (PNG, JPEG); busy with sign and accent; clean busy with HUD icons and sun | yes | `.extremes.png`, stdout JSON | black patch 900 px; sign 0.017 with the accent excluded | HUD and sky counted as clipped: 0.0101 on a clean frame (F2) |
| RD9 `value --box` per depth band | env-only with a busy far band; its layer cut | yes | JSON | env-only: far 0.50 > near 0.04 → fail (right) | layer cut: near 0.93 → pass (F1) |
| `contrast` documented form | busy frame | yes; the generic form errors safely | JSON | yes | — |
| `thumb_check.py icon --key FF00FF` | 512 magenta icon | yes | sheet, JSON | measured | — |
| `thumb_check.py thumbnail --size --bottom-band 20 --mask` (MK2 as written) | 1920x1080 + hero mask | error: needs `--size-source` | — | with the flag: subject share in band 0.06 | — (F5, safe error) |

## Round-1 findings

| Round 1 | Status now | Evidence |
| --- | --- | --- |
| F1 RD13 cannot fail | fixed | SR:76, LK:108; my runs 1.04 fail / 2.29 pass |
| F2 environment band on contaminated cuts | fixed for RD3, K19, line 8, WE §2 band; **not carried** to RD9, CL1, CL9, RD5 and P3 | F1, F2 above |
| F3 pure black and clipped not measured | fixed (line 9, RD3, RD5) | runs above; RD5 input is F2 |
| F4 paint-over budget | fixed | R-16, FBK §6, FB2, WE §2 |
| F5 option count vs recipe | fixed | AD step 6, EXP §3 item 6, §8, DR5, WE §1 |
| F6 band numbers in 4 places | fixed | only BIB §7 (WE keeps its own game's example) |
| F7 R-02, needs-decision clauses, completeness | fixed | R-02, R-03, R-05, R-11, WO8, K25 |
| F8 compaction line | fixed | AD:21 |
| F9 studio name in PEM | fixed | PEM:54 → precedents.md §4 (the case is there) |
| F10 icon rounding; PEM restated marketing | fixed | CC:108, CP1, PEM:56 |
| F11 one-sun scope | fixed | CC:66, BIB:71, C-21 |
| F12 job-type map | fixed | SR §3 table |
| F13 contrast form | fixed | LK:38 |

## Better work (C7)

I read the books as the agent would for eval E2 (cross-craft review of a busy scene: quiet, busiest, lowest-quality and phone captures, a manifest with a missing field, a VFX spec and clip list without clips) and E1 (2-3 directions, max 9 images). For E1 the new books are clearly better than df13ff4: a success test before images, a research board, hooks with the warm-up set aside, equal-finish roughs inside a stated budget, a grey and black-fill pass before colour, an owner sheet of the 2-3 that passed with a goal question, and a bible whose §7 gives every craft measurable bands, reserved colours, key light and shape code. For E2 the agent now writes a cold read first, picks its lines from the Stage row, asks for the environment-only and mask captures it lacks and marks the rest NOT REVIEWED, measures with tested commands that each list their traps, ranks one problem per note and sends marked captures instead of eight generated paint-overs. That is better work. Where it would still go wrong: with the busiest capture and a layer cut in hand (exactly E2's inputs), RD5 flags the HUD and sky as clipped white, CL1 flags the HUD's red as decoration, CL9 flags avatars as a busy player band, and RD9 passes depth contrast because characters sit in the near band (F1, F2); each would become a wrong brief to the environment or VFX designer. Smaller weak spots: the art director's upper-vs-lower body bar is weaker than the modeler's own (F4); the game designer's six concept-art questions are not in the direction packet (F6); sample boxes on generated roughs are still placed by eye (the book warns, but has no aid); and the 213-line self-review is long, though the job-type table now keeps a review to its row.
