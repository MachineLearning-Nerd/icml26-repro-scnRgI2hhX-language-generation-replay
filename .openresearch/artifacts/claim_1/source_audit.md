# Claim 1 source audit

- Source: `https://export.arxiv.org/e-print/2603.11784`
- Retrieved with an explicit browser User-Agent on 2026-08-02.
- Source archive SHA-256: `1014bb49b0b75137488266a641fa179fcd2885c6ea4217501c9e7683758cb1c4`.
- Statement/proof: `sections/04-uniform-with-replay.tex`, `thm:uniform_with_replay` and Algorithm `alg:uniform_to_uniform_replay`.
- Definitions: `sections/03-setup-results.tex`, `def:replay-seq`, `def:unif-gen-replay`; standard definition in `appendix/A-overview-generation.tex`.

The exact universal claim concerns arbitrary finite sample complexity `d`, every target, and every replay sequence. The conversion emits `x1` until `d` distinct inputs exist, then calls the original generator on the full prefix.
