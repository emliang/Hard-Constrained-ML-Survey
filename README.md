
# Hard-Constrained ML Survey

Companion repository for a survey of machine-learning methods whose predictions or generated samples must satisfy hard constraints.

The repository is organized around a mechanism-first taxonomy: where and how feasibility is enforced, what kind of guarantee supports the hard-constraint claim, and what cost or scope assumptions are introduced.

## What is included

- `docs/`: reader-facing taxonomy, evaluation terminology, and application notes.
- `data/`: machine-readable method, paper, taxonomy, benchmark, and BibTeX data.
- `tables/`: CSV versions of survey comparison tables and derived method views.
- `figures/`: reusable survey figures.
- `scripts/`: lightweight validation and data-build utilities.

## Survey scope

Machine-learning models are increasingly deployed in domains where predictions and generated samples must satisfy hard constraints. When these constraints encode balance laws, design rules, physical limits, or regulatory requirements, a violating output may be unusable regardless of its prediction error or sample quality. Methods differ in where they enforce feasibility: during training, in the model architecture, by projection or repair, in the sampler, or through verification. Existing surveys address adjacent topics, including physics-informed learning, learning for optimization, decision-focused learning, and generative modeling, but do not systematically compare these enforcement choices by their guarantees, assumptions, and training or inference complexity. This survey examines hard-constraint enforcement in discriminative prediction and generative modeling through a mechanism-first taxonomy. For predictors, we cover training-time feasibility losses, output repair and projection, structured output layers, explicit feasibility mappings, and constraint parameterization. For generators, we cover pushforward and autoregressive architectures, constrained-domain samplers, constraint parameterization, inference-time guidance, and constraint-aware training or fine-tuning. Across these families, we compare supported constraint classes, guarantee types, numerical tolerances, certification scopes, output utility, and training and inference complexity. These criteria support method selection, feasibility-claim interpretation, and benchmark design in optimization, trajectory planning, scientific modeling, and constrained generation.

## Current data snapshot

- Method-index entries: 157
- Source-verified method entries: 107
- Pending source checks: 1
- Cited paper rows: 244
- Method timeline rows: 190

## Quick start

```bash
python3 scripts/validate_data.py
python3 scripts/build_method_cards.py
```

## Important evidence rule

Method classifications in this repository should be source-backed. Do not classify a method from its title, neighboring citations, or table placement alone. If the original paper has not been checked, mark the entry as `pending_source_check`.

## Citation

If you use this repository, cite the companion survey paper and this repository. See `CITATION.cff`.
