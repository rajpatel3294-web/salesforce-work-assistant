# Source notes

Research date: 2026-10-11 UTC (2026-10-10 America/New_York). Recheck release-sensitive behavior before implementation.

- [Pub/Sub Event Message Durability](https://developer.salesforce.com/docs/platform/pub-sub-api/guide/event-message-durability.html): Platform event/CDC retention and replay behavior; replay identifiers are opaque positions, not business deduplication keys.

- [Processing Events with Salesforce Connector](https://docs.mulesoft.com/salesforce-connector/latest/salesforce-connector-processing-events): Replay options and persistent Object Store behavior; match guidance to deployed connector version.

- [Salesforce Connector Reference](https://docs.mulesoft.com/salesforce-connector/latest/salesforce-connector-reference): Reconnection and replay configuration; streaming types have different semantics.

These links support the platform guidance; local workflow design is original engineering guidance. No live-org validation is implied.

