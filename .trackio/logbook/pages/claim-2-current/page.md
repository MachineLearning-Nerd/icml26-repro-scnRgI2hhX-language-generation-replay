# Claim 2 — current exact verification

## Exact claim and candidate verdict

**VERIFIED (candidate, not a live judge result).** Theorem 4.1 (arXiv v2 Theorem 5.1) constructs the countable UUS class `H={h_infinity} union {h_n}` over all integers. It is non-uniformly generatable without replay but not with replay.

## Exact evidence

The standard side uses an explicit generator, not only the general countable-class theorem: emit fresh positives until a negative input appears, then fresh negatives. Its thresholds are 1 for `h_infinity` and `n+1` for `h_n`.

For the replay lower bound, the certificate retains symbolic arbitrary thresholds `d` and `m`. The adversary presents `1,...,d` and then replays every output. The `h_infinity` guarantee forces fresh naturals and unbounded distinct count. At `T=max(d,m)`, the same trace also activates `h_d`; both targets require a fresh output in their intersection `{1,...,d}`, already exhausted by the initial prefix. The independent checker validates this contradiction without a finite `d` sweep.

The negative control removes replay legality. The shared trace then ceases to be valid for `h_d`, and the verifier exits 1.

Fixed command: `uv sync --frozen --no-dev && uv run --no-sync python repro/src/verify.py && uv run --no-sync python repro/src/publication_gate.py`

HF run `c89d634b-4039-4d14-aba4-495b7c5b68cf` at revision
`2324dcec8bc1867501818e5df21aff90558baebe` reported 64 logical/affinity CPUs and
0.025948 s verifier runtime. It was deterministic with no seeds.

- [Raw result](../../../../.openresearch/artifacts/claim_2/raw_result.json)
- [Checker output](../../../../.openresearch/artifacts/claim_2/checker_output.json)
- [Negative-control output](../../../../.openresearch/artifacts/claim_2/negative_control_output.json)
- [Claim contract](../../../../.openresearch/artifacts/claim_2/claim_contract.json)
- [Source audit](../../../../.openresearch/artifacts/claim_2/source_audit.md)
- [Exact commands](../../../../.openresearch/artifacts/claim_2/commands.txt)
