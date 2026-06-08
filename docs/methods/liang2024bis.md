# `liang2024bis`

**Source Status**: verified_from_source

**Source Pdf File**: liang2024bis__efficient_bisection_projection_to_ensure_neural_network_solution_feasibility_for_optimization_over_general_set.pdf

**Method Family Primary**: projection-analogous correction / bisection projection.

**Learning Task**: recover feasibility of neural-network predictions for constrained optimization problems.

**Model Paradigm**: raw neural prediction plus an interior-point predictor and bisection-based feasibility recovery.

**Constraint Form**: compact input-dependent feasible sets with non-empty interiors under the paper's assumptions; experiments include convex and nonconvex constrained optimization instances.

**Constraint Geometry**: a feasible interior point and membership/feasibility checks support bisection along the segment from the raw prediction to the interior point.

**Mechanism Label**: bisection projection.

**Mechanism Summary**: The method predicts an interior point with an IPNN and applies bisection between an infeasible neural prediction and that interior point to return a feasible boundary point, avoiding a full Euclidean projection solve.

**Guarantee Target**: feasible corrected output and bounded bisection-induced optimality loss under stated assumptions.

**Guarantee Basis**: sufficient conditions for IPNN feasibility, compact-set/interior assumptions, feasibility checks, and bisection analysis.

**Inference Dependency**: raw predictor, IPNN, and finite bisection steps.

**Main Tradeoff**: lower online cost than generic projection, but performance depends on valid interior-point prediction, feasible-set membership checks, and the number of bisection steps.

**Evidence Note**: local PDF abstract, related-work comparison, framework section, and evaluation-metric appendix checked.
