# `yang2026safeflowmatcher`

**Source Status**: verified_from_source

**Source Pdf File**: yang2026__safeflowmatcher_safe_and_fast_planning_using_flow_matching_with_control_barrier_functions.pdf

**Method Family Primary**: safe flow-matching planner.

**Learning Task**: generate safe real-time plans using flow matching.

**Model Paradigm**: two-phase prediction-correction integrator with CBF-QP correction.

**Constraint Form**: control barrier function safety constraints for planning.

**Constraint Geometry**: robust safe sets for executed paths.

**Mechanism Label**: SafeFlowMatcher CBF correction.

**Mechanism Summary**: SafeFlowMatcher first integrates the learned flow to produce a candidate path, then applies a correction phase using a vanishing time-scaled vector field and a CBF-based QP that minimally perturbs the vector field.

**Guarantee Target**: certified safety of the executed path and convergence to the safe set.

**Guarantee Basis**: barrier certificate proving forward invariance of a robust safe set and finite-time convergence.

**Inference Dependency**: CBF-QP correction after flow prediction.

**Main Tradeoff**: provides certification for executed paths but adds a correction QP and depends on valid CBF/safe-set modeling.

**Evidence Note**: abstract and first pages checked; local filename differs from cite-key prefix.
