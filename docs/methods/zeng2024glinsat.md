# `zeng2024glinsat`

**Source Status**: verified_from_source

**Source Pdf File**: zeng2024glinsat__glinsat_the_general_linear_satisfiability_neural_network_layer_by_accelerated_gradient_descent.pdf

**Method Family Primary**: general linear satisfiability layer.

**Learning Task**: project batches of neural outputs onto bounded and general linear constraints.

**Model Paradigm**: entropy-regularized LP reformulation solved by accelerated gradient descent.

**Constraint Form**: bounded and general linear constraints.

**Constraint Geometry**: polyhedral feasible regions with bounds.

**Mechanism Label**: GLinSAT accelerated linear satisfiability.

**Mechanism Summary**: GLinSAT reformulates output projection as an entropy-regularized LP, dualizes it into an unconstrained smooth convex problem, and solves it with accelerated gradient descent in a differentiable, matrix-factorization-free layer.

**Guarantee Target**: satisfaction of general linear constraints up to solver tolerance.

**Guarantee Basis**: convex dual reformulation and accelerated gradient convergence.

**Inference Dependency**: accelerated gradient iterations.

**Main Tradeoff**: general linear support is obtained through iterative optimization rather than a closed-form map.

**Evidence Note**: abstract and first pages checked.
