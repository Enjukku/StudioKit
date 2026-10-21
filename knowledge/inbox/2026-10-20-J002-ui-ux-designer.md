---
type: lesson
scope: universal
status: draft
updated: 2026-10-20
source: J002-T07
supersedes: []
---
> Author: ui-ux-designer · claude-opus-5-5 · high · 2026-10-20

# J002-T07 lessons: first cartoon egg shop in Figma

| Field | Content |
| --- | --- |
| date | 2026-10-20 |
| job | J002-T07 |
| agent | ui-ux-designer |
| type | win |
| what happened | Components first (Button Role×State, Close, Coin counter, Rarity tag, Odds row/panel, Egg cards), then 8 state frames cloned from the main frame with popups on top. Cloning the finished main frame made every state consistent in one call each. Generating eggs on a flat key colour and keying them locally gave clean transparent icons with no owner step. |
| evidence link | `content/ui/egg-shop/screens/`, `content/ui/egg-shop/figma-ids.json` |
| proposed rule | Build state frames by cloning the approved main frame, then add only the overlay that differs. |

| Field | Content |
| --- | --- |
| date | 2026-10-20 |
| job | J002-T07 |
| agent | ui-ux-designer |
| type | failure |
| what happened | Binding a scrim colour to a variable reset its paint opacity to 1, so every popup frame hid the shop completely; found only in the first popup screenshot. TEXT property defaults are shared across a variant set, so all odds rows showed the same pet. |
| evidence link | `content/ui/egg-shop/skill-gaps.md` G-02, G-05 |
| proposed rule | After `setBoundVariableForPaint`, reassign opacity; set per-instance text with `setProperties`, never rely on per-variant defaults. |

| Field | Content |
| --- | --- |
| date | 2026-10-20 |
| job | J002-T07 |
| agent | ui-ux-designer |
| type | failure |
| what happened | TC tokens (outline 3, lip 4, text 22-24) disappear at the 0.347× phone check, and the grayscale check showed white utility buttons outshining the green Buy. Both fixed only because the self-review captures were taken. |
| evidence link | `content/ui/egg-shop/spec.md` §13-14; `screens/01-inspect-main-grayscale.png` |
| proposed rule | Convert every style token to phone pt before building, and take the grayscale capture before the first owner screenshot. |
