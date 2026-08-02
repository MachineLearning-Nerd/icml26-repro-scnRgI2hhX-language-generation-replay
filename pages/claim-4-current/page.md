# Claim 4 — uncountable limit-generation separation

## Claim and result

**VERIFIED by an all-phase diagonalization audit with checked cores.** Prompt
Theorem 5.6 (arXiv v2 Theorem 6.6) constructs an uncountable class that is
generatable in the limit without replay but not with replay.

The standard side audit checks the paper's explicit generator: the maximum
observed marker stabilizes at a padding index, after which the integer
subsequence is handled by the corresponding half-line generator. The free
integer subset makes the class uncountable, and Lean independently checks the
Cantor diagonal obstruction for every proposed enumeration of predicates.

```lean
theorem cantor_diagonal_not_enumerable (enumerated : Nat → Nat → Prop) :
    ∃ diagonal : Nat → Prop,
      ∀ n, ¬ (∀ x, diagonal x ↔ enumerated n x) := by
  let diagonal : Nat → Prop := fun n => ¬ enumerated n n
  refine ⟨diagonal, ?_⟩
  intro n equal
  have atDiagonal := equal n
  simp [diagonal] at atDiagonal

theorem withheld_phase_outputs_force_infinite_errors
    (stage : Nat → Nat) (invalid : Nat → Prop)
    (stageAfterPhase : ∀ phase, phase ≤ stage phase)
    (invalidAtStage : ∀ phase, invalid (stage phase)) :
    InfinitelyOften invalid := by
  intro after
  exact ⟨stage after, stageAfterPhase after, invalidAtStage after⟩
```

For replay hardness, the source-level certificate quantifies over every phase
`n`, not a six-phase prefix. Replay of marker `star^z` keeps the alternative
`H1^(z−1)` history legal. If a phase did not terminate, that alternative target
would force a fresh integer above the previous boundary; hence each phase has a
finite forced output `J_n`. The actual `H2^z` target enumerates its entire
support while withholding every `J_n`. The second Lean theorem checks that one
withheld invalid output per natural phase entails errors arbitrarily late.

## Control and scope

Removing marker replay makes the alternative history illegal and the proof
audit exits nonzero. Lean kernel-checks uncountability and the all-phase
infinite-error implication; marker stabilization, phase termination, and actual
target membership are independently transcribed and source-audited rather than
encoded as a finite experiment.

Fixed cumulative command:

```text
uv sync --frozen --no-dev && uv run --no-sync python repro/src/check_lean_certificate.py && uv run --no-sync python repro/src/verify.py && uv run --no-sync python repro/src/publication_gate.py
```

Direct evidence: [Lean source](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/repro/formal/ReplayCore.lean),
[all-phase proof audit](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/repro/src/c4_proof.py),
[independent checker](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/repro/src/c4_checker.py),
[raw result](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/.openresearch/artifacts/claim_4/raw_result.json),
[source audit](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/.openresearch/artifacts/claim_4/source_audit.md), and
[paper v2](https://arxiv.org/html/2603.11784v2).

Deterministic local CPU; no seeds, GPU, paid job, or finite phase cutoff.
