# Coverage map

This map distinguishes available workflows from verified implementations. All 246 upstream skill entries are indexed; none is automatically certified for a target org. Custom workflows are designed and locally checked, with selected synthetic evaluations documented separately.

| Area | Depth in this release | Entry point | What still must be verified |
| --- | --- | --- | --- |
| Core platform, Apex, SOQL and metadata | Custom engineering + upstream implementation | sf-build-apex; platform-* | Compile/test results in the target org |
| Flow, validation and approvals | Custom impact review + upstream generation | sf-review-automation; automation-* | Active versions, dependencies, semantic validation; Vibes pipeline for upstream generator |
| LWC, Aura, SLDS and mobile UI | Custom portal review + upstream specialist skills | experience-*; design-systems-*; mobile-* | Actual runtime, Jest and persona tests |
| Security, sharing and identity | Custom access workflow + upstream configuration | sf-review-access; platform-sharing-* | Effective grants and explicit access-mode validation |
| Org management and DevOps | Custom audit/release + upstream tools | sf-audit-org; sf-release-change; dx-* | Connected org, supported CLI, release evidence |
| Sales and Service Cloud | Custom lifecycle workflow + upstream service skills | sf-operate-sales-service; sales-*; service-* | Enabled product features and end-to-end process tests |
| CPQ, Revenue Cloud and billing | Custom CPQ workflow; distinct product APIs | sf-engineer-cpq | Package/version-specific implementation; Revenue Cloud must not use SBQQ assumptions |
| Advanced Approvals and S-Docs | Custom stage and acceptance guidance | sf-engineer-cpq; sf-project-context | Vendor/package contracts and real document/send job checks; no universal S-Docs adapter bundled |
| REST, SOAP, events, CDC and MuleSoft | Custom resilience workflow + upstream integration | sf-integrate-reliably; integration-* | Connector versions, transport, schemas and runtime fault tests |
| Experience Cloud and partner portals | Custom authorization workflow + upstream site skills | sf-review-portal; experience-* | External personas, site runtime and document authorization |
| Marketing Cloud Engagement / Account Engagement | Custom product-aware workflow; limited upstream support | sf-operate-marketing; marketing-* | Tenant/BU scopes, consent, test audiences; product-specific code still required |
| Data 360 / Data Cloud | Custom lineage workflow + upstream skills | sf-operate-data-analytics; data360-* | Data spaces, ingestion, identity and activation validation |
| Reports, CRM Analytics and Tableau | Custom semantics workflow + upstream analytics | platform-report-generate; crm-analytics-*; tableau-* | Data access, dataset freshness, aggregation reconciliation |
| Agentforce and AI agents | Custom evaluation workflow + upstream agent skills | sf-evaluate-agentforce; agentforce-* | Compatible enabled agent, real evaluation runs and action tests |
| OmniStudio and Industries CPQ | Specialist routing + upstream implementation | omnistudio-* | Standard/managed runtime, namespace and dependency verification |
| Field Service | Specialist routing + upstream implementation | field-service-* | Scheduling, mobile, offline and license prerequisites |
| Commerce | Specialist routing; upstream emphasis on B2B | commerce-* | B2B/B2C stack distinction; dedicated B2C implementation not supplied |
| Education, Consumer Goods, Life Sciences, Insurance | Specialist routing + targeted upstream skills | education-*; consumer-goods-*; life-sciences-*; insurance-* | Only selected workflows; confirm actual feature coverage |
| Health, Financial Services, Nonprofit and other industry products | Research and routing coverage | sf-route-specialist-clouds | No claim of complete dedicated implementations; official product research required |
| Packaging and AppExchange | Custom lifecycle guidance + selected upstream skills | sf-package-solution; dx-pkg-* | Install/upgrade org tests and separate security review |
| Project-specific operational context | Custom historical acceptance profile | sf-project-context | Current metadata/business confirmation; no production evidence included |

For an unlisted feature, use sf-route-specialist-clouds to research the exact product and record a gap. Do not claim that a related skill implements it.

