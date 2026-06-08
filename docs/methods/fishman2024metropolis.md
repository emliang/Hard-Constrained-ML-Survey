# `fishman2024metropolis`

**Source Status**: verified_from_source

**Source Pdf File**: fishman2024metropolis__metropolis_sampling_for_constrained_diffusion_models.pdf

**Method Family Primary**: Metropolis constrained diffusion sampler.

**Learning Task**: sample diffusion models under arbitrary domain-informed constraints.

**Model Paradigm**: Metropolis noising scheme for constrained diffusion.

**Constraint Form**: convex and nonconvex constraints in the paper's experiments.

**Constraint Geometry**: constrained subsets beyond simple Euclidean convex cases.

**Mechanism Label**: Metropolis constrained sampling.

**Mechanism Summary**: The paper replaces costly reflected or barrier noising processes with a Metropolis-based noising scheme and proves it is a valid discretization of reflected Brownian motion.

**Guarantee Target**: constrained-domain sampling under the Metropolis process.

**Guarantee Basis**: valid discretization of reflected Brownian motion and accept-reject sampling.

**Inference Dependency**: Metropolis-style constrained sampler.

**Main Tradeoff**: efficiency and sample quality depend on proposal behavior, acceptance, and mixing.

**Evidence Note**: abstract and first pages checked.
