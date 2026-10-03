
# Hard-Constrained Generative Models

Generative methods produce samples under explicit validity, physical, structural, logical, or design constraints.

## Families

| Family | Core idea | Typical evidence |
|---|---|---|
| Direct generation | Produce a complete candidate using a sample map, with a feasible representation or output-side enforcement. | Map validity, correction accuracy, and coverage. |
| Autoregressive generation | Construct successive elements using prefix, grammar, completion, or search information. | Completed-output validity and fidelity to the intended constrained distribution. |
| Diffusion and flow-based generation | Evolve sampler states using geometry, parameterization, correction, guidance, or bridge/control interventions. | The property established for the completed sample, including numerical and decoding effects. |

Training, fine-tuning, and mechanism combinations apply across these generation procedures. Guidance changes sampling preferences; it does not establish feasibility without further evidence or an enforcement operation. General one-step generators are background examples of sample maps.

Compare validity together with quality, diversity, coverage, and total cost per valid sample. See [the numbered paper tables](../papers/generation.md).
