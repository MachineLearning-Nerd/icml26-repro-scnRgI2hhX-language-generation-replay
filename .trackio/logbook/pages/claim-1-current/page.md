# Claim 1 — current exact verification

## Exact claim and candidate verdict

**VERIFIED (candidate, not a live judge result).** Theorem 3.1 (arXiv v2 Theorem 4.1) states that a UUS binary class is uniformly generatable with replay exactly when it is uniformly generatable without replay, with no increase in sample complexity.

## Proof certificate

The verifier reconstructs Algorithm 1 for symbolic arbitrary `d`. Before `d` distinct inputs appear it emits only `x1`. Strong induction proves that every replay-sequence input remains in the target support: the pre-threshold replay set is `{x1}`, and after the threshold the assumed standard generator emits a supported fresh point. Consequently its own outputs cannot introduce unsupported future replays.

This establishes `d_replay <= d_standard`. Every standard sequence is also a replay sequence, establishing `d_standard <= d_replay`. Antisymmetry gives equality of the optimal complexities. The independent checker validates the five-node proof DAG.

The negative control emits an arbitrary outsider during burn-in. Support closure becomes false and the verifier must exit 1. This directly exercises the failure described by the paper.

Fixed command: `uv sync --frozen --no-dev && uv run --no-sync python repro/src/verify.py && uv run --no-sync python repro/src/publication_gate.py`

HF run `eebaedd5-f831-42f2-b21c-98931b550467` at revision
`f4d046d1f37fe024ff50405e205e79ea3b353ab7` reported 64 logical/affinity CPUs and
0.021013 s verifier runtime. It was deterministic with no seeds. The proof and independent checker
passed; the mutation exited 1.

- [Raw result](./.openresearch/artifacts/claim_1/raw_result.json)
- [Checker output](./.openresearch/artifacts/claim_1/checker_output.json)
- [Negative-control output](./.openresearch/artifacts/claim_1/negative_control_output.json)
- [Claim contract](./.openresearch/artifacts/claim_1/claim_contract.json)
- [Source audit](./.openresearch/artifacts/claim_1/source_audit.md)
- [Exact commands](./.openresearch/artifacts/claim_1/commands.txt)
- [Proof source](./repro/src/c1_proof.py)
- [Independent checker source](./repro/src/c1_checker.py)
- [Method](./.openresearch/artifacts/claim_1/method.md)
- [Limitations](./.openresearch/artifacts/claim_1/limitations.md)
- [Evaluator audit](./.openresearch/artifacts/claim_1/EVAL.md)
- [Pinned environment](./uv.lock)

Historical finite-support verification remains reachable and is labeled rejected baseline.
