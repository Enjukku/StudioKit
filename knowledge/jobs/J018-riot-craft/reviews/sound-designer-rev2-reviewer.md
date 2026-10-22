---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer sound-designer · claude-opus-5-5 · high · 2026-10-22

# Review: sound-designer books, rebuild round 2 (J018 stage 3)

```text
<spec>
artifact: .agents/roles/sound-designer.md (body) + .agents/skills/sound-design/ (SKILL.md, references/ incl. craft-process.md, review.md, worked-examples.md), working tree on top of df13ff4 after repair round 1, 2026-10-22
reviewer: J018 reviewer sound-designer (opus, high)
looked_at_first: [
  role file body, SKILL.md, review.md, craft-process.md, worked-examples.md, roblox-audio.md, cue-card.md read in full; git diff df13ff4 of reward-and-juice, craft-satisfying, emotion-recipes, genre-presets, horror-and-tension, mix-and-loudness, repetition, elements, ai-generation-prompts (changed lines); script: every S-/D- id of the old SKILL.md is still defined or was a citation only,
  my round-1 review (reviews/sound-designer-rev1-reviewer.md), every finding re-checked against the files,
  roblox-creator-docs: SoundService.yaml:175-197 (DopplerScale), AudioEmitter.yaml:130-190 (Bounds, Mode), :345-370 (GetDistanceAttenuation), AudioListener.yaml:287-310, :423-460 (listener curve multiplies),
  partner books: progression-design/references/reward-tiers.md §2 (T1-T4), ui-design/references/motion.md (sync rule, Sound column, refusals, counters), environment-craft/references/handoffs.md (floor_materials, C3), templates/environment/ambience-map.md (feeling, sound: keys), studio-mcp SKILL.md C-03 (Client data model),
  tools: clip_check.py --help, shotlist.py log-diff --help and the drill fixture run (signed diff column),
  matrix.md sound column (96 IDs, script), proposals/*.md rows naming sound,
  sound-design/evals/briefs.md briefs 2 and 4 (read as the agent would)
  ]   # the maker's coverage and proposals files were read after this
findings:
  - {id: B1, class: blocking, check: C8 V3 + C3 (the paid-reveal guardrail measure),
     where: ".agents/skills/sound-design/references/review.md:131 (F-13), :75 (R-31); SKILL.md:122 (D-03 'within 1 LU, F-13'); worked-examples.md:51, :53",
     expected: "D-03: paid results differ by notes, register and tail (up to 2x), never by loudness. The measure that proves it must catch a result that hits louder, also when that result has the longer tail D-03 allows",
     observed: "F-13 is integrated loudness of each file padded to one length. Integrated loudness averages the tail blocks in (they pass the -10 LU relative gate), so a rare result whose body is 3 LU louder but which carries a longer, quieter tail reads within 1 LU of the common result. With equal sample peaks (the louder body made denser, as compression does), R-31 passes. This is the exact shape of the worked example's Legendary result (5 notes, 2x tail). The wrong number comes with no error. Note: my round-1 smallest fix proposed integrated LUFS; the maker followed it, so this hole is partly mine",
     evidence: "V3 run (scratchpad sound-rev2/trap.py, pyloudnorm, soundfile 0.14.0, numpy 2.4.6): common result 3 ms click + 300 ms body (peak -6.02 dBFS); rare result 300 ms body 3 dB louder + 600 ms tail 7 dB below it (peak -6.02 dBFS). F-13 -15.57 vs -14.84 LUFS (0.73 LU: R-31 PASS); loudest 400 ms block (momentary) -13.76 vs -10.57 LUFS (3.19 LU louder). trap2.py: with the tail only as long as the body (rare result 2x the common length) a 2.5-3 dB louder body still passes F-13 (0.69-0.97 LU) at 2.7-3.2 LU louder momentary loudness",
     smallest_fix: "F-13 Compute: add 'and the momentary maximum: integrated_loudness of every 400 ms window at 100 ms steps (pad a shorter file to 0.4 s), the largest value'. F-13 wrong-number cell: add 'integrated loudness averages the tail in: a longer, quieter tail hides a body up to 3 LU louder; compare paid results by the momentary maximum'. R-31 last clause: 'Paid random reveal results: F-13 momentary maximum within 1 LU of each other and sample peaks (F-03) within 1 dB (D-03)'. D-03: '(within 1 LU momentary maximum, F-13)'. worked-examples.md:51 and :53: 'within 1 LU (F-13 momentary maximum)'. Integrated F-13 stays as it is for loudness-matching options at check-in B"}
  - {id: B2, class: blocking, check: C8 V3 (a Studio check passes the case it exists to catch),
     where: ".agents/skills/sound-design/references/roblox-audio.md:106 (§G 'Graph matches the card'); review.md:84 (R-40 'the AudioPlayer count in the Client data model stays flat across a 10 s burst')",
     expected: "The pooling check fails code that creates and destroys an AudioPlayer per hit (S-149)",
     observed: "§G says to compare the Client data model's AudioPlayer count before and after a 10 s burst. Create-per-hit code that destroys each player when it ends returns to the same count after the burst, so the check reads flat and passes. A count taken during the burst does not separate them either: a pool of N and N live per-hit players give the same number",
     evidence: "Reasoning from the check's own definition (no Studio connected to this session, as in round 1); studio-mcp SKILL.md C-03 confirms execute_luau can run on the Client data model, so a creation counter is runnable",
     smallest_fix: "§G graph row: 'in a play-test, on the Client data model, count AudioPlayers created during a 10 s burst (a DescendantAdded counter started before it): pooled = no new AudioPlayer after warm-up'. R-40: replace 'the AudioPlayer count ... stays flat across a 10 s burst' with 'no AudioPlayer is created during a 10 s burst after warm-up (§G)'; (G) also: no Instance.new(\"AudioPlayer\") outside the pool module"}
  - {id: B3, class: blocking, check: C3 + C7 (two self-review lines contradict; a correct design fails),
     where: ".agents/skills/sound-design/references/review.md:78 (R-34) vs :49 (R-09), :72 (R-28) and SKILL.md:103 (S-76 'a telegraphed attack gets a longer attack or a pre-sound')",
     expected: "The sharp-is-danger check (SS-05) compares like with like: threat hits and attacks against friendly one-shots",
     observed: "R-34 says 'onset-to-peak (F-02 minus F-01) of every threat cue is shorter than that of every friendly cue'. Tells, timer warnings and charges are threat cues that must rise (R-09 wants a warning's peak in the last third; S-76 gives a telegraph a longer attack). In any scene with a warning and a pickup, R-34 fails the correct warning, or pushes the agent to sharpen the telegraph and break S-76 and R-09. The F-02 cell's 'measure the attack layer's part' does not help: a rising warning is one layer",
     evidence: "V3 run (scratchpad sound-rev2/r34.py): shield-break warning built to R-09 (1 s, level rising to the end): rise 916 ms; enemy tell with a 400 ms swell (S-76): rise 423 ms; friendly pickup with a 40 ms soft attack: rise 38.6 ms. R-34 fails both correct threat cues. The maker's own run compared only a hit-like threat (coverage d2, R-34 row)",
     smallest_fix: "R-34: 'In one scene, threat hits and attacks (impact and contact one-shots) rise faster than friendly one-shots: onset-to-peak (F-02 minus F-01) of each is shorter. Tells, warnings, charges and build-ups are not compared: they rise by design (S-76, R-09, R-28)'"}
  - {id: R1, class: recommendation, check: C7 (a worked example teaches a different length than the rule),
     where: ".agents/skills/sound-design/references/worked-examples.md:27, :29",
     expected: "reward-and-juice.md S-194 maps T2 to tier B (150-300 ms) and T3 milestone to tier C (500-1000 ms); progression reward-tiers.md §2 names T2 'small goal', T3 'milestone'",
     observed: "The example calls bag-full 'the bag-full milestone at T2' and gives it 'its own short flourish under 2 s'. An agent copying the example sizes a T2 event like a milestone",
     evidence: "worked-examples.md:27, :29; reward-and-juice.md S-194 row; progression-design/references/reward-tiers.md:12-13",
     smallest_fix: ":27 'the bag-full event at T2 (small goal)'; :29 'Bag full (T2) gets its own short confirm, 150-300 ms (S-194 tier B)'"}
  - {id: R2, class: recommendation, check: C7 (evals, proposal only),
     where: "knowledge/jobs/J018-riot-craft/proposals/sound-designer.md:25 (evals row) vs .agents/skills/sound-design/evals/briefs.md checks 4.2, 4.3",
     expected: "The evals grade what the books now teach",
     observed: "4.2 expects no countdown tension 'for under-13 or restricted players' (D-07 now: on any paid roll; never sort by age or region). 4.3 expects odds 'behind a labelled button' (S-166 now follows platform-policy: odds as numbers before purchase, only a long list behind a worded label). A grader could mark the new, stricter answer as off-script",
     evidence: "evals/briefs.md:69-70; SKILL.md:126 D-07; roblox-audio.md:72 S-166",
     smallest_fix: "Add (e) to the evals proposal row: '4.2 no countdown tension or siren on any paid roll (D-07); 4.3 odds as numbers before purchase per platform-policy rules.md §A'"}
  - {id: R3, class: recommendation, check: records (coverage file only),
     where: "knowledge/jobs/J018-riot-craft/coverage/sound-designer.md:276 (F2b row)",
     expected: "The citation points at the listener's distance curve",
     observed: "It cites AudioListener.yaml ':398', which is in SetAngleAttenuation; the distance-curve multiplication sentence is at :450 (SetDistanceAttenuation). The book text is right",
     evidence: "grep of AudioListener.yaml: :374 SetAngleAttenuation, :423 SetDistanceAttenuation, :450 'multiplied with the volumes from all other attenuation curves'",
     smallest_fix: "coverage :276 ':398' -> ':450'"}
keep: [
  "round-1 fixes that hold: Doppler row and SC-10 now match SoundService.yaml:194-195 (graph emitters get no engine Doppler); R-16 and §G read DistanceAttenuationMode first and the listener curve too (AudioEmitter.yaml:167-185, :349-365; AudioListener.yaml:450)",
  "the five missing checks now exist and are runnable: R-62 + check-in B reference listen (SD-28), R-35 + R-53 + sequence question (SD-21), R-33 (WT-02), R-22 celebration length (GD-02); R-34 exists but needs B3's scope",
  "F table: DC removal first, F-10 band to 12 kHz with the 20 dB trust rule, F-09's K-weighting trap named, F-13 one common padded length (all traps found by runs)",
  "D-07 now points at ArePaidRandomItemsRestricted and forbids sorting players by age or region; S-164 points at D-03 and D-07 instead of restating them",
  "same-wave rows adopted: T1-T4 tier mapping in S-194, UI cue list keyed to the UI event names (matches ui-design motion.md Sound column and refusal/counter rules), floor-material refusal names the substitute (matches environment-craft handoffs C3), emotion per zone from the ambience map",
  "R-43 log-diff read from the signed column without --tol-ms (fixture re-run: +12 ms late cue shows as +12.000), with the asymmetric-tolerance and --pair rows as proposals",
  "the 'You cannot hear' frame, input codes on every line, check-ins A/B/C with goal questions and budgets, stage sheets on event ids, attempt/outcome split, worked examples in step order"
  ]
verdict: fix-first
</spec>
```

