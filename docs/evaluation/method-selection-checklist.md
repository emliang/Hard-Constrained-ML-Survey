
# Method-Selection Checklist

| Starting condition | Candidate families | Checks before a hard-feasibility claim |
|---|---|---|
| Simple or structured continuous set; low-latency deployment | Activation, completion, explicit feasibility layer, constraint parameterization | State exact constraint class, map validity, numerical tolerance, and whether feasibility is by construction or empirical. |
| Projection, repair, or constrained solver is available at inference time | Post-processing, optimization layer, unrolled repair | Report solver tolerance, termination rule, iteration count, differentiability assumptions, and inference latency. |
| Constraint changes with input or conditioning variable | Input-dependent completion, recovery layer, learned map, reflected sampler, guided generator | Check how each feasible set is represented and whether interior points, boundary operations, or oracles remain valid. |
| Constraint is broad, uncertain, discrete, or partly specified | Penalty, Lagrangian, verifier/editor, constrained decoding, guided sampling | Separate feasibility pressure from certified, solver-tolerance, probabilistic, or empirical evidence. |
