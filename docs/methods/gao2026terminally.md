# `gao2026terminally`

**Source Status**: verified_from_source

**Source Pdf File**: gao2026terminally__terminally_constrained_flow_based_generative_models_from_an_optimal_control_perspective.pdf

**Method Family Primary**: terminally constrained flow guidance.

**Learning Task**: sample from terminally constrained distributions using pretrained flow-based models.

**Model Paradigm**: optimal-control guidance in a co-moving frame.

**Constraint Form**: terminal constraints/manifold constraints.

**Constraint Geometry**: terminal constraint manifolds with Riemannian-gradient guidance.

**Mechanism Label**: TOCFlow terminal optimal control.

**Mechanism Summary**: TOCFlow formulates terminally constrained sampling as an optimal-control problem, derives a feedback control from an HJB perspective, and implements a geometry-aware sampling-time guidance method with a closed-form scalar damping factor.

**Guarantee Target**: terminal-constraint convergence/projection behavior under the control formulation.

**Guarantee Basis**: optimal-control analysis; as penalty vanishes, the terminal law approaches a generalized Wasserstein projection onto the constraint manifold.

**Inference Dependency**: sampling-time control/guidance computation.

**Main Tradeoff**: adds optimal-control guidance cost and relies on terminal constraint geometry.

**Evidence Note**: abstract and first pages checked.
