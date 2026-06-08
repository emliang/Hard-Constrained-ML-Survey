# `amos2017optnet`

**Source Status**: verified_from_source

**Source Pdf File**: amos2017optnet__optnet_differentiable_optimization_as_a_layer_in_neural_networks.pdf

**Method Family Primary**: differentiable optimization layer.

**Learning Task**: embed a constrained optimization solve inside a neural network.

**Model Paradigm**: quadratic-program layer with differentiable solver.

**Constraint Form**: QP constraints.

**Constraint Geometry**: convex quadratic program feasible region.

**Mechanism Label**: differentiable QP layer.

**Mechanism Summary**: OptNet places a QP solver as a network layer and differentiates through the solver using sensitivity/implicit differentiation, enabling constrained optimization problems to be learned end to end.

**Guarantee Target**: QP-layer feasibility and optimality up to solver tolerance.

**Guarantee Basis**: numerical optimization solve.

**Inference Dependency**: QP solve.

**Main Tradeoff**: strong constraint handling comes with solver cost and QP-form modeling limits.

**Evidence Note**: abstract and first pages checked.
