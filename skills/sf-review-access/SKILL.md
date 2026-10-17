---
name: sf-review-access
description: "Review CRUD/FLS, sharing, Experience Cloud access, integration principals, credentials and Apex API version changes. Use for security-sensitive Salesforce design and code reviews."
---

# Review Salesforce Access

Read [runtime contract](references/runtime-contract.md) before operating.

## Workflow

1. Identify personas, their intended records/fields/actions and actual effective grants. Separate object permissions, field permissions, record sharing, Apex class access and custom business authorization.

2. Read class API versions and operation access modes. Current official documentation distinguishes API 66 and earlier from 67 and later; verify the target release and explicitly test an API-version upgrade.

3. Inspect every caller-supplied ID, dynamic query field/operator, download endpoint and admin action. Derive tenant/distributor scope server-side; do not trust hidden buttons or client filters.

4. Keep approved elevated-access architecture documented and narrowly scoped. Require evidence of business authorization and negative tests instead of mechanically replacing every without-sharing class.

5. Use supported credential storage and least-privilege integration users. Never commit tokens, org auth files, private keys or customer exports.

6. Deliver reproducible findings with affected persona, exploit preconditions, location, impact, corrective change and verification. Do not claim a full security certification from a static scan.

## Sources and constraints

Read [source notes](references/sources.md) for official references and version caveats.

