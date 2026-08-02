# Claim 6 source audit

- Source: `https://export.arxiv.org/e-print/2603.11784`
- Retrieved with an explicit browser User-Agent on 2026-08-02.
- Source archive SHA-256: `1014bb49b0b75137488266a641fa179fcd2885c6ea4217501c9e7683758cb1c4`.
- Anchor: `sections/07-proper.tex`, `thm:hardness-proper-replay` (arXiv v2 Theorem 7.3; judge numbering Theorem 6.3).
- Definition anchor: `sections/03-setup-results.tex`, `def:proper-limit-replay`.

The theorem quantifies over every deterministic proper generator. Its witness class is exactly
`{h_1^-, h_2^-, h_1^+, h_2^+}` over all integers, with supports
`Z_{<=0} union {i}` and `Z_{>=0} union {-i}` for `i in {1,2}`. A bounded integer window is not
the stated domain and is rejected by the claim contract.
