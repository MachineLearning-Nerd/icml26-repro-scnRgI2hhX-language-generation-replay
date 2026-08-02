# Current verification — Claim 6 exact cell certificate

## Exact claim

The paper's Theorem 6.3 (Theorem 7.3 in arXiv v2) gives a finite class of four subsets of the integers that is properly generatable in the limit without replay but is not properly generatable in the limit with replay.

## Current certificate

This route is independent of the historical `[-40,40]` check. It partitions all of `Z` into two unbounded cells and five boundary singletons. Membership in every defining half-line and exceptional singleton is constant on each cell, so the resulting truth table is an exact quantifier elimination, not sampling.

The checker exhausts all four possible first outputs. The opposite target pair intersects in exactly `x >= 0` or exactly `x <= 0`; every proper hypothesis has a certified cell outside that intersection. A shared legal replay history therefore prevents any deterministic proper generator from being eventually correct for both targets.

Status before remote evidence capture: **candidate VERIFIED**. The result is not a new judge score. The superseded finite-window page is preserved as **Historical rejected baseline**.

## Reproducibility contract

Fixed command: `uv sync --frozen --no-dev && uv run --no-sync python repro/src/verify.py && uv run --no-sync python repro/src/publication_gate.py`

- Producer: `repro/src/c6_cell_solver.py`
- Independent checker: `repro/src/c6_cell_checker.py`
- Negative control: delete the exceptional point `-2` from `h2+`; the verifier must exit nonzero.
- Domain: every integer, represented by a complete symbolic partition.
- Stochasticity: none.

Run metadata and raw output will be mirrored on the cumulative descendant after this sibling route is evaluated.
