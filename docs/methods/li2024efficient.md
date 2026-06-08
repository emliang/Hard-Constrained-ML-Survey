# `li2024efficient`

**Source Status**: verified_from_source

**Source Pdf File**: li2024efficient__efficient_and_guaranteed_safe_non_convex_trajectory_optimization_with_constrained_diffusion_model.pdf

**Method Family Primary**: constrained diffusion warm-start for trajectory optimization.

**Learning Task**: solve nonconvex robotic trajectory optimization with improved speed and safety.

**Model Paradigm**: constrained diffusion model plus numerical solver refinement.

**Constraint Form**: trajectory dynamics and safety constraints in nonconvex robotics settings.

**Constraint Geometry**: nonconvex trajectory feasible sets.

**Mechanism Label**: constrained diffusion solver warm start.

**Mechanism Summary**: The method trains a diffusion model with an additional constraint-violation loss to sample approximate locally optimal trajectories, then passes those samples to a numerical solver for refinement and formal feasibility/optimality verification.

**Guarantee Target**: verified final trajectory feasibility after solver refinement.

**Guarantee Basis**: numerical solver verification; the diffusion model alone is a guided warm-start distribution.

**Inference Dependency**: diffusion sampling followed by numerical trajectory optimization.

**Main Tradeoff**: improves speed by providing high-quality initial guesses, but final guarantees depend on the downstream solver.

**Evidence Note**: abstract and first pages checked.
