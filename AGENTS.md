# Repository operating instructions

Read README.md, docs/CAPABILITIES.md and the selected skill before work.
Use current primary Salesforce/MuleSoft documentation for version-sensitive decisions.
Treat vendor/sf-skills as pinned third-party source, not proof of tool availability.
Never modify that submodule as a shortcut to changing a custom workflow.
Use one authoritative workflow per task; resolve overlaps explicitly.

Keep sources, evidence and hypotheses distinguishable. Never claim org tests passed
without recorded results. Confirm explicit org identity before any operation.
No credentials, .sf/.sfdx auth stores, raw production logs, customer records or private keys
belong in this repository. Store evidence outside version control.

Run python scripts/validate_repo.py and python -m unittest discover -s tests -v
after changing scripts or skills. Structural validation is not Salesforce validation.
Run selected realistic evaluations when behavior or routing changes.

Keep custom skills self-contained for selective installation; preserve the runtime
contract and source references inside each skill. Document any portability limitations.
Do not deploy, send messages, activate agents, modify data or expand access beyond
the user's authorized scope. Continue authorized read-only work without redundant prompts.


For new development and enhancements, use the selected skill's project lifecycle:
inspect existing systems and reuse options, approve a versioned architecture plan,
implement against its requirements, record material deviations and update project
records. This request to maintain the skills hub authorizes its agreed workflow changes;
it is not approval of future Salesforce feature plans. Keep company records separate.
