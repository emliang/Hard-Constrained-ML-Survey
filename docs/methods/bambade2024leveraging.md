# `bambade2024leveraging`

**Source Status**: verified_from_source

**Source Pdf File**: bambade2024__leveraging_augmented_lagrangian_techniques_for_differentiating_over_infeasible_quadratic_pro.pdf

**Method Family Primary**: differentiable QP layer.

**Learning Task**: train models containing QP layers even when QPs become infeasible during training.

**Model Paradigm**: augmented-Lagrangian differentiation for feasible and infeasible convex QPs.

**Constraint Form**: convex quadratic programs with linear constraints.

**Constraint Geometry**: convex QP feasible regions; closest feasible QP solution for infeasible cases.

**Mechanism Label**: infeasible-QP differentiation.

**Mechanism Summary**: The paper extends QP-layer differentiation to infeasible QPs by differentiating closest feasible QP solutions in an l2 sense, enabling training-time infeasibility while encouraging test-time feasible layers.

**Guarantee Target**: differentiability and feasibility-driven training of QP layers.

**Guarantee Basis**: augmented-Lagrangian/KKT-based construction and closest-feasible-solution formulation.

**Inference Dependency**: QP/QPLayer solve.

**Main Tradeoff**: improves trainability of QP layers but still relies on specialized QP solves.

**Evidence Note**: abstract and first pages checked; local filename differs from cite key prefix.
