# Evaluator-visible evidence matrix

This retained route now points to the canonical claim pages. The live judged
score remains **6/12** until the live judge evaluates a new exact revision.

| Claim | Canonical page | Visible checked code | Independent route | Falsifying control | Scope |
| --- | --- | --- | --- | --- | --- |
| 1 | [Uniform equivalence](#/claim-1-current) | Lean same-threshold and replay-closure theorems inline | [proof audit](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/repro/src/c1_proof.py) | unsupported burn-in rejected | arbitrary support, history, threshold |
| 2 | [Countable separation](#/claim-2-current) | Lean all-integer arbitrary-`d` intersection inline | [proof audit](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/repro/src/c2_proof.py) | no-replay history rejected | every finite threshold, exact `Z` |
| 3 | [Witness Protection](#/claim-3-current) | Lean sure-set, UUS exclusion, criticality monotonicity inline | [proof audit](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/repro/src/c3_proof.py) | unprotected witness rejected | arbitrary countable UUS class |
| 4 | [Uncountable separation](#/claim-4-current) | Lean Cantor and all-phase error theorems inline | [proof audit](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/repro/src/c4_proof.py) | missing marker replay rejected | every phase, no finite cutoff |
| 5 | [MQ lower bound](#/claim-5-current) | Lean exhaustive temporal dichotomy inline | [proof audit](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/repro/src/c5_proof.py) | missing final trap rejected | arbitrary deterministic computable generator |
| 6 | [Finite replay hardness](#/claim-6-current) | Lean exhaustive first/later outputs inline | [exact solver](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/repro/src/c6_exact.py), [cell solver](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/repro/src/c6_cell_solver.py) | two mutations rejected | all integers, all four branches |

The [Lean runner](https://huggingface.co/spaces/DineshAI/scnRgI2hhX/blob/main/repro/src/check_lean_certificate.py)
rejects proof escapes, compiles the unmutated certificate, and requires two
materially different theorem-breaking mutations to fail. The historical finite
checks remain at [Historical rejected baseline](#/historical-rejected-baseline)
and are not used as universal evidence.

