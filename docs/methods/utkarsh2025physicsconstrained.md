# `utkarsh2025physicsconstrained`

**Source Status**: verified_from_source

**Source Pdf File**: utkarsh2025physicsconstrained__physics_constrained_flow_matching_sampling_generative_models_with_hard_constraints.pdf

**Method Family Primary**: physics-constrained flow matching.

**Learning Task**: enforce nonlinear physical constraints in pretrained flow-based generative models.

**Model Paradigm**: zero-shot flow-matching sampler with physics-based corrections.

**Constraint Form**: arbitrary nonlinear physical constraints in the paper's stated scope.

**Constraint Geometry**: PDE/physics-informed feasible solution sets.

**Mechanism Label**: PCFM physics correction.

**Mechanism Summary**: PCFM guides flow-matching sampling through physics-based corrections to intermediate states, keeping the trajectory aligned with the learned flow and satisfying physical constraints at the final solution.

**Guarantee Target**: exact constraint satisfaction at the final generated solution in the studied PDE settings.

**Guarantee Basis**: physics-based correction step applied during sampling.

**Inference Dependency**: correction during flow-matching sampling.

**Main Tradeoff**: zero-shot and flexible, but correction cost and exactness depend on the physical constraint evaluator.

**Evidence Note**: abstract and first pages checked.
