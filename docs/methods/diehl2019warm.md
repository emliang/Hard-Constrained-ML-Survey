# `diehl2019warm`

**Source Status**: verified_from_source

**Source Pdf File**: diehl2019warm__warm_starting_ac_optimal_power_flow_with_graph_neural_networks.pdf

**Method Family Primary**: OPF warm start.

**Learning Task**: predict good AC-OPF initial points or approximate solutions.

**Model Paradigm**: graph neural network.

**Constraint Form**: AC-OPF power-network constraints.

**Constraint Geometry**: nonlinear power-flow feasible region.

**Mechanism Label**: learning-to-warm-start.

**Mechanism Summary**: A GNN exploits power-grid graph structure to produce AC-OPF solution estimates and warm starts; feasibility is inherited only when a downstream optimizer is run to convergence.

**Guarantee Target**: faster AC-OPF solving, not standalone hard feasibility.

**Guarantee Basis**: downstream solver tolerance for the warm-started solve.

**Inference Dependency**: optimizer if feasibility certification is required.

**Main Tradeoff**: direct predictions are fast but not independently certified.

**Evidence Note**: abstract and first pages checked.
