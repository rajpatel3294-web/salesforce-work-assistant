---
name: sf-route-work
description: "Route Salesforce development, administration, architecture or incident work. Also use for reviewing changes, preparing validation, drafting Jira updates, saving handovers and resuming project work."
---

# Route Salesforce Work

Read [runtime contract](references/runtime-contract.md) before operating.

## Workflow

Start by reading the project lifecycle and the target project's docs/assistant/INDEX.md when available. For new development or enhancements route to sf-design-architecture before implementation; for an unexplained failure route to sf-investigate-issue. Load only installed relevant skills; do not assume this hub's catalog or sibling skills exist after selective installation.

For work-assistant requests use [work assistant workflows](references/work-assistant.md). They cover change review, validation preparation, Jira drafts and handover without needing external write integrations.

1. Identify the requested outcome, product, edition, namespace/package, environment, API version and available evidence. Infer obvious scope; ask only for missing facts that change the action.

2. Classify the task as investigate, design, implement, test, release, data operation or product research. Start investigation for an unexplained failure before proposing code.

3. Select the smallest set of local skills from the repository catalog. For specialist products consult the pinned upstream catalog and verify prerequisites before using its instructions.

4. Load the runtime contract and capability matrix. If a required tool is unavailable, produce a useful offline result and state exactly what remains unverified. Do not invent tool results or silently substitute a different product.

5. For novel areas, research official product documentation and record sources, dates and version constraints. Keep unverified proposals separate from confirmed behavior.

6. Finish with the outcome, changed components, evidence, test results and remaining action. A broad product catalog is not proof that every feature has been tested.

## Sources and constraints

Read [source notes](references/sources.md) for official references and version caveats.


## Project record templates
Use [index](assets/INDEX.md), [system overview](assets/system-overview.md),
[component catalog](assets/component-catalog.md), [feature plan](assets/feature-plan.md),
[decision record](assets/decision-record.md) and [handover](assets/handover.md).
Copy only missing records into the company project's docs/assistant directory.
Never replace existing project records with blank templates.
