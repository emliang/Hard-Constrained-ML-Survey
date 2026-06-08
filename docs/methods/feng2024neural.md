# `feng2024neural`

**Source Status**: verified_from_source

**Source Pdf File**: feng2024neural__neural_approximate_mirror_maps_for_constrained_diffusion_models.pdf

**Method Family Primary**: learned mirror-map constrained diffusion.

**Learning Task**: train constrained diffusion models for general differentiable constraints.

**Model Paradigm**: neural approximate mirror map and approximate inverse.

**Constraint Form**: general possibly nonconvex constraints with differentiable distance to the constraint set.

**Constraint Geometry**: learned mirror space paired with an approximate constraint-set inverse.

**Mechanism Label**: NAMM learned mirror map.

**Mechanism Summary**: NAMM learns an approximate mirror map into an unconstrained space and an approximate inverse back to the constraint set, allowing diffusion models to train in the learned mirror space and restore samples through the inverse map.

**Guarantee Target**: improved constraint satisfaction of generated samples.

**Guarantee Basis**: learned approximate map; feasibility is map-validity dependent rather than exact by construction in this first-pass reading.

**Inference Dependency**: learned mirror map/inverse around the diffusion sampler.

**Main Tradeoff**: broader constraint coverage comes with approximation error and the need to validate the learned map.

**Evidence Note**: abstract and first pages checked.
