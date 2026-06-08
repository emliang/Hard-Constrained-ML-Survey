# `chen2021enforcing`

**Source Status**: verified_from_source

**Source Pdf File**: chen2021enforcing__enforcing_policy_feasibility_constraints_through_differentiable_projection_for_energy_optimization.pdf

**Method Family Primary**: differentiable projection policy layer.

**Learning Task**: train RL policies for energy systems while enforcing operational constraints.

**Model Paradigm**: neural policy followed by differentiable convex projection.

**Constraint Form**: convex approximations of energy-system operational constraints.

**Constraint Geometry**: convex feasible action sets.

**Mechanism Label**: PROF differentiable projection.

**Mechanism Summary**: PROF appends a differentiable projection onto a convexified operational constraint set to a neural policy, enforcing feasible actions in the forward pass and backpropagating through the projection during policy learning.

**Guarantee Target**: action feasibility with respect to the specified convex constraint set.

**Guarantee Basis**: projection onto the modeled convex set.

**Inference Dependency**: convex projection solve/layer.

**Main Tradeoff**: feasibility is with respect to approximate convex constraints, so model fidelity matters.

**Evidence Note**: abstract and first pages checked.
