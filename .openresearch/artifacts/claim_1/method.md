# Method

`c1_proof.py` emits a proof DAG for the black-box reduction. The central node is a strong-induction invariant: before the threshold every replayable output is `x1`, which is in the target; after the threshold, the standard generator receives only a target-support prefix and emits a supported fresh point, preserving the invariant. Thus the converted generator needs at most `d` distinct examples.

The reverse implication is the set inclusion from standard sequences to replay sequences. Applying both directions to the optimal complexities yields `d_standard <= d_replay` and `d_replay <= d_standard`, hence equality. No finite support, horizon, or formula-selected sweep appears in this route.
