---
type: template
scope: universal
status: active
updated: 2026-10-21
source: J012; owner's marketing paper, image brief (knowledge/reference/marketing/03-launch-measurement-policy-process-templates.md §6.3 TP-BRIEF); reference-images skill (manifest, families thumbnail and game-icon); rules/messages.md
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Image brief: <game> · <brief id> · <icon | thumbnail> · <date>

Workflow: `marketing-craft` (image route), `reference-images` (manifest and `art_refs.py`). The marketing agent owns the message; the art director owns the look (art bible); the owner approves the chosen concept. Copy to `knowledge/jobs/<job>/marketing/briefs/`. One brief per concept; variants of one concept share a brief.

**Rule.** Never ask the image model for a feature, reward, item or scene the game does not have, to raise click appeal. Title text is never drawn by the image model: approved wording is added afterwards in an editor and checked.

## A. Message (marketing)
| Field | Value |
| --- | --- |
| game, build version, release state | |
| destination and format | icon (square, master ≥ 512×512) / thumbnail (16:9, master 1920×1080); check the live doc on the day (`marketing-craft` references) |
| audience, language, policy limits | age bands this game allows; anything `platform-policy` restricts |
| player fantasy | the experience the player will really have (vision record line) |
| single message | what a viewer understands before reading any text |
| truth reference | gameplay captures, object references, approved art (paths) |
| promise-ledger claim id | the feature that delivers what the image shows |

## B. Picture (marketing proposes, art director checks)
| Field | Value |
| --- | --- |
| hero subject | identity, silhouette, expression, pose, scale (character anchor ids) |
| playable action | what happens and why it matters |
| environment | just enough to name the place; never hides the action |
| composition | what the eye meets first, second; camera; foreground / background |
| contrast and palette | art bible roles; how it separates from the Roblox page around it |
| text | none / exact approved wording, added after generation |
| exclusions | unreleased rewards, fake buttons, fake currency, misleading scale, unlicensed characters or logos, clutter |
| crop variants | per destination: Home tile, game page, ads tile |
| accessibility | small-size read, contrast, never color alone |
| rights | source and permission for any outside asset |

## C. Test (marketing with the analyst)
| Field | Value |
| --- | --- |
| hypothesis | which player expectation this image changes, and why that may bring better-fitting players |
| comparison | the current live image(s) and what stays unchanged |
| primary outcome | exact dashboard metric name (for example qPTR as labelled today), numerator, denominator |
| guardrails | first-play bounce, playtime, D1/D7 of the arriving cohort; policy |
| method label | Home personalization = adaptive allocation, not an A/B test; icon swap = observational |

## D. Manifest row (for `art_refs.py`)
| id | family | identity | inputs | anchors |
| --- | --- | --- | --- | --- |
| <brief-id>-a | thumbnail / game-icon | subject, action, consequence, camera, must-keep details, subject-specific "no" items (style comes from the locks) | capture or character anchor paths | |

## E. Approval and archive
| Field | Value |
| --- | --- |
| checklist file | `thumbnail-icon-checklist` copy |
| art director recommendation | |
| owner decision id | |
| asset id after upload, version, publish date | owner action |
| replaced asset and reason | |
