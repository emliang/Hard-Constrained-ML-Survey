
# How to Read a Hard-Constraint Claim

When a paper says that a method satisfies hard constraints, read the claim as a contract. The contract has a mechanism, evidence, cost, and scope.

## 1. Identify the enforcement mechanism

Ask where feasibility enters the method.

- Training loss or penalty
- Lagrangian or primal-dual update
- Output repair or projection
- Differentiable optimization layer
- Feasibility-preserving map
- Constrained decoding
- Constrained sampler
- Inference-time guidance
- Verification or model editing

## 2. Identify the guarantee basis

Then ask why the output should be feasible.

| Basis | What to check |
|---|---|
| By construction | Is the map valid, and does it cover the intended feasible set? |
| Solver tolerance | What tolerance, termination rule, and solver failure mode are reported? |
| Certificate | What input/output region is certified, and how tight is the relaxation? |
| Convergence | What assumptions are required, and is finite-time behavior reported? |
| Probabilistic | What probability statement is made, and under which distribution? |
| Empirical | Are residuals, violation rates, and stress tests reported? |

## 3. Check output utility

Feasibility alone is not enough. A repaired prediction, constrained sample, or decoded sequence may satisfy the constraint while losing task quality.

Look for:

- prediction error,
- objective gap,
- reward or control performance,
- sample fidelity and diversity,
- downstream success,
- application-specific utility.

## 4. Check enforcement cost

The cost may move from training to inference.

Report or look for:

- extra loss terms or dual updates,
- verifier or solver calls,
- projection or repair iterations,
- sampler steps,
- decoding overhead,
- memory use,
- latency under deployment conditions.

## 5. Check scope

A hard-constraint claim may apply only under a specific geometry, bounded input region, oracle, discretization, or solver condition.

The most useful papers state this scope explicitly. When the scope is hidden, treat the claim cautiously.
