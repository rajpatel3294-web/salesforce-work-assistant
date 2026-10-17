# Claude Code work assistant setup

This release extends the existing 20 workflows. It does not create a Salesforce
connection, enforce read-only access, or install anything on your Windows computer.
Use an employer-approved Claude account and company repository for company code.

## Install selected skills on Windows
Open PowerShell in the cloned skills hub. Git and Python 3.10+ must be available.
First update this checkout normally and initialize the pinned submodule. Preserve any
local changes; do not force/reset to update. Run:

```powershell
git pull --ff-only
git submodule update --init --recursive
py -3 scripts/validate_repo.py
py -3 -m unittest discover -s tests -v
```

Set the actual destination Salesforce project, which contains sfdx-project.json:

```powershell
$sfProjectPath = 'C:\Work\YourSalesforceProject'
$skillDestination = Join-Path $sfProjectPath '.claude\skills'
$selectedSkills = @('sf-route-work', 'sf-design-architecture', 'sf-investigate-issue', 'sf-build-apex', 'sf-test-behavior', 'sf-release-change')
foreach ($skill in $selectedSkills) {
  py -3 scripts/install_skills.py --skill $skill --destination $skillDestination
  if ($LASTEXITCODE -ne 0) { throw "Skill preflight failed: $skill" }
}
```

Review the dry-run paths. To copy the selected skills:

```powershell
foreach ($skill in $selectedSkills) {
  py -3 scripts/install_skills.py --skill $skill --destination $skillDestination --apply
  if ($LASTEXITCODE -ne 0) { throw "Skill installation failed: $skill" }
}
```

Existing skill directories are deliberately rejected. For an upgrade, inspect the
installed version and local customizations, back it up outside .claude/skills, then
remove/move only the reviewed old skill directory before installing its replacement.
Never delete the entire .claude directory. An interrupted loop may leave some skills
installed; inspect them before retrying. Add CPQ, portal, integration or other skills
with the same installer when those tasks need them.

## Activate project instructions and records
Open the company Salesforce project in VS Code, install the official Anthropic Claude
Code extension and sign in. Merge the contents of templates/CLAUDE.project.md from this
hub into that project's CLAUDE.md. Preserve existing instructions; do not overwrite them.
Copy the missing INDEX.md, system-overview.md, component-catalog.md and handover.md
from the installed sf-route-work/assets directory into docs/assistant. Keep feature-plan
and decision-record templates in assets; instantiate them only for actual work.
Review and version company-specific records only in the approved company repository.

Start a fresh Claude session. Verify the project instructions are loaded and that
/sf-route-work and /sf-design-architecture appear in the skill menu. Inspect the
installed paths if they do not. GitHub storage alone does not activate skills.
Project skills use .claude/skills/<name>/SKILL.md; their names become slash commands.
The agents/openai.yaml metadata is for compatible OpenAI tooling, not required by Claude.

## Permissions and sandbox
Use manual tool approvals initially. Review shell commands rather than allowing every
sf command. Plan files and instructions are not access-control enforcement. Use a
least-privilege Salesforce identity and isolated credentials where stronger boundaries
are required. A system administrator login remains powerful even in an investigation.
Verify the explicit sandbox identity; use current CLI help for query/retrieval commands.
Do not print full auth details. Preserve local edits and review retrieval conflicts.
This setup intentionally does not modify permissions, log in or run org commands.

## First tests (offline before sandbox)
1. /sf-route-work Inspect this local project and prepare a scoped system overview and
   reusable component catalog. No org commands, implementation edits or deployment.
2. /sf-design-architecture Plan an enhancement using existing components where suitable.
   Record requirements, alternatives and acceptance tests. Wait for my plan approval.
3. After inspecting a real plan, explicitly approve its feature ID and revision for
   local implementation. Verify changes map to the requirements; org actions remain separate.
4. /sf-route-work Review my changes against the approved plan, prepare validation and
   draft a Jira update. Do not post it or deploy.
5. /sf-route-work Save a handover. In a fresh session ask it to resume and check whether
   it finds the saved plan, validates source freshness and identifies pending tests.
6. Change a source component or present a conflicting old note. Verify it reports the
   discrepancy instead of assuming memory is authoritative. Request a material design
   change and verify it records a revised plan before implementation.

Expected: no invented approvals, no silent plan deviations, no overwritten user edits,
no claim of org validation from local checks, and project records retained across sessions.
Live Claude execution and sandbox validation must be recorded on your machine; local
repository checks cannot prove those behaviors.

## Official references
- [Claude Code in VS Code](https://code.claude.com/docs/en/vs-code)
- [Skills and project installation](https://code.claude.com/docs/en/skills)
- [Project instructions and memory](https://code.claude.com/docs/en/memory)
- [Tool permissions](https://code.claude.com/docs/en/permissions)

Documentation checked October 16, 2026. Verify current documentation if the interface changes.
