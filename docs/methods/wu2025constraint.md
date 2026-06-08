# `wu2025constraint`

**Source Status**: verified_from_source

**Source Pdf File**: wu2025constraint__constraint_boundary_wandering_framework_enhancing_constrained_optimization_with_deep_neural_networks.pdf

**Method Family Primary**: correction/boundary-search framework.

**Learning Task**: improve neural solutions for equality/inequality constrained optimization.

**Model Paradigm**: DC3-style neural solver with active-set-inspired boundary wandering.

**Constraint Form**: smooth equality and inequality constraints.

**Constraint Geometry**: problem-dependent constrained feasible regions.

**Mechanism Label**: constraint boundary wandering.

**Mechanism Summary**: CBWF modifies DC3 with an improved correction module and a second-stage Boundary Wandering Step that explores near inequality-constraint boundaries to reduce objective value while improving constraint handling.

**Guarantee Target**: lower objective and reduced constraint loss for constrained optimization predictions.

**Guarantee Basis**: correction plus active-set-inspired boundary wandering; paper states convergence/theoretical guarantees for BWS.

**Inference Dependency**: trained network plus correction/boundary-wandering procedure.

**Main Tradeoff**: additional correction/search steps improve feasibility-objective balance but add inference complexity.

**Evidence Note**: abstract and first pages checked.
