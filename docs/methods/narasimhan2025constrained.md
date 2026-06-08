# `narasimhan2025constrained`

**Source Status**: verified_from_source

**Source Pdf File**: narasimhan2025constrained__constrained_posterior_sampling_time_series_generation_with_hard_constraints.pdf

**Method Family Primary**: constrained posterior sampling.

**Learning Task**: generate time-series samples satisfying hard domain constraints.

**Model Paradigm**: diffusion posterior sampling with repeated projection of the posterior mean.

**Constraint Form**: time-series hard constraints, including many simultaneous constraints in experiments.

**Constraint Geometry**: terminal or noisy-state constraint sets with a projection operation.

**Mechanism Label**: CPS posterior-mean projection.

**Mechanism Summary**: CPS projects the posterior mean estimate into the constraint set after each denoising update, requiring no additional training while scaling to many constraints.

**Guarantee Target**: constrained generated time-series samples after projected denoising.

**Guarantee Basis**: projection step applied during posterior sampling; tolerance and projection quality matter.

**Inference Dependency**: projection after denoising updates.

**Main Tradeoff**: repeated projection improves feasibility but adds sampling-time correction cost.

**Evidence Note**: abstract and first pages checked.
