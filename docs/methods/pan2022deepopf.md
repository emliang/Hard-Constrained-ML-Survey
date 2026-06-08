# `pan2022deepopf`

**Source Status**: verified_from_source

**Source Pdf File**: pan2022deepopf__deepopf_a_feasibility_optimized_deep_neural_network_approach_for_ac_optimal_power_flow_problems.pdf

**Method Family Primary**: predictive AC-OPF.

**Learning Task**: approximate AC-OPF solutions from load inputs.

**Model Paradigm**: DNN predict-and-reconstruct framework.

**Constraint Form**: AC power-flow equalities and operational inequalities.

**Constraint Geometry**: nonlinear AC power-system feasible region.

**Mechanism Label**: AC predict-and-reconstruct with penalty training.

**Mechanism Summary**: DeepOPF predicts independent operating variables, reconstructs remaining variables by solving AC power-flow equations, and uses penalty training with zero-order gradient estimation to reduce operation-limit violations.

**Guarantee Target**: power-flow balance satisfaction by reconstruction and improved inequality feasibility.

**Guarantee Basis**: equality reconstruction plus penalty-based training; first-pass evidence does not support treating all inequalities as hard-certified at inference.

**Inference Dependency**: DNN prediction plus AC power-flow reconstruction.

**Main Tradeoff**: fast inference depends on reconstruction and penalty-trained feasibility rather than a full OPF solve.

**Evidence Note**: abstract and first pages checked.
