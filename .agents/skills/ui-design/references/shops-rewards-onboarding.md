---
type: reference
scope: universal
status: active
updated: 2026-10-22
source: "J002; research paper RP via knowledge/reference/ui/05a (RA-66..83), 05b (T05-T11, T15), 06a (records 14-18); J018 (honest reveals, outcome feedback); platform-policy references/rules.md §§ A-D (binding)"
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Revised by J018 maker ui-ux-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (attempt and outcome in the purchase states, honest paid reveals, wording for younger players, ads as a pointer to the binding rules).

# Shops, rewards and onboarding

Binding platform rules live in the `platform-policy` skill (`references/rules.md` § A paid random items, § B purchases, § C ads, § D younger players); load it for any of these screens (AGENTS.md §2). It wins over this file. This file is the screen side.

## 1. Offer contract (T08, O)
Each offer card shows or links: what you get · quantity · duration (if any) · price + currency (Robux price read from `MarketplaceService`, never typed; ui-basics U-07) · eligibility · random or not · purchase limits · what happens after. Preview and commit are separate actions. A card hiding ownership, real cost or duration is incomplete (RA-77). Owned and equipped items say so on the card; a locked item shows its readable requirement ("Unlocks at Rebirth 3") from the progression export, and each reward's tier name comes from the tier table. The price sits on its own buy button (proximity), never in a corner of the card. Sales wording stays calm for younger players: "View Item", "See Price", "Open Shop", never "GET IT NOW" or "LAST CHANCE" (`platform-policy` § D).

## 2. Purchase state machine (T09, O + V R22)
`inspect → review → commit → pending → confirmed | failed → recovered`
| State | Must show | Must not |
| --- | --- | --- |
| inspect | item, what it does, odds control if random | buy on a single accidental tap of a big card |
| review | price, currency, terms, balance after | hide the price in art |
| commit | a deliberate button that answers on the press (attempt cue); then disable repeat commits | double charge on a second tap |
| pending | visible waiting state ("Buying…", spinner) once confirmation takes longer than about 100 ms | look like success |
| confirmed | ownership + celebration (only now), sized by the outcome | celebrate when the prompt merely closed (V R22) |
| failed | plain reason + retry or back; a declined or cancelled Roblox prompt returns quietly to the screen (a parent's spend limit can decline it for a reason the game cannot see) | a celebration, an item that seems owned, or a message that blames the player |
| recovered | where the player lands, focus restored | a dead end |

Young audience: a free reward claim must never look like a purchase (RA-15).

**Robux products (PROPOSAL flow).** Roblox's own purchase prompt is the review + commit step. A non-random Robux item: Buy opens Roblox's prompt directly (no second confirm of ours). A paid random item: our odds-and-review popup first (odds before commit), then Roblox's prompt. Coin purchases: our review popup is the review step. Pending lasts until the server confirms the grant (`ProcessReceipt`), not until the prompt closes. A not-enough-currency tap is a refusal at the button (cause and fix: "Need 40 more coins"), not a dead popup.

## 3. Paid random items (screen side of `platform-policy` § A)
§ A holds the rules (what counts as paid random, the odds disclosure and rounding, odds that change while a modifier is active or after a once-only win, restricted players, the currency-prize gamble). On the screen:
- Odds for every outcome are visible **before the buy button**, as numbers, never covered or animated by effects. A long list may open in a pop-up from a visible worded label (`platform-policy` names "Info" or "Details"; for children "Odds" or "Chances" read plainer; if I use another word, I put the policy's word beside it until the policy owner confirms it). Never a bare ⓘ.
- Disclosure before commit, not inside the reveal. A rare-looking frame is not an explanation of odds.
- **Restricted players** (`ArePaidRandomItemsRestricted`): prefer hiding the item or replacing it with an eligible alternative (a fixed-price screen, an earn-only path); a blocked button with an error message is allowed by the policy but confusing, so it is my last choice and I say so in the spec.
- **Pity or a guarantee inside a batch.** When a hard pity falls inside a ×10, say which roll it changes before commit: Review "Summon n of 10 is a sure <unit>"; odds panel "Your next summon: <unit> 100 %" when the count is at max − 1 (J002-T09).
- **Luck boosts** show their numeric effect before purchase, and the odds panel shows the boosted odds while the boost runs; sparkles never suggest more than the numbers.
- **Mixed economy.** If a soft currency can be bought with Robux, random items bought with it are paid random too, so restricted players can lose the whole egg shop. Patterns (PROPOSAL; the economy designer and the policy owner decide): (a) two currencies: an earned-only one for random items, a bought one for fixed-price items; (b) a fixed-price alternative screen for restricted players. Put the choice in the owner's digest; never decide it in the UI.
- No fake perpetual discounts, false scarcity or misleading countdowns; regional prices differ, so show live product info (V R15-R16, R21).

## 4. Ads (screen side of `platform-policy` § C)
§ C holds the rules (formats, ages, eligibility, rewards). On the screen: a rewarded ad starts only from a button the player presses, and that button states the reward before the ad; the reward is never random and arrives right after; core progress never depends on an ad; reserve space for the ad label and a fallback when no ad is available or `AreAdsAllowed` is false (the control hides or is replaced, never left dead).

## 5. Reward and rarity reveals (T15, records 14-16, O; E seeds)
Order: opening accepted → outcome confirmed (server) → anticipation → rarity signal (colour **plus** text and frame shape) → item name and quantity readable → ownership settled → back to play.
- **One windup for every result.** Anticipation looks and lasts the same for every rarity, up to the result frame; no rarity tint, shake or sound that differs before the result; the reveal goes straight to the real rarity (no fake-out: never gold first, then down to Rare; no "so close" near-miss; J002-T09).
- **The tier ladder starts after the result.** Rarer results add layers (a ring, rays, a crescendo, the game's motif; pure white only for the top tiers); a lower result never shows a higher tier's layer; a result worth less than its price is not celebrated.
- After the result is confirmed, a tap skips to it and reaches the same confirmed result. Batch rewards end on a full inspectable summary (sorted, best first; Hearthstone mass opening, E M09); in a batch only the best result gets the full ceremony.
- Never imply tap speed or holding changes odds unless it really does; a hold-to-open needs a non-hold equivalent.
- Size the celebration to the consequence; routine rewards stay quiet (RA-96); in-play celebrations end before the next decision (motion.md §8).
- Check: `review.md` §6 S-44 (the lowest tier's windup against every tier that adds a layer, frame by frame).

## 6. Onboarding (T05-T07, O; V U01)
- Tutorials help or hurt by game and outcome (randomised study, 45,000 players: more playtime in one game, lower return in another; V U01). Do not assume a tutorial helps; test it.
- Per lesson write: the action the player must perform · the world cue · the UI cue · the feedback · the recovery if missed. Teach what / how / why (E U03), never during heavy action. The UI cue is the screen's one attention motion (a slow pulse or an arrow on the control to press); everything else stays still.
- A lesson counts when the player repeats it **unprompted** (RA-73).
- First-session plan: first meaningful goal · first success · first reward · first voluntary repeat · first optional system. Shop introduction timing is unspecified: introduce it after the player understands the currency and the benefit, then test.
- Funnel to instrument (with the `analytics` skill): first controllable moment → core action attempted → first success → unprompted repeat → first meaningful reward → free-play choice → return. Separate crashes, skips and misunderstandings.
