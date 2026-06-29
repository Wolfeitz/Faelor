# AGENTS

You are working in Lughbrugh, a git-portable canon workspace.

This folder is a template. After cloning or copying it for a real project, rename the folder to the project slug and treat the root `README.md` as the project/world README. Lughbrugh should be one section of that README, not the entire document.

## Operating Contract

- Coach first. Ask, reflect, scaffold, and organize before writing canon.
- Do not assume genre, ruleset, physics, magic, time, cosmology, folders, or entity categories.
- Start every new project or major feature with:
  1. What are we building this for?
  2. Does this follow an existing pattern, ruleset, source canon, or lore base?
- Use feature packets under `.features/` for major work.
- Build or update needed tools, indexes, reports, and validators before broad canon creation.
- Preserve unknowns instead of filling blanks with genre defaults.
- Track provenance for imported, inferred, generated, and approved material.
- If git is available and the folder is not already a repository, offer to initialize git after the folder has been renamed.

## Authorship Modes

- `guided_only`: ask questions and organize user answers; do not author canon.
- `suggestive`: provide options but keep them non-canon until selected.
- `example_driven`: provide examples for the user to adopt, reject, or rewrite.
- `assisted_draft`: draft bounded content for review before canonization.
- `full_generation`: generate canon only when the feature/task scope grants authority; still track provenance.

If uncertain whether an action exceeds the active mode, ask.

## Source And Web Import

Web search and source import are core capabilities when available.

- If browsing/network access is available, use it for source acquisition when the task depends on current or external canon.
- Record source inventory entries before using important facts.
- Convert important facts into claims with provenance.
- If web access is unavailable, create explicit source-acquisition tasks for the user or another agent/runtime.
- Warn when material appears copyrighted, derivative, or publication-risky.
- Distinguish private/personal use from publication-oriented use.

Do not rely on untracked source facts as background memory.

## Visual Workflow

Visual development is first-class.

- Use `canon/visuals/style-bible.md` before generating images or prompts.
- Respect scoped visual styles. Global style may be overridden by medium, nexus, realm/world, era, race/species/culture, faction/guild/institution, UI/message layer, scene, page, or asset-specific rules.
- If image generation is available and appropriate, generate drafts with metadata.
- If not, generate strong external prompts that preserve canon facts, style, map constraints, and negative constraints.
- For comics or graphic novels, preserve recurring character model sheets, page/panel language, speech/caption conventions, UI overlays, and scene-to-scene continuity.
- Track generated images, prompts, references, and approvals in `canon/visuals/assets-index.md`.
- Do not treat draft images or prompts as canon until approved.

## Validation

Before marking major work complete, run:

```bash
python tools/lughbrugh.py validate
python tools/lughbrugh.py index
```

Use `python tools/lughbrugh.py doctor` when the environment changes or when more tooling may help.

## Git Initialization

If this is a new project folder and git is available, recommend:

```bash
git init
git add .
git commit -m "Initialize Lughbrugh canon workspace"
```

Do this after the template folder has been renamed to the project slug.

## Parent Folder Rule

This prototype must not depend on parent folders at runtime. Do not reference files outside this workspace as required runtime inputs.
