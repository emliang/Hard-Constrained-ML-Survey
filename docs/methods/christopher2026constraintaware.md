# `christopher2026constraintaware`

**Source Status**: verified_from_source

**Source Pdf File**: christopher2026constraintaware__constraint_aware_flow_matching_decision_aligned_end_to_end_training_for_constrained_sampling.pdf

**Method Family Primary**: constraint-aware flow-matching training.

**Learning Task**: improve constrained sampling quality by aligning training with projection-based constrained inference.

**Model Paradigm**: flow matching with constraint projections in the training objective.

**Constraint Form**: constraints handled by projection-based constrained sampling.

**Constraint Geometry**: projection-accessible feasible sets.

**Mechanism Label**: Constraint-Aware Flow Matching.

**Mechanism Summary**: The method explicitly incorporates constraint projections into the flow-matching training objective so the learned dynamics better match the constrained sampling procedure and reduce projection-induced distribution shift.

**Guarantee Target**: higher-quality constrained samples when paired with the constrained sampling/projection procedure.

**Guarantee Basis**: training-sampling alignment plus projection-based inference; pointwise feasibility comes from the projection procedure, not the loss alone.

**Inference Dependency**: constrained sampler/projection at generation time.

**Main Tradeoff**: improves alignment but requires training with the intended projection mechanism.

**Evidence Note**: abstract and first pages checked.
