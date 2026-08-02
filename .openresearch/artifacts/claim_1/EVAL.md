# Evaluation contract

Fixed command: `uv sync --frozen --no-dev && uv run --no-sync python repro/src/verify.py && uv run --no-sync python repro/src/publication_gate.py`

Estimated compute: 1 core, under 1 GiB RAM, under 2 minutes. Formal execution is Hugging Face `cpu-upgrade`. Accept only if the proof DAG and independent checker pass and changing the burn-in output from `x1` to an arbitrary outsider exits nonzero.
