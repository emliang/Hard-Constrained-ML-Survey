# `yang2026efficient`

**Source Status**: verified_from_source

**Source Pdf File**: yang2026efficient__efficient_and_provably_convergent_end_to_end_training_of_deep_neural_networks_with_linear_constraints.pdf

**Method Family Primary**: linearly constrained projection-layer training.

**Learning Task**: train deep networks with selected layer outputs satisfying linear constraints.

**Model Paradigm**: projection layer with HS-Jacobian for nonsmooth automatic differentiation.

**Constraint Form**: linear constraints/polyhedral projection sets.

**Constraint Geometry**: polyhedral feasible regions.

**Mechanism Label**: HS-Jacobian projection training.

**Mechanism Summary**: The paper introduces an efficiently computable HS-Jacobian for projection layers onto polyhedral sets, proving it is a conservative mapping and enabling convergent end-to-end training with nonsmooth automatic differentiation.

**Guarantee Target**: linearly constrained layer outputs and convergence of the training algorithm.

**Guarantee Basis**: projection layer plus HS-Jacobian conservative-map analysis.

**Inference Dependency**: projection layer evaluation.

**Main Tradeoff**: targets linear/polyhedral constraints and focuses on efficient backpropagation through nonsmooth projections.

**Evidence Note**: abstract and first pages checked.
