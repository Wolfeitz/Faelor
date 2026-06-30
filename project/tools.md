# Tools And Environment

Record the active environment here.

## Access

- Local or cloud:
- CLI, IDE, browser, or other:
- Shell access:
- Network/web access:
- Git forge:
- Git initialized:
- Image generation available:
- Local models available:
- Codex `/goal` available, if using Codex:

## Optional Services

- SQLite:
- PostgreSQL:
- Redis:
- RabbitMQ:
- Vector store:
- Graph store:
- Full-text search:
- Local background model for audits:
- Cheap model/background agent for small consistency passes:

## Commands

```bash
python tools/lughbrugh.py doctor
python tools/lughbrugh.py validate
python tools/lughbrugh.py index
```

## New Project Git Setup

After the template folder is renamed to the project slug:

```bash
git init
git add .
git commit -m "Initialize Lughbrugh canon workspace"
```

Skip this if the project is embedded in an existing repository or git is unavailable.

## Objective Tracking

For long-running setup or feature work, write a clear objective after the opening guided conversation.

In Codex, use `/goal` when available.

If `/goal` is unavailable in the slash command list, try:

```bash
codex features enable goals
```

Then restart or refresh Codex if prompted.

For non-Codex agents, use `project/goal.md` as a normal prompt reference or task brief.

## Background Consistency Work

When local models or low-cost background agents are available, they are good candidates for:

- orphan variant scans
- base/derived comparison
- archetype completeness drafts
- source/index refreshes
- visual style drift checks
- Provocateur candidate reports

Background agents should produce reports and questions, not silently rewrite canon.
