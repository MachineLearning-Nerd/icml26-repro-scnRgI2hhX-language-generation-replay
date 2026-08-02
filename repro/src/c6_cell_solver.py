#!/usr/bin/env python3
"""Exact cell-decomposition certificate for Theorem 6.3 / v2 Theorem 7.3."""
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass


@dataclass(frozen=True)
class Cell:
    name: str
    lower: int | None
    upper: int | None


CELLS = (
    Cell("x<=-3", None, -3),
    Cell("x=-2", -2, -2),
    Cell("x=-1", -1, -1),
    Cell("x=0", 0, 0),
    Cell("x=1", 1, 1),
    Cell("x=2", 2, 2),
    Cell("x>=3", 3, None),
)


def atom_truth(cell: Cell, operator: str, value: int) -> bool:
    if operator == "<=":
        if cell.upper is not None and cell.upper <= value:
            return True
        if cell.lower is not None and cell.lower > value:
            return False
    elif operator == ">=":
        if cell.lower is not None and cell.lower >= value:
            return True
        if cell.upper is not None and cell.upper < value:
            return False
    elif operator == "=":
        if cell.lower == cell.upper == value:
            return True
        if (cell.upper is not None and cell.upper < value) or (
            cell.lower is not None and cell.lower > value
        ):
            return False
    raise AssertionError(f"atom {operator}{value} is not constant on {cell.name}")


def support_vector(direction: str, exception: int | None) -> tuple[bool, ...]:
    half_line = "<=" if direction == "minus" else ">="
    return tuple(
        atom_truth(cell, half_line, 0)
        or (exception is not None and atom_truth(cell, "=", exception))
        for cell in CELLS
    )


def certify(mutated: bool = False) -> dict:
    supports = {
        "h1-": support_vector("minus", 1),
        "h2-": support_vector("minus", 2),
        "h1+": support_vector("plus", -1),
        "h2+": support_vector("plus", None if mutated else -2),
    }
    expected_adjacency = (
        (None, -3), (-2, -2), (-1, -1), (0, 0),
        (1, 1), (2, 2), (3, None),
    )
    complete_partition = tuple((cell.lower, cell.upper) for cell in CELLS) == expected_adjacency
    branches = []
    for first in supports:
        minus_first = first.endswith("-")
        targets = ("h1+", "h2+") if minus_first else ("h1-", "h2-")
        intersection = tuple(a and b for a, b in zip(supports[targets[0]], supports[targets[1]]))
        expected = tuple(
            atom_truth(cell, ">=" if minus_first else "<=", 0) for cell in CELLS
        )
        no_subset = all(
            any(member and not shared for member, shared in zip(vector, intersection))
            for vector in supports.values()
        )
        branches.append({
            "first_output": first,
            "targets": list(targets),
            "intersection_cells": [cell.name for cell, present in zip(CELLS, intersection) if present],
            "intersection_is_exact_half_line": intersection == expected,
            "no_proper_support_is_subset": no_subset,
            "contradiction": intersection == expected and no_subset,
        })
    verdict = "VERIFIED" if complete_partition and all(row["contradiction"] for row in branches) else "REJECTED"
    return {
        "claim": "Theorem 6.3 (arXiv v2 Theorem 7.3)",
        "method": "exact quantifier elimination by a complete symbolic integer-cell partition",
        "domain": "all integers; two unbounded cells, five singleton boundary cells",
        "cells": [cell.name for cell in CELLS],
        "complete_disjoint_partition": complete_partition,
        "support_truth_vectors": {name: list(vector) for name, vector in supports.items()},
        "branches": branches,
        "mutated_control": mutated,
        "verdict": verdict,
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
