# `zeng2024qcqp`

**Source Status**: verified_from_source

**Source Pdf File**: zeng2024qcqp__qcqp_net_reliably_learning_feasible_alternating_current_optimal_power_flow_solutions_under_constraints.pdf

**Method Family Primary**: structured AC-OPF feasibility layer.

**Learning Task**: learn feasible AC-OPF solutions from load inputs.

**Model Paradigm**: feed-forward neural prediction plus nonconvex QCQP activation.

**Constraint Form**: AC-OPF power-flow constraints formulated through a relaxed QCQP.

**Constraint Geometry**: nonconvex quadratic AC power-flow structure.

**Mechanism Label**: QCQP activation.

**Mechanism Summary**: QCQP-Net predicts independent AC-OPF variables and then computes state variables through a relaxed power-flow QCQP used as an implicit activation, with losses designed to improve constraint satisfaction.

**Guarantee Target**: high-feasibility AC-OPF predictions under the relaxed QCQP framework.

**Guarantee Basis**: differentiable QCQP activation and constraint-violation loss; exact hard-feasibility scope should be checked against the theorem/algorithm section before final claims.

**Inference Dependency**: QCQP activation solve.

**Main Tradeoff**: stronger AC structure handling adds a specialized nonconvex QCQP component.

**Evidence Note**: abstract and first pages checked.
