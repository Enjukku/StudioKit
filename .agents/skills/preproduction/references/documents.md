> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Part of `preproduction`. Sources: N2 §1.3 (T1 pillar sheet), §3 (document architecture, T3 feature spec, T4 tuning table), §4.1 (T6 decision record), `rules/knowledge.md` §3-§4 (paths, frontmatter). Templates are O. The status words and paths are J003 additions.

# Documents: short vision, living specs, one source per number

## 1. Architecture and states
A short vision-and-pillars record links to living feature, system, content and craft specs. Long documents fail when readers cannot find the current rule or duplicated values drift; a one-page design works only when the left-out detail is truly unneeded or linked (N2 5.1 O).

States (J003 addition, aligning the paper's mixed words, N2 W14): **proposed** → **approved** (owner decision id) → **implemented** (build revision) → **superseded** (replaced by a newer version, link it) or **retired** (removed, no replacement). Never delete; supersede.

| Document | Path | Holds | Frontmatter `type` |
| --- | --- | --- | --- |
| Vision record | `knowledge/design/game-profile.md` (fill its table) + `## Vision` section | fantasy line, title, first image, audience, device mix, signature moment, pillar names, style direction summary, excluded references | profile |
| Pillar sheets | `knowledge/design/pillars.md` | one T1 sheet per pillar (§2) | profile |
| Promise ledger | `knowledge/design/promise-ledger.md` | claim → feature map (`game-concept/references/hook-promise.md` §2) | reference |
| World and characters | `knowledge/design/world-and-characters.md` | places, landmarks, characters and the role they make readable, where each key moment happens | reference |
| Key moments | `knowledge/design/moments/<moment-id>.md` (beat-sheet template) | setup, decision, consequence, payoff; state names; who owns what | reference |
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
| 2 | Purpose | the player problem, the pillar, the promised action, why it is needed |
| 3 | Scope and exclusions | included, omitted, postponed |
| 4 | Actors and permissions | who may start, observe, interrupt, complete, reverse |
| 5 | Prerequisites and inputs | player and world state, inputs, resources, ownership, network assumptions |
| 6 | State model | every state, entry condition, transition, timeout, interruption, end state |
| 7 | Rules and invariants | what always holds, including server authority and saved data |
| 8 | Tuning references | parameter keys, units, allowed range, current value or TBD, provenance, owner (§4) |
| 9 | Outputs and feedback | world change, UI, animation, VFX, sound, analytics events, each tied to a state or event |
| 10 | Failure handling | disconnect, duplicate request, data unavailable, invalid target, cancel, full inventory; recovery |
| 11 | Dependencies | systems, craft assets, compatibility limits, order of work |
| 12 | Acceptance criteria | Given / when / then + invariant; 5 paths: success, boundary, interruption, denied action, multiplayer disagreement |
| 13 | Test and instrumentation plan | test ids, audience, device and network conditions, event fields, privacy limits, decision criterion |
| 14 | Open choices | craft-owned decisions and the limits they must respect |
| 15 | Approval and change log | owner decision, lead reviews, superseded version, linked tuning revision |

Add an **experience test** to field 13: what players should do or say if the feature works (P-09). Client-callable features: field 7 lists the server checks (`networking-security`); saved fields: the save schema owner (`data-saving`).

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
