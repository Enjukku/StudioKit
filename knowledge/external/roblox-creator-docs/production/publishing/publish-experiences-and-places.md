---
title: Create and publish experiences and places
description: Explains how to create and publish experiences.
tags: [roblox, documentation, external-reference, priority-reference, production]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [production/publishing/publish-experiences-and-places.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/publishing/publish-experiences-and-places.md). Published page: [https://create.roblox.com/docs/production/publishing/publish-experiences-and-places](https://create.roblox.com/docs/production/publishing/publish-experiences-and-places).

> [!warning] Not in the current upstream docs
> Not published in [github.com/Roblox/creator-docs](https://github.com/Roblox/creator-docs) as of 2026-10-20 (revision `74006430`). The closest current page is [[external/roblox-creator-docs/production/publishing/publish-games-and-places]]. Kept locally so existing links keep working; read that page for current information.

When you open Studio and create a new **experience**, your project starts with a single **place** that players load into when they first join the experience. Experiences can have one or multiple places that each contain all components for that portion of the experience, including its specific environment, 3D objects, and scripts.

<Alert severity="info">
Places are comparable to scenes in Unity or maps in Unreal Engine.
</Alert>

<figure>
<iframe width="800" height="450" src="https://www.youtube-nocookie.com/embed/_RxK6l2y7Ac" title="YouTube video player" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen></iframe>
</figure>

Many creators create additional places within an experience to organize assets for different gameplay areas. For example, if you want players to join a dungeon before [[external/roblox-creator-docs/projects/teleport|teleporting]] to either a vast desert or spooky island, you can organize the assets for each area into their own place.

<figure>
<img src="../../assets/publishing/experiences-places-assets/Experience-Hierarchy.png" width="800" />
</figure>

Every place is represented by a data model that stores and organizes:

- All objects that make up the 3D world of a place, such as its parts, meshes, terrain, and lighting.
- All objects that can control runtime behavior, such as scripts.

Understanding both the general structure of a place's data model, and how the Roblox engine uses it as the source of truth for a place's state is important for understanding where to store and configure different types of objects. For more information, see [[external/roblox-creator-docs/projects/data-model|data model]].

## Create experiences

When you create a new experience, it opens a start place that all players will load into when they join the experiences. The start place represents the overall experience until you add additional places for different gameplay areas.

To create an experience:

1. Open Studio.
2. In the **Open a Template** section, select a template with the objects you want to start working with for your experience, such as:

   - **Baseplate** — Starts with a `Class.SpawnLocation` and a baseplate.
   - **Platformer** — Starts with customizable platforms, coin pickups, and double-jump, dashing, rolling, and long jump character mechanics!
   - **Racing** — Starts with a working racecar and customizable track objects.

When Studio opens up the template, you now have `Place1` that represents your overall experience.

## Publish experiences

When you publish an experience, Roblox stores the data model of your start place as a `.rblx` file in the cloud. This is an important process because it connects the experience to your account, allowing you to access and work on it from any computer.

By default, new experiences are set to **private**, meaning that they are only accessible to you as the creator, to users with **Edit** or **Playtest** access, and to group members with the appropriate [[external/roblox-creator-docs/projects/groups#roles-and-permissions|roles and permissions]]. When you are ready to go live to everyone, you can [release your experience to the public](#make-experience-public) and optionally mark it as a beta.

<Alert severity="info">
When creating and collaborating on experiences as part of a [[external/roblox-creator-docs/projects/groups|group]], the ability for group members to playtest/edit/publish experiences is, by default, dependent on their role permissions. However, group owners or members with sufficient permissions can adjust access on a per‑experience level. For more info, see [[external/roblox-creator-docs/projects/configure-experiences|configure experiences]].
</Alert>

To publish an experience:

1. In the top-left corner of your computer, click **File** ⟩ **Publish to Roblox**.
2. In the **Publish Experience** window, fill in the following fields:

   - **Name** / **Description** — The experience name and a description that describes what a potential player should expect. See the metadata best practices dropdown at the bottom of this section for guidelines.
   - **Creator** — The creator or [[external/roblox-creator-docs/projects/groups|group]] (<Chip label="RECOMMENDED" size="small" variant="outlined" color="success" />) you'd like to attribute as the creator of the experience.
   - **Devices** — Each applicable device type that you want to support. The default options are practical for most new creators.

3. Click **Create**.

<BaseAccordion>
<AccordionSummary>
<Typography variant="subtitle2">Metadata best practices</Typography>
</AccordionSummary>
<AccordionDetails>

Your experience's name and description create an important first impression and contribute to how easily players find your experience through Roblox's dynamic [[external/roblox-creator-docs/discovery|discovery]] systems.

<h4>Experience name</h4>

All experiences should adhere to the following best practices for naming:

- **Keep the name consistent** &ndash; Renaming an experience too often reduces the chances that players can find it using a previous name.

- **Avoid spamming** &ndash; Frequent repetition of words or phrases may result in demotion of your experience.

<Alert severity="success">
**Obby Madness**
</Alert>
<Alert severity="error">
**Obby Madness OBBY OBBY OBBY OBBY OBBY**
</Alert>

- **Use decorations cautiously** &ndash; Decorating the name with one or two well-placed emojis isn't harmful, but misplaced or excessive decorations can confuse players who quickly want to identify the experience.

<Alert severity="success">
🌍 **Evolution Simulator** 🌍
</Alert>
<Alert severity="error">
🐒🐬🐊 **Ev**🌍**luti**🌍**n Simulator** 🌷🍀🌿
</Alert>

<h4>Experience description</h4>

A well-written description promotes the genre and unique qualities of your experience while also providing the best context for both players and Roblox's dynamic discovery systems.

- **Summarize your experience** &ndash; Summarize what your experience is about in the first sentence, as this is your opportunity to present the most accurate impression of its genre and content.

<Alert severity="success">
Compete with racers around the world in some of the craziest courses you've ever seen!
</Alert>
<Alert severity="success">
Fight off hordes of zombies with bats, guns, swords, and a bunch of weapons hidden throughout challenging mazes.
</Alert>

- **Provide keywords** &ndash; Include all keywords that may be relevant to your experience. This makes it easier for players and Roblox to understand the themes and genres presented in your experience.

<Alert severity="success">
Do you enjoy being a <u>sheriff</u>? Join and rid our town of <u>robbers</u> and <u>crooks</u>! <u>Arrest</u> the bad guys, throw them in <u>jail</u>, and even have a <u>guns</u>-blazing <u>shoot</u>-out outside the saloon.
</Alert>
<Alert severity="success">
Open your own <u>restaurant</u>, make delicious <u>food</u>, get lots of <u>customers</u>, and expand! Earn experience along the way and learn more <u>recipes</u>. If you love <u>cooking</u> and starting your own <u>business</u>, this is your chance to become a <u>tycoon</u>!
</Alert>

- **Avoid spamming** &ndash; Avoid repeating keywords or adding irrelevant keywords. This may result in demotion of your experience.

<Alert severity="error">
Play our fun granny obby game. Obby obby obby obby obby obby obby adopt me bloxburg arsenal ninja legends parkour tycoon battle disaster survival super hero simulator run jump gun rpg pokemon wild west space alien piggy baldi granny murder mystery prison life jail break mario zelda dungeon quest.
</Alert>

</AccordionDetails>
</BaseAccordion>

<Alert severity="info">
Roblox supports places up to 100 MB (104,857,600 bytes). Beyond that limit, **Save&nbsp;to&nbsp;Roblox** and **Publish&nbsp;to&nbsp;Roblox** might fail. The data that Studio uploads to Roblox is slightly smaller than the `.rbxl` file format, so you can export your place to `.rbxl` to get a sense of its size.

Very few places, even the most complex ones, reach this limit, and when they do, it's often due to inefficiencies in the place. See [Troubleshooting](../../projects/place-files.md#troubleshoot-place-file-size).
</Alert>

### Create additional places

After you have published your experience, you can add additional places for different gameplay areas. To create a new place within an existing experience:

1. Open an existing place file or create a new place from any Studio template.
2. Select **File** ⟩ **Publish to Roblox As…**.
3. In the **Publish Experience** window, click the tile for the experience you'd like to add the place to.
4. Select **Add as a new place**, then click **Create**.

Whether you choose to have a single, large place or many smaller places is mostly personal preference. For more information, see [[external/roblox-creator-docs/performance-optimization/design#streaming-and-teleportation|design for performance]].

### Change start place

The start place of an experience cannot be instantly swapped with another place, but you can overwrite the current start place.

To change the start place:

1. <Chip label="OPTIONAL" size="small" variant="outlined" /> Save your **current** start place to a `.rbxl` file or to a new place within the experience.
2. Go to the [Creator Dashboard][creatordashboard] and select the experience with the start place that you want to change.
3. Go to **Configure** ⟩ **Places**.
4. Click **Edit in Studio** for the intended **new** start place. Studio opens and loads that specific place.

   <img src="../../assets/creator-dashboard/Experience-Change-Start-Place.png" width="550" />

5. In the top-left corner of Studio, go to **File** ⟩ **Publish to Roblox As…**.

   <Alert severity="error">
   Do not select **Publish to Roblox** as this would publish the place over itself.
   </Alert>

6. Click the tile for the same experience, then choose the **current** start place. Click **Overwrite**.

   <img src="../../assets/publishing/experiences-places-assets/Publish-Window-Select-Start-Place.png" width="720" />

7. <Chip label="OPTIONAL" size="small" variant="outlined" /> If the experience is live, it's recommended that you [[external/roblox-creator-docs/projects/update-experiences#restart-servers|restart its servers]].

### Make experience public

<Alert severity="warning">
To make a new experience public or update an existing public experience, you must:

- Have an account that is at least 48 hours old
- Complete the [[external/roblox-creator-docs/production/promotion/content-maturity|content maturity & compliance]] questionnaire for the specific experience
- Meet at least one of the following:
  - Have an [[external/roblox-creator-docs/production/publishing/account-verification#verify-through-government-id|ID-verified account]] **OR**
  - Have made a purchase using real currency or a gift card since January 1, 2025

These requirements apply to both **publishing a new experience** and **updating an existing public experience**, including:

- Using **Publish to** or **Publish as** in Studio
- Publishing a new version of a place within an existing experience
- Setting your audience to **Public** or **Community members**

You do **not** need to meet these requirements if you keep your experience private or if your audience is set to **Friends**.
</Alert>

<Alert severity="info">
You can make up to **5 private experiences that have never been public before** public per day. This limit resets daily. Making an experience that was already public private and then public again does **not** count toward this limit.
</Alert>

By default, new experiences are set to **private**, meaning that they are only accessible to you as the creator, to users with **Edit** or **Playtest** access, and to group members with the appropriate [[external/roblox-creator-docs/projects/groups#roles-and-permissions|roles and permissions]]. To make your experience available to everyone on Roblox, you have to update its privacy settings.

To update your experience's privacy settings:

1. In the [Creator Dashboard][creatordashboard], select the experience you want to make public.
1. Go to **Configure** ⟩ **Settings**.
1. Under **Privacy**, select **Public**.
1. <Chip label="OPTIONAL" size="small" variant="outlined" /> Choose **Enable Beta mode** to omit the experience from **Recommended For You** in the Roblox client. Beta experiences are still public, but have more limited reach and exposure.

   <Alert severity="success">
   To widen your audience while still remaining in beta, click **Create campaign** to set up a sponsored ad. To learn more, see [[external/roblox-creator-docs/production/promotion/ads-manager|Ads Manager]]. If you enable sponsored ads, the experience analytics charts might show some users from **Recommended For You**.
   </Alert>

1. Click **Save Changes**.

After you make your experience public, you can choose the scope of your audience:

1. In the [Creator Dashboard][creatordashboard], select the experience you want to specify the audience for.
1. Go to **Audience** ⟩ **Access Settings**.
1. Under **Join**, select one of the following options:
   - **Public** — available to all users on Roblox.
   - **Friends** — available only to the experience owner's friends. This option only appears for non–group-owned experiences.
   - **Community members** — available only to group members. This option only appears for group-owned experiences.
1. Click **Save Changes**.

[creatordashboard]: https://create.roblox.com/dashboard/creations


## Related Files

- [[external/roblox-creator-docs/production/publishing/about-GDPR-and-CCPA]] - About GDPR and CCPA.
- [[external/roblox-creator-docs/production/publishing/accessibility]] - Accessibility guidelines.
- [[external/roblox-creator-docs/production/publishing/account-verification]] - Account verification.
- [[external/roblox-creator-docs/production/publishing/adaptive-design]] - Adaptive design guidelines.
- [[external/roblox-creator-docs/production/promotion/ads-manager]] - Ads Manager.
- [[external/roblox-creator-docs/production/publishing/badges]] - Badges.
- [[external/roblox-creator-docs/projects/configure-experiences]] - Configure experiences and places.
- [[external/roblox-creator-docs/production/publishing/console-guidelines]] - Console development guidelines.
- [[external/roblox-creator-docs/production/promotion/content-maturity]] - Content maturity and compliance.
- [[external/roblox-creator-docs/projects/data-model]] - Data model.
- [[external/roblox-creator-docs/performance-optimization/design]] - Design for performance.
- [[external/roblox-creator-docs/discovery]] - Discovery.
- [[external/roblox-creator-docs/production/publishing/dmca-guidelines]] - DMCA guidelines.
- [[external/roblox-creator-docs/production/publishing/descriptions]] - Experience descriptions.
- [[external/roblox-creator-docs/projects/groups]] - Groups (teams).
- [[external/roblox-creator-docs/production/index]] - Production.
- [[external/roblox-creator-docs/projects/update-experiences]] - Release experience updates.
- [[external/roblox-creator-docs/projects/teleport]] - Teleport between places.
