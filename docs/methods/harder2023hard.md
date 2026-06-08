# `harder2023hard`

**Source Status**: verified_from_source

**Source Pdf File**: harder2023hard__hard_constrained_deep_learning_for_climate_downscaling.pdf

**Method Family Primary**: hard-constrained prediction for physical super-resolution.

**Learning Task**: climate/weather downscaling and super-resolution while preserving conservation-style statistics.

**Model Paradigm**: neural downscaler with terminal constraint layer.

**Constraint Form**: statistical/physical consistency constraints between low-resolution inputs and high-resolution outputs.

**Constraint Geometry**: application-specific conservation constraints.

**Mechanism Label**: renormalizing constraint layer.

**Mechanism Summary**: The paper adds a constraint layer at the end of neural downscaling architectures, using additive, multiplicative, or softmax-adapted renormalization to guarantee specified conservation constraints.

**Guarantee Target**: satisfaction of stated physical consistency constraints.

**Guarantee Basis**: by-construction terminal renormalization layer.

**Inference Dependency**: constraint layer evaluation after the base neural model.

**Main Tradeoff**: applies when the input-output relationship admits known aggregate/statistical constraints.

**Evidence Note**: abstract and first pages checked.
