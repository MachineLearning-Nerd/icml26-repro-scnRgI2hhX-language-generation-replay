# Method

`repro/src/c6_exact.py` represents each support as an exact half-line plus one exceptional
integer. It normalizes the two relevant intersections symbolically to `x >= 0` or `x <= 0`,
constructs all four adversarial continuations, and emits a concrete outside-intersection witness
for every possible proper output. There is no integer truncation and no finite time horizon.

`repro/src/c6_independent.py` rechecks the emitted certificate without importing the producer.
The mutation control changes `h_2^+` to the exact common half-line; the main contradiction must
then disappear and the verifier must exit nonzero.
