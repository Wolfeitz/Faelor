# Tasks

- [x] 1. Add seed learning guidance.
  - Intent: Preserve reusable lessons without importing lore.
  - Required inputs: Current scaffold and seeded-work lessons.
  - Allowed changes: Project guidance.
  - Disallowed changes: Project-specific canon.
  - Output: `project/seed-learning.md`.
  - Validation: File exists and contains no setting-specific premise.
  - Gate: Reusable across projects.
  - Worklog evidence: Completed.

- [x] 2. Add reusable lenses.
  - Intent: Support interface and translation modeling.
  - Required inputs: Current lens structure.
  - Allowed changes: `canon/lenses/`.
  - Disallowed changes: Mandatory ontology.
  - Output: `interface-abstraction.md`, `cross-context-translation.md`.
  - Validation: Lenses are optional and project-agnostic.
  - Gate: No single genre assumption.
  - Worklog evidence: Completed.

- [x] 3. Add seed extraction workflow.
  - Intent: Turn seed material into candidate stubs before canon hardens.
  - Required inputs: Current skill structure.
  - Allowed changes: `.skills/`.
  - Disallowed changes: Approved canon generation.
  - Output: `.skills/seed-extraction.md`.
  - Validation: Workflow separates known facts, inference, and open points.
  - Gate: Provocateur pass remains required before promotion.
  - Worklog evidence: Completed.

- [x] 4. Wire guidance into agent instructions.
  - Intent: Make agents discover and use the new concepts.
  - Required inputs: `AGENTS.md`, lens and skill registries.
  - Allowed changes: Instruction references.
  - Disallowed changes: Startup prompt regression.
  - Output: Updated `AGENTS.md`, `canon/lenses/README.md`, `.skills/README.md`.
  - Validation: `python tools/lughbrugh.py validate`.
  - Gate: Clean validation.
  - Worklog evidence: Pending validation.
