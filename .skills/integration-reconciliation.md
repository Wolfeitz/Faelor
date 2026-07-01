# Integration Reconciliation Skill

Use this workflow when two or more lenses, systems, source imports, feature packets, or canon areas touch the same material.

## Purpose

Prevent cross-module drift without forcing a fixed module architecture.

## Inputs

- relevant lenses
- affected things, realms, events, sources, visuals, or rules
- active output goal
- known conflicts
- authoring mode

## Steps

1. Identify the systems or lenses involved.
2. Determine whether each one controls, mirrors, translates, augments, displays, constrains, or merely references the others.
3. Identify shared terms, shared entities, and duplicated assumptions.
4. Check caps, prerequisites, permissions, visibility, resources, source claims, and visual style scope.
5. Flag conflicts and suggest reconciliation options.
6. Ask for confirmation before hardening the reconciliation.

## Output Shape

```markdown
Integration reconciliation:

- Areas involved:
- Relationship type:
- Shared facts:
- Conflicts:
- Missing gates:
- Options:
- Recommended next prompt:
```

## Relationship Types

- controls
- mirrors
- augments
- translates
- displays
- constrains
- imports
- derives from
- conflicts with
- independent but adjacent

## Rules

- Do not assume one system has authority over another.
- Do not erase local exceptions.
- Preserve creator-approved weirdness.
- Use the Provocateur when reconciliation would change canon, rules, or source interpretation.
