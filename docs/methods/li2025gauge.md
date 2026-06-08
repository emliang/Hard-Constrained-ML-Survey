# `li2025gauge`

**Source Status**: verified_from_source

**Source Pdf File**: li2025gauge__gauge_flow_matching_for_efficient_constrained_generative_modeling_over_general_convex_set.pdf

**Method Family Primary**: gauge-based constrained flow matching.

**Learning Task**: generate samples over compact convex sets while preserving constraints.

**Model Paradigm**: flow matching with bijective gauge map to the unit ball.

**Constraint Form**: arbitrary compact convex sets in the paper's stated scope.

**Constraint Geometry**: compact convex domains mapped to a unit ball.

**Mechanism Label**: gauge flow matching.

**Mechanism Summary**: GFM introduces a bijective gauge mapping that converts generation over a compact convex set into an equivalent process over the unit ball, then maps generated samples back to the constrained domain.

**Guarantee Target**: strict sample-level constraint satisfaction over the modeled compact convex set.

**Guarantee Basis**: bijective gauge map and bounded distribution-approximation analysis.

**Inference Dependency**: gauge-map evaluation around the flow-matching sampler.

**Main Tradeoff**: applicability depends on constructing a valid gauge map for the target compact convex set.

**Evidence Note**: abstract and first pages checked; workshop version.
