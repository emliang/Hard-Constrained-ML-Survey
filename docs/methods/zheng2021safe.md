# `zheng2021safe`

**Source Status**: verified_from_source

**Source Pdf File**: zheng2021safe__safe_reinforcement_learning_of_control_affine_systems_with_vertex_networks.pdf

**Method Family Primary**: vertex-coordinate safe policy.

**Learning Task**: learn safe RL policies for control-affine systems with hard state and action constraints.

**Model Paradigm**: vertex network predicting convex-combination weights.

**Constraint Form**: action constraints derived from next-step safety in convex polytopes.

**Constraint Geometry**: convex polytopes represented by vertices.

**Mechanism Label**: Vertex Network.

**Mechanism Summary**: Vertex Networks exploit the fact that any point in a convex polytope can be written as a convex combination of its vertices; the policy network predicts the combination weights and outputs an action from precomputed safe vertices.

**Guarantee Target**: next-step safety during exploration and execution.

**Guarantee Basis**: convex-combination representation of the safe action polytope.

**Inference Dependency**: vertex-weight prediction and convex combination.

**Main Tradeoff**: requires tractable vertex representation of the relevant safe set.

**Evidence Note**: abstract and first pages checked.
