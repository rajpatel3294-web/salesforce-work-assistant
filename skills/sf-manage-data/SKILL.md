---
name: sf-manage-data
description: "Plan SOQL, data migration, deduplication and controlled bulk changes. Use for data repair, import/export, reconciliation and query design."
---

# Manage Salesforce Data

Read [runtime contract](references/runtime-contract.md) before operating.

## Workflow

1. Describe schema and relationships, key fields, required values and ownership. Establish source of truth, expected counts and operation permissions.

2. Write selective scoped queries with explicit fields and bound values. Validate relationship names; avoid guessing object APIs or treating a page-layout requirement as the entire data-validation model.

3. For migration, stage parent-child dependencies, external IDs, mapping, timezone/currency transforms and duplicate rules. Choose API and batch size from volumes and automation behavior.

4. Separate selection from mutation and freeze an auditable input manifest. Capture before-images, row-level results and errors in approved storage.

5. Make retries idempotent, reconcile successes before reprocessing and protect against stale input and concurrent changes. Record source-to-target mappings.

6. Validate counts, uniqueness, relationships, totals and representative business outcomes. Never claim rollback of sent messages or external transactions from a database restore.

## Sources and constraints

Read [source notes](references/sources.md) for official references and version caveats.

