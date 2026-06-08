# `nguyen2025fsnet`

**Source Status**: verified_from_source

**Source Pdf File**: nguyen2025fsnet__fsnet_feasibility_seeking_neural_network_for_constrained_optimization_with_guarantees.pdf

**Method Family Primary**: feasibility-seeking neural solver.

**Learning Task**: solve parametric constrained optimization with feasible neural predictions.

**Model Paradigm**: neural prediction followed by differentiable feasibility-seeking optimization.

**Constraint Form**: equality and inequality constraints, including convex and nonconvex cases covered experimentally.

**Constraint Geometry**: problem-dependent feasible sets.

**Mechanism Label**: feasibility-seeking step.

**Mechanism Summary**: FSNet uses a neural prediction as a starting point, then solves an unconstrained constraint-violation minimization problem through an iterative differentiable feasibility-seeking step, training the full procedure end to end.

**Guarantee Target**: convergence to feasible points and feasible outputs under stated assumptions.

**Guarantee Basis**: feasibility-seeking optimization and stated boundedness/smoothness/PL-condition analysis.

**Inference Dependency**: iterative feasibility-seeking solve after neural prediction.

**Main Tradeoff**: general feasibility handling requires unrolled iterative correction at training and inference.

**Evidence Note**: abstract and first pages checked.
