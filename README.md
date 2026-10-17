# Salesforce Engineering Hub

**An evidence-driven workspace for Salesforce development, investigation and delivery.**

Version 0.2.0 · Research baseline: October 10, 2026 (New York).

| Foundation | Custom workflows | Execution model |
| --- | --- | --- |
| 246 upstream Salesforce skills, pinned to an exact commit | 20 original engineering workflows | Local-first; explicit org connection for runtime checks |

Start with [Getting Started](docs/GETTING_STARTED.md), browse the [Coverage Map](docs/COVERAGE.md),
or choose a task in the [Skill Catalog](catalog/README.md).

## What this project does

- Routes broad Salesforce tasks to focused skills and primary documentation.
- Investigates issues from code, metadata, logs and reproducible evidence.
- Guides Apex, Flow, LWC, security, CPQ, integrations, testing and releases.
- Adds product routing for Sales, Service, Marketing, Data 360, Agentforce, Commerce,
  Field Service, OmniStudio and industry clouds.
- Applies project-specific requirements from approved local context records.
- Provides deterministic local metadata inventory/diff tools, capability checks and CI.

**Breadth is not universal certification.** Upstream coverage varies by product and
some skills require Vibes-only or product-specific tools. Custom workflows have local
structural validation; no Salesforce org is connected or production behavior certified.
See [Validation](docs/VALIDATION.md) and [Known Limitations](docs/LIMITATIONS.md).

## Quick start

```bash
git clone --recurse-submodules https://github.com/rajpatel3294-web/salesforce-work-assistant.git
cd salesforce-work-assistant
python scripts/doctor.py
python scripts/validate_repo.py
python -m unittest discover -s tests -v
```

The `vendor/sf-skills` Git submodule contains the complete upstream repository at the
recorded commit. A normal clone without submodules does **not** download that content:

```bash
git submodule update --init --recursive
```

Open this repository in a skill-capable coding assistant and select a local skill,
or install only the custom skills you need using [the installer](docs/GETTING_STARTED.md).
The GitHub connector alone does not install skills or authenticate Salesforce.

## Suggested requests

> Use sf-investigate-issue to trace why a Case never reaches the downstream repair system.

> Use sf-engineer-cpq to define and verify clone parity before changing quote automation.

> Use sf-review-portal to test that Distributor A cannot download Distributor B's certificate.

> Use sf-review-automation to find every writer of Quote expiration and explain the final value.

## Navigate

| Resource | Purpose |
| --- | --- |
| [Architecture](docs/ARCHITECTURE.md) | Repository layers and operating model |
| [Capabilities](docs/CAPABILITIES.md) | What works offline and what needs tools |
| [Research](research/REVIEW.md) | Findings, sources and design decisions |
| [Roadmap](docs/ROADMAP.md) | Prioritized project work and acceptance criteria |
| [Templates](templates/) | Investigation, decision and release records |
| [Evaluations](evals/README.md) | Synthetic scenarios and evaluation process |
| [Security](SECURITY.md) | Private evidence and access boundaries |
| [Contributing](CONTRIBUTING.md) | Maintaining and validating this collection |

This is an independent engineering project, not an official Salesforce product.
Upstream ownership and license notices remain intact. See [Third-party notices](THIRD_PARTY_NOTICES.md).


## Personal work assistant
See [Claude Code setup and acceptance tests](docs/CLAUDE_CODE_SETUP.md) for architecture approval,
reuse analysis, plan-based implementation, Jira drafts and persistent project records.

## Install through Claude's plugin marketplace

Add this marketplace in Claude's Plugins interface:

```text
rajpatel3294-web/salesforce-work-assistant
```

Sync the marketplace, then install **salesforce-work-assistant** from it. Adding a
marketplace and installing its plugin are separate steps. In Claude Code you can use:

```text
/plugin marketplace add rajpatel3294-web/salesforce-work-assistant
/plugin install salesforce-work-assistant@salesforce-work-assistant
```

Start a new session after installation and select the namespaced skill:

```text
/salesforce-work-assistant:sf-route-work
```

The plugin packages the 20 custom skills in skills/. It does not authenticate to
Salesforce or automatically install the 246 upstream catalog entries. Marketplace
installation does not load the root CLAUDE.md as project instructions; each custom
skill includes its own runtime and architecture lifecycle guidance. Use the setup
guide for company-project instructions. Avoid installing duplicate copies of the
same skills through both the plugin and the manual copy installer.
