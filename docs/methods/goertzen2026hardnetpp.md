# `goertzen2026hardnetpp`

**Source Status**: verified_from_source

**Source Pdf File**: goertzen2026hardnetpp__hardnetpp_nonlinear_constraint_enforcement_in_neural_networks.pdf

**Method Family Primary**: unrolled local-linearization feasibility layer.

**Learning Task**: map unconstrained neural outputs to outputs satisfying nonlinear constraints.

**Model Paradigm**: base network plus differentiable iterative constraint-satisfaction layer.

**Constraint Form**: nonlinear equality and inequality constraints with lower/upper bounds \\(b_l(x)\\le c_x(y)\\le b_u(x)\\).

**Constraint Geometry**: input-dependent nonlinear feasible sets under regularity assumptions.

**Mechanism Label**: HardNet++.

**Mechanism Summary**: HardNet++ iteratively adjusts the raw network output using damped projections onto local linearizations of nonlinear equality and inequality constraints.

**Guarantee Target**: arbitrarily small constraint violations under the paper's regularity and convergence assumptions.

**Guarantee Basis**: convergence analysis for the iterative local-linearization procedure.

**Inference Dependency**: finite or converged iterative correction layer.

**Main Tradeoff**: handles broader nonlinear constraints than closed-form affine layers, but feasibility is convergence/tolerance-dependent and iteration cost must be reported.

**Evidence Note**: local original PDF abstract, introduction, and problem formulation checked.
