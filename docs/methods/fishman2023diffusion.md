# `fishman2023diffusion`

**Source Status**: verified_from_source

**Source Pdf File**: fishman2023diffusion__diffusion_models_for_constrained_domains.pdf

**Method Family Primary**: constrained diffusion model.

**Learning Task**: generate samples on constrained domains.

**Model Paradigm**: diffusion with constrained-domain noising processes.

**Constraint Form**: inequality-constrained domains.

**Constraint Geometry**: constrained domains handled through barrier or reflection geometry.

**Mechanism Label**: barrier/reflected diffusion.

**Mechanism Summary**: The paper develops diffusion models whose noising processes respect constrained domains, including a logarithmic-barrier-metric construction and a reflected Brownian-motion construction.

**Guarantee Target**: sampling support inside the constrained domain.

**Guarantee Basis**: stochastic process design; numerical discretization and score-model approximation remain practical considerations.

**Inference Dependency**: reverse diffusion sampler.

**Main Tradeoff**: domain-aware diffusion is more specialized than unconstrained Euclidean diffusion.

**Evidence Note**: abstract and first pages checked.
