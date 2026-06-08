# `tao2024provable`

**Source Status**: verified_from_source

**Source Pdf File**: tao2024provable__provable_parameter_editing_for_enforcing_safety_in_neural_networks.pdf

**Method Family Primary**: network editing for safety.

**Learning Task**: edit a trained network so outputs satisfy a target safety set.

**Model Paradigm**: parameter editing via linear relaxation.

**Constraint Form**: input polytope to output polytope inclusion.

**Constraint Geometry**: polytope-to-polytope safety property.

**Mechanism Label**: provable parameter editing.

**Mechanism Summary**: PREPARED edits DNN parameters so that every input in an input polytope is mapped into a desired output polytope; the hard editing problem is relaxed into an LP using parametric linear relaxation.

**Guarantee Target**: output-set inclusion for all inputs in the specified input polytope.

**Guarantee Basis**: LP relaxation/certificate described by the paper.

**Inference Dependency**: none after editing.

**Main Tradeoff**: the certified property is tied to specified polytopes and relaxation tightness.

**Evidence Note**: abstract and first pages checked.
