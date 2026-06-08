# `klamkin2024dual`

**Source Status**: verified_from_source

**Source Pdf File**: klamkin2024dual__dual_interior_point_optimization_learning.pdf

**Method Family Primary**: dual feasible linear-optimization proxy.

**Learning Task**: learn dual feasible solutions to complement primal optimization proxies.

**Model Paradigm**: dual interior-point learning with completion.

**Constraint Form**: linear optimization dual constraints.

**Constraint Geometry**: linear-program dual feasible regions.

**Mechanism Label**: dual completion.

**Mechanism Summary**: The paper trains dual linear-optimization proxies with a smoothed self-supervised loss and applies a dual completion strategy, sometimes in closed form, to guarantee dual feasibility.

**Guarantee Target**: dual feasibility and primal quality bounds.

**Guarantee Basis**: dual completion optimization and closed-form completion formulas for covered penalty classes.

**Inference Dependency**: dual proxy plus completion step.

**Main Tradeoff**: provides dual certificates rather than direct primal feasibility; primal decisions still require a compatible primal method.

**Evidence Note**: abstract and first pages checked.
