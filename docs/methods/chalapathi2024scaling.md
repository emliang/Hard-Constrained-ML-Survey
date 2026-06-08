# `chalapathi2024scaling`

**Source Status**: verified_from_source

**Source Pdf File**: chalapathi2024scaling__scaling_physics_informed_hard_constraints_with_mixture_of_experts.pdf

**Method Family Primary**: decomposed physics-informed hard constraints.

**Learning Task**: enforce physical/PDE constraints in neural dynamics models at larger scale.

**Model Paradigm**: mixture-of-experts differentiable optimization.

**Constraint Form**: equality constraints from physical laws/PDE residuals over spatiotemporal domains.

**Constraint Geometry**: mesh/discretization-defined physical constraint systems.

**Mechanism Label**: PI-HC-MoE local hard constraints.

**Mechanism Summary**: PI-HC-MoE decomposes a large physical constraint domain into smaller expert subdomains, each solved through differentiable optimization with local implicit differentiation, enabling parallel hard-constraint enforcement.

**Guarantee Target**: hard physical-constraint satisfaction over the modeled local domains.

**Guarantee Basis**: differentiable constrained optimization per expert.

**Inference Dependency**: local expert optimization solves.

**Main Tradeoff**: scalability improves through decomposition, but the hard constraint is enforced through multiple optimization layers.

**Evidence Note**: abstract, introduction, and contributions checked.
