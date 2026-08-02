# Independent cell-decomposition route

The integer domain is partitioned at every predicate boundary: `(-inf,-3]`, `{-2}`, `{-1}`, `{0}`, `{1}`, `{2}`, `[3,inf)`. Each atom in the four hypothesis definitions is constant on every cell. Exhaustive Boolean evaluation across these complete cells therefore decides the required subset and intersection identities for all integers.

This implementation shares no Claim 6 code with the structural-normal-form sibling. It uses only the baseline's locked standard-library environment.

The route does not mechanize every definition from first principles. It checks the complete finite proper class and the exact adversarial set identities used by the source proof; the canonical page states that boundary.
