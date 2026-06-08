# `pan2020deepopf`

**Source Status**: verified_from_source

**Source Pdf File**: pan2020deepopf__deepopf_a_deep_neural_network_approach_for_security_constrained_dc_optimal_power_flow.pdf

**Method Family Primary**: predictive OPF.

**Learning Task**: map system load inputs to DC-OPF decision variables.

**Model Paradigm**: DNN surrogate.

**Constraint Form**: DC-OPF equality and inequality constraints.

**Constraint Geometry**: linear/power-network feasible region.

**Mechanism Label**: predict-and-reconstruct.

**Mechanism Summary**: The DNN predicts the independent generation variables from load inputs, and the remaining variables such as phase angles are reconstructed through power-flow equations instead of learned freely.

**Guarantee Target**: fast approximate OPF solution.

**Guarantee Basis**: equality structure is partly reconstructed; inequality feasibility is not a hard by-construction guarantee in this first source pass.

**Inference Dependency**: direct DNN prediction plus equation-based reconstruction.

**Main Tradeoff**: speed is gained by replacing optimization with prediction, but strict feasibility still needs checking or additional safeguards.

**Evidence Note**: abstract and first pages checked.
