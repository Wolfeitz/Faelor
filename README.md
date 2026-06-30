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

Start with a short guided conversation, not file editing.

Prompt:

```text
Give me the seed for this project in whatever form you have it.

What are we building it for: novel, tabletop campaign, game, wiki, visual bible, private fan project, graphic novel, or something else?

Is there an existing pattern, ruleset, source canon, or lore base I should respect?
```

Then:

1. Rename the copied `lughbrugh/` template folder to the project slug.
2. Capture the working frame in this README and `project/identity.md`.
3. Choose how hands-on the agent should be.
4. Optionally pin the next phase with a clear objective. In Codex, `project/goal.md` can be used with `/goal`; other agents can use it as a normal prompt reference.
5. Create a project-foundation feature packet under `.features/`.
6. If git is available and desired, initialize a repository after the folder is renamed:

```bash
git init
git add .
git commit -m "Initialize Lughbrugh canon workspace"
```

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
