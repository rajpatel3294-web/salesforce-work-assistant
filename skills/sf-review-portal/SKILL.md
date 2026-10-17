---
name: sf-review-portal
description: "Build and investigate Experience Cloud LWC, distributor visibility, assets, entitlements and Salesforce Files. Use for portal search and certificate access or download failures."
---

# Review Experience Cloud Portals

Read [runtime contract](references/runtime-contract.md) before operating.

## Workflow

1. Identify Aura versus LWR runtime, external license, user/contact/account relationships, component entry points, Apex access and the approved business access model.

2. Trace record access and file access independently. Start from the verified business record link; inspect ContentDocumentLink, ContentDocument and the intended version without assuming email attachments are authoritative.

3. Enforce server-side scope for list, detail and download requests. Reject arbitrary record or document IDs outside that scope; prevent cached data from crossing users or distributors.

4. Verify runtime-supported navigation/download behavior from current documentation. Test real external users, not just an administrator or local component test.

5. Cover permitted distributor, different distributor, missing relationship, anonymous user, stale link and guessed file ID. Test both visibility and actual retrieval.

6. Keep retrieval and generation separate. Do not expose a certificate request or generation action unless it belongs to the approved release. Deliver the authorization matrix and evidence for every route.

## Sources and constraints

Read [source notes](references/sources.md) for official references and version caveats.

