# Claim 4 — current infinite diagonalization proof

## Exact claim and candidate verdict

**VERIFIED (candidate, not a live judge result).** Theorem 5.6 (arXiv v2 Theorem 6.6) constructs an uncountable class that is generatable in the limit without replay but not with replay.

## Proof-level evidence

The current certificate covers both halves of the separation. It verifies the source's explicit standard generator, including marker-index stabilization and both half-line subclasses. Uncountability follows from the arbitrary integer subset in each subclass; every support is infinite.

For replay hardness, it reasons over every natural phase `n`, not six phases. The fresh marker `star^z` makes each counterfactual `H1^(z-1)` enumeration legal only through replay. Nontermination of any phase would force a fresh integer above its current boundary, so every phase terminates. The constructed `H2^z` target enumerates every integer below `z` but withholds each forced output `J_n`, producing infinitely many invalid outputs.

The independent checker validates the proof DAG. Removing replay permission for `star^z` invalidates the phase argument and causes exit 1.

Fixed command: `uv sync --frozen --no-dev && uv run --no-sync python repro/src/verify.py && uv run --no-sync python repro/src/publication_gate.py`

HF run `85301bff-155c-425e-9fc8-76973c7a9c5d` at revision
`14ee45596d549cd6f1cfbb3e09155f5d50706718` reported 64 logical/affinity CPUs and
0.042127 s verifier runtime. It was deterministic with no seeds.

- [Raw result](../../../../.openresearch/artifacts/claim_4/raw_result.json)
- [Checker output](../../../../.openresearch/artifacts/claim_4/checker_output.json)
- [Negative-control output](../../../../.openresearch/artifacts/claim_4/negative_control_output.json)
- [Claim contract](../../../../.openresearch/artifacts/claim_4/claim_contract.json)
- [Source audit](../../../../.openresearch/artifacts/claim_4/source_audit.md)
- [Exact commands](../../../../.openresearch/artifacts/claim_4/commands.txt)
