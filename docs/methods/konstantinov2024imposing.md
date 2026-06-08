# `konstantinov2024imposing`

**Source Status**: verified_from_source

**Source Pdf File**: konstantinov2024imposing__imposing_star_shaped_hard_constraints_on_the_neural_network_output.pdf

**Method Family Primary**: star-shaped feasible mapping.

**Learning Task**: impose nonconvex star-shaped output constraints.

**Model Paradigm**: ray-based output layer with differentiable ray marching.

**Constraint Form**: star-shaped hard constraints.

**Constraint Geometry**: star-shaped regions with an origin from which each point is visible.

**Mechanism Label**: star-shaped ray marching.

**Mechanism Summary**: The method parameterizes a ray from an origin inside the star-shaped region, computes the largest admissible shift using a differentiable ray-marching algorithm, and returns points guaranteed to satisfy the constraints.

**Guarantee Target**: output feasibility for the modeled star-shaped constraint region.

**Guarantee Basis**: ray visibility and differentiable boundary-search construction.

**Inference Dependency**: ray-marching boundary computation.

**Main Tradeoff**: requires a valid star-shaped origin and boundary/ray-intersection routine.

**Evidence Note**: abstract and first pages checked.
