
# Hard-Constrained ML Survey

A reader-oriented guide to machine learning methods whose predictions or generated samples must satisfy hard constraints.

The repository is organized around the questions a reader usually has when entering the area:

- What does a "hard constraint" claim actually mean?
- Which method families exist, and when are they useful?
- What assumptions make a feasibility claim valid?
- How should feasibility, utility, and cost be compared across papers?
- Which applications and benchmarks make these trade-offs visible?

## Start here

| Reader goal | Go to |
|---|---|
| Get the big picture | [`docs/start-here.md`](docs/start-here.md) |
| Understand the taxonomy | [`docs/taxonomy/overview.md`](docs/taxonomy/overview.md) |
| Choose a method family | [`docs/reader-guide/which-method-family.md`](docs/reader-guide/which-method-family.md) |
| Read a hard-constraint claim critically | [`docs/reader-guide/how-to-read-a-hard-constraint-claim.md`](docs/reader-guide/how-to-read-a-hard-constraint-claim.md) |
| Compare guarantees | [`docs/evaluation/guarantee-terminology.md`](docs/evaluation/guarantee-terminology.md) |
| Check reporting dimensions | [`docs/evaluation/reporting-dimensions.md`](docs/evaluation/reporting-dimensions.md) |
| Browse application settings | [`docs/applications/optimization.md`](docs/applications/optimization.md) |

## Core idea

Hard-constrained ML methods differ less by application name than by enforcement mechanism. A method may enforce constraints through:

- the training objective,
- post-processing, projection, or repair,
- a differentiable solver or structured layer,
- a feasibility-preserving map or parameterization,
- constrained decoding or sampling,
- inference-time guidance,
- verification or model editing.

The central question is therefore not only "does the paper say hard constraint?" but:

> What supports the feasibility claim, what useful output is preserved, what cost is paid, and under what assumptions does the claim apply?

## Reader map

The repository has four reader-facing layers.

1. **Conceptual guide** in [`docs/start-here.md`](docs/start-here.md) and [`docs/reader-guide/`](docs/reader-guide/).
2. **Taxonomy pages** in [`docs/taxonomy/`](docs/taxonomy/) for prediction, generation, and constraint families.
3. **Evaluation pages** in [`docs/evaluation/`](docs/evaluation/) for guarantees, reporting dimensions, and method selection.
4. **Application pages** in [`docs/applications/`](docs/applications/) for optimization, science, and constrained synthesis settings.

The `data/`, `tables/`, and `scripts/` folders support browsing and maintenance. The main entry point is the reader guide.

## What is included

- Reader summaries of hard-constrained prediction and generation families.
- A practical vocabulary for exact, certified, solver-tolerance, probabilistic, and empirical feasibility claims.
- Method-selection checklists and claim-reading checklists.
- Application-oriented notes for optimization, science, and constrained synthesis.
- Machine-readable method and reference metadata for readers who want to inspect the literature map.

## Citation

If this repository helps your work, please cite the companion survey and this repository. See [`CITATION.cff`](CITATION.cff).
