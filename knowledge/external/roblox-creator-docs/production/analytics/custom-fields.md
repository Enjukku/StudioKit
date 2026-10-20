---
title: Custom fields
description: Use custom fields as an additional analytics tool to track unique milestones in your game.
tags: [roblox, documentation, external-reference, priority-reference, production]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [production/analytics/custom-fields.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/analytics/custom-fields.md). Published page: [https://create.roblox.com/docs/production/analytics/custom-fields](https://create.roblox.com/docs/production/analytics/custom-fields).

You can use up to three **custom fields** to filter your [[external/roblox-creator-docs/production/analytics/economy-events|economy]], [[external/roblox-creator-docs/production/analytics/funnel-events|funnel]], and [[external/roblox-creator-docs/production/analytics/custom-events|custom]] events by unique dimensions specific to your game. Some examples include:

- Levels — 1, 2, 3, . . .
- Player class — Warrior, Mage, Archer
- Weapon type — SMG, Pistol, Rocket Launcher

The `customFields` parameter is a dictionary that lets you send up to three custom values using the provided `Enum.AnalyticsCustomFieldKeys` as keys by accessing them as `Enum.AnalyticsCustomFieldKeys.CustomField{01, 02, 03}.Name`. Anything other than `CustomField01.Name`, `CustomField02.Name`, and `CustomField03.Name` is ignored. You can have up to 8,000 unique combinations of values across the three custom fields.

<Alert severity="info">
The **values** assigned to custom fields must be **strings**. If you need to log another data type like a boolean or number, pass it in string format.
</Alert>

Using a fantasy-related game as an example, you can track an economy event regarding equipment type, player class, and level with the following:

```lua title="Tracking Custom Fields"
local AnalyticsService = game:GetService("AnalyticsService")

AnalyticsService:LogEconomyEvent(
    player,
    Enum.AnalyticsEconomyFlowType.Sink,
    "Coins", -- Currency name
    80, -- Cost
    20, -- Balance after transaction
    Enum.AnalyticsEconomyTransactionType.Shop.Name,
    "Obsidian Sword", -- Item SKU
    {
        [Enum.AnalyticsCustomFieldKeys.CustomField01.Name] = "Category - Weapon",
        [Enum.AnalyticsCustomFieldKeys.CustomField02.Name] = "Class - Warrior",
        [Enum.AnalyticsCustomFieldKeys.CustomField03.Name] = "Level - 10",
    } -- Custom field dictionary
)
```

Including the dimension name in the value is not required, but can help you remember the context later when reviewing your charts. Other keys in the `customFields` table are ignored.


## Related Files

- [[external/roblox-creator-docs/production/analytics/acquisition]] - Acquisition.
- [[external/roblox-creator-docs/production/analytics/alerts]] - Alerts.
- [[external/roblox-creator-docs/production/analytics/index]] - Analytics.
- [[external/roblox-creator-docs/production/analytics/analytics-dashboard]] - Analytics dashboard.
- [[external/roblox-creator-docs/production/analytics/insights]] - Analytics insights.
- [[external/roblox-creator-docs/production/analytics/custom-dashboards]] - Custom dashboards.
- [[external/roblox-creator-docs/production/analytics/custom-events]] - Custom events.
- [[external/roblox-creator-docs/production/analytics/demographics]] - Demographics.
- [[external/roblox-creator-docs/production/analytics/economy-events]] - Economy events.
- [[external/roblox-creator-docs/production/analytics/engagement]] - Engagement.
- [[external/roblox-creator-docs/production/analytics/error-report]] - Error Report.
- [[external/roblox-creator-docs/production/analytics/event-types]] - Event types.
- [[external/roblox-creator-docs/production/analytics/feedback]] - Feedback.
- [[external/roblox-creator-docs/production/analytics/funnel-events]] - Funnel events.
- [[external/roblox-creator-docs/production/analytics/get-started]] - Get started with analytics.
- [[external/roblox-creator-docs/production/analytics/monetization]] - Monetization.
- ...and 3 more local docs.
