#!/usr/bin/env python3
"""Exact structural certificate for Theorem 6.3 (arXiv v2: 7.3)."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "outputs" / "c6_exact.json"


def supports(mutated: bool = False) -> dict[str, tuple[str, int, int | None]]:
    return {
        "h1-": ("le", 0, 1),
        "h2-": ("le", 0, 2),
        "h1+": ("ge", 0, -1),
        "h2+": ("ge", 0, None if mutated else -2),
    }


def contains(support: tuple[str, int, int | None], x: int) -> bool:
    direction, boundary, exception = support
    in_halfline = x <= boundary if direction == "le" else x >= boundary
    return in_halfline or x == exception


def exact_intersection(
    left: tuple[str, int, int | None], right: tuple[str, int, int | None]
) -> tuple[str, int]:
    assert left[:2] == right[:2]
    assert left[2] != right[2]
    if left[2] is not None:
        assert not contains((left[0], left[1], None), left[2])
    if right[2] is not None:
        assert not contains((right[0], right[1], None), right[2])
    return left[0], left[1]


def outside_witness(
    support: tuple[str, int, int | None], intersection: tuple[str, int]
) -> int | None:
    direction, boundary, exception = support
    target_direction, target_boundary = intersection
    candidates = [exception]
    candidates.append(boundary - 1 if direction == "le" else boundary + 1)
    for candidate in candidates:
        if candidate is None or not contains(support, candidate):
            continue
        in_intersection = candidate <= target_boundary if target_direction == "le" else candidate >= target_boundary
        if not in_intersection:
            return candidate
    return None


def branch_certificate(first: str, hs: dict[str, tuple[str, int, int | None]]) -> dict:
    first_sign = first[-1]
    if first_sign == "-":
        replays = [-1, -2]
        targets = ["h1+", "h2+"]
        tail = "all positive integers"
        intersection = exact_intersection(hs[targets[0]], hs[targets[1]])
    else:
        replays = [1, 2]
        targets = ["h1-", "h2-"]
        tail = "all negative integers"
        intersection = exact_intersection(hs[targets[0]], hs[targets[1]])

    replay_legal = all(contains(hs[first], x) for x in replays)
    prefix = {0, *replays}
    enumerates = {}
    for target in targets:
        direction, boundary, exception = hs[target]
        tail_matches_halfline = (direction == "ge" and tail == "all positive integers") or (
            direction == "le" and tail == "all negative integers"
        )
        enumerates[target] = tail_matches_halfline and boundary == 0 and exception in prefix

    witnesses = {name: outside_witness(support, intersection) for name, support in hs.items()}
    no_admissible_proper_output = all(witness is not None for witness in witnesses.values())
    return {
        "first_output": first,
        "replays": replays,
        "targets": targets,
        "tail": tail,
        "replay_legal_for_every_target": replay_legal,
        "enumerates_both_targets_exactly": all(enumerates.values()),
        "intersection_normal_form": f"x {intersect_symbol(intersection)} 0",
        "outside_witness_for_each_proper_output": witnesses,
        "no_admissible_proper_output": no_admissible_proper_output,
        "contradiction": replay_legal and all(enumerates.values()) and no_admissible_proper_output,
    }


def intersect_symbol(intersection: tuple[str, int]) -> str:
    return "<=" if intersection[0] == "le" else ">="


def verify(mutated: bool = False) -> dict:
    hs = supports(mutated)
    branches = [branch_certificate(first, hs) for first in hs]
    all_first_outputs_exhausted = {row["first_output"] for row in branches} == set(hs)
    theorem_holds = all_first_outputs_exhausted and all(row["contradiction"] for row in branches)
    result = {
        "claim": "Theorem 6.3 (arXiv v2 Theorem 7.3)",
        "verdict": "VERIFIED" if theorem_holds else "REJECTED",
        "domain": "all integers, represented by exact half-line predicates; no truncation or horizon",
        "quantifiers": "for every deterministic proper generator; all four possible first outputs",
        "assumptions": {
            "finite_class_size": len(hs),
            "uus": True,
            "proper_outputs_restricted_to_class": True,
            "enumeration_with_replay": True,
        },
        "all_first_outputs_exhausted": all_first_outputs_exhausted,
        "branches": branches,
        "proof_rule": (
            "The identical history is a legal full enumeration for two targets. Eventual properness "
            "for both therefore requires one output support to be a subset of their intersection; "
            "the structural witnesses prove that no class member is such a subset."
        ),
        "mutated_control": mutated,
    }
    if mutated:
        assert not theorem_holds, "mutation must destroy the contradiction"
    else:
        assert theorem_holds
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutated-control", action="store_true")
    args = parser.parse_args()
    result = verify(args.mutated_control)
    if args.mutated_control:
        print(json.dumps(result, sort_keys=True))
        raise SystemExit(1)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("C6_EXACT_RESULT=" + json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
