# Claim 3 — current universal Witness Protection proof

## Exact claim and candidate verdict

**VERIFIED (candidate, not a live judge result).** Theorem 5.1 (arXiv v2 Theorem 6.1) states that exact Algorithm 2, Witness Protection, is a computable membership-query-only generator for every countable UUS class under replay.

## Proof-level evidence

The current verifier checks the source's three universal lemmas and their composition for symbolic arbitrary target index `z`, round `t`, and prefix `m`:

1. Every round terminates: critical indices stabilize and the infinite support outgrows at most `2t+t^2` exclusions.
2. The target eventually remains critical: each of finitely many earlier false candidates is evicted when its protected witness is enumerated.
3. Outputs are eventually valid and fresh: critical inclusion transfers the chosen output to the target, while avoidance of the sure set and prior outputs excludes every seen point.

All finite predicates use membership queries only. The independent checker validates the six-node proof DAG. The negative control disables witness protection; witness eviction and eventual criticality become unjustified, so the verifier exits 1.

Fixed command: `uv sync --frozen --no-dev && uv run --no-sync python repro/src/verify.py && uv run --no-sync python repro/src/publication_gate.py`

Raw remote evidence is added in the next cumulative descendant.
