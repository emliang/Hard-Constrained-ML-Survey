# `karalias2025geometric`

**Source Status**: verified_from_source

**Source Pdf File**: karalias2025geometric__geometric_algorithms_for_neural_combinatorial_optimization_with_constraints.pdf

**Method Family Primary**: geometric constrained combinatorial optimization.

**Learning Task**: train neural solvers for discrete constrained optimization in a self-supervised way.

**Model Paradigm**: convex-geometric decomposition using feasible polytope corners.

**Constraint Form**: discrete/combinatorial constraints such as cardinality and matroid-style feasible sets in examples.

**Constraint Geometry**: convex hulls of feasible discrete solutions.

**Mechanism Label**: Caratheodory-style feasible decomposition.

**Mechanism Summary**: The framework decomposes neural outputs into convex combinations of polytope corners corresponding to feasible discrete solutions, enabling differentiable self-supervised training and quality-preserving rounding to feasible solutions.

**Guarantee Target**: feasible rounded combinatorial solutions.

**Guarantee Basis**: convex-geometric decomposition over feasible polytope corners.

**Inference Dependency**: decomposition and rounding procedure.

**Main Tradeoff**: requires access to geometric/decomposition routines for the target combinatorial constraint family.

**Evidence Note**: abstract and first pages checked.
