# Claim 3 — Witness Protection for countable classes

## Claim and result

**VERIFIED by a source-level three-lemma audit with checked cores.** Prompt
Theorem 5.1 (arXiv v2 Theorem 6.1) gives a membership-query-only algorithm that
generates in the limit every countable UUS class even with replay.

The reproduction transcribes Algorithm 2 and audits its three universal proof
steps: per-round termination, eventual target criticality, and eventual valid
fresh output. Unlike the historical three-hypothesis execution, the proof audit
keeps target index `z`, round `t`, and prefix bound `m` symbolic.

Lean checks three failure-prone mechanisms directly. A non-replay observation
from an admissible stream must be a true target point; UUS supplies a supported
point outside every finite exclusion; and criticality can only be lost as the
finite prefix expands:

```lean
theorem criticality_monotone_in_prefix
    (support : Nat → Nat → Prop) (sure priorOutputs : Nat → Prop)
    (candidate small large : Nat) (hbound : small ≤ large)
    (critical : Critical support sure priorOutputs candidate large) :
    Critical support sure priorOutputs candidate small := by
  constructor
  · exact critical.1
  · intro earlier hearlier hconsistent x hx hsupported hnew
    exact critical.2 earlier hearlier hconsistent x
      (Nat.le_trans hx hbound) hsupported hnew
```

The full audit then follows the paper: the largest critical index stabilizes for
each round because it ranges over a finite active set; at most `2t+t²` points
are excluded; protected distinguishing witnesses cannot be generator outputs,
so their eventual appearance makes them sure and permanently evicts each false
earlier candidate. Only finitely many candidates precede the target's first
index, giving a finite stabilization time. Critical inclusion transfers every
later selected output to the target support, and avoidance of sure/prior-output
sets makes it fresh.

## Controls and formal boundary

The negative control allows the algorithm to emit a distinguishing witness.
Its later appearance can then be classified as replay, so eviction no longer
follows and the audit exits nonzero. Lean does not reimplement the entire
unbounded search loop; it kernel-checks the reusable logical cores while the
longer termination/criticality composition is audited line-by-line against the
paper source and independently checked as a proof DAG.

Fixed cumulative command:

```text
uv sync --frozen --no-dev && uv run --no-sync python repro/src/check_lean_certificate.py && uv run --no-sync python repro/src/verify.py && uv run --no-sync python repro/src/publication_gate.py
```

Direct evidence: [Lean source](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/repro/formal/ReplayCore.lean),
[full Witness Protection audit](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/repro/src/c3_proof.py),
[independent checker](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/repro/src/c3_checker.py),
[raw result](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/.openresearch/artifacts/claim_3/raw_result.json),
[source audit](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/.openresearch/artifacts/claim_3/source_audit.md), and
[paper v2](https://arxiv.org/html/2603.11784v2).

Deterministic local CPU; no seeds, GPU, paid job, or single-class inference.
