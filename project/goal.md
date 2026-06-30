# Objective Reference

Use this optional file to capture a clear objective, definition of done, and validation path for longer Lughbrugh setup or feature work.

Codex can use this with `/goal` when that command is available. Other agents can use the same content as ordinary prompt/context instructions.

## When To Use This

Use an objective reference after the creator has given the project seed and working frame, not as the first interaction.

Good candidates:

- initialize the project foundation
- import and index a source corpus
- build a realm topology
- create a visual style bible and prompt pack
- audit continuity across a large feature
- migrate a feature packet from design to implementation

Do not use this for:

- the opening conversation
- tiny one-step edits
- unclear creative exploration where success criteria are not known yet

If the objective is hard to define, plan first, then write a clearer objective after the plan has success criteria.

## Recommended Project-Foundation Objective

```text
Establish the Lughbrugh project foundation for this renamed workspace. Capture the creator's project purpose, source/ruleset/lore base, authorship mode, source policy, visual policy, and first feature packet. Update README.md, project/identity.md, project/creator.md, project/operating-mode.md, and .features/project-foundation/. Run python tools/lughbrugh.py validate and python tools/lughbrugh.py index before marking complete.
```

For Codex, the same objective can be used with `/goal`:

```text
/goal Establish the Lughbrugh project foundation for this renamed workspace. Capture the creator's project purpose, source/ruleset/lore base, authorship mode, source policy, visual policy, and first feature packet. Update README.md, project/identity.md, project/creator.md, project/operating-mode.md, and .features/project-foundation/. Run python tools/lughbrugh.py validate and python tools/lughbrugh.py index before marking complete.
```

## Objective Writing Rules

A useful objective should include:

- concrete objective
- files or feature packet to update
- success criteria
- validation commands
- stop/review condition

If instructions are longer than a short paragraph, put the details in a feature packet or project file and point the goal at that file.

## Codex `/goal` Availability

Codex supports `/goal` in current CLI, IDE, and app surfaces. If `/goal` does not appear in the slash command list, enable the goals feature where available.

```bash
codex features enable goals
```

Then restart or refresh Codex if prompted.

For non-Codex agents, use this file as a general prompt reference or task brief.
