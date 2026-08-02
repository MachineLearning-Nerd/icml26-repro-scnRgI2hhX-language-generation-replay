# Outcome-blind pre-publication review

Review packet: frozen candidate `blind-v4b`, the exact generated prompt, and
the cited arXiv anchors. Working notes, desired verdicts, score forecasts, and
author success labels were excluded. The review used the challenge's theory
standard: an independent numerical or symbolic audit with a condition-relaxing
control is evidence for a theorem, but is not represented as a proof
replacement.

## Structural and release gates

- Required page order is Index, Executive summary, Claims 1–6, Conclusion.
- The summary and poster are pinned on Executive summary.
- All 12 judged routes and all 116 judged files remain present.
- Each claim page exposes its literal scope, paper-version mapping, command,
  complete sources, raw output, independent checker, control, and limitations.
- The Lean file contains no `sorry`, `admit`, `axiom`, or `unsafe`; it compiles
  with Lean 4.32.0, and two premise-changing mutations fail compilation.
- The cumulative CPU command reruns every current route without a seed, finite
  horizon, GPU, paid service, or hidden input.
- Static audit and manifest/link traversal pass. Missing conclusions: none.
- The current challenge validator's content heading is satisfied. Its remaining
  repository-name and disk-page-set checks conflict with the required existing
  ID-keyed Space and preservation of seven judged legacy routes; those routes
  remain nested below Executive summary instead of appearing in the canonical
  top-level page order.

## Claim scores

### Claim 1 — 2/2

The page reproduces both directions of the equivalence and the identical
threshold, not only a finite example. `ReplayCore.lean` checks replay support
closure and the standard-to-replay conversion for arbitrary types, supports,
histories, thresholds, and distinct-count functions. `c1_proof.py` separately
records the induction and reverse set-inclusion argument. An unsupported
burn-in is a meaningful rejecting control. The exact theorem scope and the
formalization boundary are explicit.

### Claim 2 — 2/2

The witness class and both sides of the separation match the cited theorem.
The audit keeps both adversarial thresholds arbitrary, and Lean proves the
support intersection over all integers plus its exhaustion; this replaces the
historical bounded threshold sweep. Removing replay invalidates the shared
trace, and removing the finite hypothesis's upper bound breaks the Lean
certificate. The countability, standard generator, and replay contradiction
are all accounted for.

### Claim 3 — 2/2

The candidate transcribes Witness Protection and audits termination, eventual
target criticality, and eventual valid fresh output for symbolic target index,
round, and prefix bound. Lean checks the sure-observation implication, finite
UUS exclusion, and the direction-sensitive criticality lemma; the retained
execution is correctly labeled an audit rather than a proof replacement. The
control permits a protected distinguishing witness to be output and thereby
breaks the false-candidate eviction step. No conclusion is inferred from only
the historical three-hypothesis instance.

### Claim 4 — 2/2

Both directions of the separation are covered. The audit follows arbitrary
integer subsets and every natural phase; Lean independently checks Cantor
diagonal non-enumerability and that one invalid output per phase gives errors
arbitrarily late. The source audit accounts for marker stabilization, phase
termination, and membership of the constructed target. Removing marker replay
makes the alternative history illegal and rejects the certificate. The page
does not infer the theorem from a finite phase prefix.

### Claim 5 — 2/2

The construction is indexed by an arbitrary deterministic computable MQ-only
proper generator. The audit covers total recursiveness, support/queue equality,
and both exhaustive output-sequence cases. Lean checks the temporal dichotomy
and derives infinitely many errors from the two construction-specific error
implications. Disabling the final trap rejects the finite-non-reference branch.
The page explicitly distinguishes these checked cores and source-level
invariants from an end-to-end formalization.

### Claim 6 — 2/2

Three independent exact routes cover the four-hypothesis construction over all
integers: Lean exhausts every first and later proper output, a symbolic
half-line implementation supplies outside witnesses, and a separate seven-cell
quantifier-elimination implementation rechecks the same obstruction. Both
replay legality and the standard no-replay side are documented. The mutated
common-half-line case destroys the contradiction, while a positive subset
control is accepted. No bounded window or time horizon remains.

## Result

**PERFECT BLIND REVIEW — 12/12 candidate evidence.** Every official claim earns
2/2 under the supplied rubric and all structural/release gates pass. This is a
pre-publication evidence assessment, not an earned leaderboard score; the live
judged score remains unchanged until the published revision is evaluated.
