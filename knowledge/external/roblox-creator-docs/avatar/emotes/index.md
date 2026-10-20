---
title: Emotes
description: Emotes are full body animations that an avatar character can perform to communicate and celebrate with others in games.
tags: [roblox, documentation, external-reference, priority-reference, avatar]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [avatar/emotes/index.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/avatar/emotes/index.md). Published page: [https://create.roblox.com/docs/avatar/emotes](https://create.roblox.com/docs/avatar/emotes).

**Emotes** are full body animations that an avatar character can perform to communicate and celebrate with others in a game, such as gestures, reactions, and dances. While Roblox provides a set of default emotes for each avatar on the platform, you can create and sell your own emotes on the Marketplace or within games.

<Alert severity = 'info'>
Game developers can access and modify emotes within their games. For more information on this process, see [[external/roblox-creator-docs/characters/emotes|character emotes]].
</Alert>

## Components

Emotes are made up of an `Class.Animation` object with the unique `Class.Animation.AnimationId|AnimationId` property set to the asset ID of your animation sequence.

<GridContainer numColumns="2">
  <figure>
    <img src="../../assets/avatar/avatar-emotes/Animation-Explorer.png" />
    <figcaption><center>`Animation` object in the Explorer window.</center></figcaption>

  </figure>
  <figure>
    <img src="../../assets/avatar/avatar-emotes/Animation-Properties.png" />
    <figcaption><center>`AnimationId` property in the Properties window.</center></figcaption>
  </figure>
</GridContainer>

All emotes must meet Roblox's technical [[external/roblox-creator-docs/avatar/emotes/specifications|emote specifications]], [Community Standards](https://en.help.roblox.com/hc/en-us/articles/203313410-Roblox-Community-Standards), and [[external/roblox-creator-docs/marketplace/marketplace-policy|Marketplace policies]].

## Create emotes

There are several ways you can create emotes using either Studio or a third-party animation tool. Review the following table for specific workflows and resources:

<table><thead>
  <tr>
    <th>Animation workflow</th>
    <th>Description</th>
  </tr></thead>
<tbody>
  <tr>
    <td>Animation Capture</td>
    <td>Use Studio's [[external/roblox-creator-docs/animation/capture#body|Animation Capture]] tool to convert a full body video into a keyframe sequence for your emote.</td>
  </tr>
  <tr>
    <td>Manual animation with Animation Editor</td>
    <td>Use Studio's [[external/roblox-creator-docs/animation/editor|Animation Editor]] to manually animate a character rig. For an in-depth tutorial on creating a character animation, see [[external/roblox-creator-docs/tutorials/use-case-tutorials/animation/create-an-animation|Create character animations]].</td>
  </tr>
  <tr>
    <td>Third-party plug-ins</td>
    <td>Use a third-party animation plugin, such as [Moon Animator](https://create.roblox.com/store/asset/4725618216/Moon-Animator-2), to generate your animation.</td>
  </tr>
</tbody>
</table>

To convert your keyframe sequence into an animation that you can upload to the Marketplace, see [[external/roblox-creator-docs/avatar/emotes/import#generate-asset-id|Import emotes - Generate asset ID]].


## Related Files

- [[external/roblox-creator-docs/avatar/emotes/specifications]] - Emote specifications.
- [[external/roblox-creator-docs/avatar/emotes/export]] - Export emotes.
- [[external/roblox-creator-docs/avatar/emotes/import]] - Import emotes.
