---
name: sf-operate-marketing
description: "Investigate or design Marketing Cloud Engagement and Account Engagement integrations, journeys and audience operations. Use for SFMC REST/SOAP, data extensions, subscriber keys and marketing automation."
---

# Operate Marketing Cloud

Read [runtime contract](references/runtime-contract.md) before operating.

## Workflow

1. Identify Engagement versus Account Engagement versus another Marketing product. Record tenant, business unit, endpoint, package scopes, contact/subscriber identity and consent source.

2. Map CRM synchronization, data extensions, entry events, audience filters, journey versions, schedules and suppression/unsubscribe behavior.

3. Inspect actual API contracts and operation scopes. Do not reuse CRM SOQL or authentication assumptions for Marketing Cloud data extensions.

4. Use test audiences and preview/test mechanisms. Separate authoring or validation from journey activation, publication and sending to recipients.

5. Check duplicate entry, retries, consent changes, timezone, retention and failed automation recovery. Avoid exposing subscriber data in logs.

6. Deliver mapping, tested audience criteria, API evidence, activation prerequisites and rollback/stop limitations. Sending requires authorization for the actual audience and content.

## Sources and constraints

Read [source notes](references/sources.md) for official references and version caveats.

