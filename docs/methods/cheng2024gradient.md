# `cheng2024gradient`

**Source Status**: verified_from_source

**Source Pdf File**: cheng2024gradient__gradient_free_generation_for_hard_constrained_systems.pdf

**Method Family Primary**: gradient-free constrained flow-matching sampling.

**Learning Task**: adapt pretrained flow-matching models to hard-constrained scientific systems.

**Model Paradigm**: extrapolation-correction-interpolation sampling.

**Constraint Form**: hard constraints in systems where gradients are sparse or expensive, including PDE examples.

**Constraint Geometry**: constraint sets handled through correction without expensive gradient computation.

**Mechanism Label**: ECI sampling.

**Mechanism Summary**: ECI sampling alternates extrapolation, correction, and interpolation during flow-matching sampling so pretrained unconstrained models can satisfy constraints in a zero-shot, gradient-free manner.

**Guarantee Target**: hard-constraint adherence in the paper's constrained-generation settings.

**Guarantee Basis**: correction step in the ECI sampling loop.

**Inference Dependency**: ECI correction during each iterative sampling step.

**Main Tradeoff**: avoids gradients/fine-tuning but adds correction stages and depends on the available constraint-correction routine.

**Evidence Note**: abstract and first pages checked.
