# `liu2024mirror`

**Source Status**: verified_from_source

**Source Pdf File**: liu2024mirror__mirror_diffusion_models_for_constrained_and_watermarked_generation.pdf

**Method Family Primary**: convex-domain diffusion.

**Learning Task**: generate data on convex constrained sets.

**Model Paradigm**: mirror-map diffusion.

**Constraint Form**: convex constrained sets.

**Constraint Geometry**: mirror-mapped convex domain, including examples such as simplex and l2 ball.

**Mechanism Label**: mirror diffusion.

**Mechanism Summary**: Mirror Diffusion learns a diffusion process in the unconstrained dual space induced by a mirror map, then maps samples back to the convex constrained domain.

**Guarantee Target**: constrained-domain sampling.

**Guarantee Basis**: valid mirror map and dual-primal transformation.

**Inference Dependency**: mirror map and reverse diffusion sampler.

**Main Tradeoff**: practical scope depends on tractable mirror maps for the target domain.

**Evidence Note**: abstract and first pages checked.
