> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `live-ops-design`. Evidence: notes `01` §1 and §7 (LP:5-17, 212-246), `02` §1 (LP:248-285), Roblox fact-check FR-49, feedback-routes fact sheet (Q ids). Shared with the analyst: `analysis-design/references/diagnosis.md` §6 (player voice), which this file follows. Tags: V · E · O. Revised by J018 maker live-ops-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (§4 item 7 what fans want, §5 pain points from the current build).

# Evidence and player feedback

## 1. The evidence contract (O)
Treat every piece of evidence as a record: **claim, source, date, population, time window, metric definition, intervention, comparison, uncertainty, decision relevance** (LP:17).
Never convert:
- visits → unique players
- peak concurrent players → retention
- event attendance → returning-player rate
- gross spend → studio profit
- a scheduled release interval → development time
- a Discord share → "% of players"

Labels: VERIFIED (a platform documents it), EXPERIENCE (someone's account, not a controlled test), OPINION (a proposal), plus **studio-measured** for the analyst's numbers on our own game. An official announcement proves what was announced, not that it caused growth (LP:11). Unknown is not zero (LP:15).

## 2. Three evidence streams, three owners
| Stream | Owner | Live-ops reads it for | Never |
| --- | --- | --- | --- |
| Player data (weekly page, investigations, test results) | analyst (`analysis-design`) | the binding constraint; who is affected; denominators; measurement plans | invent a number, a denominator or a cause the analyst did not give |
| Player feedback | live-ops (sorting and counting), analyst (behaviour check) | the reasons players give; severe problems; contradictions | count by model estimate; treat one source as all players |
| Market signals | trend scout (`market-trends`) | dated outside appeal, rights, timing | treat "popular this week" as fit |

## 3. Feedback: every source is a different population (V, O)
Roblox's own testing page warns community feedback "may be biased" (fans are more likely to be in Discord) and says in-game feedback gathers quantifiable data from the general audience (FR-49, V).

| Source | Reaches | Misses | Facts (read 2026-10-21) |
| --- | --- | --- | --- |
| Roblox built-in prompt (`SocialService:PromptFeedbackSubmissionAsync`) | current players at a moment the game chooses | players who left | rating + optional filtered comment; comments 13+ only; one per player per day; creator export `.csv` only, no API (Q1-02..Q1-12) |
| Own in-game form | current players, all ages, with exposure counts | players who left | fixed choices first; typed text filtered on the server (`platform-policy` P-06) |
| Discord | engaged players aged 13+ | younger players (Discord 13+; links shown only to age-checked 16+); quiet players | no player ids from the game to Discord (DevForum 4665118) (Q5-27, Q6, Q8-07) |
| Comments, ratings, reviews | expectations, trust | context, author experience; campaigns | Roblox has no public written-review list today; votes and comments sit on the creator Feedback page (Q7-01..Q7-03) |
| Support reports | severe failures | players who cannot or will not report | Player Support is an alpha, 13+ only (Q1-15) |
| Behaviour data (analyst) | silent players | reasons | needs interpretation |

**Asking (O).** Ask at a meaningful moment with a small optional prompt that does not interrupt essential play. Ask what the player tried to do and what happened before asking for a rating or a solution. No leading questions ("How much did you love the event?"). Record who could see the prompt: eligible, exposed, responding. Prompting only event finishers hides the players whose failure matters most (LP:254).

**Always-available report route (O, from the J014 G2 test).** Timed prompts miss players at the moment of harm. Every game needs an in-game "Report a problem" entry (lost progress, missing purchase, bug) that any player can open at any time, plus at least one prompt that reaches new players in their first session. Discord is never the only route. Roblox's own Player Support flow is an alpha for age-checked 13+ players only (Q1-15), so it cannot be the only route either. If the game has none, the plan lists it as a candidate fix.

**Moderation is not research (O).** Remove abuse under community rules; never file legitimate criticism as abuse to make sentiment look better. Safety, exploit, purchase and data-loss reports go **at once** to their owner; they never wait to become a frequent theme. Never repeat exploit steps or personal information when closing the loop (LP:256).

## 4. Sorting (O)
1. **Keep excerpts and context first,** then tag. Tags: area/system · player goal · symptom · suspected cause · requested solution · sentiment · severity · cohort (observed, never inferred) · device/build · reproducible? · date (LP:258).
2. **Problem apart from solution.** "I cannot find the event entrance" and "give us more rewards" are different themes even if both are negative. "More rewards" may mean unclear progress (LP:224, 258).
3. **Several tags per item, one author once per theme.** Keep contradicting sub-themes visible (faster economy vs scarcity).
4. **Count with the tool,** never by model estimate: distinct authors per theme, per source, per window; messages as a separate intensity column; share = theme authors ÷ sampled authors **of that source** (`tools/liveops/feedback_count.py`). Cross-source overlap is "unknown" unless the sources share an id scheme; Roblox gives new players a per-game id and Discord ids are separate, so in practice overlap stays unknown (Q8-09, X-01).
5. **Quality checks** (template §E): read raw examples for every theme you use; review ambiguous items; keep a sample of exclusions with reasons; mark new themes apart from repeated ones; keep evidence that contradicts your preferred proposal.
6. A Discord poll measures the voters, not the game. Weighting is allowed only with a known sampling model and the analyst's approval (LP:260).
7. **What fans want (the line every theme, event or variant brief carries).** Name the audience first (age band, devices, which players: the brief's cohort), then the top problem themes and wanted traits with their distinct-author counts per source and the count file, plus the analyst's behaviour check for the same cohort. Write it as what this audience wants at its strongest, not what every player is "okay with". Never a model's guess, never one source as all players. A wanted trait the evidence does not show is marked `uncertain`.

## 5. Loud and silent (O)
- A loud minority is **neither representative nor wrong by default.** Detailed reports can expose a real exploit or an advanced-system problem: weigh **severity and reproducibility** with prevalence (LP:262).
- **Silence is not satisfaction.** Ask the analyst whether the same friction shows in behaviour for new players, non-payers, mobile players, returning players and veterans.
- The tool flags "one loud author" when one author wrote most of a theme's messages (threshold: at least 5 of a theme's messages and at least half of them; PROPOSAL, `tools/liveops/README.md`; owner digest J014 item 11). The flag is a warning; it changes no count.
- Never infer sensitive traits from language, usernames or spending.
- **Pain points from the current build.** Before a change to a live game, list what costs players now (extra taps, a hidden entrance, missed information, a dead walk) with where each was observed: a studio-operator capture walk of the area the feedback names, a funnel step from the analyst, or a theme id. A change that names no observed pain point is a restyle, not a fix.

## 6. Closing the loop (O)
Tell players: what they reported, what the studio verified, what changed, what is still open, when the next status comes. "You asked, we did" only where the sort links the theme to the change. When declining a request, explain the trade-off without blaming players. After the change, check whether the original problem is solved in behaviour; praise for an announcement is not evidence (LP:278).

## 7. Collection setup
The routes, the one folder, pseudonyms, deletion and secrets: `knowledge/jobs/J014-live-ops-designer/feedback-plan.md` (owner gate G1b; nothing is set up before the owner's yes). Per game, the approved setup goes to `knowledge/design/feedback-setup.md`.
