# `diederen2025flows`

**Source Status**: verified_from_source

**Source Pdf File**: diederen2025flows__flows_on_convex_polytopes.pdf

**Method Family Primary**: normalizing flows on convex polytopes.

**Learning Task**: model high-dimensional distributions supported on convex polytopes.

**Model Paradigm**: flow on unit ball mapped back through polytope homeomorphism; barycentric-coordinate variant for vertex representations.

**Constraint Form**: convex polytope support constraints.

**Constraint Geometry**: full-dimensional convex polytopes homeomorphic to a unit ball.

**Mechanism Label**: polytope flow via ball homeomorphism.

**Mechanism Summary**: The framework defines flows on a unit ball and maps them to convex polytopes through a homeomorphism, with an additional construction based on maximum-entropy barycentric coordinates and Aitchison geometry when a vertex representation is available.

**Guarantee Target**: generated samples remain on the modeled polytope support.

**Guarantee Basis**: polytope-to-ball homeomorphism or barycentric-coordinate construction.

**Inference Dependency**: flow sampling plus homeomorphic/barycentric map.

**Main Tradeoff**: requires a valid polytope representation and map construction.

**Evidence Note**: abstract and first pages checked.
