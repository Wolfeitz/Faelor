# Fixture: Prototype Derivation

Purpose: test optional inheritance patterns without requiring every project to use stats.

## Creature Example

Prototype:

- Base goblin
- Small, social ambusher
- Baseline traits: darkvision, nimble movement, group tactics
- Stats: optional; only present if the project uses a mechanical ruleset

Derived variants:

- Goblin shaman
  - derives from base goblin
  - adds ritual role, spirit relationship, altered equipment, spell/power layer if mechanics exist
- Goblin chieftain
  - derives from base goblin
  - adds leadership, morale effects, better equipment, social authority
- Level 20 goblin
  - derives from base goblin plus progression model
  - must explain stat changes if stats exist

Provocateur checks:

- Are variants linked to base goblin?
- Are changes explained?
- Are stats derivable, if stats exist?
- Are overrides labeled?

## Settlement Example

Prototype:

- Base village template
- Includes water, food, shelter, governance, safety, trade, waste, health, communication, social life, pressure points

Derived variant:

- Mining town
  - adds mine economy, tool supply chains, labor structure, hazard profile, guild pressure
  - missing baseline pieces are questions, not automatic errors

## Visual / UI Example

Prototype:

- Global system message style
- Base typography, box shape, icon placement, neutral background

Derived variants:

- Adventurers guild notice
  - guild seal, parchment background, rank colors, quest block layout
- Goblin culture notice
  - jagged border motifs, green/bone palette, different iconography, localized terminology

This mirrors CSS-style inheritance: broad defaults, scoped overrides, and explicit conflict rules.

