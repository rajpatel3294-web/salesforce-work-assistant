---
name: sf-investigate-issue
description: "Trace Salesforce errors, incorrect data, unexpected automation, debug logs and integration failures to evidence. Use for root-cause investigation before implementing a fix."
---

# Investigate Salesforce Issues

Read [runtime contract](references/runtime-contract.md) before operating.

## Workflow

Read relevant project records and revalidate them against current evidence. Inspect existing reusable services before proposing a fix. Distinguish root-cause confidence from missing metadata/logs. When the remedy is new development or an enhancement, hand off to an approved architecture plan before implementation.

1. Record expected and actual behavior, timestamp/timezone, actor type, environment, entry point and sanitized record/request correlation IDs. Do not copy raw production data into this repository.

2. Read the complete relevant implementation and metadata, including active Flow versions, validation rules, trigger handlers, permission paths and package boundaries. A class fragment cannot establish the whole transaction.

3. Build a chronological evidence table: observation, source file/line or log event, interpretation, confidence, and next discriminating check. Mark truncated logs and missing stages.

4. Separate symptom, proximate failure and underlying cause. Maintain competing hypotheses until evidence distinguishes them; a restart restoring service does not identify a root cause.

5. Use a minimal sandbox reproduction with matching persona and inputs. Trace async jobs and downstream outcomes separately from the initiating transaction.

6. Propose the smallest durable fix and a regression matrix. Include alternative explanations, side effects, recovery and observability. Hand implementation to the appropriate skill only after enough evidence exists.

## Sources and constraints

Read [source notes](references/sources.md) for official references and version caveats.

