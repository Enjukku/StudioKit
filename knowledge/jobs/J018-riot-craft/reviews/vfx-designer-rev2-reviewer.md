---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer vfx-designer · claude-opus-5-5 · high · 2026-10-22

# Review: vfx-designer books, rebuild round 2 (J018 stage 3)

```text
<spec>
artifact: .agents/roles/vfx-designer.md (body) + .agents/skills/vfx-design/ (SKILL.md, references/) + .agents/skills/vfx-craft/ (SKILL.md, references/); working tree on top of df13ff4 after repair round 1, 2026-10-22
reviewer: J018 reviewer vfx-designer (opus, high)
looked_at_first: [
  role file body and frontmatter (md5 of lines 1-10 equal to df13ff4); vfx-design SKILL.md, read-card.md, review.md (all of §A-§I) read in full; vfx-craft SKILL.md, measure.md read in full; git diff df13ff4 (ignore CR at EOL) of plan-and-spec, pro-defaults, techniques, camera-and-screen, effect-card-and-presets, elements, moment-recipes, scene-and-clutter; removed lines of both SKILL.md walked again; flipbooks-and-kitbash, roblox-vfx, juice-repetition-sync: status-only (no content diff),
  knowledge/reference/craft/riot/universal-principles.md (all 20 'effect:' lines and general checks), matrix.md vfx column (214 IDs, script-extracted), principle/apply/check/roblox_fit lines of all 214 tagged findings (extracted to scratch; VR-01..VR-26, WT-11/12/13/21, VC-07, CF-03, GD-23 read line by line),
  partner books: film-craft/references/blender-previs.md §7 flash count (:77-100), animation-design/references/game-timing.md §4-§6, sound-design SKILL.md S-133, platform-policy/references/rules.md §A,
  tools: clip_metrics.py source, look_check.py contrast and silhouette --help, tool-modes.md; docs mirror: ParticleEmitter.yaml TimeScale (:962-968), Model.yaml ScaleTo (:730-740), effects/highlighting.md:37, effects/particle-emitters.md:212,
  earlier review rev1 (every finding re-checked), stage2-brief-v2.md, job-card.md fixed list, eval brief 1
  ]   # the maker's coverage and proposals files were read after this
v3_runs (scratchpad rev2/, my own synthetic 1280x720 JPEG folders at 30 fps (and one at 60 fps): sky gradient, noisy ground, a character block, frames f###_<ms>ms.jpg; the §6 script extracted byte-for-byte from measure.md; the film director's script extracted from blender-previs.md §7 with its glob changed to *.jpg):
  - S1 slam (build 1000-1100 ms, 1-frame white contact flash at 1100, eased ring, tail): clip_metrics runs; brightest bright_pct rows 1100/1133 = the marker (BL-03 right); mask one-liner, cover one-liner (character box 321 px where the ring is drawn over the body, HUD box 0), look_check value/thumb/silhouette --keep-holes/palette --roles, contrast --min-ratio 3 --tolerance-source: all run and write the files measure.md names
  - S2 busiest scene (three 1-frame flashes over 55 % of the screen at 500/900/1300 ms + a zone pulsing at 2 Hz): §6 onsets 3, most in 1 s 3 (right); film script 3 (right)
  - S3 three flashes in 1 s, each ramping over 2 frames: §6 counts 6; film script 3
  - S5 two eased full-screen grade pulses 500 ms apart (design-legal, 2 per second): §6 counts 6 at 30 fps and 10 at 60 fps; film script 2 and 2
  - S6 zone pulsing at 2 Hz: alone 2.0 Hz (right); same zone with one large flash crossing the box: 2.29 Hz, no error
  - S7 bursts after a flash: a ring with the books' own fixed curve (grow from 38 % with a key at t 0.25 at 0.72 of max): coverage reading of BL-04 FAIL (first 70 % row 667 ms, quarter by 566 ms); box-width reading 567 ms (pass at frame resolution)
  - S8 a 6.5 %-of-screen pure-white flash 3 times a second: §6 0 onsets, film script 0, clip_metrics bright_pct 6.5 on those rows
  - S4 footprint: base ring vs a moved copy vs a 15 % larger copy: compare.iou 1.0 and 0.88; keys area_frac, compare.alignment.bbox_a_px (= the variant) and bbox_b_px (= the base) exist as measure.md §3 says; moved copy's boxes 280 px apart (footprint FAIL, right)
  - curve one-liner on content/vfx/curves.json: values equal measure.md §5
findings:
  - {id: F1, class: blocking, check: C8 V3 + V10 + V6, C3 (IG-07),
     where: ".agents/skills/vfx-craft/references/measure.md:90 (onset = per-pixel rise from the frame before), :101 ('the same as the film director's count'; 'A flash under 10 % of the screen is not a large flash: BL-03 and VS-02 judge it'); .agents/skills/vfx-design/references/review.md:288 (IG-07)",
     expected: "The composite flash count gives the right count for the flashes our own effects make (a 1-frame flash, an eased flash, a tweened grade pulse) at any capture rate, and agrees with the partner book whose thresholds it says it shares (film-craft/references/blender-previs.md §7: a flash counts once per net rise and re-arms only after a net fall, so 'an eased flash counts once and the same footage gives the same count at 30 and 60 fps'). Flashes the count leaves out are judged by a named line",
     observed: "(a) The §6 script counts every frame whose pixels rose 0.1 from the frame before, so a flash that rises over 2-3 frames is counted 2-3 times and the count changes with the capture rate. A T4 grade pulse that the books allow (camera-and-screen.md, read-card.md §2 T4) fails IG-07 on its own. (b) The thresholds are the film director's, the algorithm is not: the two books give different counts for the same frames. (c) A flash between about 3 % and 10 % of the screen is not counted, and BL-03 and VS-02 judge where and when near-white sits, not its rate; review.md §H:195 says this file follows X-44 (about 2.8 % of the screen) and RV-T06:80 caps 0.006 sr in any 10° field, so a flash the book itself calls large passes IG-07 at 3 per second with no error",
     evidence: "my runs: S5 two eased grade pulses (2 per second, design-legal): §6 6 at 30 fps, 10 at 60 fps, film script 2 and 2; S3 three 2-frame ramps: §6 6, film 3; S2 1-frame flashes: both 3 (right); S8 a 6.5 % white flash at 3 Hz: §6 0, clip_metrics bright_pct 6.505 on those rows. The film director's maker filed the same request against this file after the repair round (proposals/film-director.md:26), not yet answered in the coverage V11 block",
     smallest_fix: "measure.md §6: replace the onset loop with the net trough/peak test (and the nine-block regions) of film-craft/references/blender-previs.md §7, or point to that script with its glob set to f*_*ms.jpg; keep the box pulse-rate part. Then re-run the tests in table d and record S5-type eased flashes. measure.md:101 and IG-07: 'a flash between about 3 % and 10 % of the screen is not counted: count those from the spec (each near-white or post-effect pulse's rate and screen area) and from the bright_pct rows (rows with bright_pct ≥ about 3 %, PROPOSAL, per rolling second)'. Answer proposals/film-director.md:26 in the V11 block"}
  - {id: F2, class: blocking, check: C8 V3 + C3 (BL-04 fails correct work; S and M halves disagree),
     where: ".agents/skills/vfx-design/references/review.md:232 (BL-04 'the first row at ≥ about 70 % of that segment's own peak'); .agents/skills/vfx-craft/references/measure.md:29 (BL-04 row, coverage_pct); against vfx-craft/references/pro-defaults.md:16 (ring row: 'grow from 38% with a key at about t 0.25 at ≥0.7 of max'), measure.md:73 (§5 size test) and vfx-craft SKILL.md:65 (C-21)",
     expected: "The clip reading of 'fast in' measures the same thing as the rule it checks: the library and the books state it on size (about 70-80 % of the size in the first 20-25 %); a burst built from the books' own passing curve passes the clip reading too",
     observed: "coverage_pct is screen area. For a ring, disc or shockwave the area grows with the square of the size, so '70 % of the peak coverage in the first quarter' asks for about 84 % of the size, not 70 %. A ring built exactly to the pro-defaults fix (0.72 of max at t 0.25) passes SP-02 and §5 and fails the M half of BL-04, with no error; the agent then gets two verdicts on one line and is pushed to over-fast curves the books do not ask for",
     evidence: "my run S7_ring38_key (keys 0.38 / 0.72 at t 0.25 / 1.0, ground ring): segment 433-967 ms, first row at 70 % of peak coverage 667 ms, quarter by 566 ms -> FAIL; the same rows by box width (x1-x0, a linear size): 567 ms (pass at frame resolution). S7_disc_075 (0.75 at t 0.25): coverage FAIL (667 vs 566). Library WT-11 apply: '70-80 % of max size within the first 20-25 %'; check: 'sample size per frame'",
     smallest_fix: "measure.md:29 and review.md BL-04: read a linear size, not the area: 'the row box width (x1 − x0) for a shape that grows from its centre, or the square root of coverage_pct; the first row at ≥ 70 % of the segment's peak width falls in its first quarter' (coverage ≥ about 50 % of its peak is the same test). Re-run the maker's clip A and clip F and record the numbers"}
  - {id: R1, class: recommendation, check: C2 (a core-principle check points to the wrong line),
     where: ".agents/skills/vfx-design/SKILL.md:125 (§9 #9 check 'debris spec has acceleration and drag (CP-15)'); knowledge/jobs/J018-riot-craft/coverage/vfx-designer.md:268 (UP-09 row 'BL-04, CP-15')",
     expected: "The line id names the self-review line that carries the check",
     observed: "CP-15 is 'detail indicated, clumped at the focus; flow lines' (review.md:274). Acceleration, drag and arcs are BL-12 (review.md:240) and C-31",
     evidence: "review.md:240, :274",
     smallest_fix: "§9 #9 check: '(BL-12)'; the coverage UP-09 row the same"}
  - {id: R2, class: recommendation, check: C8 V3 (a known trap built into the capture request),
     where: ".agents/skills/vfx-craft/references/measure.md:11 (busiest-scene folder 'Used by IG-07, IG-08'); review.md:289 (IG-08 confirm with the §6 box reading)",
     expected: "The pulse rate is confirmed on frames where the box holds only the pulsing layer (measure.md:102 already says a box that holds another moving thing mixes the rates)",
     observed: "The busiest scene is the folder most likely to put other effects and large flashes inside the pulse box",
     evidence: "my run S6: a 2 Hz zone alone 2.0 Hz; the same zone with one large flash through the box 2.29 Hz, no error; S2 (three flashes through the box) 'n/a (fewer than 2 rises)' for a folder with 5 cycles",
     smallest_fix: "measure.md:11 'Used by IG-07'; IG-08 confirm on the effect's own folder (dark test place) or a stretch of the busiest folder with no other change in the box"}
  - {id: R3, class: recommendation, check: C3 (two lines name a reading the tool does not output),
     where: "review.md:247 (VS-02 'near-white only at the focus ... (`bright_pct` rows and box)'); review.md:234 (BL-06 'the centre of the changed (or near-white) pixels moves')",
     expected: "Each reading names an output that exists",
     observed: "clip_metrics' box and centre cover every changed pixel; there is no box or centre of the near-white pixels (clip_metrics.py:66-72)",
     evidence: "clip_metrics.py:66-74",
     smallest_fix: "VS-02: '(bright_pct rows say when; the zoomed still's luminance image says where)'; BL-06: drop '(or near-white)' or say 'on the key stills'"}
  - {id: R4, class: recommendation, check: C8 V10 (event names),
     where: ".agents/skills/vfx-design/references/read-card.md:40 (worked card timing 'windup_start 0.00 s')",
     expected: "The worked card uses the animator's event names (game-timing.md:36: tell start, anticipation complete, active start, contact candidate, active end ...)",
     observed: "'windup_start' is not on the animator's list; the same card uses the animator's contact_candidate and contact_confirmed correctly",
     evidence: "animation-design/references/game-timing.md:36, :42",
     smallest_fix: "'tell_start 0.00 s'"}
  - {id: R5, class: recommendation, check: C8 V11 (stale records),
     where: "knowledge/jobs/J018-riot-craft/proposals/vfx-designer.md (sound-design S-133 row); coverage/vfx-designer.md:13 (SKILL.md lines 134), V11 block row numbers",
     expected: "Proposal rows still ask for something not done; record numbers match the files",
     observed: "sound-design SKILL.md:107 S-133 now states 'the first lit contact frame or up to about 40 ms after it, never more than one frame before' (the wave-2 sound maker aligned it): the row's 'today −35 to +100 ms' is stale. vfx-design SKILL.md is 136 lines, not 134; the cited partner rows moved (environment row 37 is now :40, film 31 is :32, game-designer 13 is :29)",
     evidence: "sound-design/SKILL.md:107; wc -l; grep of proposals/*.md",
     smallest_fix: "mark the S-133 row 'done by the sound-designer maker (J018 wave 2)'; update the line count and row numbers"}
keep: [
  every rev1 finding fixed and checked: F1 traps listed in §2 and the count moved off the clip rows, F2 shape vs footprint split with the right JSON keys (verified), F3 cover test on effect masks (verified), F4 one T2 near-white rule across read card, BL-03, SP-04 and C-07, F5 contrast with --min-ratio and our tolerance source (verified), F6 C-27 matches Model.yaml:739; R1-R7 all done,
  the read card with its loudness tiers and two worked cards, and the short route for T1-T2 effects and fixes,
  the build order: blocking with placeholder sprites -> check-in -> grey and black-fill gates -> colour -> polish -> in-game, with decisions frozen after the check-in,
  review.md §I: self-review lines per pass with their input codes, the image budget under J005-D8 and the fresh-read protocol,
  measure.md: tested commands with an honest list of wrong numbers with no error, today's capture route, and the footprint method,
  craft rows C-17 to C-31 and the spec lines SP-01 to SP-13,
  the partner table in the role file (what to ask whom, and when),
  §9 core principles: all 20, each with its own example and a runnable check
  ]
verdict: fix-first
</spec>
```

