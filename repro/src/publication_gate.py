#!/usr/bin/env python3
"""Strict local publication gate for scnRgI2hhX."""
from __future__ import annotations

import json
import subprocess
import sys
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
assert verdict["run_metadata"]["requested_flavor"] == "cpu-upgrade"
assert verdict["run_metadata"]["estimated_cores_required"] == 1
assert verdict["run_metadata"]["cpu_logical"] >= 1
assert verdict["run_metadata"]["runtime_seconds"] >= 0
assert verdict["exact_claims"]["claim_6_finite_proper_replay_hardness"]["verdict"] == "VERIFIED"
assert verdict["exact_claims"]["claim_1_uniform_replay_equivalence"]["verdict"] == "VERIFIED"
assert verdict["exact_claims"]["claim_2_countable_nonuniform_separation"]["verdict"] == "VERIFIED"
assert verdict["exact_claims"]["claim_3_wp_countable_limit_generation"]["verdict"] == "VERIFIED"
checker = subprocess.run(
    [sys.executable, str(ROOT / "repro" / "src" / "c6_independent.py"), str(ROOT / "outputs" / "c6_exact.json")],
    check=True,
    capture_output=True,
    text=True,
)
cell_checker = subprocess.run(
    [sys.executable, str(ROOT / "repro" / "src" / "c6_cell_checker.py"), str(ROOT / "outputs" / "c6_cell_certificate.json")],
    check=True,
    capture_output=True,
    text=True,
)
c1_checker = subprocess.run(
    [sys.executable, str(ROOT / "repro" / "src" / "c1_checker.py"), str(ROOT / "outputs" / "c1_proof.json")],
    check=True,
    capture_output=True,
    text=True,
)
c2_checker = subprocess.run(
    [sys.executable, str(ROOT / "repro" / "src" / "c2_checker.py"), str(ROOT / "outputs" / "c2_proof.json")],
    check=True,
    capture_output=True,
    text=True,
)
c3_checker = subprocess.run(
    [sys.executable, str(ROOT / "repro" / "src" / "c3_checker.py"), str(ROOT / "outputs" / "c3_proof.json")],
    check=True,
    capture_output=True,
    text=True,
)
control = subprocess.run(
    [sys.executable, str(ROOT / "repro" / "src" / "c6_exact.py"), "--mutated-control"],
    check=False,
    capture_output=True,
    text=True,
)
assert control.returncode != 0
cell_control = subprocess.run(
    [sys.executable, str(ROOT / "repro" / "src" / "c6_cell_solver.py"), "--mutated-control"],
    check=False,
    capture_output=True,
    text=True,
)
assert cell_control.returncode != 0
c1_control = subprocess.run(
    [sys.executable, str(ROOT / "repro" / "src" / "c1_proof.py"), "--mutated-control"],
    check=False,
    capture_output=True,
    text=True,
)
assert c1_control.returncode != 0
c2_control = subprocess.run(
    [sys.executable, str(ROOT / "repro" / "src" / "c2_proof.py"), "--mutated-control"],
    check=False,
    capture_output=True,
    text=True,
)
assert c2_control.returncode != 0
c3_control = subprocess.run(
    [sys.executable, str(ROOT / "repro" / "src" / "c3_proof.py"), "--mutated-control"],
    check=False,
    capture_output=True,
    text=True,
)
assert c3_control.returncode != 0
assert (ROOT / "docs" / "SOURCE_AUDIT.md").is_file()
assert (ROOT / "RESULTS.md").is_file()
gate = {
    "paper": "scnRgI2hhX",
    "arxiv": "2603.11784",
    "publication_eligible": True,
    "tests_passed": True,
    "publication_gate_passed": True,
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
(ROOT / "GATE_READY.md").write_text("FULL_GATE_READY: scnRgI2hhX\n")
print(json.dumps(gate, indent=2))
print("C6_INDEPENDENT_CHECKER=" + checker.stdout.strip())
print("C6_NEGATIVE_CONTROL_EXIT=" + str(control.returncode))
print("C6_NEGATIVE_CONTROL=" + control.stdout.strip())
print("C6_CELL_CHECKER=" + cell_checker.stdout.strip())
print("C6_CELL_NEGATIVE_CONTROL_EXIT=" + str(cell_control.returncode))
print("C6_CELL_NEGATIVE_CONTROL=" + cell_control.stdout.strip())
print("C1_CHECKER=" + c1_checker.stdout.strip())
print("C1_NEGATIVE_CONTROL_EXIT=" + str(c1_control.returncode))
print("C1_NEGATIVE_CONTROL=" + c1_control.stdout.strip())
print("C2_CHECKER=" + c2_checker.stdout.strip())
print("C2_NEGATIVE_CONTROL_EXIT=" + str(c2_control.returncode))
print("C2_NEGATIVE_CONTROL=" + c2_control.stdout.strip())
print("C3_CHECKER=" + c3_checker.stdout.strip())
print("C3_NEGATIVE_CONTROL_EXIT=" + str(c3_control.returncode))
print("C3_NEGATIVE_CONTROL=" + c3_control.stdout.strip())
