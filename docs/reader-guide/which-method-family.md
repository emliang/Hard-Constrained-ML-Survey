
# Which Method Family?

Use this page as a first-pass decision guide. It does not rank methods; it narrows the families worth reading.

## If the feasible set has a simple structure

Consider:

- feasibility-preserving activations,
- completion layers,
- explicit feasibility maps,
- constraint parameterizations.

Check:

- whether the parameterization covers the whole feasible set,
- whether the map is valid for all inputs,
- whether the method remains low-latency at inference.

## If a solver or projection is acceptable at inference

Consider:

- post-processing,
- projection or repair,
- differentiable optimization layers,
- unrolled solvers.

Check:

- solver tolerance,
- failure cases,
- number of iterations,
- differentiability assumptions,
- total inference latency.

## If the constraint is input-dependent

Consider:

- input-dependent completion,
- learned feasible-set maps,
- interior-point or boundary-based recovery,
- reflected or constrained samplers,
- guided generation with validity checks.

Check:

- how the feasible set is represented for each input,
- whether membership, projection, or boundary oracles are available,
- whether map validity is local or global.

## If the constraint is discrete, symbolic, or grammar-like

Consider:

- constrained decoding,
- grammar or automaton constraints,
- neuro-symbolic layers,
- verifier/editor methods,
- mixed-integer or combinatorial solver hybrids.

Check:

- whether decoding is complete or heuristic,
- whether relaxation changes the problem,
- whether validity is guaranteed or only encouraged.

## If strict certification is required

Consider:

- verification,
- certified repair,
- model editing,
- robust or worst-case guarantee methods.

Check:

- certified domain,
- relaxation tightness,
- scalability,
- conservativeness,
- whether the certificate covers the deployment regime.
