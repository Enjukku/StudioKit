---
title: Audio
description: An overview of audio features on Roblox.
tags: [roblox, documentation, external-reference, priority-reference, audio, index]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [audio/index.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/audio/index.md). Published page: [https://create.roblox.com/docs/audio](https://create.roblox.com/docs/audio).

Adding audio to your games is crucial for elevating your games to new heights. By strategically using positional and non-positional audio, you can immerse players into your worlds, provide them useful feedback for their actions, and direct their attention to what they need to do to be successful in their objectives.

## Audio assets

You can import [[external/roblox-creator-docs/audio/assets|audio assets]] that you're certain you have permission to use, such as audio that you make yourself. However, Roblox's [[external/roblox-creator-docs/production/creator-store|Creator Store]] provides you a wide variety of free-to-use audio assets, including more than 100,000 professionally-produced sound effects and music tracks from top audio and music partners.

## Audio objects

Roblox offers many different types of [[external/roblox-creator-docs/audio/objects|audio objects]] that you can use to play and modify your audio until it meets your game's design requirements:

- The `Class.AudioPlayer` object loads and plays the **audio file** using a set [[external/roblox-creator-docs/audio/assets|audio asset ID]].
- The `Class.AudioEmitter` object is a **virtual speaker** that emits audio into the 3D environment.
- The `Class.AudioListener` object is a **virtual microphone** that picks up audio from the 3D environment.
- The `Class.AudioDeviceOutput` object is a **physical hardware device** within the real world, such as a speaker or headphones.
- The `Class.AudioDeviceInput` object is a **physical microphone** within the real world.
- The `Class.AudioTextToSpeech` object converts **text to audio** using an artificial voice.
- The `Class.AudioSpeechToText` object converts **audio to text**.
- `Class.Wire|Wires` carry audio streams from one object to another.

Using these objects, you can either set audio to play automatically at runtime, or trigger it to play from scripts. For practical applications of these audio objects, see the [[external/roblox-creator-docs/tutorials/use-case-tutorials/audio/add-2D-audio|Add 2D audio]], [[external/roblox-creator-docs/tutorials/use-case-tutorials/audio/add-3D-audio|Add 3D audio]], [[external/roblox-creator-docs/tutorials/use-case-tutorials/audio/add-text-to-speech|Add text-to-speech]], [[external/roblox-creator-docs/tutorials/use-case-tutorials/audio/speech-to-text|Add speech-to-text]], and [[external/roblox-creator-docs/tutorials/use-case-tutorials/audio/add-voice-chat|Add voice chat]] tutorials.

## Audio effects

[[external/roblox-creator-docs/audio/effects|Audio effects]] non-destructively modify or enhance audio streams from `Class.AudioPlayer` objects. You can apply these effects to make your environments more captivating and immersive, such as using a `Class.AudioEqualizer` object to make rain sound muffled, `Class.AudioCompressor` object to control a sound's maximum volume, or `Class.AudioReverb` to add more realistic reflections of sound in interior spaces.


## Related Files

- [[external/roblox-creator-docs/audio/assets]] - Audio assets.
- [[external/roblox-creator-docs/audio/effects]] - Audio effects.
- [[external/roblox-creator-docs/audio/objects]] - Audio objects.
