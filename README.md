# Project Title

Replace this heading with the actual project/world/story title during initialization.

## Project Overview

Fill this in after discovery.

- Built for:
- Existing pattern/ruleset/source canon:
- Authorship mode:
- Source policy:
- Visual policy:
- Primary outputs:

## Lughbrugh

Lughbrugh: Workshop of the gods, by Kadzu WorldBuilder.

This project uses Lughbrugh as a git-portable canon workspace for agent-assisted worldbuilding, storybuilding, campaigns, games, fan fiction, series continuation, and visual development.

## Initialization

1. What are we building this for?
   - Examples: tabletop campaign, video game, MUD, MOO, MMORPG, book, series continuation, fan fiction, wiki, visual bible, or hybrid project.

2. Does this follow an existing pattern, ruleset, source canon, or lore base?
   - Examples: D&D 5e, Pathfinder, Star Trek, Star Wars, a published setting, a specific book series, a custom homebrew system, or no existing source.

3. Rename the copied `lughbrugh/` template folder to the project slug.

4. If git is available and desired, initialize a repository after the folder is renamed:

```bash
git init
git add .
git commit -m "Initialize Lughbrugh canon workspace"
```

5. Start a project-foundation feature packet under `.features/`.

## Commands

```bash
python tools/lughbrugh.py doctor
python tools/lughbrugh.py validate
python tools/lughbrugh.py index
```

## Workspace Shape

- `project/` contains identity, creator preferences, operating mode, and environment notes.
- `canon/` contains human-readable canon, candidates, sources, claims, realms, things, lenses, visuals, and committed indexes.
- `.features/` contains spec-driven work packets.
- `.agents/` contains optional role definitions.
- `.skills/` contains optional reusable workflows.
- `tools/` contains local validation and index tooling.
- `fixtures/` contains small artificial examples for validation.

## Canon Policy

Human-readable files are canonical by default. Generated indexes are committed support artifacts and must be rebuildable.

Agent-authored material must carry provenance and must not silently become canon unless the active authorship mode allows it.
