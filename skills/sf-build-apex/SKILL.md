---
name: sf-build-apex
description: "Implement and review Apex classes, triggers, Batch, Queueable, Finalizer, invocable and REST services. Use for .cls and .trigger changes after scope or root cause is established."
---

# Build and Review Apex

Read [runtime contract](references/runtime-contract.md) before operating.

## Workflow

Before implementation, verify the approved feature-plan revision and relevant reuse decisions under the project lifecycle. For a new feature/enhancement without an approved plan, complete the plan and obtain approval before changing implementation. During review, compare the diff with requirement IDs, flag material deviations, and preserve approval history. At completion, update affected component records and handover with actual validation status.

1. Inspect existing frameworks, log services, tests, metadata and package versions. Preserve public contracts and match the supported API version; do not upgrade versions incidentally.

2. Describe required object and field APIs instead of guessing. Choose bulk-safe collection operations, selective queries, bounded work and a clear transaction boundary.

3. Declare sharing intentionally and choose database access modes explicitly where supported. Document narrowly justified system operations; test external and restricted personas.

4. Define success, failure and partial-success behavior. Catch only recoverable exceptions or add useful context and rethrow. Debug-only exception handling is insufficient for operational failures.

5. For async work, persist run/record status and correlate jobs. Handle retry limits, idempotency, callouts, locking, chain termination and Finalizer behavior. Logging in a rolled-back transaction is not durable.

6. Add behavior-focused tests, deploy metadata to a sandbox when authorized, run static analysis and relevant Apex tests, and capture actual outcomes. Report compilation and runtime checks as unrun if tools/orgs are missing.

## Sources and constraints

Read [source notes](references/sources.md) for official references and version caveats.

