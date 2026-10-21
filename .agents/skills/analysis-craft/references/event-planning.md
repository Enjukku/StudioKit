# Event planning: what a new feature must log

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `analysis-craft`. Owner J013-D3: "It decides which events a new feature should log, using the approved analytics skill from J001 (that skill covers the logging code; this agent covers reading the data)." Sources: owner's analyst paper (AP) §8, extracted in `knowledge/reference/analyst/03-practice-diagnosis-reporting.md` §2.8, §2.16, §4.3 (PR-EV ids); `.agents/skills/analytics/SKILL.md` (T ids). Tags: **V** documented · **O** practice.

## 1. Who owns what
| The analyst decides (this file) | The `analytics` skill and engineering decide |
| --- | --- |
| the decision each observation serves | the AnalyticsService method (funnel, onboarding, economy, custom) (T-04) |
| the competing explanations it must tell apart | where the call fires: server, after the server decided (T-01, T-03) |
| the meaning: trigger, eligible population, unit, success and failure, time basis | field slots: max 3 custom fields, bucketed values, 8,000 combinations (T-05, T-06) |
| which properties matter most (ranked) | names within limits: 100 custom event names, 10 funnels, 10 currencies, 20 transaction types, 100 SKUs (T-05) |
| version boundaries and comparability notes | rate: 120 + 20 × CCU requests per minute per server; never per frame or hit (T-05, T-07) |
| what archive of aggregates replaces Roblox's 90-day event roll-off | the telemetry module and the plan row in `knowledge/design/telemetry.md` |

The analyst writes the **measurement spec**; the engineering brief carries it (`handoffs.md` §5). The analyst never writes logging code.

## 2. Steps
1. **Start from the decision, not from the feature's actions** (O, AP:375). Write: the player benefit the feature promises; the decision the data must support ("keep, tune or cut the new upgrade tree"); the competing explanations that would lead to different actions (`analysis-design/references/diagnosis.md` §3).
2. **Pick the fewest observations that tell those explanations apart.** Every event answers a named question; an event with no decision is cut. Event count is not maturity (O, AP:401).
3. **Separate the four stages** (O, AP:379): *saw it* (opportunity, eligibility) · *chose it* (action) · *did it work* (result, incl. server-decided failure and its reason) · *got the reward* (authoritative delivery). "feature_used" cannot tell an invisible button from a failed try from a success.
4. **Fill the contract per event** (§3), then rank its properties by decision value: only the top 3 fit as custom fields (T-05). A spare field can carry the event version.
5. **Plan the acceptance walk** (§4) and **the retirement rule**.
6. **Hand to engineering** with the brief in `handoffs.md` §5; the builder implements through the `analytics` skill and adds the telemetry plan row.

Tension with `analytics` T-03 ("log the success, not the attempt"): the analyst needs tries and failure reasons. Both fit when a server-decided failure (not enough currency, requirement not met) is logged as its own funnel step or custom event *after the server decided*. Client-side attempts stay unlogged. (Flag J013: the owner decides whether T-03 gets this line.)

## 3. Event contract (one row per event; 16 fields, O, AP:377)
| Field | What to write | Note |
| --- | --- | --- |
| semantic name | outcome-style, stable: `feature_entered`, `reward_granted` | changing ids (map, item) go in properties, never in new names |
| exact trigger | the server moment it fires | after the server decided |
| eligible population | who could have produced it | needed for every rate |
| unit | player · session · attempt · transaction | repeating flows: one run id per run (T-04) |
| success / failure meaning | what success is; which failures are recorded and their reasons | |
| time basis | which clock (server UTC) | |
| required properties | ranked; top 3 become custom fields | bucketed values (T-06) |
| supported dimensions | which Roblox dimensions the analysis needs (platform, new user) | funnel segments go on step 1 (T-08) |
| currency and amount units | economy events: currency, positive amount, balance after | T-04 |
| deduplication meaning | when two firings count as one | one-time steps: saved flag (T-07) |
| version | v1, v2…; a change of meaning = new version + comparability note | append funnel steps, never renumber (T-08) |
| sampling plan | complete, or sampled with the inclusion rule | money and progression accounting are never sampled |
| privacy purpose | why we need it; no typed text, chat, personal data (`platform-policy`) | |
| retention | Roblox drops events 90 days after last data (T-05): name the aggregate archive we keep (`tools/analytics`) | |
| owner | role that answers for it | |
| decision it enables | the question and the report it feeds | no row → no event |

## 4. Acceptance before ship and retirement
- Walk these journeys in a test build and check each is recorded as intended: success, cancel, retry, interruption (leave mid-step), returning player (O, AP:399).
- Totals reconcile with an independent authoritative record where one exists (purchases vs receipts, grants vs saves).
- No missing properties; no impossible order (reward before attempt).
- In an experiment, both arms have the same chance to log.
- Say what a session with no terminal event means: "unknown", never a quit reason.
- Authoritative money and progression accounting stays apart from sampled diagnostics (O, AP:401).
- Retire a measurement no decision uses any more; keep its definition and history so old analyses still read.

## 5. Example shape (generic; fill per feature)
| Decision question | Observation | Context to record | Why it earns its place |
| --- | --- | --- | --- |
| Did eligible players find the feature? | eligibility + a real chance to see it | feature version; earlier progress; test arm | separates reach from choice |
| Can players start? | entry try + server accept or failure reason | required resource state | separates unclear UI from unmet requirements |
| Is the first round understood? | round start, one meaningful checkpoint, result | tier; party or solo | finds friction without logging every action |
| Is progress too slow? | milestone reached; time and attempt summaries | progress stage; active play time | tells difficulty from affordability |
| Was the reward delivered? | authoritative grant | reward category; currency | completion is not delivery |
| Does the feature help the game? | later return and total play | eligible cohort; follow-up window; test arm | stops clicks becoming the success metric |
| Does it hurt performance or trust? | version-linked crash, FPS, feedback | device, OS | guardrails |

(O, AP:383-393, generic rows only.)
