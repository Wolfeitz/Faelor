# System Profile Lens

Use this lens when a project has a system of rules, progression, interfaces, unlocks, stats, tiers, permissions, achievements, classes, rituals, dashboards, or other structured behavior.

This lens is optional. Do not assume a project has stats, levels, UI, magic, classes, or game mechanics.

## Guided Questions

### Visibility And Tone

- Is the system visible, hidden, partially visible, inferred, or only visible to certain actors?
- What tone does it convey: technical, divine, bureaucratic, natural, hostile, playful, neutral, social, ritual, or something else?
- Is it global, local, realm-specific, faction-specific, user-bound, object-bound, or temporary?

### Structure

- Does the system have stats, tags, states, ranks, classes, professions, skills, stages, permissions, or resources?
- Are these literal rules, interface labels, social conventions, symbolic markers, or user-facing simplifications?
- Are caps, prerequisites, costs, risks, or failure modes important?

### Progression

- What triggers change: practice, milestones, XP, quests, discovery, training, time, social recognition, ritual, resources, injury, death, politics, or narrative events?
- Are there tiers, breakthroughs, unlocks, evolutions, or regressions?
- What can improve without becoming mastery?

### Integration

- What other lenses or systems does this touch: magic, technology, source canon, professions, species, factions, items, quests, locations, visual UI, or narrative arcs?
- Does it control those systems, mirror them, translate them, or merely display them?

### Output

- Should the result be conversational notes, reference prose, tables, hybrid Markdown, YAML/JSON, visual prompts, game-ready data, or multiple exports?

## Profile Template

Use Markdown by default. Use YAML/JSON only when requested or exporting.

```yaml
system_name:
status: candidate
visibility:
scope:
tone:
interface:
underlying_mechanism:
progression:
  type:
  triggers:
  gates:
  caps:
stats_or_properties:
  enabled:
  entries:
unlock_logic:
integration_hooks:
output_profile:
provenance:
open_points:
```

## Starter Profiles

Starter profiles are accelerators, not boxes.

- visible progress overlay
- hidden influence model
- assistant or AI-like interface
- internal cultivation or mastery model
- social rank or institution model
- ritual permission model
- custom freeform system

When using a starter profile, ask whether to keep it, modify it, combine it, or start fresh.

## Provocateur Checks

- Are we mistaking an interface label for an underlying law?
- Are stats or levels being added because the genre suggests them, not because the creator asked?
- Are progression triggers compatible with source canon and project output?
- Are caps, gates, and failure modes missing?
- Are integration hooks creating contradictions with other lenses?
