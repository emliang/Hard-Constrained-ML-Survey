
# Contributing

This repository is a reader guide. Contributions should improve understanding, comparison, or navigation for readers of hard-constrained ML papers.

## Add or Correct a Paper

1. Provide an original paper or proceedings link, publication venue, and year.
2. Suggest the closest numbered subsection in the [paper lists](README.md#browse-papers). Use the constraint-handling mechanism described in the paper, rather than its title alone.
3. Write a few distinguishing keywords, such as `CBF action filtering` or `feasible-coordinate transport`.
4. Briefly explain the placement. A hybrid paper can appear in several sections when different mechanisms are relevant.

General model foundations should be identified as background. Low measured violations, solver convergence, and by-construction feasibility support different claims.

Edit the relevant list under `docs/papers/`. Keep the columns `# | Keywords | Paper | Venue | Year`, link the paper title, use a recognizable venue abbreviation, and preserve chronological order. Keep the paper index, timeline, BibTeX, and homepage counts in sync.

Issues are welcome when the proposed classification needs discussion. Other useful contributions include clearer comparisons, formulas, minimal implementations, and corrections to publication metadata.
