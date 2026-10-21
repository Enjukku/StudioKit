---
name: art-direction
description: What and why of one visual direction for a Roblox game - player fantasy in pictures, shape language, value, color roles, light and mood, cohesion across crafts. Use when the look is set or changed, for "it doesn't look like one game", "it looks generic / like AI", "the screen is busy", "I can't see the attack", "make it look great". Art director reads first; art-review is the how.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit skill: universal. Built in J009 from the owner's art-director research paper (2026-10-21, fact-checked), the owner-supplied Riot "So You Wanna Make Games??" transcripts (via the first game's art-fundamentals skill) and the first game's art history. Evidence ids point to `knowledge/reference/art-direction/` notes: `01:` precedents, `02:` direction/bible/readability, `03:` light/cohesion/anchors/feedback, `04:` platform/evolution/marketing/process, `05:` first game, `FC-S`/`FC-A` fact-checks.

# Art direction: one world, read at a glance

## 1. When this skill starts
It answers four questions, in this order, for any game or feature:
1. **What must the player feel and decide?** The fantasy, the repeated decisions, the camera, the devices (from the game designer).
2. **What is the world's grammar?** The few relationships every craft must show (shape, value, color roles, material, light, motion, sound) and what may vary.
3. **What reads first, right now?** The hierarchy for each moment, from the player's current decision.
4. **Does the combined frame still work?** On a phone, at the real camera, in the busiest supported scene, at the lowest supported quality.

The art director owns the answers as **proposals**. The owner approves every lock and every anchor (J009-D3). How to write the bible, run the checks and brief specialists: `art-review`.

## 2. Read this file when
| You need | Open |
| --- | --- |
| Deadlock, League, TF2, Dota 2 and 8 other studio cases: what to learn, what not to copy, what is the studio's own word | `references/precedents.md` |
| Readability by task, hierarchy, shape, value, color roles, light across quality tiers, cohesion across crafts | `references/clarity-cohesion.md` |
| Phones and Roblox rendering, evolving a style, marketing art, the 10 don'ts | `references/platform-evolution-marketing.md` |
| How to write the art bible, explore directions with ChatGPT images, measure, review and brief | `art-review` skill |
| Reference images, locks format, anchors tool | `reference-images` skill |
| The craft owners' own rules | `ui-design`, `vfx-design`, `sound-design`, `rig-pipeline`, `environment-design`, `level-design` |
| The source notes and fact-checks | `knowledge/reference/art-direction/` |

## 3. Steps
1. **Restate the moment.** What the player does, the 1-2 things they must notice first, the intended feeling, camera, device (phone first). Missing input that would change the direction: ask the game designer; never fill it with another game's convention (04:PS01, 05:AD03).
2. **Name the world rule.** One causal premise the whole world obeys, so every craft can derive its choices from it (example pattern: familiar institutions changed by one supernatural premise). Each craft must show what the rule changes; a pretty place with unrelated icons and generic effects fails (01:DL-13, 01:SC-S3-L).
3. **Turn pillars into visual hypotheses.** A pillar becomes observable relationships (masses, states, what looks causal), never a particle count or polygon budget. Specialists propose the implementation (02:D3-D4).
4. **Explore distinct directions, not palette swaps.** Each candidate states what it changes (proportion, material, density, light, camera reading, emotion) and is shown as a comparable packet at the same camera. Stop exploring when new images test no real uncertainty. The owner picks after hearing appeal and risks (02:D5-D12; `art-review` §3).
5. **Lock little, lock well.** A lock constrains a relationship that carries identity or meaning, with purpose, scope, approved example, failure example and test. Write what may vary next to it (01:EC4, 02:RD3, 02:BF4).
6. **Set the hierarchy per moment.** Rank what must be noticed now, read next, and left as atmosphere; give each craft its screen job (§4 C-05).
7. **Review in context, then in combination.** Gameplay camera, busiest scene, small screen, lowest quality, with motion and sound evidence or marked NOT REVIEWED (`art-review` §4-5).
8. **Direct by outcome.** Ranked discrepancy, why it matters to the player, what must survive, acceptance evidence; the specialist picks the craft (`art-review` §6).
9. **Keep the direction alive.** Versioned bible, anchors and exceptions; drift checks; owner-approved changes with a transition plan (`references/platform-evolution-marketing.md` §2).

