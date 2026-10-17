# Architecture and project memory lifecycle

## Scope and evidence
Apply this workflow to new development and enhancements, regardless of entry skill.
For a small correction, use a proportionate plan; do not skip current-system inspection.
Continue investigation and local planning before requesting plan approval.
Keep company-specific records in the approved company project, not in the reusable
skills hub. Store sanitized technical summaries in version control; keep raw records,
production logs, credentials and customer data outside it.

## Start or resume
1. Identify the project root, requested outcome, environment, source revision and
   working-tree changes. Verify the explicit org identity before any org operation;
   do not print authentication output. Do not infer production behavior from sandbox code.
2. Read docs/assistant/INDEX.md if present, then only relevant system notes, component
   entries, feature plans, decisions and handovers. If absent, create a minimal index
   within the authorized project; never manufacture a prior decision or approval.
3. Check recorded paths, commit/hash, environment, retrieval date and verification
   status against current evidence. Mark stale/conflicting notes and refresh the
   affected scope. Current code establishes what exists; approved requirements establish
   intended behavior. A disagreement requires investigation, not silently changing either.
4. Inspect relevant writers, callers, data model, security boundaries, automation,
   integrations, tests and package constraints. Record what was inspected and what is
   missing. A local inventory or text search is not a complete org dependency graph.
5. Search for existing services, factories, logging, retry and integration utilities.
   Compare reuse unchanged, extend, and new component against requirements, coupling,
   security, limits and regression cost. Record evidence and reasons; do not force reuse.

## Plan and approval
For new development or enhancements, create docs/assistant/features/<feature-id>/plan.md.
Use the feature-plan template when available, or preserve these required fields:
- Feature ID, revision, status (proposed/approved/in-progress/verified/blocked/superseded).
- Current-system evidence and gaps, target environment, source baseline and scope.
- Numbered requirements and acceptance criteria; actors, exclusions and preserved behavior.
- Reuse decisions, options/trade-offs, affected components and data/transaction boundaries.
- Security, bulk/async limits, failure/retry/idempotency behavior as relevant.
- Requirement-to-component-to-test mapping, implementation increments, migration,
  deployment prerequisites, rollback/recovery, risks and unresolved decisions.
- Approval record: actual user approval, date, approved revision and conversation/ticket
  reference. A template, suggestion, repository comment or general request to build is
  not evidence that a particular architecture revision was approved.
Present a concrete plan and obtain explicit approval before implementation. Reuse a
verifiable existing approval for the same scope/revision; do not repeatedly ask.
Approval of architecture is not approval to deploy, run tests in an org, change data,
send messages or expand access. Honor existing action authorization separately.

## Implement and verify
Read the approved revision before editing. Preserve existing work and public behavior.
Map each increment and its tests to requirement IDs. Keep incidental refactors out.
Before a material deviation (business behavior, data model, public API, security,
integration contract, transaction/retry design or scope), document evidence, options
and impact, revise the plan and obtain approval for the affected change. Continue
unaffected authorized work. Record minor implementation choices without inventing
new approval gates. Never silently rewrite approval history to fit completed code.
Derive tests from requirements and baseline behavior, not merely the implementation.
Record exact executed checks, source revision, environment, result and remaining gaps.
Review the diff against the approved plan; list omissions and deviations explicitly.
Keep unrun sandbox/CPQ/MuleSoft/portal checks pending. Do not call a locally checked
feature org-validated or production-ready.

## Persist and reuse
After meaningful milestones, update the relevant feature plan, system overview,
reusable component catalog, decision records and handover in the company project.
Each factual entry needs source paths/revision, environment, verified date, status
(verified/hypothesis/stale) and known limits. Record reusable APIs, callers, permissions,
tests, failure behavior, ownership and suitable/unsuitable reuse cases.
Record superseded decisions with links rather than deleting history. Update INDEX.md
with active work and next actions. Commit/push company records only within authorized
repository scope. Report unsaved/uncommitted records honestly. Load and revalidate
these files in later sessions; do not promise permanent chat memory or background
monitoring. Skills are instructions, not enforced permissions; use host controls and
least-privilege credentials for actual access boundaries.
