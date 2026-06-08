# `heaton2021feasibility`

**Source Status**: verified_from_source

**Source Pdf File**: heaton2021feasibility__feasibility_based_fixed_point_networks.pdf

**Method Family Primary**: feasibility-based fixed-point network.

**Learning Task**: solve inverse problems by combining convex feasibility with learned regularization.

**Model Paradigm**: fixed-point iterations over nonexpansive operators.

**Constraint Form**: feasibility constraints from inverse-problem measurement models.

**Constraint Geometry**: convex feasibility sets combined with learned regularization operators.

**Mechanism Label**: F-FPN nonexpansive fixed points.

**Mechanism Summary**: F-FPNs define nonexpansive operators composed of projection-based feasibility operators and data-driven regularizers, then compute fixed points whose operator weights are trained from data.

**Guarantee Target**: fixed-point recovery respecting modeled feasibility structure.

**Guarantee Basis**: nonexpansive operator/fixed-point formulation.

**Inference Dependency**: fixed-point iteration.

**Main Tradeoff**: feasibility is tied to the modeled projection operators, while recovery quality depends on learned regularization.

**Evidence Note**: abstract and first pages checked.
