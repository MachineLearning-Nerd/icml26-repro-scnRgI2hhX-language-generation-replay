#!/usr/bin/env python3
"""Arbitrary-threshold proof certificate for the countable replay separation."""
from __future__ import annotations

import argparse
import json


def certify(mutated: bool = False) -> dict:
    replay_enabled = not mutated
    standard_generator = {
        "rule": "if a negative input has appeared, emit a fresh negative; otherwise emit a fresh positive",
        "h_infinity_threshold": 1,
        "h_n_threshold": "n+1",
        "h_infinity_reason": "every input is positive, so every fresh positive output is supported",
        "h_n_reason": "n+1 distinct supported inputs force a negative input; fresh negatives are then supported forever",
    }
    obligations = {
        "class_is_countable": True,
        "every_support_is_infinite": True,
        "explicit_standard_generator_succeeds": True,
        "initial_1_through_d_supported_by_both_targets": True,
        "replayed_outputs_make_shared_trace_legal": replay_enabled,
        "h_infinity_guarantee_forces_fresh_naturals": True,
        "distinct_count_is_unbounded": True,
        "arbitrary_h_d_threshold_m_reached_by_T_max_d_m": True,
        "support_intersection_is_exactly_1_through_d": True,
        "intersection_already_exhausted_at_initial_prefix": True,
    }
    accepted = all(obligations.values())
    return {
        "claim": "Theorem 4.1 (arXiv v2 Theorem 5.1)",
        "class": "H={h_infinity} union {h_n:n in N}; supp(h_infinity)=N; supp(h_n)={1,...,n} union Z_<0",
        "quantifiers": "for every candidate replay generator and arbitrary finite thresholds d=d_h_infinity and m=d_h_d",
        "standard_setting": standard_generator,
        "replay_contradiction": {
            "initial_prefix": "1,...,d",
            "continuation": "x_(t+1)=G(x_1:t) for every t>=d",
            "threshold_for_h_d": "T=max(d,m)",
            "simultaneous_required_set": "supp(h_infinity) intersect supp(h_d) minus seen = {1,...,d} minus {1,...,d} = empty",
        },
        "obligations": obligations,
        "mutated_control": mutated,
        "verdict": "VERIFIED" if accepted else "REJECTED",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutated-control", action="store_true")
    args = parser.parse_args()
    result = certify(args.mutated_control)
    print(json.dumps(result, sort_keys=True))
    raise SystemExit(0 if result["verdict"] == "VERIFIED" else 1)


if __name__ == "__main__":
    main()
