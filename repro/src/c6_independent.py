#!/usr/bin/env python3
"""Independent consumer-side checker for the C6 structural certificate."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> None:
    data = json.loads(Path(sys.argv[1]).read_text())
    assert data["verdict"] == "VERIFIED"
    assert data["domain"].startswith("all integers")
    rows = {row["first_output"]: row for row in data["branches"]}
    assert set(rows) == {"h1-", "h2-", "h1+", "h2+"}
    for first, row in rows.items():
        assert row["replay_legal_for_every_target"]
        assert row["enumerates_both_targets_exactly"]
        assert row["no_admissible_proper_output"]
        assert row["contradiction"]
        if first.endswith("-"):
            assert row["replays"] == [-1, -2]
            assert row["targets"] == ["h1+", "h2+"]
            assert row["intersection_normal_form"] == "x >= 0"
            assert row["outside_witness_for_each_proper_output"] == {
                "h1-": -1,
                "h2-": -1,
                "h1+": -1,
                "h2+": -2,
            }
        else:
            assert row["replays"] == [1, 2]
            assert row["targets"] == ["h1-", "h2-"]
            assert row["intersection_normal_form"] == "x <= 0"
            assert row["outside_witness_for_each_proper_output"] == {
                "h1-": 1,
                "h2-": 2,
                "h1+": 1,
                "h2+": 1,
            }
    print(json.dumps({"checker": "independent-c6", "status": "PASS", "branches": 4}, sort_keys=True))


if __name__ == "__main__":
    main()
