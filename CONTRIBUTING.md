
# Contributing

Contributions are welcome when they preserve the repository's evidence standard.

## Paper and method additions

1. Add or update the BibTeX entry in `data/references.bib`.
2. Add the method metadata in `data/methods.yaml`.
3. Use the original paper text or at least the abstract and first pages before assigning a method family.
4. If source evidence has not been checked, set `source_status: "pending_source_check"`.
5. State the constraint form, enforcement mechanism, guarantee basis, inference dependency, and main trade-off as separate fields.
6. Run `python3 scripts/validate_data.py`.

## What not to add

- Do not upload paper PDFs unless licensing explicitly allows it.
- Do not infer method labels from titles alone.
- Do not collapse solver-tolerance, certified, probabilistic, and empirical feasibility into a single "guaranteed" label.
