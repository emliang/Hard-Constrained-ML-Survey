# `cardei2025constrained`

**Source Status**: verified_from_source

**Source Pdf File**: cardei2025constrained__constrained_discrete_diffusion.pdf

**Method Family Primary**: constrained discrete diffusion.

**Learning Task**: generate discrete sequences satisfying logic, safety, or task constraints.

**Model Paradigm**: discrete diffusion with differentiable constraint optimization during sampling.

**Constraint Form**: sequence-level constraints and logic rules over discrete outputs.

**Constraint Geometry**: categorical/discrete state space with constraint optimizer.

**Mechanism Label**: CDD constrained discrete sampling.

**Mechanism Summary**: Constrained Discrete Diffusion embeds differentiable constraint optimization directly into the discrete diffusion sampling process, avoiding post-hoc filtering or retraining.

**Guarantee Target**: constraint-satisfying generated sequences in the studied tasks.

**Guarantee Basis**: sampling-time differentiable constraint optimization.

**Inference Dependency**: constrained discrete diffusion correction during sampling.

**Main Tradeoff**: training-free constraint insertion adds sampling-time optimization and depends on the constraint optimizer.

**Evidence Note**: abstract and first pages checked.
