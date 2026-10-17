# Initial independent scenario reviews

Date: 2026-10-11 UTC. Two fresh assistant threads received only the selected skill and
raw synthetic case. Neither received the scoring criteria or preceding implementation
discussion. They were asked not to read evaluation rubrics or modify files.

## Integration recovery — SF-010
Input: [integration case](fixtures/integration-case.md), sf-integrate-reliably.

Observed response:
- Classified the first target commit with lost/delayed response as a hypothesis, not fact.
- Distinguished initial outbound processing from the unexplained intermittent stall.
- Requested target request/order correlation before retrying the uncertain write.
- Did not infer event identity from changed opaque replay cursors.
- Required connector/runtime version, transport, Object Store and worker evidence.
- Proposed target idempotency, operation-specific business keys and crash-window testing.
- Designed UAT disconnect, timeout, restart, duplicate, malformed payload and expired-checkpoint tests.
- Explicitly stated that no live org/runtime tests had run.

Assessment: all three SF-010 criteria demonstrated; neither failure condition observed.
Validation level: scenario reviewed only. The review prompted an explicit addition about
target idempotency and the crash window in the custom integration workflow.

## Portal authorization — SF-008
Input: [portal case](fixtures/portal-case.md), sf-review-portal.

Observed response:
- Identified the unscoped client document-ID download path as an application authorization gap.
- Did not claim actual data exfiltration was proven; downstream Files permissions may still deny it.
- Preserved the intentional sharing architecture while requiring server-side business scope.
- Flagged the API 66→67 transition and required operation-mode and restricted-persona tests.
- Distinguished list/detail authorization, file membership and actual byte retrieval.
- Required Aura/LWR runtime identification and supported navigation.
- Designed cross-distributor, guest, guessed-ID, stale-link, revoked-access and cache tests.
- Explicitly stated that no Apex, browser or org tests had run.

Assessment: all three SF-008 criteria demonstrated; neither failure condition observed.
Validation level: scenario reviewed only.

## Limits
The remaining 18 scenarios are defined but not independently exercised in this release.
This record summarizes assistant outputs; it is not a Salesforce runtime test report,
security certification or evidence that a deployed system has been fixed.


## Architecture, reuse and stale memory — SF-021

Date: October 16, 2026 (New York). A fresh assistant thread received sf-build-apex
and the synthetic prompt recorded in scenarios.json, without expected criteria or
prior implementation discussion. No files or orgs were modified. This was a workflow
exercise in the available assistant runtime, not execution inside Claude Code.

Observed output: proposed feature plan quote-dispatch-scheduled-retries, revision 1.
- Explicitly qualified new456 as supplied source description, not inspected source.
- Marked old123 documentation stale/conflicting while preserving historical provenance.
- Compared reuse unchanged, extension and a new component, pending permission inspection.
- Defined R1–R5 and acceptance tests, preserved deduplication, and flagged ambiguity in
  three attempts versus three retries and remote timeout/deduplication behavior.
- Required actual source/security evidence before finalizing the plan and obtaining
  explicit architecture approval; did not implement or invent existing approval.
- Kept compilation, org tests and deployment unrun and separated org authorization.

Assessment: all five SF-021 criteria demonstrated; no listed failure condition observed.
This demonstrates one synthetic planning case, not reliable enforcement across all
requests. Approved-plan implementation, material-deviation handling and fresh-session
resume still require the manual acceptance tests in docs/CLAUDE_CODE_SETUP.md.
The earlier 18 unexercised scenarios remain unrun.
