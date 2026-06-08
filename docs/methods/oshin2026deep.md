# `oshin2026deep`

**Source Status**: verified_from_source

**Source Pdf File**: oshin2026__deep_flexqp_accelerated_nonlinear_programming_via_deep_unfolding.pdf

**Method Family Primary**: unfolded robust QP solver for NLP/SQP.

**Learning Task**: accelerate QP subproblem solving inside nonlinear programming workflows.

**Model Paradigm**: FlexQP elastic relaxation plus deep unfolding.

**Constraint Form**: convex QP constraints, including infeasible QP subproblems from SQP linearizations.

**Constraint Geometry**: convex QP feasible sets or elastic-relaxed infeasibility sets.

**Mechanism Label**: Deep FlexQP.

**Mechanism Summary**: FlexQP uses an l1 elastic relaxation so feasible QPs recover the original optimum while infeasible QPs return sparse constraint-violation-minimizing solutions; Deep FlexQP unfolds the solver and learns parameter policies to accelerate it.

**Guarantee Target**: robust QP subproblem solution or infeasibility-minimizing relaxed solution.

**Guarantee Basis**: exact relaxation and convergence results under the paper's assumptions.

**Inference Dependency**: unfolded FlexQP iterations, often inside SQP.

**Main Tradeoff**: improves QP/SQP robustness and speed, but infeasible original QPs are handled by relaxation rather than made feasible.

**Evidence Note**: abstract and first pages checked; local filename omits the full cite-key prefix.
