# Method

`repro/src/c6_exact.py` represents each support as an exact half-line plus one exceptional
integer. It normalizes the two relevant intersections symbolically to `x >= 0` or `x <= 0`,
constructs all four adversarial continuations, and emits a concrete outside-intersection witness
for every possible proper output. There is no integer truncation and no finite time horizon.

`repro/src/c6_independent.py` rechecks the emitted certificate without importing the producer.
The mutation control changes `h_2^+` to the exact common half-line; the main contradiction must
then disappear and the verifier must exit nonzero.

An independently written second route partitions every integer into seven exact predicate cells,
including two unbounded cells. Its truth-table checker shares no Claim 6 implementation with the
structural normalizer. Both routes were independently executed on Hugging Face `cpu-upgrade`.
