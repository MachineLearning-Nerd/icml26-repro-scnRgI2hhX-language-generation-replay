#!/usr/bin/env python3
"""Evaluator-blind traversal of an assembled static logbook."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

LINK = re.compile(r"\[[^]]+\]\(([^)]+)\)")
FIXED_COMMAND = "uv sync --frozen --no-dev && uv run --no-sync python repro/src/check_lean_certificate.py && uv run --no-sync python repro/src/verify.py && uv run --no-sync python repro/src/publication_gate.py"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("candidate")
    args = parser.parse_args()
    root = Path(args.candidate).resolve()
    opened: list[str] = []

    def read(relative: str) -> str:
        path = root / relative
        assert path.is_file(), relative
        opened.append(relative)
        return path.read_text()

    read("README.md")
    manifest = json.loads(read("logbook.json"))
    index = read("pages/index.md")
    assert index.startswith("# Reproduction: Language Generation with Replay: A Learning-Theoretic View of Model Collapse\n")
    children = manifest["root"]["children"]
    assert [child["slug"] for child in children] == [
        "executive-summary",
        "claim-1-current",
        "claim-2-current",
        "claim-3-current",
        "claim-4-current",
        "claim-5-current",
        "claim-6-current",
        "conclusion",
    ]
    slugs = {child["slug"] for child in children}
    slugs.update(child["slug"] for child in children[0]["children"])
    executive = read("pages/executive-summary/page.md")
    assert '"pinned":true' in executive
    assert "poster_embed.html" in executive
    read("poster_embed.html")
    read("pages/conclusion/page.md")
    matrix = read("pages/visibility-matrix/page.md")
    assert "Lean runner" in matrix

    for claim_number in range(1, 7):
        page_name = f"pages/claim-{claim_number}-current/page.md"
        page = read(page_name)
        assert "```lean" in page
        assert "https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/" in page
        raw_name = f".openresearch/artifacts/claim_{claim_number}/raw_result.json"
        raw = json.loads(read(raw_name))
        assert raw["verdict"] == "VERIFIED"
        assert FIXED_COMMAND in page
        assert "no seeds" in page.lower()
        for required in ("claim_contract.json", "source_audit.md", "method.md", "checker_output.json", "negative_control_output.json", "commands.txt", "EVAL.md", "limitations.md"):
            read(f".openresearch/artifacts/claim_{claim_number}/{required}")
        checker = json.loads(read(f".openresearch/artifacts/claim_{claim_number}/checker_output.json"))
        control = json.loads(read(f".openresearch/artifacts/claim_{claim_number}/negative_control_output.json"))
        assert checker["status"] == "PASS"
        assert control["exit_code"] != 0 and control["verdict"] == "REJECTED"
        for url in LINK.findall(page):
            if url.startswith("#/"):
                assert url[2:] in slugs
            elif not url.startswith(("http://", "https://")):
                read(url.removeprefix("./"))

    report = read("reports/replay-reproduction/report.md")
    for image in re.findall(r"!\[[^]]*\]\(([^)]+)\)", report):
        read(f"reports/replay-reproduction/{image}")
    read("notebooks/replay_reproduction.py")
    read("pages/historical-rejected-baseline/page.md")
    read("pages/verification-run/page.md")
    assert "Historical rejected baseline" in matrix
    assert "../../../../" not in matrix

    allowlist = read("release/upload-allowlist.txt").splitlines()
    assert allowlist == sorted(set(allowlist))
    assert all((root / relative).is_file() for relative in allowlist)
    manifest_lines = read("release/candidate-manifest.sha256").splitlines()
    manifest_hashes = {line.split("  ", 1)[1]: line.split("  ", 1)[0] for line in manifest_lines}
    assert "release/candidate-manifest.sha256" not in manifest_hashes
    for relative, expected in manifest_hashes.items():
        actual = hashlib.sha256((root / relative).read_bytes()).hexdigest()
        assert actual == expected, relative

    result = {
        "status": "PASS",
        "claims_located": 6,
        "current_verifiers_obvious": True,
        "lean_source_visible_inline": True,
        "canonical_page_order": True,
        "pinned_summary_and_poster": True,
        "historical_baseline_labeled": True,
        "missing_conclusions": [],
        "opened_files": list(dict.fromkeys(opened)),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
