
#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
text = (ROOT / "data" / "references.bib").read_text(encoding="utf-8")
keys = re.findall(r"@\w+\{([^,\s]+)", text)
dupes = sorted({key for key in keys if keys.count(key) > 1})
if dupes:
    print("Duplicate BibTeX keys:")
    for key in dupes:
        print(f"- {key}")
    raise SystemExit(1)
print(f"Checked {len(keys)} BibTeX keys; no duplicates found.")
