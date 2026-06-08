# `heaton2022wasserstein`

**Source Status**: verified_from_source

**Source Pdf File**: heaton2022wasserstein__wasserstein_based_projections_with_applications_to_inverse_problems.pdf

**Method Family Primary**: learned projection for inverse problems.

**Learning Task**: approximate projection onto a data manifold for inverse-problem regularization.

**Model Paradigm**: Wasserstein-based projection operator.

**Constraint Form**: data-manifold constraint/regularization.

**Constraint Geometry**: manifold of true data, approximated from samples.

**Mechanism Label**: Wasserstein-based projection.

**Mechanism Summary**: The method learns a Wasserstein-based projection operator from samples of the true-data manifold, so the learned projection can be inserted into optimization methods similarly to plug-and-play denoisers but with theoretical approximation guarantees.

**Guarantee Target**: approximate projection onto the data manifold with high probability under stated assumptions.

**Guarantee Basis**: Wasserstein projection learning analysis.

**Inference Dependency**: learned projection inside an iterative inverse-problem method.

**Main Tradeoff**: guarantees are for approximating the data-manifold projection, not arbitrary task constraints.

**Evidence Note**: abstract and first pages checked.
