# `liu2025fast`

**Source Status**: verified_from_source

**Source Pdf File**: liu2025fast__fast_projection_free_approach_without_optimization_oracle_for_optimization_over_compact_convex_set.pdf

**Method Family Primary**: homeomorphic projection-free optimization.

**Learning Task**: optimize over compact convex sets without projection or linear-optimization oracles.

**Model Paradigm**: homeomorphism from constraint set to unit ball plus gradient-based optimization.

**Constraint Form**: compact convex sets, with some nonconvex extensions in the paper's stated scope.

**Constraint Geometry**: compact convex feasible sets homeomorphic to a unit ball.

**Mechanism Label**: Hom-PGD.

**Mechanism Summary**: Hom-PGD constructs a homeomorphism between the target constrained set and a unit ball, solves an equivalent ball-constrained problem by gradient methods, and maps iterates back while preserving feasibility.

**Guarantee Target**: iteration-wise feasibility and convergence to approximate stationary/optimal points under stated assumptions.

**Guarantee Basis**: homeomorphic transformation and convergence-rate analysis.

**Inference Dependency**: homeomorphism evaluation during optimization iterations.

**Main Tradeoff**: this is an optimization algorithm rather than a trained prediction layer; it needs a valid homeomorphism for the target set.

**Evidence Note**: abstract and first pages checked.