## Check results

| Check | Result | Note |
| --- | --- | --- |
| C1 coverage | pass (214 rows checked, 0 failed) | 214 / 214 tagged IDs have a row (script diff against matrix.md, none missing or extra); every landing file read in full or by diff; kept anchors (JU-07, JU-25..27, SC-17, SC-18, SC-61, EL-10, EL-18, EL-19, FB-10, FB-26, T-11, moment-recipes §C6, §C7) exist; rejections sound; CF-03 now lands on CP-13 and C-29 |
| C2 core principles | pass, one wrong line id (R1) | §9 covers UP-01..UP-20 with own example and check; no contradiction with the master (the UP-03 "never blow out to white" wording has a proposal row) |
| C3 self-review | fail | lines exist for every checkable finding with inputs named; IG-07 over-counts eased flashes and misses 3-10 % flashes (F1); BL-04 clip reading fails correct work (F2); two readings name outputs the tool lacks (R3) |
| C4 kit rules and engine | pass | TimeScale, Model:ScaleTo, Highlight 255 and Rate 400/100 match the docs mirror; no tool mode invented (contrast --min-ratio, silhouette --compare/--compare-mask, shortlist --out checked against --help); V4 paid-random lines agree with platform-policy §A |
| C5 nothing valuable lost | pass | removed lines of both SKILL.md files walked again; each kept, sharpened or moved (the "under ~10 studs" particle rule sits in techniques.md:20) |
| C6 fixed rules | pass | only vfx books and the two job files changed for this role (three references status-only); frontmatter identical; SKILL.md 136 and 113 lines; descriptions 377 and 353 characters; no section renumbered (craft §3 and §5 retitled, same numbers; §9 appended); J018 phrase in every changed header and the role comment; no Riot, games, champions or library IDs in the bodies; no tips section; evals/ unchanged |
| C7 better work | yes, with two measuring faults | see below |
| C8 brief v2 | fail on V3 and V10 (F1, F2) | V1 inputs and budgets named; V2 real modes only; V4 agrees; V6 one pointer line for the toolbox; V7 steps and self-checks inside the first ~18 KB (vfx-design §6 at 17.3 KB, vfx-craft §5 at 13.8 KB; §1 says to re-read §9); V8 n/a (craft role); V11 all wave-2 rows answered except the later film-director row 26 (F1) |

**C7 judgement (eval brief 1, the heavy rocket hit, read as the agent would).** With the old books the agent restated the brief, wrote a layer plan and asked for one capture. With these books it fills a read card (verb, three read lines, tier with caps, truth from config, information areas, stop criteria), weighs 2-3 options with one atypical, blocks the hit with placeholder sprites on the real timing, and proves build, peak, tail, footprint and cover with clip numbers and masked stills before any texture. It then passes grey and black-fill gates, checks colour against roles and runs a named in-game pass with reduced modes and a flash count. Each stage catches a known failure of the old route (polish on a weak read, a flash off the contact frame, white blowout from stacked additive layers, dust over players, a skin that changes the read), and the repair round made the earlier wrong readings honest. The agent will make clearly better work. What is still weak: two readings give wrong verdicts with no error. The flash count over-counts eased flashes and tweened grade pulses and does not see 3-10 % flashes, against the film director's count for the same frames (F1). The fast-in clip reading measures area where the rule is size, so it fails the books' own fixed ring curve (F2). Each fix is a few lines in measure.md and review.md; no rebuild is needed.
