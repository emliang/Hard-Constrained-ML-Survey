# `tabas2022safe`

**Source Status**: verified_from_source

**Source Pdf File**: tabas2022safe__safe_and_efficient_model_predictive_control_using_neural_networks_an_interior_point_approach.pdf

**Method Family Primary**: gauge-map MPC feasible-set parameterization.

**Learning Task**: learn approximate explicit MPC policies while preserving finite-horizon MPC constraints.

**Model Paradigm**: neural policy predicts coordinates in a simple reference domain; an interior-point construction and gauge map send them into the MPC feasible set.

**Constraint Form**: finite-horizon MPC constraints with polytopic state/input constraints in the paper's studied settings.

**Constraint Geometry**: state-dependent MPC feasible set with an interior point and gauge map from \\(B_\\infty\\).

**Mechanism Label**: Gauge NN / interior-point gauge map.

**Mechanism Summary**: The method first constructs an interior point of the MPC feasible set, then uses a differentiable gauge map from the infinity-norm unit ball to the state-dependent feasible set so that the neural policy output is feasible by construction without an online MPC oracle or projection solve.

**Guarantee Target**: constraint satisfaction of the learned MPC policy output.

**Guarantee Basis**: Phase-I interior-point construction and gauge-map parameterization of the MPC feasible set.

**Inference Dependency**: interior-point construction and closed-form gauge-map evaluation.

**Main Tradeoff**: feasibility depends on the MPC feasible set being strictly feasible and on the availability and stability of the gauge-map construction; the approach targets speed compared with online MPC or projection-based correction.

**Evidence Note**: PDF text checked around abstract, method, gauge-map construction, and conclusion.
