# `donti2021dc3`

**Source Status**: verified_from_source

**Source Pdf File**: donti2021dc3__dc3_a_learning_method_for_optimization_with_hard_constraints.pdf

**Method Family Primary**: completion and correction layer.

**Learning Task**: predict solutions to hard-constrained optimization problems.

**Model Paradigm**: neural prediction followed by differentiable completion/correction.

**Constraint Form**: equality and inequality constraints in hard-constrained optimization.

**Constraint Geometry**: problem-dependent.

**Mechanism Label**: DC3 completion-correction.

**Mechanism Summary**: DC3 trains a neural predictor together with differentiable completion and correction steps so the network output is adjusted toward feasibility instead of being used as an unconstrained prediction.

**Guarantee Target**: feasible or near-feasible optimization solution.

**Guarantee Basis**: analytical completion plus iterative correction; tolerance and problem structure matter.

**Inference Dependency**: completion/correction steps.

**Main Tradeoff**: stronger feasibility handling requires extra inference-time correction.

**Evidence Note**: abstract and first pages checked; exact classes of guaranteed constraints should be checked in the method section before final table wording.
