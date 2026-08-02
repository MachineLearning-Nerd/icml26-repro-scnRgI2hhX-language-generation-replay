# Campaign command inventory

This records the reproducibility-relevant commands. Secrets and generated backend wrappers are intentionally excluded.

## Startup and source audit

```bash
orx skill
orx skill orx-experiment-tree
orx skill orx-evidence
orx skill orx-git
orx skill orx-compute
orx projects --json
orx runs f1234a68-857f-46e2-b1f0-2c77995610a0
git rev-parse HEAD
git status --short
git branch -a
df -h .
env | sed 's/=.*//' | sort
curl -L -A 'Mozilla/5.0 OpenResearch-Reproduction/1.0' https://export.arxiv.org/e-print/2603.11784
curl -L -A 'Mozilla/5.0 OpenResearch-Reproduction/1.0' https://ar5iv.labs.arxiv.org/html/2603.11784
sha256sum <downloaded-paper-source>
```

The exact judged Space revision and reference Space were downloaded read-only with Git/LFS disabled for modification. The verdict JSON was fetched and filtered by exact `space_id == "DineshAI/scnRgI2hhX"`. No token value was displayed.

## Fixed experiment contract

```bash
orx project edit f1234a68-857f-46e2-b1f0-2c77995610a0 --run-command 'uv sync --frozen --no-dev && uv run --no-sync python repro/src/verify.py && uv run --no-sync python repro/src/publication_gate.py'
```

Every successful node was submitted with the same launch shape:

```bash
orx exp run <experiment-id> --flavor cpu-upgrade --timeout 20m --image ghcr.io/astral-sh/uv:0.8.11-python3.12-bookworm-slim
orx exp wait <experiment-id> --timeout 480
orx logs <run-id>
```

The launch was applied to baseline `fceea689-00b2-4eaa-a20b-bcf38a7c28a6`, Claim-6 routes `3411167e-80ef-4358-8374-46c3c1682668` and `e3e8a331-5eb9-46cb-bb6a-d8e66ddc22b8`, cumulative Claim 6 `a7570893-27ea-4121-951a-c657dfc0725a`, then Claims 1–5 `bfe05a3c-4054-41ea-9764-617efac0fa56`, `6ca17002-8d7f-42c6-8c3f-bc23a93ef788`, `bad82a73-bba7-402a-a1b6-0c0dea30f142`, `986b6ebb-9301-4659-a6ce-ab2af20a9d15`, and `11d08e74-cc13-47af-b288-22d2963b0040`. The candidate node is `b7cdf31c-08f5-4350-a68c-fd9ba58f881a`.

## Presentation validation

```bash
marimo check --fix notebooks/replay_reproduction.py
marimo check --strict notebooks/replay_reproduction.py
python3 -m py_compile repro/src/*.py notebooks/replay_reproduction.py
xmllint --noout reports/replay-reproduction/images/*.svg
jq empty .trackio/logbook/logbook.json
git diff --check
```

Scientific verifiers were never executed locally. All claim checks, controls, raw-data generation, and cumulative regression ran through `orx exp run` on Hugging Face `cpu-upgrade`.
