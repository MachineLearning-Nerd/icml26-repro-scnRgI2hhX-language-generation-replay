# Claim 6 — current exact verification

## Exact claim and verdict

**VERIFIED (candidate, not yet a live judge result).** Theorem 6.3 (arXiv v2 Theorem 7.3)
states that there is a finite class that no deterministic proper generator can generate in the
limit with replay. The quantified domain is all integers.

## What supersedes the historical verifier

`repro/src/c6_exact.py` supersedes the bounded `[-40,40]` check. It represents the four supports
as exact half-lines plus exceptions, exhausts all four first outputs, and proves the relevant
intersection is exactly `Z_{>=0}` or `Z_{<=0}`. `repro/src/c6_independent.py` independently
checks the emitted certificate. A second implementation, `repro/src/c6_cell_solver.py`, performs
exact quantifier elimination over a complete seven-cell partition of all integers; its checker
uses an independently hard-coded truth table.

## Exact observed evidence

| First output | Legal replays | Simultaneous targets | Exact intersection | Proper outputs available |
|---|---:|---|---|---:|
| `h1-` | `-1,-2` | `h1+,h2+` | `Z_{>=0}` | 0 |
| `h2-` | `-1,-2` | `h1+,h2+` | `Z_{>=0}` | 0 |
| `h1+` | `1,2` | `h1-,h2-` | `Z_{<=0}` | 0 |
| `h2+` | `1,2` | `h1-,h2-` | `Z_{<=0}` | 0 |

Both routes returned `VERIFIED` on Hugging Face `cpu-upgrade`. The structural run
`7edf5531-6c44-4aad-a09c-9caba93d4380` used revision `89016e13954320ae9997865dc98d5bb1f8f15b0f`,
reported 64 logical/affinity CPUs, and took 0.019140 s in the verifier. The cell route
`97114bfa-86a7-4a21-8583-4ddd4c51bb4f` used revision
`01d8d9fbdea511715c7715f125402d585a5b5ffd`, reported the same allocation, and took 0.017153 s.
Both are deterministic and use no seeds.

Fixed command: `uv sync --frozen --no-dev && uv run --no-sync python repro/src/verify.py && uv run --no-sync python repro/src/publication_gate.py`

The negative control changes one hypothesis to the common half-line. The contradiction then
disappears and both verifiers exit 1. The independent structural checker and independent cell
truth-table checker both return `PASS` on the unmutated evidence.

Downloadable evidence:

- [Structural raw result](./.openresearch/artifacts/claim_6/raw_result.json)
- [Independent checker output](./.openresearch/artifacts/claim_6/checker_output.json)
- [Negative-control output](./.openresearch/artifacts/claim_6/negative_control_output.json)
- [Independent cell-route result](./.openresearch/artifacts/claim_6/cell_route_result.json)
- [Claim contract](./.openresearch/artifacts/claim_6/claim_contract.json)
- [Source audit](./.openresearch/artifacts/claim_6/source_audit.md)
- [Exact commands](./.openresearch/artifacts/claim_6/commands.txt)
- [Structural proof source](./repro/src/c6_exact.py)
- [Structural checker source](./repro/src/c6_independent.py)
- [Cell proof source](./repro/src/c6_cell_solver.py)
- [Cell checker source](./repro/src/c6_cell_checker.py)
- [Method](./.openresearch/artifacts/claim_6/method.md)
- [Limitations](./.openresearch/artifacts/claim_6/limitations.md)
- [Evaluator audit](./.openresearch/artifacts/claim_6/EVAL.md)
- [Pinned environment](./uv.lock)

## Scope

This page makes no claim about a new judge score. It addresses the prior judge's sole Claim-6
criticism: the current verifier uses exact predicates over every integer and no bounded window.
