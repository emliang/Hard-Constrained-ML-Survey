# `constante2025enforcing`

**Source Status**: verified_from_source

**Source Pdf File**: constante2025enforcing__enforcing_hard_linear_constraints_in_deep_learning_models_with_decision_rules.pdf

**Method Family Primary**: decision-rule hard linear constraint architecture.

**Learning Task**: enforce input-dependent linear equality and inequality constraints on neural outputs.

**Model Paradigm**: task network plus safe network based on optimization decision rules.

**Constraint Form**: input-dependent linear equalities and inequalities.

**Constraint Geometry**: linear/polyhedral feasible sets.

**Mechanism Label**: safe-network decision rules.

**Mechanism Summary**: The architecture combines a prediction-oriented task network with a safe network trained using stochastic/robust optimization decision rules, and outputs a convex combination that guarantees linear constraint satisfaction without runtime optimization.

**Guarantee Target**: hard satisfaction of input-dependent linear constraints.

**Guarantee Basis**: decision-rule feasible safe network and convex-combination construction.

**Inference Dependency**: feed-forward evaluation only.

**Main Tradeoff**: guarantee is tied to tractable decision-rule formulations for the specified linear constraints.

**Evidence Note**: abstract and first pages checked.
