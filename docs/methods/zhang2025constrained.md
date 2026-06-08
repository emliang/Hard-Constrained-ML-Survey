# `zhang2025constrained`

**Source Status**: verified_from_source

**Source Pdf File**: zhang2025constrained__constrained_diffusers_for_safe_planning_and_control.pdf

**Method Family Primary**: constrained Langevin diffusion planning.

**Learning Task**: safe planning and control with pretrained diffusion models.

**Model Paradigm**: constrained Langevin sampling with projected, primal-dual, or augmented-Lagrangian updates.

**Constraint Form**: trajectory and safety constraints, including discrete control barrier functions.

**Constraint Geometry**: planning/control feasible trajectory sets.

**Mechanism Label**: Constrained Diffusers.

**Mechanism Summary**: Constrained Diffusers modifies the reverse diffusion process with constrained Langevin sampling algorithms that jointly optimize the trajectory and enforce constraints, and uses discrete control barrier functions in receding-horizon control.

**Guarantee Target**: constraint satisfaction and safety in planning/control samples.

**Guarantee Basis**: constrained Langevin iterations and CBF constraints; final strength depends on iteration/tolerance choices.

**Inference Dependency**: iterative constrained sampling during reverse diffusion.

**Main Tradeoff**: avoids retraining but adds iterative optimization cost at sampling time.

**Evidence Note**: abstract and first pages checked.
