
#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ALLOWED_SOURCE_STATUS = {
    "verified_from_source",
    "source_checked_needs_detail",
    "pending_source_check",
}


def bib_keys() -> set[str]:
    text = (ROOT / "data" / "references.bib").read_text(encoding="utf-8")
    return set(re.findall(r"@\w+\{([^,\s]+)", text))


def method_blocks() -> list[dict[str, str]]:
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


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    keys = bib_keys()
    methods = method_blocks()
    if not methods:
        errors.append("No methods found in data/methods.yaml")
    for method in methods:
        cite_key = method.get("cite_key", "")
        if cite_key not in keys:
            warnings.append(f"{cite_key}: missing from data/references.bib")
        status = method.get("source_status")
        if status and status not in ALLOWED_SOURCE_STATUS:
            errors.append(f"{cite_key}: invalid source_status {status!r}")
        for required in ["method_family_primary", "mechanism_label", "guarantee_basis"]:
            if method.get("source_status") == "verified_from_source" and not method.get(required):
                errors.append(f"{cite_key}: verified entry missing {required}")
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    if warnings:
        print("Validation warnings:")
        for warning in warnings:
            print(f"- {warning}")
    print(f"Validated {len(methods)} method entries against {len(keys)} BibTeX keys.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
