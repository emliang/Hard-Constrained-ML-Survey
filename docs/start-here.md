
# Start Here

Hard-constrained machine learning studies models whose outputs must satisfy constraints before they are usable.

Examples include:

- predicted power-flow decisions that must satisfy network limits,
- generated molecules or materials that must satisfy validity rules,
- trajectories that must remain safe,
- text or structured outputs that must obey grammar or logic,
- scientific surrogates that must respect conservation laws or physical bounds.

## The first distinction

A hard-constraint paper can mean several different things.

| Claim type | What it usually means |
|---|---|
| By construction | The model architecture or parameterization only produces feasible outputs under stated assumptions. |
| Solver tolerance | A projection, repair, decoder, or optimizer returns an output satisfying numerical tolerances. |
| Certified | A verifier or certificate covers a specified input/output domain. |
| Probabilistic | Feasibility holds with a probability or distributional statement. |
| Empirical | Experiments show small violations or high validity rates, but no general guarantee is established. |

These labels are not interchangeable. A method with excellent empirical validity may not support the same claim as a certified or by-construction method.

## The four questions to ask

Every hard-constraint method should be read through four questions.

1. **Constraint satisfaction**: What supports feasibility, and what residuals or tolerances remain?
2. **Output utility**: Does the constrained output still solve the task well?
3. **Cost**: What training or inference cost is paid for enforcement?
4. **Scope and assumptions**: Which constraint classes, domains, solvers, or maps make the claim valid?

## Why mechanism matters

Application names are useful, but they do not tell the whole story. Two optimal-power-flow papers may use very different enforcement mechanisms. A constrained generator and a constrained predictor may both rely on a projection or a feasibility-preserving map.

The survey therefore uses a mechanism-first view: where does the method intervene, and why should the output be feasible?
