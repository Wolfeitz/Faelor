# Facet Routing Lens

Use this lens when a thing could be handled by several workflows, lenses, agents, or output formats.

This lens is advisory. It must not become a fixed taxonomy.

## Purpose

Facet routing helps agents decide what kind of support a thing needs without forcing it into one category.

A single thing may have many facets:

- sovereign or political
- organizational
- cultural
- ecological
- encounter-facing
- character-facing
- mechanical
- narrative
- visual
- source-derived
- interface-facing
- artifact/resource
- location/topology

## Routing Pattern

```text
creator intent -> active output -> thing facets -> best next workflow -> redirect prompt
```

## Checks

- Is the creator trying to build a person, population, culture, state, faction, species, encounter, tool, location, rule, interface, or story function?
- Does the thing claim territory, enforce law, host population, or provide infrastructure?
- Does it have a focused mission inside or across other powers?
- Is it primarily ecological, social, mechanical, visual, narrative, or combat-facing?
- Does it have personal identity, agency, growth, and motivation?
- Is the current workflow still the right one?

## Redirect Prompt

When another workflow would fit better, suggest the redirect without blocking.

```markdown
This looks like it has a stronger [facet] facet than the workflow we are using.

I can keep going here, or switch to [better workflow/lens] so we preserve [reason].
```

## Rules

- Use facets instead of single labels.
- Do not force a category just because a template exists.
- Do not switch workflows without creator confirmation unless the creator has granted auto-routing authority.
- Preserve the current thread of thought when redirecting.
