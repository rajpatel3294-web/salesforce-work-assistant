---
name: sf-audit-org
description: "Inventory and compare Salesforce metadata, package versions, permissions and environment drift. Use for sandbox versus production analysis or a scoped org assessment."
---

# Audit Salesforce Orgs

Read [runtime contract](references/runtime-contract.md) before operating.

## Workflow

1. Identify explicit source and target orgs, purpose, retrieval timestamp and target API version. Begin read-only and record unavailable metadata types or permissions.

2. Use supported CLI/Metadata/Tooling APIs and retrieve scoped source. Inventory alone does not establish logic parity; compare Flow XML, validation formulas and Apex content when those matter.

3. Run the repository local snapshot utility for deterministic file-level changes after retrieval. Interpret hashes as byte changes, not proof of a behavioral difference.

4. Separate expected environment configuration from defects: credentials/endpoints, package versions, licenses, schedules, users and integration enablement.

5. Classify high-impact differences and trace consumers of affected fields/actions. Mark managed-package internals and dynamic references as blind spots.

6. Deliver a comparison with scope, exclusions, evidence, environment-specific exceptions and prioritized remediation. Do not mutate either org during an audit.

## Sources and constraints

Read [source notes](references/sources.md) for official references and version caveats.

