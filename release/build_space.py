#!/usr/bin/env python3
"""Assemble the additive, text-only Space candidate from a judged revision."""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COPY_DIRS = ("repro", "reports", "notebooks", "docs", "release")
COPY_FILES = (".python-version", "pyproject.toml", "uv.lock")
TEXT_SUFFIXES = {"", ".css", ".html", ".js", ".json", ".lock", ".md", ".py", ".sha256", ".svg", ".toml", ".txt"}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def copy_tree(source: Path, target: Path) -> None:
    shutil.copytree(source, target, dirs_exist_ok=True, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("judged")
    parser.add_argument("candidate")
    args = parser.parse_args()
    judged = Path(args.judged).resolve()
    candidate = Path(args.candidate).resolve()
    assert judged.is_dir()
    assert not candidate.exists(), "candidate directory must be fresh"

    shutil.copytree(judged, candidate, ignore=shutil.ignore_patterns(".git"))
    copy_tree(ROOT / ".trackio" / "logbook", candidate)
    copy_tree(ROOT / ".openresearch" / "artifacts", candidate / ".openresearch" / "artifacts")
    for relative in COPY_DIRS:
        copy_tree(ROOT / relative, candidate / relative)
    for relative in COPY_FILES:
        shutil.copy2(ROOT / relative, candidate / relative)
    shutil.copy2(ROOT / "release" / "space-README.md", candidate / "README.md")

    protected = sorted(path.relative_to(judged).as_posix() for path in judged.rglob("*") if path.is_file() and ".git" not in path.parts)
    candidate_paths = sorted(path.relative_to(candidate).as_posix() for path in candidate.rglob("*") if path.is_file())
    assert set(protected) <= set(candidate_paths)

    immutable = set(protected) - {"README.md", "logbook.json", "pages/index.md"}
    for relative in immutable:
        if relative.startswith("pages/") or relative.endswith((".css", ".html", ".js", ".png", ".svg")):
            assert digest(judged / relative) == digest(candidate / relative), relative

    changed = []
    for relative in candidate_paths:
        path = candidate / relative
        old = judged / relative
        if old.is_file() and digest(old) == digest(path):
            continue
        assert path.suffix in TEXT_SUFFIXES, f"non-text upload blocked: {relative}"
        path.read_text()
        changed.append(relative)

    result = {
        "candidate_file_count": len(candidate_paths),
        "protected_file_count": len(protected),
        "protected_subset": True,
        "immutable_historical_files_unchanged": True,
        "text_upload_count": len(changed),
        "upload_allowlist": changed,
        "manifest": {relative: digest(candidate / relative) for relative in candidate_paths},
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
