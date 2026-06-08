# `davis2024fisher`

**Source Status**: verified_from_source

**Source Pdf File**: davis2024fisher__fisher_flow_matching_for_generative_modeling_over_discrete_data.pdf

**Method Family Primary**: Fisher-geometric flow matching for discrete data.

**Learning Task**: generative modeling over discrete/categorical data.

**Model Paradigm**: flow matching on Fisher-Rao statistical manifold.

**Constraint Form**: categorical simplex/positive-orthant support induced by discrete data distributions.

**Constraint Geometry**: positive orthant of a hypersphere under Fisher-Rao geometry.

**Mechanism Label**: Fisher Flow.

**Mechanism Summary**: Fisher Flow reparameterizes categorical distributions as points on the positive orthant of a hypersphere with the Fisher-Rao metric and learns flows along closed-form geodesics for discrete-data generation.

**Guarantee Target**: geometry-respecting continuous representation of discrete distributions.

**Guarantee Basis**: Fisher-Rao manifold construction and geodesic flow matching.

**Inference Dependency**: manifold flow sampler and discrete decoding.

**Main Tradeoff**: support geometry is respected in the categorical distribution space; task-level validity after decoding still needs evaluation.

**Evidence Note**: abstract and first pages checked.
