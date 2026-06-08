# `sambharya2024learning`

**Source Status**: verified_from_source

**Source Pdf File**: sambharya2024learning__learning_to_warm_start_fixed_point_optimization_algorithms.pdf

**Method Family Primary**: learned warm start for iterative solvers.

**Learning Task**: map problem parameters to warm starts for fixed-point algorithms.

**Model Paradigm**: neural warm-start model plus fixed-point iterations.

**Constraint Form**: optimization constraints handled by the target fixed-point method.

**Constraint Geometry**: solver-dependent.

**Mechanism Label**: fixed-point residual warm start.

**Mechanism Summary**: The neural model predicts warm starts that are evaluated by fixed-point residual or ground-truth distance losses, and the paper analyzes generalization for classes of fixed-point operators.

**Guarantee Target**: faster convergence or better initial residual.

**Guarantee Basis**: fixed-point algorithm properties and PAC-Bayes-style generalization analysis; not a direct feasibility layer by itself.

**Inference Dependency**: fixed-point iterations.

**Main Tradeoff**: feasibility and optimality depend on the downstream iterative method.

**Evidence Note**: abstract and first pages checked.
