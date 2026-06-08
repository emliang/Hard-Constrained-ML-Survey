# `min2024hardnet`

**Source Status**: verified_from_source

**Source Pdf File**: min2024hardnet__hardnet_hard_constrained_neural_networks_with_universal_approximation_guarantees.pdf

**Method Family Primary**: closed-form hard constraint enforcement layer for the HardNet-Aff setting.

**Learning Task**: construct neural networks that satisfy hard input-output constraints without losing model capacity.

**Model Paradigm**: base network plus differentiable closed-form enforcement layer.

**Constraint Form**: multiple input-dependent affine constraints, including linear inequalities with input-dependent bounds; the paper's broader HardNet-Cvx discussion is optimization-based rather than the closed-form HardNet-Aff layer.

**Constraint Geometry**: input-dependent feasible output regions.

**Mechanism Label**: HardNet-Aff enforcement layer.

**Mechanism Summary**: HardNet-Aff appends a differentiable closed-form layer to the neural output, enabling standard end-to-end training while enforcing multiple input-dependent affine/linear inequalities and retaining universal approximation guarantees.

**Guarantee Target**: hard satisfaction of the specified input-dependent constraints.

**Guarantee Basis**: closed-form HardNet-Aff enforcement layer and universal-approximation analysis.

**Inference Dependency**: feed-forward enforcement layer.

**Main Tradeoff**: closed-form guarantees apply to the affine/linear HardNet-Aff scope; broader convex constraints require the paper's optimization-based HardNet-Cvx construction.

**Evidence Note**: abstract and first pages checked.
