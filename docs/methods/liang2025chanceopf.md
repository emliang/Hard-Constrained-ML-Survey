# `liang2025chanceopf`

**Source Status**: verified_from_source

**Source Pdf File**: liang2025chanceopf__solving_chance_constrained_ac_opf_problem_by_neural_network_with_bisection_based_projection.pdf

**Method Family Primary**: projection-analogous correction / bisection-based projection for chance-constrained OPF.

**Learning Task**: solve chance-constrained AC-OPF quickly under uncertainty.

**Model Paradigm**: neural deterministic AC-OPF approximation followed by projection.

**Constraint Form**: chance constraints in AC-OPF with specified confidence level.

**Constraint Geometry**: power-system feasible set under sampled uncertainty.

**Mechanism Label**: bisection-based projection.

**Mechanism Summary**: The method first uses a neural network to approximate deterministic AC-OPF solutions, then applies a bisection-based projection algorithm using random sampling to recover solutions satisfying chance constraints.

**Guarantee Target**: feasible CC-ACOPF solutions and optimality bounds.

**Guarantee Basis**: bisection-based projection and the paper's feasibility/optimality analysis.

**Inference Dependency**: projection phase after neural prediction.

**Main Tradeoff**: feasibility comes from the projection stage, and sampling/projection adds inference cost.

**Evidence Note**: abstract and first pages checked; local PDF key includes `chanceopf`.
