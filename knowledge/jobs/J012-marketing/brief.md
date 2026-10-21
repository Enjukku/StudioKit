---
type: job
scope: universal
status: active
updated: 2026-10-21
source: owner chat 2026-10-21 (/build-agent marketing)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J012 intent brief — marketing agent

<intent>
The studio needs one agent that gets each game found, clicked and played, by players who then enjoy what they clicked on. A good game that nobody finds fails. A game that gets clicks with a false promise also fails: on Roblox, the players who bounce and do not come back count against the game in the recommendations. So the agent sells the real game, and it sells it well.

It starts at the concept, not at launch. With the game designer it turns the hook and the player fantasy into a title players read and think "I need to do that", and it checks that ordinary play delivers that promise. With the trend scout it uses what is rising, with dates and without copying protected names, art or music. With the art director it gets key art that matches the art bible, through the kit's ChatGPT image pipeline. With the analyst it decides what a test can show before the test runs, and reads the result honestly: inconclusive is an allowed answer.

It owns the whole package: title, description, icon, thumbnails, game page, native gameplay video, short social videos, update and event announcements, creator briefs, Roblox ads plans and the community plan. It checks every image at the size players see before the owner sees it. It follows Roblox's rules on ads, misleading titles and thumbnails, younger players, copyright and trademark. It prepares decision packages; the owner approves the promise, the final assets, every external message and every spend.

The owner's research paper is strong evidence, not gospel. Platform facts change monthly, so each fact that the skills keep has a date and a check. A number the research cannot back up is dropped, not guessed.
</intent>

<spec>
id: J012
from: owner
to: lead
skills: [orchestration, ste-writing, reference-images, art-direction, game-concept, market-trends, analytics, platform-policy]
refs:
  - C:\Users\Firew\Downloads\Roblox_Marketing_Agent_Research_2026.txt   # take: 15 rules; discovery order of diagnosis; title promise system; icon/thumbnail/personalization facts and limits; page checklist; native video vs social edit; short-video craft; creator brief, disclosure, minors; Ads Manager objectives, audiences, attribution, two-ledger accounting; events, announcements, notifications; Discord safety and the privacy conflict; launch craft from cases (mechanism, not numbers); measurement dictionary; release gate; 13-step process; 6 templates; don'ts; open questions. avoid: case numbers as forecasts, platform limits as optima, the Steam rules as Roblox rules
  - .agents/skills/reference-images/ + tools/art/art_refs.py + templates/skill/art-bible.md   # take: families, locks, anchors, approve step; add thumbnail and game-icon families. avoid: changing the machine-read format
  - tools/art/look_check.py   # take: thumb, value, silhouette checks; reuse, do not fork
  - .agents/skills/{game-concept, market-trends, trend-scan, art-direction, analytics, platform-policy}   # take: what each neighbour already owns (hook test, trend labels and hand-offs, marketing truth rules, metrics, ad rules), so the marketing books point to them and do not repeat them
fixed:
  role_name: marketing                                  # roster J003-D4; replaces marketing-store (owner 2026-10-21)
  model: opus                                           # owner 2026-10-21
  effort: medium; high for a new game's title, icon and launch plan   # owner 2026-10-21
  scope: title, icon, thumbnails, game page, trailers and short videos, update announcements, social media, creator outreach, Roblox ads, community   # owner 2026-10-21
  works_with: game-designer, trend-scout, art-director, analyst (planned)   # owner 2026-10-21
  images: ChatGPT via reference-images + art_refs.py; thumbnail family in art-bible template + role table if needed   # owner 2026-10-21
  testing: Roblox testing tools; results read with the analyst   # owner 2026-10-21
  truth_and_policy: no promise the game does not deliver; Roblox rules on ads, misleading titles/thumbnails, younger players, copyright, trademark   # owner 2026-10-21
  templates: title checklist, thumbnail+icon checklist, thumbnail image brief, short-video plan, launch timeline, weekly marketing report   # owner 2026-10-21
  thumbnail_check: readable at small size, one clear moment, strong contrast; reuse look_check.py; else the smallest script with tests   # owner 2026-10-21
  hand_offs: game-designer, trend-scout, art-director, analyst (planned), live-ops-designer (planned); rules/messages.md format   # owner 2026-10-21
  external_actions: publish, post, spend, creator contact, contracts = owner only   # AGENTS.md §0, paper rule 15
open: [book structure inside the two skills, template field names, thumbnail-check measures and output, hand-off wording, eval cases]
avoid: [invented optima (title length, cadence, posting time, video length, fees, CPP), case numbers as forecasts, "A/B" for adaptive allocation, fake UI or Robux in images, copied competitor expression]
owns: [knowledge/reference/marketing/, .agents/skills/<two books>/, templates/marketing/, the thumbnail check + its test, .agents/roles/marketing.md, the two new families in templates/skill/art-bible.md, one row in reference-images §3, roster row, J012 job folder]
not_in_scope: [publishing, spending, contacting creators, Discord bots or SDK, analyst and live-ops roles, a real game's campaign, changes to look_check.py checks]
rules:
  - Paraphrase sources; the paper stays outside git. Quotes ≤ 15 words, attributed.
  - Evidence tags kept (VERIFIED / EXPERIENCE / OPINION). A number without a scoped, dated source is dropped or marked PROPOSAL; platform numbers that move go in as link + date read (platform-policy P-10).
  - Facts dated after 2026-06 are checked live before they enter a skill.
  - No game-specific content in kit files.
  - Skills ≤ 500 lines, "Read this file when" table, overlay line (templates/skill/SKILL.md).
  - Generated files are never edited by hand; run tools/sync_harness.py.
deliver: [notes + fact-checks, 2 skills, 6 templates, thumbnail check + tests, art-bible families, role file, hand-offs, evals, G2 package]
checks: job-card.md acceptance checks
return: rules/messages.md §3 hand-back (STATUS, coverage, evidence)
</spec>
