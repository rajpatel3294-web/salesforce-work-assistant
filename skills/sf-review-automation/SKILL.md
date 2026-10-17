---
name: sf-review-automation
description: "Investigate, design or change Salesforce Flow, validation rules, approval dependencies and trigger interactions. Use for automation conflicts, expiration overwrites, recursion and Flow metadata."
---

# Review and Build Automation

Read [runtime contract](references/runtime-contract.md) before operating.

## Workflow

1. Retrieve active versions and all writers of the affected fields. Map before-save, trigger, validation, after-save and async boundaries using current order-of-execution documentation for the target release.

2. Record entry criteria, changed-field checks, Flow trigger order, execution context, scheduled paths, subflows and invocable dependencies. Never promise that a numeric order makes an automation globally last.

3. Choose before-save logic for suitable same-record updates; use an after-save or async path only when required. Preserve business distinctions between create, update, clone and integration entry points.

4. For Vibes generation, verify the upstream MCP pipeline exists before selecting it. If absent, use this independent source-based workflow: inspect retrieved XML, make a minimal schema-supported change, retain a diff and validate through Metadata API/SF CLI. XML parsing alone is not semantic validation.

5. Test criteria boundaries, nulls, bulk updates, recursion, actor permissions, timezones and interactions with existing rules. Confirm the intended active version in the target org.

6. Deliver changed elements, field-writer map, activation sequence, validation results, rollback plan and any remaining business decision.

## Sources and constraints

Read [source notes](references/sources.md) for official references and version caveats.

