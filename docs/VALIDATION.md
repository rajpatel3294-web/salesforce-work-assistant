# Validation evidence

Initial local checks are recorded below. No Salesforce org, CPQ package, Mule runtime,
Marketing tenant or Agentforce agent was connected during creation.

| Check | Status | Scope |
| --- | --- | --- |
| Custom skill structural checks | Passed | 20 folders, skill-creator validator, local links and lock consistency |
| Local utility tests | Passed | 8 tests covering snapshots, comparison and selective install |
| Upstream catalog generation | Passed | 246 skills at the pinned commit |
| Independent synthetic workflow reviews | Passed criteria | Two scenarios; see ../evals/RESULTS.md; other 18 not run |
| Salesforce compilation/tests | Not run | Requires authenticated test org |
| Portal external-user tests | Not run | Requires test site and personas |
| CPQ/Mule/Marketing/Agentforce runtime checks | Not run | Requires corresponding test environments |
| GitHub Actions run | Not run | Requires repository publication and runner execution |

Run local checks:
```bash
python scripts/validate_repo.py
python -m unittest discover -s tests -v
python scripts/doctor.py
```

Local metadata snapshot example (use retrieved source, not raw production evidence):
```bash
python scripts/metadata_snapshot.py /path/to/retrieved-source --output artifacts/before.json
python scripts/compare_snapshots.py artifacts/before.json artifacts/after.json
```
The snapshot command exits 2 when XML parsing errors exist. It omits file bodies but
metadata names can still be private. The comparison refuses invalid snapshots.


## Work assistant update — October 16, 2026

Repository validation passed with the pinned upstream checkout. All 9 local utility
tests passed, including copying all 20 skills into a clean destination and resolving
every bundled Markdown reference inside each individual installed skill. Git diff
whitespace checks passed. See the current synthetic review record in evals/RESULTS.md.
Claude Code execution on Windows and live sandbox validation remain unrun. These
checks validate packaging and workflows, not enforcement of approval or org permissions.
