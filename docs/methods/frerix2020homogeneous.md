# `frerix2020homogeneous`

**Source Status**: verified_from_source

**Source Pdf File**: frerix2020homogeneous__homogeneous_linear_inequality_constraints_for_neural_network_activations.pdf

**Method Family Primary**: constrained activation parameterization.

**Learning Task**: train neural networks whose activations satisfy linear inequalities.

**Model Paradigm**: parameterized feasible activation set.

**Constraint Form**: homogeneous linear inequalities `Ax <= 0`.

**Constraint Geometry**: polyhedral cone.

**Mechanism Label**: activation-space parameterization.

**Mechanism Summary**: The method computes a parameterization of the feasible activation set at initialization so the network satisfies homogeneous linear inequality activation constraints throughout training.

**Guarantee Target**: activation-level constraint satisfaction.

**Guarantee Basis**: by-construction feasible parameterization.

**Inference Dependency**: none beyond the constrained network layer.

**Main Tradeoff**: limited to the homogeneous linear inequality setting in this first pass.

**Evidence Note**: abstract and first pages checked.
