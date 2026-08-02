# Limitations and deviations

This is a machine-checked reconstruction of the paper's finite-class contradiction, not a proof
assistant kernel. Its trusted base consists of the exact half-line normalizer, integer membership
predicates, and the logical rule that one deterministic output history subject to two eventual
properness guarantees must eventually be a subset of both targets. Unlike the historical check,
it does not approximate infinite supports by a window.
