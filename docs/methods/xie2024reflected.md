# `xie2024reflected`

**Source Status**: verified_from_source

**Source Pdf File**: xie2024reflected__reflected_flow_matching.pdf

**Method Family Primary**: reflected flow matching.

**Learning Task**: train continuous normalizing flows on constrained domains.

**Model Paradigm**: reflected CNF trained by reflected flow matching.

**Constraint Form**: constrained-domain support constraints.

**Constraint Geometry**: domains with boundary constraints suitable for reflected dynamics.

**Mechanism Label**: reflected flow matching.

**Mechanism Summary**: The method adds a boundary constraint term to continuous normalizing flows so trajectories remain in the constrained domain, and trains the resulting reflected CNF with simulation-free reflected flow matching.

**Guarantee Target**: constrained-domain trajectory/sample support.

**Guarantee Basis**: reflected dynamics and boundary constraint construction.

**Inference Dependency**: reflected ODE/flow sampling.

**Main Tradeoff**: support preservation depends on boundary handling and numerical simulation error.

**Evidence Note**: abstract and first pages checked.
