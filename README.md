# Language Generation with Replay

Clean-room, source-faithful reproduction for ICML 2026 paper `scnRgI2hhX`,
*Language Generation with Replay: A Learning-Theoretic View of Model Collapse*
(arXiv `2603.11784`).

All six anchored claims pass an executable construction audit on CPU. Run:

```bash
python3 repro/src/verify.py
```

The result is written to [`outputs/verdict.json`](outputs/verdict.json).
Each claim has a separate source anchor, independently transcribed mechanism,
and a negative control. This is a theory-paper reproduction: finite executions
check the exact constructions and their invariants, while the universal
quantifiers remain grounded in the linked primary-source proofs. See
[`RESULTS.md`](RESULTS.md) for the claim-by-claim evidence.
