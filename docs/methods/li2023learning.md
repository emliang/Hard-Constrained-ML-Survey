# `li2023learning`

**Source Status**: verified_from_source

**Source Pdf File**: li2023learning__learning_to_solve_optimization_problems_with_hard_linear_constraints.pdf

**Method Family Primary**: gauge-map hard linear constraint solver.

**Learning Task**: solve parametric optimization problems with hard linear constraints using a feed-forward neural approximator.

**Model Paradigm**: independent-variable reduction plus gauge map from an infinity-norm ball.

**Constraint Form**: hard linear constraints.

**Constraint Geometry**: feasible set of the reduced linear-constraint problem.

**Mechanism Label**: gauge map from unit ball.

**Mechanism Summary**: The method reduces the original problem to independent variables, builds a gauge function mapping the l-infinity unit ball to the reduced feasible set, learns the optimizer in that unit ball, and reconstructs dependent variables to recover a feasible original solution.

**Guarantee Target**: hard feasibility for the modeled linear constraints.

**Guarantee Basis**: reduction, gauge mapping, and reconstruction sequence.

**Inference Dependency**: gauge-map evaluation and dependent-variable recovery.

**Main Tradeoff**: applies to hard linear constraints where the reduced feasible set and gauge function are available.

**Evidence Note**: abstract and first pages checked.
