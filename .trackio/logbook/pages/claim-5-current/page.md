# Claim 5 — current universal MQ lower-bound proof

## Exact claim and candidate verdict

**VERIFIED (candidate, not a live judge result).** Theorem 6.1 (arXiv v2 Theorem 7.1) states that no deterministic membership-query-only generator properly generates in the limit every countable class.

## Proof-level evidence

The current certificate validates the full generator-indexed Algorithm 3 construction. It proves `F` total recursive even if the generator issues infinitely many queries in one round, proves every support infinite, and proves the minimum queue enumerates its limiting contents.

It then checks the exhaustive dichotomy for an arbitrary output sequence. If non-`h1` hypotheses appear infinitely often, the queue enumerates `h1` and each such output gets an exclusive point outside `h1`. If they appear only finitely often, the queue enumerates the final trap hypothesis and eventual `h1` always contains its omitted trap point. Both cases yield infinitely many errors.

The independent checker validates all proof nodes. Removing the final trap destroys the second case and causes exit 1.

Fixed command: `uv sync --frozen --no-dev && uv run --no-sync python repro/src/verify.py && uv run --no-sync python repro/src/publication_gate.py`

HF run `9d904828-3252-4f26-a2a2-b10d40775567` at revision
`5be61e11000cbb2ffddacc1ae6d95030b6c48284` reported 64 logical/affinity CPUs and
0.017040 s verifier runtime. It was deterministic with no seeds.

- [Raw result](../../../../.openresearch/artifacts/claim_5/raw_result.json)
- [Checker output](../../../../.openresearch/artifacts/claim_5/checker_output.json)
- [Negative-control output](../../../../.openresearch/artifacts/claim_5/negative_control_output.json)
- [Claim contract](../../../../.openresearch/artifacts/claim_5/claim_contract.json)
- [Source audit](../../../../.openresearch/artifacts/claim_5/source_audit.md)
- [Exact commands](../../../../.openresearch/artifacts/claim_5/commands.txt)
- [Proof source](../../../../repro/src/c5_proof.py)
- [Independent checker source](../../../../repro/src/c5_checker.py)
- [Method](../../../../.openresearch/artifacts/claim_5/method.md)
- [Limitations](../../../../.openresearch/artifacts/claim_5/limitations.md)
- [Evaluator audit](../../../../.openresearch/artifacts/claim_5/EVAL.md)
- [Pinned environment](../../../../uv.lock)
