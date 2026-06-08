# `lee2025local`

**Source Status**: verified_from_source

**Source Pdf File**: lee2025__local_manifold_approximation_and_projection_for_manifold_aware_diffusion_planning.pdf

**Method Family Primary**: manifold-aware diffusion planning.

**Learning Task**: improve feasibility of diffusion-generated trajectories in offline planning.

**Model Paradigm**: training-free local manifold approximation and projection.

**Constraint Form**: trajectory feasibility as adherence to the data/manifold of valid offline trajectories.

**Constraint Geometry**: local low-rank trajectory manifold approximated from nearest neighbors.

**Mechanism Label**: LoMAP local projection.

**Mechanism Summary**: LoMAP denoises the current guided sample, retrieves nearby offline trajectories, forward-diffuses them to the same timestep, approximates a local low-rank subspace by PCA, and projects the sample back to reduce off-manifold trajectory artifacts.

**Guarantee Target**: reduced manifold deviation and infeasible trajectory generation.

**Guarantee Basis**: local manifold approximation and projection; feasibility is data-manifold dependent.

**Inference Dependency**: nearest-neighbor retrieval, local PCA, and projection at sampling steps.

**Main Tradeoff**: training-free but adds retrieval/projection cost and depends on offline dataset coverage.

**Evidence Note**: abstract, introduction, and method overview checked; local filename differs from cite-key prefix.
