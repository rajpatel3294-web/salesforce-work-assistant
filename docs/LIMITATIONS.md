# Known limitations

- This is a skills/workflow repository, not a running Salesforce SaaS agent or browser extension.
- No repository can truthfully guarantee coverage of every Salesforce feature, industry
  add-on, managed package, org customization and future release. The catalog records breadth;
  the coverage map records depth and gaps.
- Upstream contents are pinned and unmodified, not all audited or executed. Some contain
  tool-specific assumptions, rigid defaults or incomplete operational templates.
- API/security behavior is version-sensitive. Do not treat all Apex as having the same
  default mode, or upgrade class versions without regression checks.
- Inventory and hash comparison do not infer a complete dependency graph or semantic parity.
- A successful parse of Flow XML does not establish deployability or correct runtime behavior.
- Neither this repository's tests nor synthetic scenario reviews establish org validation.
- Industry product routing is broad, but custom end-to-end implementations for every cloud
  are not supplied. Use official sources, upstream skills and a product-specific validation plan.
- Project-specific records must be verified before use and retained in approved private storage.
- CI checks repository structure and local tools only; it holds no Salesforce credentials.
- GitHub Projects boards and ChatGPT Projects are separate products. This repository is a
  standalone project; neither type of external project container is created by these files.