## Round-1 findings: fixed or open

| Round-1 id | Now |
| --- | --- |
| F1 R-31 measured RMS | fixed as asked (F-13 + F-03), but the integrated measure I proposed has a tail hole: B1 |
| F2a Doppler | fixed (roblox-audio.md:52, SKILL.md:93, we §1, proposals library row) |
| F2b distance curve | fixed (roblox-audio.md:107, R-16) |
| F3 five checks missing | fixed; R-34's scope is wrong: B3 |
| R1 D-07 wording | fixed (SKILL.md:126, reward-and-juice S-164) |
| R2 DC offset, F-10 band | fixed (review.md:113-115, :128) |
| R3 copies of the sync rule | fixed: numbers only in S-133; R-43 and R-54 keep the signed bounds they compare |
| R4 wiring self-check | fixed in text (R-40, §G), but the pooling measure passes per-hit creation: B2 |
| R5 same-wave rows | fixed (coverage V11 table; files confirmed) |
| R6 animator books | open for the lead: proposals row present; animation-design files unchanged |
| R7 SKILL size | fixed: §1-§5 end at 19,088 bytes; S-75, S-78 moved to craft-satisfying §B |
| R8 evals 3.5 | proposals row (d) present |

## C1-C8 results

| Check | Result | Note |
| --- | --- | --- |
| C1 coverage | fail (2 of 96 rows) | All 96 tagged IDs have a row (script); 5 rejections keep sound reasons. This round I opened the 5 rows that failed in round 1 and the about 25 rows whose landings the repair touched; the rest were opened in round 1 and are unchanged. GD-35 and SS-05 now have checks, but the checks give wrong answers (B1, B3) |
| C2 core principles | pass | §7 unchanged in substance, 20 rows, examples and checks; no contradiction with the master |
| C3 self-review | fail | B3 (R-34 fails correct warnings and tells); B1 (R-31 passes a louder rare result) |
| C4 kit rules and engine | pass | Doppler and distance curves now match the docs mirror; Client data model execute_luau is a real mode; clip_check --timing and shotlist log-diff verified; policy lines defer to platform-policy |
| C5 nothing valuable lost | pass | Every old SKILL.md rule id is still defined (script); moved rows found with the same text; dry-assets wording replaced by the baked/live split everywhere |
| C6 fixed rules | pass | Frontmatter byte-identical (md5 of lines 1-11 matches df13ff4); SKILL.md 205 lines, description 328 characters; no section renumbered; J018 phrase in every book file; no Riot, library ids or champions in bodies; no tips section; evals/ and evidence/ unchanged; no file outside the books and the two job files changed by this maker |
| C7 better work | yes, clearly | see below |
| C8 brief v2 | fail on V3 | V1 pass. V2 pass. V3: B1 (F-13 tail hole), B2 (pool count before/after). V4 pass. V6 pass. V7 pass (19.1 KB, re-read rule after compaction). V8 n/a (craft role; partner table and brief asks present). V10 pass (S-133 window, UI Sound column, floor_materials, T1-T4, ambience feeling key all agree). V11 pass (every row naming sound adopted or supported) |

## Will an agent make better work with these books?

Yes. I read eval brief 4 (egg reveal for young players) and brief 2 (horror stalker) as the agent would.

With the old books the agent had good rules and a cue card, but no process and no honest way to say what it checked. With the new books it does these things:
- It loads `platform-policy` first.
- It uses one windup asset for every tier and puts rarity only after the result.
- It sizes the results by notes, register and tail.
- It gives a tap to skip and a batch ceremony for the best result only.
- It sends the owner goal questions instead of claiming it listened.

For the horror brief, it gets one tell asset with no jitter keyed to the VFX tell event, a rising warning on the end-of-state event, and a distance check that reads the real attenuation mode.

Weak spots:
- The one number that guards "no louder rare results" can still be beaten by a longer tail (B1). It is the line the egg brief depends on.
- R-34 would make the agent fail or flatten its own tells and warnings (B3).
- The pooling check cannot see per-hit creation (B2).
- The always-loaded text is about 38 KB, and every job runs eleven steps. A minor cue gets lighter only through the short card and "picked by numbers".
- The bag-full example sizes a T2 event like a milestone (R1).

All three blocking fixes are one or two lines each.
