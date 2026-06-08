# `zampini2025trainingfree`

**Source Status**: verified_from_source

**Source Pdf File**: zampini2025trainingfree__training_free_constrained_generation_with_stable_diffusion_models.pdf

**Method Family Primary**: training-free latent-space constrained stable diffusion.

**Learning Task**: generate stable-diffusion outputs satisfying physical, functional, or safety constraints.

**Model Paradigm**: latent-space proximal/Lagrangian correction during stable diffusion sampling.

**Constraint Form**: arbitrary constraint sets in the paper's stated stable-diffusion framework, with convex-constraint guarantees discussed.

**Constraint Geometry**: image-space constraints imposed through decoded latent representations.

**Mechanism Label**: latent proximal correction.

**Mechanism Summary**: The method enforces constraints on stable diffusion samples by backpropagating image-space constraint violations through the frozen decoder and applying proximal/Lagrangian corrections directly to the latent during sampling.

**Guarantee Target**: constraint satisfaction of final decoded samples, with formal guarantees for convex constraints in the paper.

**Guarantee Basis**: proximal Langevin correction and projection/surrogate constraint evaluation.

**Inference Dependency**: iterative latent correction during sampling; surrogate or simulator if constraints are not directly differentiable.

**Main Tradeoff**: training-free and compatible with stable diffusion, but correction quality depends on decoder gradients and constraint/surrogate fidelity.

**Evidence Note**: abstract, introduction, and method overview checked because automatic extraction was incomplete.
