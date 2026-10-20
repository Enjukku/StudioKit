---
title: LiveOps planning
description: LiveOps Essentials is an overview of what live ops are and how to think about designing them effectively.
tags: [roblox, documentation, external-reference, priority-reference, production]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [production/game-design/liveops-planning.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/game-design/liveops-planning.md). Published page: [https://create.roblox.com/docs/production/game-design/liveops-planning](https://create.roblox.com/docs/production/game-design/liveops-planning).

[[external/roblox-creator-docs/production/game-design/liveops-essentials|LiveOps]] maintain a dynamic and captivating game through releasing two interweaving content types:

- **Events:** Temporary activities like contests and promotions that complement the [[external/roblox-creator-docs/production/game-design/core-loops|core loop]]. Events offer rewards like exclusive items, status, or currency to maintain player interest between larger content releases.
- **Content updates:** Significant permanent game updates that expand or deepen the core loop. Larger content releases provide robust new content for players to enjoy. To learn more about content updates, see [[external/roblox-creator-docs/production/game-design/content-updates|Content updates]].

To initiate and execute a continuous LiveOps plan, consider how you will:

- **Plan:** Define your objectives and methods for achieving them.
- **Communicate:** Determine how to inform players about upcoming events.
- **Monitor and analyze:** Evaluate player involvement and the event's success in meeting objectives and assess the event's effectiveness post-completion.

## Plan

When designing LiveOps for your game, consider your **key performance indicators** (KPIs). Determine which metric you want to impact, like daily active users. It's crucial to acknowledge that events typically influence several KPIs simultaneously.

When planning for KPI objectives, consider the following:

- **Player actions:** Clarify the intended player actions during the event and the KPIs these actions will likely influence.
- **Player impact:** Consider how increased player interaction with certain events might alter the usual patterns of earning or buying in-game currencies and items. An event like a fishing tournament exposes players to a key currency-earning part of the game and likely yields significant engagement, but the type of reward players receive has to be intentionally designed to not negatively impact the game's economy.

To learn more about KPIs, see [[external/roblox-creator-docs/production/game-design/analytics-essentials|Analytics essentials]].

<figure>
    <img src="../../assets/game-design/live-ops-planning/live-ops-planning.png" width="70%"/>
    <figcaption>Fishing tournament in *Overlook Bay 2*</figcaption>
  </figure>

## Communicate

When designing LiveOps for your game, consider how to inform players about your event:

- **External communication:** Consider how to alert players to your game's event outside of the game itself. Think about what social media platforms or community tools you can leverage to increase awareness.
- **Internal communication:** Decide on the method of notifying players in your game about the event. Compare different options, from utilizing pop-up messages when they log in, to integrating an alert into the UI or displaying it prominently in the game lobby.
- **Communication timing:** Think about when you'll communicate the event to players.
  - Communicating the event in advance encourages players to schedule their return at the event time and can maximize participation.
  - Waiting until just before the event begins can show spontaneity and can be effective in certain situations, but runs the risk of being overlooked if your players are busy with other options.

<figure>
    <img src="../../assets/game-design/live-ops-planning/live-ops-communication.png" width="70%"/>
    <figcaption>Event Communication in *World//Zero*</figcaption>
  </figure>

After deciding how to communicate your event to players, be intentional with designing what happens in the game after the event starts. Is the event limited to a certain space within the game, or is the event game-wide?

> Take the time to design an impactful and memorable start to an event to inspire players and ensure sure they're excited about the event, will want to engage with it, and keep coming back after the event is over.

## Monitor and analyze

When designing LiveOps for your game, monitor your game effectively by accessing comprehensive data, such as the sources of and spending of your game's currency and other relevant resources. Integrate tracking into your game's design to understand how players interact with your features.

For more about monitoring the impact your events have on your economy, see [[external/roblox-creator-docs/production/game-design/balance-virtual-economies|Balance virtual economies]].

When tracking data, make sure it's:

- **Timely:** Having quick access to data is essential for fine-tuning and ensuring your event is successful. Seeing hourly, same-day data to confirm that an event is not granting too many prizes and that players are able to accomplish what you're asking them to accomplish is crucial.
- **Comparable:** Since events take place during a limited period of time, it's important to actively compare data collected during the event with data from non-event periods to determine whether its impact is greater or less than your intended goals.

Comparing your event's data to the week before the event and the week after helps you understand whether the event had a lasting impact on typical in-game activity or KPIs. KPIs that can give you insight into an event's success are:

- An increase in short and longer term retention during and after the event.
- A boost in item and currency sales during and after the event.

If the event had a lasting impact, determine whether it was positive or negative, and if your findings impact how you'll design future events to achieve your desired outcome.

For additional information and best practices on how to design optimal events, see [[external/roblox-creator-docs/production/game-design/liveops-essentials|LiveOps essentials]].


## Related Files

- [[external/roblox-creator-docs/production/game-design/analytics-essentials]] - Analyze and experiment.
- [[external/roblox-creator-docs/production/game-design/balance-virtual-economies]] - Balance virtual economies.
- [[external/roblox-creator-docs/production/game-design/content-updates]] - Content updates.
- [[external/roblox-creator-docs/production/game-design/contextual-purchases]] - Contextual purchases.
- [[external/roblox-creator-docs/production/game-design/core-loops]] - Core loops.
- [[external/roblox-creator-docs/production/game-design/design-for-roblox]] - Design for Roblox.
- [[external/roblox-creator-docs/production/game-design/index]] - Design games on Roblox.
- [[external/roblox-creator-docs/production/game-design/introduction-to-quest-design]] - Introduction to quest design.
- [[external/roblox-creator-docs/production/game-design/liveops-essentials]] - LiveOps essentials.
- [[external/roblox-creator-docs/production/game-design/monetization-foundations]] - Monetization foundations.
- [[external/roblox-creator-docs/production/game-design/onboarding]] - Onboarding.
- [[external/roblox-creator-docs/production/game-design/onboarding-techniques]] - Onboarding techniques.
- [[external/roblox-creator-docs/production/game-design/prototyping]] - Prototyping.
- [[external/roblox-creator-docs/production/game-design/season-pass-design]] - Season pass design.
- [[external/roblox-creator-docs/production/game-design/starter-pack-design]] - Starter pack design.
- [[external/roblox-creator-docs/production/game-design/subscription-design]] - Subscription design.
- ...and 1 more local docs.
