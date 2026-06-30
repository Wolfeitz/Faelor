# Prototype And Derivation Lens

Use this lens when the project benefits from base definitions, variants, layers, and explainable progression.

This lens is optional. Do not force it into projects that do not need repeated structure.

## Core Pattern

```text
prototype -> layer/modifier/progression -> variant -> instance/placement
```

## Metadata Pattern

```yaml
derivation:
  base: ""
  parents: []
  layers: []
  progression: ""
  modifiers: []
  equipment: []
  source_notes: ""
  override: false
  override_reason: ""
```

Use Markdown prose if YAML is not desired.

## Monster / Creature Pattern

Use only when the world has monsters, creatures, species, or comparable recurring beings.

- Base definition:
  - identity
  - ordinary traits
  - ecology or role
  - baseline capabilities
  - baseline stats if stats exist
  - common equipment or behavior

- Derived variant:
  - parent/base
  - changed traits
  - role layer, such as chieftain, shaman, scout, elder, corrupted, elite
  - progression model, if any
  - stat derivation, if stats exist
  - override rationale, if needed

- Instance:
  - where it appears
  - what variant it uses
  - local modifications
  - encounter/story purpose

## Settlement Pattern

- Base settlement template:
  - water
  - food
  - shelter
  - governance
  - safety
  - trade
  - waste
  - health
  - communication
  - social/ritual life
  - pressure points

- Derived settlement:
  - parent template
  - economy layer
  - geography layer
  - faction/political layer
  - law/safety layer
  - omitted baseline features and consequences

## Visual / UI Pattern

- Base visual style:
  - typography
  - palette
  - composition
  - frame/border rules
  - icon rules
  - material/background rules

- Derived scoped style:
  - realm/world override
  - race/species/culture override
  - faction/guild/institution override
  - UI/system message override
  - page/panel/scene override

## Provocateur Checks

Ask:

- Does every derived variant have a parent or source?
- Are changes explained?
- Are stats derivable, if stats exist?
- Are missing archetype pieces intentional?
- Are overrides labeled?
- Are instances referencing the right base or variant?
- Could this become a useful manual/catalog entry?

Report as questions and levers. Do not auto-fix unless the authorship mode permits it.

