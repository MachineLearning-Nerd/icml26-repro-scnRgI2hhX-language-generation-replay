# Primary-source audit

- TeX source: `https://export.arxiv.org/e-print/2603.11784`, retrieved with an explicit browser User-Agent on 2026-08-02; SHA-256 `1014bb49b0b75137488266a641fa179fcd2885c6ea4217501c9e7683758cb1c4`.
- HTML cross-check: `https://ar5iv.labs.arxiv.org/html/2603.11784`, retrieved 2026-08-02; SHA-256 `b3220f5cfa110088b01df476f2fdd366fbe6e5088507be9a1f15cfe1c9ebba2b`.
- No unreleased code, data, model weights, proprietary API, stochastic sampling, or GPU is required. The six judged claims are theorem/construction claims.

## Exact source anchors and quantifiers

| Judge claim | arXiv v2 anchor | Domain and exact quantifier audited |
| --- | --- | --- |
| 1 | `sections/04-uniform-with-replay.tex`, `thm:uniform_with_replay`, Algorithm `alg:uniform_to_uniform_replay` | Every binary class, target, replay sequence, and finite standard complexity `d`; equality of optimal complexities. |
| 2 | `sections/05-nonuniform-with-replay.tex`, separation theorem | Constructed countable class over all integers; every replay generator and arbitrary finite target thresholds `d,m`. |
| 3 | `sections/06-limit-with-replay.tex`, Witness Protection theorem and Algorithm 2 | Every countable uniformly unbounded-support class, target index, replay enumeration, and round. |
| 4 | `sections/06-limit-with-replay.tex`, uncountable separation theorem and lemmas | Constructed uncountable class; every deterministic generator and every natural adversarial phase. |
| 5 | `sections/07-proper-generation.tex`, MQ lower-bound theorem and Algorithm 3 | Every deterministic computable membership-query-only proper generator. |
| 6 | `sections/07-proper-generation.tex`, finite replay-hardness theorem | Every deterministic proper generator on the exact four-member class over all integers. |

The judge-facing numbering refers to an earlier version: Claims 1–6 are Theorems 3.1, 4.1, 5.1, 5.6, 6.1, and 6.3 there; the corresponding arXiv v2 numbers are 4.1, 5.1, 6.1, 6.6, 7.1, and 7.3. Each per-claim `source_audit.md` records its exact labels, assumptions, and proof dependencies.
