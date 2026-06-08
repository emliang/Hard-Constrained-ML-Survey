
#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "methods"


def parse_methods() -> list[dict[str, str]]:
    text = (ROOT / "data" / "methods.yaml").read_text(encoding="utf-8")
    blocks: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    for line in text.splitlines():
        if line.startswith("- cite_key:"):
            if current:
                blocks.append(current)
            current = {"cite_key": line.split(":", 1)[1].strip().strip('"')}
        elif current and line.startswith("  ") and ":" in line:
            key, value = line.strip().split(":", 1)
            current[key] = value.strip().strip('"')
    if current:
        blocks.append(current)
    return blocks


def clean_filename(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.+-]+", "_", value)


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    for method in parse_methods():
        cite_key = method["cite_key"]
        lines = [f"# `{cite_key}`", ""]
        for key in [
            "source_status",
            "source_pdf_file",
            "method_family_primary",
            "learning_task",
            "model_paradigm",
            "constraint_form",
            "constraint_geometry",
            "mechanism_label",
            "mechanism_summary",
            "guarantee_target",
            "guarantee_basis",
            "inference_dependency",
            "main_tradeoff",
            "evidence_note",
        ]:
            if method.get(key):
                lines.append(f"**{key.replace('_', ' ').title()}**: {method[key]}")
                lines.append("")
        (OUT / f"{clean_filename(cite_key)}.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote method cards to {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
