# `pal2026disjunctivenet`

**Source Status**: verified_from_source

**Source Pdf File**: pal2026disjunctivenet__disjunctivenet_neural_symbolic_learning_via_differentiable_convexified_optimization_layers.pdf

**Method Family Primary**: differentiable convexified logical constraint layer.

**Learning Task**: enforce input-dependent logical and mixed-integer linear rules in neural outputs.

**Model Paradigm**: differentiable LP layer from disjunctive convex-hull relaxations.

**Constraint Form**: disjunctive constraints, logical rules, QF-LRA-style linear logic, and MILP-equivalent bounded rules.

**Constraint Geometry**: unions of polyhedra and their DNF convex-hull formulations.

**Mechanism Label**: DisjunctiveNet DNF projection.

**Mechanism Summary**: DisjunctiveNet represents rules as disjunctive constraints, sequentially convexifies them using disjunctive-programming convex hulls, and embeds the resulting LP as a differentiable optimization layer.

**Guarantee Target**: exact rule satisfaction for the original logical constraints under the DNF projection extreme-point conditions.

**Guarantee Basis**: DNF convex-hull LP formulation and exactness theorem.

**Inference Dependency**: LP projection layer.

**Main Tradeoff**: DNF convexification can grow exponentially in interacting active rules; CNF relaxations are more scalable but weaker.

**Evidence Note**: abstract, introduction, and method overview checked.
