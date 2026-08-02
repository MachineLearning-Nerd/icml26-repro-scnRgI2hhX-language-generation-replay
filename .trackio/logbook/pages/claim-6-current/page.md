# Claim 6 — current exact verification

## Exact claim and verdict

**VERIFIED (candidate, not yet a live judge result).** Theorem 6.3 (arXiv v2 Theorem 7.3)
states that there is a finite class that no deterministic proper generator can generate in the
limit with replay. The quantified domain is all integers.

## What supersedes the historical verifier

`repro/src/c6_exact.py` supersedes the bounded `[-40,40]` check. It represents the four supports
as exact half-lines plus exceptions, exhausts all four first outputs, and proves the relevant
intersection is exactly `Z_{>=0}` or `Z_{<=0}`. `repro/src/c6_independent.py` independently
checks the emitted certificate. The exact revision and HF run are inserted after execution.

## Expected exact evidence

| First output | Legal replays | Simultaneous targets | Exact intersection | Proper outputs available |
|---|---:|---|---|---:|
| `h1-` | `-1,-2` | `h1+,h2+` | `Z_{>=0}` | 0 |
| `h2-` | `-1,-2` | `h1+,h2+` | `Z_{>=0}` | 0 |
| `h1+` | `1,2` | `h1-,h2-` | `Z_{<=0}` | 0 |
| `h2+` | `1,2` | `h1-,h2-` | `Z_{<=0}` | 0 |

The negative control changes one hypothesis to the common half-line. The contradiction then
disappears and the verifier exits nonzero. Raw output, checker output, CPU allocation, runtime,
and Git SHA will be mirrored here from the HF `cpu-upgrade` run before release.

## Scope

This page makes no claim about a new judge score. It addresses the prior judge's sole Claim-6
criticism: the current verifier uses exact predicates over every integer and no bounded window.
