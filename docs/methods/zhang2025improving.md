# `zhang2025improving`

**Source Status**: verified_from_source

**Source Pdf File**: zhang2025improving__improving_diffusion_based_inverse_algorithms_under_few_step_constraint_via_linear_extrapolation.pdf

**Method Family Primary**: few-step inverse diffusion acceleration.

**Learning Task**: improve diffusion-based inverse algorithms when using few denoising steps.

**Model Paradigm**: learnable linear extrapolation over inverse-trajectory estimates.

**Constraint Form**: inverse-problem observation constraints handled by the underlying diffusion inverse algorithm.

**Constraint Geometry**: algorithm-dependent inverse-problem constraint set.

**Mechanism Label**: LLE inverse-algorithm extrapolation.

**Mechanism Summary**: LLE identifies a linear-combination structure in diffusion inverse trajectories and learns extrapolation coefficients to refine predictions from prior estimates across a broad class of inverse algorithms.

**Guarantee Target**: improved few-step inverse-problem performance.

**Guarantee Basis**: extrapolation over the base algorithm's approximation structure; not a separate hard feasibility mechanism.

**Inference Dependency**: LLE extrapolation on top of an existing inverse sampler.

**Main Tradeoff**: improves efficiency/performance but inherits feasibility behavior from the underlying inverse algorithm.

**Evidence Note**: abstract and first pages checked.
