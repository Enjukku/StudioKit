---
title: Event types
description: Overview of using event types to track user sources, sinks and milestones in your game.
tags: [roblox, documentation, external-reference, priority-reference, production]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [production/analytics/event-types.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/analytics/event-types.md). Published page: [https://create.roblox.com/docs/production/analytics/event-types](https://create.roblox.com/docs/production/analytics/event-types).

<iframe width="880" height="495" src="https://www.youtube-nocookie.com/embed/NFLP-FVv834" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowFullScreen></iframe>

Event types help you identify opportunities to grow and monetize your game. They allow you to integrate event tracking into your game and visualize your in-game economy and player usage patterns on the Analytics dashboard

After you begin tracking these events from your game using `Class.AnalyticsService`, you unlock new [[external/roblox-creator-docs/production/analytics/economy-events|economy]], [[external/roblox-creator-docs/production/analytics/funnel-events|funnel]], and [[external/roblox-creator-docs/production/analytics/custom-events|custom]] dashboards under Analytics on the Creator Dashboard. You can use these dashboards to identify growth opportunities and segment users by age, gender, platform, OS and custom fields. All of these features are **free to use**.

<img src="../../assets/analytics/event-types/Overview-Economy-Funnels.png" alt="Economy and Funnels dashboard pages populated with data."/>

## Event types

Roblox provides three sets of analytic dashboards you can use to track different aspects of your game:

1. **Economy events** let you track your in-game economy, such as:

   - **Top sinks** — What do users spend in-game resources on?
   - **Top sources** — Where do users earn resources?
   - **Average wallet balance** — How many resources are users holding?

2. **Funnel events** let you track your user's progress through key stages of your game, such as:

   - **Onboarding** — Where do users drop off when getting started with your game?
   - **Progression** — Where do users stop advancing through your game?
   - **Shop** — Where do users abandon purchases?

3. **Custom events**  let you track metrics specific to your game, such as:

   - **Adoption** — How many users click on a specific UI component?
   - **User behavior** — What is the most frequently used ability on each map?
   - **Core loop** — How do kill/death ratios compare across different weapons?

For more information on setting up these dashboards, see [[external/roblox-creator-docs/production/analytics/economy-events|Economy events]], [[external/roblox-creator-docs/production/analytics/funnel-events|Funnel events]] and [[external/roblox-creator-docs/production/analytics/custom-events|Custom events]].

## Validate your event tracking

Once you add [[external/roblox-creator-docs/production/analytics/economy-events|economy]], [[external/roblox-creator-docs/production/analytics/funnel-events|funnel]], or [[external/roblox-creator-docs/production/analytics/custom-events|custom]] events to your game, charts on the respective pages typically take 24 hours to appear. In the meantime, you can check if events are set up correctly using the **View Events** tool:

1. Navigate to the **Economy**, **Funnel**, or **Custom** pages of your Analytics dashboard for your game.
2. Click the **View Events** button at the top of each page. A near real-time list of the most recent events displays.
3. Refresh the page to update the list.

<img src="../../assets/analytics/event-types/Event-Tracking.png" alt="View events report displaying multiple event entries sortable by event type, user ID and keyword."/>

If you see more events than you were expecting, verify that your calls to the `Class.AnalyticsService` methods occur **after** a successful operation. For example, you should call `Class.AnalyticsService:LogEconomyEvent()|LogEconomyEvent()` after a successful purchase, not when the user attempts a purchase (which could fail due to lack of funds).

You can also visit your game's [[external/roblox-creator-docs/production/analytics/error-report|error report]] to see if there are any errors with your event tracking.

## Event tracking limitations

The following limitations apply when tracking your events with `Class.AnalyticsService`. Limitations reset daily. You will be able to send new events the next day once you stop sending previous events. Each event remains visible on the Creator Dashboard and automatically rolls off after 90 days from the last data received.

<Alert severity = 'warning'>
You can leverage [[external/roblox-creator-docs/production/analytics/custom-fields|custom fields]] to additionally filter your analytic events.

For example, instead of tracking `WarriorXP`, `MageXP`, `PaladinXP` as separate economy currencies, set `XP` as one currency and set `Warrior`, `Mage`, `Paladin`, `...`, as Custom Field 1. This allows you to break down these values on your dashboards and not use up your currency cardinality.
</Alert>

<table><thead>
  <tr>
    <th></th>
    <th>**Limitation**</th>
    <th>**Maximum value**</th>
    <th>**Examples**</th>
  </tr></thead>
<tbody>
  <tr>
    <td rowspan="1">Global Rate Limit</td>
    <td>Total `Class.AnalyticsService` requests per minute</td>
    <td>120 + (20 * CCU)</td>
    <td></td>
  </tr>
  <tr>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  </tr>
  <tr>
    <td rowspan="2">Economy, Funnel, and Custom events</td>
    <td>Number of [[external/roblox-creator-docs/production/analytics/custom-fields|custom fields]]</td>
    <td>3</td>
    <td>Class, Level, Weapon</td>
  </tr>
  <tr>
    <td>Unique values per [[external/roblox-creator-docs/production/analytics/custom-fields|custom field]]</td>
    <td>Unlimited — After 8,000 combined values across all custom fields, values will be grouped as "Other"</td>
    <td>Warrior, Mage, Archer</td>
  </tr>
  <tr>
    <td rowspan="3">Economy only</td>
    <td>Resource types</td>
    <td>10</td>
    <td>Coins, Gold, Credits</td>
  </tr>
  <tr>
    <td>transactionTypes</td>
    <td>Unlimited — After 20, values will be grouped as "Other"</td>
    <td>IAP, Gameplay</td>
  </tr>
  <tr>
    <td>itemSkus</td>
    <td>Unlimited — After 100, values will be grouped as "Other"</td>
    <td></td>
  </tr>
  <tr>
    <td rowspan="2">Funnel only</td>
    <td>Number of funnels</td>
    <td>10</td>
    <td>Onboarding, Shop</td>
  </tr>
  <tr>
    <td>Steps per funnel</td>
    <td>100</td>
    <td>Step 1, Step 2, Step 3</td>
  </tr>
  <tr>
    <td rowspan="3">Custom only</td>
    <td>eventNames</td>
    <td>100</td>
    <td>MonsterDefeated, KillDeathRatio, PetAdoption</td>
  </tr>
</tbody>
</table>


## Related Files

- [[external/roblox-creator-docs/production/analytics/acquisition]] - Acquisition.
- [[external/roblox-creator-docs/production/analytics/alerts]] - Alerts.
- [[external/roblox-creator-docs/production/analytics/index]] - Analytics.
- [[external/roblox-creator-docs/production/analytics/analytics-dashboard]] - Analytics dashboard.
- [[external/roblox-creator-docs/production/analytics/insights]] - Analytics insights.
- [[external/roblox-creator-docs/production/analytics/custom-dashboards]] - Custom dashboards.
- [[external/roblox-creator-docs/production/analytics/custom-events]] - Custom events.
- [[external/roblox-creator-docs/production/analytics/custom-fields]] - Custom fields.
- [[external/roblox-creator-docs/production/analytics/demographics]] - Demographics.
- [[external/roblox-creator-docs/production/analytics/economy-events]] - Economy events.
- [[external/roblox-creator-docs/production/analytics/engagement]] - Engagement.
- [[external/roblox-creator-docs/production/analytics/error-report]] - Error Report.
- [[external/roblox-creator-docs/production/analytics/feedback]] - Feedback.
- [[external/roblox-creator-docs/production/analytics/funnel-events]] - Funnel events.
- [[external/roblox-creator-docs/production/analytics/get-started]] - Get started with analytics.
- [[external/roblox-creator-docs/production/analytics/monetization]] - Monetization.
- ...and 3 more local docs.
