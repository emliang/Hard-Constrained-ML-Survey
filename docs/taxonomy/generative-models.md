
# Hard-Constrained Generative Models

Generative methods produce samples under explicit validity, physical, structural, logical, or design constraints.

## Families

| Family | Core idea | Typical evidence |
|---|---|---|
| Direct generation | Produce a complete candidate using a sample map, with a feasible representation or output-side enforcement. | Map validity, correction accuracy, and coverage. |
| Autoregressive generation | Construct successive elements using prefix, grammar, completion, or search information. | Completed-output validity and fidelity to the intended constrained distribution. |
| Diffusion and flow-based generation | Train and evolve a sampler using geometry, parameterization, guidance, correction, or search. | The property established for the completed sample, including numerical and decoding effects. |

Training, fine-tuning, and mechanism combinations apply across these generation procedures. Guidance changes sampling preferences; it does not establish feasibility without further evidence or an enforcement operation. General one-step generators are background examples of sample maps.

Compare validity together with quality, diversity, coverage, and total cost per valid sample. See [the numbered paper tables](../papers/generation.md).

## Diffusion and Flow-Based Categories

- [3.3.1 Training-Based Methods](../papers/generation.md#331-training-based-methods)
- [3.3.2 Geometry-Aware Sampling](../papers/generation.md#332-geometry-aware-sampling)
- [3.3.3 Constraint Parameterization](../papers/generation.md#333-constraint-parameterization)
- [3.3.4 Guidance, Correction, and Search](../papers/generation.md#334-guidance-correction-and-search)
- [3.3.5 Combining Mechanisms](../papers/generation.md#335-combining-mechanisms)
