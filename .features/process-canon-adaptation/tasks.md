# Tasks

- [x] 1. Add project guardrails.
  - Intent: Preserve creator intent across constrained, sensitive, derivative, private, or tool-limited material.
  - Required inputs: Current project guidance.
  - Allowed changes: `project/guardrails.md`, agent references.
  - Disallowed changes: Setting-specific rules.
  - Output: Guardrails file.
  - Validation: Required path validation.
  - Gate: Project-agnostic.
  - Worklog evidence: Completed.

- [x] 2. Add creative guidance.
  - Intent: Preserve tone, audience, output, story pressure, and format preferences.
  - Required inputs: Current personality and creator guidance.
  - Allowed changes: `project/creative-guidance.md`.
  - Disallowed changes: Mandatory genre assumptions.
  - Output: Creative guidance file.
  - Validation: Required path validation.
  - Gate: Optional and adaptable.
  - Worklog evidence: Completed.

- [x] 3. Add project lessons.
  - Intent: Store repeated creator corrections and workflow lessons as process canon.
  - Required inputs: Current seed learning concept.
  - Allowed changes: `project/lessons.md`, references.
  - Disallowed changes: Project-specific lore.
  - Output: Lessons file.
  - Validation: Required path validation.
  - Gate: Clearly non-canon for world/story.
  - Worklog evidence: Completed.

- [x] 4. Add thing extraction workflow and status model.
  - Intent: Support broad candidate capture before deep expansion.
  - Required inputs: `canon/things/README.md`, skills registry.
  - Allowed changes: `.skills/thing-extraction.md`, thing docs.
  - Disallowed changes: Forced ontology.
  - Output: Thing extraction skill and status model.
  - Validation: Validator and index pass.
  - Gate: Facet-based and optional.
  - Worklog evidence: Completed.

- [x] 5. Wire Provocateur and agent instructions.
  - Intent: Ensure agents detect process drift and recommend guidance updates.
  - Required inputs: `AGENTS.md`, Provocateur docs.
  - Allowed changes: Agent and skill guidance.
  - Disallowed changes: Silent guidance rewrites.
  - Output: Updated instructions.
  - Validation: Validator and index pass.
  - Gate: Confirmation remains required.
  - Worklog evidence: Completed.
