# `christopher2024constrained`

**Source Status**: verified_from_source

**Source Pdf File**: christopher2024constrained__constrained_synthesis_with_projected_diffusion_models.pdf

**Method Family Primary**: constrained guided generation.

**Learning Task**: synthesize samples satisfying specified constraints.

**Model Paradigm**: projected diffusion.

**Constraint Form**: convex and nonconvex constraints in the paper's experiments.

**Constraint Geometry**: constrained regions specified at generation time.

**Mechanism Label**: projected diffusion sampling.

**Mechanism Summary**: Projected Diffusion casts sampling as a constrained optimization process, steering diffusion outputs toward specified feasible regions and enabling constraint satisfaction/certification in the studied settings.

**Guarantee Target**: constraint satisfaction of generated samples.

**Guarantee Basis**: projection/constrained optimization during sampling.

**Inference Dependency**: projection or constrained solve during sampling.

**Main Tradeoff**: stronger constraint handling adds optimization cost and depends on solver quality.

**Evidence Note**: abstract and first pages checked.
