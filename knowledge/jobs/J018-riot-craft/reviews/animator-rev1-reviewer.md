---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer animator · claude-opus-5-5 · high · 2026-10-22

# J018 stage 3 review: animator books, round 1

Scope: `.agents/roles/animator.md` (body), `.agents/skills/animation-design/` (SKILL.md, references/), `.agents/skills/animation-craft/` (SKILL.md, references/; evals not changed), as in the working tree on 2026-10-22, against git `df13ff4`. Inputs: `knowledge/reference/craft/riot/` (README, `universal-principles.md` = master, topic files, `matrix.md`), `coverage/animator.md`, `proposals/animator.md`, `job-card.md`. Line numbers are working-tree lines.

```text
<spec>
artifact: .agents/roles/animator.md (body) + .agents/skills/animation-design/** + .agents/skills/animation-craft/** (not evals) @ working tree 2026-10-22, base df13ff4
reviewer: J018 reviewer animator (opus, high)
looked_at_first: [the 13 book files read in full before the coverage table; git show df13ff4 of every one of them and git diff df13ff4; universal-principles.md UP-01..UP-20 in full; matrix.md animator column (139 ids); tools/anim/clip_check.py --help and source; tools/art/look_check.py silhouette/thumb --help; docs mirror: characters/index.md, avatar/character-bodies/specifications.md (advanced R15), Pose.yaml, PoseEasingStyle.yaml, ParticleEmitter.yaml (TimeScale), Camera.yaml (FieldOfView vertical), production/publishing/accessibility.md (ReducedMotionEnabled); .agents/workflows/jobs/job-character.js (S7 blocking and check-ins); rules/company.md §7; rules/assistants/claude.md (Compaction)]
findings:
  - id: F1
    class: blocking
    where: "animation-design/references/game-timing.md:39 (SD-04); animation-design/SKILL.md:85 and references/worked-examples.md:78 (SD-22); coverage/animator.md:117, :120"
    expected: "C1: each landed-in location carries the finding's rule for the animator. SD-04: the motion of an ability follows its mechanic verb, the same verb VFX and sound use (a slow decelerates and spreads, a stun snaps). SD-22: a state with a timer or a breaking point gets a tell that builds as it nears its end, on the timing list so sound and VFX can key from it."
    observed: "game-timing §4 says only 'use the same stage names as VFX and sound (load, charge, release, travel, impact, tail)'; the word 'verb' is nowhere in the books, although the coverage row says '(same stage names and verb as VFX and sound)'. For SD-22 the cited SKILL §6 creatures row has nothing on state telegraphs; the worked §8 trap row is about a trap's active window, not a building tell before a break or a timer end. P-09.2 covers stress before a structure fails, but not abilities, shields, stuns or timers, and the row does not cite it."
    evidence: "grep -i 'verb|breaking point|nears its end' over the 13 book files: 0 hits. Library sound.md SD-04 apply: 'The VFX and animation of the same ability use the same verb'; SD-22 principle: 'sound also telegraphs state, like a creak of rising tension before a shield breaks'."
    smallest_fix: "game-timing.md §4, after the stage-names bullet, add one bullet: 'An ability's motion follows its mechanic verb, the same verb the VFX frame script and the sound cue card use (a slow decelerates and spreads, a stun snaps, a knock-back drives through); a state with a timer or a breaking point (a shield, a stun, a charge) gets a building tell before it ends, as a named event on the timing list.' Add one §8a or §8c line that checks it (the clip card names the verb; the end-of-state tell event exists). Correct coverage rows SD-04 and SD-22 to point there."
  - id: F2
    class: blocking
    where: "animation-design/references/principles.md:92 (P-07.5); references/body-and-species.md:19 (neck and head row); references/review.md:121 (S-15)"
    expected: "C5: the old P-07.5 rule 'gaze can lead a turn; eyes arrive first; the face does not fight posture' (df13ff4 principles.md:74) is kept or replaced by something at least as good. The new spin rule (head holds its world direction, then turns late and fast) applies to spins and fast body turns."
    observed: "'gaze can lead a turn', 'eyes arrive first' and 'face does not fight posture' are gone, and the coverage table's section c does not list the removal. The new P-07.5 sign column states without qualification 'the head's world yaw lags the chest's in a turn, then catches up fast': for an ordinary look-turn (a character turns to look at something) this is the wrong way round, since the eyes and head lead and the body follows. S-15 is qualified ('when the design asks for it'); P-07.5 is not."
    evidence: "git show df13ff4:.agents/skills/animation-design/references/principles.md line 74 vs working-tree line 92; grep 'eyes arrive|lead a turn' over the books: 0 hits. Library WT-18 is about spins ('like a dancer spotting')."
    smallest_fix: "P-07.5: restore 'in a look-turn the eyes lead, then the head, then the body; the face never fights the posture', and qualify the spin case: 'in a spin or fast body turn the head can hold its world direction, then turn late and fast'. Sign column: 'look-turns: eye and head yaw lead the chest; spins: head yaw lags, then catches up fast'. Add the same split to the body-and-species neck row and list the change in coverage section c."
  - id: F3
    class: blocking
    where: "animation-design/SKILL.md:126 (§9 #6 check), :129 (#9), :130 (#10), :38 (step 6); references/review.md:68-74 (§5 light checks), :98 (B-11), :99 (B-12), :101 (B-14); references/principles.md:108 (P-08.11); references/game-timing.md:48 (hit-stop bracket)"
    expected: "C4: no conflict with rules/company.md §7 light checks (owner J005-D8: 'numbers for every case; images only for a failing number plus a few key cases'), which the book itself restates in review.md §5 (≤ 8 key frames per action, images only on a failing number). The new plan stages the owner invited (thumbnail pass, black-fill at the game camera) need a stated image budget so they do not bring back the J005 usage problem."
    observed: "New image-producing steps and checks have no count cap and no statement of whether they count toward the ≤ 8: step 6 renders 2-3 options of each key clip's key poses plus two timing takes; §9 #6 check 'Remove each secondary channel in turn in a render'; §9 #9 and B-11 an extra unpushed take; §9 #10 and B-14 a second character's run; P-08.11 a too-low and a too-high take at the game camera; game-timing §5 a five-value hit-stop bracket at the game camera. For a set of 6 key clips with 3 key poses each, step 6 alone is about 54 black-fill renders before blocking. An agent cannot tell from the book whether these are 'checks' (capped) or 'making' (not capped)."
    evidence: "review.md:70 'Images only when a number fails, plus at most 8 key frames per action'; SKILL.md:126 check column; rules/company.md:105; owner memory 'light-checks-by-default' (J005: 'this takes way too much usage')."
    smallest_fix: "In review.md §5 add one bullet: 'Plan-stage images (key-pose options, timing takes, an unpushed take, a bracket) are making, not checks, and have their own budget: one black-fill contact sheet per key clip at phone size (all options on one image), takes and brackets judged from sample numbers first and rendered only for the pick; report their count with the check images.' Change the §9 #6 check to a number-first one: 'each secondary channel names its cause on the clip card (S-16); a channel whose cause is only \"life\" is removed; a render without it only when the read is in doubt.'"
  - id: F4
    class: recommendation
    where: "references/review.md:89 (B-02), :100 (B-13), :101 (B-14), :147 (G-15); references/principles.md:45, :67, :78, :80, :81, :83, :124; SKILL.md:130 (§9 #10), :136 (§9 #16)"
    expected: "C3: every self-review line can be run by the animator with its own tools. The animator's tools line has no Agent tool, so it cannot ask a 'fresh viewer' or a 'tester'."
    observed: "Eleven sign or check lines rest on 'a fresh viewer', 'a fresh read' or 'a tester' with no method. The master's UP-16 also asks for refreshed eyes (mirror, grayscale, another reviewer); §9 #16 drops the mirror and has no fresh-eye step."
    evidence: "roles/animator.md:7 tools line; grep 'fresh|tester' in the books (11 hits); universal-principles.md:321."
    smallest_fix: "Add one definition to review.md §8 intro: 'A fresh read = write what you read from the black-fill or capture before you open the brief, the clip name or your notes, then compare; at the check-in the reviewer repeats it blind. Mirror the frame for a second look.' Keep the existing lines."
  - id: F5
    class: recommendation
    where: "SKILL.md:38 (two timing takes); references/game-timing.md:48 (hit-stop bracket 'at the game camera'); references/review.md:10 (normal speed first), :143 (G-11 'nothing that tires'); references/principles.md:50 (P-04.1 tap-along)"
    expected: "C3/C7: a timing choice is judged by a method the agent can run. Studio MCP and Blender MCP give the agent stills only (the book says so at roblox-playback.md:62)."
    observed: "Picks between timing takes, the hit-stop bracket and 'nothing that tires' are written as if the agent watches motion at normal speed. Without a stated method the pick rests on stills or on a guess. Bracketing the hit-stop length is also outside the animator's decision right (game-timing §1: game-designer with VFX)."
    evidence: "roblox-playback.md:62 'These are stills'; game-timing.md:13 owner of hit-stop length."
    smallest_fix: "One line in review.md §1 item 5: 'You see stills: judge timing from the sample numbers (gaps between beats, spacing, B-07, S-07) and frame strips at a known rate; a pick between timing takes, and any bracket, is rendered as a playable preview for the check-in reviewer or the owner, who picks.' In game-timing §5 say that the animator supplies the freeze-frame takes; the gameplay owner and VFX run the bracket."
  - id: F6
    class: recommendation
    where: "animation-design/SKILL.md (whole file; §8 at :105, §9 at :116-140)"
    expected: "rules/assistants/claude.md:42: after compaction each skill keeps its first 5,000 tokens; steps and rules sit at the top. Owner: 'better work, not longer books'."
    observed: "SKILL.md grew from about 16 KB (about 4,000 tokens, all kept after compaction) to about 30 KB (about 7,600 tokens). §7 rules end near 5,200 tokens, so after compaction the agent loses the end of §7, all of §8 (plan self-check) and all of §9 (core principles, about 2,150 tokens). §9 repeats much of §3, the P-rows and the review lines. Its 'Where' column already points to the depth."
    evidence: "byte counts: df13ff4 15,999 B; now 30,481 B without CR; cumulative to line 93 = 19,222 chars, to line 105 = 20,794, to line 116 = 21,856."
    smallest_fix: "Make §9 shorter without renumbering: keep the principle and the check per row, cut the example to a few words or move the examples to principles.md. Shorten the §4 'Sign' column where it repeats principles.md. Target: §8 inside the first 5,000 tokens."
  - id: F7
    class: recommendation
    where: "animation-craft/SKILL.md:28 (step 4 check-in), :91 (rule 'Never spline before the blocking check-in')"
    expected: "C7: the rule works in every kind of run. The character workflow has an S7 blocking call with art and design check-ins (job-character.js:753-783), but a single-run brief (eval 5, teddy set) names no check-in reviewer."
    observed: "With no reviewer named, the hard rule leaves the agent two bad choices: stop with 'blocked' halfway, or skip the rule."
    evidence: "animation-craft/evals/briefs.md:64 (one brief: accept, idle, walk, wave, export)."
    smallest_fix: "Add to step 4: 'When the brief names no check-in reviewer, the check-in is your §8a record and the black-fills, written to the job folder before splines; say so in the hand-back.'"
  - id: F8
    class: recommendation
    where: "references/game-timing.md:42 (sync rule); references/review.md:136 (G-04); sound-design/SKILL.md:80 (S-133)"
    expected: "One sync window across the kit, or the difference stated."
    observed: "The animator's timing list now states 0 to about 40 ms late, never more than one frame early (the same as the library and vfx-design T-09). sound-design S-133 still accepts −35 to +100 ms. Until the owner rules on the maker's proposal, a sound-designer that follows its own book can fail the animator's G-04."
    evidence: "proposals/animator.md row 'sound-design SKILL.md S-133'; cross-craft.md:37."
    smallest_fix: "In game-timing §4 add 'sound-design's current window is wider; until it is aligned (proposal J018), the sound-designer's book governs the sound side and G-04 reports MEASURED'."
  - id: F9
    class: recommendation
    where: "coverage/animator.md:29 (CD-21), :117 (SD-04); animation-design/SKILL.md:44 (§4 heading); animation-craft/references/roblox-playback.md:62; craft references (AP: refs)"
    expected: "Accurate tables and headers; one way to apply 'no citations'."
    observed: "(a) The CD-21 row puts a rejection reason into the landed-in column and leaves the rejected column empty. (b) The SD-04 row says 'verb', which the book does not have (see F1). (c) The §4 heading promises 'mistakes' in principles.md, which has no mistakes column. (d) 'The phone viewport' for Studio captures is not defined; modeling-craft defines it as a capture resampled with look_check.py thumb. (e) Paper citations (AP:<line>) were removed from the design references but kept in four craft references. These are not Riot citations, so C6 holds, but the rule is applied two ways. The files also now have CRLF line endings; .gitattributes normalizes them on commit."
    evidence: "the lines cited; grep 'AP:' over craft references (14 hits)."
    smallest_fix: "Fix the two coverage rows and the §4 heading; in roblox-playback §10 add 'phone viewport = the capture resampled to the floor phone's size with look_check.py thumb --size'; choose one citation policy for paper refs and note it in the coverage table."
keep:
  - "Anticipation sized by who reacts (P-17, P-03.8, game-timing §2, B-06): enemy tells held for the designer's reaction window, the player's own moves tight. This is the biggest single gain for fair, readable combat."
  - "The new plan stages in order: who reacts and feel words with their visible change (§3.1), identity anchors and hook shapes with the side the camera sees (§3.2), a beat sheet with subtext (§3.5), 2-3 black-fill key-pose options with a recorded pick (§3.6). The role file and the craft steps follow the same order."
  - "Craft passes split into blocking (root-only preview, then key poses on shared frames, holds as copied pairs), breakdowns and offsets, spline, and polish with one named problem per pass. Each pass has its own self-review lines (review.md §8a-§8c) with inputs labelled N/K/C."
  - "blender-keying.md §8: a compute table that turns the curve lines into numbers from the same samples file. This keeps the checks light and runnable today. The clip_check `curves` proposal is the right follow-up."
  - "Attempt vs outcome and paid reveals (game-timing §4, §9; G-05, G-13): feedback follows the confirmed result; every egg result has the same windup."
  - "Every-player rules: tells read in pose with effects hidden, grayscale and reduced motion; pulses at most 3 per second (game-timing §8, C-27, G-02, G-12)."
  - "New engine facts C-22..C-27, each checked against the docs mirror: no scale in clips (Pose.CFrame), PoseEasingStyle list, clavicle and finger joints only on advanced R15, AdjustSpeed(0) hit-stop, FaceControls, GuiService.ReducedMotionEnabled. Tool modes cited (clip_check checks; look_check silhouette, thumb --size, --compare) exist."
  - "Variants keep the base (sets-and-states §1, G-08) and the freeze frame supplied by the animator (game-timing §5, roblox-playback §9)."
  - "Worked example §1 rewritten as a Roblox brawler emote that shows beat sheet, options and pick, with no outside names."
  - "§9 Core principles: all 20 UP rows present, each written for animation with an example and a check; no contradiction with universal-principles.md."
  - "proposals/animator.md: tool, template and recipe changes with reasons; G3 rows marked; nothing protected was edited."
verdict: fix-first
</spec>
```

