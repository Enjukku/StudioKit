---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J009-T11 (grader); evals-hidden.md; output/art-direction/j009-t10/case-1..3.md; art/test-b/*; J002-D9, J002-D12
supersedes: []
held_out: true   # repeats held-out cases, keys, rubrics or answers (rules/knowledge.md §3)
---
> Author: grader · claude-sonnet-5-5 · high · 2026-10-21

# J009 G2 grades (art-director agent)

Paths: `C1/C2/C3` = `output/art-direction/j009-t10/case-1.md` etc. `EGG` = `knowledge/jobs/J009-art-director/art/test-b/art-review-egg-shop.md`, `ANI` = `.../art-review-anime-summon.md`, `BR` = `.../briefs-ui.md`. Line numbers are file lines. I checked that every skill rule id the agent cited (C-04..C-17, EL-04, EL-65, CD-05, SC-04..SC-29, M-54, M-64/65, RV-05, R-03, K07) exists in the skills and says what the agent claims. No fabricated rule ids found.

Grade truth for part 2 (lead correction, 2026-10-21): egg shop = C minus; anime summon = B minus (after ChatGPT image generation). J002-D12 "B minus, some buttons A" stays as the owner's overall remark for the (b) points.

## Part 1: hidden cases

### H1 (cosmetic attack variant): 10 / 10
| Row | Pts | Evidence |
| --- | --- | --- |
| Parity rule (C-06) | 2/2 | C1:47 names vfx-design area-parity and art-direction C-06 and says reading *more* clearly is also a fault. Matches the C-06 text ("parity is two-sided"). |
| Captures at phone size, dodge clip, motion NOT REVIEWED | 2/2 | C1:77-82 (E2 same-seed frame-stepped base vs variant, E3 muted/unmuted clips, E4 real phone, E6 tester notes); C1:88-94 K-rows NOT REVIEWED; C1:104 motion "not reviewed (no clip)"; C1:13 verdict NOT REVIEWED. |
| Thin lines: raster width at device size, no universal minimum | 2/2 | C1:57 "There is no universal minimum line width", record the edge raster width; C1:79 E4; C1:203 C3. |
| Color: non-color channel, affected-player test, grayscale not proof | 2/2 | C1:52 (not color alone; "grayscale or one simulator capture alone does not prove a fix"; test with affected players); C1:80 E5; C1:246-247 Ticket 2 C2/C3; C1:234 avoid "a brighter red as the only change". |
| Direction to VFX as outcome + acceptance evidence, no recipe | 2/2 | C1:159-208 Ticket 1 and C1:210-249 Ticket 2: `fixed` values carry sources, method left in `open`, `avoid` list, runnable checks. |

General rubric
| Item | Result | Evidence |
| --- | --- | --- |
| Observation / interpretation / decision separate | PASS | C1:34-62 (each finding has the three labels). |
| No invented threshold or studio rule | PASS | C1:57, C1:83 ("measured (diagnostic) until a tolerance is approved"); briefs say "no invented thresholds" (C1:194, C1:238). |
| Owner decides, nothing called approved | PASS | C1:114-119 D1-D3 are PROPOSAL with defaults; C1:194. |
| Hand-back in messages.md section 3 form with coverage | FAIL (on the files) | The file starts with "Verdict" (C1:13). No `STATUS:` first line and no `coverage` block in the file. The agent's closing chat message was not given to me, so this is not shown. |

### H2 (card board effect): 10 / 10
| Row | Pts | Evidence |
| --- | --- | --- |
| Attention does not match importance; spectacle reads as "best move" | 3/3 | C2:37-40 (F1, C-04), C2:53-57 (F3: "its strength says play this"; C-04, C-10, C-17). |
| Persistent effects get less demand than short decisive events; must not hide next decision | 3/3 | C2:39 ("a lasting board state matters most when it starts"; persistent state is a UI job, event information a VFX job); Ticket 1 C2:154-200 (`importance_rank` below decision cues, onset kept, `avoid` full-screen persistent layer). |
| Combined-frame capture, not isolated sheet | 2/2 | C2:13 ("The combined frame is the problem"), C2:61 F4, C2:75 E1 layer cut, C2:284 process note. The E2 clip (C2:76) is of the board effect over time, in the same turn; accepted. |
| Briefs to VFX and UI with protected qualities and acceptance evidence | 2/2 | Ticket 1 (C2:154-200, protects onset and style) and Ticket 3 (C2:238-280); game-designer Ticket 2 for the meaning (C2:203-236). |

General rubric: obs/interp/decision PASS (C2:35-61); no invented threshold PASS (C2:81, C2:186 "screen share is reported, not targeted"); owner decides PASS (C2:110-115); hand-back form FAIL on the files (C2:13, same reason as H1).

### H3 (pickups vs debris): 9 / 10
| Row | Pts | Evidence |
| --- | --- | --- |
| Diagnosis: shared shape, color, value; collect state has no distinct role | 3/3 | C3:37-47 (H1 same family, H2 debris louder, H3 same timing), C3:51-52 F2. |
| Color role never matching surroundings + non-color channel; recorded as bible role + lock proposal | 2/3 | C3:71 (at least one identity feature "not hue (value, form, motion or material response)"), C3:72 debris never uses the "reward color role", C3:123 lock PICKUP-ID as PROPOSAL. Lost 1: the agent never proposes the color role itself or a bible row (it only asks for an existing role, E7 C3:88); no concrete channel such as hover or glint is named. |
| Respects owner's 2D-sprite rejection as locked | 2/2 | C3:54-57 F3, C3:74 C4, C3:191 and C3:229 repeated as rules in the briefs. |
| In-game phone clip after change; route to VFX / modeler as outcome | 2/2 | C3:79 E1, C3:200 and C3:243 after-capture requests, C3:204-205 C3 check; Tickets 1 and 2 (C3:162-250). |

General rubric: obs/interp/decision PASS (C3:35-57); no invented threshold PASS (C3:87, C3:193; "2-3 iconic features" is sourced to C-07); owner decides PASS (C3:119-123); hand-back form FAIL on the files (C3:13).

Part 1 total: **29 / 30** on the case rows; general rubric **9 / 12** (three fails, all the missing STATUS/coverage in the files).

## Part 2: blind UI reviews (egg shop, anime summon)

### (a) Grade agreement
| Screen | Agent grade | Owner grade | Steps apart | Result |
| --- | --- | --- | --- | --- |
| Egg shop | B- (EGG:13) | C- | 2 (C-, C, C+... lead counts it as two) | DISAGREE (over-grade). It would have agreed with the earlier "B minus". |
| Anime summon | B+ (ANI:15) | B- | 2 | DISAGREE (over-grade) |

### (b) Owner points caught
| Owner point | Egg shop | Anime summon |
| --- | --- | --- |
| Face gradients without a visible step (D9) | PARTLY. EGG:64 measures the card-face span (dL* 15.6 in v1, 26.9 in v2) and EGG:98 says v2 "face is darker", but there is no finding that v1 gradients are weak. I checked the images: the v1 Meadow/Ocean/Lava faces are a faint light-to-light blue; v2 is a clearer step. | not present in current screens (the crystal buttons show a clear step) |
| Shine bars stop short of the face edge (D9) | CAUGHT. EGG:98 (EF5) and EGG:83 (K12) say the v1 bars stop mid-face and v2 crosses edge to edge. Confirmed in the images (v1 vs v2 Meadow card). Weak spot: ranked 5 of 7 and framed as "two candidates" evidence. | not present in current screens |
| Overall "alright, usable, not great" | PARTLY. B- and "usable" fit (EGG:13), but the tone is "convincing, on-style" and the weak finish is not said. Against the C- truth: leans too kind. | MISSED. ANI:15 "clear, premium, honest"; ANI:99-107 praise. Owner: B-. |
| Some buttons strong | PARTLY. EGG:112-114 keeps the cartoon signature, yet EF3 (EGG:96) says Buy is not the brightest control. | CAUGHT. ANI:15 and ANI:102 (Summon buttons ratio 6.3 own the frame). |
| "With the reference photos, this can be improved" (D12) | CAUGHT. EGG:100 (EF7) and EGG:138 (D-c) ask for a screen-level target image. | PARTLY. ANI:26 and ANI:89 note no screen target, but AF6 turns it into "owner taste" and no decision row (ANI:126-128) asks for the target image. |
Tally: egg 1 caught + 3 partly + 0 missed; anime 2 caught-or-partly (1 caught, 1 partly) + 1 missed (applicable points only).

### (c) Review quality
| Check | Result | Evidence |
| --- | --- | --- |
| feedback-briefs.md section 3 layout (9 sections) | PASS | EGG sections 1-9 (EGG:13-139); ANI sections 1-9 (ANI:13-129). Names by content (`art-review-<subject>`). |
| Measured numbers cited from look_check JSON | PASS | EGG:53-65 and ANI:49-59 give the JSON path per row; values match the findings (81.7 %, 23.1 %, 0.183 vs 0.044). |
| Observation / interpretation / decision separate | PASS | Ranked-finding tables split Observation, Consequence (interpretation), Verdict (EGG:92-100, ANI:82-90). R-03 respected: only WCAG rows carry pass/fail (EGG:67, ANI:59). |
| NOT REVIEWED for motion and device | PASS | EGG:82-84 (K11, K13) and EGG:120-129; ANI:74-76 and ANI:109-119. |
| Briefs in messages.md section 2 form, no recipes | MOSTLY | BR:30-78 and BR:96-139 have all keys, sourced `fixed`, `avoid`, runnable checks. Flags: BR:74 "at least 1 visible px" is an unsourced threshold; BR:71 and BR:135 tune to a luminance ordering although BR:62 says do not tune to numbers; briefs are labelled NOT sent (fine). |
| Hand-back form (extra) | FAIL on the files | Neither review file has a `STATUS:` first line or a `coverage` block (EGG:13, ANI:13); the briefs ask for it from others (BR:77) but do not follow it themselves. |

### (d) False or unsupported claims
I opened the images and checked the top 3 findings of each review.
| Finding | Image check | Result |
| --- | --- | --- |
| EGG EF1 Review Buy over Chances Buy | `02-odds-open.png` Buy y 690-810; `03-review.png` Buy y 712-832, same x. | Supported. Consequence ("a double tap can skip Review") is an inference; the agent labels it as consequence. |
| EGG EF2 paw placeholder, faint celebration | `06-confirmed.png`: white paw in a blue circle, pale yellow sunburst on a white panel; `02` rows all paw icons. | Supported. |
| EGG EF3 Buy not brightest; white Chances lighter | `01-inspect-main-1920*.png`: Chances is a near-white button above a mid-green Buy. | Supported. |
| ANI AF1 Confirm over Summon x1 | `03-review.png` Confirm y 780-914 vs Summon x1 starting y 883, x overlap 983-1377. | Supported. The x1 Review is not drawn; the agent says so (ANI:84). |
| ANI AF2 pressed button jumps | `04-commit.png` Confirm y ~790-924 vs `05-pending.png` button y ~718-852 and wider; the popup shrinks. | Supported. |
| ANI AF3 disabled Cancel louder | `03` Cancel is dark glass; `05` Cancel is a light metallic grey. | Supported. |
| Extra check: ANI AF5 and EGG e06 stray "250" | `07-reveal-10x-summary.png`: Toma x6, Mythic head inside the card; `06-confirmed.png`: cut "250" top-left. | Supported. |
False claims found: 0. Unsupported items: the "1 visible px" brief threshold (BR:74); "13 of 17 units" (ANI:79) I did not check against the spec; the grades themselves (see weaknesses). Scope note: EGG:100 cites J002-D12 (from the style book) in a blind test; harmless but it names the owner decision.

## Totals
| Part | Score |
| --- | --- |
| Part 1 case rows | 29 / 30 |
| Part 1 general rubric | 9 / 12 (all three fails = hand-back form) |
| Part 2 (a) grade agreement | 0 / 2 screens |
| Part 2 (b) owner points | egg 1 caught, 3 partly; anime 1 caught, 1 partly, 1 missed |
| Part 2 (c) review quality | 4 pass, 1 mostly, 1 fail (hand-back form) |
| Part 2 (d) false claims | 0 false; 1 unsupported threshold |

## The 5 most important weaknesses
1. **Grades are too high and have no anchor.** B- for the egg shop (truth C-) and B+ for the anime screen (truth B-); both two steps off. The agent lists failed checks (egg K01, K04, R-11, EF1 purchase safety; anime AF1-AF3) and still grades up. The skills hold no grade scale or rule that links fails to a grade. Points to: `art-review/SKILL.md` section 3 step 6 and `references/feedback-briefs.md` section 1 (verdict words only, no grade).
2. **Leniency comes from weighting measured passes over look and finish.** The verdict lines lead with passes: "convincing, on-style ... reads on the smallest phone, and the purchase flow is honest" (EGG:13), "clear, premium, honest" (ANI:15). The what-works lists are mostly contrast, odds honesty and hierarchy numbers (EGG:115-116, ANI:100-107; K05 pass at EGG:76, ANI:68). Look and finish items sit low or outside the grade: popups "a calmer, older form look" is only a cohesion note (EGG:109); "tidy, not sharp ... energy is low" is called taste (ANI:89). Points to: `art-review/SKILL.md` R-03 (no tolerance, no verdict) and `feedback-briefs.md` section 1 ("a metric that only differs from a preferred image is never revise"), which together push look problems into needs-decision; and `art-direction/SKILL.md` section 4 craft core (look quality is not measured by the gate).
3. **Look and finish findings are pushed to owner taste.** No finding that the v1 face gradients lack a visible step (only a number, EGG:64); AF6 and D-f hand the energy question to the owner (ANI:89, ANI:128); the screen target image is a low-priority process item (EGG:100) although the owner said reference photos are the fix. Points to: `art-review/SKILL.md` section 3 step 6 and `art-direction/SKILL.md` C-04, C-08, C-10.
4. **Hand-back form missing in the files.** None of the 5 files (C1-C3, EGG, ANI) has `STATUS:` first or a `coverage` block; the cases open with "Verdict". Points to: `rules/messages.md` section 3 and `art-review/SKILL.md` section 6 (self-check).
5. **Briefs carry small unsourced or tuning checks, and C3 left the color role open.** BR:74 "at least 1 visible px"; BR:71 and BR:135 check a luminance ordering against a no-tuning rule (BR:62); C3 never proposes the pickup color role or names concrete channels (C3:71-72, 2/3). Points to: `rules/messages.md` section 1 (a `fixed` value needs a source), `art-review/SKILL.md` R-03, `art-direction/SKILL.md` C-10 (color roles).
