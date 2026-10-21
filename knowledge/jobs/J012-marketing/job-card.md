---
type: job
scope: universal
status: done
updated: 2026-10-21
source: owner chat 2026-10-21 (/build-agent marketing)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J012 — Build the marketing agent

| Field | Value |
| --- | --- |
| Job id | J012-marketing (J006 is kept for the animator) |
| Size | L (new role, 2 skill books, a 1,164-line paper with 79 dated sources (many after the model cutoff) to extract and fact-check, 6 templates, a thumbnail check on top of `look_check.py` with tests, an art-bible family change, a real test with ChatGPT images) |
| Owner (human) | owner |
| Job owner (agent) | lead (orchestrator) |
| Status | G1 approved 2026-10-21 (J012-D6). Steps 2-5 done 2026-10-21: 3 notes + 3 fact-checks (FD 74, FA 70, FS 66 rows) in `knowledge/reference/marketing/`; tool `tools/art/thumb_check.py` (15 tests); skills marketing-design, marketing-craft; 6 templates in `templates/marketing/`; art-bible families `thumbnail`, `game-icon`; role `marketing`; evals E1-E5 + hidden H1-H4; roster row. Gate PASS. Step 6 (G2) not run (J012-D8). Closed 2026-10-21 (J012-D9): in kit, not yet tested |
| Depends on | `reference-images` skill + `tools/art/art_refs.py` (exist); `tools/art/look_check.py` (J009, exists, 20 tests); `templates/skill/art-bible.md` (exists); `platform-policy`, `analytics`, `game-concept`, `market-trends`, `art-direction` skills (exist); analyst and live-ops-designer roles (planned, not built) |

## Owner's words (2026-10-21, excerpts)
- "It gets each game found, clicked and played: the title, icon, thumbnails, game page, trailers and short videos, update announcements, social media, creator outreach, Roblox ads and the community (for example Discord)."
- "It works from the start with the game designer (the hook and the fantasy: titles players read and think 'I need to do that'), the trend scout (what is rising), the art director (key art that matches the game) and the analyst (what works, measured)."
- "Icon and thumbnail images are made with ChatGPT through the kit's reference-images skill and tools/art/art_refs.py. If the art bible template needs a family for thumbnails, add it to templates/skill/art-bible.md and to the skill's role table."
- "It tests titles, icons and thumbnails with Roblox's testing tools and reads the results with the analyst."
- "It never promises what the game does not deliver, and it follows Roblox's rules on advertising, misleading titles and thumbnails, younger players, and copyright and trademark."
- "Use it as strong evidence, but not as gospel. Check claims that matter, especially Roblox discovery facts, click-through numbers, ad costs and platform rules, and drop what you cannot back up."
- "A thumbnail check the agent can run before showing me anything: readable at small size, one clear moment, strong contrast. Reuse the art director's image check tools if they exist."
- "This agent replaces marketing-store in the roster."
- "Model: Opus, medium effort; high effort for a new game's title, icon and launch plan."

## Goal
One `marketing` agent that gets each game found, clicked and played by players who then enjoy it. It sells the game's real, playable promise: title, icon, thumbnails, game page, native gameplay video, short social videos, update and event announcements, creator briefs, Roblox ads plans and the community. It starts at the concept with the game designer, uses the trend scout's dated signals, gets key art that matches the art bible, and defines every test with the analyst before it runs. It checks every image before the owner sees it, and it prepares decision packages: it never publishes, spends, contacts creators or signs anything without the owner's yes.

## Material received
| Source | What | Size | Trust |
| --- | --- | --- | --- |
| `C:\Users\Firew\Downloads\Roblox_Marketing_Agent_Research_2026.txt` (outside git; owner wrote it) | 15 rules; Roblox discovery (custom-thumbnail eligibility 2026-10-19, RFY 28-day signals, retrieval vs ranking); titles; icons, thumbnails and personalization (bandit, not A/B; qPTR vs PTR); game page and native gameplay video (YouTube embeds removed); short videos and trailers (Shorts, TikTok, Reels; music rights; cadence); creators (disclosure, minors, quotes, share links); Roblox Ads Manager (objectives, audiences, attribution, published incrementality, DevEx rates); updates, events, notifications; Discord and the Roblox privacy notice; launch craft (Roblox and non-Roblox cases with limits); measurement (2026-10-12 recording change, cohort maturity, Open Cloud APIs, YouTube view change); rules for younger audiences, ad integrations, copyright, trademark; 13-step process; 6 templates (title checklist, thumbnail/icon checklist, image brief, short-video plan, 4+4-week launch timeline, weekly report); don'ts; open questions; source register D01-D20, P01-P19, C01-C06, S01-S22, N01-N12 | 1,164 lines, 99 KB | high: VERIFIED / EXPERIENCE / OPINION tags on every claim, dated sources, numbers kept with their scope. The paper ran no campaign, account test or player study. 30+ sources are dated after the model cutoff (2026-06) → live check |
| Kit: `reference-images`, `art_refs.py`, `look_check.py`, `art-bible.md` template, `art-direction` §marketing, `game-concept` (title and hook test), `market-trends` + `trend-scan` (hand-offs to marketing), `analytics`, `platform-policy` (ads rules C) | The pipeline and the rules the marketing agent works inside | — | owner-approved |

