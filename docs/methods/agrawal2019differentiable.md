# `agrawal2019differentiable`

**Source Status**: verified_from_source

**Source Pdf File**: agrawal2019differentiable__differentiable_convex_optimization_layers.pdf

**Method Family Primary**: differentiable convex optimization layer.

**Learning Task**: differentiate through parametrized convex programs inside deep models.

**Model Paradigm**: disciplined convex programming layer with cone-solver differentiation.

**Constraint Form**: disciplined parametrized convex programs, lowered to cone programs.

**Constraint Geometry**: convex/conic feasible regions.

**Mechanism Label**: DPP-to-ASA differentiable layer.

**Mechanism Summary**: The method introduces disciplined parametrized programming and represents each compliant problem in affine-solver-affine form, enabling end-to-end differentiation through a high-level convex optimization specification.

**Guarantee Target**: convex-program solution feasibility and differentiability of the solution map when solver/regularity assumptions hold.

**Guarantee Basis**: numerical conic solve plus analytical differentiation through the ASA representation.

**Inference Dependency**: convex/conic optimization solve.

**Main Tradeoff**: broad convex modeling support comes with solver cost and DPP grammar restrictions.

**Evidence Note**: abstract and first pages checked.
