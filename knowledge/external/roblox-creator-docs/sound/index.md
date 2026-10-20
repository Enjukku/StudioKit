---
title: Sound
description: An overview of legacy Sound objects and effects.
tags: [roblox, documentation, external-reference, priority-reference, sound]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [sound/index.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/sound/index.md). Published page: [https://create.roblox.com/docs/sound](https://create.roblox.com/docs/sound).

<Alert severity = 'warning'>
There is a newer set of [[external/roblox-creator-docs/audio/objects|audio objects]] and [[external/roblox-creator-docs/audio/effects|effects]] that offer more control and address robust use cases. For more information, see [[external/roblox-creator-docs/audio/index|Audio]].
</Alert>

Sound effects and music enhance your games and make them more immersive. You can import your own [[external/roblox-creator-docs/audio/assets|audio assets]] or search for free-to-use audio in the [[external/roblox-creator-docs/production/creator-store|Creator Store]], play audio through `Class.Sound` or objects, and enhance audio playback through [dynamic effects](#dynamic-effects).

## Sound objects

A [[external/roblox-creator-docs/sound/objects|sound object]] emits audio within a game. Roblox assigns each [[external/roblox-creator-docs/audio/assets|audio asset]] a unique ID that you can assign to `Class.Sound` objects to play a specific sound effect or music track. You can either set this audio to play automatically at runtime, or trigger it to play from scripts.

The location of where you place a `Class.Sound` object in the [[external/roblox-creator-docs/studio/explorer|Explorer]] hierarchy affects how users hear audio. If you want users to only hear audio near a specific position, you must parent the `Class.Sound` object to a 3D object or `Class.Attachment` to behave as positional audio. If you want users to hear audio regardless of their position, you must insert the `Class.Sound` object directly into `Class.Workspace` or `Class.SoundService` to behave as background audio.

## Sound groups

A [[external/roblox-creator-docs/sound/groups|sound group]] acts as an audio mixer for multiple audio objects, such as `Class.Sound` objects or additional `Class.SoundGroup|SoundGroups`, allowing you to control the volume and dynamic effects properties of multiple audio signals at once.

## Dynamic effects

[[external/roblox-creator-docs/sound/dynamic-effects|Dynamic effects]] modify or enhance the audio of individual `Class.Sound` objects or an entire `Class.SoundGroup`. You can apply these effects to make audio more immersive within the game, such as using `Class.EqualizerSoundEffect` to make rain sound muffled, `Class.CompressorSoundEffect` to control a sound's maximum volume, or `Class.ReverbSoundEffect` to add more realistic reflections of sound in interior spaces.


## Related Files

- [[external/roblox-creator-docs/sound/dynamic-effects]] - Dynamic effects.
- [[external/roblox-creator-docs/sound/groups]] - Sound groups.
- [[external/roblox-creator-docs/sound/objects]] - Sound objects.
