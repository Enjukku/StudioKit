---
title: Managed pricing
description: Managed pricing brings regional pricing and price optimization into one unified system in Creator Hub.
tags: [roblox, documentation, external-reference, priority-reference, production]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [production/monetization/managed-pricing.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/managed-pricing.md). Published page: [https://create.roblox.com/docs/production/monetization/managed-pricing](https://create.roblox.com/docs/production/monetization/managed-pricing).

**Managed pricing** is a unified system in Creator Hub that combines [[external/roblox-creator-docs/production/monetization/price-optimization|price optimization]] and [[external/roblox-creator-docs/production/monetization/regional-pricing|regional pricing]] under a single opt-in. Price optimization helps you find the right price points for your passes and developer products. Regional pricing helps you offer accessible prices to users across different economic regions.

From the **Managed Pricing** tab, you can:

- [Opt in](#opt-in-and-enroll-items) through a one-time flow for existing games.
- Review eligible items and choose what to include for Managed Pricing.
- Opt specific items in or out of automation.
- Use bulk actions to enable or disable multiple items at once.
- View past tests, upcoming tests, and revenue impact in one view. You can also reschedule tests.

## Opt in and enroll items

<Alert severity='info'>
After initial opt-in, **Managed Pricing** replaces the **Price Optimization** tab in your Creator Dashboard.
</Alert>

Managed pricing lives in the **Managed Pricing** tab under **Monetization** in Creator Hub.

To enroll a game:

1. Go to [Creations](https://create.roblox.com/dashboard/creations) and select a game.
2. Go to **Monetization** ⟩ **Managed Pricing**.
3. Complete the one-time opt-in flow. If managed pricing detects hard-coded prices in your game, you're prompted to fix them first.
4. Review eligible items and choose what to include. Use bulk actions to enable or disable multiple items at once, and opt specific items in or out of automation at any time.

After opt-in, the **Managed Pricing** tab shows past tests, upcoming tests, and reports for completed tests.

### Item eligibility and defaults

<Alert severity='warning'>
If you are already using regional pricing, your existing regional pricing items transition to managed pricing automatically.
</Alert>

- **New games and newly created items** are enrolled in Managed pricing by default. Item-level opt-out is available at any time.
- **Subscriptions, Private Servers, and Developer Servers** are regionalized automatically and don't require opt-in. Subscriptions are not included in price optimization tests.

## Price optimization

Managed pricing uses [[external/roblox-creator-docs/production/monetization/price-optimization|price optimization]] to identify better prices for passes and developer products based on signals from your own game, including demand, conversion, spend, and your game's spender penetration in specific countries. Items below the experiment-eligibility threshold for price optimization tests are unaffected.

For details on [[external/roblox-creator-docs/production/monetization/price-optimization#how-tests-work|how tests work]], the dynamic price check tool, the price review period, and the metric glossary, see [[external/roblox-creator-docs/production/monetization/price-optimization|price optimization]].

## Regional pricing

Managed pricing uses [[external/roblox-creator-docs/production/monetization/regional-pricing|regional pricing]] to adjust prices based on a user's economic location, using signals like purchasing power, currency exchange rates, and local spending behavior. Regional prices are bound between 30% and 100% of the default price.

For details on how economic location is determined, displaying regional prices in your game, and protecting in-game trades and gifts with `Class.MarketplaceService.GetUsersPriceLevelsAsync|GetUsersPriceLevelsAsync`, see [[external/roblox-creator-docs/production/monetization/regional-pricing|regional pricing]].


## Related Files

- [[external/roblox-creator-docs/production/monetization/avatar-creation-token]] - Avatar creation token.
- [[external/roblox-creator-docs/production/monetization/avatar-items]] - Avatar items.
- [[external/roblox-creator-docs/production/monetization/commerce-products]] - Commerce products.
- [[external/roblox-creator-docs/production/monetization/developer-products]] - Developer Products.
- [[external/roblox-creator-docs/production/monetization/devex-portal]] - DevEx Portal.
- [[external/roblox-creator-docs/production/monetization/tax-information]] - DevEx tax information.
- [[external/roblox-creator-docs/production/monetization/engagement-based-payouts]] - Engagement-based payouts.
- [[external/roblox-creator-docs/production/monetization/immersive-ads]] - Immersive ads.
- [[external/roblox-creator-docs/production/monetization/index]] - Monetization.
- [[external/roblox-creator-docs/production/monetization/paid-access-local-currency]] - Paid access in local currency.
- [[external/roblox-creator-docs/production/monetization/paid-access-robux]] - Paid access in Robux.
- [[external/roblox-creator-docs/production/monetization/paid-random-items]] - Paid random items policy guidelines.
- [[external/roblox-creator-docs/production/monetization/passes]] - Passes.
- [[external/roblox-creator-docs/production/monetization/price-optimization]] - Price optimization.
- [[external/roblox-creator-docs/production/monetization/private-servers]] - Private servers.
- [[external/roblox-creator-docs/production/monetization/regional-pricing]] - Regional pricing.
- ...and 7 more local docs.
