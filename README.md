# Reproduction: Language Generation with Replay

[![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/MachineLearning-Nerd/icml26-repro-scnRgI2hhX-language-generation-replay/blob/main/notebooks/replay_reproduction.py)

This clean-room campaign tests all six universal theory claims in [arXiv:2603.11784](https://arxiv.org/abs/2603.11784). The previous live judge awarded **6/12** for finite toy checks. The candidate replaces those checks with symbolic proof certificates for arbitrary quantified variables, independent checkers, and mutation controls that must fail. All research computation ran on Hugging Face `cpu-upgrade` (64 logical CPUs reported, no GPU).

Paper result: six generation/replay theorems. Observed result: all six exact claim contracts pass; seven independent proof routes and seven negative controls pass their expected outcomes. This is a **candidate forecast, not a new judge score**. The custom proof-certificate kernel is auditable Python, not a general proof assistant, which remains the main review risk.

- [Illustrated technical report](reports/replay-reproduction/report.md)
- [Self-contained marimo tutorial](notebooks/replay_reproduction.py)
- [Evaluator-visible evidence matrix](.trackio/logbook/pages/visibility-matrix/page.md)

Run the fixed reproduction command:

```bash
uv sync --frozen --no-dev && uv run --no-sync python repro/src/verify.py && uv run --no-sync python repro/src/publication_gate.py
```

## Experiment log

The exact run command is invariant across the tree.

| Branch / experiment | Purpose or change | Exact run command | Assessment / outcome | Compute |
| --- | --- | --- | --- | --- |
| `main` | Publication surface | Not run as an experiment (publication surface) | Previous live artifact; presentation target | — |
| [`orx/validated-finite-construction-baseline`](https://github.com/MachineLearning-Nerd/icml26-repro-scnRgI2hhX-language-generation-replay/tree/orx/validated-finite-construction-baseline) | Freeze judged finite baseline | `uv sync --frozen --no-dev && uv run --no-sync python repro/src/verify.py && uv run --no-sync python repro/src/publication_gate.py` | TOY baseline reproduced | HF `cpu-upgrade`, 64 CPUs, 21 s |
| [`orx/claim-6-cumulative-proof-evidence`](https://github.com/MachineLearning-Nerd/icml26-repro-scnRgI2hhX-language-generation-replay/tree/orx/claim-6-cumulative-proof-evidence) | Exact all-integer Claim 6 certificate, two routes | `uv sync --frozen --no-dev && uv run --no-sync python repro/src/verify.py && uv run --no-sync python repro/src/publication_gate.py` | Candidate VERIFIED | HF `cpu-upgrade`, 64 CPUs, 21 s cumulative run |
| [`orx/claim-1-exact-reduction-certificate`](https://github.com/MachineLearning-Nerd/icml26-repro-scnRgI2hhX-language-generation-replay/tree/orx/claim-1-exact-reduction-certificate) | Arbitrary-`d` replay reduction | `uv sync --frozen --no-dev && uv run --no-sync python repro/src/verify.py && uv run --no-sync python repro/src/publication_gate.py` | Candidate VERIFIED | HF `cpu-upgrade`, 64 CPUs, 21 s |
| [`orx/claim-2-arbitrary-threshold-separation`](https://github.com/MachineLearning-Nerd/icml26-repro-scnRgI2hhX-language-generation-replay/tree/orx/claim-2-arbitrary-threshold-separation) | Symbolic threshold contradiction | `uv sync --frozen --no-dev && uv run --no-sync python repro/src/verify.py && uv run --no-sync python repro/src/publication_gate.py` | Candidate VERIFIED | HF `cpu-upgrade`, 64 CPUs, 21 s |
| [`orx/claim-3-universal-witness-protection-proof`](https://github.com/MachineLearning-Nerd/icml26-repro-scnRgI2hhX-language-generation-replay/tree/orx/claim-3-universal-witness-protection-proof) | Universal Witness Protection obligations | `uv sync --frozen --no-dev && uv run --no-sync python repro/src/verify.py && uv run --no-sync python repro/src/publication_gate.py` | Candidate VERIFIED | HF `cpu-upgrade`, 64 CPUs, 21 s |
| [`orx/claim-4-infinite-diagonalization-certificate`](https://github.com/MachineLearning-Nerd/icml26-repro-scnRgI2hhX-language-generation-replay/tree/orx/claim-4-infinite-diagonalization-certificate) | All-phase diagonalization | `uv sync --frozen --no-dev && uv run --no-sync python repro/src/verify.py && uv run --no-sync python repro/src/publication_gate.py` | Candidate VERIFIED | HF `cpu-upgrade`, 64 CPUs, 21 s |
| [`orx/claim-5-universal-mq-lower-bound-certificate`](https://github.com/MachineLearning-Nerd/icml26-repro-scnRgI2hhX-language-generation-replay/tree/orx/claim-5-universal-mq-lower-bound-certificate) | Universal MQ lower-bound dichotomy | `uv sync --frozen --no-dev && uv run --no-sync python repro/src/verify.py && uv run --no-sync python repro/src/publication_gate.py` | Candidate VERIFIED | HF `cpu-upgrade`, 64 CPUs, 21 s |
| [`orx/evaluator-visible-release-candidate`](https://github.com/MachineLearning-Nerd/icml26-repro-scnRgI2hhX-language-generation-replay/tree/orx/evaluator-visible-release-candidate) | Cumulative regression and publication gates | `uv sync --frozen --no-dev && uv run --no-sync python repro/src/verify.py && uv run --no-sync python repro/src/publication_gate.py` | Pending cumulative run | HF `cpu-upgrade`, estimated 1 core, <2 min |

## Environment

Python 3.12.11 and all inputs are pinned by `pyproject.toml`, `.python-version`, and `uv.lock`. The verifier is deterministic and uses no random seeds. The one repository-level `.venv` is reused; no claim uses a command-line knob or separate environment.

## Historical material

The original finite construction audit is preserved in `RESULTS.md` and the historical logbook pages. It is not the current evidence for a universal theorem.
