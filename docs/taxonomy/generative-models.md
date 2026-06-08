
# Hard-Constrained Generative Models

Generative methods produce samples under explicit validity, physical, structural, logical, or design constraints.

## Families

| Family | Core idea | Typical evidence |
|---|---|---|
| Push-forward generators | Transform simple latent variables into a constrained domain. | Map validity and support coverage. |
| Autoregressive and constrained decoding | Restrict token or construction choices step by step. | Decoder validity, grammar/automaton correctness, search completeness. |
| Diffusion and flow matching | Adapt stochastic or continuous generative dynamics to constrained domains. | Boundary behavior, sampler validity, discretization assumptions. |
| Inference-time guidance | Steer samples toward constraints during generation. | Violation rates, utility preservation, guidance cost. |
| Constraint-aware training or fine-tuning | Train or adapt the generator with feasibility objectives. | Empirical validity, downstream utility, and robustness tests. |
