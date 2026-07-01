# Tasks

- [x] 1. Review Kadzu v1.5 files.
  - Intent: Identify reusable concepts not already captured.
  - Required inputs: Downloaded markdown files.
  - Allowed changes: None during review.
  - Disallowed changes: Importing project-specific or fixed module assumptions.
  - Output: Concept list.
  - Validation: Compare against current scaffold.
  - Gate: Project-agnostic only.
  - Worklog evidence: Completed.

- [x] 2. Add export closeout.
  - Intent: Preserve outputs and close major sessions cleanly.
  - Required inputs: Output formatter and shared behavior docs.
  - Allowed changes: `project/export.md`, `.skills/export-closeout.md`, references.
  - Disallowed changes: Required attribution footer.
  - Output: Export guidance.
  - Validation: Validator pass.
  - Gate: Optional and project-specific.
  - Worklog evidence: Completed.

- [x] 3. Add facet routing.
  - Intent: Generalize old entity classification without hard modules.
  - Required inputs: Entity classification doc.
  - Allowed changes: `canon/lenses/facet-routing.md`.
  - Disallowed changes: Fixed taxonomy.
  - Output: Facet routing lens.
  - Validation: Validator pass.
  - Gate: Advisory only.
  - Worklog evidence: Completed.

- [x] 4. Add system profile lens.
  - Intent: Generalize system engine guided flow and schema.
  - Required inputs: Guided flow, schema, template loader.
  - Allowed changes: `canon/lenses/system-profile.md`.
  - Disallowed changes: Assuming stats, levels, UI, or LitRPG.
  - Output: Optional system profile lens.
  - Validation: Validator pass.
  - Gate: Zero-assumption compatible.
  - Worklog evidence: Completed.

- [x] 5. Add integration reconciliation.
  - Intent: Generalize cross-module hooks.
  - Required inputs: Cross-module hooks doc.
  - Allowed changes: `.skills/integration-reconciliation.md`.
  - Disallowed changes: Fixed module architecture.
  - Output: Reconciliation workflow.
  - Validation: Validator pass.
  - Gate: Relationship-based, not hierarchy-based.
  - Worklog evidence: Completed.
