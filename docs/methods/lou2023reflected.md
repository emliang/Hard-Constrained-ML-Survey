# `lou2023reflected`

**Source Status**: verified_from_source

**Source Pdf File**: lou2023reflected__reflected_diffusion_models.pdf

**Method Family Primary**: constrained diffusion model.

**Learning Task**: generate samples under domain constraints.

**Model Paradigm**: reflected diffusion.

**Constraint Form**: constrained support.

**Constraint Geometry**: reflected-domain geometry.

**Mechanism Label**: reflection-based diffusion.

**Mechanism Summary**: The source positions reflected diffusion as a way to keep the diffusion process compatible with constrained support rather than relying on ad hoc clipping or thresholding.

**Guarantee Target**: constrained-support sampling.

**Guarantee Basis**: reflection mechanism; exact assumptions need method-section check.

**Inference Dependency**: reflected reverse diffusion sampler.

**Main Tradeoff**: implementation and guarantees depend on the supported domain/reflection construction.

**Evidence Note**: first-page extraction was partial; requires a full abstract/method pass before final wording.
