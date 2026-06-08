# `kim2025mpadnn`

**Source Status**: verified_from_source

**Source Pdf File**: kim2025mpadnn__mpa_dnn_projection_aware_unsupervised_learning_for_multi_period_dc_opf.pdf

**Method Family Primary**: differentiable projection layer for multi-period DC-OPF.

**Learning Task**: learn multi-period DC-OPF dispatch without supervised labels.

**Model Paradigm**: DNN produces a raw generation schedule; a differentiable projection layer projects it onto the multi-period DC-OPF feasible set and the projected output is used in the unsupervised loss.

**Constraint Form**: DC-OPF constraints with power balance, generator limits, ramping limits, energy-storage dynamics, and line limits.

**Constraint Geometry**: convex multi-period DC-OPF feasible set represented by linear equalities and inequalities.

**Mechanism Label**: projection-aware differentiable layer.

**Mechanism Summary**: The method embeds a constrained quadratic projection in the forward pass and backpropagates through the KKT system, so feasibility is enforced during both training and inference.

**Guarantee Target**: feasible multi-period dispatch schedules for the modeled linear DC-OPF constraints.

**Guarantee Basis**: exact solution of the projection layer over the modeled feasible set and KKT-based differentiation assumptions.

**Inference Dependency**: differentiable projection solve.

**Main Tradeoff**: strict feasibility for modeled linear constraints comes with projection-layer runtime and numerical differentiation cost; the scope is application-specific to multi-period DC-OPF.

**Evidence Note**: local PDF abstract, architecture figure, projection formulation, and evaluation section checked.