## 4. Craft core (what separates great art direction from weak)
| ID | Practice | Evidence |
| --- | --- | --- |
| C-01 | **Coherent decisions, not attractive assets.** Good art can be wrong for this game: a beautiful effect can hide a threat, an impressive environment can flatten character reads, a polished thumbnail can promise a game that does not exist | paper rules 1, 12, 14 (01:EC1-EC2, OPINION); owner: "the models look fine, but they don't look like they exist in the same world" (05:OR16) |
| C-02 | **Three jobs of game art:** clarity (threat, goal, mine, interactable, how am I doing), satisfaction (every action answered at once), style (one look that sets the emotion). Style is a tool for emotion, not decoration | owner-supplied Riot transcripts (05:AF01) |
| C-03 | **A world grammar, not a rendering recipe.** Shared construction rules plus a contrast in how each faction or district relates to them beat "one side blue, one side red". Signature objects and motifs organize the action vocabulary (names, icons, animation accents, roles), not only decoration | Deadlock updates and hero introductions, Valve 2026 (01:DL-05 to DL-08, studio-published facts; the transfer is the paper's reading, 01:DL-13 to DL-19) |
| C-04 | **Attention matches importance.** Rank effects and cues by consequence (damage, control, dodgeability, how it changes the opponent's play) and make screen attention match the rank. A big telegraph that promises a dodge the mechanic does not give miscommunicates | Riot "Clarity in League", 2021 (01:LL-04; the over-promising telegraph example is the Arcane Comet rune, LL-05 corrected FC-S) |
| C-05 | **Screen ownership.** Level = navigable structure and calm regions; character = identity; VFX = event information; UI = persistent state and controls; animation = action and intent. A foreground effect may dominate briefly for a major event but never hides what the player must answer. Negotiate per game; it is not a fixed law | paper (02:HI2, OPINION); Rift layering is a 2014 description, not a rule (01:LL-10, LL-12) |
| C-06 | **One clarity budget per thing.** A costume, skin or variant shares one budget of change across model, motion, VFX and sound; turning all of them up erases recognition. Parity is two-sided: a variant reads neither less nor more clearly than the base (a stronger or earlier read changes the outcome as much as a weaker one). Say which recognition cues a variant has spent and which must stay | Riot describes skin clarity as one "bucket" each discipline fills, never "everything up to 11", aiming at clarity parity with the base (01:LL-06, LL-08, corrected FC-S) |
| C-07 | **Identity contract per character or tool.** The silhouette feature that must survive, the facing cue, the power-source cue, the 2-3 iconic elements to push when small | Riot 2021 (01:LL-02); Riot transcripts (05:AF11-AF12); TF2 class silhouettes, Valve 2007 (01:TF-01) |
| C-08 | **Lower everything else.** To make one thing stand out, lower the contrast of its neighbors, not only raise the target. If every element is loud, nothing is; save the biggest, brightest, longest effect, sound and motion for the biggest moment | Riot transcripts (05:AF03, AF09) |
| C-09 | **Detail is a contrast channel.** Alternate calm, simple areas with dense detail where the eye should land; spend complexity where it changes recognition or emotion and simplify where the camera shows nothing | Riot transcripts (05:AF05); paper (04:SP1); Dota 2 character guide rest areas (01:DO-01) |
| C-10 | **Value first, color by role.** Check hierarchy with hue removed. Write color as roles (threat, ally, interactable, reward, disabled, selected, accent, decoration), one meaning per treatment, with a non-color backup for every essential state. No universal palette size | paper (02:SH2-SH3, M4, OPINION); Xbox guideline 103 (02:M4, verified FC-A) |
| C-11 | **Shape meaning is learned per game.** Spiky = danger, round = friendly is a starting hypothesis; fix this game's shape language in the bible and test it with its audience | paper (02:SH1); Riot transcripts as a hypothesis (05:AF08) |
| C-12 | **Light keeps the information.** A lighting direction states the impression it must give and the information that must survive it (route, character, interaction, danger) on the supported quality settings. Never let bloom or a thin shadow carry importance alone | paper (03:LM1-LM3, QT5, QT7, OPINION); Roblox lighting facts (03:RB1-RB9, FC-A) |
| C-13 | **Review the event, not the pieces.** Pose, prop silhouette, effect, camera, UI response and sound must announce the same event, agree on its importance and keep the next decision clear. Stills cannot show motion or sound: missing clip or audio = NOT REVIEWED | paper (03:CC2, CC4); one shared clarity budget per event (01:LL-06, FC-S) |
| C-14 | **Design for the real camera.** Composition, proportion and even geometry may bend for what the player sees; test every reachable viewpoint when players control the camera | Nintendo on Mario Wonder (01:SC-MW, studio account); Luca vs player-controlled cameras (01:TS-LU-L) |
| C-15 | **Phones are the target, not a shrunk desktop.** Protect identity silhouettes, semantic cues and key value relationships first; let microdetail go first. No universal phone triangle budget, light count or palette size exists | paper (04:SP2, PF3); Roblox FY2025 mobile share of DAU (04:AU1, FC-A) |
| C-16 | **Match how the owner judges.** The owner grades by look and finish at a pro bar (kit test screens: C- and B-, J009-D6); a correct, honest, readable screen can still be a C. Show 2-3 options of the same subject at one camera; the owner picks by looking. What the owner already likes is locked; test changes side by side | owner rulings (05:OR03, OR20); style test with one cast in 3-4 styles (05:AB10) |
| C-17 | **Art and rules must agree.** Soft-looking things do not stop a truck; weak-looking materials break easily; a doorway that looks open is walkable | Riot transcripts (05:AF19) |
| C-18 | **Copy relationships, never a franchise.** "Valve clarity, Riot polish" is a research agenda, not a brief. Name the relationship to transfer (which shapes carry identity, where contrast is reserved, how materials separate at the camera) and keep source characters, logos, UI and silhouettes out | paper (01:CO-3); owner rule on protected marks (05:OR32); `platform-policy` |

## 5. Rules (final check, short)
- The owner decides every lock, anchor, direction and exception. The art director proposes, compares and records; it never changes the creative brief silently.
- No universal thresholds: palette size, DeltaE, silhouette pixels, world-art contrast, exploration and review counts are project choices the owner approves or the project measures. Only scoped standards (WCAG / Xbox) apply to UI text and UI components, with the standard named.
- A measurement is evidence, not taste. Missing capture, clip or audio = NOT REVIEWED, never a pass.
- Studio precedents: say who said it (studio-published, developer account, the paper's reading). Never write "Valve's rule" or "Riot requires" for a reading.
- The art director reviews and directs; it never edits another craft's files or final assets.
- Franchise characters, logos, lettering and real brands stay out of every image and asset (`platform-policy`).

## 6. Self-check before returning
- [ ] The moment, the fantasy and the player's decision are stated before any judgment.
- [ ] Every lock or direction proposed has purpose, scope, example, failure example, test and allowed variation.
- [ ] Hierarchy is ranked for the moment; each craft's screen job is named.
- [ ] Combined frame, phone size, lowest quality and busiest scene were reviewed or marked NOT REVIEWED.
- [ ] Each precedent cited carries its provenance; no studio rule was invented.
- [ ] Owner approvals cited by decision id with the owner's words; nothing is called approved without one.

Project overlay: if `knowledge/overlays/art-direction.md` exists, read it after this file; it wins for this game.
