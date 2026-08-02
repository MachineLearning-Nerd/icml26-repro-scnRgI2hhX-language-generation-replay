# Claim 5 — deterministic membership-query lower bound

## Claim and result

**VERIFIED by a generator-indexed source audit with a checked exhaustive
dichotomy.** Prompt Theorem 6.1 (arXiv v2 Theorem 7.1) says no deterministic
membership-query-only generator can properly generate in the limit every
countable hypothesis class.

The audit follows Algorithm 3 for an arbitrary deterministic computable
generator. It checks that each instance column of `F(i,j)` is assigned once,
the assigned columns are exactly an initial segment, and `J` is unbounded
whether each round has finitely many queries or one round has infinitely many.
This makes `F` total recursive. Universally supported fresh columns make every
hypothesis support infinite, and the minimum-queue policy enumerates every
queued point.

Lean kernel-checks the exhaustive temporal split and its consequence:

```lean
theorem proper_diagonalization_dichotomy
    (nonReference error : Nat → Prop)
    (diagonalError : ∀ time, nonReference time → error time)
    (finalTrapError : EventuallyNever nonReference →
      ∃ after, ∀ time, after ≤ time → error time) :
    InfinitelyOften error := by
  rcases infinite_or_eventually_never nonReference with often | eventually
  · intro after
    rcases often after with ⟨time, htime, hnonref⟩
    exact ⟨time, htime, diagonalError time hnonref⟩
  · rcases finalTrapError eventually with ⟨start, herror⟩
    intro after
    let time := max after start
    exact ⟨time, Nat.le_max_left _ _, herror time (Nat.le_max_right _ _)⟩
```

If non-`h1` outputs occur infinitely often, every such output receives an
exclusive diagonal point outside target `h1`, while the queue enumerates
`supp(h1)`. Otherwise a final trap exists, the queue enumerates its hypothesis,
and eventual `h1` always contains the trap point omitted by the target. Either
case gives errors arbitrarily late.

## Control and formal boundary

Removing the final trap destroys the eventually-`h1` branch and makes the
Python proof audit fail. Lean checks that the two temporal cases are exhaustive
and that the construction's two error implications prove infinitely many
errors. Total recursiveness and queue/support equality remain explicit
source-level invariants, not pretense that a finite sample covers arbitrary
generators.

Fixed cumulative command:

```text
uv sync --frozen --no-dev && uv run --no-sync python repro/src/check_lean_certificate.py && uv run --no-sync python repro/src/verify.py && uv run --no-sync python repro/src/publication_gate.py
```

Direct evidence: [Lean source](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/repro/formal/ReplayCore.lean),
[generator-indexed proof audit](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/repro/src/c5_proof.py),
[independent checker](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/repro/src/c5_checker.py),
[raw result](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/.openresearch/artifacts/claim_5/raw_result.json),
[source audit](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/.openresearch/artifacts/claim_5/source_audit.md), and
[paper v2](https://arxiv.org/html/2603.11784v2).

Deterministic local CPU; no seeds, GPU, paid job, or finite output-pattern claim.
