#!/usr/bin/env python3
"""Minimal Lughbrugh validator and index builder."""

from __future__ import annotations

import argparse
import datetime as _dt
import os
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = [
    "AGENTS.md",
    "README.md",
    "project/identity.md",
    "project/creator.md",
    "project/kickoff.md",
    "project/personality.md",
    "project/operating-mode.md",
    "project/tools.md",
    "canon/README.md",
    "canon/sources/README.md",
    "canon/claims/README.md",
    "canon/things/README.md",
    "canon/realms/README.md",
    "canon/lenses/README.md",
    "canon/visuals/style-bible.md",
    "canon/visuals/prompt-patterns.md",
    "canon/visuals/assets-index.md",
    "canon/indexes/README.md",
    ".features/_template/brief.md",
    ".features/_template/requirements.md",
    ".features/_template/design.md",
    ".features/_template/tasks.md",
]

FEATURE_REQUIRED = [
    "brief.md",
    "requirements.md",
    "questions.md",
    "decisions.md",
    "design.md",
    "tasks.md",
    "acceptance.md",
    "worklog.md",
]

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
TODO_RE = re.compile(r"\b(TODO|FIXME|QUESTION|TBD)\b", re.IGNORECASE)


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def iter_markdown() -> list[Path]:
    ignored_parts = {".git", "__pycache__"}
    files: list[Path] = []
    for path in ROOT.rglob("*.md"):
        if any(part in ignored_parts for part in path.parts):
            continue
        files.append(path)
    return sorted(files)


def check_required() -> list[str]:
    errors = []
    for item in REQUIRED_PATHS:
        if not (ROOT / item).exists():
            errors.append(f"missing required path: {item}")
    return errors


def check_feature_packets() -> list[str]:
    errors = []
    features = ROOT / ".features"
    if not features.exists():
        return ["missing .features directory"]
    for packet in sorted(p for p in features.iterdir() if p.is_dir() and p.name != "_template"):
        for required in FEATURE_REQUIRED:
            if not (packet / required).exists():
                errors.append(f"feature {packet.name} missing {required}")
    return errors


def check_markdown_links() -> list[str]:
    errors = []
    for path in iter_markdown():
        text = path.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            target = match.group(1).strip()
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            target = target.split("#", 1)[0]
            if not target:
                continue
            if target.startswith("/"):
                errors.append(f"{rel(path)} has absolute local link: {target}")
                continue
            target_path = (path.parent / target).resolve()
            try:
                target_path.relative_to(ROOT)
            except ValueError:
                errors.append(f"{rel(path)} links outside workspace: {target}")
                continue
            if not target_path.exists():
                errors.append(f"{rel(path)} broken link: {target}")
    return errors


def check_parent_runtime_refs() -> list[str]:
    errors = []
    forbidden = [str(ROOT.parent), "/home/rob/Projects/Lughbrugh"]
    for path in iter_markdown() + [ROOT / "AGENTS.md"]:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for marker in forbidden:
            if marker and marker in text:
                errors.append(f"{rel(path)} contains parent workspace reference: {marker}")
    return errors


def unresolved_items() -> list[tuple[str, int, str]]:
    items = []
    for path in iter_markdown():
        if rel(path) == "canon/indexes/unresolved.md":
            continue
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if TODO_RE.search(line):
                items.append((rel(path), lineno, line.strip()))
    return items


def validate() -> int:
    errors = []
    errors.extend(check_required())
    errors.extend(check_feature_packets())
    errors.extend(check_markdown_links())
    errors.extend(check_parent_runtime_refs())

    unresolved = unresolved_items()

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
    else:
        print("Validation passed.")

    print(f"Unresolved markers: {len(unresolved)}")
    if unresolved:
        for file, lineno, line in unresolved[:20]:
            print(f"- {file}:{lineno}: {line}")
        if len(unresolved) > 20:
            print(f"- ... {len(unresolved) - 20} more")

    return 1 if errors else 0


def write_index(path: Path, title: str, rows: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    now = _dt.datetime.now().isoformat(timespec="seconds")
    body = [f"# {title}", "", f"Generated: {now}", ""]
    body.extend(rows or ["No entries found."])
    body.append("")
    path.write_text("\n".join(body), encoding="utf-8")


def index() -> int:
    md_files = iter_markdown()
    index_dir = ROOT / "canon" / "indexes"

    source_rows = [f"- {rel(p)}" for p in md_files if "/sources/" in rel(p)]
    claim_rows = [f"- {rel(p)}" for p in md_files if "/claims/" in rel(p)]
    visual_rows = [f"- {rel(p)}" for p in md_files if "/visuals/" in rel(p)]
    feature_rows = [f"- {rel(p)}" for p in md_files if "/.features/" in rel(p) or rel(p).startswith(".features/")]
    unresolved_rows = [f"- {file}:{lineno}: {line}" for file, lineno, line in unresolved_items()]

    write_index(index_dir / "sources.md", "Source Index", source_rows)
    write_index(index_dir / "claims.md", "Claim Index", claim_rows)
    write_index(index_dir / "visuals.md", "Visual Index", visual_rows)
    write_index(index_dir / "features.md", "Feature Index", feature_rows)
    write_index(index_dir / "unresolved.md", "Unresolved Questions And TODOs", unresolved_rows)

    print("Indexes rebuilt:")
    for name in ["sources.md", "claims.md", "visuals.md", "features.md", "unresolved.md"]:
        print(f"- {rel(index_dir / name)}")
    return 0


def doctor() -> int:
    git_present = (ROOT / ".git").exists()
    print("Lughbrugh Doctor")
    print(f"Root: {ROOT}")
    print(f"Python: {sys.version.split()[0]}")
    print(f"Git root present: {git_present}")
    print(f"Network access: not tested")
    if not git_present:
        print("")
        print("Git setup recommendation:")
        print("- After this template folder is renamed to the project slug, initialize git if available:")
        print("  git init")
        print("  git add .")
        print('  git commit -m "Initialize Lughbrugh canon workspace"')
    print("")
    print("Suggested optional tooling:")
    print("- Git remote: Codeberg, Forgejo/Gitea, GitLab, GitHub, or local-only.")
    print("- SQLite: useful for lightweight claim/source projections.")
    print("- Vector index: useful for large imported corpora.")
    print("- Graph index: useful for realm topology, relationships, and transference.")
    print("- Image generation: useful for characters, maps, factions, items, and style sheets.")
    print("- Local models: useful for private or model-restricted creative workflows.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Lughbrugh tools")
    parser.add_argument("command", choices=["validate", "index", "doctor"])
    args = parser.parse_args()
    if args.command == "validate":
        return validate()
    if args.command == "index":
        return index()
    if args.command == "doctor":
        return doctor()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
