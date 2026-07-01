# Thing Extraction Skill

Use this workflow to extract candidate things from conversation, source notes, drafts, feature packets, imported corpora, visual briefs, rulesets, or brainstorms.

The output is candidate stubs, not approved canon.

## What Counts As A Thing

A thing is anything important enough to identify.

Extract broadly:

- entities
- people or roles
- places or realms
- systems
- laws or rules
- events
- jobs or classes
- species or cultures
- tools or artifacts
- resources
- institutions
- interfaces
- relationships
- styles
- routes or boundaries
- implied infrastructure
- supply chains
- social consequences
- contradictions
- deferred material

Do not force categories. Use facets when one thing has multiple roles.

## Workflow

1. Read only the relevant material.
2. Separate explicit creator statements from inference.
3. Extract a breadth-first inventory.
4. Capture implied infrastructure.
5. Assign a status and build depth.
6. Mark source needs, provenance, and promotion gate.
7. Run a Provocateur pass for drift, assumptions, missing parents, missing infrastructure, or premature hardening.
8. Let the creator choose which stubs deserve depth.

## Stub Format

```markdown
## Name

Status:
Build depth:
Facets:

Known:

Inferred:

Implied infrastructure:

Dependencies:

Source/provenance:

Risks:

Promotion gate:
```

## Status Values

- `captured`: mentioned or implied.
- `candidate`: plausible but not approved.
- `needs_review`: creator decision needed.
- `approved`: canonized.
- `deferred`: intentionally parked.
- `rejected`: preserved as a rejected idea.
- `sensitive`: requires special handling.
- `derived`: inferred from another thing.

## Build Depth

- `mention`: keep as a note only.
- `stub`: identify and track.
- `sketch`: outline structure and dependencies.
- `reference`: build a reusable canon reference.
- `system`: build rules, validators, indexes, or templates around it.

## Breadth Before Depth

After a major brainstorm, capture broad stubs first. Do not immediately expand everything. Let the creator choose which lines deserve depth.

## Implied Infrastructure Rule

When a thing implies infrastructure, capture the implied stubs.

Examples:

- Weapons imply makers, materials, training, repair, laws, trade, and violence norms.
- Medicine implies ingredients, preparation, quality control, healers, access, law, and failure modes.
- Books imply literacy, writers, copying, storage, education, access control, and preservation.
- Ships imply builders, crews, routes, maintenance, docking, navigation, law, and cargo.
- Messages imply senders, receivers, channels, formats, trust, interception, and archives.
