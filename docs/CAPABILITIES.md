# Capability matrix

| Capability | Offline | Additional requirement | Evidence of completion |
| --- | --- | --- | --- |
| Read source and design a fix | Yes | Supplied or retrieved files | Findings with locations |
| Inventory/hash diff metadata | Yes | Local source directories | JSON snapshot/diff |
| Run this repository's checks | Yes | Python 3.10+ | Actual test output |
| Retrieve current org metadata | No | SF CLI/API, authenticated explicit org | Retrieval results and scope |
| Compile Apex / validate Flow semantics | No | Salesforce target and supported CLI/API | Validation job result |
| Run Apex tests | No | Deployed test code, authenticated target | Test run and coverage scope |
| Run LWC Jest | Locally possible | Relevant project Node dependencies | Actual Jest output |
| Prove portal access | No | External test personas and target site | Positive/negative access tests |
| Run Code Analyzer | Locally possible | SF CLI plus compatible analyzer/engines | Actual analysis output |
| Upstream Flow generation | No | execute_metadata_action MCP pipeline | Pipeline result and org validation |
| CPQ pricing / Advanced Approvals | No | Correct installed package and sandbox | Package/API business results |
| Mule runtime recovery | No | Mule project, connector version, test runtime | Failure-injection/replay results |
| Agentforce evaluation | No | Enabled compatible agent and DX/API | Evaluation result identifiers |
| Marketing sends/activation | No | Correct tenant/scopes and user authorization | Authorized operation results |

Missing tools do not mean an entire task must stop: finish useful offline work and
report which checks remain unexecuted. Never use an unverified substitute silently.
Scripts in this repository do not log into, query, or mutate an org.

