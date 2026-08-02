# Claim 6 — finite proper-generation replay hardness

## Claim and result

**VERIFIED by three exact all-integer routes.** Prompt Theorem 6.3 (arXiv v2
Theorem 7.3) constructs four hypotheses that are properly generatable without
replay but impossible to properly generate in the limit with replay.

The four exact predicates are `Z≤0 ∪ {1}`, `Z≤0 ∪ {2}`,
`Z≥0 ∪ {−1}`, and `Z≥0 ∪ {−2}`. Lean exhausts all four possible first
proper outputs and all four possible later outputs:

```lean
theorem every_first_output_has_ambiguous_targets
    (first : ProperHypothesis) :
    let targets := ambiguousTargets first
    (∃ replayA replayB,
      properSupport first replayA ∧ properSupport first replayB ∧
      properSupport targets.1 replayA ∧ properSupport targets.2 replayB) ∧
    ∀ output, ¬ (∀ x, properSupport output x →
      properSupport targets.1 x ∧ properSupport targets.2 x) := by
  cases first <;> constructor
  -- each branch is discharged from exact all-Int intersection theorems
```

| First output | Legal replays | Simultaneous targets | Exact intersection | Class member inside it |
| --- | --- | --- | --- | --- |
| `h1−` | `−1,−2` | `h1+,h2+` | `Z≥0` | none |
| `h2−` | `−1,−2` | `h1+,h2+` | `Z≥0` | none |
| `h1+` | `1,2` | `h1−,h2−` | `Z≤0` | none |
| `h2+` | `1,2` | `h1−,h2−` | `Z≤0` | none |

The adversarial history is a legal full enumeration for both simultaneous
targets. Eventual properness for both would require every sufficiently late
output support to lie in their intersection, but the exhaustive theorem shows
that no class member does.

Two independent Python implementations agree: one manipulates exact half-line
predicates and explicit outside witnesses; the other performs exact integer
quantifier elimination over two unbounded and five singleton cells with a
separately hard-coded checker. Neither uses the historical `[-40,40]` window.

## Controls

The Lean mutation removes the exceptional point from `h2+`; the certificate
must fail compilation. Both Python routes apply the analogous mutation and must
exit nonzero. A common-half-line control is also proved positively, confirming
that the subset test is capable of accepting a genuine subset.

Fixed cumulative command:

```text
uv sync --frozen --no-dev && uv run --no-sync python repro/src/check_lean_certificate.py && uv run --no-sync python repro/src/verify.py && uv run --no-sync python repro/src/publication_gate.py
```

Direct evidence: [Lean source](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/repro/formal/ReplayCore.lean),
[structural route](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/repro/src/c6_exact.py),
[structural checker](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/repro/src/c6_independent.py),
[cell route](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/repro/src/c6_cell_solver.py),
[cell checker](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/repro/src/c6_cell_checker.py),
[raw exact result](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/.openresearch/artifacts/claim_6/raw_result.json),
[source audit](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/.openresearch/artifacts/claim_6/source_audit.md), and
[paper v2](https://arxiv.org/html/2603.11784v2).

Deterministic local CPU; no seeds, GPU, paid job, bounded window, or horizon.
