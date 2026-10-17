---
name: sf-operate-data-analytics
description: "Review Data 360/Data Cloud ingestion, identity resolution, activation, CRM Analytics, reports and Tableau integration. Use for data lineage, incorrect aggregates and analytics access."
---

# Operate Data and Analytics

Read [runtime contract](references/runtime-contract.md) before operating.

## Workflow

1. Identify product, data space, source systems, schema, lineage, ingestion mode, refresh frequency and access model. Distinguish CRM reports from Data 360 queries and analytics datasets.

2. For identity resolution, inspect match and reconciliation rules and examine false merges and missed matches using approved anonymized samples.

3. For reports, distinguish row count from unique entity count and inspect joins, grouping and filters before changing a formula or chart.

4. For activation, verify consent, destination, identity mapping and audience membership. Treat export or activation as a separate authorized action.

5. Measure freshness, completeness, duplicates, reconciliation totals, persona access and cost/limits. Record sample bias and missing source data.

6. Deliver lineage diagram or table, semantic definitions, transformation changes and source-to-output checks. Use upstream analytics skills only after checking their product-specific tools.

## Sources and constraints

Read [source notes](references/sources.md) for official references and version caveats.

