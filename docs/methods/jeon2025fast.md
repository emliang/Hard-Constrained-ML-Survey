# `jeon2025fast`

**Source Status**: verified_from_source

**Source Pdf File**: jeon2025fast__fast_non_log_concave_sampling_under_nonconvex_equality_and_inequality_constraints_with_landing.pdf

**Method Family Primary**: landing-based constrained Langevin sampler.

**Learning Task**: sample non-log-concave distributions under nonconvex equality and inequality constraints.

**Model Paradigm**: overdamped Langevin with landing.

**Constraint Form**: nonlinear equality and inequality constraints.

**Constraint Geometry**: nonconvex feasible sets satisfying the paper's regularity conditions.

**Mechanism Label**: OLLA constrained Langevin.

**Mechanism Summary**: OLLA modifies Langevin dynamics with a deterministic landing correction along constraint-normal directions, avoiding explicit projections while accommodating equality and inequality constraints.

**Guarantee Target**: convergence to the constrained target density.

**Guarantee Basis**: exponential convergence in 2-Wasserstein distance under stated regularity assumptions.

**Inference Dependency**: landing-based Langevin sampler.

**Main Tradeoff**: rigorous guarantees require the paper's regularity assumptions and sampler discretization choices.

**Evidence Note**: abstract and first pages checked.
