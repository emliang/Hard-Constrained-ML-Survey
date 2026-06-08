# `liu2023learning`

**Source Status**: verified_from_source

**Source Pdf File**: liu2023learning__learning_diffusion_bridges_on_constrained_domains.pdf

**Method Family Primary**: constrained-domain diffusion bridge.

**Learning Task**: learn diffusion models on mixed constrained and structured domains.

**Model Paradigm**: diffusion bridge with singular Doob h-transform force and neural force field.

**Constraint Form**: bounded, unbounded, continuous, discrete, categorical, ordinal, and product-domain constraints in the paper's stated scope.

**Constraint Geometry**: constrained product domains.

**Mechanism Label**: constrained diffusion bridge.

**Mechanism Summary**: The model drives diffusion with a singular force from Doob's h-transform that ensures outcomes belong to the desired domain, plus a trainable nonsingular neural force field that matches the data distribution.

**Guarantee Target**: generated outcomes remain in the desired constrained domain.

**Guarantee Basis**: bridge construction with domain-enforcing singular force.

**Inference Dependency**: constrained diffusion bridge sampler.

**Main Tradeoff**: broad domain support depends on constructing the appropriate bridge forces for the target domain.

**Evidence Note**: abstract and first pages checked.
