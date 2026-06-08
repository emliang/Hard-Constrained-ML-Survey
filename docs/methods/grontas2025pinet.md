# `grontas2025pinet`

**Source Status**: verified_from_source

**Source Pdf File**: grontas2025pinet__pinet_optimizing_hard_constrained_neural_networks_with_orthogonal_projection_layers.pdf

**Method Family Primary**: orthogonal projection layer.

**Learning Task**: train feasible-by-design proxies for parametric constrained optimization.

**Model Paradigm**: neural output layer with operator-splitting projection and implicit differentiation.

**Constraint Form**: convex constraints.

**Constraint Geometry**: convex feasible regions.

**Mechanism Label**: PiNet orthogonal projection.

**Mechanism Summary**: PiNet appends an output projection layer that uses operator splitting for fast convex projections in the forward pass and implicit differentiation for backpropagation.

**Guarantee Target**: satisfaction of convex constraints by projected outputs.

**Guarantee Basis**: orthogonal projection onto the convex feasible set.

**Inference Dependency**: operator-splitting projection solve.

**Main Tradeoff**: feasible outputs require a projection solve; accuracy and speed depend on projection convergence.

**Evidence Note**: abstract and first pages checked.
