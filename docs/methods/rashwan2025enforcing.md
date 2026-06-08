# `rashwan2025enforcing`

**Source Status**: verified_from_source

**Source Pdf File**: rashwan2025enforcing__enforcing_convex_constraints_in_graph_neural_networks.pdf

**Method Family Primary**: graph-output convex projection.

**Learning Task**: enforce input-dependent constraints for graph neural network outputs.

**Model Paradigm**: GNN plus sparse clipping and Component-Averaged Dykstra projection.

**Constraint Form**: convex constraints over variable-size graph outputs.

**Constraint Geometry**: convex feasible sets for graph-structured outputs.

**Mechanism Label**: ProjNet CAD projection.

**Mechanism Summary**: ProjNet combines sparse vector clipping with the Component-Averaged Dykstra algorithm to project GNN outputs onto input-dependent convex constraints, using a GPU implementation and a surrogate gradient for end-to-end training.

**Guarantee Target**: convex-constraint satisfaction for projected graph outputs.

**Guarantee Basis**: CAD best-approximation convergence for the modeled convex sets.

**Inference Dependency**: iterative CAD projection.

**Main Tradeoff**: exact projection gradients are replaced by a surrogate gradient for training efficiency.

**Evidence Note**: abstract and first pages checked.
