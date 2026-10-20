---
title: Acquisition
description: Explains how to interpret and improve acquisition metrics for your game.
tags: [roblox, documentation, external-reference, priority-reference, production]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [production/analytics/acquisition.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/analytics/acquisition.md). Published page: [https://create.roblox.com/docs/production/analytics/acquisition](https://create.roblox.com/docs/production/analytics/acquisition).

**Acquisition** measures where new and returning users are coming from and how well they convert.

When acquiring users to your game, such as announcing an in-game event or creating ad campaigns, make sure your game has good [[external/roblox-creator-docs/production/analytics/retention|retention]] and [[external/roblox-creator-docs/production/analytics/engagement|engagement]].

## View acquisition metrics

To view your game's acquisition analytics:

1. Navigate to your [Creations](https://create.roblox.com/dashboard/creations) page on **Creator Dashboard** and select your game.
1. In the **Analytics** menu on the left, select **Acquisition**.

You can view analytics for individual or group owned game. To view the latter, you need to have [[external/roblox-creator-docs/production/analytics/analytics-dashboard|group permissions for analytics]].

## Acquisition sources

On the acquisition dashboard, you'll see the following charts and tables:

- New users with play per source
- New users with impressions per source
- Returning users with plays per source
- Returning users with impressions per source
- Play through rate
- Cumulative new users funnel

Here's a list of all the available acquisition sources:

<table>
  <tr>
    <th>Source</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Home recommendations</td>
    <td>**Recommended Experiences** section on **Home**</td>
  </tr>
  <tr>
    <td>Continue play</td>
    <td>**Continue Play** on **Home**</td>
  </tr>
  <tr>
    <td>Today's Picks</td>
    <td>**Today's Picks** on **Home**</td>
  </tr>
  <tr>
    <td>Home other</td>
    <td>**Favorites** and all other traffic on **Home**</td>
  </tr>
  <tr>
    <td>Friends</td>
    <td>**Friend Activity** section on **Home**</td>
  </tr>
  <tr>
    <td>Search</td>
    <td>Organic traffic from **Search** results and **Recommended Experiences** on **Experience Details** page</td>
  </tr>
  <tr>
    <td>Charts</td>
    <td>**All sorts** on **Charts**</td>
  </tr>
  <tr>
    <td>Sponsored ads</td>
    <td>Acquisition from [[external/roblox-creator-docs/production/promotion/ads-manager|sponsored experiences]] and **Sponsored Takeovers** on **Home**</td>
  </tr>
  <tr>
    <td>Search ads</td>
    <td>Acquisition from [[external/roblox-creator-docs/production/promotion/ads-manager|search ads]]</td>
  </tr>
  <tr>
    <td>Portal ads</td>
    <td>Acquisition from [[external/roblox-creator-docs/production/monetization/immersive-ads#portal-ads|portal ads]]</td>
  </tr>
  <tr>
    <td>Teleport</td>
    <td>Traffic coming from another game through [[external/roblox-creator-docs/projects/teleport|teleporting]]</td>
  </tr>
  <tr>
    <td>Other</td>
    <td>All other traffic with unknown sources or can't be attributed, including the traffic from external sources</td>
  </tr>
</table>

<Alert severity="info">
If your game has [[external/roblox-creator-docs/production/publishing/publish-games-and-places#audience|Exclude from Recommendations]] enabled, all other analytics remain available, but **Home recommendations** metrics are zero; games excluded from recommendations aren't included in **Recommended For You**, so they can't receive any traffic from it.
</Alert>

## Acquisition attribution

You can view the acquisition dashboard by [acquisition source](#acquisition-sources) or by [[external/roblox-creator-docs/production/promotion/share-links|share links]]. The dashboard categorizes results for both views as follows:

<table>
  <tr>
    <th>Attribution</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Users with plays</td>
    <td>Unique new users with plays on the game.</td>
  </tr>
  <tr>
    <td>Conversion rate</td>
    <td>Percent of new users who played your game after viewing an impression.</td>
  </tr>
  <tr>
    <td>D7 retention</td>
    <td>Percentage of new players acquired in the date range who played again on the 8th day (D8) after their first session ended.</td>
  </tr>
  <tr>
    <td>7D playtime per user (cumulative)</td>
    <td>Cumulative playtime for new players acquired in the date range in their first 7 days divided by the number of new players acquired in the date range.</td>
  </tr>
  <tr>
    <td>30D payer conversion (cumulative)</td>
    <td>Number of paying users from new players acquired in the date range in their first 30 days divided by the number of new players acquired in the date range.</td>
  </tr>
  <tr>
    <td>30D revenue per user (cumulative)</td>
    <td>Cumulative revenue, excluding subscriptions, engagement payouts, and immersive ads, for new players acquired in the date range in their first 30 days divided by the number of new players acquired in the date range.</td>
  </tr>
</table>

<img src="../../assets/analytics/acquisition/New-Users-Funnel.png" width= "100%" alt="Chart indicating new users funnel by acquisition source."/>

## Improve acquisition

To improve acquisition, you can run an acquisition funnel to identify sources that might drive more traffic or convert better, such as:

- The sources driving **the most number of new users** to your game.
- The sources with the best **end-to-end conversion rate**.

### Improve acquisition from Roblox sources

Among all Roblox sources, **Home** is usually where the vast majority of users find games. To improve your game's discovery on Home:

1. **Improve engagement and retention.** Get your [[external/roblox-creator-docs/production/analytics/engagement#improve-average-session-time|session time]] and [[external/roblox-creator-docs/production/analytics/retention#improve-day-1-retention|day 1 retention]] to be comparable or above your similar game benchmarks. The algorithm cares about these metrics because they signal how engaging and satisfying your game is for users.
2. **Optimize monetization.** Get your [[external/roblox-creator-docs/production/analytics/monetization#improve-payer-conversion-rate|payer conversion]] rate and [[external/roblox-creator-docs/production/analytics/monetization#improve-average-revenue-per-paying-user-arppu|ARPPU]] (average revenue per paying user) to be comparable or above your similar game benchmarks. The algorithm cares about these metrics because they measure how invested users are in your game.

<img src="../../assets/analytics/acquisition/Unique-Users-by-Source.png" width= "100%" alt="An example shows the statistics by unique users with impressions and unique users with plays by source." />

You can adopt the following strategies to improve the number of users visiting your game from Roblox sources, including **Home**, **Discover**, and **Search**:

1. **Improve your retention**: Day 1 retention signals how engaging and satisfying your game is for users. Games with high Day 1 retention are more likely to be featured in **Recommended Experiences**. For more information on improving Day 1 retention, see [[external/roblox-creator-docs/production/analytics/retention#improve-day-1-retention|Day 1 retention]].

2. **Grow your engagement**. Average session time measures how much time users spend in your game and signals how much users enjoy your content. Games with high average session time are more likely to be featured in **Recommended Experiences**.

For more information on Roblox sources and best practices on improving the discovery of your game, see [[external/roblox-creator-docs/discovery|Discovery]].

### Improve play through rate from Roblox sources

You can get more users to convert by making your game metadata engaging and accurate:

1. **Use a title, description, and icon** that's true and unique to your game.
2. **Add images and videos** to your game detail page to engage users.

<img src="../../assets/analytics/overview/step2.png" width="100%"/>

## Improve acquisition from external sources

Here are some tips to get users to visit your game from external sources:

1. **Create social accounts and post regularly**: Add social accounts such as Twitter, YouTube, and Instagram to your Roblox Game Detail Page. Share regular updates, teasers, and screenshots to build buzz for your game. Reply to other large social accounts to grow your following.
2. **Create a user community**: Users in your community can share feedback, suggestions, bug reports, fan art, and more. Engage with your community regularly by hosting events and replying to comments and suggestions.
3. **Partner with other creators and influencers**: You can partner with other creators who make similar games to grow together. You can also reach out to influencers who have large followings on platforms like YouTube or Twitch to see if they're willing to use or review your game.
4. **Create [[external/roblox-creator-docs/production/promotion/share-links|share links]]**: Track your off-platform user acquisition and use the **New users funnel** table to understand:
   - **Users with qualified plays**: How many new users are joining from each link?
   - **7-day playtime per user**: Which links are bringing in users who engage the most?
   - **D7 retention**: Which platforms drive users that keep coming back?
   - **30-day revenue per user**: Which channels are attracting users who spend in-game?

<img src="../../assets/analytics/acquisition/Share-Link-Acquisition-Dashboard.png" width= "100%" alt="Chart indicating new users funnel by share links."/>


## Related Files

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
- [[external/roblox-creator-docs/production/analytics/event-types]] - Event types.
- [[external/roblox-creator-docs/production/analytics/feedback]] - Feedback.
- [[external/roblox-creator-docs/production/analytics/funnel-events]] - Funnel events.
- [[external/roblox-creator-docs/production/analytics/get-started]] - Get started with analytics.
- [[external/roblox-creator-docs/production/analytics/monetization]] - Monetization.
- ...and 3 more local docs.
