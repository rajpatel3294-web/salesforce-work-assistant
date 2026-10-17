# Source notes

Research date: 2026-10-11 UTC (2026-10-10 America/New_York). Recheck release-sensitive behavior before implementation.

- [Record-Triggered Automation](https://architect.salesforce.com/docs/architect/decision-guides/guide/record-triggered.html): Choose Flow, Apex, or a hybrid from automation density, complexity and maintainability.

- [Secure Apex Classes](https://developer.salesforce.com/docs/platform/lwc/guide/apex-security): API-version-aware database access modes; sharing does not by itself enforce CRUD/FLS.

- [Pub/Sub Event Message Durability](https://developer.salesforce.com/docs/platform/pub-sub-api/guide/event-message-durability.html): Platform event/CDC retention and replay behavior; replay identifiers are opaque positions, not business deduplication keys.

These links support the platform guidance; local workflow design is original engineering guidance. No live-org validation is implied.

