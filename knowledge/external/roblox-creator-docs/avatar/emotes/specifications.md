---
title: Emote specifications
description: Emote specifications list the specific technical requirements necessary for Studio compatibility.
tags: [roblox, documentation, external-reference, priority-reference, avatar]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [avatar/emotes/specifications.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/avatar/emotes/specifications.md). Published page: [https://create.roblox.com/docs/avatar/emotes/specifications](https://create.roblox.com/docs/avatar/emotes/specifications).

Emotes are made up of an `Class.Animation` object with the `Class.Animation.AnimationId` property set to the asset ID of your animation sequence. The `Class.Animation` object is the only component required to upload an emote to the Marketplace because animations do not require meshes, textures, or other 3D art components.

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

## Animation requirements

Emotes must meet the following requirements before you upload them to the Marketplace, otherwise they may fail validation:

- Emotes must be less than 10 seconds.
- The joint root of the character cannot move too far from its starting position.
- Movement speed can't exceed a certain threshold to prevent teleportation abuse (measured from a frame-by-frame basis).
- Animation data must reference a [[external/roblox-creator-docs/avatar/character-bodies/specifications#standard-r15-rigs|standard R15 rig]].

   <Alert severity = 'info'>
   Emotes for [[external/roblox-creator-docs/avatar/character-bodies/specifications#advanced-r15-rigs|advanced R15 rigs]] are currently in a closed beta. For more information, see the [DevForum announcement](https://devforum.roblox.com/t/upload-and-publish-for-emotes-with-additional-joints-is-now-open/4710932).
   </Alert>

- Animation must be sourced from a `CurveAnimation`. For information on converting animation data, see [[external/roblox-creator-docs/avatar/emotes/import#generate-asset-id|Import emotes - Generate asset ID]].
- Animations must meet Roblox's [Community Standards](https://en.help.roblox.com/hc/en-us/articles/203313410-Roblox-Community-Standards) and [[external/roblox-creator-docs/marketplace/marketplace-policy|Marketplace policies]].


## Related Files

- [[external/roblox-creator-docs/avatar/emotes/index]] - Emotes.
- [[external/roblox-creator-docs/avatar/emotes/export]] - Export emotes.
- [[external/roblox-creator-docs/avatar/emotes/import]] - Import emotes.
