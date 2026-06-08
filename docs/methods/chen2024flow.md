# `chen2024flow`

**Source Status**: verified_from_source

**Source Pdf File**: chen2024flow__flow_matching_on_general_geometries.pdf

**Method Family Primary**: Riemannian flow matching.

**Learning Task**: train continuous normalizing flows on manifolds and general geometries.

**Model Paradigm**: flow matching with geometry-aware per-sample vector fields.

**Constraint Form**: manifold/geometric support constraints.

**Constraint Geometry**: Riemannian manifolds, triangular meshes, maze-like manifolds with boundaries.

**Mechanism Label**: Riemannian Flow Matching.

**Mechanism Summary**: RFM constructs geometry-aware kernel/vector fields for flow matching on manifolds, enabling simulation-free training on simple geometries and tractable training on more general geometries through spectral decompositions.

**Guarantee Target**: generated samples live on the modeled geometric state space.

**Guarantee Basis**: manifold-valued flow construction.

**Inference Dependency**: geometry-aware flow sampler and geometric computations.

**Main Tradeoff**: support modeling depends on the availability and cost of geometry-specific kernels or spectral computations.

**Evidence Note**: abstract and first pages checked.
