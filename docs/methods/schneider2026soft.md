# `schneider2026soft`

**Source Status**: verified_from_source

**Source Pdf File**: schneider2026soft__soft_radial_projection_for_constrained_end_to_end_learning.pdf

**Method Family Primary**: smooth radial feasibility layer.

**Learning Task**: enforce hard constraints in end-to-end learning while preserving useful gradients.

**Model Paradigm**: differentiable soft-radial reparameterization.

**Constraint Form**: constraints whose feasible set supports the radial interior map described by the paper.

**Constraint Geometry**: feasible sets with a valid radial interior parameterization.

**Mechanism Label**: soft-radial projection.

**Mechanism Summary**: Soft-Radial Projection maps Euclidean predictions into the interior of the feasible set through a radial transformation, avoiding the rank-deficient Jacobians induced by boundary projections.

**Guarantee Target**: strict interior feasibility.

**Guarantee Basis**: by-construction radial interior map and full-rank-Jacobian analysis almost everywhere.

**Inference Dependency**: soft-radial layer evaluation.

**Main Tradeoff**: interior feasibility can trade off boundary reach, and applicability depends on a valid radial map.

**Evidence Note**: abstract and first pages checked.
