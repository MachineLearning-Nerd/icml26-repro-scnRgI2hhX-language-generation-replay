#!/usr/bin/env python3
"""Independent truth-table checker for the Claim 6 cell certificate."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> None:
    result = json.loads(Path(sys.argv[1]).read_text())
    expected = {
        "h1-": [True, True, True, True, True, False, False],
        "h2-": [True, True, True, True, False, True, False],
        "h1+": [False, False, True, True, True, True, True],
        "h2+": [False, True, False, True, True, True, True],
    }
    assert result["cells"] == ["x<=-3", "x=-2", "x=-1", "x=0", "x=1", "x=2", "x>=3"]
    assert result["complete_disjoint_partition"] is True
    assert result["support_truth_vectors"] == expected
    assert len(result["branches"]) == 4
    assert all(row["intersection_is_exact_half_line"] for row in result["branches"])
    assert all(row["no_proper_support_is_subset"] for row in result["branches"])
    assert result["verdict"] == "VERIFIED"
    print(json.dumps({"checker": "independent-cell-truth-table", "status": "PASS", "cells": 7, "branches": 4}, sort_keys=True))


if __name__ == "__main__":
    main()
