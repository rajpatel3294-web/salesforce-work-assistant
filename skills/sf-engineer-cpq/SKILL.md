---
name: sf-engineer-cpq
description: "Investigate or implement Salesforce CPQ quoting, pricing, cloning, approvals, orders and document generation. Use for SBQQ managed package workflows and quote reissue; distinguish Revenue Cloud first."
---

# Engineer CPQ and Revenue Workflows

Read [runtime contract](references/runtime-contract.md) before operating.

## Workflow

1. Identify the product precisely: Salesforce CPQ managed package, Revenue Cloud, Industries CPQ or standard Quotes. Record installed package/version, calculator plugins, price/product rules and custom automations.

2. Capture a manual baseline and expected invariants for header fields, lines, groups, bundle relationships, discount units, currency, term, pricebook, approvals, related parties and documents.

3. Use supported package APIs for pricing and quote persistence where applicable. A deepClone or raw DML operation does not prove parity with Clone with Related or complete recalculation.

4. Define an idempotency key and per-stage statuses for clone, calculate, approve, generate document and send. Reconcile partial completion before any retry; never resend merely because a later stage failed.

5. Preserve source/run linkage and approved source-update policy. Treat existing orders and missing required contacts as business decisions, not errors to bypass automatically.

6. Test representative bundle/discount/currency/approval cases against the manual baseline. Report semantic differences separately from expected system-generated fields. Never assume setting an approval bypass checkbox completes downstream document jobs.

## Sources and constraints

Read [source notes](references/sources.md) for official references and version caveats.

