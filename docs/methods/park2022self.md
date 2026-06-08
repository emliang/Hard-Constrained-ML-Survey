# `park2022self`

**Source Status**: verified_from_source

**Source Pdf File**: park2022self__self_supervised_primal_dual_learning_for_constrained_optimization.pdf

**Method Family Primary**: primal-dual learning.

**Learning Task**: learn constrained optimization solutions without full supervised labels.

**Model Paradigm**: self-supervised primal-dual network/training.

**Constraint Form**: constrained optimization problems.

**Constraint Geometry**: problem-dependent.

**Mechanism Label**: self-supervised primal-dual learning.

**Mechanism Summary**: PDL jointly trains primal and dual networks to mimic augmented-Lagrangian trajectories; the dual network provides instance-specific multipliers used in the primal loss, improving the balance between optimality and constraint violations.

**Guarantee Target**: constrained optimization solution quality/feasibility.

**Guarantee Basis**: empirical feasibility and optimality-gap evaluation; no by-construction pointwise feasibility of the raw primal network is claimed.

**Inference Dependency**: feed-forward primal and dual networks, with training inspired by ALM updates.

**Main Tradeoff**: avoids presolved labels and uses instance-specific multipliers, but feasibility remains measured by violations unless paired with an additional repair/certificate.

**Evidence Note**: PDF text checked around abstract, related work, method, and conclusion.
