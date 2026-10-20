---
title: Emotes
description: All Roblox users are represented by an avatar character which can be customized with body parts, accessories, and clothes from the Marketplace or within experiences.
tags: [roblox, documentation, external-reference, priority-reference, art, assets, index]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [art/emotes/index.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/art/emotes/index.md). Published page: [https://create.roblox.com/docs/art/emotes](https://create.roblox.com/docs/art/emotes).

> [!warning] Not in the current upstream docs
> Not published in [github.com/Roblox/creator-docs](https://github.com/Roblox/creator-docs) as of 2026-10-20 (revision `74006430`). The closest current page is [[external/roblox-creator-docs/avatar/emotes/index]]. Kept locally so existing links keep working; read that page for current information.

**Emotes** are short animations that an avatar performs, making it easier to communicate and celebrate with others, enhancing the experience to feel more social and more lively.

Creators sell their own emotes, such as gestures, reactions, dances, and more, by publishing their animation to sell on the Marketplace or within experiences.

<Alert severity = 'info'>
Developers can access and modify emotes within their own experiences. For more information, see [[external/roblox-creator-docs/characters/emotes|character emotes]].
</Alert>

## Components of an emote

Emotes are made up of an `Class.Animation` object with the unique `Class.Animation.AnimationId` property set to the asset ID of your animation sequence.

<GridContainer numColumns="2">
  <figure>
    <img src="../../assets/avatar/avatar-emotes/Animation-Explorer.png" />
    <figcaption><center>`Animation` object in the Explorer.</center></figcaption>

  </figure>
  <figure>
    <img src="../../assets/avatar/avatar-emotes/Animation-Properties.png" />
    <figcaption><center>`AnimationId` property in the Properties window.</center></figcaption>
  </figure>
</GridContainer>

Emotes must meet [[external/roblox-creator-docs/art/emotes/specifications|technical specifications]] as well as [[external/roblox-creator-docs/marketplace/marketplace-policy|Marketplace]] and [Community](https://en.help.roblox.com/hc/en-us/articles/203313410-Roblox-Community-Standards) policies.

## Creation process

There are several ways to create an animation both in Studio or using a third-party tool. See the following table for common workflows and various resources to create your own.

<table><thead>
  <tr>
    <th>Animation workflow</th>
    <th>Description</th>
  </tr></thead>
<tbody>
  <tr>
    <td>Animation Capture</td>
    <td>Use the [[external/roblox-creator-docs/animation/capture#body|Animation Capture (Body)]] to convert a video of your emote into a keyframe sequence.</td>
  </tr>
  <tr>
    <td>Manual animation with Animation Editor</td>
    <td>Use the [[external/roblox-creator-docs/animation/editor|Animation Editor]] to manually animate a character rig. For an in-depth tutorial on creating a character animation, see [[external/roblox-creator-docs/tutorials/use-case-tutorials/animation/create-an-animation|Create character animations]].</td>
  </tr>
  <tr>
    <td>Third-party plug-ins</td>
    <td>Use a third-party animation plugin, such as [Moon Animator](https://create.roblox.com/store/asset/4725618216/Moon-Animator-2), to generate your animation.</td>
  </tr>
</tbody>
</table>

To convert your keyframe sequence into an animation and upload to the Marketplace, see [[external/roblox-creator-docs/art/emotes/import#configure|import and configure emotes]].


## Related Files

- [[external/roblox-creator-docs/art/index]] - 3D art in Roblox.
- [[external/roblox-creator-docs/animation/capture]] - Animation capture.
- [[external/roblox-creator-docs/animation/editor]] - Animation Editor.
- [[external/roblox-creator-docs/art/emotes/export-settings]] - Animation export settings.
- [[external/roblox-creator-docs/tutorials/use-case-tutorials/animation/create-an-animation]] - Create character animations.
- [[external/roblox-creator-docs/characters/emotes]] - Emotes.
- [[external/roblox-creator-docs/art/emotes/specifications]] - Emotes specifications.
- [[external/roblox-creator-docs/art/emotes/import]] - Import and configure animations.
- [[external/roblox-creator-docs/marketplace/marketplace-policy]] - Marketplace policy.
