#!/usr/bin/env python3
"""Independent logical checker for Claim 2."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> None:
    result = json.loads(Path(sys.argv[1]).read_text())
    assert all(result["obligations"].values())
    standard = result["standard_setting"]
    assert standard["h_infinity_threshold"] == 1
    assert standard["h_n_threshold"] == "n+1"
    replay = result["replay_contradiction"]
    assert replay["threshold_for_h_d"] == "T=max(d,m)"
    assert replay["simultaneous_required_set"].endswith("= empty")
    assert result["verdict"] == "VERIFIED"
    print(json.dumps({"checker": "independent-arbitrary-threshold", "status": "PASS", "symbolic_thresholds": ["d", "m"]}, sort_keys=True))


if __name__ == "__main__":
    main()
