# `cao2026scpo`

**Source Status**: verified_from_source

**Source Pdf File**: cao2026scpo__constrained_policy_optimization_via_sampling_based_weight_space_projection.pdf

**Method Family Primary**: safe-update training for policy networks.

**Learning Task**: constrained policy learning with rollout-based safety constraints.

**Model Paradigm**: safe backup policy plus neural residual policy, updated through projected weight-space steps.

**Constraint Form**: rollout-evaluated safety metrics and local smoothness-based safe regions in parameter space.

**Constraint Geometry**: local convex QCQP inner approximation of a safe weight-space region.

**Mechanism Label**: SCPO weight-space projection.

**Mechanism Summary**: SCPO samples local weight perturbations, estimates how safety metrics change, constructs a local safe region, and projects each raw gradient update through a convex QCQP.

**Guarantee Target**: safe-by-induction preservation of safety from a safe initialization, subject to feasible projections and stated rollout/smoothness assumptions.

**Guarantee Basis**: sampling-based local safe region and projected policy-update analysis.

**Inference Dependency**: no output repair layer; safety is enforced during parameter updates.

**Main Tradeoff**: provides training-time safe-update guarantees for policy learning, but depends on rollout coverage, local smoothness bounds, feasible QCQP projections, and a safe initialization.

**Evidence Note**: local original PDF abstract, introduction, and preliminaries checked.
