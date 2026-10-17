---
name: sf-release-change
description: "Plan, validate and release Salesforce metadata and controlled data changes. Use for deployment failures, release sequencing, production rollout and rollback planning."
---

# Release Salesforce Changes

Read [runtime contract](references/runtime-contract.md) before operating.

## Workflow

Verify the implemented diff against the approved plan and decision records. List missing requirements, material deviations, and unexecuted acceptance checks before release. Architecture approval does not authorize deployment. Update environment-specific validation and handover after authorized release activity.

1. Identify exact commit, target org, manifest, dependencies, package versions, business window, release owner and permission changes. Confirm production explicitly rather than relying on a default org.

2. Separate metadata rollback from data recovery and external side effects. Export necessary before-images through approved storage; document irreversible actions and compensations.

3. Inspect installed CLI help and supported test levels. Validate the smallest complete change set with relevant tests; do not invent validation job IDs or claim a dry-run is a deployment.

4. Resolve dependencies as a graph. Permission sets may reference new Apex as well as fields; a universal objects-permissions-Apex ordering can be wrong.

5. For bulk data work, define canary, wave selection, eligibility, pause criteria, idempotency, reconciliation and checkpointed resume. Numeric wave size alone does not establish safety.

6. Execute only within user authorization and platform gates. Verify active Flow versions, permissions, scheduled jobs, async completion and business outcomes after deployment.

7. Produce a release record containing exact scope, validation/test evidence, actual outcomes and recovery instructions. Keep unknown checks explicitly pending.

## Sources and constraints

Read [source notes](references/sources.md) for official references and version caveats.

