---
type: job
scope: universal
status: active
updated: 2026-10-20
source: owner chat 2026-10-20 (/build-agent trend-scout)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · medium · 2026-10-20

# J004 intent brief — trend-scout agent

<intent>
The owner wants to see, each week, what is rising on Roblox and around it early enough to make a game from it, and how sure the studio can be. The trend-scout finds rising Roblox games and rising core loops with dated numbers, watches outside trends (TikTok, YouTube, Instagram, creators, memes, shows and films, music, events, Steam and mobile games) that may move into Roblox, and turns the strongest signals into 3 research opportunities of the form "proven loop + new theme + twist". It flags where copying a loop crosses Roblox rules or copyright. The game-designer turns the opportunities into pitches; the scout never designs the game.

Accuracy is the point. The owner said to be strict about which numbers are official and which are third-party estimates. Revenue and playtime for other games are always estimates. CCU is not players per day, visits are not players, a chart rank is not money. Growth is measured over time from the studio's own saved history, so the data tools and their history matter as much as the skill books. Access must be legal: official or free documented routes only, no scraping against a site's terms, keys only in environment variables.

The research paper is strong evidence but not gospel: check the numbers, endpoints, quotas, terms and Roblox facts that the skills and tools depend on, and drop what cannot be backed up.
</intent>

<spec>
id: J004
from: owner
to: lead
skills: [orchestration, ste-writing, platform-policy, analytics, code-review, architecture]
refs:
  - C:\Users\Firew\Downloads\uterd\NewGame\Roblox_Trend_Scout_Research_2026.txt   # take: evidence contract, endpoint map, tracker models, history schema, g7/acceleration/coverage, breakout and fade flags, loop line + 8 fields, loop catalogue, copying vs expression, transmission chain, source/permission registry, scoring sheet, test card, weekly template, scout performance; avoid: treating its thresholds (+50% g7, +100 CCU, 90% coverage, score cut-offs) as proven
  - knowledge/reference/game-design/02-preproduction-docs.md   # take: the game-designer's intake of trend opportunities (7 fields) so the hand-off matches
  - .agents/roles/README.md   # take: trend-scout (research → Sonnet medium), marketing (planned), analyst kept separate
