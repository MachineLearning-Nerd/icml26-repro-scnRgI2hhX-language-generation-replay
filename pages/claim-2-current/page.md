# Claim 2 — countable non-uniform separation

## Claim and result

**VERIFIED by an arbitrary-threshold construction audit plus Lean.** Prompt
Theorem 4.1 (arXiv v2 Theorem 5.1) constructs the countable UUS class
`{h∞} ∪ {h_n : n ∈ N}`, which is non-uniformly generatable without replay but
not with replay.

The supports are represented exactly over all integers:

```lean
def hInf (x : Int) : Prop := 1 ≤ x
def hFinite (d x : Int) : Prop :=
  (1 ≤ x ∧ x ≤ d) ∨ x < 0

theorem countable_intersection_exact (d x : Int) :
    hInf x ∧ hFinite d x ↔ 1 ≤ x ∧ x ≤ d := by
  simp only [hInf, hFinite]
  constructor
  · rintro ⟨hx, hfd⟩
    rcases hfd with hfd | hneg
    · exact hfd
    · omega
  · rintro h
    exact ⟨h.1, Or.inl h⟩
```

For arbitrary replay thresholds `d` and `m`, the adversary presents
`1,…,d`, then feeds back every output. Correctness for `h∞` forces fresh
naturals and therefore unbounded distinct count. The same history is legal for
`h_d`; after its finite threshold, a simultaneous output must be fresh and in
`supp(h∞) ∩ supp(h_d) = {1,…,d}`. Lean checks that exact quantified
intersection and that no point above `d` belongs to it. The initial prefix has
already exhausted it, yielding the contradiction.

The standard side uses the explicit paper-compatible rule: output a fresh
positive until a negative observation appears, then a fresh negative. Threshold
`1` works for `h∞`; `n+1` distinct supported observations force a negative
for `h_n` by pigeonhole, after which fresh negatives remain supported.

## Controls and scope

Removing replay makes the shared `h_d` trace illegal and the Python proof
audit exits nonzero. The Lean runner removes `hFinite`'s upper bound; the exact
intersection theorem must then fail compilation. This is all-integer,
arbitrary-threshold evidence, not the historical `d=1,…,12` sweep.

Fixed cumulative command:

```text
uv sync --frozen --no-dev && uv run --no-sync python repro/src/check_lean_certificate.py && uv run --no-sync python repro/src/verify.py && uv run --no-sync python repro/src/publication_gate.py
```

Direct evidence: [Lean source](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/repro/formal/ReplayCore.lean),
[Lean result](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/.openresearch/artifacts/formal/lean_certificate.json),
[arbitrary-threshold audit](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/repro/src/c2_proof.py),
[independent checker](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/repro/src/c2_checker.py),
[raw result](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/.openresearch/artifacts/claim_2/raw_result.json),
[source audit](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/.openresearch/artifacts/claim_2/source_audit.md), and
[paper v2](https://arxiv.org/html/2603.11784v2).

Deterministic local CPU; no seeds, GPU, paid job, or truncated domain.
