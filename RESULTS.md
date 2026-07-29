# Results

`python3 repro/src/verify.py` passes all six source-anchored claims using only
the Python standard library. The detailed, machine-readable traces are in
[`outputs/verdict.json`](outputs/verdict.json).

| Claim | Source construction | Independent executable evidence | Negative control |
|---|---|---|---|
| C1 | Theorem 3.1, Algorithm 1 | Exhaustive replay-tree audit across the burn-in boundary | Calling the base generator before burn-in lets an outsider be replayed forever |
| C2 | Theorem 4.1 | `h_infty`/`h_d` adversarial traces for twelve thresholds | The shared trace is invalid for `h_d` without replay |
| C3 | Theorem 5.1, Witness Protection | Direct transcription of sure sets, criticality, witnesses, and output rule | Emitting a protected witness prevents its later observation from becoming sure |
| C4 | Theorem 5.6 | Six symbolic adversarial phases for the padded `H_2^z` construction | The pivotal marker is illegal in the alternative target without replay |
| C5 | Theorem 6.1, Algorithm 3 | Both diagonalization and eventual-`h1` trap cases | Removing the trap removes the overgeneralization argument |
| C6 | Theorem 6.3 | All four possible first proper outputs and the exact support intersections | Without the exceptional replayed examples, the common adversarial sequence is illegal |

## Scope

These are not proxy empirical experiments. They are executable audits of the
complete constructions used by this theory paper: the finite class in C6 is
exhausted, and C1--C5 execute the stated algorithm/proof transitions with the
author-provided unbounded constructions. No finite computation is represented
as a proof of a universally quantified theorem; the primary-source proof is
the authority for those quantifiers.

## Re-run

```bash
python3 repro/src/verify.py
python3 -m json.tool outputs/verdict.json
```
