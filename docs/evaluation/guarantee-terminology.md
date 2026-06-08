
# Guarantee Terminology

The repository separates several meanings of feasibility.

| Label | Meaning |
|---|---|
| `exact_by_construction` | The architecture or parameterization only produces feasible outputs under stated assumptions. |
| `solver_tolerance_exactness` | Feasibility follows from a solver, repair, or projection run to a numerical tolerance. |
| `certified_or_verified_feasibility` | A certificate or verifier covers a specified input or output domain. |
| `convergence_or_asymptotic_feasibility` | Feasibility is tied to an algorithmic convergence statement. |
| `probabilistic_feasibility` | The claim is probabilistic or distributional. |
| `empirical_feasibility` | The claim is supported by observed violation rates or residuals only. |
