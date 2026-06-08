# `tanneau2024dual`

**Source Status**: verified_from_source

**Source Pdf File**: tanneau2024dual__dual_lagrangian_learning_for_conic_optimization.pdf

**Method Family Primary**: dual conic optimization proxy.

**Learning Task**: learn dual solutions for parametric conic optimization.

**Model Paradigm**: dual Lagrangian learning with conic completion/projection.

**Constraint Form**: linear and nonlinear conic optimization problems.

**Constraint Geometry**: conic feasible regions.

**Mechanism Label**: dual-feasible completion.

**Mechanism Summary**: Dual Lagrangian Learning trains ML dual proxies using conic duality, dual completion, differentiable conic projection layers, and a self-supervised Lagrangian loss to produce dual-feasible solutions and valid dual bounds.

**Guarantee Target**: dual feasibility and Lagrangian dual bounds, rather than primal pointwise feasibility.

**Guarantee Basis**: conic dual completion and projection.

**Inference Dependency**: dual proxy plus completion/projection formulas or layers.

**Main Tradeoff**: provides certificates/bounds but must be paired with a primal proxy if a feasible primal decision is needed.

**Evidence Note**: abstract and first pages checked.
