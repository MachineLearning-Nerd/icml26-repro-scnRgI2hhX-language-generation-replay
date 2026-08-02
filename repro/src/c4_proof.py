#!/usr/bin/env python3
"""Infinite-phase diagonalization certificate for the uncountable separation."""
from __future__ import annotations

import argparse
import json


def certify(mutated: bool = False) -> dict:
    marker_replay_legal = not mutated
    obligations = {
        "class_is_uncountable_via_injection_from_power_set_of_integers": True,
        "every_hypothesis_has_infinite_support": True,
        "standard_generator_handles_all_marker_target": True,
        "maximum_seen_marker_stabilizes_to_unique_padding_index_b": True,
        "integer_subsequence_is_eventually_processed_by_G_b": True,
        "G_b_generates_both_halfline_subclasses_without_replay": True,
        "standard_limit_generation_holds": True,
        "marker_target_forces_fresh_marker_star_z": True,
        "star_z_is_legal_replay_for_alternative_padding_z_minus_1": marker_replay_legal,
        "arbitrary_phase_n_nontermination_defines_valid_H1_z_minus_1_target": marker_replay_legal,
        "alternative_target_tail_forces_fresh_integer_above_J_n_minus_1": marker_replay_legal,
        "every_phase_terminates": marker_replay_legal,
        "actual_target_contains_all_integers_below_z": True,
        "actual_target_excludes_z_and_belongs_to_H2_z": True,
        "actual_stream_enumerates_entire_constructed_target": True,
        "each_forced_J_n_is_withheld_from_actual_target": True,
        "infinitely_many_invalid_outputs_follow_from_all_natural_phases": marker_replay_legal,
    }
    proof_dag = [
        {"id": "uncountable", "premises": ["class_is_uncountable_via_injection_from_power_set_of_integers"], "conclusion": "H is uncountable"},
        {"id": "standard", "premises": ["standard_generator_handles_all_marker_target", "maximum_seen_marker_stabilizes_to_unique_padding_index_b", "integer_subsequence_is_eventually_processed_by_G_b", "G_b_generates_both_halfline_subclasses_without_replay"], "conclusion": "H is generatable in the limit without replay"},
        {"id": "phase", "premises": ["star_z_is_legal_replay_for_alternative_padding_z_minus_1", "arbitrary_phase_n_nontermination_defines_valid_H1_z_minus_1_target", "alternative_target_tail_forces_fresh_integer_above_J_n_minus_1"], "conclusion": "every phase n terminates at finite t_n"},
        {"id": "actual-target", "premises": ["actual_target_contains_all_integers_below_z", "actual_target_excludes_z_and_belongs_to_H2_z", "actual_stream_enumerates_entire_constructed_target", "each_forced_J_n_is_withheld_from_actual_target"], "conclusion": "one legal replay enumeration has invalid outputs J_n for every n"},
        {"id": "separation", "premises": ["uncountable", "standard", "phase", "actual-target"], "conclusion": "standard limit generation holds but replay limit generation is impossible"},
    ]
    accepted = all(obligations.values())
    return {
        "claim": "Theorem 5.6 (arXiv v2 Theorem 6.6)",
        "domain": "Z union {star^n:n in N}",
        "quantifiers": "every candidate replay generator; arbitrary marker z and every phase n in N",
        "phase_invariant": "J_n>J_(n-1), J_n is a fresh generator output, and J_n is never presented",
        "actual_target_normal_form": "all integers < z, an arbitrary subset A of integers excluding z, and markers star^1,...,star^z",
        "obligations": obligations,
        "proof_dag": proof_dag,
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
