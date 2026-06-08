# `liang2024hp`

**Source Status**: verified_from_source

**Source Pdf File**: liang2024hp__homeomorphic_projection_to_ensure_neural_networks_out_of_distribution_generalization.pdf

**Method Family Primary**: projection-analogous correction / homeomorphic projection.

**Learning Task**: enforce feasibility for neural predictions under distribution shift.

**Model Paradigm**: invertible neural network/homeomorphic projection.

**Constraint Form**: constrained sets satisfying the paper's homeomorphism assumptions.

**Constraint Geometry**: feasible set mapped to a unit ball.

**Mechanism Label**: INN-based homeomorphic projection.

**Mechanism Summary**: Homeomorphic Projection learns a bi-Lipschitz invertible neural map between the constraint set and a unit ball and projects in latent space via bisection, yielding feasible predictions with bounded optimality loss under stated conditions.

**Guarantee Target**: feasible prediction and bounded optimality loss.

**Guarantee Basis**: homeomorphism/bi-Lipschitz assumptions and bisection construction.

**Inference Dependency**: invertible map and latent bisection.

**Main Tradeoff**: requires a learned map that accurately represents the feasible set geometry.

**Evidence Note**: abstract and first pages checked.
