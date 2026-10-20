---
title: MicroProfiler modes
description: The MicroProfiler includes several different modes, all of which offer different ways to understand your game's performance profile.
tags: [roblox, documentation, external-reference, priority-reference, performance, profiling, optimization]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [performance-optimization/microprofiler/modes.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/performance-optimization/microprofiler/modes.md). Published page: [https://create.roblox.com/docs/performance-optimization/microprofiler/modes](https://create.roblox.com/docs/performance-optimization/microprofiler/modes).

The MicroProfiler includes several modes, which can help you visualize your game's performance characteristics in different ways. After opening the MicroProfiler, use the **Modes** menu to switch between them.

**Frame mode** and **detailed mode** are covered under [[external/roblox-creator-docs/performance-optimization/microprofiler/index#microprofiler-basics|MicroProfiler basics]].

## Timers mode

**Timers mode** is an alternative way of visualizing the data in the detailed view: as a list of labels with processing times and call counts. Horizontal bar graphs in some columns help you spot the busiest tasks.

<img alt="Timers mode." src="../../assets/optimization/microprofiler/micro-timers-mode.png" width="600px" />

Controls are similar to detailed view:

- Left-click and hold to pan up and down.
- Left-click a label to add it to the line graph in the lower-right.
- Use the **Groups** menu to filter the list.
- Use the **Timers** menu to customize the columns.

<Alert severity="info">
All of the information in this view is visible when you hover over a label in the detailed view.
</Alert>

## Counters mode

Counters mode is a lengthy list of categories and statistics, including instance count and memory usage (in bytes) for the various tasks.

<img alt="Counters mode with a single graph." src="../../assets/optimization/microprofiler/micro-counters-mode.png" width="400px" />

- Just like the detailed view, left-click and hold to pan up and down.
- Left-click in the **Graph** column to add a small usage graph with minimum and maximum values. Left-click the graph again to expand it.
- Right-click a graph to close it.
- You can't filter this view, but you can left-click on a category (for example, `memory`) to collapse it.

While counters mode can be useful, the [[external/roblox-creator-docs/studio/optimization/memory-usage|Developer Console]] is the best way to [[external/roblox-creator-docs/performance-optimization/identify#client-memory|identify memory issues]]. You might also find the [[external/roblox-creator-docs/performance-optimization/microprofiler/index#web-only-features|X-ray view]] helpful for identifying when problematic memory allocation occurs.

## Groups mode

Only available in the web UI. Similar to timers mode, groups mode provides average, max, and total task times for each group, broken down by thread, to help you identify how broad categories of tasks are impacting your frame times.

<img alt="MicroProfiler web UI showing groups mode." src="../../assets/optimization/microprofiler/micro-groups-mode.png" width="600px" />

## Threads mode

Only available in the web UI. Similar to timers mode, threads mode provides average and total task times for each thread, broken down by group, to help you identify how your game is distributing tasks across threads.

<img alt="MicroProfiler web UI showing threads mode." src="../../assets/optimization/microprofiler/micro-threads-mode.png" width="600px" />

## Hidden mode

Only available in the desktop UI. Hidden mode keeps the MicroProfiler menu open, but hides the bar graph. It's useful for reducing visual clutter, [[external/roblox-creator-docs/performance-optimization/microprofiler/index#save-frame-data|saving frame data]], and pausing and unpausing while you observe the line graph.


## Related Files

- [[external/roblox-creator-docs/performance-optimization/microprofiler/index]] - MicroProfiler.
- [[external/roblox-creator-docs/performance-optimization/microprofiler/use-microprofiler]] - MicroProfiler walkthrough.
- [[external/roblox-creator-docs/performance-optimization/microprofiler/network]] - Network usage.
- [[external/roblox-creator-docs/performance-optimization/microprofiler/tag-table]] - Tag reference.
- [[external/roblox-creator-docs/performance-optimization/microprofiler/task-scheduler]] - Task scheduler.
