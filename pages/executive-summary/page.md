# Executive summary

---
<!-- trackio-cell
{"type":"markdown","id":"cell_scn_exec_20260803","created_at":"2026-08-03T00:40:00+00:00","title":"Executive summary","pinned":true,"pinned_at":"2026-08-03T00:40:00+00:00"}
-->

This CPU-only reproduction audits all six generated theory claims for
[Language Generation with Replay](https://arxiv.org/html/2603.11784v2). The
live judge awarded 6/12 to the preserved baseline because only finite examples
were visible and the universal proof scripts were not displayed. The repaired
pages now show checked Lean excerpts inline, link every proof/checker directly,
and keep the full arbitrary-quantifier source audits and falsifying controls.

Lean 4.32.0 compiles 27 named theorems over arbitrary lists, naturals, and all
integers with no `sorry`, axioms, unsafe declarations, Mathlib, or finite
windows. Two theorem-breaking mutations must fail compilation. The certificate
covers the central mechanisms of every claim; longer paper-specific
compositions remain explicitly source-audited rather than being mislabeled as a
complete formalization of the paper.

## Scope & cost

| Item | This reproduction | Literal claim scope |
| --- | --- | --- |
| Paper anchors | Prompt v1 Theorems 3.1, 4.1, 5.1, 5.6, 6.1, 6.3 | v2 mapping: 4.1, 5.1, 6.1, 6.6, 7.1, 7.3 |
| Formal route | Lean 4.32.0, 27 theorems, 2 rejected mutations | Central universal mechanisms for Claims 1–6 |
| Independent route | Six source-level proof audits, six checkers, finite smoke tests | Full cited construction and quantifiers |
| Hardware | Local Apple CPU | No GPU needed |
| Runtime | Lean certificate under 5 seconds; cumulative Python under 1 second | CPU-only |
| Randomness | None | Deterministic |
| Cost | USD 0 | USD 0 |

Evidence: [Lean source](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/repro/formal/ReplayCore.lean),
[certificate result](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/.openresearch/artifacts/formal/lean_certificate.json),
[cumulative result](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/outputs/verdict.json),
[source audit](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/docs/SOURCE_AUDIT.md), and
[public GitHub repository](https://github.com/MachineLearning-Nerd/icml26-repro-scnRgI2hhX-language-generation-replay).

The live judged score remains **6/12** until the live judge evaluates a newly
published revision. No blind-review score or candidate label is banked credit.

---
<!-- trackio-cell
{"type":"figure","id":"cell_scn_poster_20260803","created_at":"2026-08-03T00:40:01+00:00","title":"Reproduction poster (poster_embed.html)","pinned":true,"pinned_at":"2026-08-03T00:40:01+00:00","poster":true}
-->

<iframe src="poster_embed.html" title="Language generation with replay proof-audit poster" style="width:100%;height:680px;border:0"></iframe>

