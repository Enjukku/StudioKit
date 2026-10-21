---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "J002; research paper RP via knowledge/reference/ui/05a (RA-66..83), 05b (T05-T11, T15), 06a (records 14-18)"
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20

# Shops, rewards and onboarding

Binding platform rules live in the `platform-policy` skill; load it for any of these screens (AGENTS.md §2). This file is the UX side.

## 1. Offer contract (T08, O)
Each offer card shows or links: what you get · quantity · duration (if any) · price + currency (Robux price read from `MarketplaceService`, never typed; ui-basics U-07) · eligibility · random or not · purchase limits · what happens after. Preview and commit are separate actions. A card hiding ownership, real cost or duration is incomplete (RA-77). Owned and equipped items say so on the card.

## 2. Purchase state machine (T09, O + V R22)
`inspect → review → commit → pending → confirmed | failed → recovered`
| State | Must show | Must not |
| --- | --- | --- |
| inspect | item, what it does, odds button if random | buy on a single accidental tap of a big card |
| review | price, currency, terms, balance after | hide the price in art |
| commit | a deliberate button; then disable repeat commits | double charge on a second tap |
| pending | visible waiting state (spinner or label) | look like success |
| confirmed | ownership + celebration (only now) | celebrate when the prompt merely closed (V R22) |
| failed | plain reason + retry or back | a celebration, or an item that seems owned |
| recovered | where the player lands, focus restored | a dead end |

Young audience: a free reward claim must never look like a purchase (RA-15).

**Robux products (PROPOSAL flow).** Roblox's own purchase prompt is the review + commit step. A non-random Robux item: Buy opens Roblox's prompt directly (no second confirm of ours). A paid random item: our odds-and-review popup first (odds before commit), then Roblox's prompt. Coin purchases: our review popup is the review step. Pending lasts until the server confirms the grant (`ProcessReceipt`), not until the prompt closes.

## 3. Paid random items (V R14; placement O)
- Before purchase: every possible final outcome and its real numeric % odds; player-specific remaining outcomes and paid modifiers when they apply; totals 100 % (rounded display allowed with a disclaimer).
- Odds open from a **labelled** control ("Odds", "Chances"), not a bare ⓘ icon.
- Restricted users (PolicyService) get an eligible alternative or the paid-random path is blocked.
- Disclosure before commit, not inside the reveal. A rare-looking frame is not an explanation of odds.
- No fake perpetual discounts, false scarcity or misleading countdowns; regional prices differ, so show live product info (V R15-R16, R21).
- **Pity or a guarantee inside a batch.** When a hard pity falls inside a ×10, say which roll it changes before commit: Review "Summon n of 10 is a sure <unit>"; odds panel "Your next summon: <unit> 100 %" when the count is at max − 1 (platform-policy: odds that change while a modifier is active must show the changed odds; J002-T09).
- Label words: "Odds", "Chances" (plain for kids) or `platform-policy`'s "Info" / "Details" are all fine when the control clearly opens the odds.
- **Mixed economy.** If a soft currency can be bought with Robux, random items bought with it are paid random too (R14 covers indirectly purchased currencies), so restricted players can lose the whole egg shop. Patterns (PROPOSAL; the economy designer and the policy owner decide): (a) two currencies: an earned-only one for random items, a bought one for fixed-price items; (b) a fixed-price alternative screen for restricted players. Put the choice in the owner's digest; never decide it in the UI.

## 4. Ads (V R17-R19, P04, as of the paper's stated date 2026-10-21; conflict open)
Personalised ads none under 18; no rewards for under-13 ad engagement; Rewarded Video 13+. Some non-rewarded formats are all-age since 2026-05-04, but one Ad Standards example still lists under-13 as ineligible: resolve per format with the policy owner, never invent an age gate. Reserve space for the ad label and a fallback; core progress never depends on an ad.

## 5. Reward and rarity reveals (T15, records 14-16, O; E seeds)
Order (proposed): opening accepted → outcome confirmed (server) → anticipation → rarity signal (colour **plus** text or shape) → item name and quantity readable → ownership settled → back to play. Rules: skip reaches the same confirmed result; batch rewards end on a full inspectable summary (Hearthstone mass opening, E M09); never imply tap speed or holding changes odds unless it really does; anticipation looks and lasts **the same for every rarity**, and the reveal goes straight to the real rarity (no fake-out: never gold first, then down to Rare; J002-T09); a hold-to-open needs a non-hold equivalent. Size the celebration to the consequence; routine rewards stay quiet (RA-96).

## 6. Onboarding (T05-T07, O; V U01)
- Tutorials help or hurt by game and outcome (randomised study, 45,000 players: more playtime in one game, lower return in another; V U01). Do not assume a tutorial helps; test it.
- Per lesson write: the action the player must perform · the world cue · the UI cue · the feedback · the recovery if missed. Teach what / how / why (E U03), never during heavy action.
- A lesson counts when the player repeats it **unprompted** (RA-73).
- First-session plan: first meaningful goal · first success · first reward · first voluntary repeat · first optional system. Shop introduction timing is unspecified: introduce it after the player understands the currency and the benefit, then test.
- Funnel to instrument (with the `analytics` skill): first controllable moment → core action attempted → first success → unprompted repeat → first meaningful reward → free-play choice → return. Separate crashes, skips and misunderstandings.
