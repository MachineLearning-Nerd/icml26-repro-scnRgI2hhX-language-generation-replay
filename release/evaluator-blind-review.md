# Evaluator-blind pre-publication red team

The reviewer was given only the assembled candidate and the rubric. Repository knowledge, OpenResearch run descriptions, unpublished branches, and dashboard paths were excluded.

## Pass 1 — rejected

Files opened:

1. `README.md`
2. `logbook.json`
3. `pages/visibility-matrix/page.md`
4. `pages/claim-1-current/page.md`

Conclusion that could not be verified: the Claim 1 raw result and source code. The page’s `../../../../` links were authored relative to the repository source directory, but the static Space resolves them from its root document. The same defect affected all six current pages. The candidate was rejected and no score forecast was accepted from that traversal.

## Pass 2 — passed after link repair

The replacement links resolve from the static Space root. The audit began at `README.md` and `logbook.json`, opened the visibility matrix, then followed every current claim page to its contract, source audit, method, raw JSON, independent checker output, negative-control output, command, evaluator audit, limitations, verifier source, checker source, and lockfile. It also opened the report and four figures, notebook, historical wrapper, and preserved historical verifier.

The exact ordered list of every file opened is stored in `release/evaluator-blind-review.json`. Result: all six current verifiers were obvious; every raw result said `VERIFIED`; every independent checker said `PASS`; every control recorded nonzero exit and `REJECTED`; page run IDs, SHAs, six-decimal runtimes, seeds, CPU allocation, and fixed command matched raw evidence. Missing conclusions: none.

This review evaluates discoverability and internal consistency. It does not convert the candidate forecast into a live judge result.
