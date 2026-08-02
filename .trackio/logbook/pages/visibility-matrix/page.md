# Evaluator-visible evidence matrix

Start here. Each current claim page states the exact quantified claim, observed proof obligations, fixed command, CPU/runtime, limitations, and links to code and raw evidence. The live judged score remains **6/12** until a new judge verdict is recorded.

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [Exact reduction](#/claim-1-current) | [proof](./repro/src/c1_proof.py), [checker](./repro/src/c1_checker.py) | Both complexity inequalities; 5 proof nodes | [JSON](./.openresearch/artifacts/claim_1/raw_result.json) | PASS | Unsafe burn-in REJECTED, exit 1 | Arbitrary class, target, replay sequence, and finite `d` | Candidate VERIFIED; HIGH confidence |
| 2 | [Arbitrary thresholds](#/claim-2-current) | [proof](./repro/src/c2_proof.py), [checker](./repro/src/c2_checker.py) | Standard thresholds `1,n+1`; replay `T=max(d,m)` | [JSON](./.openresearch/artifacts/claim_2/raw_result.json) | PASS | No-replay trace REJECTED, exit 1 | Every generator and arbitrary finite `d,m` | Candidate VERIFIED; HIGH confidence |
| 3 | [Universal WP proof](#/claim-3-current) | [proof](./repro/src/c3_proof.py), [checker](./repro/src/c3_checker.py) | 18 obligations; 6 proof nodes; exclusion bound | [JSON](./.openresearch/artifacts/claim_3/raw_result.json) | PASS | Unprotected witnesses REJECTED, exit 1 | Every countable UUS class, target, replay enumeration | Candidate VERIFIED; MEDIUM confidence |
| 4 | [Infinite diagonalization](#/claim-4-current) | [proof](./repro/src/c4_proof.py), [checker](./repro/src/c4_checker.py) | All natural phases; 5 proof nodes | [JSON](./.openresearch/artifacts/claim_4/raw_result.json) | PASS | Missing marker replay REJECTED, exit 1 | Every generator and every phase `n` | Candidate VERIFIED; MEDIUM confidence |
| 5 | [Universal MQ lower bound](#/claim-5-current) | [proof](./repro/src/c5_proof.py), [checker](./repro/src/c5_checker.py) | Totality/UUS and both exhaustive cases | [JSON](./.openresearch/artifacts/claim_5/raw_result.json) | PASS | Missing final trap REJECTED, exit 1 | Every deterministic computable MQ-only proper generator | Candidate VERIFIED; MEDIUM confidence |
| 6 | [Exact integer certificate](#/claim-6-current) | [structural proof](./repro/src/c6_exact.py), [cell proof](./repro/src/c6_cell_solver.py), [two checkers](#/claim-6-current) | 4 first outputs; exact half-lines; 7 cells | [JSON](./.openresearch/artifacts/claim_6/raw_result.json) | Two PASS | Two mutations REJECTED, exit 1 | Every deterministic proper generator over exact four-member class on all `Z` | Candidate VERIFIED; HIGH confidence |

## Fixed environment and command

- Python 3.12.11, repository `uv.lock`, exactly one `.venv`, no third-party runtime dependency.
- Hugging Face `cpu-upgrade`; every scientific run reported 64 logical and affinity CPUs.
- Deterministic; no random seeds are used.
- Fixed command: `uv sync --frozen --no-dev && uv run --no-sync python repro/src/verify.py && uv run --no-sync python repro/src/publication_gate.py`

## Historical evidence

The prior finite checks remain reachable at [Historical rejected baseline](#/historical-rejected-baseline). They are not the current verifiers and are not used to justify candidate full-credit verdicts.
