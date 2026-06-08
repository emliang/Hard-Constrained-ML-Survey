# `chzhen2026improving`

**Source Status**: verified_from_source

**Source Pdf File**: chzhen2026improving__improving_feasibility_via_fast_autoencoder_based_projections.pdf

**Method Family Primary**: projection-analogous correction / amortized autoencoder projection.

**Learning Task**: rapidly correct infeasible predictions for complex nonconvex constraints.

**Model Paradigm**: autoencoder with structured convex latent representation.

**Constraint Form**: complex operational constraints, including nonconvex examples in the paper.

**Constraint Geometry**: learned feasible-set representation with a simple convex latent correction set.

**Mechanism Label**: autoencoder-based projection.

**Mechanism Summary**: The method trains an autoencoder adversarially so feasible outputs have a structured convex latent representation; a raw prediction is encoded, its latent code is projected or mapped onto a simple convex set, and the decoder maps it back to the output space.

**Guarantee Target**: fast approximate feasibility correction.

**Guarantee Basis**: amortized learned projection; constraint satisfaction should be empirically validated for the target problem.

**Inference Dependency**: encoder, latent projection, and decoder.

**Main Tradeoff**: much cheaper than solver-based correction, but accuracy depends on learned feasible-set representation.

**Evidence Note**: abstract and first pages checked.
