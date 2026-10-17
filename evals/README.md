# Workflow evaluations

The suite contains 21 synthetic scenarios covering every custom skill and the architecture lifecycle. These are
evaluation definitions, not a claim that all scenarios have passed.

For a forward test, give a fresh assistant only the selected skill, runtime contract
and the scenario's user prompt or raw fixture. Do not supply expected criteria or an
earlier review. Evaluate the output afterward against must_demonstrate and failure_conditions.

Record date, model/environment if available, prompt, source fixture, output, criterion
results and limitations. A synthetic review cannot establish Salesforce runtime behavior.
Keep private org data out of fixtures. Use docs/VALIDATION.md for the current evidence summary.

