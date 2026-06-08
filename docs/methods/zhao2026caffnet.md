# `zhao2026caffnet`

**Source Status**: verified_from_source

**Source Pdf File**: zhao2026caffnet__caffnet_hard_constraint_affine_neural_networks.pdf

**Method Family Primary**: closed-form affine enforcement layer.

**Learning Task**: embed hard constraint satisfaction into feedforward neural networks and transformers.

**Model Paradigm**: base network plus trainable constraint-affine layer.

**Constraint Form**: arbitrary-cardinality input-dependent affine inequality constraints.

**Constraint Geometry**: input-dependent affine feasible regions.

**Mechanism Label**: CAffNet / CAffine layer.

**Mechanism Summary**: CAffNet introduces a trainable constraint-affine layer that enforces input-dependent affine constraints without restricting the number of constraints to the HardNet-Aff cardinality setting.

**Guarantee Target**: hard satisfaction of the specified input-dependent affine constraints.

**Guarantee Basis**: closed-form construction and universal-approximation analysis under the paper's assumptions.

**Inference Dependency**: feed-forward affine enforcement layer.

**Main Tradeoff**: scope remains affine; the method extends HardNet-Aff cardinality/rank limitations rather than handling general nonlinear constraints.

**Evidence Note**: local original PDF abstract and comparison table checked.
