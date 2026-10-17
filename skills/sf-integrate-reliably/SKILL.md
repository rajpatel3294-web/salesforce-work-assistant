---
name: sf-integrate-reliably
description: "Design and diagnose Salesforce REST/SOAP, Platform Events, CDC, Pub/Sub and MuleSoft connections. Use for intermittent delivery, timeout, replay, duplicate and recovery problems."
---

# Build Reliable Salesforce Integrations

Read [runtime contract](references/runtime-contract.md) before operating.

## Workflow

1. Inventory publisher, broker/channel, subscriber, Mule runtime, connector version, transport, credential method, target API and schema contract. Distinguish CometD from Pub/Sub.

2. Correlate source publication, subscriber receipt, transformation, outbound request, acknowledgement and business completion with timestamps. A restart is a recovery observation, not a diagnosis.

3. Inspect reconnection policy, backoff, token refresh, connection pools, persistent Object Store, checkpoints, concurrency and worker topology. Match settings to the deployed connector documentation.

4. Treat replay positions as opaque cursors. Use an appropriate stable event/business key for deduplication; do not use a replay ID as a universal unique key. Establish catch-up and reconciliation for events outside retention.

5. For uncertain request outcomes, check whether the target committed before retrying. Prefer target-enforced idempotency or an atomic operation key; a local ledger alone leaves a crash window after remote commit. Make the key distinguish legitimate repeat business operations. Retry only eligible transient failures, cap attempts, keep durable failed-work records and allow controlled replay.

6. Validate SOAP namespaces, ordering, optional versus nil fields and WSDL/XSD versions from actual payloads. Redact secrets and payload PII. Build from source with supported tools; do not label a patched archive production-ready without a reproducible build and contract tests.

7. Exercise disconnection, restart, duplicate delivery, slow target, malformed payload and expired checkpoint in UAT. Verify end-to-end business outcomes and backlog reconciliation.

## Sources and constraints

Read [source notes](references/sources.md) for official references and version caveats.

