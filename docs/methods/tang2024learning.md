# `tang2024learning`

**Source Status**: verified_from_source

**Source Pdf File**: tang2024learning__learning_to_optimize_for_mixed_integer_non_linear_programming_with_feasibility_guarantees.pdf

**Method Family Primary**: L2O for mixed-integer nonlinear programs.

**Learning Task**: produce fast feasible solutions for parametric MINLPs.

**Model Paradigm**: neural L2O with integer correction layers and projection.

**Constraint Form**: integer constraints plus continuous feasibility constraints in MINLPs.

**Constraint Geometry**: mixed discrete-continuous feasible regions.

**Mechanism Label**: integer correction plus projection.

**Mechanism Summary**: The method uses two integer correction layers to enforce integrality and a projection step to enforce feasibility, with a convergence result for the projection step.

**Guarantee Target**: integrality and projected feasibility for MINLP solutions.

**Guarantee Basis**: correction-layer construction and projection convergence proof.

**Inference Dependency**: integer correction layers plus projection step.

**Main Tradeoff**: general MINLP coverage requires correction/projection logic after neural prediction.

**Evidence Note**: abstract and first pages checked.
