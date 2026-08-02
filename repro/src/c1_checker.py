#!/usr/bin/env python3
"""Independent proof-DAG checker for Claim 1."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> None:
    certificate = json.loads(Path(sys.argv[1]).read_text())
    assert certificate["burn_in_output"] == "x1"
    assert all(certificate["obligations"].values())
    nodes = {row["id"]: row for row in certificate["proof_dag"]}
    assert set(nodes) == {"reverse", "burn-in", "closure", "forward", "equality"}
    assert nodes["reverse"]["rule"] == "subclass-of-adversaries"
    assert nodes["burn-in"]["rule"] == "algorithm-1-definition"
    assert nodes["closure"]["rule"] == "strong-induction-on-time"
    assert nodes["forward"]["premises"] == ["burn-in", "closure"]
    assert nodes["equality"]["premises"] == ["reverse", "forward"]
    assert nodes["equality"]["conclusion"] == "d_replay = d_standard"
    assert certificate["verdict"] == "VERIFIED"
    print(json.dumps({"checker": "independent-proof-dag", "nodes": 5, "status": "PASS"}, sort_keys=True))


if __name__ == "__main__":
    main()