fixed:
  role_name: trend-scout                      # owner 2026-10-20; roster J003-D4
  model: sonnet, effort medium                # owner 2026-10-20
  tool_builders: opus, effort medium or higher   # owner 2026-10-20
  report_cadence: weekly, to owner + game-designer   # owner 2026-10-20
  opportunities_per_report: top 3, with evidence     # owner 2026-10-20
  opportunity_form: proven loop + new theme + twist  # owner 2026-10-20
  analyst_role: separate (own game's player data)    # owner 2026-10-20
  marketing_role: roster "planned" + hand-off brief only   # owner 2026-10-20
  schedule: plan only; owner approves before setup         # owner 2026-10-20
open: [book structure inside the two skills, tool structure inside tools/trends/, report wording, chart types]
not_in_scope: [game design, own-game analytics, building the marketing agent, paid data services, scrapers, setting up a schedule]
rules:
  - Paraphrase sources; never copy paper text; the paper stays outside git.
  - Every number carries one provenance label (official, third-party sampled, third-party estimate, owner/developer statement, derived with formula); revenue and playtime of other games are always estimates; unknown stays UNKNOWN, never zero.
  - Only legal, allowed access; no scraping that breaks a site's terms; no login, CAPTCHA or rate-limit bypass; a 200 response is not permission.
  - Keys and tokens only in environment variables or key files outside the repo; never in code, notes, commits or chat.
  - Every script has offline tests; the gate must PASS.
  - No personal data about children; creators are tracked by channel, never by viewer.
  - Branded or franchise themes get a rights/policy flag (platform-policy); an unknown right means HOLD.
  - Thresholds from the paper stay PROPOSAL until backtested or owner-approved.
  - Skills ≤ 500 lines, kit template, project-overlay line.
deliver: knowledge/reference/trends/*, .agents/skills/market-trends/*, .agents/skills/trend-scan/*, .agents/roles/trend-scout.md, tools/trends/*, tools/tests/test_trends_*.py, templates/trends/weekly-report.md, knowledge/jobs/J004-trend-scout/schedule-plan.md, knowledge/jobs/J004-trend-scout/handoffs.md
checks: see job-card.md acceptance checks
return: G1 to owner now; G2 first real scan + tool demo; G3 approval
</spec>

## Proposed skill books
| Skill | Kind | Holds | Read by |
| --- | --- | --- | --- |
| `market-trends` | design | What a trend signal is and is not; provenance labels; what each metric means (CCU, visits, favorites, votes, chart ranks, tracker estimates); growth vs spike vs fade; loop line and 8 loop fields; loop families (dated, checked); proven loop + new theme + twist; copying a loop vs copying expression (copyright, trademark, Roblox IP and discovery rules); outside-trend transmission chain; timing and "too late"; opportunity gates and scoring sheet; test card | trend-scout, game-designer, marketing |
| `trend-scan` | craft | Source and permission registry; how to run each tool; formulas (time-weighted CCU, g7, acceleration, coverage, momentum vs WoW, playtime estimate, half-life); breakout and fade flags (PROPOSAL thresholds); manual-entry workflow for TikTok, Instagram, Google Trends and tracker pages; weekly procedure; report template; hand-off formats; scout self-score (false alerts, missed breakouts) | trend-scout |

## Proposed data tools (`tools/trends/`, Python standard library, offline tests)
| Tool | Source | Access | Condition |
| --- | --- | --- | --- |
| history store | local files (`TREND_DATA_DIR`, default `.tools/trend-data/`, gitignored) | none | raw rows keep source, timestamps, provenance, gap and event flags |
| Roblox collector | public Games API: game details, votes, favorites | no key | only if the terms check allows automated reads; polite rate, honours 429 |
| metrics | the history store | none | paper formulas, tested |
| Steam collector | Valve Web API current players | free key in env var if needed | official route only (no SteamDB) |
| Apple collector | Apple RSS chart feed | none | official feed builder |
| YouTube collector | YouTube Data API | owner's key in env var | quota and 30-day storage rule respected |
| Twitch collector | Twitch Helix top games/streams | owner's client id + secret in env vars | optional |
| manual import | CSV the scout fills from TikTok Creative Center, Google Trends, Instagram, tracker pages | none | for sources with no allowed API |
| report renderer | history + scout's notes | none | Markdown report + HTML page with charts |

## Known risks (to resolve in step 2)
1. Roblox terms and automated reads: the paper notes new terms with AI-use language from 2026-11-01. The fact-checker checks whether automated reads of the public Games API are allowed. If not, the Roblox collector becomes a manual import and the item goes to the owner.
2. Growth needs history: g7 needs 2 full weeks of samples. The first report can show snapshots and "emerging leads" only.
3. A weekly scan alone cannot measure growth: the collector must sample often (several times a day); the report is weekly. The schedule plan covers both.
4. Trackers (Rolimon's, RoVitals, RoTrends) are read by hand, not scraped; their revenue and playtime numbers are third-party estimates.
5. "Verity" in the paper is a Minecraft horror character from the channel ThatMob, not a child creator. Creators are tracked by exact channel ID.

## Hidden test set (evals)
Held out of the skills: the paper's dated candidate example (§9: three games with 24 h and 7-day means) and the "too late" cases (§8). The eval gives the agent raw numbers and dates only and checks that it labels overlapping-window momentum as not week-over-week, marks estimates, refuses fake precision, flags rights, and ranks research priority without inventing approvals. A separate grader scores it.

## First real test (G2), proposed
The trend-scout runs the first real weekly scan with the new tools (live Roblox counters for a seed watchlist, official outside sources, manual entries) and writes the first report (Markdown + HTML). Shown next to the paper's §9 example.
