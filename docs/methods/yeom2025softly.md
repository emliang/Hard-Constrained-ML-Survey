# `yeom2025softly`

**Source Status**: verified_from_source

**Source Pdf File**: yeom2025softly__softly_constrained_denoisers_for_diffusion_models.pdf

**Method Family Primary**: softly constrained diffusion denoiser.

**Learning Task**: improve PDE compliance of diffusion priors while remaining robust to PDE misspecification.

**Model Paradigm**: denoiser architecture with soft PDE-derived inductive biases.

**Constraint Form**: PDE residual/physics constraints used as soft inductive bias.

**Constraint Geometry**: PDE solution manifold approximated by denoiser bias.

**Mechanism Label**: softly constrained denoiser.

**Mechanism Summary**: The method incorporates PDE-derived soft inductive biases into the denoiser architecture so diffusion models can improve physical compliance while retaining flexibility when the PDE is misspecified.

**Guarantee Target**: improved compliance, not hard pointwise constraint satisfaction.

**Guarantee Basis**: architecture-level soft inductive bias.

**Inference Dependency**: modified denoiser evaluation.

**Main Tradeoff**: deliberately avoids strict hard constraints to tolerate model misspecification.

**Evidence Note**: abstract and first pages checked.
