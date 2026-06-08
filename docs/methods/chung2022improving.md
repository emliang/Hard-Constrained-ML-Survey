# `chung2022improving`

**Source Status**: verified_from_source

**Source Pdf File**: chung2022improving__improving_diffusion_models_for_inverse_problems_using_manifold_constraints.pdf

**Method Family Primary**: manifold-constrained inverse-problem guidance.

**Learning Task**: improve diffusion-based inverse problem solvers.

**Model Paradigm**: reverse diffusion plus manifold correction term.

**Constraint Form**: measurement consistency and data-manifold constraints for inverse problems.

**Constraint Geometry**: learned data manifold during diffusion sampling.

**Mechanism Label**: manifold constraint correction.

**Mechanism Summary**: The method adds a manifold-inspired correction term to diffusion inverse-problem samplers to keep sample paths closer to the data manifold and reduce accumulated error after measurement projections.

**Guarantee Target**: improved manifold consistency and inverse-problem reconstruction quality.

**Guarantee Basis**: correction term analysis and empirical validation; not a standalone hard feasibility guarantee.

**Inference Dependency**: manifold correction during sampling.

**Main Tradeoff**: simple to attach, but feasibility depends on the base solver and correction quality.

**Evidence Note**: abstract and first pages checked.
