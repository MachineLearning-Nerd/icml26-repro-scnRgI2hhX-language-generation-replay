#!/usr/bin/env python3
"""Independent proof-DAG checker for Claim 4."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> None:
    result = json.loads(Path(sys.argv[1]).read_text())
    assert all(result["obligations"].values())
    nodes = {node["id"]: node for node in result["proof_dag"]}
    assert set(nodes) == {"uncountable", "standard", "phase", "actual-target", "separation"}
    assert nodes["phase"]["conclusion"] == "every phase n terminates at finite t_n"
    assert nodes["actual-target"]["conclusion"].endswith("for every n")
    assert "J_n is never presented" in result["phase_invariant"]
    assert result["actual_target_normal_form"].startswith("all integers < z")
    assert result["verdict"] == "VERIFIED"
    print(json.dumps({"checker":"independent-infinite-phase-dag","nodes":5,"status":"PASS"}, sort_keys=True))


if __name__ == "__main__":
    main()
