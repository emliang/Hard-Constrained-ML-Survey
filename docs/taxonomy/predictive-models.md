
# Hard-Constrained Predictive Models

Predictive methods return decisions, labels, trajectories, controls, or optimization variables subject to constraints.

## Families

| Family | Core idea | Typical evidence |
|---|---|---|
| Training-time losses and dual methods | Penalize or optimize violations during fitting. | Empirical residuals, convergence assumptions, or dual certificates. |
| Post-processing and repair | Correct raw predictions after inference. | Solver tolerance, projection quality, repair success rate. |
| Structured NN or optimization layers | Embed a differentiable solve, completion, or fixed-point operation. | Solver exactness, layer assumptions, KKT or fixed-point conditions. |
| Explicit feasibility mappings | Map unconstrained outputs into feasible regions. | Map validity and by-construction feasibility. |
| Constraint parameterization | Parameterize only feasible outputs. | Exactness of the parameterization and coverage of the feasible set. |
| Verification and editing | Certify or edit a trained model over a specified domain. | Certificate scope, relaxation tightness, or edited-property proof. |
