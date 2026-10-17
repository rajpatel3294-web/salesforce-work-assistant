---
name: sf-design-architecture
description: "Plan new Salesforce development or enhancements, review architecture and evaluate reuse. Inspect current systems, produce a versioned architecture plan with acceptance criteria, and obtain approval before implementation."
---

# Design Salesforce Architecture

Read [runtime contract](references/runtime-contract.md) before operating.

## Workflow

1. Read the project lifecycle. Inspect current components and project records before designing. Build an evidence-backed reuse/extend/new comparison and identify incomplete retrieval scope.

2. Use [feature plan](assets/feature-plan.md) and [decision record](assets/decision-record.md) as templates in the target company's docs/assistant directory. Assign requirement IDs, map them to components/tests, and specify preserved behavior.

3. Present the architecture for explicit approval before implementation. Record the approved revision and actual approval reference. If already approved for the same scope, continue without asking again.

1. Define business outcomes, actors, volume, peak load, data sensitivity, latency, recovery objectives, budget and ownership. List assumptions as assumptions.

2. Map systems of record, transaction boundaries, synchronous and asynchronous paths, permission boundaries and failure recovery responsibilities.

3. Compare standard configuration, Flow, Apex, middleware and external services against requirements. Prefer supported capabilities and maintainability; avoid rewriting a functioning architecture without evidence.

4. Model duplicate delivery, partial completion, contention, limits, external outages, API version changes and data reconciliation.

5. Write a decision record with options, trade-offs, chosen approach, rejected alternatives, operational cost, migration and reversal strategy.

6. Link every material claim to the relevant official source and target version. Deliver scoped implementation increments with measurable acceptance criteria.

## Sources and constraints

Read [source notes](references/sources.md) for official references and version caveats.

