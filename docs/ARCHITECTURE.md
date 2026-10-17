# Architecture

The repository has three maintained layers:

1. **Pinned foundation** — `vendor/sf-skills` is the full upstream Git submodule.
   `upstream.lock.json` records its exact commit and declared inventory.
2. **Custom workflows** — `skills/` contains original, self-contained instructions
   with runtime contracts and primary references. These address operational gaps.
3. **Evidence tooling** — `scripts/`, `tests/`, `evals/` and templates support repeatable
   offline checks and honest runtime-validation reporting.

Request handling: determine product and environment → collect evidence → choose a
scoped workflow → implement where authorized → verify → report actual outcomes.
No background deployment, autonomous production mutation or credential handling is built in.

## Choosing between overlapping skills
Use custom investigation/CPQ/portal/reliability workflows for their stated operational
tasks. Load an upstream generation skill only after inspecting its prerequisites.
The custom Flow workflow is independent of the upstream MCP-only generation workflow;
do not claim to execute that upstream workflow without its required tool.

## Upstream updates
Create a branch, fetch upstream, inspect the diff and changed tool/API requirements,
update the submodule commit and lockfile together, regenerate the catalog, validate,
and run impacted scenario tests. Do not track upstream main automatically at execution time.
Preserve the upstream license. Never overwrite custom skills during an update.

