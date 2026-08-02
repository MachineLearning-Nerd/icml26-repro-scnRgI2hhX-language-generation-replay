#!/usr/bin/env python3
"""Create the exact text upload allowlist and candidate SHA-256 manifest."""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWLIST_PATH = "release/upload-allowlist.txt"
MANIFEST_PATH = "release/candidate-manifest.sha256"
TEXT_SUFFIXES = {"", ".css", ".html", ".js", ".json", ".lean", ".lock", ".md", ".py", ".sha256", ".svg", ".toml", ".txt"}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("judged")
    parser.add_argument("candidate")
    args = parser.parse_args()
    judged = Path(args.judged).resolve()
    candidate = Path(args.candidate).resolve()

    changed = []
    for path in sorted(candidate.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(candidate).as_posix()
        old = judged / relative
        if old.is_file() and digest(old) == digest(path):
            continue
        assert path.suffix in TEXT_SUFFIXES
        path.read_text()
        changed.append(relative)
    changed = sorted(set(changed) | {ALLOWLIST_PATH, MANIFEST_PATH})
    (ROOT / ALLOWLIST_PATH).write_text("\n".join(changed) + "\n")

    hashes = {}
    for path in sorted(candidate.rglob("*")):
        if path.is_file():
            relative = path.relative_to(candidate).as_posix()
            if relative != MANIFEST_PATH:
                hashes[relative] = digest(path)
    hashes[ALLOWLIST_PATH] = digest(ROOT / ALLOWLIST_PATH)
    (ROOT / MANIFEST_PATH).write_text("".join(f"{value}  {relative}\n" for relative, value in sorted(hashes.items())))

    print(f"UPLOAD_ALLOWLIST_COUNT={len(changed)}")
    print(f"MANIFEST_HASH_COUNT={len(hashes)}")
    print("MANIFEST_EXCLUDES_SELF=true")


if __name__ == "__main__":
    main()
