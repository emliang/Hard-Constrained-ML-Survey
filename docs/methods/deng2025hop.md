# `deng2025hop`

**Source Status**: verified_from_source

**Source Pdf File**: deng2025hop__hop_homeomorphic_polar_learning_for_hard_constrained_optimization.pdf

**Method Family Primary**: homeomorphic polar L2O.

**Learning Task**: learn solutions to hard-constrained star-convex optimization problems.

**Model Paradigm**: neural output in polar coordinates plus homeomorphic mapping.

**Constraint Form**: star-convex hard constraints.

**Constraint Geometry**: star-convex feasible regions with a valid interior/polar center.

**Mechanism Label**: HoP polar homeomorphism.

**Mechanism Summary**: HoP makes the neural network output bounded polar variables, then maps them through a homeomorphic polar transformation into Cartesian decision variables that remain inside the original star-convex feasible set.

**Guarantee Target**: strict feasibility for the modeled star-convex constraint set.

**Guarantee Basis**: polar homeomorphism and boundary-distance construction.

**Inference Dependency**: polar homeomorphic map and boundary-distance calculation.

**Main Tradeoff**: requires a valid polar center and boundary-distance routine; training can require reconnection strategies to avoid polar-coordinate stagnation.

**Evidence Note**: abstract, introduction, and method overview checked because first automatic extraction was incomplete.
