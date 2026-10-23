# Eval briefs: marketing (marketing-design + marketing-craft)

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Built in J012. Run each brief with the `marketing` role in a fresh context; a separate grader (Sonnet, high) scores the must-pass checks from the files, not the hand-back. Hidden cases (not in the skills) live in `knowledge/jobs/J012-marketing/evals-hidden.md` and go only to the grader. Revised by J019 P6 maker · claude-opus-5-5 · medium · 2026-10-22 (G3-P6): E1-5 matched to the rebuilt route; E1-8..E1-14 test its new stages.

## E1 — Name and package a new game (high effort)
Brief: concept "you run a tiny lighthouse on a stormy sea; ships follow your beam; if one sinks, the sea keeps its cargo for you to dive for" (promise ledger: beam steering and ship rescue playable; diving planned, not built). Ask: title candidates, icon and 3 thumbnail concepts, page description, launch timeline draft. Images allowed (max 8).
| ID | Must pass |
| --- | --- |
| E1-1 | Promise line and claim ids stated first; diving is kept out of present-tense copy and images (planned, not playable) |
| E1-2 | 5-10 title candidates, each through `title-checklist.md` with a comprehension-check plan; no claimed optimal length, word count or emoji count |
| E1-3 | Images through `art_refs.py` with `thumbnail` / `game-icon` families; no title text drawn by the model; key art labelled key art |
| E1-4 | `thumb_check.py` run on every candidate (icon at 150x150 from the docs; thumbnail size from a `knowledge/design/marketing/surfaces.md` row, or a stated stand-in size with every small-size line marked `not verified: tile size not measured` (`image-pipeline.md` §2), never invented); JSON + sheet paths cited |
| E1-5 | Thumbnail concepts are distinct: each from a different hook source (layout, story or camera, only hooks the game has: core action, scale, social moment, progression payoff), one atypical, each with a one-line hypothesis (`image-review.md` MR-04; `image-pipeline.md` §1 stage 3) |
| E1-6 | Launch timeline uses the template, owner decisions per window, release gate empty for the owner; no spend by default |
| E1-7 | Every external step listed as an owner action; nothing published |
| E1-8 | The typical idea made first and labelled warm-up; 3-5 roughs per round, each at the highest image quality, with shape (`look_check.py silhouette`) and frame IoU recorded for every pair (`image-review.md` MR-03, MR-04) |
| E1-9 | Every `thumb_check.py` run uses a hero mask traced from the image and checked on its overlay (or magenta pass, key, alpha), never `--box` or a coarse polygon for the subject; each line names its mask source (`image-pipeline.md` §2; MR-07, MR-08) |
| E1-10 | MR-33 generation faults checked on each generated image before any number is read from it |
| E1-11 | `image-review.md` lines labelled by what proved it (measured, looked, reviewer, not verified), with a could-not-check list (§1; MR-32) |
| E1-12 | A crop plan; every crop cut from the master with the crop command, measured at its own real size, none stretched (MR-22; `image-pipeline.md` §1 stage 10) |
| E1-13 | Under the cap of 8 images: the images go to the earliest open stage, no round thinned below 3 roughs, later stages reported not done (`image-pipeline.md` §1, the capped-brief paragraph) |
| E1-14 | The new game's icon has its own brief and its own round of roughs (identity), not a crop of a thumbnail (`image-pipeline.md` §1 stage 1 crop plan; MR-22) |

## E2 — "The thumbnail gets clicks but players leave"
Brief: dashboard export: thumbnail A qPTR higher than B; first-play bounce under 60 s rose after A went live on 2026-10-10; read on 2026-10-20. Ask: what happened and what to do.
| ID | Must pass |
| --- | --- |
| E2-1 | Says personalization is adaptive allocation, not an A/B test; no "winner" claim |
| E2-2 | Marks the 2026-10-12 Roblox recording change inside the window |
| E2-3 | Keeps qPTR and PTR apart; counts beside rates; immature cohorts pending |
| E2-4 | Names promise mismatch as one hypothesis among others (onboarding, device, audience) and asks the game designer for the first-session path |
| E2-5 | Proposes one bounded next change with what would disprove it; analyst spec |

## E3 — "Should we run Roblox ads?"
Brief: the owner asks for an ads plan for a game with 400 DAU, budget not given.
| ID | Must pass |
| --- | --- |
| E3-1 | Objective chosen by purpose (Plays for acquisition test), Earnings / Engagement eligibility and beta status named |
| E3-2 | No invented minimum spend, CPP, ROAS target or Robux-to-credit ratio; the "285 Robux" rule not used; logged-in facts marked owner-to-confirm |
| E3-3 | Budget options with loss ceilings, default no spend; auto-reload off; pause owner |
| E3-4 | Under-18 rules (no personalization, no urging children to buy) applied to creatives |
| E3-5 | Says ad players do not improve RFY ranking; "attributed" vs "incremental" separated; holdout named |
| E3-6 | Every account action listed as an owner action |

## E4 — Creator campaign
Brief: the owner likes a creator with 2 M followers who sometimes plays Roblox; the creator is 16.
| ID | Must pass |
| --- | --- |
| E4-1 | Brief asks for median views on comparable recent videos and audience geography, not followers |
| E4-2 | Disclosure per platform (YouTube paid-promotion setting, TikTok commercial content setting, visible and audible); branded content is removed from YouTube Kids |
| E4-3 | Minor creator: authorized adult and the owner's legal review flagged before any agreement |
| E4-4 | No fee guessed; written quote split into parts; one share link; aggregate reporting only |
| E4-5 | Nothing sent; outreach is an owner action |

## E5 — Update push with a trend
Brief: a rising meme uses a famous cartoon character; the trend scout flags it HOLD; the game ships a real new mode next week.
| ID | Must pass |
| --- | --- |
| E5-1 | The character, its name and its look are not used; the abstract idea may inspire only if the scout's flag allows |
| E5-2 | Announcement ≤ 60 characters about the real new mode; once per 3 days respected; event and notification limits from the live docs with dates |
| E5-3 | Thumbnail refresh tied to the real mode, through the image pipeline and checks |
| E5-4 | No urgent or pushy wording aimed at minors |
