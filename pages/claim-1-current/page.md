# Claim 1 — uniform generation equivalence

## Claim and result

**VERIFIED by a source-anchored audit with a checked universal core.** Prompt
Theorem 3.1 (arXiv v2 Theorem 4.1) says uniform generation with replay is
equivalent to ordinary uniform generation and does not increase the optimal
sample complexity.

The paper's conversion repeats the supported first observation until the
standard threshold is reached, then calls the standard generator. The Lean
certificate checks this for arbitrary types, support predicates, histories,
thresholds, and distinct-count functions. It also checks that replay preserves
support once every generator call on a supported prefix is safe.

```lean
theorem converted_generator_same_threshold {α : Type u}
    (support : α → Prop) (gen : List α → α) (burn : α)
    (threshold : Nat) (distinctCount : List α → Nat)
    (standardGuarantee : ∀ xs, AllSupported support xs →
      threshold ≤ distinctCount xs → support (gen xs) ∧ gen xs ∉ xs)
    (xs : List α) (hxs : AllSupported support xs)
    (reached : threshold ≤ distinctCount xs) :
    support (convertedGenerator gen burn threshold distinctCount xs) ∧
      convertedGenerator gen burn threshold distinctCount xs ∉ xs := by
  simpa [convertedGenerator, reached] using standardGuarantee xs hxs reached
```

The reverse inequality needs no conversion: every standard target-support
sequence is an allowed replay sequence. Together the two inequalities give the
same optimal threshold. The custom proof-DAG and finite replay-tree executor are
retained as independent transcription and smoke-test routes.

## Falsifying control and scope

Changing burn-in to an unsupported outsider rejects the Python certificate.
The Lean runner also changes theorem definitions in two independent ways and
requires both mutated files to fail compilation. The Lean kernel covers the
support-closure and same-threshold mechanism; the equivalence's full paper
definitions are audited against the cited proof rather than redefined wholesale
inside Lean.

Fixed cumulative command:

```text
uv sync --frozen --no-dev && uv run --no-sync python repro/src/check_lean_certificate.py && uv run --no-sync python repro/src/verify.py && uv run --no-sync python repro/src/publication_gate.py
```

Direct evidence: [Lean source](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/repro/formal/ReplayCore.lean),
[Lean result](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/.openresearch/artifacts/formal/lean_certificate.json),
[full proof audit](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/repro/src/c1_proof.py),
[independent checker](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/repro/src/c1_checker.py),
[raw result](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/.openresearch/artifacts/claim_1/raw_result.json),
[source audit](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/.openresearch/artifacts/claim_1/source_audit.md),
[ar5iv paper](https://ar5iv.labs.arxiv.org/html/2603.11784), and
[GitHub repository](https://github.com/MachineLearning-Nerd/icml26-repro-scnRgI2hhX-language-generation-replay).

Deterministic local CPU; no seeds, GPU, paid job, or finite-window inference.
