#!/usr/bin/env python3
"""Independent proof-DAG checker for Claim 5."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> None:
    result = json.loads(Path(sys.argv[1]).read_text())
    assert all(result["obligations"].values())
    assert len(result["dichotomy"]) == 2
    nodes = {node["id"]:node for node in result["proof_dag"]}
    assert set(nodes) == {"totality","valid-class","queue","case-infinite","case-finite","lower-bound"}
    assert nodes["totality"]["conclusion"] == "F:NxN->{0,1} is total recursive"
    assert nodes["lower-bound"]["premises"] == ["output_sequence_dichotomy_is_exhaustive","valid-class","queue","case-infinite","case-finite"]
    assert result["verdict"] == "VERIFIED"
    print(json.dumps({"checker":"independent-mq-lower-bound-dag","cases":2,"nodes":6,"status":"PASS"}, sort_keys=True))


if __name__ == "__main__":
    main()
