# Provocateur Review Skill

Use this workflow when a Lughbrugh agent needs a focused challenge pass.

## Inputs

Gather only what is available:

- creator request or feature brief
- current working frame
- relevant canon files
- source inventory or claims, if source material is involved
- active authorship mode
- active source and visual policies
- relevant prototype/derivation notes
- relevant project guidance from `project/creator.md`, `project/guardrails.md`, `project/creative-guidance.md`, `project/lessons.md`, and `project/operating-mode.md`

Do not block the review because one input is missing. Mark missing inputs as risks.

## Steps

1. Identify what the creator explicitly approved.
2. Separate facts, inferences, suggestions, drafts, and unknowns.
3. Look for assumptions the agent may be making because of genre, medium, ruleset, or familiar story structure.
4. Look for contradictions with approved canon or tracked sources.
5. Look for missing decisions that would affect later work.
6. If repeated structures exist, check prototype/variant/layer/instance relationships.
7. If visual work exists, check style scope and continuity.
8. If the creator has corrected the same behavior repeatedly, recommend a project guidance update.
9. Return decision prompts and pressure tests, not automatic rewrites.

## Output Template

```markdown
Provocateur pass:

- Assumptions to confirm:
- Possible conflicts:
- Missing decisions:
- Drift risks:
- Useful pressure tests:
- Recommended next prompt:
- Suggested guidance updates:
```

## Severity

Use lightweight labels only when helpful:

- `blocker`: continuing will likely harden the wrong foundation
- `risk`: continuing is possible, but the issue should be visible
- `decision`: creator choice needed
- `note`: useful context, not urgent

## Behavior

- Keep the pass proportional to the work.
- Do not create canon.
- Do not reject creator intent.
- Do not turn every ambiguity into a blocker.
- Preserve unusual choices if they appear intentional.
- If an issue can be resolved by one focused prompt, ask that prompt.
- Do not edit project guidance without confirmation unless maintenance authority has been granted.
