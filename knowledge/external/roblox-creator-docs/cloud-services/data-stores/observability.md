---
title: Data store observability
description: Explains how to use the observability dashboard for data stores (DataStores).
tags: [roblox, documentation, external-reference, priority-reference, cloud, services, datastores]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [cloud-services/data-stores/observability.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/cloud-services/data-stores/observability.md). Published page: [https://create.roblox.com/docs/cloud-services/data-stores/observability](https://create.roblox.com/docs/cloud-services/data-stores/observability).

The data stores observability dashboard provides real-time charts on your request counts and on your usage against future data store limits, and allows you to filter the request data by standard or ordered data stores.

![An image showing the request count by API dashboard in the Creator Hub.](../../assets/data/data-store/Data-Store-API.png)

## Access the dashboard

The data stores dashboard is available for any game that uses `Class.DataStoreService`, but you must either be the game owner or have [[external/roblox-creator-docs/production/analytics/analytics-dashboard#grant-group-permission|analytics group permissions]] to access the dashboard.

1. Navigate to the [Creations](https://create.roblox.com/dashboard/creations) page on the **Creator Hub**.
2. Under the **Creator Hub** dropdown, select your account or the group owning the target game.
3. Select the game.
4. In the **Monitoring** dropdown, select **Data Stores**.

## Available charts

- **Storage Usage Bytes** on amount of data store storage and limit currently available for the selected universe.
- **Request Count by API** on API request count per minute by API method, such as `Class.DataStore:SetAsync()` or `Class.OrderedDataStore:GetSortedAsync()`.
- **Request Count by Status** on API request count by [response status](#response-status-codes).
- **Request by API x Status** on response statuses returned by all or a specific API method.
- **Read Request Type Quota Usage** on number of read API method calls against future read category limits.
- **Write Request Type Quota Usage** on number of write API method calls against future write category limits.
- **List Request Type Quota Usage** on number of list API method calls against future list category limits.
- **Remove Request Type Quota Usage** on number of remove API method calls against future remove category limits.

Use the selector at the top of the page to filter by standard or ordered data stores. The default view includes standard data store only.

Use the **Explore** button next to each chart to deep dive into that metric, compare the current period against past periods, or break down that metric by its available categories.

Each chart contains data for the past 30 days, and you can select to view a custom time range with the selector at the top of the page. If you select a time range earlier than 30 days, the system returns a **Request Failed** error.

Data from the most recent three minutes might be incomplete, so it's normal to see a drop at the end of the charts.

Storage usage and limit are displayed in bytes, where 1 kilobyte is 1024 bytes.

## Response status codes

The dashboard's **Request Count by Status** and **Requests by API x Status** charts include status codes of API responses that you can use to understand usage and troubleshoot errors. For a table that lists and describes all of these status codes (aside from `200 OK`), see [[external/roblox-creator-docs/cloud-services/data-stores/error-codes-and-limits#error-code-reference|Error codes]].

## Service limits

For information on current limits, usage quotas, and future limits, see [[external/roblox-creator-docs/cloud-services/data-stores/error-codes-and-limits#limits|Limits]].


## Related Files

- [[external/roblox-creator-docs/cloud-services/data-stores/best-practices]] - Best practices for data stores.
- [[external/roblox-creator-docs/cloud-services/data-stores/error-codes-and-limits]] - Data store error codes and limits.
- [[external/roblox-creator-docs/cloud-services/data-stores/right-to-be-forgotten]] - Data store right to be forgotten (RTBF).
- [[external/roblox-creator-docs/cloud-services/data-stores/versioning-listing-and-caching]] - Data store versioning, listing, and caching.
- [[external/roblox-creator-docs/cloud-services/data-stores/index]] - Data stores.
- [[external/roblox-creator-docs/cloud-services/data-stores/data-stores-manager]] - Data Stores Manager.
- [[external/roblox-creator-docs/cloud-services/data-stores/player-data-purchasing]] - Implement player data and purchasing systems.
