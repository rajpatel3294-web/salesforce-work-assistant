---
name: sf-test-behavior
description: "Create and assess Apex, LWC, Flow, integration and user acceptance tests. Use for test failures, coverage improvement and regression design without weakening business assertions."
---

# Test Salesforce Behavior

Read [runtime contract](references/runtime-contract.md) before operating.

## Workflow

Read the approved feature plan and map every acceptance criterion to a test or an explicit validation gap. Include preserved behavior and rejected regressions. Do not change business expectations to make tests pass. Report plan compliance separately from test execution status.

1. Derive assertions from requirements and known baseline behavior, not from the new implementation. Include positive, negative, permissions, bulk, duplicate and recovery scenarios where relevant.

2. Reuse org-appropriate test factories, create dependencies and resolve metadata names dynamically. Avoid hardcoded record IDs, SeeAllData dependence and artificial assertions used only to increase coverage.

3. Mock external boundaries. Test Queueable stages independently and verify chaining contracts; do not assume Test.stopTest executes a complete async chain. Respect Batch test execution constraints.

4. Use real browser/user acceptance checks for portal access and file download permissions; Jest alone cannot establish server authorization or production behavior.

5. Run focused tests first and expand to affected regressions. Record exact commands, target, timestamps, counts, failures, coverage scope and environment limitations.

6. Do not equate a coverage percentage with correctness. If unavailable, supply runnable tests and an explicit unexecuted status; never mark production-ready solely from static review.

## Sources and constraints

Read [source notes](references/sources.md) for official references and version caveats.

