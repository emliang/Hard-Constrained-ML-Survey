# `kim2026fastdips`

**Source Status**: verified_from_source

**Source Pdf File**: kim2026__fast_dips_adjoint_free_analytic_steps_and_hard_constrained_likelihood_correction_for_diffusi.pdf

**Method Family Primary**: diffusion-prior inverse-problem correction.

**Learning Task**: solve inverse problems with pretrained diffusion priors and hard measurement consistency.

**Model Paradigm**: adjoint-free ADMM-style feasibility correction inside diffusion-prior sampling.

**Constraint Form**: measurement-space residual constraints for inverse problems.

**Constraint Geometry**: l2 feasibility ball around measurements under a forward operator.

**Mechanism Label**: FAST-DIPS measurement correction.

**Mechanism Summary**: FAST-DIPS anchors each diffusion step at the denoiser prediction, enforces a hard measurement-space residual budget through an ADMM-style splitting with closed-form projection and analytic step sizes, then re-anneals for the next diffusion level.

**Guarantee Target**: measurement-space feasibility under the residual budget.

**Guarantee Basis**: hard residual projection plus local descent/backtracking analysis.

**Inference Dependency**: fixed-budget correction iterations using operator evaluations and autodiff primitives.

**Main Tradeoff**: efficient for inverse problems, but guarantees are local/per-step and tied to the measurement model and residual budget.

**Evidence Note**: abstract, introduction, and method overview checked; local filename differs from cite-key prefix.
