---
title: Virtual item policies
description: Summarizes Roblox's policy for offering virtual items in an experience.
tags: [roblox, documentation, external-reference, priority-reference, production, monetization]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [production/monetization/virtual-items.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/virtual-items.md). Published page: [https://create.roblox.com/docs/production/monetization/virtual-items](https://create.roblox.com/docs/production/monetization/virtual-items).

> [!warning] Not in the current upstream docs
> Not published in [github.com/Roblox/creator-docs](https://github.com/Roblox/creator-docs) as of 2026-10-20 (revision `74006430`). It has no successor page. Kept locally for reference only; treat it as possibly outdated.

Due to regulations in various countries, certain restrictions may apply to virtual items offered through in‑experience currency or Robux.

## Randomized virtual items

Under Roblox's [Terms of Use](https://en.help.roblox.com/hc/en-us/articles/115004647846-Roblox-Terms-of-Use), if you offer randomized virtual items that users can purchase with Robux or other in-experience currency, you must indicate all the **actual numerical odds** of what they may receive. For example, if a user has the opportunity to purchase a magic charm that has the random chance to have either a common, rare, epic, or legendary status, you must disclose the odds of their potential award **before they spend Robux**.

<img src="../../assets/monetization/earning/Virtual-Items-Odds.png" width="680" />

<Alert severity="warning">
This policy also applies to **indirect** purchases. For example, if a user uses their Robux to purchase a seed, then later plants the seed in exchange for a randomized virtual item, you must disclose the odds of their potential award **before they plant the seed.**
</Alert>

<Alert severity="info">
If your experience offers randomized virtual rewards in exchange for completing an action that does <strong>not</strong> involve the payment of Robux or other in-experience currency, you aren't required to disclose the odds. For example, if a user locates a key that opens a treasure chest, you don't need to state the odds of what items they might receive from the treasure chest.
</Alert>

## Per-player regulations

To help you determine, per player, how to handle virtual items in your experience, utilize the `Class.PolicyService:GetPolicyInfoForPlayerAsync()` method. Specifically, the structure of the returned dictionary includes:

- `ArePaidRandomItemsRestricted` &mdash; When `true`, the player can **not** interact with paid random item generators, either via in‑experience currency bought with Robux or Robux directly.
- `IsPaidItemTradingAllowed` &mdash; When `true`, the player can trade virtual items that they purchased with in‑experience currency or Robux.


## Related Files

- [[external/roblox-creator-docs/production/monetization/avatar-creation-token]] - Avatar creation token.
- [[external/roblox-creator-docs/production/monetization/avatar-items]] - Avatar items.
- [[external/roblox-creator-docs/production/monetization/commerce-products]] - Commerce products.
- [[external/roblox-creator-docs/production/monetization/developer-products]] - Developer Products.
- [[external/roblox-creator-docs/production/monetization/immersive-ads]] - Immersive ads.
- [[external/roblox-creator-docs/production/monetization/index]] - Monetization.
- [[external/roblox-creator-docs/production/monetization/paid-access-local-currency]] - Paid access in local currency.
- [[external/roblox-creator-docs/production/monetization/paid-access-robux]] - Paid access in Robux.
- [[external/roblox-creator-docs/production/index]] - Production.
