> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Part of `preproduction`. Sources: N2 §1.3 (T1 pillar sheet), §3 (document architecture, T3 feature spec, T4 tuning table), §4.1 (T6 decision record), `rules/knowledge.md` §3-§4 (paths, frontmatter). Templates are O. The status words and paths are J003 additions. Revised by J018 maker game-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (vision record parameters, feature spec fields 2, 6, 9, 13 sharpened; new §6 feedback stack, §7 threat and hazard sheets, §8 role card, §9 read rank and information list).

# Documents: short vision, living specs, one source per number

## 1. Architecture and states
A short vision-and-pillars record links to living feature, system, content and craft specs. Long documents fail when readers cannot find the current rule or duplicated values drift; a one-page design works only when the left-out detail is truly unneeded or linked (N2 5.1 O).

States (J003 addition, aligning the paper's mixed words, N2 W14): **proposed** → **approved** (owner decision id) → **implemented** (build revision) → **superseded** (replaced by a newer version, link it) or **retired** (removed, no replacement). Never delete; supersede.

| Document | Path | Holds | Frontmatter `type` |
| --- | --- | --- | --- |
| Vision record | `knowledge/design/game-profile.md` (fill its table) + `## Vision` section | fantasy line, title, first image, audience, device mix, target experience (one or two kinds of fun), parameters (camera, player count, input, session shape), one physics and motion language (gravity, jump arc and hang time, impact weight; agreed with the animator where a jump or hit is gameplay), orientation conventions, signature moment, pillar names, style direction summary, excluded references | profile |
| Pillar sheets | `knowledge/design/pillars.md` | one T1 sheet per pillar (§2) | profile |
| Promise ledger | `knowledge/design/promise-ledger.md` | claim → feature map (`game-concept/references/hook-promise.md` §2) | reference |
| World and characters | `knowledge/design/world-and-characters.md` | places, landmarks, characters and the role they make readable, where each key moment happens | reference |
| Key moments | `knowledge/design/moments/<moment-id>.md` (beat-sheet template) | setup, decision, consequence, payoff; state names; the timed stages (tell, build, peak, result); who owns what | reference |
| Role cards | `knowledge/design/world-and-characters.md` (one section per character, unit or pet) | §8 | reference |
| Closed doors | the job folder, `closed-doors.md` (final ones also in `tried-and-failed.md`) | directions the owner closed, with the date and words; never re-proposed without new owner words | job |
| Core loop | `knowledge/design/core-loop.md` | three scales, coupling, resets vs persists, experiment cards (`game-design`) | reference |
| Feature specs | `knowledge/design/features/<F-id>.md` | T3, 15 fields (§3) | reference |
| Tuning values | the game's data files under `content/` (path set by the architect) + the T4 table (§4) in the feature spec | one source per value | — |
| Decisions | `knowledge/design/decisions.md` (+ T6 record in the job folder for big ones) | owner's words | decision |
| Uncertainty register | `knowledge/design/open-questions.md` (column "proposal in use"; put the owner and test in the question text) | every open assumption | — |
| Concepts | `knowledge/design/concepts/<concept-id>.md` | pitch records (`game-concept`) | reference |

Every authored file starts with the frontmatter of `rules/knowledge.md` §5 and an author line. Dense tables, fixed keys.

## 2. Pillar sheet (T1, 9 fields)
A pillar is a constraint on decisions, not an adjective; no pillar count is optimal (N2 T1 O).
| Field | Holds |
| --- | --- |
| Vision and owner | the approved fantasy; who decides |
| Pillar name | a plain behavioural intention ("Every hit moves the world") |
| Player evidence | what players can do, perceive or choose if the pillar works |
| Required implications | systems, art, controls, social structures that must support it |
| Tradeoff | what the team gives up rather than weaken it |
| Rejected example | a tempting feature that breaks it, and why |
| Conflict rule | how it ranks against another pillar; who decides an unresolved conflict |
| Test | prototype condition, observation, failure signal, next decision |
| Status | proposed / approved / retired; date; decision id; linked specs |

## 3. Feature spec (T3, 15 fields)
An implementation contract for decided behaviour that also names what stays with each craft (N2 T3 O).
| # | Field | Holds |
| --- | --- | --- |
| 1 | ID, version, status | `F-<nn>-<slug>`, vN, state |
| 2 | Purpose | the player problem, the target experience it serves, the pillar, the promised action, why it is needed; the four parts (goal, opposition, decisions, rules) one line each |
| 3 | Scope and exclusions | included, omitted, postponed |
| 4 | Actors and permissions | who may start, observe, interrupt, complete, reverse |
| 5 | Prerequisites and inputs | player and world state, inputs, resources, ownership, network assumptions |
| 6 | State model | every state, entry condition, transition, timeout, interruption, end state; the named timing stages each craft keys to; threats and hazards on their sheets (§7) |
| 7 | Rules and invariants | what always holds, including server authority and saved data |
| 8 | Tuning references | parameter keys, units, allowed range, current value or TBD, provenance, owner (§4) |
| 9 | Outputs and feedback | world change, UI, animation, VFX, sound, analytics events, each tied to a state or event; the feedback stack per action (§6); the read rank and information list (§9) |
| 10 | Failure handling | disconnect, duplicate request, data unavailable, invalid target, cancel, full inventory; recovery |
| 11 | Dependencies | systems, craft assets, compatibility limits, order of work |
| 12 | Acceptance criteria | Given / when / then + invariant; 5 paths: success, boundary, interruption, denied action, multiplayer disagreement |
| 13 | Test and instrumentation plan | test ids, audience, device and network conditions, event fields, privacy limits, decision criterion |
| 14 | Open choices | craft-owned decisions and the limits they must respect |
| 15 | Approval and change log | owner decision, lead reviews, superseded version, linked tuning revision |

Add an **experience test** to field 13: what players should do or say if the feature works (P-09), and the plain-block test for any new object or enemy (a tester names it from behaviour alone). Client-callable features: field 7 lists the server checks (`networking-security`); saved fields: the save schema owner (`data-saving`).

## 4. Tuning table (T4, 7 fields)
One authoritative data source; documents link to its revision. A number copied by hand into several briefs drifts (N2 T4 O; no measured failure rate).
| Field | Required |
| --- | --- |
| Parameter identity | stable key, system, meaning, owner |
| Value and units | current value or `TBD`; seconds, studs, currency or another stated unit |
| Domain and relationships | legal min and max where known; dependencies; invariants |
| Provenance | source, calculation, experiment, or "untested starting hypothesis" |
| Version and application | data revision, build revision, migration rule, server or client authority |
| Evaluation | intended behaviour, telemetry, test condition, result |
| Change record | old → new, reason, approver, rollback route |

Making values easy to change during balance work is supported by Sakurai's account; it gives no schema and no default values (N2 5.3; P19 O, video not reviewed).

## 5. Decision record (T6, 13 items, for big decisions)
ID and date · question · approved intent · recommendation · material alternatives · evidence and uncertainty · the owner's exact decision (owner's words) · rationale · affected specs, assets, tuning, tests · accountable leads · next verification · reconsideration trigger · superseded decision. A pending decision stays pending. Small decisions: one row in `decisions.md`.

