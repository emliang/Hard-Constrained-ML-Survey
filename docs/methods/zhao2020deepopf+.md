# `zhao2020deepopf+`

**Source Status**: verified_from_source

**Source Pdf File**: zhao2020deepopf+__deepopf+_a_deep_neural_network_approach_for_dc_optimal_power_flow_for_ensuring_feasibility.pdf

**Method Family Primary**: predictive OPF with feasibility calibration.

**Learning Task**: learn fast DC-OPF mappings while reducing constraint violations.

**Model Paradigm**: DNN surrogate with calibrated limits.

**Constraint Form**: generation and transmission line constraints in DC-OPF.

**Constraint Geometry**: linear/power-network feasible region.

**Mechanism Label**: constraint-limit calibration.

**Mechanism Summary**: DeepOPF+ anticipates DNN prediction error by calibrating generation and line-flow limits during training so that the predicted solution remains feasible under the paper's stated calibration analysis.

**Guarantee Target**: feasibility of predicted DC-OPF solutions.

**Guarantee Basis**: analytical calibration magnitude under stated assumptions.

**Inference Dependency**: direct DNN prediction; no optimization solve is the main intended path.

**Main Tradeoff**: calibration can make the learned feasible region more conservative.

**Evidence Note**: abstract and first pages checked.
