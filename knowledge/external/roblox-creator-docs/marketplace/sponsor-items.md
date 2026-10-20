---
title: Sponsored items
comment: Changes to this article require additional review
description: Sponsoring items allows you to increase the discoverability of 3D user-generated content within the Marketplace.
tags: [roblox, documentation, external-reference, priority-reference, marketplace]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [marketplace/sponsor-items.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/marketplace/sponsor-items.md). Published page: [https://create.roblox.com/docs/marketplace/sponsor-items](https://create.roblox.com/docs/marketplace/sponsor-items).

Sponsor items to increase the discoverability of your 3D user-generated content to users within the [Marketplace](https://www.roblox.com/catalog). You can choose your audience, schedule the duration of your ad, and specify your budget per day. Sponsored item ads cycles can run anywhere from 24 hours to 28 days.

<img src="../assets/promotion/misc/Sponsored-Items.png" width="846" />

<Alert severity="info">
This article covers sponsoring **Marketplace items**. To advertise an **experience**, use [[external/roblox-creator-docs/production/promotion/ads-manager|Ads Manager]] or the [[external/roblox-creator-docs/cloud/guides/advertising|Advertising API]] instead.
</Alert>

## Bidding system

Advertisement space works on a bidding system where the higher you set your **Daily Budget** amount in relation to other creators' bids, the more likely your sponsored item will display within the **Sponsored** category on any item's details page on the Roblox website or in the Roblox app. The location of each sponsored item within the category is random.

For example, if there are three sponsored items in the bidding system, advertising space is split according to how much each user has bid:

<table>
<thead>
  <tr>
    <th>User</th>
    <th>Bid amount</th>
    <th>Result</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>A</td>
    <td>50 Robux</td>
    <td>&mdash;</td>
  </tr>
  <tr>
    <td>B</td>
    <td>100 Robux</td>
    <td>User B's sponsored item will display **twice** as often as User A's.</td>
  </tr>
  <tr>
    <td>C</td>
    <td>300 Robux</td>
    <td>User C's sponsored item will display **six times** as often as User A's, and **three times** as often as User B's.</td>
  </tr>
</tbody>
</table>

## Create sponsored items

Once you have at least **10 Robux** to bid on advertising space per day, you can create a new sponsored item for a specific audience, including gender, age, and platform.

To create a new sponsored item:

1. Navigate to the [Sponsored Items page](https://www.roblox.com/sponsorships/list).
1. In the horizontal navigation, select **Items**. All filters update.
1. In the top-right corner, click the **Create Sponsored Ad** button. The **Sponsor This Item** page displays.
1. Click the **Select Item** dropdown menu, then select the item you want to sponsor. The **Icon** section displays the current version of your item's icon.
1. In the **Target Audience**, **Schedule**, and **Daily Budget** sections, choose who can see your sponsored item, how long you want to sponsor your item, and the amount of Robux you want to spend per day.
1. In the **Ad Name** section, enter a descriptive name for your sponsored item. This is only visible to you.
1. Click the **Preview Your Ad** button. A new page with a preview of your sponsored item and a sponsorship summary display.
1. Click the **Run** button.

Roblox holds the full amount for your ad cycle as soon as you click the Run button. If you cancel the ad cycle, you will receive a refund for any amount per full day left of the ad cycle.

## View sponsored item statistics

After you have created a sponsored item, you can view statistics related to the ad's performance.

To view a sponsored item's statistics:

1. Navigate to the [Sponsored Items page](https://www.roblox.com/sponsorships/list).
1. In the horizontal navigation, select the **Items** tab. All filters update.
1. Click the **Select Item** dropdown menu, then select the sponsored item you want to view the statistics for. A high-level view of the statistics for this sponsored item displays.

<table>
<thead>
  <tr>
    <th>Metric</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Attributed Purchases</td>
    <td>The amount of people who purchase your item after they click on your ad. This is only recorded once per user.</td>
  </tr>
  <tr>
    <td>Clicks</td>
    <td>Every time a person clicks on your ad.</td>
  </tr>
  <tr>
    <td>Conversion Rate</td>
    <td>The amount of attributed purchases divided by impressions.</td>
  </tr>
  <tr>
    <td>CPC (Cost Per Click)</td>
    <td>The total Robux spent divided by the number of clicks.</td>
  </tr>
  <tr>
    <td>CPP (Cost Per Purchase)</td>
    <td>The total Robux spent divided by the number of attributed purchases.</td>
  </tr>
  <tr>
    <td>CTR (Click Through Rate)</td>
    <td>Clicks divided by impressions.</td>
  </tr>
    <tr>
    <td>Impressions</td>
    <td>Estimate for the number of times your ad was shown to a user when using the Roblox app or website, or when your ad was requested from servers.</td>
  </tr>
  <tr>
    <td>Status</td>
    <td>A report if your ad is running or not.</td>
  </tr>
  <tr>
    <td>Spent</td>
    <td>The amount of Robux you have spent on the ad.</td>
  </tr>
</tbody>
</table>

## Cancel sponsored items

You can cancel a sponsored item at any time and receive a refund for any amount per full day left of the ad cycle. For example, if you set up a three day ad cycle and cancel on the first day, you will receive a refund for the remaining two days.

To cancel a sponsored item:

1. Navigate to the [Sponsored Items page](https://www.roblox.com/sponsorships/list).
1. In the horizontal navigation, select the **Items** tab. All filters update.
1. Click the **Select Item** dropdown menu, then select the sponsored item you want to cancel. A high-level view of the statistics for this sponsored item displays.
1. Select the **&ctdot;** button, then **Stop**. A warning pop-up dialog displays to confirm that you want to stop your ad.
1. Click the **Stop** button.


## Related Files

- [[external/roblox-creator-docs/marketplace/custom-thumbnails]] - Custom thumbnails.
- [[external/roblox-creator-docs/marketplace/frequently-asked-questions]] - Frequently asked questions.
- [[external/roblox-creator-docs/marketplace/intellectual-property]] - Intellectual property for avatar items.
- [[external/roblox-creator-docs/marketplace/categories]] - Marketplace asset categories.
- [[external/roblox-creator-docs/marketplace/marketplace-fees-and-commissions]] - Marketplace fees and commissions.
- [[external/roblox-creator-docs/marketplace/index]] - Marketplace overview.
- [[external/roblox-creator-docs/marketplace/marketplace-policy]] - Marketplace policy.
- [[external/roblox-creator-docs/marketplace/moderation]] - Moderation.
- [[external/roblox-creator-docs/marketplace/publish-to-marketplace]] - Publish to Marketplace.
- [[external/roblox-creator-docs/marketplace/homestore]] - UGC Homestore.
- [[external/roblox-creator-docs/marketplace/validation-system]] - UGC validation system.
