# Research and design review

Research date: 2026-10-11 UTC / 2026-10-10 America/New_York.
Method: inspect Salesforce's repository and selected workflows/templates; consult primary
Salesforce developer/architect and MuleSoft documentation. The source register is
[sources.json](sources.json). This is a targeted engineering review, not a full audit of
every upstream file. No production or sandbox connection was used.

## Findings that shaped this project

| Finding | Evidence | Design response |
| --- | --- | --- |
| Upstream is broad but changes frequently | sf-skills README and catalog | Pin exact commit; review updates instead of following main at runtime |
| Flow generator requires a specific MCP pipeline | upstream automation-flow-generate/SKILL.md | Explicit capability preflight and a separately authored source-based Flow workflow |
| Generic async template catches exceptions with debug-only logging | upstream platform-apex-generate/assets/queueable.cls | Require observable failure state, durable logging and retry reconciliation |
| Org inventories do not establish complete behavioral parity | dx-org-analyze collection-details reference | Compare retrieved source and inspect business semantics; label local hash diffs accurately |
| Apex security defaults vary by API version | official Secure Apex Classes page | Record class versions and access modes; test upgrades and restricted personas |
| CPQ managed-package API is distinct from Revenue Cloud | official CPQ API introduction | Identify product before choosing models or APIs |
| Replay position is not a universal event identity | Pub/Sub Event Message Durability | Separate cursor recovery, deduplication and business reconciliation |
| Mule replay settings depend on source/connector behavior | Salesforce Connector docs | Require actual runtime/connector version and checkpoint evidence |
| File preview behavior depends on UI container | LWC Open Files documentation | Validate Experience Cloud download flows in the real site runtime |
| Static analysis and Agentforce batch evaluations provide different evidence | Code Analyzer and Agentforce Testing API docs | Record actual tool results; no readiness claims from self-assigned scores |

## Source conflicts and version scope
Search results and older articles can describe different API defaults or event retention.
Use documentation specific to the deployed version and event type. In particular, do not
apply a generic legacy PushTopic retention description to Pub/Sub platform events/CDC.
Current official Pub/Sub guidance describes a 72-hour retained stream for platform events
and CDC, but recovery design must also handle maintenance/reset and expired positions.

## Why the design is a companion repository
The complete upstream remains in an unmodified Git submodule, with its original license
and history. The custom layer adds cross-component diagnosis, explicit capabilities,
business invariants and verification records. This limits merge conflicts and avoids
pretending that a newly written collection replaces all product expertise.

## Research boundary
The source register documents consulted references, not an exhaustive survey of every
Salesforce product. Broad cloud entries use a documented research-and-routing workflow;
new integrations and specialist implementations require their own current-source review.

