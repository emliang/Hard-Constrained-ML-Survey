# `tang2026lminet`

**Source Status**: verified_from_source

**Source Pdf File**: tang2026lminet__lmi_net_linear_matrix_inequality_constrained_neural_networks_via_differentiable_projection_layers.pdf

**Method Family Primary**: differentiable projection layer for LMI constraints.

**Learning Task**: learn parameter-to-solution maps for repeated LMI-constrained problems.

**Model Paradigm**: neural predictor plus Douglas--Rachford projection layer.

**Constraint Form**: parameterized linear matrix inequalities \\(F_0(\\xi)+\\sum_i y_i F_i(\\xi)\\succeq 0\\).

**Constraint Geometry**: lifted intersection of an affine equality constraint and the positive semidefinite cone.

**Mechanism Label**: LMI-Net.

**Mechanism Summary**: LMI-Net lifts LMI feasibility into affine-equality and PSD-cone projections, uses Douglas--Rachford splitting in the forward pass, and supports implicit differentiation.

**Guarantee Target**: LMI feasibility to the convergence/tolerance of the splitting projection layer.

**Guarantee Basis**: Douglas--Rachford convergence under the stated assumptions.

**Inference Dependency**: iterative splitting projection layer.

**Main Tradeoff**: expands feasibility layers to semidefinite/LMI constraints but introduces splitting iterations and tolerance-dependent feasibility.

**Evidence Note**: local original PDF abstract, introduction, and problem formulation checked.
