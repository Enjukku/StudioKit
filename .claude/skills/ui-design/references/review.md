---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "J002; research paper RP §11-12 via knowledge/reference/ui/06a §4, 06b §5 (22 checks, do-not list, failure modes)"
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20

# Reviewing a screen

Each check is PASS, FAIL or UNVERIFIED, with the capture or test. **UNVERIFIED is not PASS.** Never write "looks AI-generated"; name the failure (§3).

## 1. The 22 checks (RP §12; untagged rows are the paper's OPINION gates, V marks a verified rule)
| # | Check | Pass when |
| --- | --- | --- |
| 01 | Context | device, build, input, locale, scale recorded |
| 02 | Text size | meets the declared text rubric (default 11 pt font size, screen-contract §5; if XAG is chosen, rendered glyph height, V U12) |
| 03 | Text enlargement | 200 % with no lost content (V U12) |
| 04 | Contrast | 4.5:1 / 3:1 large / 7:1 high-contrast, weakest background (V U13) |
| 05 | Touch | declared rubric met; no overlapping hit areas |
| 06 | Safe areas | nothing required under cutouts or Roblox chrome |
| 07 | Digital navigation | every action reachable with gamepad / keys |
| 08 | Focus | one clear target; no focus behind an open modal |
| 09 | State semantics | selected / owned / equipped / pending / success distinguishable |
| 10 | Busy HUD | no essential signal pushed out by lower priority |
| 11 | Critical cues | nothing critical by colour only (V U18) |
| 12 | Captions | essential audio events have a visual equivalent |
| 13 | Motion provenance | every timing / easing / scale has a source or PROPOSAL tag |
| 14 | Motion completeness | all handoff fields filled before release |
| 15 | Reduced motion | same meanings in the reduced variant |
| 16 | Temporal safety | flashing checked over time, not from a still (V U20) |
| 17 | Localisation | price, conditions, names never clipped |
| 18 | Paid randomness | odds total 100 %, rounding explained (V R14) |
| 19 | Price and grant | shown price = charge; ownership confirmed before celebration |
| 20 | Advertising | no rewarded-ad path for under-13 players; format eligibility checked |
| 21 | First-session learning | unprompted core action tested; threshold set before the test |
| 22 | Real-device performance | claims backed by phone measurements |

## 2. Do not (RP §12)
infer a rule from a flourish · remove a shortcut for a cleaner layout · treat your icon preference as player meaning · add more equal-priority statuses than the HUD can explain · turn "feels better" into invented % · equate longer sessions or more openings with better UX · use promo screenshots as specs · call one fade constant a studio preset · force repeated spectacle · celebrate when a prompt closes · hide odds behind a bare ⓘ · use old blanket ad age rules · use colour, sound or animation as the only cue · shrink translations to fit an English box · treat emulator memory as a phone benchmark.

## 3. Failure modes in AI-made UI (O)
Generic panels unrelated to the game · too much text · weak grouping · tiny controls · wrong apparent scale · flat state feedback · many animations at once. Diagnose each as: style-role mismatch · failed comprehension · target geometry too small · hidden urgency · missing acknowledgement · motion or performance failure.

## 4. Which evidence proves what (O)
| Evidence | Can support |
| --- | --- |
| still screenshot | layout, some contrast, content |
| recording | sequence, focus, interruption |
| real interaction | hit testing |
| profiler on a phone | performance |
| real players | comprehension |
| live analytics | how often, at scale |
A simulated user (another model) is not player evidence.

## 5. Self-review captures for every visual hand-back
At real size: phone, tablet, PC (and TV if console is supported) · grayscale · longest text / biggest number · every state in the spec · next to the style book's reference picture. Look for: elements touching or overlapping that were not designed to; layers showing through popups (counters, labels); variants of one state that use different marks (e.g. only some pending buttons show the spinner); focus rings, glows or break-out art cut flat by a parent frame (zoom to 2× on every focused control; J002-T09 popups clipped every focus ring); shine bars outlined by a stray stroke. Label each check: gate-verified / MCP-verified (say Figma or Studio) / owner-confirmed / not verified (AGENTS.md §3).
