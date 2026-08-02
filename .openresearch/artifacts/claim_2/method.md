# Method

The certificate first supplies a direct standard-setting generator: emit a fresh positive until a negative input appears, then fresh negatives. It succeeds for `h_infinity` at threshold 1 and for `h_n` at threshold `n+1`, because `h_n` contains only `n` positive points.

For replay hardness, assume arbitrary finite thresholds `d` and `m`. Present `1,...,d`, then replay each output. Correctness for `h_infinity` forces fresh naturals, so by `T=max(d,m)` the same legal trace triggers `h_d`. Simultaneous correctness requires a fresh point in `N intersect supp(h_d)={1,...,d}`, but every such point was in the initial prefix. This is an exact symbolic contradiction for arbitrary thresholds.
