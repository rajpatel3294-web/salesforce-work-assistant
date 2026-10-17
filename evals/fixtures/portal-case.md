# Synthetic portal change request

An Experience Cloud certificate component lists only the logged-in distributor's
Entitlements. Its Apex controller is intentionally declared without sharing.
The list query derives distributor scope from the current user's business relationship.
The download method accepts a ContentDocument ID supplied by the client and returns
a URL without checking whether that document belongs to an allowed Entitlement.
The new release also changes the Apex metadata version from 66.0 to 67.0.
The team has only tested using an internal administrator; no external persona tests ran.

User request: review this release and propose the necessary changes and acceptance tests.
No current org metadata, credentials or actual customer data is supplied.

