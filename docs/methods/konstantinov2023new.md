# `konstantinov2023new`

**Source Status**: verified_from_source

**Source Pdf File**: konstantinov2023new__a_new_computationally_simple_approach_for_implementing_neural_networks_with_output_hard_constraints.pdf

**Method Family Primary**: hard-constrained output layer.

**Learning Task**: impose hard convex constraints on neural network outputs.

**Model Paradigm**: additional constraint layer mapping hidden parameters into a feasible set.

**Constraint Form**: convex constraints including linear, quadratic, equality, dynamic, and boundary-form constraints in the paper's stated scope.

**Constraint Geometry**: convex feasible sets.

**Mechanism Label**: computationally simple feasible mapping.

**Mechanism Summary**: The method adds a neural-network layer that maps hidden parameters to points guaranteed to lie inside the feasible set, with extensions to joint input-output constraints and projection-style variants.

**Guarantee Target**: output feasibility for modeled hard convex constraints.

**Guarantee Basis**: by-construction feasible mapping layer.

**Inference Dependency**: additional constraint layer evaluation.

**Main Tradeoff**: scope and computational complexity depend on the supported constraint types.

**Evidence Note**: abstract and first pages checked.
