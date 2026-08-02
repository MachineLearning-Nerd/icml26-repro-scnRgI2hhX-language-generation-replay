# Evaluation contract

Fixed command:

`uv sync --frozen --no-dev && uv run --no-sync python repro/src/verify.py && uv run --no-sync python repro/src/publication_gate.py`

Environment: Python `3.12.*`, locked by `uv.lock`, one repository `.venv`. Compute estimate:
1 core, under 1 GiB RAM, under 2 minutes. Formal runs use Hugging Face `cpu-upgrade` only.

Release verdict is `VERIFIED` only if the exact structural certificate, independent checker,
and rejection control all behave as specified. The historical bounded-window result remains TOY.