## Scope
| In | Out |
| --- | --- |
| Reference notes in `knowledge/reference/marketing/` + fact-check tables (Roblox discovery, thumbnails, video, events, notifications, ads, policy; social platforms; creator and legal; the case numbers) | Publishing, posting, ad spend, creator contact, contracts (owner actions; the agent prepares packages) |
| Skills `marketing-design` (what and why) and `marketing-craft` (how), names in digest item 4 | Changing `look_check.py` checks or `art_refs.py` beyond what the thumbnail families need |
| 6 templates in `templates/marketing/` | The analyst and live-ops-designer roles (planned; hand-off briefs only) |
| Thumbnail check on top of `look_check.py` + offline tests (digest item 3) | Discord bots, Discord Social SDK, any cross-platform user data |
| Art-bible template: thumbnail and game-icon families + locks; `reference-images` role table row | A real game's title, page or campaign |
| Role file `marketing`; roster row replaces marketing-store; pointer lines in game-designer, trend-scout, art-director role files where they say "marketing (planned)" | Player studies, buying views or engagement |
| Hand-off briefs to game designer, trend scout, art director, analyst (planned), live-ops designer (planned) | |
| Eval briefs + hidden cases; 1 real test (G2) | |

## Crew
| Role | Model | Effort | Deliverable |
| --- | --- | --- | --- |
| extractors ×3 (paper §1-4 discovery, titles, images, page; §5-9 video, creators, ads, updates, community; §10-13 + templates + don'ts + open questions) | Sonnet | high (J004, J009 precedent; digest item 6) | dense notes per part |
| fact-checkers ×3 (Roblox discovery, thumbnails, video, events, notifications, analytics: live docs + DevForum + local docs mirror; ads, ad policy, DevEx, younger players: live docs + `platform-policy` rules; social platforms, creators, FTC, Discord, legal, case numbers: web) | Sonnet | high | fact-check tables: claim, source, checked against, verdict |
| tool builder (thumbnail check + tests) | Opus | medium | script + tests (digest item 3) |
| lead (merge, skills, templates, role, art-bible families, hand-offs, evals, review) | Opus | high | 2 skills, 6 templates, role, families, hand-offs, evals, roster |
| marketing test (new agent) | Opus | high (new game's title, icon and launch plan) | G2 package (digest item 7) |
| grader (hidden cases, separate context) | Sonnet | high | rubric scores |

## Mechanism
Subagents, max 3 at a time. Wave 1: 3 extractors. Wave 2: 3 fact-checkers (they read the extract notes and the paper's register). Tool builder runs in wave 2 if a slot is free, else wave 3. The lead writes the skills and templates (it needs the paper, the fact-checks and the kit's neighbour skills together). The new agent runs the G2 test as a subagent with `art_refs.py` and the thumbnail check.

## Budget
| | Estimate | Actual |
| --- | --- | --- |
| Sessions | 1 (this one) | |
| Agents | 3 extract + 3 fact-check + 1 tool + 1 test + 1 grader = 9 | |
| Models / effort | Sonnet high ×7; Opus medium ×1; Opus high ×1 + lead | |
| Image generations | G2 test: about 6-10 ChatGPT images (2 icons, 3 thumbnails, retries) | |

## Acceptance checks
- [ ] Every Roblox discovery fact, click-through or lift number, ad cost or rate and platform rule in a skill has a source, a date and a fact-check verdict (confirmed / corrected / unverified-kept-with-label / dropped); dropped claims listed with the reason.
- [ ] No invented numbers: no optimal title length, posting time, cadence, video length, creator fee, CPM, CPP or budget. Platform limits are stated as limits, never as optima. Case results stay EXPERIENCE with their scope.
- [ ] Every "test" names what the Roblox tool really does (thumbnail personalization = adaptive bandit, not A/B; titles and icons: what native testing exists, from the fact-check) and the analyst-defined metric, denominator, cohort and window.
- [ ] Truth rule is checkable: each marketed feature maps to a build and a real capture (proof sheet); generated key art is never labelled gameplay.
- [ ] Policy: ads, under-13 and under-18 rules, disclosures, misleading metadata, paid random items, copyright and trademark restated from `platform-policy` and the fact-check, with the owner actions listed.
- [ ] Owner gate: the role never publishes, spends, contacts creators or contracts; packages end in an owner decision.
- [ ] Thumbnail check: offline tests pass; it reports measurements and saved diagnostic images (small-size preview, grayscale, subject/ring value, subject count), never a pass without an owner tolerance.
- [ ] Art-bible template: new families parse in `art_refs.py print`; `reference-images` role table updated.
- [ ] 6 templates exist and each one is used in the G2 test or an eval.
- [ ] Hand-off briefs to the 5 roles follow `rules/messages.md`.
- [ ] Skills ≤ 500 lines, "Read this file when" table, overlay line; `python tools/sync_harness.py --check` and `python tools/verify.py` PASS.
- [ ] Evals: 3-5 briefs with must-pass checks; hidden cases scored by a separate grader.

## Gates
| Gate | Date | Owner's words |
| --- | --- | --- |
| G1 brief | 2026-10-21 | "All right, understood. Go ahead and begin." |
| G2 first real test | — | not run: "No." (J012-D8) |
| G3 final approval | 2026-10-21 | "I think we're just fine. Because I don't want to do any testing right now." (accepted without the G2 test, J012-D9) |