## 6. Feedback stack (in feature spec field 9, one table per action)
Every player action gets feedback; its size teaches what matters (`game-design/references/principles.md` §7). I fix the events, order, tiers and lengths; each craft owns how its layer looks and sounds.

| Field | Holds |
| --- | --- |
| Action and target experience | the input, what the player should feel (one line) |
| Named stages | e.g. load → charge → release → travel → impact → result; the same names animation markers, VFX and sound cue cards use (marker names in the vocabulary) |
| Attempt cue | what answers on the input (small, client side, on the press frame or the next), per channel: animation, VFX, sound, UI |
| Outcome response | what plays on the confirmed result only, per channel; the confirmation source (server event or replicated state); the pending state when confirmation is slow (PROPOSAL default: `game-design/references/principles.md` §7) |
| Outcome tiers | miss · blocked · hit · big hit (or sale sizes, rarity tiers), each graded by a cause the player can learn; never random; never louder than the outcome |
| Failure and refusal | the distinct cue per failure; for a refusal, the message at the control (cause and fix), the icon, the rate-limited sound |
| Celebration | tier (from the progression designer's reward tier table, `progression-design/references/reward-tiers.md`, when the feature has rewards), what triggers it (real threshold only), length (PROPOSAL default: `principles.md` §7), where bigger ceremonies run |
| Frequency | expected rate (the measured rate from the same reward tier table when the feature has rewards) and burst; merge window (PROPOSAL default: `principles.md` §7); cap on live copies; label and sound once per window |
| Counters | the true value used by logic; count-up length; exact final number |
| Channels and comfort | every state change in at least two channels; shake, flash, tint or slow motion only at the top tier of the local player; the reduced variant of each intense channel |
| Checks | press-to-first-change and celebration length from a fixed-camera frame folder with `tools/vfx/clip_metrics.py` (`onset_ms`, `visible_ms`; the clip conditions in `game-design/references/principles.md` §7 checks); rejected-request capture; outcomes distinct with sound off; 100-trigger repeat at the real rate |

## 7. Threat and hazard sheets (in the feature spec, or the stage brief)
Threat sheet, one row per enemy or boss attack and per timed hazard:
| Field | Holds |
| --- | --- |
| Attack id, owner | the attack, who owns its data |
| Counter | the tool, skill or route that beats it |
| Reaction window | telegraph lead as a tuning key (PROPOSAL starting values and the floor: `game-design/references/principles.md` §8); longer for bigger attacks |
| Tell | the wind-up pose intent and the second channel (effect, sound); identical every time; removed on the damage frame |
| Danger area | shape, size, timing as tuning keys the effect reads (never set by eye); the drawn edge equals the hit area from warning to last tick |
| Importance | the threatened player sees it at full strength; how bystanders see it |
| Escalation | phase changes (low health), the climax behaviour |
| Check | frame-stepped capture against the window; two captures with an identical tell; server hit-shape overlay at warning, contact, end |

Hazard sheet, one row per hazard (`game-design/references/spaces.md` §5):
| Field | Holds |
| --- | --- |
| Hazard id, why it exists | boundary, risk and reward, a pacing beat |
| Entry effect | kill, or damage per second (tuning key); server owns the rule |
| Items in it | what happens to items thrown or placed in it (destroyed after N s, kept, pushed out) |
| Duration and end | how long the danger lasts; the danger look ends on the last tick |
| Source and containment | where it visibly comes from; what contains it |
| Reward spot | any brave position inside it, and its counter |
| Visibility | the shape, value and colour role that read it (never colour alone); reserved danger colour |
| Check | a QA case per rule; art and design describe the same rule |

## 8. Role card (every character, unit, pet, tower; before any reference image)
| Field | Holds |
| --- | --- |
| Roster gap | what the game needs that this fills ("a front line", "a slow heavy threat"); the roster entries with the same role |
| Role and behaviour | what it does in play, its movement pattern (distinct per enemy type), its verb |
| Threat or importance rank | where it sits among the roster; its screen size follows the rank (bigger = more important) |
| Shape and build intent | sharp, round or square by role (threats sharp, friendly round); thinnest, average or bulkiest against the cast; its source of power that must read first; a hero's signature item is more intricate than common items of its class (big parts, not micro detail), so it signals a skilled owner |
| Character core | 2-4 traits and the tension in them (e.g. "elegant + deadly"); what it would never do or wear; for a known archetype (knight, ninja, golem), the traits that make the archetype work, kept in every option |
| Sell list | the 2-4 things every image of it must sell |
| Numbers that must show | health, speed, range, area, as tuning keys the look expresses |
| Nearest look-alike | the roster neighbour it must not be confused with |
| Cost flags | extra forms (each counts as another character of work), flowing parts, new joint chains, each with the reason it earns its cost; a creature meant to scare is flagged "keep it scary" with a reference (half-human creatures turn silly easily) |
| Check | a fresh reader names the role from the image alone; lineup capture: size rank equals threat rank; black-fill differs from the nearest look-alike (on flat-key captures at the game camera, `game-design/references/review.md` §7, or with `--mask`: `tools/art/look_check.py silhouette <capture> --compare <look-alike capture>`; a high aligned IoU is a flag); the hero signature item has clearly more parts and moving pieces than common items of its class (counted) |

## 9. Read rank and information list (per scene, level, screen)
| Field | Holds |
| --- | --- |
| Read rank | what must be noticed 1st, 2nd, 3rd... (default: threat to the local player, own action, objective and pickups, other players' effects, ambient; environment is the backdrop) |
| Information per moment | what the player must know to decide, at each moment of the loop (health, ability ready, objective, currency, timer); each item names where it lives (world, HUD, menu) and how fast it must be read (critical: about 1 s, PROPOSAL) |
| Information areas | what must stay visible in this scene (other players, HUD zones, targets, shop and placement areas, the smallest gameplay object on each floor) and the maximum effect height in studs that keeps them clear (PROPOSAL until a capture tests it); the VFX read card reads them (`vfx-design/references/read-card.md`) |
| Loudness tiers | the importance tiers of effects, sounds and celebrations in this scene and their caps |
| Reserved signals | the gameplay colours and shapes this scene uses, kept out of decoration |
| Screens and states | every screen and popup the feature needs, with empty, error, loading, disabled, reward and purchase states |
| Check | blurred or thumbnail capture: first-noticed = rank 1; each HUD element maps to an information need; every state reached in a play-test is on the list |
