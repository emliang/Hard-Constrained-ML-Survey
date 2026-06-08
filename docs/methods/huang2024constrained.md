# `huang2024constrained`

**Source Status**: verified_from_source

**Source Pdf File**: huang2024__constrained_diffusion_with_trust_sampling.pdf

**Method Family Primary**: trust-region constrained diffusion guidance.

**Learning Task**: training-free constrained generation with diffusion models.

**Model Paradigm**: loss-guided diffusion with trust sampling and manifold-deviation checks.

**Constraint Form**: proxy-constraint functions used during diffusion inference.

**Constraint Geometry**: diffusion state manifold plus constraint proxy landscape.

**Mechanism Label**: trust sampling.

**Mechanism Summary**: Trust sampling formulates constrained optimization subproblems at each diffusion step, takes multiple gradient steps on a proxy constraint only while the proxy remains trustworthy, and terminates early when the sample appears to leave the diffusion state manifold.

**Guarantee Target**: improved constraint adherence during guided generation.

**Guarantee Basis**: trust-region/proxy-guidance heuristic; first-pass source does not support a hard pointwise guarantee.

**Inference Dependency**: multiple proxy-gradient steps and manifold trust checks during sampling.

**Main Tradeoff**: flexible and training-free, but guidance strength and trust criteria affect sample quality and feasibility.

**Evidence Note**: abstract and first pages checked; local filename differs from cite-key prefix.