## Checks C1-C7

| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | FAIL (2 rows) | All 139 matrix ids for animator have a row (0 missing). I opened every landed-in location of the 155 finding rows (139 tagged + 16 untagged) and the 20 UP rows: 175 checked. 2 failed: SD-04 (keyword only, no verb rule) and SD-22 (cited locations do not carry it), F1. The 3 rejections (CF-18, CF-19, RI-15) have sound reasons. CD-21 is a partial landing with its reason in the wrong column (F9). |
| C2 core principles | PASS | `animation-design/SKILL.md` §9, in the skill the agent loads first. UP-01..UP-20 each stated for animation with an example and a check. No contradiction. Small gap: UP-16 'refresh your eyes (mirror)' (F4). |
| C3 self-review | PASS with gaps | Most lines run on sample numbers (clip_check plus the blender-keying §8 compute table), on ≤ 8 key frames with look_check, or on Studio MCP captures and the Output log. Weak: 'fresh viewer' lines (F4) and timing picks judged from stills (F5). |
| C4 kit rules and engine | FAIL | Engine claims verified in the mirror; no invented tool modes; the protected files are untouched (changes are proposals). The image budget of the new stages conflicts with light checks (F3). Sync window differs from sound-design (F8, proposal filed). |
| C5 nothing valuable lost | FAIL (1) | All other old rules are kept, moved or improved (walked the diff of all 13 files against coverage §c). 'Gaze leads a look-turn / face does not fight posture' was lost, and the head-lag sign is too broad (F2). |
| C6 fixed rules | PASS | Animator changes are limited to the 13 book files and the two job files (the other modified files belong to the modeler and game-designer makers and the lead's `crew.md`). Role frontmatter is byte-identical to df13ff4 (md5 match). SKILL.md lengths 140 and 107 lines. Descriptions 399 and 387 characters (unchanged). No section renumbered (§9, review §8, game-timing §7-9, principles §10, keying §7-8 and playback §9-10 are appended). The J018 phrase is in all 12 skill files and in the role comment. No Riot, games, champions, artists, library ids or transcript lines in the bodies. No tips section. Evals unchanged. |
| C7 better work | YES, with weak spots | See the judgement below. |

## C7: will the agent make better work?

I read the books as the agent would for eval brief 4 (heavy beast pounce, 0.8 s telegraph, 0.25 s active, dodge on a phone).

**Old books.** The old books give a crouch-load "telegraph: the readable part of startup", a silhouette check and the events.

**New books.** The new books make the agent do these things:
- Write "who reacts: the player dodges". Hold a distinct crouch pose for at least 24 frames at 30 fps, and count it (B-06).
- List the hook shapes (jaw, forelegs).
- Render 2-3 black-fill crouch options at the game camera and record the pick.
- Use the same tell for every pounce (G-09).
- Put the big hit reaction only on the confirmed hit (G-05).
- State the sync rule and the freeze frame in the timing list.
- Prove the tell with VFX hidden and in grayscale (G-02).

That is a clearly better and fairer result. The same holds for the sword swing (anticipation sizing, source of power clear at contact, freeze frame) and the teddy set (feel words with a visible change, the blocking check-in, curve lines as numbers).

**Weak spots.**
- The image budget of the new stages is not stated (F3).
- The agent sees only stills but is asked to pick timing and to use a "fresh viewer" (F4, F5).
- `animation-design/SKILL.md` doubled. After compaction the agent loses its own plan self-check and core principles (F6).
- Two sound-sourced findings landed only as keywords (F1).
- One old face rule was lost (F2).

All three blocking fixes are a few lines each. None of them needs a stage to be removed.
