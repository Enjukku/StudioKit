---
title: Heads
description: Facial animations enable avatars to create dynamic facial expressions.
tags: [roblox, documentation, external-reference, priority-reference, art, assets, animation, index]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [art/characters/facial-animation/index.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/art/characters/facial-animation/index.md). Published page: [https://create.roblox.com/docs/art/characters/facial-animation](https://create.roblox.com/docs/art/characters/facial-animation).

> [!warning] Not in the current upstream docs
> Not published in [github.com/Roblox/creator-docs](https://github.com/Roblox/creator-docs) as of 2026-10-20 (revision `74006430`). The closest current page is [[external/roblox-creator-docs/avatar/dynamic-heads/index]]. Kept locally so existing links keep working; read that page for current information.

Heads are a fundamental component of an avatar character body. Roblox avatar heads, such as those available on the Marketplace, contains components that allow you to:

- Set default custom facial expressions.
- Trigger emotes that combine both face and body animations.
- Equip face accessories that deform with your facial expressions. For example, facial hair moves accordingly when the character changes facial expressions.

<video controls width="90%" src="../../../assets/avatar/dynamic-heads/Blocky_And_Goblin_Dynamic_Heads.mp4">
</video>

## Create basic heads

<Alert severity = 'warning'>
When creating heads intended for the Marketplace, ensure that your head meets Roblox's [[external/roblox-creator-docs/art/characters/head-specifications|head specifications]].
</Alert>

Using third-party modeling tools, you can either modify a rigged character model to meet head requirements, or create a head from scratch. For step-by-step instructions on how to add face bones, apply skinning, posing, and mapping poses on a head model in Blender, see [[external/roblox-creator-docs/art/characters/facial-animation/create-basic-heads|Create basic heads]]. This guide includes several reference files you can use to compare and track your progress.

### Resources

Heads designated for the Marketplace require specific components to ensure universal support across Roblox's platform. Heads are often the most complex part of an avatar character. Use the following docs to best equip your assets to pass validation and work well with other assets:

- Understand how Roblox tests facial animations in the [[external/roblox-creator-docs/art/characters/head-validation|validation process]] and learn common issues that you can self-resolve.
- Similar to character bodies and clothing, Marketplace heads must also follow [[external/roblox-creator-docs/art/characters/head-specifications|Roblox's specifications]].
- Ensure that you are following Roblox's [[external/roblox-creator-docs/art/characters/face-caging-best-practices|head caging best practices]] to ensure the best results for clothing, validation, and makeup.
- Use the [[external/roblox-creator-docs/art/characters/facial-animation/facs-poses-reference|FACS poses reference]] when posing and mapping your head.

## Create face accessories

Similar to creating heads, you can design and model face accessories using a third-party modeling software and import the models as a cosmetic `Class.Accessory` in Studio. When created correctly, equipped accessories stretch and deform as the head animates and emotes.

See [[external/roblox-creator-docs/art/characters/facial-animation/create-face-accessories|Create face accessories]] for step-by-step instructions on setting up a reference model as a face accessory. This guide includes several project files you can use for reference and covers details on time-saving steps, such as auto-skin transfer.

## Test heads

Testing is an important part of the iterative creation process. To test heads in Studio, see [[external/roblox-creator-docs/art/characters/facial-animation/use-heads-in-studio|Testing in Studio]].

## Animate heads

If you're interested in animating a head, for use in-experience or to further test your character's face rig, see [[external/roblox-creator-docs/art/characters/facial-animation/animate-heads|Animate heads]].

<video controls width="80%" src="../../../assets/avatar/dynamic-heads/animating-dynamic-heads/videos/2-Face-Controls-Example-Goblin.mp4">
</video>


## Related Files

- [[external/roblox-creator-docs/art/index]] - 3D art in Roblox.
- [[external/roblox-creator-docs/art/characters/facial-animation/animate-heads]] - Animate heads.
- [[external/roblox-creator-docs/art/characters/index]] - Avatar characters.
- [[external/roblox-creator-docs/art/characters/facial-animation/create-basic-heads]] - Create basic heads.
- [[external/roblox-creator-docs/art/characters/facial-animation/create-face-accessories]] - Create face accessories.
- [[external/roblox-creator-docs/art/characters/face-caging-best-practices]] - Face caging best practices.
- [[external/roblox-creator-docs/art/characters/facial-animation/facs-poses-reference]] - FACS poses reference.
- [[external/roblox-creator-docs/art/characters/head-specifications]] - Head specifications.
- [[external/roblox-creator-docs/art/characters/head-validation]] - Head validation.
- [[external/roblox-creator-docs/art/characters/facial-animation/moods]] - Moods.
- [[external/roblox-creator-docs/art/characters/facial-animation/use-heads-in-studio]] - Test heads in Studio.
