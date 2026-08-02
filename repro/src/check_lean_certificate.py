#!/usr/bin/env python3
"""Compile the Lean certificate and require two theorem-breaking controls."""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "repro" / "formal" / "ReplayCore.lean"
OUT = ROOT / ".openresearch" / "artifacts" / "formal" / "lean_certificate.json"
LEAN = ("elan", "run", "leanprover/lean4:v4.32.0", "lean")

FORBIDDEN_DECLARATIONS = re.compile(
    r"^\s*(?:axiom|admit|opaque|unsafe\s+(?:def|theorem))\b|\bsorry\b",
    re.MULTILINE,
)

MUTATIONS = {
    "remove_h2plus_exception": (
        "def h2Plus (x : Int) : Prop := 0 ≤ x ∨ x = -2",
        "def h2Plus (x : Int) : Prop := 0 ≤ x",
    ),
    "remove_hfinite_upper_bound": (
        "(1 ≤ x ∧ x ≤ d) ∨ x < 0",
        "1 ≤ x ∨ x < 0",
    ),
}

THEOREMS = [
    "replay_support_closure",
    "converted_generator_safe",
    "converted_generator_same_threshold",
    "criticality_monotone_in_prefix",
    "sure_observation_is_target",
    "finite_exclusion_cannot_block_uus",
    "infinite_or_eventually_never",
    "proper_diagonalization_dichotomy",
    "withheld_phase_outputs_force_infinite_errors",
    "countable_intersection_exact",
    "countable_intersection_exhausted",
    "plus_intersection_exact",
    "minus_intersection_exact",
    "minus_replays_legal",
    "plus_replays_legal",
    "h1Minus_not_subset_plus_intersection",
    "h2Minus_not_subset_plus_intersection",
    "h1Plus_not_subset_plus_intersection",
    "h2Plus_not_subset_plus_intersection",
    "h1Minus_not_subset_minus_intersection",
    "h2Minus_not_subset_minus_intersection",
    "h1Plus_not_subset_minus_intersection",
    "h2Plus_not_subset_minus_intersection",
    "common_plus_halfline_is_subset",
    "common_minus_halfline_is_subset",
    "every_first_output_has_ambiguous_targets",
    "cantor_diagonal_not_enumerable",
]


def run_lean(path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        (*LEAN, str(path)),
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def main() -> None:
    source = SOURCE.read_text()
    forbidden = sorted(set(FORBIDDEN_DECLARATIONS.findall(source)))
    if forbidden:
        raise SystemExit(f"forbidden proof escape found: {forbidden}")

    missing = [name for name in THEOREMS if f"theorem {name}" not in source]
    if missing:
        raise SystemExit(f"missing theorem declarations: {missing}")

    version = subprocess.run(
        (*LEAN[:-1], "lean", "--version"),
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    ).stdout.strip()
    main_run = run_lean(SOURCE)
    if main_run.returncode != 0:
        raise SystemExit(main_run.stderr or main_run.stdout)

    controls = {}
    with tempfile.TemporaryDirectory(prefix="replay-lean-controls-") as tmp:
        tmp_path = Path(tmp)
        for name, (old, new) in MUTATIONS.items():
            if source.count(old) != 1:
                raise SystemExit(f"mutation anchor {name!r} is not unique")
            mutated = source.replace(old, new)
            mutation_path = tmp_path / f"{name}.lean"
            mutation_path.write_text(mutated)
            run = run_lean(mutation_path)
            controls[name] = {
                "compile_failed_as_required": run.returncode != 0,
                "returncode_nonzero": run.returncode != 0,
            }
            if run.returncode == 0:
                raise SystemExit(f"negative control unexpectedly compiled: {name}")

    result = {
        "certificate": str(SOURCE.relative_to(ROOT)),
        "certificate_sha256": hashlib.sha256(source.encode()).hexdigest(),
        "domain": "all quantified List/Nat/Int values; no finite test window",
        "forbidden_proof_escapes_absent": True,
        "lean_version": version,
        "main_compile_succeeded": True,
        "negative_controls": controls,
        "theorems": THEOREMS,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("LEAN_CERTIFICATE_RESULT=" + json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
