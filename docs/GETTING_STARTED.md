# Getting started

## 1. Clone and check
Install Git and Python 3.10+ using their official distributions. Clone this
repository with `--recurse-submodules`, or initialize submodules after cloning.
Run `python scripts/doctor.py`, `python scripts/validate_repo.py` and the unittest suite.
The doctor reports missing tools; it does not install software or access credentials.

## 2. Select custom skills
Open the project in a compatible assistant and point it to `skills/<name>/SKILL.md`.
For an assistant that discovers skills from a directory, copy only selected skills:

```bash
python scripts/install_skills.py --list
python scripts/install_skills.py --skill sf-investigate-issue --destination /absolute/path/to/assistant/skills
```

The installer defaults to a dry-run. Add `--apply` after reviewing its destination.
Existing skill directories are never overwritten. Use your assistant's documented
skill directory; this project does not assume all assistant products use the same one.
References are bundled inside each custom skill so selective installation works.
The router can also be used in this repository to access the complete catalog.

## 3. Use upstream specialist skills
Read the relevant SKILL.md under vendor/sf-skills/skills and check its dependencies.
Salesforce documents `npx skills add forcedotcom/sf-skills` as an installation option,
but that follows the installer's upstream selection, not necessarily this pinned
baseline. For reproducibility use the checked-out submodule and the host's supported
local installation workflow. Do not execute every upstream script automatically.

## 4. Connect a sandbox when runtime work is needed
Install Salesforce CLI from Salesforce's official distribution and check `sf --version`.
Use its supported web/OAuth login flow for the chosen sandbox. Never paste tokens or
passwords into chat, source files or issues. Confirm alias, org identity and environment
before retrieval or deployment. Use current CLI help for operation flags.

Start with metadata retrieval and read-only investigation. Record the retrieval scope;
no wildcard manifest can guarantee complete coverage of all metadata or package internals.
Only run mutating operations within the user's explicit task scope.

## 5. First practical task
Retrieve one affected object's automation and related Apex, then ask the assistant to
use sf-investigate-issue. Capture its report in the investigation template. Follow with
implementation and relevant tests, keeping unexecuted checks visibly pending.

## Windows
The repository's Python scripts use pathlib and subprocess argument arrays. Use
`py -3` instead of `python` if that is how Python is installed. Individual upstream
skills may require Bash, jq, Node, Java or other dependencies; review each skill first.


## Personal work assistant
See [Claude Code setup and acceptance tests](CLAUDE_CODE_SETUP.md) for architecture approval,
reuse analysis, plan-based implementation, Jira drafts and persistent project records.
