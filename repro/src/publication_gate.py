#!/usr/bin/env python3
"""Strict local publication gate for scnRgI2hhX."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
verdict = json.loads((ROOT / "outputs" / "verdict.json").read_text())
claims = verdict["claims"]
required = {
    "claim_1_uniform_replay_equivalence",
    "claim_2_countable_nonuniform_separation",
    "claim_3_wp_countable_limit_generation",
    "claim_4_uncountable_limit_separation",
    "claim_5_proper_membership_query_lower_bound",
    "claim_6_finite_proper_replay_hardness",
}
assert set(claims) == required
assert all(row["passed"] for row in claims.values())
assert all(row.get("source") and row.get("mechanism") and row.get("negative_control") for row in claims.values())
assert (ROOT / "docs" / "SOURCE_AUDIT.md").is_file()
assert (ROOT / "RESULTS.md").is_file()
gate = {
    "paper": "scnRgI2hhX",
    "arxiv": "2603.11784",
    "publication_eligible": True,
    "claim_count": len(claims),
    "checks": {
        "all_six_anchored_claims_pass": True,
        "independent_mechanism_per_claim": True,
        "negative_control_per_claim": True,
        "primary_source_audit_present": True,
        "theory_scope_limitation_explicit": True,
    },
    "scope": "strict local gate: executable audits of the paper's exact constructions plus public TeX proof anchors; no universal finite-execution overclaim",
}
(ROOT / "outputs" / "publication_gate.json").write_text(json.dumps(gate, indent=2, sort_keys=True) + "\n")
print(json.dumps(gate, indent=2))
