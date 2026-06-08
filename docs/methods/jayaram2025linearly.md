# `jayaram2025linearly`

**Source Status**: verified_from_source

**Source Pdf File**: jayaram2025linearly__linearly_constrained_diffusion_implicit_models.pdf

**Method Family Primary**: linearly constrained DDIM.

**Learning Task**: solve noisy linear inverse problems with pretrained diffusion models.

**Model Paradigm**: constrained diffusion implicit model.

**Constraint Form**: linear output constraints or residual-distribution constraints for noisy inverse problems.

**Constraint Geometry**: affine/linear constraint sets.

**Mechanism Label**: CDIM constrained update.

**Mechanism Summary**: CDIM modifies DDIM updates so the final output satisfies linear inverse-problem constraints exactly in noiseless settings, and enforces an exact constraint on the residual distribution in noisy settings.

**Guarantee Target**: exact linear constraint satisfaction for noiseless inverse problems; residual-distribution constraint in noisy cases.

**Guarantee Basis**: constrained DDIM update construction.

**Inference Dependency**: CDIM sampling updates.

**Main Tradeoff**: scope is linear inverse constraints; broader validity depends on reducing the problem to this structure.

**Evidence Note**: abstract and first pages checked.
