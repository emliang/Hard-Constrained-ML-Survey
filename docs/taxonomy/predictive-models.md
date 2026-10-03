
# Hard-Constrained Predictive Models

Predictive methods return decisions, labels, trajectories, controls, or optimization variables subject to constraints.

## Families

| Family | Core idea | Typical evidence |
|---|---|---|
| Training-based approaches | Soft penalties, Lagrangian procedures, or verification-guided training and editing. | Evaluated residuals or a property established for the resulting predictor over a stated domain. |
| Structured NN layers | Explicit constructions, equality completion, or embedded optimization. | Construction assumptions or the residual of the returned numerical output. |
| Constraint parameterization | Feasible combinations, feasible distributions, or global feasible-set maps. | Valid generators, distribution support, or map image within the feasible set. |
| Post-processing approaches | Warm-start a solver or correct a completed prediction. | Feasibility and quality of the final solve or corrected output. |

Hybrid pipelines combine these roles. Explicit layers act on predictive output quantities within the trained forward pass; parameterizations interpret reference coordinates or coefficients. Verification of an unchanged model supplies evidence, while verification-guided training or editing changes the predictor.

See [the numbered paper tables](../papers/prediction.md).
