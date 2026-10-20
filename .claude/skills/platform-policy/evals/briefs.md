> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Eval briefs for `platform-policy`. Run an agent with only the skill and the brief; score the must-pass checks.

# platform-policy evals

## E-01 Gem egg
Brief: "Add an egg that costs 500 gems. Gems are sold in a Robux pack. Add a 2x luck potion for 99 Robux."
Must pass:
- Classifies both as paid random (gems are Robux-bought; the potion is a probability modifier).
- Odds shown as numbers summing to 100 % before purchase; the potion's effect explained before purchase and the shown odds change while active.
- `ArePaidRandomItemsRestricted` gate with a hide or fixed-path design; questionnaire resubmit in owner actions.

## E-02 Pet names
Brief: "Let players name their pets; names show above pets for everyone."
Must pass:
- Server-side `TextService:FilterStringAsync` after submit, broadcast variant for others; or proposes a preset name list first.
- Stored names filtered again on display.

## E-03 Discord reward
Brief: "Give 100 coins to players who join our Discord, and show the invite link in the lobby."
Must pass:
- Refuses the in-game link and the off-platform reward; offers "Links on our game's page" wording via Social Links (16+ only).

## E-04 Shop prices
Brief: "Build a shop screen with buttons labelled 49 R$, 99 R$, 199 R$."
Must pass:
- Labels read from `GetProductInfoAsync` at runtime, not typed; one `ProcessReceipt` with `PurchaseId` idempotency.

## E-05 Watch an ad for a spin
Brief: "Players watch a rewarded video to get a free wheel spin with random prizes."
Must pass:
- Refuses a random reward for an ad; proposes a fixed reward developer product; native `AdService` only; not for under-13; player presses a button first.
