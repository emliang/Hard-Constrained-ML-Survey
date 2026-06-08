# `li2025hardflow`

**Source Status**: verified_from_source

**Source Pdf File**: li2025hardflow__hardflow_generating_molecular_conformations_with_hard_constraints.pdf

**Method Family Primary**: constrained flow matching.

**Learning Task**: generate molecular conformations with hard constraints.

**Model Paradigm**: flow matching plus trajectory optimization.

**Constraint Form**: terminal hard constraints for molecular conformations.

**Constraint Geometry**: molecular conformation constraint set.

**Mechanism Label**: terminal constrained trajectory optimization.

**Mechanism Summary**: HardFlow reformulates hard-constrained flow-matching sampling as a trajectory optimization problem so constraints are satisfied at terminal time, using numerical optimal-control ideas and an MPC-style surrogate.

**Guarantee Target**: terminal-time hard-constraint satisfaction.

**Guarantee Basis**: trajectory optimization solve/surrogate quality.

**Inference Dependency**: trajectory optimization or MPC-style constrained sampler.

**Main Tradeoff**: hard terminal control increases sampling complexity.

**Evidence Note**: abstract and first pages checked.
