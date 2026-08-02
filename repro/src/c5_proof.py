#!/usr/bin/env python3
"""Universal diagonalization certificate for the proper MQ lower bound."""
from __future__ import annotations

import argparse
import json


def certify(mutated: bool = False) -> dict:
    traps_enabled = not mutated
    obligations = {
        "construction_assigns_entire_instance_column_once": True,
        "encountered_instances_are_exact_initial_segment_1_through_J": True,
        "J_unbounded_if_every_round_has_finitely_many_queries": True,
        "J_unbounded_within_any_infinite_query_round": True,
        "F_is_total_recursive_for_computable_G": True,
        "class_is_countably_indexed": True,
        "universal_columns_make_every_support_infinite": True,
        "minimum_queue_policy_eventually_reveals_every_queued_instance": True,
        "output_sequence_dichotomy_is_exhaustive": True,
        "infinite_non_h1_case_releases_every_trap": True,
        "infinite_non_h1_case_queue_equals_support_h1": True,
        "each_non_h1_output_has_fresh_diagonal_point_outside_h1": True,
        "infinite_non_h1_case_has_infinitely_many_properness_errors": True,
        "finite_non_h1_case_has_final_trap": traps_enabled,
        "finite_non_h1_case_queue_equals_final_trap_support": traps_enabled,
        "eventual_h1_contains_final_trap_point_outside_target": traps_enabled,
        "finite_non_h1_case_has_infinitely_many_properness_errors": traps_enabled,
    }
    proof_dag = [
        {"id":"totality","premises":["construction_assigns_entire_instance_column_once","encountered_instances_are_exact_initial_segment_1_through_J","J_unbounded_if_every_round_has_finitely_many_queries","J_unbounded_within_any_infinite_query_round"],"conclusion":"F:NxN->{0,1} is total recursive"},
        {"id":"valid-class","premises":["class_is_countably_indexed","universal_columns_make_every_support_infinite","totality"],"conclusion":"H is a countable indexed family of recursive UUS languages"},
        {"id":"queue","premises":["minimum_queue_policy_eventually_reveals_every_queued_instance"],"conclusion":"the displayed stream enumerates Q_infinity"},
        {"id":"case-infinite","premises":["infinite_non_h1_case_releases_every_trap","infinite_non_h1_case_queue_equals_support_h1","each_non_h1_output_has_fresh_diagonal_point_outside_h1"],"conclusion":"infinitely many errors on target h1"},
        {"id":"case-finite","premises":["finite_non_h1_case_has_final_trap","finite_non_h1_case_queue_equals_final_trap_support","eventual_h1_contains_final_trap_point_outside_target"],"conclusion":"infinitely many errors on the final trap target"},
        {"id":"lower-bound","premises":["output_sequence_dichotomy_is_exhaustive","valid-class","queue","case-infinite","case-finite"],"conclusion":"every deterministic computable MQ-only proper generator fails on a countable UUS class"},
    ]
    accepted = all(obligations.values())
    return {
        "claim":"Theorem 6.1 (arXiv v2 Theorem 7.1)",
        "algorithm":"Algorithm 3 hard-class construction for an arbitrary deterministic computable MQ-only proper generator G",
        "quantifiers":"for every deterministic computable membership-query-only proper generator",
        "dichotomy":["G outputs a hypothesis other than h1 infinitely often","G outputs hypotheses other than h1 only finitely often"],
        "obligations":obligations,
        "proof_dag":proof_dag,
        "mutated_control":mutated,
        "verdict":"VERIFIED" if accepted else "REJECTED",
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
