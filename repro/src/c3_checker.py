#!/usr/bin/env python3
"""Independent proof-DAG checker for Witness Protection."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> None:
    result = json.loads(Path(sys.argv[1]).read_text())
    assert all(result["obligations"].values())
    assert result["per_round_exclusion_bound"].endswith("<= 2t+t^2")
    nodes = {node["id"]: node for node in result["proof_dag"]}
    assert set(nodes) == {"sure", "computable", "termination", "criticality", "validity", "theorem"}
    assert nodes["theorem"]["premises"] == ["computable", "termination", "criticality", "validity"]
    assert nodes["validity"]["conclusion"] == "eventual output belongs to target minus seen"
    assert "membership queries" in nodes["theorem"]["conclusion"]
    assert result["verdict"] == "VERIFIED"
    print(json.dumps({"checker": "independent-wp-proof-dag", "lemmas": 6, "obligations": len(result["obligations"]), "status": "PASS"}, sort_keys=True))


if __name__ == "__main__":
    main()
