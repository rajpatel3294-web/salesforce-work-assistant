# Contributing

Keep tasks scoped, source-backed and testable. Add a custom skill only for a meaningful
workflow; use product routing rather than duplicating vague prompts for every product name.
Each custom skill must have name/description frontmatter, a workflow, runtime contract,
primary references and at least one evaluation scenario in the shared scenario suite.

Run repository validation and local tests. For behavioral changes run relevant scenario
reviews without revealing expected answers to the evaluator. Record failures honestly.
Salesforce code changes need real target-org validation before claiming runtime success.

Do not change the upstream submodule without a reviewed update to upstream.lock.json
and catalog regeneration. Preserve license attribution and document tool dependencies.
Use a PR description with problem, change, evidence, compatibility and remaining risks.

