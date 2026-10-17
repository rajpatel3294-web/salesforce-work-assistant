---
name: sf-package-solution
description: "Plan Salesforce unlocked or managed packaging, namespace boundaries, dependencies, upgrades and AppExchange preparation. Use for reusable package delivery and multi-org distribution."
---

# Package Salesforce Solutions

Read [runtime contract](references/runtime-contract.md) before operating.

## Workflow

1. Identify packaging model, namespace, Dev Hub/project setup, dependency versions, target editions and ownership of subscriber configuration.

2. Inventory packageable metadata and unsupported/configuration-only steps. Separate secrets and environment-specific values from the package.

3. Define install/upgrade/uninstall behavior, public/global API compatibility, data migration and backward compatibility. Never widen class visibility merely for convenience.

4. Test fresh install and upgrade paths in representative clean orgs, plus permission assignment, feature requirements and missing dependencies.

5. Run current static analysis and document justified security exceptions. An analyzer pass is not an AppExchange security review approval.

6. Deliver dependency manifest, version strategy, release notes, post-install checklist and observed test results. Confirm distribution visibility before publishing.

## Sources and constraints

Read [source notes](references/sources.md) for official references and version caveats.

