# `tabas2022computationally`

**Source Status**: verified_from_source

**Source Pdf File**: tabas2022computationally__computationally_efficient_safe_reinforcement_learning_for_power_systems.pdf

**Method Family Primary**: gauge-map safe-action parameterization.

**Learning Task**: learn safe RL policies for power-system frequency regulation.

**Model Paradigm**: neural policy that predicts a virtual action in a simple reference domain and maps it to a safe-action set through a gauge map.

**Constraint Form**: state and action safety constraints for linear system models with bounded disturbances.

**Constraint Geometry**: polytopic robust controlled-invariant set and safe-action set.

**Mechanism Label**: gauge map from virtual action to safe action.

**Mechanism Summary**: The method computes a robust controlled-invariant polytope, lets the neural policy output a virtual action in the infinity-norm unit ball, and uses a differentiable gauge map to send that coordinate into the state-dependent safe-action set without solving MPC or projection problems at runtime.

**Guarantee Target**: safety-critical state/action constraint satisfaction during policy execution.

**Guarantee Basis**: set-theoretic control, RCI polytope construction, and valid gauge-map parameterization of the safe-action set.

**Inference Dependency**: closed-form gauge-map evaluation.

**Main Tradeoff**: safety guarantee depends on the computed RCI, linear model assumptions, disturbance set, and validity of the gauge map for the safe-action set.

**Evidence Note**: abstract and first pages checked; method summary verified by separately reading the introduction because automatic abstract extraction was incomplete.
