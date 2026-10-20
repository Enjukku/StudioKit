---
title: Monitor performance
description: Explains how to use the Performance Dashboard to monitor your games.
tags: [roblox, documentation, external-reference, priority-reference, performance, optimization]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [performance-optimization/monitor.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/performance-optimization/monitor.md). Published page: [https://create.roblox.com/docs/performance-optimization/monitor](https://create.roblox.com/docs/performance-optimization/monitor).

The [[external/roblox-creator-docs/production/analytics/performance|Performance Dashboard]] is the best way to monitor the performance of your published games. The two tabs include real-time performance information for both clients and servers, and you can use date ranges to track the impact of your changes over time.

For example, imagine you've just added a new place to your game:

1. You publish the updated game, and hours later, you notice a distinct uptick in client crash rate on the Performance Dashboard that seems to correlate with client memory usage.
1. You test the new place in Studio and don't see any issues. Memory usage seems similar to other places in your game.
1. You note that average player session time has increased dramatically since your update.
1. You test again, but this time, you spend more time in the game and keep a closer eye on memory usage over time. Sure enough, usage is growing over time and could cause crashes on lower-end devices.
1. You check the server tab and notice that server memory usage is growing over time, too. It's not a problem yet, but could become a problem soon.
1. Under the **Memory** tab of the Developer Console, in the **PlaceScriptMemory** breakdown, you notice that the memory usage for one of your new scripts grows each time you interact with some key objects in the world. The script runs on both the client and the server.
1. You check the script, which adds some user data to a large table, but never cleans the data up—it's growing infinitely.
1. You fix the problem, publish the updated game, and client crash rate returns to its previous value.

Comparing the Performance Dashboard to other dashboards can help you correlate performance improvements (or regressions) to business metrics for a more complete idea of how a performant game impacts your bottom line. For more information, see [[external/roblox-creator-docs/production/analytics/index|Analytics]].


## Related Files

- [[external/roblox-creator-docs/performance-optimization/design]] - Design for performance.
- [[external/roblox-creator-docs/performance-optimization/identify]] - Identify performance issues.
- [[external/roblox-creator-docs/performance-optimization/improve]] - Improve performance.
- [[external/roblox-creator-docs/performance-optimization/index]] - Performance optimization.
- [[external/roblox-creator-docs/performance-optimization/scene-analysis]] - Scene Analysis.
- [[external/roblox-creator-docs/performance-optimization/test-on-hardware]] - Test on hardware.
