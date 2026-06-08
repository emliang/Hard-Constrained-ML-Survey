# `graikos2025fast`

**Source Status**: verified_from_source

**Source Pdf File**: graikos2025fast__fast_constrained_sampling_in_pre_trained_diffusion_models.pdf

**Method Family Primary**: fast training-free constrained diffusion sampling.

**Learning Task**: generate samples under new constraints with pretrained diffusion models.

**Model Paradigm**: approximate Newton-style correction without denoiser backpropagation.

**Constraint Form**: arbitrary constraints in the paper's inference framework, including linear and nonlinear examples.

**Constraint Geometry**: constraint sets accessible through correction objectives.

**Mechanism Label**: fast constrained sampling.

**Mechanism Summary**: The method uses an approximation to Newton's method to enforce constraints during diffusion inference while avoiding costly backpropagation through the denoiser network.

**Guarantee Target**: improved constraint satisfaction in training-free constrained sampling.

**Guarantee Basis**: optimization-style correction; first-pass evidence does not support an exact hard feasibility claim for all constraints.

**Inference Dependency**: sampling-time correction iterations.

**Main Tradeoff**: faster than denoiser-backprop approaches, but correction accuracy and constraint satisfaction remain task-dependent.

**Evidence Note**: abstract and first pages checked.
