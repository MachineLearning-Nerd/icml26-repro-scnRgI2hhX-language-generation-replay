# Method

The certificate reconstructs the WP proof as six checked nodes: sure-set decomposition, MQ computability, per-round termination, eventual criticality, eventual validity, and theorem composition. It retains symbolic target index `z`, time `t`, and prefix `m`.

Termination follows because the selected critical index is nonincreasing in `m` and stabilizes in the finite active set, while the excluded set has size at most `2t+t^2` and UUS makes the selected support prefix outgrow it. Eventual criticality follows from finitely many earlier candidates and protected witnesses that an enumeration must eventually present. Validity follows from critical inclusion; freshness follows because every seen point is sure or a prior output and WP avoids both.
