# `liang2023hp`

**Source Status**: verified_from_source

**Source Pdf File**: liang2023hp__hp_universal_approximators_for_constrained_neural_networks.pdf

**Method Family Primary**: projection-analogous correction / homeomorphic projection.

**Learning Task**: map unconstrained neural outputs into a constrained feasible region.

**Model Paradigm**: learned homeomorphic map plus projection in a simple latent set.

**Constraint Form**: constraints whose feasible set is homeomorphic to a unit ball.

**Constraint Geometry**: ball-homeomorphic feasible sets.

**Mechanism Label**: homeomorphic projection.

**Mechanism Summary**: The method learns a low-distortion homeomorphic mapping between the feasible set and the unit ball, then performs projection by bisection in the unit ball rather than solving a hard projection in the original space.

**Guarantee Target**: pointwise feasible output.

**Guarantee Basis**: mapping validity and latent bisection under the paper's assumptions.

**Inference Dependency**: learned map and bisection/projection step.

**Main Tradeoff**: effectiveness depends on learning a valid low-distortion homeomorphism.

**Evidence Note**: abstract and first pages checked.
