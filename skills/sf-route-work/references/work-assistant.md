# Work assistant workflows

Apply the runtime contract and project lifecycle before task execution.
Use these requests with /sf-route-work; they are not separate installed commands.

## Review my changes
Read git status and diff plus relevant untracked files without staging or resetting
user work. Compare with the approved feature plan and current callers/permissions.
Report findings by severity with paths, evidence, requirement IDs and recommended fixes.
Separate verified defects from hypotheses; report review scope and missing evidence.

## Prepare validation and deployment
Use installed sf-test-behavior and sf-release-change when available. Prepare focused
behavior tests, affected regressions, dependencies/manifest, prerequisites and rollback.
Run only authorized checks. Distinguish local checks from org execution and preserve
job IDs, environment, time and results. Do not deploy merely to prepare a checklist.

## Draft Jira update
Read the investigation, current diff, feature plan and actual validation evidence.
Draft: issue/impact, confirmed findings, completed changes, test status, blockers and
next steps. Keep business language concise; offer technical detail when requested.
Do not invent ticket IDs, completion, approvals or test results. Draft only unless
sending/posting is explicitly authorized and a suitable connection is available.

## Save handover / resume / daily summary
Update docs/assistant/INDEX.md and handover.md using the bundled asset templates.
Link the feature ID and approved revision, changed files/commit, pending work,
executed and unexecuted checks, unresolved risks and next safe action. Update system
and component records only for inspected scope; mark hypotheses and stale entries.
On resume, verify the revision and working tree before relying on notes.
For a daily summary, summarize available records; do not imply inbox/Jira/calendar
access or unattended scheduling. Do not post or send the summary automatically.
